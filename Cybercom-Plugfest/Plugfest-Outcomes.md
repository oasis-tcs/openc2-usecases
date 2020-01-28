# Participation

Summary:

* X people
* Y Companies / Organizations
* 3? Countries (Norway, UK, USA)

Companies / Organizations Participating

* AT&T
* BAE Systems
* BluVector
* CACI UK
* Clarity Cyber
* Google
* Hereuco
* Huntington-Ingalls
* National Security Agency
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

## Project: OpenC2 Cloud Compute Actuator
*Description:* The project implements an actuator to create and control cloud VM
s.

*State:*
* At plugfest / described
* Initial / Final State
* Releaseability: open source [OpenC2-aws-actuator](https://github.com/newcontex
t-oss/openc2-aws-actuator)
* Demonstrated? yes
* Interworked? no, no other implementations available

## Project 1: Name1

*Description:* this project ...

*State:*
* At plugfest / described
* Initial / Final State
* Releaseability: open source vs. proprietary
* Demonstrated?
* Interworked?

## Project 2: Name2

*Description:* this project ...

*State:*
* At plugfest / described
* Initial / Final State
* Releaseability: open source vs. proprietary
* Demonstrated?
* Interworked?

## Project: sFractal HaHa/SBOM/Blinky

*Description:* This project is based on the HaHa elixir open
source code. See https://github.com/oasis-open/openc2-lycan-beam/tree/master/haha/elixir

*State:*
* State before plugfest
  + openc2 haha server running on laptop on HTTP (not OC2 compliant HTTPS)
  + blinky running on raspberry pi - but not yet OpenC2 controlled
* State at end of plugfest
  + HTTPS was added - alot of issues with certs, headers, and stuff that really wasn't OC2 but impeded
  + other people accessed HaHa using postman. Accessing from HI OIF did not work due to header issues. Accessing from NineFX code worked if all the cert checks were disabled
* Everything used was open source
* Demonstrated - yes
* Interworked:
  + Yes via HTTP (non compliant with OC2 Transport Spec)using Postman
  + Yes via HTTPS using postman
  + Sort of Yes from NineFX code (custom response header issues on sFractal side)
  + No from HI OIF

# Scenarios

## Scenario 1: Name1

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
