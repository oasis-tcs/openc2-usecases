## Schema
| . | . |
| ---: | :--- |
| **title:** | OpenC2 LED Display Actuator Profile |
| **module:** | https://oasis-open.org/openc2/blinky/v1.1 |
| **description:** | Derived from OpenC2 v1.1 Actuator Profile Template |
| **imports:** | **ls**:&nbsp;https://oasis-open.org/openc2/oc2ls-types/v1.1 |
| **exports:** | AP-Target, AP-Args, AP-Specifiers, AP-Results |

**_Type: Action (Enumerated)_**

| ID | Name | Description |
| ---: | :--- | :--- |
| 3 | **query** | Initiate a request for information. |
| 15 | **set** | Change a value, configuration, or state of a managed entity. |

**_Type: Target (Choice)_**

| ID | Name | Type | # | Description |
| ---: | :--- | :--- | ---: | :--- |
| 9 | **features** | ls:Features | 1 | A set of items used with the query Action to determine an Actuator's capabilities. |
| 0 | **ap_name/** | AP-Target | 1 | Profile-defined targets |

**_Type: Args (Map{1..*})_**

| ID | Name | Type | # | Description |
| ---: | :--- | :--- | ---: | :--- |
| 1 | **start_time** | ls:Date-Time | 0..1 | The specific date/time to initiate the Command |
| 2 | **stop_time** | ls:Date-Time | 0..1 | The specific date/time to terminate the Command |
| 0 | **ap_name/** | AP-Args | 0..1 | Profile-defined command arguments |

**_Type: Actuator (Choice)_**

| ID | Name | Type | # | Description |
| ---: | :--- | :--- | ---: | :--- |
| 0 | **ap_name/** | AP-Specifiers | 1 | Actuator specifiers defined in this profile |

**_Type: Results (Map{1..*})_**

| ID | Name | Type | # | Description |
| ---: | :--- | :--- | ---: | :--- |
| 1 | **versions** | ls:Version unique | 0..10 | List of OpenC2 language versions supported by this Actuator |
| 2 | **profiles** | ls:FieldName unique | 0..* | List of profiles supported by this Actuator |
| 3 | **pairs** | Action-Targets | 0..1 | List of targets applicable to each supported Action |
| 4 | **rate_limit** | Number{0.0..*} | 0..1 | Maximum number of requests per minute supported by design or policy |
| 5 | **args** | Enumerated(Enum[Args]) | 0..* | List of supported Command Arguments |
| 0 | **ap_name/** | AP-Results | 0..1 | Profile-defined response results |

**_Type: AP-Target (Choice)_**

| ID | Name | Type | # | Description |
| ---: | :--- | :--- | ---: | :--- |
| 1 | **device** | ArrayOf(Enum[Device]){1..*} unique | 1 | Device properties to return |
| 2 | **display** | Display | 1 |  |

**_Type: AP-Args (Map{1..*})_**

| ID | Name | Type | # | Description |
| ---: | :--- | :--- | ---: | :--- |

**_Type: AP-Specifiers (Map)_**

| ID | Name | Type | # | Description |
| ---: | :--- | :--- | ---: | :--- |

**_Type: AP-Results (Map{1..*})_**

| ID | Name | Type | # | Description |
| ---: | :--- | :--- | ---: | :--- |
| 1 | **device** | Device | 0..1 |  |

**_Type: Device (Map{1..*})_**

| ID | Name | Type | # | Description |
| ---: | :--- | :--- | ---: | :--- |
| 1 | **product** | String | 0..1 | Descriptive name of actuator device |
| 2 | **resolution** | String | 0..1 | width x height |

**_Type: Display (Choice)_**

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
