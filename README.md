# Inspur SA5212M5
## What is it?
The Inspur SA5212M5 is an Alibaba-custom made series of servers with LGA3647 sockets and 24 DIMM slots.
The BIOS is pretty heavily locked down on Inspur units.

The same server design seems to have been submitted to multiple server vendors, known to me being Inspur and Inventec.
I've yet to find a method of manually controlling the fans on the Inventec servers.

## fanctl.py
fanctl.py is a shot script I had Claude throw up that will keep the fans in check via HTTP over the webinterface.
Unfortunately I could not find an interface the BMC would expose that allows me to control the fans 'manually' (as in, implement my own fan curve).

If you have MQTT, this script can also expose the controls and sensors to Home Assistant.
