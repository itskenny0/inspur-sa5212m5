#!/usr/bin/env python3
"""
Automatic fan control script for IPMI-based server BMC.
Controls fan speed based on temperature readings.
"""

import requests
import time
import argparse
import logging
import json
from datetime import datetime
from typing import Dict, List, Optional

try:
    import paho.mqtt.client as mqtt
    MQTT_AVAILABLE = True
except ImportError:
    MQTT_AVAILABLE = False


class BMCFanController:
    """Controls server fans via BMC REST API."""

    def __init__(self, host: str, username: str, password: str,
                 emergency_temp: float = 90.0, emergency_duration: int = 300,
                 night_start: str = "01:30", night_end: str = "07:00",
                 mqtt_broker: Optional[str] = None, mqtt_port: int = 1883,
                 mqtt_user: Optional[str] = None, mqtt_password: Optional[str] = None,
                 ha_discovery_prefix: str = "homeassistant"):
        self.host = host
        self.username = username
        self.password = password
        self.base_url = f"http://{host}/api"
        self.session = requests.Session()
        self.csrf_token = None

        # MQTT configuration
        self.mqtt_enabled = mqtt_broker is not None and MQTT_AVAILABLE
        self.mqtt_broker = mqtt_broker
        self.mqtt_port = mqtt_port
        self.mqtt_user = mqtt_user
        self.mqtt_password = mqtt_password
        self.ha_discovery_prefix = ha_discovery_prefix
        self.mqtt_client = None
        self.device_id = f"server_fanctl_{host.replace('.', '_')}"
        self.manual_mode = False  # Manual override mode
        self.manual_speed = None  # Manual fan speed override

        # Temperature to fan speed curve - daytime (temp_celsius: duty_percent)
        self.fan_curve_day = {
            0: 12,    # Below 40°C: 12% (minimum)
            40: 12,   # 40°C: 12%
            50: 14,   # 50°C: 14%
            60: 17,   # 60°C: 17%
            70: 21,   # 70°C: 21%
            75: 24,   # 75°C: 24%
            80: 27,   # 80°C: 27%
            85: 30,   # 85°C+: 30% (maximum)
        }

        # Temperature to fan speed curve - nighttime (1:30 AM - 7:00 AM)
        # Allows higher fan speeds for better cooling during quiet hours
        self.fan_curve_night = {
            0: 12,    # Below 40°C: 12% (minimum)
            40: 12,   # 40°C: 12%
            50: 18,   # 50°C: 18%
            60: 25,   # 60°C: 25%
            70: 33,   # 70°C: 33%
            75: 39,   # 75°C: 39%
            80: 45,   # 80°C: 45%
            85: 50,   # 85°C+: 50% (maximum)
        }

        # Parse nighttime hours
        night_start_parts = night_start.split(':')
        self.night_start_hour = int(night_start_parts[0])
        self.night_start_minute = int(night_start_parts[1])

        night_end_parts = night_end.split(':')
        self.night_end_hour = int(night_end_parts[0])
        self.night_end_minute = int(night_end_parts[1])

        # Which temperature sensors to monitor (highest temp wins)
        self.monitored_sensors = [
            "CPU0_Temp",
            "CPU1_Temp",
            "DIMMG0_Temp",
            "DIMMG1_Temp",
        ]

        self.num_fans = 8  # Fan zones 0-7

        # Emergency thermal protection
        self.emergency_temp_threshold = emergency_temp
        self.emergency_duration = emergency_duration
        self.high_temp_start_time = None  # Track when high temp started
        self.emergency_mode = False  # Emergency mode flag

    def login(self) -> bool:
        """Authenticate with the BMC and get CSRF token."""
        try:
            response = self.session.post(
                f"{self.base_url}/session",
                data=f"username={self.username}&password={self.password}",
                headers={"Content-Type": "application/x-www-form-urlencoded"},
                timeout=10
            )
            response.raise_for_status()
            data = response.json()

            self.csrf_token = data.get("CSRFToken")
            if not self.csrf_token:
                logging.error("Failed to get CSRF token from login response")
                return False

            logging.info(f"Successfully logged in to BMC at {self.host}")
            return True

        except Exception as e:
            logging.error(f"Login failed: {e}")
            return False

    def get_sensors(self) -> Optional[List[Dict]]:
        """Retrieve all sensor readings from the BMC."""
        try:
            response = self.session.get(
                f"{self.base_url}/sensors",
                headers={"X-CSRFTOKEN": self.csrf_token},
                timeout=10
            )
            response.raise_for_status()
            return response.json()

        except Exception as e:
            logging.error(f"Failed to get sensors: {e}")
            return None

    def get_max_temp(self, sensors: List[Dict]) -> float:
        """Get the highest temperature from monitored sensors."""
        max_temp = 0.0

        for sensor in sensors:
            if sensor.get("type") == "temperature" and sensor.get("name") in self.monitored_sensors:
                temp = sensor.get("reading", 0.0)
                if temp > max_temp:
                    max_temp = temp
                    logging.debug(f"Sensor {sensor['name']}: {temp}°C")

        return max_temp

    def get_total_power(self, sensors: List[Dict]) -> float:
        """Get the total system power consumption in watts."""
        for sensor in sensors:
            if sensor.get("name") == "Total_Power":
                return sensor.get("reading", 0.0)
        return 0.0

    def is_nighttime(self) -> bool:
        """Check if current time is within nighttime hours (1:30 AM - 7:00 AM)."""
        now = datetime.now()
        current_minutes = now.hour * 60 + now.minute

        # Convert nighttime window to minutes since midnight
        night_start_minutes = self.night_start_hour * 60 + self.night_start_minute
        night_end_minutes = self.night_end_hour * 60 + self.night_end_minute

        return night_start_minutes <= current_minutes < night_end_minutes

    def calculate_fan_speed(self, temp: float) -> int:
        """Calculate fan duty cycle based on temperature using the fan curve."""
        # Select appropriate fan curve based on time of day
        fan_curve = self.fan_curve_night if self.is_nighttime() else self.fan_curve_day

        # Find the two points on the curve to interpolate between
        temps = sorted(fan_curve.keys())

        if temp <= temps[0]:
            return fan_curve[temps[0]]
        if temp >= temps[-1]:
            return fan_curve[temps[-1]]

        # Linear interpolation between two points
        for i in range(len(temps) - 1):
            if temps[i] <= temp <= temps[i + 1]:
                t1, t2 = temps[i], temps[i + 1]
                s1, s2 = fan_curve[t1], fan_curve[t2]

                # Linear interpolation
                ratio = (temp - t1) / (t2 - t1)
                speed = int(s1 + ratio * (s2 - s1))
                return speed

        return 50  # Fallback to 50%

    def set_fan_speed(self, fan_id: int, duty: int) -> bool:
        """Set the duty cycle for a specific fan (0-100%)."""
        try:
            response = self.session.put(
                f"{self.base_url}/settings/fan/{fan_id}",
                json={"duty": duty},
                headers={
                    "Content-Type": "application/json",
                    "X-CSRFTOKEN": self.csrf_token
                },
                timeout=10
            )
            response.raise_for_status()
            return True

        except Exception as e:
            logging.error(f"Failed to set fan {fan_id} speed: {e}")
            return False

    def set_all_fans(self, duty: int) -> bool:
        """Set all fans to the same duty cycle."""
        success = True
        for fan_id in range(self.num_fans):
            if not self.set_fan_speed(fan_id, duty):
                success = False
        return success

    def mqtt_on_connect(self, client, userdata, flags, rc):
        """MQTT connection callback."""
        if rc == 0:
            logging.info("Connected to MQTT broker")
            # Subscribe to command topics
            client.subscribe(f"{self.device_id}/set_speed/set")
            client.subscribe(f"{self.device_id}/mode/set")
            # Publish Home Assistant discovery with current sensor list
            sensors = self.get_sensors()
            self.publish_ha_discovery(sensors)
        else:
            logging.error(f"Failed to connect to MQTT broker: {rc}")

    def mqtt_on_message(self, client, userdata, msg):
        """Handle incoming MQTT messages."""
        try:
            topic = msg.topic
            payload = msg.payload.decode()

            if topic == f"{self.device_id}/set_speed/set":
                # Manual fan speed control
                speed = int(payload)
                if 0 <= speed <= 100:
                    self.manual_speed = speed
                    self.manual_mode = True
                    logging.info(f"MQTT: Manual mode enabled, fan speed set to {speed}%")
                    self.set_all_fans(speed)

            elif topic == f"{self.device_id}/mode/set":
                # Mode control (auto/manual)
                if payload.lower() == "auto":
                    self.manual_mode = False
                    self.manual_speed = None
                    logging.info("MQTT: Auto mode enabled")
                elif payload.lower() == "manual":
                    self.manual_mode = True
                    logging.info("MQTT: Manual mode enabled")

        except Exception as e:
            logging.error(f"Error handling MQTT message: {e}")

    def connect_mqtt(self) -> bool:
        """Connect to MQTT broker."""
        if not self.mqtt_enabled:
            return False

        try:
            self.mqtt_client = mqtt.Client(client_id=self.device_id)
            self.mqtt_client.on_connect = self.mqtt_on_connect
            self.mqtt_client.on_message = self.mqtt_on_message

            if self.mqtt_user and self.mqtt_password:
                self.mqtt_client.username_pw_set(self.mqtt_user, self.mqtt_password)

            self.mqtt_client.connect(self.mqtt_broker, self.mqtt_port, 60)
            self.mqtt_client.loop_start()
            logging.info(f"Connecting to MQTT broker at {self.mqtt_broker}:{self.mqtt_port}")
            return True

        except Exception as e:
            logging.error(f"Failed to connect to MQTT broker: {e}")
            self.mqtt_enabled = False
            return False

    def publish_ha_discovery(self, sensors: Optional[List[Dict]] = None):
        """Publish Home Assistant MQTT discovery messages."""
        if not self.mqtt_enabled or not self.mqtt_client:
            return

        device_info = {
            "identifiers": [self.device_id],
            "name": f"Server Fan Controller ({self.host})",
            "manufacturer": "Custom",
            "model": "IPMI Fan Controller",
            "sw_version": "1.0"
        }

        # Max temperature sensor (for backward compatibility)
        temp_config = {
            "name": "Server Temperature (Max)",
            "unique_id": f"{self.device_id}_temperature",
            "state_topic": f"{self.device_id}/state",
            "value_template": "{{ value_json.temperature }}",
            "unit_of_measurement": "°C",
            "device_class": "temperature",
            "device": device_info
        }
        self.mqtt_client.publish(
            f"{self.ha_discovery_prefix}/sensor/{self.device_id}_temperature/config",
            json.dumps(temp_config), retain=True
        )

        # Dynamically create discovery for all available sensors
        if sensors:
            for sensor in sensors:
                sensor_name = sensor.get("name", "")
                sensor_type = sensor.get("type", "")
                reading = sensor.get("reading", 0.0)

                # Only publish sensors that are active (non-zero or temperature type)
                if sensor_type == "temperature":
                    sensor_id = sensor_name.lower()
                    friendly_name = sensor_name.replace("_", " ").title()
                    sensor_config = {
                        "name": f"Server {friendly_name}",
                        "unique_id": f"{self.device_id}_{sensor_id}",
                        "state_topic": f"{self.device_id}/sensors",
                        "value_template": f"{{{{ value_json.{sensor_id} }}}}",
                        "unit_of_measurement": "°C",
                        "device_class": "temperature",
                        "device": device_info
                    }
                    self.mqtt_client.publish(
                        f"{self.ha_discovery_prefix}/sensor/{self.device_id}_{sensor_id}/config",
                        json.dumps(sensor_config), retain=True
                    )

                elif sensor_type == "fan" and "RPM" in sensor_name:
                    sensor_id = sensor_name.lower()
                    friendly_name = sensor_name.replace("_", " ").upper()
                    sensor_config = {
                        "name": f"Server {friendly_name}",
                        "unique_id": f"{self.device_id}_{sensor_id}",
                        "state_topic": f"{self.device_id}/sensors",
                        "value_template": f"{{{{ value_json.{sensor_id} }}}}",
                        "unit_of_measurement": "RPM",
                        "icon": "mdi:fan",
                        "device": device_info
                    }
                    self.mqtt_client.publish(
                        f"{self.ha_discovery_prefix}/sensor/{self.device_id}_{sensor_id}/config",
                        json.dumps(sensor_config), retain=True
                    )

        # Power sensor
        power_config = {
            "name": "Server Power",
            "unique_id": f"{self.device_id}_power",
            "state_topic": f"{self.device_id}/state",
            "value_template": "{{ value_json.power }}",
            "unit_of_measurement": "W",
            "device_class": "power",
            "device": device_info
        }
        self.mqtt_client.publish(
            f"{self.ha_discovery_prefix}/sensor/{self.device_id}_power/config",
            json.dumps(power_config), retain=True
        )

        # Fan duty cycle sensor
        fan_speed_config = {
            "name": "Server Fan Duty Cycle",
            "unique_id": f"{self.device_id}_fan_speed",
            "state_topic": f"{self.device_id}/state",
            "value_template": "{{ value_json.fan_speed }}",
            "unit_of_measurement": "%",
            "icon": "mdi:fan",
            "device": device_info
        }
        self.mqtt_client.publish(
            f"{self.ha_discovery_prefix}/sensor/{self.device_id}_fan_speed/config",
            json.dumps(fan_speed_config), retain=True
        )

        # Mode sensor
        mode_config = {
            "name": "Server Fan Mode",
            "unique_id": f"{self.device_id}_mode",
            "state_topic": f"{self.device_id}/state",
            "value_template": "{{ value_json.mode }}",
            "icon": "mdi:cog",
            "device": device_info
        }
        self.mqtt_client.publish(
            f"{self.ha_discovery_prefix}/sensor/{self.device_id}_mode/config",
            json.dumps(mode_config), retain=True
        )

        # Fan speed control (number entity)
        fan_control_config = {
            "name": "Server Fan Speed Control",
            "unique_id": f"{self.device_id}_set_speed",
            "command_topic": f"{self.device_id}/set_speed/set",
            "state_topic": f"{self.device_id}/state",
            "value_template": "{{ value_json.fan_speed }}",
            "min": 0,
            "max": 100,
            "step": 1,
            "unit_of_measurement": "%",
            "icon": "mdi:fan",
            "device": device_info
        }
        self.mqtt_client.publish(
            f"{self.ha_discovery_prefix}/number/{self.device_id}_set_speed/config",
            json.dumps(fan_control_config), retain=True
        )

        # Mode control (select entity)
        mode_control_config = {
            "name": "Server Fan Mode Control",
            "unique_id": f"{self.device_id}_mode_control",
            "command_topic": f"{self.device_id}/mode/set",
            "state_topic": f"{self.device_id}/state",
            "value_template": "{{ value_json.mode }}",
            "options": ["auto", "manual"],
            "icon": "mdi:cog",
            "device": device_info
        }
        self.mqtt_client.publish(
            f"{self.ha_discovery_prefix}/select/{self.device_id}_mode_control/config",
            json.dumps(mode_control_config), retain=True
        )

        logging.info("Published Home Assistant discovery messages")

    def publish_mqtt_state(self, temperature: float, power: float, fan_speed: int, sensors: Optional[List[Dict]] = None):
        """Publish current state to MQTT."""
        if not self.mqtt_enabled or not self.mqtt_client:
            return

        mode = "manual" if self.manual_mode else "auto"
        state = {
            "temperature": round(temperature, 1),
            "power": round(power, 0),
            "fan_speed": fan_speed,
            "mode": mode
        }

        self.mqtt_client.publish(f"{self.device_id}/state", json.dumps(state), retain=True)

        # Publish individual sensor data
        if sensors:
            sensor_data = {}

            # Extract temperature sensors
            for sensor in sensors:
                sensor_name = sensor.get("name", "")
                sensor_type = sensor.get("type", "")
                reading = sensor.get("reading", 0.0)

                if sensor_type == "temperature":
                    # Map sensor names to lowercase IDs
                    sensor_id = sensor_name.lower()
                    sensor_data[sensor_id] = round(reading, 1)

                elif sensor_type == "fan" and "RPM" in sensor_name:
                    # Extract fan RPM sensors (FAN1_RPM through FAN8_RPM)
                    sensor_id = sensor_name.lower()
                    sensor_data[sensor_id] = round(reading, 0)

            if sensor_data:
                self.mqtt_client.publish(f"{self.device_id}/sensors", json.dumps(sensor_data), retain=True)

    def run_control_loop(self, interval: float = 1.5, max_ramp_rate: float = 1.0/3.0):
        """Main control loop - monitors temps and adjusts fans.

        Args:
            interval: Update interval in seconds
            max_ramp_rate: Maximum fan speed increase rate in percent per second (default: 1% per 3 seconds)
        """
        logging.info(f"Starting fan control loop (interval: {interval}s)")
        logging.info(f"Monitoring sensors: {', '.join(self.monitored_sensors)}")
        logging.info(f"Emergency thermal protection: >={self.emergency_temp_threshold}°C for {self.emergency_duration}s → 100% fans")
        logging.info(f"Fan ramp rate: max {max_ramp_rate * interval:.2f}% per {interval}s")

        current_duty = None  # Track actual current duty cycle
        last_duty = None  # Track last logged duty

        try:
            while True:
                # Get sensor readings
                sensors = self.get_sensors()
                if not sensors:
                    logging.warning("Failed to get sensor data, retrying...")
                    time.sleep(interval)
                    continue

                # Get maximum temperature and power
                max_temp = self.get_max_temp(sensors)
                total_power = self.get_total_power(sensors)
                current_time = time.time()

                # Emergency thermal protection logic
                if max_temp >= self.emergency_temp_threshold:
                    # Temperature is dangerously high
                    if self.high_temp_start_time is None:
                        # Just crossed the threshold
                        self.high_temp_start_time = current_time
                        logging.warning(f"Temperature {max_temp:.1f}°C exceeded emergency threshold! Monitoring for {self.emergency_duration}s...")
                    else:
                        # Check how long we've been above threshold
                        high_temp_duration = current_time - self.high_temp_start_time

                        if high_temp_duration >= self.emergency_duration and not self.emergency_mode:
                            # Activate emergency mode - max out fans
                            self.emergency_mode = True
                            logging.critical(f"EMERGENCY MODE ACTIVATED! Temperature {max_temp:.1f}°C for {high_temp_duration:.0f}s - Setting fans to 100%!")
                            self.set_all_fans(100)
                            last_duty = 100
                            time.sleep(interval)
                            continue
                        elif self.emergency_mode:
                            # Stay in emergency mode
                            target_duty = 100
                            if target_duty != last_duty:
                                logging.warning(f"Emergency mode active - Temperature: {max_temp:.1f}°C → Fans at 100%")
                                self.set_all_fans(100)
                                last_duty = 100
                            time.sleep(interval)
                            continue
                        else:
                            # Still monitoring
                            remaining = self.emergency_duration - high_temp_duration
                            logging.warning(f"Temperature {max_temp:.1f}°C still high - Emergency mode in {remaining:.0f}s")
                else:
                    # Temperature is below threshold
                    if self.emergency_mode:
                        logging.info(f"Temperature dropped to {max_temp:.1f}°C - Exiting emergency mode")
                        self.emergency_mode = False

                    if self.high_temp_start_time is not None:
                        logging.info(f"Temperature dropped below {self.emergency_temp_threshold}°C - Resetting emergency timer")

                    self.high_temp_start_time = None

                # Check for manual mode override
                if self.manual_mode and self.manual_speed is not None:
                    # In manual mode, use the manual speed setting
                    current_duty = self.manual_speed
                    if current_duty != last_duty:
                        logging.info(f"Manual mode: Setting fans to {current_duty}%")
                        self.set_all_fans(current_duty)
                        last_duty = current_duty
                else:
                    # Calculate required fan speed (normal mode)
                    target_duty = self.calculate_fan_speed(max_temp)

                    # Initialize current_duty on first run
                    if current_duty is None:
                        current_duty = target_duty

                    # Apply smoothing for ramp up (gradual increase)
                    if target_duty > current_duty:
                        max_increase = max_ramp_rate * interval
                        current_duty = min(target_duty, current_duty + max_increase)
                    else:
                        # Allow immediate decrease (no smoothing on ramp down)
                        current_duty = target_duty

                    # Round to integer
                    current_duty = int(round(current_duty))

                    # Only update fans if speed changed
                    if current_duty != last_duty:
                        mode = "(night)" if self.is_nighttime() else "(day)"
                        if target_duty != current_duty:
                            logging.info(f"Temperature: {max_temp:.1f}°C | Power: {total_power:.0f}W → Ramping to {target_duty}%, currently {current_duty}% {mode}")
                        else:
                            logging.info(f"Temperature: {max_temp:.1f}°C | Power: {total_power:.0f}W → Setting fans to {current_duty}% {mode}")
                        self.set_all_fans(current_duty)
                        last_duty = current_duty
                    else:
                        logging.debug(f"Temperature: {max_temp:.1f}°C | Power: {total_power:.0f}W → Fan speed unchanged ({current_duty}%)")

                # Publish state to MQTT
                self.publish_mqtt_state(max_temp, total_power, current_duty if current_duty is not None else 0, sensors)

                time.sleep(interval)

        except KeyboardInterrupt:
            logging.info("Fan control stopped by user")
        except Exception as e:
            logging.error(f"Control loop error: {e}")
            raise


