# Participation

## Summary: 

* X people
* Y Companies / Organizations
* Countries

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
* New Context
* NineFX
* Northrup Grumman
* Saltstack
* U.K. Ministry of Defense
* U.S. Department of Defense
* University of North Carolina
* University of Oslo
* sFractal Consulting
* *others TBSL*

# Projects / BoF Groups

If writing up a project, please capture the initial (start of plug fest) and final (end of plug fest) state of your project, so that we have some indication of progress made during the event.

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

