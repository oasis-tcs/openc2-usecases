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
* Endpoint Manager (EPM) - actuator that requests a SWID-formatted inventory.  Consumer in C2C profile, Producer in EPM profile.
* Endpoint - device that attempts to connect to a network, Consumer in EPM profile

### Network Functions
* Comply-to-connect (C2C) profile - NM Producer, EPM Consumer
    * 'contain' action on 'device' target
    * 'investigate' action on 'device' target
    * 'query' action to determine conformance of software inventory to network policy ('scan' isn't right)
* Network Control (NC) profile - NM Producer, NC Consumer
    * 'allow' action on device target
    * 'deny' action on device target
    * 'contain' action on device target
* Endpoint Management (EPM) profile - EPM Producer, Endpoint Consumer
    * 'query' action on S/W inventory target
    * 'update' action on a S/W target
