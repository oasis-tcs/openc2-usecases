# Test Configurations for IoT
Duncan needs to put more stuff here.

Table of Contents:
- TL;DR
- Hardware
  * Raspberry Pi Zero
  * Raspberry Pi 3
  * Raspberry Pi 4
- Software
  * Blinky MicroSD
  * Blinky-SBoM MicroSD
  * Blinky-SBoM-Phoenix MicroSD
  * Blinky-SBoM-OpenC2 MicroSD
  * Sensor with SPA microSD
  * Actuator with SPA MicroSD
  * Pi-Hole with OpenC2 MicroSD
  * OpenC2-enabled pfSense MicroSD
  * OpenC2-enabled SNORT IDS MicroSD
- Test scenarios
  * blinky/sensor/actuator Comply2Connect "get SBoM"
  * Sensor "change settings"
  * Actuator "change settings"
  * Pi-Hole "blackhole a subdomain"
  * pfSense "add firewall rule"
  * Snort "increase logging"


## TL;DR
TL;DR - indeterminate number of Raspberry Pi's of various flavors (zero, 3, 4) with larger number of microSD cards preprogramed for various tests shown below

## Hardware
Duncan needs to put more stuff here on what he's bringing
### Raspberry Pi Zero
blah blah ref material + how many bringing + how expect to network
### Raspberry Pi 3
blah blah ref material + how many bringing + how expect to network
### Raspberry Pi 4
blah blah ref material + how many bringing + how expect to network
### Peripheral stuff
Figure outwhat to bring for demo so can see affect

## Software

### Blinky MicroSD
Only for A/B testing and first step to Blinky-SBoM-OC2.
Blinky is the "Hello World" of Nerves IoT - it just blinks the LED on the Raspberry Pi.
Nerves (https://nerves-project.org/) is for crafting and deploying bulletproof embedded software in Elixir or Erlang.

### Blinky-SBoM MicroSD
Blinky with SBoM software included as part of creating Blinky so you have the SBoM for Blinky. Similar to Blinky it is only or A/B testing and is step 2 in getting to Blinky-SBoM-OC2. It uses the sbom package on Hex (https://github.com/voltone/sbom).

### Blinky-SBoM-Phoenix MicroSD
...

### Blinky-SBoM-OpenC2 MicroSD
...

### Sensor with SPA microSD
blinky but with a psuedo-sensor (switch? thermometer? accelerometer?).
...

### Actuator with SPA MicroSD
blinky but with a psuedo-actuator (e.g. a valve, or something that rotates for a good demo).
...

### Pi-Hole with OpenC2 MicroSD
This may not be done by plugfest.

Pi-Hole (https://pi-hole.net/) is Raspberry Pi programmed as ad-blocking DNS sinkhole

### OpenC2-enabled pfSense MicroSD
This may not be done by plugfest, or may use OpenSense instead (and still may not be done).

pfSense (https://www.pfsense.org/) is most popular opensource firewall.

### OpenC2-enabled SNORT IDS MicroSD
This may not be done by plugfest.

See https://projects-raspberry.com/raspberry-pi-firewall-and-intrusion-detection-system/

## Test scenarios
duncan needs to fill in

### blinky/sensor/actuator Comply2Connect "get SBoM"

### Sensor "change settings"

### Actuator "change settings"

### Pi-Hole "blackhole a subdomain"

### pfSense "add firewall rule"

### Snort "increase logging"
