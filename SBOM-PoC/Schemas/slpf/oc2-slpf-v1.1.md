## Schema
| . | . |
| ---: | :--- |
| **title:** | Stateless Packet Filtering Profile |
| **module:** | https://oasis-open.org/openc2/oc2slpf/v1.1 |
| **description:** | Stateless Packet Filtering (SLPF) data definitions |
| **imports:** | **ls**:&nbsp;https://oasis-open.org/openc2/oc2ls-types/v1.1 |
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
| 6 | **deny** | Prevent a certain event or action from completion, such as preventing a flow from reaching a destination or preventing access. |
| 8 | **allow** | Permit access to or execution of a Target. |
| 16 | **update** | Instruct a component to retrieve, install, process, and operate in accordance with a software update, reconfiguration, or other update. |
| 20 | **delete** | Remove an entity (e.g., data, files, flows). |

**_Type: Target (Choice)_**

| ID | Name | Type | # | Description |
| ---: | :--- | :--- | ---: | :--- |
| 7 | **domain_name** | ls:Domain-Name | 1 | A network domain name. |
| 9 | **features** | ls:Features | 1 | A set of items used with the query Action to determine an Actuator's capabilities. |
| 10 | **file** | ls:File | 1 | Properties of a file. |
| 13 | **ipv4_net** | ls:IPv4-Net | 1 | An IPv4 address range including CIDR prefix length. |
| 14 | **ipv6_net** | ls:IPv6-Net | 1 | An IPv6 address range including prefix length. |
| 15 | **ipv4_connection** | ls:IPv4-Connection | 1 | A 5-tuple of source and destination IPv4 address ranges, source and destination ports, and protocol. |
| 16 | **ipv6_connection** | ls:IPv6-Connection | 1 | A 5-tuple of source and destination IPv6 address ranges, source and destination ports, and protocol. |
| 1024 | **slpf/** | AP-Target | 1 | Profile-defined targets |

**_Type: Args (Map{1..*})_**

| ID | Name | Type | # | Description |
| ---: | :--- | :--- | ---: | :--- |
| 1 | **start_time** | ls:Date-Time | 0..1 | The specific date/time to initiate the Command |
| 2 | **stop_time** | ls:Date-Time | 0..1 | The specific date/time to terminate the Command |
| 3 | **duration** | ls:Duration | 0..1 | The length of time for an Command to be in effect |
| 4 | **response_requested** | ls:Response-Type | 0..1 | The type of Response required for the Command: none, ack, status, complete |
| 1024 | **slpf/** | AP-Args | 0..1 | Profile-defined command arguments |

**_Type: Actuator (Choice)_**

| ID | Name | Type | # | Description |
| ---: | :--- | :--- | ---: | :--- |
| 1024 | **slpf/** | AP-Specifiers | 1 | Actuator specifiers defined in the Stateless Packet Filtering profile |

**_Type: Results (Map{1..*})_**

| ID | Name | Type | # | Description |
| ---: | :--- | :--- | ---: | :--- |
| 1 | **versions** | ls:Version unique | 0..10 | List of OpenC2 language versions supported by this Actuator |
| 2 | **profiles** | ls:FieldName unique | 0..* | List of profiles supported by this Actuator |
| 3 | **pairs** | Action-Targets | 0..1 | List of targets applicable to each supported Action |
| 4 | **rate_limit** | Number{0.0..*} | 0..1 | Maximum number of requests per minute supported by design or policy |
| 5 | **args** | Enumerated(Enum[Args]) | 0..* | List of supported Command Arguments |
| 1024 | **slpf/** | AP-Results | 0..1 | Profile-defined response results |

**_Type: Action-Targets (Map)_**

| ID | Name | Type | # | Description |
| ---: | :--- | :--- | ---: | :--- |
| 3 | **query** | Target-query unique | 1..* |  |
| 6 | **deny** | Target-allow-deny unique | 1..* |  |
| 8 | **allow** | Target-allow-deny unique | 1..* |  |
| 16 | **update** | Target-update unique | 1..* |  |
| 20 | **delete** | Target-delete unique | 1..* |  |

**_Type: Target-query (Enumerated)_**

| ID | Name | Description |
| ---: | :--- | :--- |
| 1 | **features** |  |
| 2 | **slpf/rule_number** |  |

**_Type: Target-allow-deny (Enumerated)_**

| ID | Name | Description |
| ---: | :--- | :--- |
| 1 | **ipv4_connection** |  |
| 2 | **ipv6_connection** |  |
| 3 | **ipv4_net** |  |
| 4 | **ipv6_net** |  |
| 5 | **domain_name** |  |

**_Type: Target-update (Enumerated)_**

| ID | Name | Description |
| ---: | :--- | :--- |
| 1 | **file** |  |

**_Type: Target-delete (Enumerated)_**

| ID | Name | Description |
| ---: | :--- | :--- |
| 1 | **slpf/rule_number** |  |

**_Type: AP-Target (Choice)_**

| ID | Name | Type | # | Description |
| ---: | :--- | :--- | ---: | :--- |
| 1 | **rule_number** | Rule-ID | 1 | Immutable identifier assigned when a rule is created. Identifies a rule to be deleted. |

**_Type: AP-Args (Map{1..*})_**

| ID | Name | Type | # | Description |
| ---: | :--- | :--- | ---: | :--- |
| 1 | **drop_process** | Drop-Process | 0..1 | Specifies how to handle denied packets |
| 2 | **persistent** | Boolean | 0..1 | Normal operations assume any changes to a device are to be implemented persistently. Setting the persistent modifier to FALSE results in a change that is not persistent in the event of a reboot or restart |
| 3 | **direction** | Direction | 0..1 | Specifies whether to apply rules to incoming or outgoing traffic. If omitted, rules are applied to ingress packets |
| 4 | **insert_rule** | Rule-ID | 0..1 | Specifies the identifier of the rule within a list, typically used in a top-down rule list |
| 5 | **logged** | Boolean | 0..1 | Specifies if a log entry should be recorded as traffic matches the rule. The manner and mechanism for recording these entries is implementation specific and not defined by this specification. |

**_Type: Drop-Process (Enumerated)_**

| ID | Name | Description |
| ---: | :--- | :--- |
| 1 | **none** | Drop the packet and do not send a notification to the source of the packet |
| 2 | **reject** | Drop the packet and send an ICMP host unreachable (or equivalent) to the source of the packet |
| 3 | **false_ack** | Drop the traffic and send a false acknowledgment |

**_Type: Direction (Enumerated)_**

| ID | Name | Description |
| ---: | :--- | :--- |
| 1 | **both** | Apply rules to all traffic |
| 2 | **ingress** | Apply rules to incoming traffic only |
| 3 | **egress** | Apply rules to outgoing traffic only |

**_Type: AP-Specifiers (Map)_**

| ID | Name | Type | # | Description |
| ---: | :--- | :--- | ---: | :--- |
| 1 | **hostname** | String | 0..1 | [RFC1123] hostname (can be a domain name or IP address) for a particular device with SLPF functionality |
| 2 | **named_group** | String | 0..1 | User defined collection of devices with SLPF functionality |
| 3 | **asset_id** | String | 0..1 | Unique identifier for a particular SLPF |
| 4 | **asset_tuple** | String | 0..1 | Unique tuple identifier for a particular SLPF consisting of a list of up to 10 strings |

**_Type: AP-Results (Map{1..*})_**

| ID | Name | Type | # | Description |
| ---: | :--- | :--- | ---: | :--- |
| 1 | **rule_number** | Rule-ID | 1 | Rule identifier returned from allow or deny Command |


| Type Name | Type Definition | Description |
| :--- | :--- | :--- |
| **Rule-ID** | Integer | Access rule identifier |
