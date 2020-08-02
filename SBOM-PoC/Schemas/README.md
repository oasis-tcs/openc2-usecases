# OpenC2 v1.1 Plugfest Schemas

The [Custom Actuator Profiles](https://github.com/oasis-open/openc2-custom-aps/blob/master/Schema-Template/README.md)
document provides an overview of creating and using actuator profile schemas.
This document illustrates creating a schema for a new actuator profile, using an OpenC2 controller for
[LED display panels](https://www.amazon.com/panels-digital-module-display-P3-19296mm/dp/B079JSKF21)
as an example. Using a toy example separates the mechanics of profile creation from unnecessary consideration of
of cybersecurity functionality.
Following the Sparrell naming scheme we'll call this the "[blinky](https://github.com/sparrell/BlinkyHaHa)"
profile, but it is intended to support a range of LED matrix displays including the Sparrell device.

#### 1. Select Names
The mechanism used to reference definitions from other documents is described in the OpenC2
[Namespace Registry](https://github.com/oasis-open/openc2-custom-aps/blob/master/namespace-registry.md).
We are creating the blinky profile, which initially does not need to reference other actuator profiles. But it
needs its own namespace so that it can be referenced by other documents, and for testing it needs a provisional
property name used in the OpenC2 actuator, target, args, and results lists.
Select a namespace using the registry examples:

* **Namespace:** http://oasis-open.org/openc2/custom/blinky/v1.0
* **Property Name:** blinky

#### 2. Select Actions and Targets
Define an initial set of commands that accomplish the goals of the profile.

* query features: required by OpenC2
* query blinky/device: We want to know something about the physical or virtual actuator.
* set blinky/display: We want the actuator to display something.

Additional actions and targets may be defined later.

#### 3. Create the blinky schema from the Profile Template

* Copy the Actuator Profile
[Template](https://github.com/oasis-open/openc2-custom-aps/blob/master/Schema-Template/v1.1/IDL/oc2ls-v1.1-ap-template_gen.jidl)
to a new schema file ['blinky.jidl'](blinky/blinky.jidl).
* Delete all of the actions, targets, and args that are not used.
* Fill in **blinky** where "xyz" appears in the template.
* Customize the Action-Target list to reflect the commands from step 2.

#### 4. Define profile-specific types
We specified two profile-specific targets (device and display) above.  Define their contents in AP-Target.  Define
the desired response format for these commands in AP-Results.

After defining the device-specific content, the blinky profile schema should look like
[blinky.jidl](blinky/blinky.jidl). This schema, in text or table ([blinky.md](blinky/blinky.md)) format,
forms the basis for the actuator profile document.

#### 5. Generate device schemas
Producers and Consumer devices use a machine-readable complete schema
[blinky_resolved.jadn](blinky/blinky_resolved.jadn) which has all referenced definitions copied from their source documents.
Example commands and responses can be validated using complete schema in either JADN or JSON Schema
([blinky_resolved.json](blinky.json)) format. If a "query features schema" command is added to the language spec,
Producers will be able to retrieve an actuator's machine-readable schema to determine its capabilities. The resolved
schemas for most actuators are expected to include elements from multiple profiles.

The resolved schemas can be created by hand from the actuator profile and language spec schemas, or generated using
JADN processing tools.

#### 6. Create test data
Create four directories "Bad-command", "Bad-response", "Good-command", "Good-response" in the directory containing
the resolved schema. Create test commands and responses in these locations based on whether the schema should detect
them as valid or invalid. Using a standard directory structure allows a test harness to locate and validate
test data for multiple profiles.

**Note on data formats:**

The January Plugfest used [Test Data](https://github.com/oasis-open/openc2-custom-aps/tree/master/Test) extrapolated
from two confusing JSON examples shown in the
[Language Specification V1.0 CS02](https://docs.oasis-open.org/openc2/oc2ls/v1.0/cs02/oc2ls-v1.0-cs02.html), in
section 3.1.4 (Extensions) and Annex C.  Version 1.1 of the LS is expected to correct errors in the Extensions
section and align the examples with the JSON Pointer standard (RFC 6901) and the Namespace Registry.

Summary:
1) Property names do not contain special characters such as colon or slash
2) JSON Pointers (strings that contain property names separated by slashes, e.g., "abc/def/gx")
refer to namespaced properties (as in the results returned from query features pairs)
3) There is no distinction between propery names for types defined in standard or custom profiles.
Properties named any or all of "blinky", "x-blinky", "led", "src", "dst", etc. may refer to types defined in
"http://oasis-open.org/openc2/custom/blinky/v1.0".