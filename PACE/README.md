# Posture Attribute Collection and Evaluation (PACE) Prototype

## Overview

**Posture Attribute Collection and Evaluation (PACE)** is an
[Open Cybersecurity Alliance
(OCA)](https://opencybersecurityalliance.org/) project. Posture
assessment generally consists of understanding, for a given
computing resource (or set of computing resources), software
load, composition of that software load, patch levels,
vulnerability (implied to be software vulnerability), and
configuration state. Together, these attributes of a computing
resource represent its cybersecurity posture. PACE will leverage
and/or contribute to Open Cybersecurity Alliance (OCA) Ontology
and OpenC2 for command and control. PACE will be an instantiation
of the IETF Security Automation and Continuous Monitoring (SACM)
group’s architecture.

Initially, the project intends to focus on building the pipes and connectors between components, leveraging existing payload formats such as SCAP/OVAL, SBOM, etc. Later phases of the project may consider updating payload formats to include other types (i.e. NETCONF/RESTCONF, InSpec, Puppet, Ansible, etc.)

## Status

As of October 2021, the PACE prototyping effort is focused on
implementing a version of the [**Security Automation and
Continuous Monitoring
(SACM)**](https://datatracker.ietf.org/wg/sacm/documents/)
architecture documented in [this Internet
Draft](https://datatracker.ietf.org/doc/draft-ietf-sacm-arch/)
(expires January 2022). The draft focuses on capabilities for
*collection* and *evaluation* of "security posture attributes",
and uses [RFC 7632, *Endpoint Security Posture Assessment:
Enterprise Use
Cases*](https://datatracker.ietf.org/doc/rfc7632/), as a
reference. Current PACE efforts are prototyping posture attribute
collection using open source tools such as
[osquery](https://osquery.io/) and [nmap](https://nmap.org/),
using OpenC2 to control collection activities. An OpenC2 Actuator
Profile (AP) for Security Posture Attribute Collection is an
anticipated product of this work. 

## Documentation

Documentation related to PACE protoptyping is maintained in the
OCA [PACE](https://github.com/opencybersecurityalliance/PACE)
GitHub respository. The following documents help to illustrate
SACM concepts, their connection to OpenC2, and the initial
direction of the PACE protoptying effort, along with possible
future use cases that could be implemented.

 * [SACM and OpenC2
   Concept](https://github.com/opencybersecurityalliance/PACE/blob/main/docs/SACM_and_OpenC2_Concept.pdf)
   starts from the high level SACM architecure contained in the
   Internet Draft and illustrates a concept for applying OpenC2
   to its implemenation. This concept document also illustrates a
   potential use for the presently-undefined OpenC2 notification
   message concept.
  
 * The [18 October 2021 Status
   Update](https://github.com/opencybersecurityalliance/PACE/blob/main/docs/2021-10-18_HII_PACE-Prototype-Update.pdf)
   illustrates messages flows and gives an overview of the
   prototyping network environment.

 * The repository includes use cases to illustrate [prioritizing
   intrustion
   alerts](https://github.com/opencybersecurityalliance/PACE/blob/main/docs/ips-pcs-pes-usecase.md)
   and [theat
   hunting](https://github.com/opencybersecurityalliance/PACE/blob/main/docs/stix-pcs-pes-usecase.md)
   triggered by a indicator received as a
   [STIX](https://oasis-open.github.io/cti-documentation/stix/intro.html)
   [Cyber Observable
   object](https://docs.oasis-open.org/cti/stix/v2.0/stix-v2.0-part4-cyber-observable-objects.html).

Information contained in the OCA
[documentation](https://github.com/opencybersecurityalliance/documentation)
repository may also be helpful.

The PACE prototyping work will likely also include the retrieval
of [Software Bill of Materials
(SBOM)](https://en.wikipedia.org/wiki/Software_bill_of_materials)
objects that play a role in various cybersecurity scenarios, such
as this vision for a [Comply to Connect
implementation](https://github.com/oasis-tcs/openc2-usecases/tree/main/PlugFests/2021.06.22-BC-SBOM-PoC#11-vision)
captured for a previous OpenC2 plugfest.

The PACE prototyping effort is a conceptual successor to
prototyping previously done related to the [Security Content
Automation Protocol,
v2](https://csrc.nist.gov/projects/security-content-automation-protocol-v2/scapv2-community).

