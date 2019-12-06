# Test Configurations for IoT
Duncan needs to put more stuff here.

Table of Contents:
- [1. TL;DR](#1-tldr)
- [2. Hardware](#2-hardware)
  * 2.1 Raspberry Pi Zero
  * 2.2 Raspberry Pi 3
  * 2.3 Raspberry Pi 4
  ...
- [3. Software](#3-software)
  * 3.1 Blinky MicroSD
  * 3.2 Blinky-SBoM MicroSD
  * 3.3 Blinky-SBoM-Phoenix MicroSD
  * 3.4 Blinky-SBoM-OpenC2 MicroSD
  * 3.5 Sensor with SPA microSD
  * 3.6 Actuator with SPA MicroSD
  * 3.7 Pi-Hole with OpenC2 MicroSD
  * 3.8 OpenC2-enabled pfSense MicroSD
  * 3.9 OpenC2-enabled SNORT IDS MicroSD
  * 3.10 IoTivity microSD
  * 3.11 IoTivity-SBoM microSD
  * 3.12 IoTivity-SBoM-OpenC2 microSD
  ...
- [4. Test Scenarios](#4-test-scenarios)
  * 4.1 blinky/sensor/actuator Comply2Connect "get SBoM"
  * 4.2 Sensor "change settings"
  * 4.3 Actuator "change settings"
  * 4.4 Pi-Hole "blackhole a subdomain"
  * 4.5 pfSense "add firewall rule"
  * 4.6 Snort "increase logging"
  * 4.7 IoTivity
  ...


## 1. TL;DR
TL;DR - indeterminate number of Raspberry Pi's of various flavors (zero, 3, 4) with larger number of microSD cards preprogramed for various tests shown below

## 2. Hardware
Duncan needs to put more stuff here on what he's bringing
### 2.1 Raspberry Pi Zero
blah blah ref material + how many bringing + how expect to network
### 2.2 Raspberry Pi 3
blah blah ref material + how many bringing + how expect to network
### 2.3 Raspberry Pi 4
blah blah ref material + how many bringing + how expect to network
### Peripheral stuff
Figure outwhat to bring for demo so can see affect

## 3. Software

### 3.1 Blinky MicroSD
Only for A/B testing and first step to Blinky-SBoM-OC2.
Blinky is the "Hello World" of Nerves IoT - it just blinks the LED on the Raspberry Pi.
Nerves (https://nerves-project.org/) is for crafting and deploying bulletproof embedded software in Elixir or Erlang.

### 3.2 Blinky-SBoM MicroSD
Blinky with SBoM software included as part of creating Blinky so you have the SBoM for Blinky. Similar to Blinky it is only for A/B testing and is step 2 in getting to Blinky-SBoM-OC2. It uses the sbom package on Hex (https://github.com/voltone/sbom).

### 3.3 Blinky-SBoM-Phoenix MicroSD
Blinky with SBoM and Phoenix software included. Phoenix is a webserver which will be used for OpenC2 API. Similar to Blinky, Blinky-SBoM, this is only for A/B testing and is step 3 in getting to Blinky-SBoM-OC2. For more on Phoenix see https://www.phoenixframework.org.


### 3.4 Blinky-SBoM-OpenC2 MicroSD
This builds on 3.3 Blinky-SBoM-Phoenix to include a HTTPS OpenC2 transport connection carrying OpenC2 commands to this custom Actuator. The OpenC2 actuator profiles are:
- Https Api Helloworld Actuator (HAHA) is a very simple actuator that is conformant with the OpenC2 Language Specification but does no actual security functions. It has a Custom Actuator Profile (CAP) and will respond to the query openc2 command with it's profile and schema. It also responds to a custom query extension "query Hello World" with "Hello World" - but that is all it does.
- SBoM is the (currently custom, but hopefully will be standardized) Actuator Profile to respond to the QUERY SBoM command with a Software Bill of Materials (SBoM) for the entire actuator.

### 3.5 Sensor with SPA microSD
blinky but with a psuedo-sensor (switch? thermometer? accelerometer?).
...

### 3.6 Actuator with SPA MicroSD
blinky but with a psuedo-actuator (e.g. a valve, or something that rotates for a good demo).
...

### 3.7 Pi-Hole with OpenC2 MicroSD
This may not be done by plugfest.

Pi-Hole (https://pi-hole.net/) is Raspberry Pi programmed as ad-blocking DNS sinkhole

### 3.8 OpenC2-enabled pfSense MicroSD
This may not be done by plugfest, or may use OpenSense instead (and still may not be done).

pfSense (https://www.pfsense.org/) is most popular opensource firewall.

### 3.9 OpenC2-enabled SNORT IDS MicroSD
This may not be done by plugfest.

See https://projects-raspberry.com/raspberry-pi-firewall-and-intrusion-detection-system/

### 3.10 IoTivity microSD
IoTivity is the OCF opensource. See https://iotivity.org/getting-started. This is just vanilla IoTivity that is first step for a more useful device in a couple of specifications

### 3.11 IoTivity-SBoM microSD
This may not be done by plugfest.
IoTivity with SBoM software included as part of creating IoTivity so you have the SBoM for IoTivity. Similar to IoTivity(3.10) it is only or A/B testing and is step 2 in getting to IoTivity-SBoM-OC2.

### 3.12 IoTivity-SBoM-OpenC2 microSD
This may not be done by plugfest. This is software of 3.11 with OpenC2 added to do something (not clear what yet).

## 4. Test scenarios
duncan needs to fill in

### 4.1 blinky/sensor/actuator Comply2Connect "get SBoM"

### 4.2 Sensor "change settings"

### 4.3 Actuator "change settings"

### 4.4 Pi-Hole "blackhole a subdomain"

### 4.5 pfSense "add firewall rule"

### 4.6 Snort "increase logging"

### 4.7 something IoTivity
