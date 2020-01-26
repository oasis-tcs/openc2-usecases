<!-- Generated from schema\oc2ls-v1.0.1-acme_cmd.jadn, Mon Nov  4 15:03:29 2019-->
## Schema
| . | . |
| ---: | :--- |
| **title:** | SLPF + Acme schema - Command |
| **module:** | http://oasis-open.org/openc2/oc2ls/v1.0.1/acme/cmd |
| **patch:** | 0 |
| **description:** | OpenC2 LS version 1.0 + errata + SLPF + Acme types |
| **exports:** | OpenC2-Command |
| **config:** | **$FS**:&nbsp;: **$FieldName**:&nbsp;^[a-z][-_:a-z0-9]{0,31}$ |

**_Type: OpenC2-Command (Record)_**

| ID | Name | Type | # | Description |
| ---: | :--- | :--- | ---: | :--- |
| 1 | **action** | Action | 1 | The task or activity to be performed (i.e., the 'verb'). |
| 2 | **target** | Target | 1 | The object of the Action. The Action is performed on the Target. |
| 3 | **args** | Args | 0..1 | Additional information that applies to the Command. |
| 4 | **actuator** | Actuator | 0..1 | The subject of the Action. The Actuator executes the Action on the Target. |
| 5 | **command_id** | String | 0..1 | An identifier of this Command. |

**_Type: Action (Enumerated)_**

| ID | Name | Description |
| ---: | :--- | :--- |
| 1 | **scan** | Systematic examination of some aspect of the entity or its environment. |
| 2 | **locate** | Find an object physically, logically, functionally, or by organization. |
| 3 | **query** | Initiate a request for information. |
| 6 | **deny** | Prevent a certain event or action from completion, such as preventing a flow from reaching a destination or preventing access. |
| 7 | **contain** | Isolate a file, process, or entity so that it cannot modify or access assets or processes. |
| 8 | **allow** | Permit access to or execution of a Target. |
| 9 | **start** | Initiate a process, application, system, or activity. |
| 10 | **stop** | Halt a system or end an activity. |
| 11 | **restart** | Stop then start a system or an activity. |
| 14 | **cancel** | Invalidate a previously issued Action. |
| 15 | **set** | Change a value, configuration, or state of a managed entity. |
| 16 | **update** | Instruct a component to retrieve, install, process, and operate in accordance with a software update, reconfiguration, or other update. |
| 18 | **redirect** | Change the flow of traffic to a destination other than its original destination. |
| 19 | **create** | Add a new entity of a known type (e.g., data, files, directories). |
| 20 | **delete** | Remove an entity (e.g., data, files, flows). |
| 22 | **detonate** | Execute and observe the behavior of a Target (e.g., file, hyperlink) in an isolated environment. |
| 23 | **restore** | Return a system to a previously known state. |
| 28 | **copy** | Duplicate an object, file, data flow, or artifact. |
| 30 | **investigate** | Task the recipient to aggregate and report information as it pertains to a security event or incident. |
| 32 | **remediate** | Task the recipient to eliminate a vulnerability or attack point. |

**_Type: Target (Choice)_**

