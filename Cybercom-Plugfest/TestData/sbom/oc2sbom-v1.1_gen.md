<!-- Generated from schema\oc2sbom-v1.1.jadn, Fri Dec 20 15:53:48 2019-->
## Schema
| . | . |
| ---: | :--- |
| **title:** | Software Bill of Materials |
| **module:** | http://oasis-open.org/openc2/oc2sbom/v1.1 |
| **patch:** | 0-wd01 |
| **description:** | Query an actuator for its Software Bill of Materials |
| **exports:** | OpenC2-Command, OpenC2-Response |
| **imports:** | **ls**:&nbsp;http://oasis-open.org/openc2/oc2ls-types/v1.1 |

**_Type: OpenC2-Command (Record)_**

| ID | Name | Type | # | Description |
| ---: | :--- | :--- | ---: | :--- |
| 1 | **action** | Action | 1 | The task or activity to be performed |
| 2 | **target** | Target | 1 | The object referenced by the Action |
| 3 | **args** | Args | 0..1 | Additional information that applies to the Command |
| 4 | **actuator** | Actuator | 0..1 | The profile that defines the Command |
| 5 | **command_id** | ls:Command-ID | 0..1 | An identifier of this Command |

**_Type: OpenC2-Response (Map)_**

| ID | Name | Type | # | Description |
| ---: | :--- | :--- | ---: | :--- |
| 1 | **status** | ls:Status-Code | 1 | Integer status code |
| 2 | **status_text** | String | 0..1 | Free-form description of the Response status |
| 3 | **results** | Results | 0..1 | Results returned by the invoked Command |

**_Type: Action (Enumerated)_**

| ID | Name | Description |
| ---: | :--- | :--- |
| 3 | **query** | Initiate a request for information |

**_Type: Target (Choice)_**

| ID | Name | Type | # | Description |
| ---: | :--- | :--- | ---: | :--- |
| 9 | **features** | ls:Features | 1 | A set of items used with the query Action to determine an Actuator's capabilities |
| 1027 | **sbom/** | P-Target | 1 | Targets defined in this profile |

**_Type: Actuator (Map{1..*})_**

| ID | Name | Type | # | Description |
| ---: | :--- | :--- | ---: | :--- |

**_Type: Args (Map{1..*})_**

| ID | Name | Type | # | Description |
| ---: | :--- | :--- | ---: | :--- |

**_Type: Results (Map{1..*})_**

| ID | Name | Type | # | Description |
| ---: | :--- | :--- | ---: | :--- |
| 1 | **versions** | ls:Version unique | 0..10 | List of OpenC2 language versions supported by this Actuator |
| 2 | **profiles** | ls:Namespace unique | 0..* | List of profiles supported by this Actuator |
| 3 | **pairs** | Action-Targets | 0..1 | List of targets applicable to each supported Action |
| 4 | **rate_limit** | Number{0..*} | 0..1 | Maximum number of requests per minute supported by design or policy |
| 1027 | **sbom/** | P-Results | 0..1 | Results defined in this profile |

**_Type: Action-Targets (Map)_**

| ID | Name | Type | # | Description |
| ---: | :--- | :--- | ---: | :--- |
| 3 | **query** | Targets-Query unique | 1..10 |  |

**_Type: Targets-Query (Enumerated)_**

| ID | Name | Description |
| ---: | :--- | :--- |
| 1 | **features** |  |
| 2 | **sbom** |  |

**_Type: P-Target (Choice)_**

| ID | Name | Type | # | Description |
| ---: | :--- | :--- | ---: | :--- |
| 1 | **type** | SBOM-Type unique | 1..10 |  |

**_Type: P-Results (Record)_**

| ID | Name | Type | # | Description |
| ---: | :--- | :--- | ---: | :--- |
| 1 | **type** | SBOM-Type | 1 |  |
| 2 | **depth** | SBOM-Depth | 1 |  |
| 3 | **manifest** | ls:Artifact | 1 |  |

**_Type: SBOM-Type (Enumerated)_**

| ID | Name | Description |
| ---: | :--- | :--- |
| 1 | **CycloneDX** |  |
| 2 | **SPDX** |  |
| 3 | **SWID** |  |

**_Type: SBOM-Depth (Enumerated)_**

| ID | Name | Description |
| ---: | :--- | :--- |
| 1 | **complete** | All components and subcomponents, recursively, are included |
| 2 | **unknown** | All components and subcomponents are attempted but some are unknown |
| 3 | **one-hop** | Just top level components are included |
