# OpenC2 v1.1 Plugfest Schemas

The [Custom Actuator Profiles](https://github.com/oasis-open/openc2-custom-aps/blob/master/Schema-Template/README.md)
document provides an overview of creating and using actuator profile schemas.
This document illustrates creating a schema for a new actuator profile, using an OpenC2 controller for
[LED display panels](https://www.amazon.com/panels-digital-module-display-P3-19296mm/dp/B079JSKF21)
as an example. Using a toy example separates the mechanics of profile creation from unnecessary consideration of
of cybersecurity functionality.
Following the Sparrell naming scheme we'll call this the "[blinky](https://github.com/sparrell/BlinkyHaHa)"
profile, but it is intended to support a range of LED matrix displays including the Sparrell device.

* **Project Name:** blinky

#### 1. Select Property Name and Namespace
The profile's property name is used in the OpenC2 actuator, target, args, and results lists.
The namespace allows this schema to be referenced from other documents.
The mechanism used to reference definitions from other documents is described in the OpenC2
[Namespace Registry](https://github.com/oasis-open/openc2-custom-aps/blob/master/namespace-registry.md).

Note that the property name is not tied to the name of the project or the profile. Although
we are calling this the "blinky" profile, we will use a shorter property name "led" to refer to that profile
in commands and responses.

* **Property Name:** led
* **Namespace:** http://oasis-open.org/openc2/custom/blinky/v1.0

#### 2. Select Actions and Targets
Define an initial set of commands that accomplish the goals of the profile.

* query features: required by OpenC2
* query led/device: We want to know something about the physical or virtual actuator.
* set led/display: We want the actuator to display something.

Additional actions and targets may be defined later.

#### 3. Create the blinky schema from the Profile Template

* Copy the Actuator Profile
[Template](https://github.com/oasis-open/openc2-custom-aps/blob/master/Schema-Template/v1.1/IDL/oc2ls-v1.1-ap-template.jidl)
to the project's schema file ['blinky.jidl'](blinky/blinky.jidl).
* Delete all of the actions, targets, and args that are not used.
* Replace "xyz" with the property name "led" everywhere it appears in the template.
* Customize the Action-Target list to reflect the commands from step 2. ([Show](images/ap-template-pairs.jpg))

#### 4. Define profile-specific types
We specified two profile-specific targets (device and display) above.  Define their contents in AP-Target.  Define
the desired response format for these commands in AP-Results. ([Show](images/ap-template-device.jpg))

After defining the device-specific content, the blinky profile schema should look like
[blinky.jidl](blinky/blinky.jidl). This schema, in text or table ([blinky.md](blinky/blinky.md)) format,
forms the basis for the actuator profile document.

#### 5. Generate device schemas
Producers and Consumer devices use a machine-readable complete schema
[blinky_resolved.jadn](blinky/blinky_resolved.jadn) which includes referenced definitions copied from their source documents.
Example commands and responses can be validated using the resolved schema in either JADN or JSON Schema
([blinky_resolved.json](blinky/blinky_resolved.json)) format.
The resolved schema is generated using JADN software, or it can be created manually by copying definitions
from the actuator profile and language spec schemas.

Most actuators are expected to support multiple profiles. The "Actuator" type in the resolved schema contains
the list of property names for supported profiles; this list is also returned by the "query features profiles"
command. If a "query features schema" command is added to the language spec,
Producers will be able to retrieve an actuator's resolved schema to determine its capabilities.

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