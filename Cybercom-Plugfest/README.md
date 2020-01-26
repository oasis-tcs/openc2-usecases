# OpenC2 Plugfest / Hackathon

Table of Contents:
- [1. About](#1-about)
- [2. Is it Plugfest or Hackathon? BOTH!](#2-is-it-plugfest-or-hackathon-both)
- [3. Who is attending?](#3-who-is-attending)
- [4. What usecases addressed?](#4-what-usecases-addressed)
  * [4.1 DoD Comply to Connect](#41-dod-comply-to-connect)
  * [4.2 Fill-in-the-blank Comply to Connect](#42-fill-in-the-blank-comply-to-connect)
  * [4.3 sFractal IoT Single Packet Authentication](#43-sfractal-iot-single-packet-authentication)
  * [4.4 others go here](#44-add-more-here)
- [5. Oasis OpenC2 wrt Plugfest/Hackathon](#5-oasis-openc2-wrt-plugfesthackathon)
- [6. Info for Participants](#6-info-for-participants)
  * [6.1 OpenC2 Plugfest Planning](#61-openc2-plugfest-planning)
  * [6.2 Lessons learned from previous plugfests](#62-lessons-learned-from-previous-plugfests)
  * [6.3 About The Facility](#63-about-the-facility)
  * [6.4 FAQ](#64-faq)
- [7. Resources](#7-resources)
- [8. Outcomes / Post Mortem](#8-outcomes--post-mortem)

## 1. About

OpenC2 is a recently released suite of OASIS specifications that define a standard language for command and control of cyber defense technologies.
The [OpenC2 Technical Committee](https://www.oasis-open.org/committees/openc2) (TC) 
is running a plug fest / hackathon on 27-28 January 2020, sponsored by US Cyber Command 
and hosted in the nearby [UMBC Training](https://umbctraining.com/) facility in Columbia, MD.
The Plug Fest is open to interested participants, regardless of whether they are OASIS members. 
The UMBC facility and the Plug Fest are unclassified, and there is no restriction to U.S. organizations or individuals.

Further details and registration information can be found at DreamPort: https://dreamport.tech/event-open-c2-plug-fest-01272820.php

A [Google Maps link](https://www.google.com/maps/place/UMBC+Training+Centers/@39.177432,-76.8033375,17z/data=!3m1!4b1!4m5!3m4!1s0x89b7e0f2a23f6065:0x6211ab036d384b90!8m2!3d39.177432!4d-76.8011488)
for the UBMC Training facility

Integrate once, reuse everywhere.
Stop having to know the
syntax of each different product that’s involved in
today’s complex, multivendor, security operations environment.
OpenC2 commoditizes the command and control (C2)
allowing security teams to automate an orchestrated response
more efficiently, as well as avoiding vendor lock-in.

A goal of the Plug Fest is to execute use cases using OpenC2 and gather lessons learned about interoperability.
The plugfest aspect is for testing interworking of existing OpenC2 implementations. Let us know what you have and we will work your implementation into the test plans.
The hackathon aspect is for improving the interworking of existing OpenC2 implementations,  extending existing implementations (e.g., the many OpenC2 open source projects), and/or creating new implementations of OpenC2.

The plugfest is not a meeting of the OASIS OpenC2 Technical Commmittee. It does not count towards voting rights for members of the OpenC2 TC. No work will be done on the OpenC2 specifications themselves
although OpenC2 members are welcome to bring inspirations or suggestions from the plugfest to the TC.

## 2. Is it Plugfest or Hackathon? BOTH!
It is both a plugfest (testing interoperability of existing implementations)
and a hackathon (writing software to meet a need).
Come prepared to participate in either or both.

## 3. Who is attending?
Although it is not required to announce if you will be attending,
the hope is many will and include what they will be bringing to the table:
- AT&T
- Broadcom/Symantec
- DoD - Active Cyber Defense of Critical Infastructure (ACDCI)
- Fornetix
- GitHub - providing these [resources](sbom-github.md) for SBoMs and comply to connect
- Google - providing these [resources](cloud-google.md) to support plugfest
- NineFX
- Net Scout
- NSA - OpenC2 Integration Framework (OIF) [Orchestrator](https://github.com/oasis-open/openc2-oif-orchestrator) and [Device](https://github.com/oasis-open/openc2-oif-device)
- sFractal Consulting - 1 attendee ready to program in erlang, elixir, or python with the following resources:
  * [Iot Tests](tests-sFractal-IoT.md) - test rigs sFractal will be bringing to plugfest consisting of a bunch of preprogrammed Raspberry Pi's.
  * [IoT C2C](uc-sFractal-IoT-C2C.md) - IoT comply to connect use case
  * [IoT SPA](uc-sFractal-IoT-SPA.md) - Single Packet Authentication IoT use case
- UNCC
- University of Oslo

### Details

  | PARTICIPANT |  DESCRIPTION |  USE CASE |  FUNCTION/ ACTIONS |  CONSUMER OR PRODUCER |  POC |  LINK |
  |-------------|--------------|------------------|---------------------|----------|-----------|-----------|
  | AT&T | | Cloud based firewall use case | Commands TBD, but will include DENY and ALLOW | Both | Michael Stair||
  | BluVector | Determines the probability of a file being malicious (or benign) | | None at this time, but potential actions include SCAN, UPDATE| Consumer | Larry Gloss ||
  |BAE| | Unmanned Terrestrial Vehicle use case| TBS, this use case will investigate the use of CAN BUS message transport| TBD|Bridgette Townsend||
  | Clear Edge | Integration and System Engineering | | TBD | TBD | Producer ||
  |Clarity Cyber ||'Denver Airport'. This is an RF situational awareness use case consisting of unattended sensors, unmanned aerial vehicles and a controller. |Some of the functions include Detection of signals of interest, direction finding, jamming hostile signals.  The OpenC2 actions inlcude LOCATE< DENY, ALLOW, REPORT, SET, CONTAIN, INVESTIGATE| The team will focus on the OpenC2 consumers.  Will probably use the OIF orchestrator to produce commands| Mike Ridge||
  | ClearEdge | Integration and System Engineering | TBD | TBD | Producer |Tina Coleman (tcoleman@clearedgeit.com)||
  | Fornetix| Key Orchestration | The Orchestrator will send commands and receive responses from an entity that uses the KMIP standard to manage cypto systems.  From the OpenC2 perspective, the KMIP is the actuator and KMIP abstracts the actual key management from the orchestrator | CREATE, SET, DENY, ALLOW | Both | TBA | |
  | GitHub | Provides information on open source dependencies and other information contained within a software bill of materials |Supports software bill of materials for Comply to connect use  case | None at this time, but potential actions include QUERY | Consumer| Brendan O'Connor||
  | GitHub | CodeQL: Analytic that queries code for a given vulnerabilty (and its variants)| | QUERY | Consumer | Xavier René-Corail||
  | Google | Google Cloud Platform and Cloud based firewall| NA| Cloud based firewall. Commands TBD but will include DENY and ALLOW | Consumer | Jason Callaway ||
  |JHU/APL | Integrator | MOSAIC| Will need QUERY, DENY, START, UPDATE, CREATE | Both |||
  | NSA | Agency within DOD | Comply to Connect | will need QUERY, SCAN, UPDATE, CONTAIN | NA| Joe Brule ||
  | NSA | OpenC2 Integration Framework (OIF)| Providing a platform for other's use cases| Various | Both | Danny Martinez ||
  |s-fractal|Test rigs sFractal will be bringing to plugfest consisting of a bunch of preprogrammed Raspberry Pi's to be IoT devices| usecases documented at https://github.com/oasis-tcs/openc2-usecases/blob/master/Cybercom-Plugfest/tests-sFractal-IoT.md, https://github.com/oasis-tcs/openc2-usecases/blob/master/Cybercom-Plugfest/uc-sFractal-IoT-C2C.md, https://github.com/oasis-tcs/openc2-usecases/blob/master/Cybercom-Plugfest/uc-sFractal-IoT-SPA.md | QUERY, ALLOW | Consumer| Duncan Sparrell||
  | Symantec| Multiple Cyber Security Products | Endpoint Remediation | OpenC2 Integrated in the ICDX product|Consumer| Brian Berliner||
  |United States Army | Unattended sensors, UAV and UTV platforms| RF situational awareness and response| TBD. SOme of hte actions include: SCAN, DELETE, CREATE, LOCATE, DENY, ALLOW. Some of the actuators include RF Transmitter (jamming signals), RF receivers (collect signals of interest) Key management, laser blinders, analytic engines (determine line of bearing) | Both| Mike Ridge||
  |University of Oslo| Academia | Firewalls & Coordinated Response | Implemented the SLPF version 1.0 into the [iosacl-adapter](https://github.com/oasis-open/openc2-iosacl-adapter) for command and control of Cisco ACLs| Both |Vasileios Mavroeidis|[PoC](https://github.com/oasis-open/openc2-iosacl-adapter) and [Plugfest Use Case](https://github.com/Vasileios-Mavroeidis/openc2-plugfest/tree/master/2020-January)|



## 4. What use cases are addressed?
It is not required, but hoped, that attendees will publish use cases of interest
prior to arriving.
One of the first orders of business will be a brainstorming session
to make this list as complete as possible for meeting the attendees needs.
Immediately following will be scheduling out what to work on during the two days.

### 4.1 DoD Comply to Connect
The DoD CIO and the Chief of CYBERCOM have been tasked (Public Law 114-328-DEC. 23, 2016 Sec 1653) with creating a ‘comply to connect’ policy for all DoD networked devices. They consider a software inventory (termed a Software Bill of Materials or SBOM in many industries. See http://ntia.gov/sbom) an integral part of ‘comply to connect’ since you can’t claim compliance if you don’t know what software is present.
The use case continues with various actions to be taken based on analyzing the SBoM.
See [here](uc-A-comply-to-connect.md) for more info.

### 4.2 Fill-in-the-blank Comply to Connect
"Fill-in-the-blank comply to connect" is a set of usecases for other industries that have similar needs to the DoD use case above. The differences will be in the policy in what the 'acceptance' criteria are and what actions will be taken. The common aspect is a request for a SBoM. In some cases the acceptance criteria may be simply that one exists. In another it may be that it is complete and no known CVE's with CVSS>7 are present. Etc. The DoD use case has a set of actions to be taken that other usecases may use a subset of, or may have unique actions of it's own.

One area that where comply-to-connect has been receiving more attention is healthcare.
Wannacry caused serious hospital outages in the UK.
Even thought the health impact was less in the US, there was still significant
resources expended in determining whether it would be an impact.
In another healhcare area, the US FDA has given pre-market guidance (govspeak for "do this or we won't approve you") to medical device makers that SBoMs are required.
OpenC2 offers one mechanism to retrieve the SBoM for use in either of these cases (vulnerability assessment ala Wannacry or regulatory compliance ala FDA).

Supply chain transparency for software is also receiving increased attention in both automotive and pubic transport.

include manufacturing scenario

include industrial actuator being added scenario

include ISP/CSP scenario

include sFractal home/small-business scenarios

### 4.3 sFractal IoT Single Packet Authentication
See [here](uc-sFractal-IoT-SPA.md) for the Single Packet Authentication usecase proposed by sFractal.

### 4.4 Firewall Configuration and Management

- University of Oslo: The use case of UiO includes a prototype implementation of the OASIS OpenC2 SLPF version 1.0 with the purpose of controling Access Control Lists (firewall capability) in Cisco devices (e.g., routers, L3 switches, firewalls). In their use case a Cisco Cloud Service Router (CSR1000V with Cisco IOS XE Software, Version 16.12.01a) in the Google Cloud Platform is controlled. The use case is available [HERE](https://github.com/Vasileios-Mavroeidis/openc2-plugfest/tree/master/2020-January). The PoC is available [HERE](https://github.com/oasis-open/openc2-iosacl-adapter). In their use case, an idea of how to enable coordinated response via OpenC2 is presented, even though it is out of OpenC2 scope (at this moment).


### 4.5 add more here
others are free to put their needs here

## 5. OASIS OpenC2 TC relationship to Plugfest/Hackathon
The OpenC2 plugfest/hackathon is open to all interested participants whether OASIS members or not, and therefore is NOT a meeting of the Technical Committee itself. The OASIS rules governing TC meetings, including provisions of the OASIS IPR policy, do not apply and any outputs from the event are not 'contributions' as defined in OASIS rules. Members of the TC who wish to formally contribute any outputs from the event to the TC must (as with any contribution) be sure that they have sufficient rights in the material to do so.

OASIS and the OpenC2 TC welcome participation by all interested parties. Participants who are not OASIS members but are interested in joining in the work being done by the TC are welcome to contact the event chairs for information on the opportunities available.

## 6. Info for Participants
The slide decks from the Nov 5th prep meeting
(attended by ~35 participants including ~7 OpenC2 TC members)
for the Dreamport Plugfest/hackathon are posted at OASIS

* **OpenC2 & Plug Fest Overview and Resources** (Joe Brule / David Lemire)  
https://www.oasis-open.org/committees/document.php?document_id=66231&wg_abbrev=openc2  

* **Symantec ICDx 1.3.1** (Brian Berliner)  
https://www.oasis-open.org/committees/document.php?document_id=66232&wg_abbrev=openc2  

* **MOSAICS ICS Use Case** (Harley Parkes)  
https://www.oasis-open.org/committees/document.php?document_id=66233&wg_abbrev=openc2  

* **Tesla Powerwall Proxy** (Efrain Ortiz)  
https://www.oasis-open.org/committees/document.php?document_id=66234&wg_abbrev=openc2  

* **OpenC2 and KMIP** (Chuck White)  
https://www.oasis-open.org/committees/document.php?document_id=66235&wg_abbrev=openc2

Note: There were no slides for Mike Ridge's presentation of a use case for RF monitoring at the Denver Airport.

The DreamPort calendar announcement is at
https://dreamport.tech/event-open-c2-plug-fest-01272820.php
with links to registration.

OASIS has created a new mail list for the plug fest, openc2-plugfest-2019@lists.oasis-open.org. The list is open to interested parties regardless of OASIS or TC membership. There is no archive for the plug fest mail list.

Registration for the event is at https://dreamport.tech/registration-open-c2-plug-fest-0120.php.

Please do a pull request against this page and add yourself to participants section

Information about DreamPort:  https://dreamport.tech/about-us.php

Information about UMBC Training:  https://umbctraining.com/

https://github.com/oasis-open?utf8=%E2%9C%93&q=openc2-&type=&language= are some
of the OpenC2 open source repositories.

https://www.oasis-open.org/news/announcements/three-committee-specifications-approved-by-open-command-and-control-openc2-tc has info on the specifications themselves.

### 6.1 OpenC2 Plugfest Planning

As discussed at the 18 September TC meeting OpenC2 has been offered the opportunity to run a plug fest hosted
by US Cyber Command in their public, unclassified DreamPort facility. TC members are encouraged to consider
participation in this event, tentatively planned for the week of 27 January 2020.

TC chair's initial request (19 Sept) for plug fest participation:
https://lists.oasis-open.org/archives/openc2/201909/msg00009.html

TC chair's request (25 Sept) for plug fest use cases and related information:
https://lists.oasis-open.org/archives/openc2/201909/msg00015.html


### 6.2 Lessons Learned from Previous Plugfests
The CTI TC published lessons learned from their STIX plugfest, which
included:

**Issue:** Lack of stable/validated schema and data sets that can be used for all clients and servers

**Action:**
* Define and maintain a package of downloadable JSON schema and test data that all plugfest/interop participants can use before plugfest.
* Need common sets of data for all to use for testing.
* Need sets of data that are unique to vendors or use cases that help provide more robust testing.

This repository includes use case descriptions, schemas, and test data (good and bad) for use by participants prior to the event.

### 6.3 About The Facility

The UMBC Training facility we'll be using has allocated us two rooms, 
each of which can accommodate 30-35ish people. We'll have tables & chairs, 
white boards, flip-chart easels, and wireless and wired network connections 
with Internet access to support our efforts. We are arranging 10-12 monitors 
to assign to tables for display purposes (but you can also bring one if you wish).

The facility has a nice break room with beverages and snacks (and pretty good coffee). 
There is plenty of (free) parking. Note that the facility entrance is on the side 
away from Columbia Gateway Drive, facing inward toward the shared parking lot. 
And there are plenty of restaurants nearby for lunch. 

### 6.4 FAQ
- Will WiFi be provided? More than one SSID? What networking details?
  * The UMBC facility provides a single WiFi network that will be readily
  accessible to plug fest participants.
- Will wired ethernet be provided? More than one network? What networking details?
  * The UMBC facility is providing wired Ethernet drops and switches for each of the two
  rooms allocated for our event. The WiFi and the wired Ethernet are all on the same LAN.
- DHCP or Static IP or choice-of-either? Will IP addresses (or at least ranges) be available prior to arriving to allow preconfiguration (eg only allow access from these ranges)
  * UMBC is mapping public ports to static LAN IPs sufficient to connect to 20 devices on ports 80 and 443.
- IPV4? IPV6?
  * IPv4 has been tested.  If anyone actually requires IPv6 please speak up and we'll see if it's available.
- Will our devices be able to reach the internet? Will IPs/ports need to be prearranged to get thru firewalls?
  * The facility freely permits outbound traffic to Internet sites, and this has been tested by NSA OpenC2 team.
  No special prearrangements are required.
- Will our devices be reachable from the internet? Will IPs/ports need to be prearranged to get thru firewalls?
  * See above; support for 20 devices has been arranged. More can be added if there is demand.
- Will whiteboards be provided?
  * One room has "whiteboard walls", the other room has some whiteboards; there are also flip-chart easels.
- Will projector be provided?
  * There is a project and screen in one room; the NSA OpenC2 team is also arranging for a monitor per
  work table for display purposes.
- Will certificates be needed for interworking (e.g., for HTTPS mutual authentication)? If so - how arrange?
  * Nothing has been arranged to supply certificates at this time.

## 7. Resources
Plugfest Preparation:
- add stuff

More on potential test scenarios and code-writing sessions:
- add page

Approved OpenC2 Specifications:
- https://docs.oasis-open.org/openc2/oc2ls/v1.0/cs01/oc2ls-v1.0-cs01.html - Open Command and Control (OpenC2) Language Specification Version 1.0 (need to update this with errata once link is published)
- https://docs.oasis-open.org/openc2/oc2slpf/v1.0/cs01/oc2slpf-v1.0-cs01.html - Open Command and Control (OpenC2) Profile for Stateless Packet Filtering Version 1.0 (need to update this with errata once link is published)
- https://docs.oasis-open.org/openc2/oc2slpf/v1.0/cs01/oc2slpf-v1.0-cs01.html - Open Command and Control (OpenC2) Profile for Stateless Packet Filtering Version 1.0 (need to update this with errata once link is published)

OpenC2 Specifications in progress:
- https://docs.google.com/document/d/1yfiZJLL0S7ENu4RMdSVrWmsetlvFUMN2LZwjZ_3bXg0 - Specification for Transfer of OpenC2 Messages via CoAP
- https://github.com/oasis-tcs/openc2-transf-odxl - OpenC2 over OpenDxl spec
- https://github.com/oasis-tcs/openc2-transf-mqtt - OpenC2 over MQTT spec
- https://github.com/oasis-open/openc2-custom-aps - Customer Actuator Profiles for anti-malware, email gateway, stateful packet filter. CAPs are precusors to AP specs
- https://github.com/oasis-open/openc2-iosacl-adapter - tool for converting Cisco Ios commands to OpenC2 commands. Not a spec per se but content will lead to stateful firewall AP specs

OpenC2 opensource
- https://github.com/oasis-tcs?utf8=%E2%9C%93&q=openc2&type=&language= are the "TC" repos (ie open for view to all but only editable by TC members) that contain the markdown versions of the approved specifications as well as work in progress
- https://github.com/oasis-open?utf8=%E2%9C%93&q=openc2-&type=&language= are the "Open" repos (ie plain old open source that anyone can contribute to)
- https://github.com/OpenC2-org/other-openc2-work is a list of OpenC2 open source that is not hosted on OASIS.

For more information about OASIS OpenC2 TC:
- https://www.oasis-open.org/committees/tc_home.php?wg_abbrev=openc2 is the TC public page. Note all work of OASIS is open (ie viewable).
- https://www.oasis-open.org/apps/org/workgroup/openc2/members/roster.php is the current roster
- Next OpenC2 TC meeting is Wednesday 18-December-2019 at 11AM and 9PM Eastern. The two times are to accomadate worldwide attendance and either may be attended.
- Contact join@oasis-open.org for more information on joining OASIS OpenC2 TC.
- https://docs.google.com/document/d/1Bz_WXOiYc9vmMS8rNEP1-ZZgPzdeGoZMN6W5W9GSmdU/edit?usp=sharing is a one-stop-shop google doc of appropriate link
- Various news and blogs about openc2
  * https://www.hardenstance.com/a-new-window-into-an-openc2-world/
  * https://www.csoonline.com/article/3386161/openc2-can-accelerate-security-operations-automation-and-orchestration.html
  * https://www.youtube.com/watch?v=kCooyNJoOrU
  * https://www.youtube.com/watch?v=HjMm_6mWePw
  * https://www.cyberscoop.com/openc2-nsa-open-source-cyber-defense/

For more information about DreamPort:
- https://dreamport.tech

For more information about DoD Comply to Connect:
- add links

For more information about SBoM (in Comply2Connect usecases):
- https://www.ntia.gov/sbom - NTIA Software Transparency Multistakeholder workgroup
  + https://www.ntia.gov/files/ntia/publications/framingsbom_20191112.pdf - Framing Software Component Transparency: Establishing a Common Software Bill of Material (SBOM)
  + https://www.ntia.gov/files/ntia/publications/ntia_sbom_use_cases_roles_benefits-nov2019.pdf - Roles and Benefits of SBoM Across the Supply Chain
  + https://www.ntia.gov/files/ntia/publications/ntia_sbom_formats_and_standards_whitepaper_-_version_20191025.pdf - Survey of Existing SBOM Formats and Standards
  + https://www.ntia.gov/files/ntia/publications/ntia_sbom_healthcare_poc_report_2019_1001.pdf - Healthcare Proof of Concept Report




## 8. Outcomes / Post Mortem
This section is for after the plugfest to document the outcomes relevant to
the OASIS OpenC2 TC. Reminder to review intellectual property considerations
prior to entering data here,
particularly for input from non-TC members
since they are not bound by sharing agreement.
