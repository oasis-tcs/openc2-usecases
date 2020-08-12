# sFractal status
The following marks will be used to show status:
- :new: - new status
- :white_check_mark: - done
- :construction: - under active development
- :soon: - not under active development yet
- :alien: - need assistance from others

There are 24 types of sFractal devices which consist of 4 environments by 3 transports by (w or wo) MUD.
- Environment
   + Blinky-X (Raspberry Pi)
   + Twinkly-x (Blinky twin in the cloud),
   + Cloudy-X (Twinkly with correct cloud SBOM instead of Raspberry Pi SBOM)
   + Stinky-X (versions of other varieties with a fictional SBOMs to drive vulnerablity use cases)
- Transports
   + X-HaHa - HTTP
   + X-MaHa - MQTT
   + X-DaHa - OpenDxl
- MUD
   + wo MUD
   + MUD

## Table of Contents
- [Sprint ending 12-Aug](#sprint-ending-12-aug)
   + [1. Devices](#1-devices)
      - [1.1 BlinkyHaHa](#11-blinkyhaha)
      - [1.2 TwinklyHaHa](#12-twinklyhaha)
      - [1.3 TwinklyMaHa](#13-twinklymaha)
      - [1.4 BlinkyMaHa](#14-blinkymaha)
      - [1.5 X-DaHa](#15-x-daha)
      - [1.6 Stinky-X](#16-stinky-x)
      - [1.7 Cloudy-X](#17-cloudy-x)
      - [1.8 MUD](#18-mud)
   + [2. Interworking](#2-interworking)
      - [2.1 HII/sFractal](#21-hiisfractal)
      - [2.2 OPEN/sFractal](#22-opensfractal)
      - [2.3 others/sFractal](#223-otherssfractal)
   + [3. Status](#3-statussbomsfractalcom)
      - status.sbom.sfractal.com

## Sprint ending 12-Aug
### 1. Devices
#### 1.1 BlinkyHaHa
- Raspberry Pi (ie physical device), Http, OpenC2, SBOM
- :white_check_mark: http OpenC2 "hello world"
- :white_check_mark: http OpenC2 SBOM
- :white_check_mark: http OpenC2 blink lights
    + see https://youtu.be/RcnRFfFtKQY - changes initiated by OpenC2 commands via Postman
- :white_check_mark: connected physically for interworking
- :construction: deeper level SBOM
- :soon: https - future unless someone wants
- :soon: connecting to internet for interworking - future unless someone wants and can help me do it in reasonably secure way
- :alien: - need someone else to build one and validate

#### 1.2 TwinklyHaHa
- cloud web page, Http, OpenC2, SBOM
- :white_check_mark: twinkly webpage
- :white_check_mark: http OpenC2 "hello world"
- :white_check_mark: http OpenC2 SBOM
- :white_check_mark: http OpenC2 blink lights
- :white_check_mark: works locally
- :construction: GCP

#### 1.3 TwinklyMaHa
- cloud web page, MQTT, OpenC2, SBOM
- :white_check_mark: twinkly webpage locally
- :new: :white_check_mark: twinkly webpage GCP
    - http://35.184.192.117:4000/twinkly check it out
- :new: :white_check_mark: MQTT OpenC2 "hello world" locally
- :construction: MQTT SBOM
- :construction: MQTT blink weblights
- :construction: MQTT GCP
- :construction: test rig (ie a Producer to test the consumers)

#### 1.4 BlinkyMaHa
- Raspberry Pi (ie physical device), MQTT, OpenC2, SBOM
- :soon: (after TwinklyMaHa)

#### 1.5 X-DaHa
- OpenDxl versions of Blinky and TwinklyDaHa
- :soon: (after GCP, MAHA, HAHA's)
#### 1.6 Stinky-X
- :soon: - versions of all devices above, but with alternate fictional SBOMs to simulate vulnerable devices
#### 1.7 Cloudy-X
- :soon: - versions of the digital twins with true cloud SBOMs instead of digital twin of Raspberry Pi SBOM (eg Ubuntu SBOM instead of Nerves Buildroot SBOM, Phoenix LiveView SBOM instead of Blinkchain LED SBOM)
#### 1.8 MUD
- :soon: - versions of all of the above with MUD interface

### 2. Interworking
#### 2.1 HII/sFractal
- :white_check_mark: - BlinkyHaHa sanity test with OIF orchestrator
- :alien: more complete BlinkyHaHa testing
- :new: :white_check_mark: - TwinklyMaHa using HII MQTT broker
- :alien: :construction: - TwinklyMaHa OIF testing
- :construction: - schema generator testing
#### 2.2 OPEN/sFractal
- :white_check_mark: - obtained sensor DIY kits
- :white_check_mark: - obtained network DIY kits
- :construction: - build kits and integrate
- :soon: - SBOM analysis
- :soon: - OpenC2 analysis
#### 2.23 others/sFractal
- :soon: - let me know who else wants to interwork

### 3. status.sbom.sfractal.com
- :construction: - website for overall plugfest status

## Sprint ending 30-Jul
### BlinkyHaHa
- done
   + http OpenC2 - hello world, sbom, blinky lights
   + see https://youtu.be/RcnRFfFtKQY - changes were done with OpenC2 commands via Postman
- WIP
   + delving into deeper SBOM

### TwinklyHaHa
- done
   + http OpenC2 - hello world, sbom, blinky local webpage
   + demo?
- WIP
   + putting on GCP

### TwinklyMaHa
- done
   + blinky local webpage
- WIP
   + MQTT
   + putting on GCP

### One Planet Interworking
- WIP
   + obtained sensor DIY kits
   + obtained network DIY kits


## Sprint ending 16-Jul
should have done at the time

## Sprint ending 2-July
should have done at the time
