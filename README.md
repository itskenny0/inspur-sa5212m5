# Inspur SA5212M5
## What is it?
The Inspur SA5212M5 is an Alibaba-custom made series of servers with LGA3647 sockets and 24 DIMM slots.
The BIOS is pretty heavily locked down on Inspur units.

The same server design seems to have been submitted to multiple server vendors, known to me being Inspur and Inventec.
I've yet to find a method of manually controlling the fans on the Inventec servers.

## fanctl.py
fanctl.py is a script I had Claude throw up that will keep the fans in check via HTTP over the webinterface.
Unfortunately I could not find another interface the BMC would expose that allows me to control the fans 'manually' (as in, implement my own fan curve).
ipmitool failed me at every step, but it is possible to inject different steps into the HTTP request for 'manual fan control' in the BMC (20/50/75/100).
Catching the PUT request that is sent when clicking that button shows that it is really being transmitted as a json object: {'duty': 20}, which takes any number from 0 to 100.
On my units, most fans won't start up correctly before I exceed 10%. However, the noise reduction going from 20% to 15% is already quite strong.

If you have MQTT, this script can also expose the controls and sensors to Home Assistant.
