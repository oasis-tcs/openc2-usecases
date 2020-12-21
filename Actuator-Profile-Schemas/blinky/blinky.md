## Schema
| . | . |
| ---: | :--- |
| **title:** | OpenC2 LED Display Actuator Profile |
| **module:** | https://oasis-open.org/openc2/custom/blinky/v1.1 |
| **description:** | Derived from OpenC2 v1.1 Actuator Profile Template |
| **imports:** | **ls**:&nbsp;https://oasis-open.org/openc2/oc2ls-types/v1.1 |
| **exports:** | AP-Target, AP-Args, AP-Specifiers, AP-Results |

**_Type: Action (Enumerated)_**

| ID | Name | Description |
| ---: | :--- | :--- |
| 3 | **query** | Collect information about the blinky device |
| 15 | **set** | Display something on the device |

**_Type: Target (Enumerated)_**

| ID | Name | Description |
| ---: | :--- | :--- |
| 9 | **features** |  |
| 0 | **ap_name** |  |

**_Type: Args (Enumerated)_**

| ID | Name | Description |
| ---: | :--- | :--- |
| 1 | **start_time** |  |
| 2 | **stop_time** |  |
| 0 | **ap_name** |  |

**_Type: Actuator (Enumerated)_**

| ID | Name | Description |
| ---: | :--- | :--- |
| 0 | **ap_name** |  |

**_Type: Results (Enumerated)_**

| ID | Name | Description |
| ---: | :--- | :--- |
| 1 | **versions** |  |
| 2 | **profiles** |  |
| 3 | **pairs** |  |
| 4 | **rate_limit** |  |
| 5 | **args** |  |
| 0 | **ap_name** |  |

**_Type: Pairs (Enumerated)_**

| ID | Name | Description |
| ---: | :--- | :--- |
| 3 | **query: features, /device** |  |
| 15 | **set: /display** |  |

**_Type: AP-Target (Choice)_**

| ID | Name | Type | # | Description |
| ---: | :--- | :--- | ---: | :--- |
| 1 | **device** | ArrayOf(Enum[Device]){1..*} unique | 1 | Device properties to return |
| 2 | **display** | Display | 1 | Content to be displayed |

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
