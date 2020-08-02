## Schema
| . | . |
| ---: | :--- |
| **title:** | OpenC2 LED Display Actuator Profile |
| **module:** | http://oasis-open.org/openc2/blinky/v1.0 |
| **description:** | Adapted from the OpenC2 Language Profile version 1.1 |
| **imports:** | **ls**:&nbsp;http://oasis-open.org/openc2/oc2ls-types/v1.1 |
| **exports:** | OpenC2-Command, OpenC2-Response |

**_Type: OpenC2-Command (Record)_**

| ID | Name | Type | # | Description |
| ---: | :--- | :--- | ---: | :--- |
| 1 | **action** | Action | 1 | The task or activity to be performed (i.e., the 'verb'). |
| 2 | **target** | Target | 1 | The object of the Action. The Action is performed on the Target. |
| 3 | **args** | Args | 0..1 | Additional information that applies to the Command. |
| 4 | **actuator** | Actuator | 0..1 | The subject of the Action. The Actuator executes the Action on the Target. |
| 5 | **command_id** | ls:Command-ID | 0..1 | An identifier of this Command. |

**_Type: OpenC2-Response (Record)_**

| ID | Name | Type | # | Description |
| ---: | :--- | :--- | ---: | :--- |
| 1 | **status** | ls:Status-Code | 1 | An integer status code. |
| 2 | **status_text** | String | 0..1 | A free-form human-readable description of the Response status. |
| 3 | **results** | Results | 0..1 | Map of key:value pairs that contain additional results based on the invoking Command. |

**_Type: Action (Enumerated)_**

| ID | Name | Description |
| ---: | :--- | :--- |
| 3 | **query** | Initiate a request for information. |
| 15 | **set** | Change a value, configuration, or state of a managed entity. |

**_Type: Target (Choice)_**

| ID | Name | Type | # | Description |
| ---: | :--- | :--- | ---: | :--- |
| 9 | **features** | ls:Features | 1 | A set of items used with the query Action to determine an Actuator's capabilities. |
| 2000 | **blinky/** | AP-Target | 1 | Profile-defined targets |

**_Type: Actuator (Map{1..*})_**

| ID | Name | Type | # | Description |
| ---: | :--- | :--- | ---: | :--- |

**_Type: Args (Map{1..*})_**

| ID | Name | Type | # | Description |
| ---: | :--- | :--- | ---: | :--- |
| 1 | **start_time** | ls:Date-Time | 0..1 | The specific date/time to initiate the Command |
| 2 | **stop_time** | ls:Date-Time | 0..1 | The specific date/time to terminate the Command |
| 2000 | **blinky/** | AP-Args | 1 | Profile-defined command arguments |

**_Type: Results (Map{1..*})_**

| ID | Name | Type | # | Description |
| ---: | :--- | :--- | ---: | :--- |
| 1 | **versions** | ls:Version unique | 0..10 | List of OpenC2 language versions supported by this Actuator |
| 2 | **profiles** | ls:Namespace unique | 0..* | List of profiles supported by this Actuator |
| 3 | **pairs** | Action-Targets | 0..1 | List of targets applicable to each supported Action |
| 5 | **args** | Enumerated(Enum[Args]) | 0..* | List of supported Command Arguments |
| 2000 | **blinky/** | AP-Results | 1 | Profile-defined response results |

**_Type: Action-Targets (Map{1..*})_**

| ID | Name | Type | # | Description |
| ---: | :--- | :--- | ---: | :--- |
| 3 | **query** | Targets-query unique | 0..10 |  |
| 15 | **set** | Targets-set unique | 0..10 |  |

**_Type: Targets-query (Enumerated)_**

| ID | Name | Description |
| ---: | :--- | :--- |
| 1 | **features** |  |
| 2 | **blinky/device** |  |

**_Type: Targets-set (Enumerated)_**

| ID | Name | Description |
| ---: | :--- | :--- |
| 1 | **blinky/display** |  |

**_Type: AP-Target (Choice)_**

| ID | Name | Type | # | Description |
| ---: | :--- | :--- | ---: | :--- |
| 1 | **device** | ArrayOf(Enum[Blinky-Device]){1..*} | 1 | Device properties to return |
| 2 | **display** | Blinky-Display | 1 |  |

**_Type: AP-Specifiers (Map{1..*})_**

| ID | Name | Type | # | Description |
| ---: | :--- | :--- | ---: | :--- |

**_Type: AP-Args (Map{1..*})_**

| ID | Name | Type | # | Description |
| ---: | :--- | :--- | ---: | :--- |

**_Type: AP-Results (Map{1..*})_**

| ID | Name | Type | # | Description |
| ---: | :--- | :--- | ---: | :--- |
| 1 | **device** | Blinky-Device | 1 |  |

**_Type: Blinky-Device (Map)_**

| ID | Name | Type | # | Description |
| ---: | :--- | :--- | ---: | :--- |
| 1 | **product** | String | 1 | Descriptive name of actuator device |
| 2 | **resolution** | String | 1 | width x height |

**_Type: Blinky-Display (Map)_**

| ID | Name | Type | # | Description |
| ---: | :--- | :--- | ---: | :--- |
| 1 | **predefined** | Canned-Displays | 1 | Pre-defined patterns to display |
| 2 | **image** | ls:Artifact | 1 | Still image file |
| 3 | **animation** | ls:Artifact | 1 | Moving image file |

**_Type: Canned-Displays (Enumerated)_**

| ID | Name | Description |
| ---: | :--- | :--- |
| 1 | **orange** |  |
| 2 | **purple** |  |
| 3 | **rainbow** | color-cycling |
| 4 | **space-invaders** | animation |
