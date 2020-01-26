<!-- Generated from schema\oc2ls-v1.0.1-acme_rsp.jadn, Mon Nov  4 15:03:29 2019-->
## Schema
| . | . |
| ---: | :--- |
| **title:** | SLPF + Acme schema - Response |
| **module:** | http://oasis-open.org/openc2/oc2ls/v1.0.1/acme/rsp |
| **patch:** | 0 |
| **description:** | OpenC2 LS version 1.0 + errata + SLPF + Acme types |
| **exports:** | OpenC2-Response |
| **config:** | **$FS**:&nbsp;: **$FieldName**:&nbsp;^[a-z][-_:a-z0-9]{0,31}$ |

**_Type: OpenC2-Response (Map)_**

| ID | Name | Type | # | Description |
| ---: | :--- | :--- | ---: | :--- |
| 1 | **status** | Status-Code | 1 | An integer status code |
| 2 | **status_text** | String | 0..1 | A free-form human-readable description of the Response status |
| 3 | **results** | Results | 0..1 | Map of key:value pairs that contain additional results based on the invoking Command. |

**_Type: Results (Map{1..*})_**

| ID | Name | Type | # | Description |
| ---: | :--- | :--- | ---: | :--- |
| 1 | **versions** | Version unique | 0..* | List of OpenC2 language versions supported by this Actuator |
| 2 | **profiles** | ArrayOf(Nsid) | 0..1 | List of profiles supported by this Actuator |
| 3 | **pairs** | Action-Targets | 0..1 | List of targets applicable to each supported Action |
| 4 | **rate_limit** | Number | 0..1 | Maximum number of requests per minute supported by design or policy |
| 1024 | **slpf:** | P-Results | 0..1 | Result properties defined in the Stateless Packet Filtering Profile |
| 3010 | **x-esm:** | P-Results$esm | 0..1 | Results from the hypothetical Energy Storage Manager profile |
| 3011 | **x-acme:** | P-Results$acme | 0..1 | Results from the hypothetical Acme profile |
| 3012 | **x-mycompany:** | P-Results$myco | 0..1 | Results from the hypothetical My Company profile |

**_Type: Action-Targets (Map{1..*})_**

| ID | Name | Type | # | Description |
| ---: | :--- | :--- | ---: | :--- |
| 1 | **scan** | Tgt-scan unique | 0..10 |  |
| 2 | **locate** | Tgt-locate unique | 0..10 |  |
| 3 | **query** | Tgt-query unique | 0..10 |  |
| 6 | **deny** | Tgt-deny unique | 0..10 |  |
| 7 | **contain** | Tgt-contain unique | 0..10 |  |
| 8 | **allow** | Tgt-allow unique | 0..10 |  |
| 9 | **start** | Tgt-start unique | 0..10 |  |
| 10 | **stop** | Tgt-stop unique | 0..10 |  |
| 11 | **restart** | Tgt-restart unique | 0..10 |  |
| 14 | **cancel** | Tgt-cancel unique | 0..10 |  |
| 15 | **set** | Tgt-set unique | 0..10 |  |
| 16 | **update** | Tgt-update unique | 0..10 |  |
| 18 | **redirect** | Tgt-redirect unique | 0..10 |  |
| 19 | **create** | Tgt-create unique | 0..10 |  |
| 20 | **delete** | Tgt-delete unique | 0..10 |  |
| 22 | **detonate** | Tgt-detonate unique | 0..10 |  |
| 23 | **restore** | Tgt-restore unique | 0..10 |  |
| 28 | **copy** | Tgt-copy unique | 0..10 |  |
| 30 | **investigate** | Tgt-investigate unique | 0..10 |  |
| 32 | **remediate** | Tgt-remediate unique | 0..10 |  |

**_Type: Tgt-scan (Enumerated)_**

| ID | Name | Description |
| ---: | :--- | :--- |

**_Type: Tgt-locate (Enumerated)_**

| ID | Name | Description |
| ---: | :--- | :--- |

**_Type: Tgt-query (Enumerated)_**

| ID | Name | Description |
| ---: | :--- | :--- |
| 1 | **features** |  |

**_Type: Tgt-deny (Enumerated)_**

| ID | Name | Description |
| ---: | :--- | :--- |
| 1 | **file** |  |
| 2 | **ipv4_net** |  |
| 3 | **ipv6_net** |  |
| 4 | **ipv4_connection** |  |
| 5 | **ipv6_connection** |  |

**_Type: Tgt-contain (Enumerated)_**

| ID | Name | Description |
| ---: | :--- | :--- |
| 1 | **device** |  |

**_Type: Tgt-allow (Enumerated)_**

| ID | Name | Description |
| ---: | :--- | :--- |
| 1 | **device** |  |
| 2 | **file** |  |
| 3 | **ipv4_net** |  |
| 4 | **ipv6_net** |  |
| 5 | **ipv4_connection** |  |
| 6 | **ipv6_connection** |  |

**_Type: Tgt-start (Enumerated)_**

| ID | Name | Description |
| ---: | :--- | :--- |

**_Type: Tgt-stop (Enumerated)_**

| ID | Name | Description |
| ---: | :--- | :--- |

