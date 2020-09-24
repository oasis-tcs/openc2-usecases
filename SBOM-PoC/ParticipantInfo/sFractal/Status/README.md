# sFractal status
The following marks will be used to show status:
- :new: - new status
- :white_check_mark: - done
- :construction: - under active development
- :soon: - not under active development yet
- :alien: - need assistance from others

There are potentially many types of sFractal devices which consist of 4 environments by 3 transports by (w or wo) MUD.
- Environment
   + Blinky-X (Raspberry Pi)
   + Twinkly-x (Blinky twin in the cloud),
   + Cloudy-X (Twinkly with correct cloud SBOM instead of Raspberry Pi SBOM)
   + Stinky-X (many versions of other varieties with a fictional SBOMs to drive vulnerability use cases)
- Transports
   + X-HaHa - HTTP
   + X-MaHa - MQTT
   + X-DaHa - OpenDxl
- MUD
   + wo MUD
   + MUD

## Table of Contents
- [Sprint ending 24-Sep](#sprint-ending-24-sep)
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
- [Sprint ending 12-Aug](#sprint-ending-12-aug)

## Sprint ending 24-Sep
TL:DR
- Focus was on TwinklyMaha
- MQTT working
   - what topic structure for plugfest? using sfract/command
   - OpenC2 over MQTT is "just command", not message envelope or signature
- Have GCP instances
   - dockerizing for duplication and still debugging
   - http://35.184.192.117:4000/twinkly is live and can change lights via HII MQTT broker   
- Need to update Sboms
   - https://sbom.democert.org/sbom/ being updated to include cycloneDx JSON. I need to update SBOMs (and SBOM AP) accordingly

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
- :white_check_mark: twinkly webpage GCP
    - http://35.184.192.117:4000/twinkly check it out
- :white_check_mark: MQTT OpenC2 "hello world" locally
- :new: :white_check_mark: MQTT SBOM
- :new: :white_check_mark:  MQTT blink weblights
- :new: :white_check_mark:  MQTT GCP
   - http://35.184.192.117:4000/twinkly  blinks lights via HII broker
- :construction: dockerize TwinklyMaha, duplicate copies, use process for HaHa, etc
- :construction: test rig (ie a Producer to test the consumers)
- :construction: update topic schema for Plugfest (to what?)
- :construction: add OpenC2 message envelope
- :question: should I add OpenC2 message signature?
- :question: can I get away without adding TLS?

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
- :white_check_mark: - TwinklyMaHa using HII MQTT broker
- :alien: :construction: - TwinklyMaHa OIF testing
- :construction: - schema generator testing
#### 2.2 OPEN/sFractal
- :white_check_mark: - obtained sensor DIY kits
- :white_check_mark: - obtained network DIY kits
   - :new: issue. new hardware on order. May not arrive in time 
- :construction: - build kits and integrate
- :soon: - SBOM analysis
- :soon: - OpenC2 analysis
#### 2.23 others/sFractal
- :soon: - let me know who else wants to interwork

### 3. status.sbom.sfractal.com
- :construction: - website for overall plugfest status
