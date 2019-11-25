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
- [7. Resources](#7-resources)
- [8. Outcomes / Post Mortem](#8-outcomes--post-mortem)

## 1. About

OpenC2 is a recently released suite of OASIS specifications that define a standard language for command and control of cyber defense technologies.
OpenC2 will be running a plug fest / hackathon 27-28 January 2020, hosted by US Cyber Command in their public, unclassified DreamPort facility in Columbia, MD.
The Plug Fest is open to interested participants, regardless of whether they are OASIS members. The DreamPort facility and the Plug Fest are unclassified, and there is no restriction to U.S. organizations or individuals.
Further details and registration information can be found at DreamPort: https://dreamport.tech/event-open-c2-plug-fest-01272820.php

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

The plugfest is NOT an OpenC2 meeting for creating/modifying the OpenC2 specifications,
although obviously OpenC2 members are welcome to bring suggestions
back to OASIS official meetings.

## 2. Is it Plugfest or Hackathon? BOTH!
This is both a plugfest (testing interoperability of existing implementations)
and a hackathon (writing software to meet a need).
Come prepared to participate in either or both.

## 3. Who is attending?
Although it is not required to announce if you will be attending,
the hope is many will and include what they will be bringing to the table:
- AT&T
- Broadcom/Symantec - ok to put? will you bring ICDX?
- Fornetix
- HII-MDIIS/G2 -ok to put? what bringing? What company name?
- GitHub - put link to new page with plugfest resources they are providing
- Google - put link to new page with plugfest resources they are providing
- NineFX
- Net Scout
- NSA - put link to what bringing
- sFractal Consulting - blah blah and link to page describing raspberry pi's configs that are being brought by sFractal
- UNCC

## 4. What usecases addressed?
It is not required, but hoped, that attendees will publish use cases of interest
prior to arriving.
One of the first orders of business will be a brainstorming session
to make this list as complete as possible for meeting the attendees needs.
Immediately following will be scheduling out what to work on during the two days.

### 4.1 DoD Comply to Connect
The DoD CIO and the Chief of CYBERCOM have been tasked (Public Law 114-328-DEC. 23, 2016 Sec 1653) with creating a ‘comply to connect’ policy for all DoD networked devices. They consider a software inventory (termed a Software Bill of Materials or SBOM in many industries. See http://ntia.gov/sbom) an integral part of ‘comply to connect’ since you can’t claim compliance if you don’t know what software is present.
The use case continues with various actions to be taken based on analyzing the SBoM.
See LINKHERE for more info.

### 4.2 Fill-in-the-blank Comply to Connect
"Fill-in-the-blank comply to connect" is a set of usecases for other industries that have similar needs to the DoD use case above. The differences will be in the policy in what the 'acceptance' criteria are and what actions will be taken. The common aspect is a request for a SBoM. In some cases the acceptance criteria may be simply that one exists. In another it may be that it is complete and no known CVE's with CVSS>7 are present. Etc. The DoD use case has a set of actions to be taken that other usecases may use a subset of, or may have unique actions of it's own.

include ref 4 links to ntia docs

blah blah on other several healthcare usecases

include transportation procurement scenario

include manufacturing scenario

include industrial actuator being added scenario

include ISP/CSP scenario

include sFractal home/small-business scenarios

### 4.3 sFractal IoT Single Packet Authentication
put in link to page and a quick overview there

### 4.4 add more here
others are free to put their needs here

## 5. Oasis OpenC2 wrt Plugfest/Hackathon
blah blah on it is open to all and therefore NOT an OASIS meeting where OASIS
intellectual property sharing rules apply.
Get better wording from Chet

## 6. Info for Participants
The slide decks from the Nov 5th prep meeting
(attended by ~35 participants including ~7 OpenC2 TC members) for the Dreamport Plugfest/hackathon are at https://www.oasis-open.org/apps/org/workgroup/openc2/documents.php?folder_id=3315.

The DreamPort calendar announcement is at
https://dreamport.tech/event-open-c2-plug-fest-01272820.php
with links to registration.

OASIS has created a new mail list for the plug fest, openc2-plugfest-2019@lists.oasis-open.org. The list is open to interested parties regardless of OASIS or TC membership.
See link on DreamPort calendar page to join.

Registration for the event is at https://dreamport.tech/registration-open-c2-plug-fest-0120.php.

Please do a pull request against this page and add yourself to participants section

Information about DreamPort:  https://dreamport.tech/about-us.php

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
- https://docs.google.com/document/d/1yfiZJLL0S7ENu4RMdSVrWmsetlvFUMN2LZwjZ_3bXg0/edit?usp=sharing - Specification for Transfer of OpenC2 Messages via CoAP
- link to OpenDxl spec?
- link to what actuator profiles are in progress?

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
