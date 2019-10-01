# OpenC2 Plugfest Planning

As discussed at the 18 September TC meeting OpenC2 has been offered the opportunity to run a plug fest hosted
by US Cyber Command in their public, unclassified DreamPort facility. TC members are encourage to consider
participation in this event, tentatively planned for the week of 27 January 2020.

A Tech Talk at DreamPort is planned for early November to provide that community information about OpenC2
and our plans for the plug fest.

TC chair's initial request (19 Sept) for plug fest participation: 
https://lists.oasis-open.org/archives/openc2/201909/msg00009.html

TC chair's request (25 Sept) for plug fest use cases and related information:
https://lists.oasis-open.org/archives/openc2/201909/msg00015.html

Information about DreamPort:  https://dreamport.tech/about-us.php

## Preparation
The CTI TC published lessons learned from their STIX plugfest, which
included:

**Issue:** Lack of stable/validated schema and data sets that can be used for all clients and servers

**Action:**
* Define and maintain a package of downloadable JSON schema and test data that all plugfest/interop participants can use before plugfest.
* Need common sets of data for all to use for testing.
* Need sets of data that are unique to vendors or use cases that help provide more robust testing.

This repository includes use case descriptions, schemas, and test data (good and bad) for use by participants prior to the event.

## Use Case A: Comply-to-Connect

### Operations from Use Case description:
* An orchestrator receives notification that a new device has joined the network.
* It instructs an actuator to determine the devices' compliance to network policy.
* The actuator requests a SWID formatted software inventory from the device,
* The software inventory is compared to network policy.
* The actuator then determines whether to sandbox the device, remove it from the network, or allow it network access based on the result of the comparison.
* The orchestrator informs an actuator that a critical vulnerability needs to be patched.
* The actuator checks the Configuration Management Database for device running the vulnerable software.
* The actuator ensures that these devices receive the required patch.

### Initial proposal for OpenC2 actions:
* An alert that is beyond the scope of OpenC2
* A ‘contain’ action on a ‘device’ target that limits the new devices permissions
* An ‘investigate’ action on a ‘device’ target
* A ‘query ‘ action and we will need to import a target to accommodate SW inventory
* A ‘scan’ action on a target to accommodate SW inventory which will compare the inventory to the network policy
* An analytic that is beyond the scope of OpenC2
* An ‘allow’ action on a device target
* A ‘deny’ action on a device target
* A ‘contain’ action on a device target
* An ‘update’ action on a target we will need to import to accommodate a software target

### Actor Roles:
* Network Manager (NM) - orchestrator that receives notifications of new devices.  Producer in C2C profile.
* Network Controller (NC) - SDN controller or other actuator that changes network configuration to enforce access decisions
* Endpoint Manager (EM) - Node that requests a SWID-formatted inventory.  Consumer in C2C profile, Producer in EM profile.
* Endpoint - device that attempts to connect to a network, Consumer in EM profile

### Network Functions
* Comply-to-connect (C2C) profile - NM Producer, EM Consumer
    * 'investigate' action on 'device' target
    * 'query' action to determine conformance of software inventory to network policy?
        * ('scan' isn't right, EM can't answer the question.  Is there a separate "Policy Repository" server to be queried, or is policy  and decision-making configured into the Network Manager?)
* Network Control (NC) profile - NM Producer, NC Consumer
    * 'contain' action on device target  (how is this different from allow and deny?)
    * 'allow' action on device target
    * 'deny' action on device target
* Endpoint Management (EM) profile - EM Producer, Endpoint Consumer
    * 'query' action on S/W inventory target
    * 'update' action on a S/W target
