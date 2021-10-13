# sFractal Goals & Objectives

Table of Contents
- [1-Introduction](#1-introduction)
- [2-Goals & Objectives](#2-goals-objectives)
   -  [2.1-OpenC2 Virtual Plugfest/Hackathon Goals & Objectives](2.1-openc2-virtual-plugfest-hackathon-goals-objectives)
   - [2.2-NTIA SBOM Exchange PoC Goals & Objectives](2.2-ntia-sbom-exchange-poc-goals-objectives)
   - [2.3-IACD Goals & Objectives](2.3-iacd-goals-objectives)
   - [2.4-CACAO Goals & Objectives](2.4-cacao-goals-objectives)
   - [2.5-Open Cybersecurity Alliance Goals & Objectives](2.5-open-cybersecurity-alliance-goals-objectives)
   - [2.6-Erlang Ecosystem Foundation Security Working Group Goals & Objectives](2.6-erlang-ecosystem-foundation-security-working-group-goals-objectives)
   - [2.7-SCAPv2 Goals](2.7-scapv2-goals)
- [3-sFractal Contributions to PoC](3-sfractal-contributions-to-poc)

## 1-Introduction

sFractal Consulting is just Duncan - whose overarching goal is just
to make the world a safer place, which all these efforts do.

## 2-Goals & Objectives

### 2.1-OpenC2 Virtual Plugfest/Hackathon Goals & Objectives
- prepare for physical-in-person [plugfest/hackathon in Oct at TTD](../TTD-PlugfestHackathon)
- show the value of virtual plugfest/hackathons
- develop [blinkyhaha](https://github.com/sparrell/BlinkyHaHa)
- interwork [blinkyhaha](https://github.com/sparrell/BlinkyHaHa) with as many other platforms as possible
- create several versions of [blinkyhaha](https://github.com/sparrell/BlinkyHaHa) SBOM
   - one hop
   - complete
   - "good"
- using both "good" and "vulnerable" SBOMs, show the value of the SBOM by using orchestration to 'connect' the 'good' SBOM while "fixing" or "sandboxing" the vulnerable devices with the vulnerable SbomG
- show how OpenC2 can be used for SBOM transfer
- show how OpenC2 can be used to command and control security functionality
- evangelize OpenC2 to the other groups involved
- validate and verify the blinkhaha opensource code for OpenC2 interface
- validate and verify the blinkhaha opensource code for SBOM
- validate and verify the blinkhaha opensource code for OpenC2 HTTPS Spec
   - develop the certs etc to allow this to work securely correctly
- validate and verify the blinkhaha opensource code for OpenC2 HTTP Spec
- develop, validate and verify the blinkhaha opensource code for OpenC2 MQTT Spec
- validate and verify the OpenC2 SBOM Actuator Profile Specifications
- validate and verify the OpenC2 HTTP, HTTPS, MQTT Specifications

### 2.2-NTIA SBOM Exchange PoC Goals & Objectives
- "Prove" the concept of SBOM exchange using OpenC2 as transport when the device has SBOM resident within device and device has OpenC2 interface
- show the value of virtual plugfest/hackathons for Proof of concept
- using both "good" and "vulnerable" SBOMs, show the value of the SBOM by using orchestration to 'connect' the 'good' SBOM while "fixing" or "sandboxing" the vulnerable devices with the vulnerable SbomG
- evangelize SBOM to the other groups involved
- put out a report similar to https://www.ntia.gov/files/ntia/publications/ntia_sbom_healthcare_poc_report_2019_1001.pdf

### 2.3-IACD Goals & Objectives
[Integrated Adaptive Cyber Defense]() (IACD) is a strategy and framework to adopt an vendor-agnostic, extensible, adaptive, commercial off-the-shelf (COTS)-based approach to cybersecurity operations. IACD's goal is to dramatically change the timeline and effectiveness of cyber defense via integration, automation, orchestration and sharing of machine-readable cyber threat information.

Many of the OpenC2 goals are consistent with IACD goals.
Ideally CACAO would be used for playbooks which would also be in keeping with
IACD goals and the PoC could be made part of one of the IACD sprints.

### 2.4-CACAO Goals & Objectives
[Collaborative Automated Course of Action Operations](https://www.oasis-open.org/committees/tc_home.php?wg_abbrev=cacao)
(CACAO) is a specification for implementing course-of-action playbooks
for cybersecurity operations.
Ideally CACAO would be used for the security policy
driving the decision making in the automated response to the SBOM
as part of the PoC.
Goals for CACAO would include:
- show how CACAO can be used for automating decision making associated with SBOM handling (eg allow if a vulnerability free SBOM and deny/sandbox if SBOM non-existent, or incomplete/one-hop, or has known vulnerabilities)
- develop new CACAO use cases (eg for SBOM)
- validate and verify the CACAO Specifications

### 2.5-Open Cybersecurity Alliance Goals & Objectives
The [Open Cybersecurity Alliance](https://opencybersecurityalliance.org/) (OCA)
is an open cybersecurity ecosystem for vendor-agnostic interworking and data sharing
using open standards like STIX and OpenC2.
Ideally the PoC would include some OCA projects such as
[stix-shifter](https://github.com/opencybersecurityalliance/stix-shifter)
or [opendxl-ontology](https://github.com/opencybersecurityalliance/opendxl-ontology).
Maybe someone (hint  to IBM, hint to McAfee) would volunteer to incorporate
one or both of them as part of the decision loop.
Goals for OCA (should an OCA project be included) would be to
show vendor-agnostic interworking and data sharing
using open standards like STIX and OpenC2

### 2.6-Erlang Ecosystem Foundation Security Working Group Goals & Objectives
The Erlang Ecosystem Foundation (EEF, https://erlef.org/) is
a 501(c)(3) not-for-profit organization
dedicated to furthering state of the art for Erlang, Elixir, LFE and other technologies based on the BEAM.
The EEF Security Working Group
has within it's charter to 'Ensure supply chain security', of which SBOM creation
is one component.
sFractal's EEF goals are synonomous with the SBOM goals in 2.2
with an additional goals of:
- evangelizing BEAM for robust applications,
- evangelizing Nerves for IoT
- proving in SBOM tools in rebar3 and Hex build tools
- establishing base of SBOMs for common BEAM applications, at least those used in PoC like Nerves
- open source elixir code for OpenC2 interface

### 2.7-SCAPv2 Goals
- show value of SCAPv2
- show how SCAPv2 fits in IACD
- show how SCAPv2 fits in OCA
- show how OpenC2 can be used in SCAPv2 Scenarios
- show how SBOM can SCAPv2 data

## 3-sFractal Contributions to PoC
- evangelism of PoC to all the organizations sFractal is a member of (OASIS OpenC2 TC, NTIA SBOM, IACD, OASIS CACAO TC, Open Cybersecurity Alliance, Erlang Ecosystem Foundation Security Working Group)
- blinkyhaha software development as test IoT device
- blinkyhaha SBOM creation - one-hop, complete, and various 'vulnerable' SBOMs to drive different behaviours by orchestrators
- interworking/integration with whatever willing to talk to blinkyhaha
- effort in support of meeting all the goals in [Section 2](#2-goals-objectives)
- work with One Planet Education Network on sensors and on education aspects
