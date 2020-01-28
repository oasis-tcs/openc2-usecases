# Participation

## Summary:

* X people
* Y Companies / Organizations
* 3? Countries (Norway, UK, USA)

## Programming Languages Used

Python, Erlang, Elixer, ...

## Transfer Protocols Used

HTTP, HTTPS, OpenDXL, MQTT, ...

## Companies / Organizations Participating

* AT&T
* BAE Systems
* BluVector
* CACI UK
* Clarity Cyber
* Google
* Hereuco
* Huntington-Ingalls
* National Security Agency
* NEC Corporation
* New Context
* NineFX
* Northrup Grumman
* Saltstack
* sFractal Consulting
* U.K. Ministry of Defense
* U.S. Department of Defense
* University of North Carolina
* University of Oslo
* *others TBSL*

# Projects / BoF Groups

If writing up a project, please capture the initial (start of plug fest) and final (end of plug fest) state of your project, so that we have some indication of progress made during the event.

## Project: OpenC2 Schema Tools
*Description:* GCP-based schema processor with a REST API and a web front end.  This is a "meta-project" intended
to support project development during and after the plugfest.

*State:*
* Initial / Final State: API functions available with manual URL typing.  Web-based UI is planned.
* Releaseability: open source [OpenC2 Schema Tools]
     * [Presentation](https://drive.google.com/open?id=1VAMWY9JriFjKNzbRXSz6ZjeVk-oOyYn4XKHP3CouiCI)
     * [API Definition](https://drive.google.com/open?id=1b3XKWbPP41qXPBlrM8BUgPyesmBV7UNz9tllR9frzXo)
     * [Plugfest Schemas](https://github.com/oasis-open/openc2-custom-aps/tree/master/Schema-Template) v1.0.1/Separate/JADN
* Demonstrated? no
* Interworked? N/A

## Project: OpenC2 Cloud Compute Actuator (New Context)
*Description:* The project implements an actuator to create and control cloud VM
s.

*State:*
* At plugfest / described
* Initial / Final State
* Releaseability: open source [OpenC2-aws-actuator](https://github.com/newcontext-oss/openc2-aws-actuator)
* Demonstrated? yes
* Interworked? no, no other implementations available

## Project: OpenC2 Integration Framework (OIF) Orchestrator (NSA OpenC2 Team)

*Description:* this project ...

*State:*
* At plugfest / described
* Initial / Final State
* Releaseability: open source vs. proprietary
* Demonstrated?
* Interworked?

## Project: Cloud Firewall Common Command (AT&T / UNC / UOslo / ...)

*Description:* this project ...

*State:*
* At plugfest / described
* Initial / Final State
* Releaseability: open source vs. proprietary
* Demonstrated?
* Interworked?

## Project: OpenC2 on CANBUS (BAE Systems)

*Description:* this project ...

*State:*
* Described
* Initial / Final State
* Releaseability: open source vs. proprietary
* Demonstrated?
* Interworked?

## Project: Unified Cyber Defense Platform (Northrup Grumman)

*Description:* this project ...

*State:*
* At plugfest / described
* Initial / Final State
* Releaseability: open source vs. proprietary
* Demonstrated?
* Interworked?

## Project: HaHa Actuator on Raspberry Pi (sFractal Consulting)

*Description:* This project is based on the HaHa elixir open
source code. See https://github.com/oasis-open/openc2-lycan-beam/tree/master/haha/elixir.
Several aspects:
* HaHa/SBOM/Blinky actuator running on laptop
* Blinky running on Raspberry Pi Zero
* Blinky running on Raspberry Pi 4

*State:*

* State before plugfest
  + openc2 haha/sbom/blink server running on laptop on HTTP (not OC2-compliant HTTPS)
  + blinky running on raspberry pi's - but not yet OpenC2 controlled
* State at end of plugfest
  + HTTPS was added - alot of issues with certs, headers, and stuff that really wasn't OC2 but impeded
  + other people accessed HaHa & SBOM using postman. Accessing from HII OIF did not work due to header issues. Accessing from NineFX code worked if all the cert checks were disabled
* Everything used was open source
* Demonstrated - yes
* Interworked:
  + Yes via HTTP (non-compliant with OC2 Transport Spec) using Postman
  + Yes via HTTPS using postman (probably not OC2-compliant, not clear on header issues)
  + Sort of Yes from NineFX code (custom response header issues on sFractal side)
  + No from HII OIF

## Project: Dynamic Recognition of Actuator Capabilities (UK Mod / CACI UK)

*Description:* this project ...

*State:*
* Described
* Initial / Final State
* Releaseability: open source vs. proprietary
* Demonstrated?
* Interworked?

## Project: Erlang-based Command Generator (NineFX)

*Description:* this project ...

*State:*
* At plugfest / described
* Initial / Final State
* Releaseability: open source vs. proprietary
* Demonstrated?
* Interworked?

## Project: Web-based Command Generator (Hereuco)

*Description:* this project ...

*State:*
* At plugfest / described
* Initial / Final State
* Releaseability: open source vs. proprietary
* Demonstrated?
* Interworked?

## Project: Vector-based Malware Classifier (BluVector)

*Description:* this project ...

*State:*
* At plugfest / described
* Initial / Final State
* Releaseability: open source vs. proprietary
* Demonstrated?
* Interworked?

## Project: VirusTotal Malware Check (Google)

*Description:* this project ...

*State:*
* At plugfest / described
* Initial / Final State
* Releaseability: open source vs. proprietary
* Demonstrated?
* Interworked?

## Project: Endpoint File Blacklist and Device Quarantine (Symantec ICDx)

*Description:* this project ...

*State:*
* At plugfest / described
* Initial / Final State
* Releaseability: open source vs. proprietary
* Demonstrated?
* Interworked?

## Project: Consumer/Orchestrator Handling Multiple Responses (Symantec ICDx)

*Description:* this project ...

*State:*
* At plugfest / described
* Initial / Final State
* Releaseability: open source vs. proprietary
* Demonstrated?
* Interworked?

## Project: Blinky Light Board (NSA OpenC2 Team)

*Description:* this project ...

*State:*
* At plugfest / described
* Initial / Final State
* Releaseability: open source vs. proprietary
* Demonstrated?
* Interworked?

# Scenarios

## Scenario: Active Cyber Defense of Critical Infrastructure (ACDCI) (Clarity Cyber / NSA OpenC2 Team)

*Description:* this project ...

*State:*
* At plugfest / described
* Initial / Final State
* Releaseability: open source vs. proprietary
* Demonstrated?
* Interworked?

## Scenario 2: Name2

*Description:* this project ...

*State:*
* At plugfest / described
* Initial / Final State
* Releaseability: open source vs. proprietary
* Demonstrated?
* Interworked?

# Issues Identified

## Issue 1: Authentication

*Source*:  Firewall / Packet Filtering BoF

*Description:* while doing X, we discovered Y ...

*Potential Solutions*: suggestions for resolutions or work-arounds developed

## Issue 2: Limited data in responses from actuators

Rules, which actuator, support for temporal?  (may need to break this into multiple issues)

*Source*:  Firewall / Packet Filtering BoF

*Description:* while doing X, we discovered Y ...

*Potential Solutions*: suggestions for resolutions or work-arounds developed

## Issue 3: Temporal Requirements - Start / Stop

*Source*:  Firewall / Packet Filtering BoF

*Description:* while doing X, we discovered Y ...

*Potential Solutions*: suggestions for resolutions or work-arounds developed

## Issue 4: Multiple Targets or Similar Commands

*Source*:  Firewall / Packet Filtering BoF

*Description:* while doing X, we discovered Y ...

*Potential Solutions*: suggestions for resolutions or work-arounds developed

## Issue 5: Logging per rule?

*Source*:  Firewall / Packet Filtering BoF

*Description:* while doing X, we discovered Y ...

*Potential Solutions*: suggestions for resolutions or work-arounds developed

## Issue 6: Comment on Rule

*Source*:  Firewall / Packet Filtering BoF

*Description:* while doing X, we discovered Y ...

*Potential Solutions*: suggestions for resolutions or work-arounds developed

## Issue 7: Clarify ipv4net

Ipv4net should be clarified as ANY->ipv4net AND ipv4net->ANY : 2 rules

*Source*:  Firewall / Packet Filtering BoF

*Description:* while doing X, we discovered Y ...

*Potential Solutions*: suggestions for resolutions or work-arounds developed

## Issue 8: Transfer Response Handling when "Response = NONE"

*Source*:  Firewall / Packet Filtering BoF

*Description:* while doing X, we discovered Y ... (conflict between OpenC2 command selecting the "repsonse = NONE" option whereas the HTTP transfer protocols *requires* a response.

*Potential Solutions*: suggestions for resolutions or work-arounds developed

## Issue 9: Forward packet/duplicate packet/offload

*Source*:  Firewall / Packet Filtering BoF

*Description:* while doing X, we discovered Y ...

*Potential Solutions*: suggestions for resolutions or work-arounds developed

## Issue 10: What knows the security-group name and priority to use?

*Source*:  Firewall / Packet Filtering BoF

*Description:* while doing X, we discovered Y ...

*Potential Solutions*: suggestions for resolutions or work-arounds developed

## Issue 11: Content Balance Between HTTPS Headers and OpenC2 Message Content

*Source*:  Multiple groups.

*Description:* PF participants had numerous interworking issues relating to informtion in HTTP headers vs. OpenC2 message content.

*Potential Solutions*: revisit the decisions made for the v1.0  HTTPS specification for such information elements as the CommandID, content type, etc., based on results of plug fest attempts to achieve interoperability between a variety of implementations. Potential changes include simplifying the content type to simply be "JSON", and adding OpenC2 version information and command IDs into the message content.  This may fold back into the definition of OpenC2 messages in the Language Specification.

## Issue N: NameN

*Source*:  (who / what group identified this issue)

*Description:* while doing X, we discovered Y ...

*Potential Solutions*: suggestions for resolutions or work-arounds developed

## Issue N: NameN

*Source*:  (who / what group identified this issue)

*Description:* while doing X, we discovered Y ...

*Potential Solutions*: suggestions for resolutions or work-arounds developed

## Issue N: NameN

*Source*:  (who / what group identified this issue)

*Description:* while doing X, we discovered Y ...

*Potential Solutions*: suggestions for resolutions or work-arounds developed