| ID | Name | Type | # | Description |
| ---: | :--- | :--- | ---: | :--- |
| 1 | **artifact** | Artifact | 1 | An array of bytes representing a file-like object or a link to that object. |
| 2 | **command** | String | 1 | A reference to a previously issued Command. |
| 3 | **device** | Device | 1 | The properties of a hardware device. |
| 7 | **domain_name** | Domain-Name | 1 | A network domain name. |
| 8 | **email_addr** | Email-Addr | 1 | A single email address. |
| 9 | **features** | Features | 1 | A set of items used with the query Action to determine an Actuator's capabilities. |
| 10 | **file** | File | 1 | Properties of a file. |
| 11 | **idn_domain_name** | IDN-Domain-Name | 1 | An internationalized domain name. |
| 12 | **idn_email_addr** | IDN-Email-Addr | 1 | A single internationalized email address. |
| 13 | **ipv4_net** | IPv4-Net | 1 | An IPv4 address range including CIDR prefix length. |
| 14 | **ipv6_net** | IPv6-Net | 1 | An IPv6 address range including prefix length. |
| 15 | **ipv4_connection** | IPv4-Connection | 1 | A 5-tuple of source and destination IPv4 address ranges, source and destination ports, and protocol |
| 16 | **ipv6_connection** | IPv6-Connection | 1 | A 5-tuple of source and destination IPv6 address ranges, source and destination ports, and protocol |
| 20 | **iri** | IRI | 1 | An internationalized resource identifier (IRI). |
| 17 | **mac_addr** | MAC-Addr | 1 | A Media Access Control (MAC) address - EUI-48 or EUI-64 as defined in [[EUI]](#eui) |
| 18 | **process** | Process | 1 | Common properties of an instance of a computer program as executed on an operating system. |
| 25 | **properties** | Properties | 1 | Data attribute associated with an Actuator |
| 19 | **uri** | URI | 1 | A uniform resource identifier (URI). |
| 900 | **slpf:rule_number** | Rule-ID | 1 | Immutable identifier assigned when a rule is created. Identifies a rule to be deleted |
| 901 | **x-acme:features** | Acme-Features | 1 | Bad design - no reason to duplicate Features in acme profile |
| 902 | **x-acme:container** | Acme-Container | 1 | Hypothetical container target |

**_Type: Args (Map{1..*})_**

| ID | Name | Type | # | Description |
| ---: | :--- | :--- | ---: | :--- |
| 1 | **start_time** | Date-Time | 0..1 | The specific date/time to initiate the Command |
| 2 | **stop_time** | Date-Time | 0..1 | The specific date/time to terminate the Command |
| 3 | **duration** | Duration | 0..1 | The length of time for an Command to be in effect |
| 4 | **response_requested** | Response-Type | 0..1 | The type of Response required for the Command: `none`, `ack`, `status`, `complete`. |
| 1024 | **slpf:** | P-Args | 0..1 | Command arguments defined in the SLPF actuator profile |
| 3011 | **x-acme:** | P-Args$acme | 0..1 | Command arguments from the hypothetical Acme profile |
| 3012 | **x-mycompany:** | P-Args$myco | 0..1 | Command arguments from the hypothetical My Company profile |
| 3013 | **x-mycompany_with_underscore:** | P-Args$myco2 | 0..1 | Command arguments from the hypothetical My Company 2 profile |
| 3014 | **x-example:** | P-Args$example | 0..1 | Command arguments from the hypothetical Example profile |
| 3020 | **x-395:** | P-Args$395 | 0..1 | Results from the hypothetical 395 company profile |

**_Type: Actuator (Choice)_**

| ID | Name | Type | # | Description |
| ---: | :--- | :--- | ---: | :--- |
| 1024 | **slpf:** | P-Actuator | 0..1 | Specifiers defined in the SLPF actuator profile |
| 3010 | **x-esm:** | P-Actuator$esm | 0..1 | Specifiers from the hypothetical Energy Storage Manager profile |
| 3012 | **x-mycompany:** | P-Actuator$myco | 0..1 | Results from the hypothetical My Company profile |

**_Type: Artifact (Record{1..*})_**

| ID | Name | Type | # | Description |
| ---: | :--- | :--- | ---: | :--- |
| 1 | **mime_type** | String | 0..1 | Permitted values specified in the IANA Media Types registry, [[RFC6838]](#rfc6838) |
| 2 | **payload** | Payload | 0..1 | Choice of literal content or URL |
| 3 | **hashes** | Hashes | 0..1 | Hashes of the payload content |

**_Type: Device (Map{1..*})_**

| ID | Name | Type | # | Description |
| ---: | :--- | :--- | ---: | :--- |
| 1 | **hostname** | Hostname | 0..1 | A hostname that can be used to connect to this device over a network |
| 2 | **idn_hostname** | IDN-Hostname | 0..1 | An internationalized hostname that can be used to connect to this device over a network |
| 3 | **device_id** | String | 0..1 | An identifier that refers to this device within an inventory or management system |


| Type Name | Type Definition | Description |
| :--- | :--- | :--- |
| **Domain-Name** | String /hostname | [[RFC1034]](#rfc1034), Section 3.5 |


| Type Name | Type Definition | Description |
| :--- | :--- | :--- |
| **Email-Addr** | String /email | Email address, [[RFC5322]](#rfc5322), Section 3.4.1 |


| Type Name | Type Definition | Description |
| :--- | :--- | :--- |
| **Features** | ArrayOf(Feature){0..10} unique | An array of zero to ten names used to query an Actuator for its supported capabilities. |

**_Type: File (Map{1..*})_**

| ID | Name | Type | # | Description |
| ---: | :--- | :--- | ---: | :--- |
| 1 | **name** | String | 0..1 | The name of the file as defined in the file system |
| 2 | **path** | String | 0..1 | The absolute path to the location of the file in the file system |
| 3 | **hashes** | Hashes | 0..1 | One or more cryptographic hash codes of the file contents |


| Type Name | Type Definition | Description |
| :--- | :--- | :--- |
| **IDN-Domain-Name** | String /idn-hostname | Internationalized Domain Name, [[RFC5890]](#rfc5890), Section 2.3.2.3. |


| Type Name | Type Definition | Description |
| :--- | :--- | :--- |
| **IDN-Email-Addr** | String /idn-email | Internationalized email address, [[RFC6531]](#rfc6531) |

**_Type: IPv4-Net (Array /ipv4-net)_**

| ID | Type | # | Description |
| ---: | :--- | ---: | :--- |
| 1 | IPv4-Addr | 1 | **ipv4_addr**::IPv4 address as defined in [[RFC0791]](#rfc0791) |
| 2 | Integer | 0..1 | **prefix_length**::CIDR prefix-length. If omitted, refers to a single host address. |

**_Type: IPv4-Connection (Record{1..*})_**

| ID | Name | Type | # | Description |
| ---: | :--- | :--- | ---: | :--- |
| 1 | **src_addr** | IPv4-Net | 0..1 | IPv4 source address range |
| 2 | **src_port** | Port | 0..1 | source service per [[RFC6335]](#rfc6335) |
| 3 | **dst_addr** | IPv4-Net | 0..1 | IPv4 destination address range |
| 4 | **dst_port** | Port | 0..1 | destination service per [[RFC6335]](#rfc6335) |
| 5 | **protocol** | L4-Protocol | 0..1 | layer 4 protocol (e.g., TCP) - see [Section 3.4.2.10](#34210-l4-protocol) |

**_Type: IPv6-Net (Array /ipv6-net)_**

| ID | Type | # | Description |
| ---: | :--- | ---: | :--- |
| 1 | IPv6-Addr | 1 | **ipv6_addr**::IPv6 address as defined in [[RFC8200]](#rfc8200) |
| 2 | Integer | 0..1 | **prefix_length**::prefix length. If omitted, refers to a single host address. |

**_Type: IPv6-Connection (Record{1..*})_**

| ID | Name | Type | # | Description |
| ---: | :--- | :--- | ---: | :--- |
| 1 | **src_addr** | IPv6-Net | 0..1 | IPv6 source address range |
| 2 | **src_port** | Port | 0..1 | source service per [[RFC6335]](#rfc6335) |
| 3 | **dst_addr** | IPv6-Net | 0..1 | IPv6 destination address range |
| 4 | **dst_port** | Port | 0..1 | destination service per [[RFC6335]](#rfc6335) |
| 5 | **protocol** | L4-Protocol | 0..1 | layer 4 protocol (e.g., TCP) - [Section 3.4.2.10](#34210-l4-protocol) |


| Type Name | Type Definition | Description |
| :--- | :--- | :--- |
| **IRI** | String /iri | Internationalized Resource Identifier, [[RFC3987]](#rfc3987). |


| Type Name | Type Definition | Description |
| :--- | :--- | :--- |
| **MAC-Addr** | Binary /eui | Media Access Control / Extended Unique Identifier address - EUI-48 or EUI-64 as defined in [[EUI]](#eui). |

**_Type: Process (Map{1..*})_**

| ID | Name | Type | # | Description |
| ---: | :--- | :--- | ---: | :--- |
| 1 | **pid** | Integer{0..*} | 0..1 | Process ID of the process |
| 2 | **name** | String | 0..1 | Name of the process |
| 3 | **cwd** | String | 0..1 | Current working directory of the process |
| 4 | **executable** | File | 0..1 | Executable that was executed to start the process |
| 5 | **parent** | Process | 0..1 | Process that spawned this one |
| 6 | **command_line** | String | 0..1 | The full command line invocation used to start this process, including all arguments |


| Type Name | Type Definition | Description |
| :--- | :--- | :--- |
| **Properties** | ArrayOf(String){1..*} unique | A list of names that uniquely identify properties of an Actuator. |


| Type Name | Type Definition | Description |
| :--- | :--- | :--- |
| **URI** | String /uri | Uniform Resource Identifier, [[RFC3986]](#rfc3986). |


| Type Name | Type Definition | Description |
| :--- | :--- | :--- |
| **Date-Time** | Integer{0..*} | Date and Time |


| Type Name | Type Definition | Description |
| :--- | :--- | :--- |
| **Duration** | Integer{0..*} | A length of time |

**_Type: Feature (Enumerated)_**

| ID | Name | Description |
| ---: | :--- | :--- |
| 1 | **versions** | List of OpenC2 Language versions supported by this Actuator |
| 2 | **profiles** | List of profiles supported by this Actuator |
| 3 | **pairs** | List of supported Actions and applicable Targets |
| 4 | **rate_limit** | Maximum number of Commands per minute supported by design or policy |

**_Type: Hashes (Map{1..*})_**

| ID | Name | Type | # | Description |
| ---: | :--- | :--- | ---: | :--- |
| 1 | **md5** | Binary /x | 0..1 | MD5 hash as defined in [[RFC1321]](#rfc1321) |
| 2 | **sha1** | Binary /x | 0..1 | SHA1 hash as defined in [[RFC6234]](#rfc6234) |
| 3 | **sha256** | Binary /x | 0..1 | SHA256 hash as defined in [[RFC6234]](#rfc6234) |


| Type Name | Type Definition | Description |
| :--- | :--- | :--- |
| **Hostname** | String /hostname | Internet host name as specified in [[RFC1123]](#rfc1123) |


| Type Name | Type Definition | Description |
| :--- | :--- | :--- |
| **IDN-Hostname** | String /idn-hostname | Internationalized Internet host name as specified in [[RFC5890]](#rfc5890), Section 2.3.2.3. |


| Type Name | Type Definition | Description |
| :--- | :--- | :--- |
| **IPv4-Addr** | Binary /ipv4-addr | 32 bit IPv4 address as defined in [[RFC0791]](#rfc0791) |


| Type Name | Type Definition | Description |
| :--- | :--- | :--- |
| **IPv6-Addr** | Binary /ipv6-addr | 128 bit IPv6 address as defined in [[RFC8200]](#rfc8200) |

**_Type: L4-Protocol (Enumerated)_**

| ID | Name | Description |
| ---: | :--- | :--- |
| 1 | **icmp** | Internet Control Message Protocol - [[RFC0792]](#rfc0792) |
| 6 | **tcp** | Transmission Control Protocol - [[RFC0793]](#rfc0793) |
| 17 | **udp** | User Datagram Protocol - [[RFC0768]](#rfc0768) |
| 132 | **sctp** | Stream Control Transmission Protocol - [[RFC4960]](#rfc4960) |

**_Type: Payload (Choice)_**

| ID | Name | Type | # | Description |
| ---: | :--- | :--- | ---: | :--- |
| 1 | **bin** | Binary | 1 | Specifies the data contained in the artifact |
| 2 | **url** | URI | 1 | MUST be a valid URL that resolves to the un-encoded content |


| Type Name | Type Definition | Description |
| :--- | :--- | :--- |
| **Port** | Integer{0..65535} | Transport Protocol Port Number, [[RFC6335]](#rfc6335) |

**_Type: Response-Type (Enumerated)_**

| ID | Name | Description |
| ---: | :--- | :--- |
| 0 | **none** | No response |
| 1 | **ack** | Respond when Command received |
| 2 | **status** | Respond with progress toward Command completion |
| 3 | **complete** | Respond when all aspects of Command completed |


| Type Name | Type Definition | Description |
| :--- | :--- | :--- |
| **Rule-ID** | Integer | Access rule identifier |

**_Type: P-Args (Map{1..*})_**

| ID | Name | Type | # | Description |
| ---: | :--- | :--- | ---: | :--- |
| 1024 | **drop_process** | Drop-Process | 0..1 | Specifies how to handle denied packets |
| 1025 | **persistent** | Boolean | 0..1 | Normal operations assume any changes to a device are to be implemented persistently. Setting the persistent modifier to FALSE results in a change that is not persistent in the event of a reboot or restart |
| 1026 | **direction** | Direction | 0..1 | Specifies whether to apply rules to incoming or outgoing traffic. If omitted, rules are applied to both |
| 1027 | **insert_rule** | Rule-ID | 0..1 | Specifies the identifier of the rule within a list, typically used in a top-down rule list |

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

**_Type: P-Actuator (Map)_**

| ID | Name | Type | # | Description |
| ---: | :--- | :--- | ---: | :--- |
| 1 | **hostname** | String | 0..1 | RFC 1123 hostname (can be a domain name or IP address) for a particular device with SLPF functionality |
| 2 | **named_group** | String | 0..1 | User defined collection of devices with SLPF functionality |
| 3 | **asset_id** | String | 0..1 | Unique identifier for a particular SLPF |
| 4 | **asset_tuple** | String | 0..10 | Unique tuple identifier for a particular SLPF consisting of a list of up to 10 strings |

**_Type: P-Args$acme (Map{1..*})_**

| ID | Name | Type | # | Description |
| ---: | :--- | :--- | ---: | :--- |
| 1 | **firewall_status** | Status$acme | 0..1 |  |

**_Type: Status$acme (Enumerated)_**

| ID | Name | Description |
| ---: | :--- | :--- |
| 0 | **off** |  |
| 1 | **on** |  |

**_Type: P-Args$myco (Map{1..*})_**

| ID | Name | Type | # | Description |
| ---: | :--- | :--- | ---: | :--- |
| 1 | **debug_logging** | Boolean | 0..1 |  |

**_Type: P-Actuator$myco (Map{1..*})_**

| ID | Name | Type | # | Description |
| ---: | :--- | :--- | ---: | :--- |
| 1 | **asset_id** | UUID | 0..1 |  |

**_Type: P-Args$myco2 (Map{1..*})_**

| ID | Name | Type | # | Description |
| ---: | :--- | :--- | ---: | :--- |
| 1 | **debug_logging** | Boolean | 0..1 |  |

**_Type: P-Args$example (Map{1..*})_**

| ID | Name | Type | # | Description |
| ---: | :--- | :--- | ---: | :--- |
| 1 | **async** | Boolean | 0..1 |  |
| 2 | **webhook_id** | UUID | 0..1 |  |

**_Type: P-Args$395 (Map{1..*})_**

| ID | Name | Type | # | Description |
| ---: | :--- | :--- | ---: | :--- |
| 1 | **debug_logging** | Boolean | 0..1 |  |

**_Type: P-Actuator$esm (Map)_**

| ID | Name | Type | # | Description |
| ---: | :--- | :--- | ---: | :--- |
| 1 | **asset_id** | String | 0..1 | Unique identifier for a particular SLPF |

**_Type: Acme-Features (Map)_**

| ID | Name | Type | # | Description |
| ---: | :--- | :--- | ---: | :--- |
| 1 | **features** | Acme-Feature-List | 1 |  |


| Type Name | Type Definition | Description |
| :--- | :--- | :--- |
| **Acme-Feature-List** | ArrayOf(Acme-Feature) |  |

**_Type: Acme-Feature (Enumerated)_**

| ID | Name | Description |
| ---: | :--- | :--- |
| 1 | **versions** | List of OpenC2 Language versions supported by this Actuator |
| 2 | **profiles** | List of profiles supported by this Actuator |
| 3 | **pairs** | List of supported Actions and applicable Targets |
| 4 | **rate_limit** | Maximum number of Commands per minute supported by design or policy |
| 5 | **schema** | Actuator Schema |

**_Type: Acme-Container (Record)_**

| ID | Name | Type | # | Description |
| ---: | :--- | :--- | ---: | :--- |
| 1 | **container_id** | UUID | 1 |  |


| Type Name | Type Definition | Description |
| :--- | :--- | :--- |
| **UUID** | String |  |