def main():
    parser = argparse.ArgumentParser(description="Automatic BMC fan controller")
    parser.add_argument("--host", default="192.168.0.2", help="BMC IP address")
    parser.add_argument("--user", default="admin", help="BMC username")
    parser.add_argument("--password", default="admin", help="BMC password")
    parser.add_argument("--interval", type=float, default=1.5, help="Update interval in seconds (default: 1.5)")
    parser.add_argument("--ramp-rate", type=float, default=1.0/3.0, help="Max fan speed increase rate in %%/sec (default: 0.33, i.e. 1%% per 3 seconds)")
    parser.add_argument("--emergency-temp", type=float, default=90.0, help="Temperature threshold for emergency mode (default: 90°C)")
    parser.add_argument("--emergency-duration", type=int, default=300, help="Time in seconds at high temp before emergency mode (default: 300)")
    parser.add_argument("--night-start", default="01:30", help="Nighttime start (HH:MM format, default: 01:30)")
    parser.add_argument("--night-end", default="07:00", help="Nighttime end (HH:MM format, default: 07:00)")
    parser.add_argument("--enable-mqtt", action="store_true", help="Enable MQTT/Home Assistant integration")
    parser.add_argument("--mqtt-broker", help="MQTT broker address for Home Assistant integration")
    parser.add_argument("--mqtt-port", type=int, default=1883, help="MQTT broker port (default: 1883)")
    parser.add_argument("--mqtt-user", help="MQTT username")
    parser.add_argument("--mqtt-password", help="MQTT password")
    parser.add_argument("--ha-discovery-prefix", default="homeassistant", help="Home Assistant MQTT discovery prefix (default: homeassistant)")
    parser.add_argument("--set-speed", type=int, metavar="DUTY", help="Set fans to specific duty cycle (0-100) and exit")
    parser.add_argument("--verbose", "-v", action="store_true", help="Enable verbose logging")

    args = parser.parse_args()

    # Setup logging
    log_level = logging.DEBUG if args.verbose else logging.INFO
    logging.basicConfig(
        level=log_level,
        format="%(asctime)s [%(levelname)s] %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )

    # Create controller
    controller = BMCFanController(
        args.host, args.user, args.password,
        emergency_temp=args.emergency_temp,
        emergency_duration=args.emergency_duration,
        night_start=args.night_start,
        night_end=args.night_end,
        mqtt_broker=args.mqtt_broker if args.enable_mqtt else None,
        mqtt_port=args.mqtt_port,
        mqtt_user=args.mqtt_user,
        mqtt_password=args.mqtt_password,
        ha_discovery_prefix=args.ha_discovery_prefix
    )

    # Login
    if not controller.login():
        logging.error("Failed to login to BMC")
        return 1

    # Connect to MQTT if configured
    if controller.mqtt_enabled:
        if not MQTT_AVAILABLE:
            logging.warning("MQTT requested but paho-mqtt library not installed. Run: pip install paho-mqtt")
        else:
            controller.connect_mqtt()
            time.sleep(1)  # Give MQTT time to connect

    # Manual fan speed mode
    if args.set_speed is not None:
        duty = max(0, min(100, args.set_speed))
        logging.info(f"Setting all fans to {duty}%")
        if controller.set_all_fans(duty):
            logging.info("Successfully set fan speed")
            return 0
        else:
            logging.error("Failed to set fan speed")
            return 1

    # Automatic control mode
    controller.run_control_loop(args.interval, args.ramp_rate)
    return 0


if __name__ == "__main__":
    exit(main())