**_Type: Tgt-restart (Enumerated)_**

| ID | Name | Description |
| ---: | :--- | :--- |

**_Type: Tgt-cancel (Enumerated)_**

| ID | Name | Description |
| ---: | :--- | :--- |

**_Type: Tgt-set (Enumerated)_**

| ID | Name | Description |
| ---: | :--- | :--- |

**_Type: Tgt-update (Enumerated)_**

| ID | Name | Description |
| ---: | :--- | :--- |
| 1 | **file** |  |

**_Type: Tgt-redirect (Enumerated)_**

| ID | Name | Description |
| ---: | :--- | :--- |

**_Type: Tgt-create (Enumerated)_**

| ID | Name | Description |
| ---: | :--- | :--- |

**_Type: Tgt-delete (Enumerated)_**

| ID | Name | Description |
| ---: | :--- | :--- |
| 1 | **slpf:rule_number** |  |

**_Type: Tgt-detonate (Enumerated)_**

| ID | Name | Description |
| ---: | :--- | :--- |

**_Type: Tgt-restore (Enumerated)_**

| ID | Name | Description |
| ---: | :--- | :--- |

**_Type: Tgt-copy (Enumerated)_**

| ID | Name | Description |
| ---: | :--- | :--- |

**_Type: Tgt-investigate (Enumerated)_**

| ID | Name | Description |
| ---: | :--- | :--- |

**_Type: Tgt-remediate (Enumerated)_**

| ID | Name | Description |
| ---: | :--- | :--- |
| 1 | **file** |  |

**_Type: Status-Code (Enumerated.ID)_**

| ID | Description |
| ---: | :--- |
| 102 | **Processing**::an interim Response used to inform the Producer that the Consumer has accepted the Command but has not yet completed it. |
| 200 | **OK**::the Command has succeeded. |
| 400 | **BadRequest**::the Consumer cannot process the Command due to something that is perceived to be a Producer error (e.g., malformed Command syntax). |
| 401 | **Unauthorized**::the Command Message lacks valid authentication credentials for the target resource or authorization has been refused for the submitted credentials. |
| 403 | **Forbidden**::the Consumer understood the Command but refuses to authorize it. |
| 404 | **NotFound**::the Consumer has not found anything matching the Command. |
| 500 | **InternalError**::the Consumer encountered an unexpected condition that prevented it from performing the Command. |
| 501 | **NotImplemented**::the Consumer does not support the functionality required to perform the Command. |
| 503 | **ServiceUnavailable**::the Consumer is currently unable to perform the Command due to a temporary overloading or maintenance of the Consumer. |


| Type Name | Type Definition | Description |
| :--- | :--- | :--- |
| **Nsid** | String{1..16} | A short identifier that refers to a namespace. |


| Type Name | Type Definition | Description |
| :--- | :--- | :--- |
| **Version** | String | Major.Minor version number |


| Type Name | Type Definition | Description |
| :--- | :--- | :--- |
| **Rule-ID** | Integer | Access rule identifier |

**_Type: P-Results (Map)_**

| ID | Name | Type | # | Description |
| ---: | :--- | :--- | ---: | :--- |
| 1024 | **rule_number** | Rule-ID | 0..1 | Rule identifier returned from allow or deny Command. |

**_Type: P-Results$acme (Map)_**

| ID | Name | Type | # | Description |
| ---: | :--- | :--- | ---: | :--- |
| 1 | **status_detail** | String | 0..1 |  |

**_Type: P-Results$myco (Map{1..*})_**

| ID | Name | Type | # | Description |
| ---: | :--- | :--- | ---: | :--- |
| 1 | **stuff** | Stuff$myco | 0..1 |  |

**_Type: Stuff$myco (Record)_**

| ID | Name | Type | # | Description |
| ---: | :--- | :--- | ---: | :--- |
| 1 | **some** | Integer | 1 |  |
| 2 | **values** | Boolean | 1..* |  |
| 3 | **defined** | String | 1 |  |

**_Type: P-Results$esm (Map{1..*})_**

| ID | Name | Type | # | Description |
| ---: | :--- | :--- | ---: | :--- |
| 1 | **asset_id** | String | 0..1 |  |
| 2 | **battery** | Battery | 0..1 |  |

**_Type: Battery (Record)_**

| ID | Name | Type | # | Description |
| ---: | :--- | :--- | ---: | :--- |
| 1 | **capacity** | Number | 1 |  |
| 2 | **charged_at** | Integer | 1 |  |
| 3 | **status** | Integer | 1 |  |
| 4 | **mode** | Battery-Mode | 1 |  |
| 5 | **visible_on_display** | Boolean | 1 |  |

**_Type: Battery-Mode (Record)_**

| ID | Name | Type | # | Description |
| ---: | :--- | :--- | ---: | :--- |
| 1 | **output** | Output-Mode | 1 |  |
| 2 | **supported** | ArrayOf(Output-Mode) | 1 |  |

**_Type: Output-Mode (Enumerated)_**

| ID | Name | Description |
| ---: | :--- | :--- |
| 10 | **high** |  |
| 13 | **trickle** |  |
