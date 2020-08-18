# OpenC2 v1.1 Plugfest Schemas

Expanding on the actuator profile
[overview](https://github.com/oasis-open/openc2-custom-aps/blob/master/Schema-Template/README.md),
this document steps through the process of creating a new actuator profile and then using that profile to create
a device schema to support development and interoperability testing:

![](images/ap-process.jpg)

It uses an OpenC2 controller for
[LED display panels](https://www.amazon.com/panels-digital-module-display-P3-19296mm/dp/B079JSKF21)
as an example. Using a toy example separates the mechanics of profile creation from unnecessary consideration
of cybersecurity functionality.
Following the Sparrell naming scheme we'll call this the "[blinky](https://github.com/sparrell/BlinkyHaHa)"
profile, but it is intended to support a range of LED matrix displays including the Sparrell device.

* **Project Name:** blinky

#### 1. Select Namespace
The profile's namespace allows it to be referenced from other documents.
Select a namespace for this profile as described in the OpenC2
[Namespace Registry](https://github.com/oasis-open/openc2-custom-aps/blob/master/namespace-registry.md).

* **Namespace:** https://oasis-open.org/openc2/custom/blinky/v1.1

#### 2. Select Actions and Targets
Define an initial set of commands that accomplish the goals of the profile.

* query features: required by OpenC2
* query led/device: We want to know something about the physical or virtual actuator.
* set led/display: We want the actuator to display something.

Additional actions and targets may be defined later.

#### 3. Create the blinky profile schema

* Copy the Actuator Profile
[Template](https://github.com/oasis-open/openc2-custom-aps/blob/master/Schema-Template/v1.1/IDL/oc2ls-v1.1-ap-template.jidl)
to the project's schema file ['blinky.jidl'](blinky/blinky.jidl).
* Delete all unused actions, targets, and args.

#### 4. Define profile-specific types
We specified two profile-specific targets (device and display) above.  Define their contents as fields of AP-Target.
Define the desired response format for these commands as fields of AP-Results. ([Show](images/ap-template-device.jpg)).
Note that this example defines a "Device" type, which also happens to be the name of an OpenC2 Target.
Namspaced type references (ls:Device) allows both definitions to be used without conflict.

After defining the device-specific content, the blinky profile schema should look like
[blinky.jidl](blinky/blinky.jidl). This schema, in text or table ([blinky.md](blinky/blinky.md)) format,
forms the basis for the actuator profile document.

#### 5. Generate device schemas
Once the actuator profile has been created, we can generate a schema for a device that supports this and other profiles.
Each profile needs to be assigned a namespace id (NSID) and a profile id/name pair.
The OpenC2 language specification contains a list of profile ids/names;
choose nonconflicting values for each of the new profiles supported by the device.
NSIDs are local to the device schema and may be chosen arbitrarily.
A profile name may be used as its NSID, but NSIDs should be short. Choose a different NSID to illustrate
that they aren't required to be the same:

* **Namespace ID:** led
* **Profile ID, Name:** 2000, blinky

Replace the id and name (0, ap_name) placeholders with actual values (2000, blinky) for each supported profile
in Target, Args, Specifiers, and Results. Replace nsid placeholders with the nsids chosen for each supported profile
in the "imports" data and in AP-Target, AP-Args, AP-Specifiers and AP-Results.

Producer and Consumer devices use a "resolved" device schema
[blinky_resolved.jadn](blinky/blinky_resolved.jadn) which includes all referenced definitions copied from their source documents.
Example commands and responses can be validated using the resolved schema in either JADN or JSON Schema
([blinky_resolved.json](blinky/blinky_resolved.json)) format.
The resolved schema is normally generated automatically by schema tools, but can be created manually by copying
definitions from the referenced actuator profile and language spec schemas.

After resolving the referenced type definitions, the device schema is ready to use.

#### 6. Create test data
Create four directories "Good-command", "Good-response", "Bad-command", and "Bad-response" in the directory
containing the resolved schema. Create good and invalid test messages in these locations.
Using a standard directory structure allows testing software to locate and validate test data for multiple profiles.

#### 7. Validate test data
The Python script [test-poc.py](test-poc.py) will validate test data against the schema for all projects.
Before running the script, obtain a GitHub
[personal access token](https://docs.github.com/en/github/authenticating-to-github/creating-a-personal-access-token)
and save it in environment variable "GitHubToken".  (Or if you have already created a token, modify the script
to use it.) Without a token the GitHub request rate is severely limited.

**Note on data formats:**

The January Plugfest used [Test Data](https://github.com/oasis-open/openc2-custom-aps/tree/master/Test) extrapolated
from two confusing JSON examples shown in the
[Language Specification V1.0 CS02](https://docs.oasis-open.org/openc2/oc2ls/v1.0/cs02/oc2ls-v1.0-cs02.html), in
section 3.1.4 (Extensions) and Annex C.  Version 1.1 of the LS is expected to correct errors in the Extensions
section and align the examples with the JSON Pointer standard (RFC 6901) and the Namespace Registry.

Summary:
1) Property names do not contain special characters such as colon or slash.
2) A JSON Pointer is a string containing property names separated by slashes, e.g., "abc/def/gh". A pointer
string is used to refer to properties with namespaced types, such as the results returned by query features pairs.
3) There is no distinction between property names for standard or custom profiles.
Properties named "blinky", "x-blinky", "led", "src", "dst", etc. may all be used by a schema to reference
types defined in "http://oasis-open.org/openc2/custom/blinky/v1.0".