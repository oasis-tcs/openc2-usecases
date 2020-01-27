# OpenC2 Hackathon Activities

This page is intended for realtime updates during the hackation of what is going on.
It is a place to see where you can help, or ask if you need help.

Table of Contents:
- [1. Intro](#1-intro)
- [2. Testing](#2-testing)
  * [2.1 Postman](#21-postman)
  * [2.2 Broadcom/Symantec ICDX Testing](#22-broadcom-symantec-icdx-testing)
  * [2.3 AWS/GCP Openc2](#23-aws-gcp-openc2)
  * [2.4 add more](#24-add-more)
  * [2.5 add more](#25-add-more)
- [3. Integration](#3-integration)
  * [3.1 Interoperability](#31-interoperability)
  * [3.2 Among plugfest/hackathon](#32-among-plugfest-hackathon)
  * [3.3 with other standards](#33-with-other-standards)
    + [3.3.1 KMIP](#331-kmip)
    + [3.3.2 SBOM](#332-sbom)
    + [3.3.3 STIX](#333-stix)
    + [3.3.4 CACAO](#334-cacao)
    + [3.3.5 OCA](#335-oca)
  * [3.4 OpenC2 HaHa Server](#34-openc2-haha-server)
    + [3.4.1 Cloud HaHa](#341-cloud-haha)
    + [3.4.2 Raspberry Pi HaHa](#342 Raspberry-Pi-HaHa)
    + [3.4.3 Elixir HaHa Vulnerabilities](#343-elixir-haha-vulnerabilities)
  * [3.5 OpenC2 PiHole](#35-openc2-pihole)
  * [3.6 OpenC2 Raspberry Pi Firewall and IDS](#36-openc2-raspberry-pi-firewall-and-ids)
- [4. Hardware](#4-hardware)
- [5. Software](#5-Software)
- [6. Learning/Teaching](#6-learning-teaching)
- [7. Issues & Problems](#7-issues-problems)
  * [7.1 Identify Issues](#71-identify-issues)
  * [7.2 Correct Errors, Fix Problems, Resolve Issues](#72-correct-errors-fix-problems-resolve-issues)
- [8. Documentation](#8-documentation)
* [8.1 Plugfest/Hackathon](#81-plugfest-hackathon)
* [8.2 Website](#82-website)

## 1. Intro

The hackathon aspect is for improving the interworking
of existing OpenC2 implementations,  
extending existing implementations
(e.g., the many OpenC2 open source projects),
and/or creating new implementations of OpenC2.

"Hacking" is about more than just writing code.
Obviously we'd welcome you writing code,
but don't feel you can't contribute if
that isn't your thing.
See the sections below to see how you can help -
note writing code was purposely moved to middle of
list to show there is lots to do beside writing code.

Let's document here what is going on, so
observers and other plugfest/hackathon groups can see what is going on
and potentially chip in to help.
Put stuff here if you could use help.

A companion page for plugfest aspects is at
[PlugFestActivites](plugfest-activities.md).
Maybe you can hack together something that will
help with someone's plugfest activities.

## 2. Testing
Everybody can always use more help testing.
Walk around to hackathon participants and to
plugfest participants and ask how you can help.

### 2.2 Postman
Any OpenC2 consumers being worked on should be able to be accessed using
Postman (https://www.getpostman.com/).
All projects would welcome cold eyes helping test their interfaces.
And its a good learning experience to boot.

If you aren't familar with Postman - ask around and someone here will help you

### 2.2 Broadcom/Symantec ICDX Testing
Syantec couldn't attend but has ICDX setup to test
and is available to consult via phone and email.
Help them setup and show off OpenC2 capability.

### 2.3 AWS/GCP Openc2
Various project (put in links - if none here ask Duncan)
use AWS or GCP or other clouds.
AddLink and AddLink can be used to control AWS and/or GCP.
From your laptop, test these yourself and set up some cloud resources.

### 2.4 add more

### 2.5 add more

## 3. Integration

### 3.1 Interoperability

### 3.2 Among plugfest/hackathon

### 3.3 with other standards

#### 3.3.1 KMIP

#### 3.3.2 SBOM

#### 3.3.3 STIX

#### 3.3.4 CACAO

#### 3.3.5 OCA
The Open Cybersecurity Alliance (https://opencybersecurityalliance.org/)

bring interoperability and data sharing across cybersecurity products

### 3.4 OpenC2 HaHa Server
Https Api Helloworld Actuator (HAHA)
is a very simple actuator
that is conformant with the 1.0 OpenC2 Language Specification
but does no actual security functions.
It has a Custom Actuator Profile (CAP)
and will respond to the query openc2 command with it's profile and schema.
It also responds to a custom query extension
"query Hello World" with "Hello World" - but that is all it does.

Various implementations of HaHa may exist.
One is in the elixir portion of the lycan-beam opensource repo -
https://github.com/oasis-open/openc2-lycan-beam/tree/master/haha

Actually that code currently has a tiny bit more to show
how to put stub functions
in for other actions, and to have something to play with at plugfest.

To understand what it does, you might want to start by looking at the
[test data](https://github.com/oasis-open/openc2-lycan-beam/tree/master/haha/elixir/test/data) which consists of OpenC2 commands,
e.g. [query_features_pairs.json](https://github.com/oasis-open/openc2-lycan-beam/tree/master/haha/elixir/test/data/query_features_pairs.json),
and of OpenC2 responses
e.g. [query_features_pairs_reply.json](https://github.com/oasis-open/openc2-lycan-beam/tree/master/haha/elixir/test/data/query_features_pairs_reply.json).
If there isn't a 'reply' file, then the reply is
[./test/data/ok_reply.json](ok_reply.json).
The files starting with err are for testing error conditions

#### 3.4.1 Cloud HaHa

Duncan would be happy to help anyone install this on their machines to play with.

Ideally someone would volunteer to figure out a script
to (1) create some cloud VM's, either AWS or GCP, using openc2 commands in
https://github.com/newcontext-oss/openc2-aws-actuator
and then (2)run this code to be an HaHa server in the cloud.

If the above is accomplished, then the HaHa code base could be modified to
simulate whatever command-consumers are required by other projects

#### 3.4.2 Raspberry Pi HaHa
Duncan hoped to have this up prior to hackathon but now will be
finished during hackathon

#### 3.4.3 Elixir HaHa Vulnerabilities
Serendipitously the code in 3.4 has some known vulnerabilities
in the javascipt templates for html.
Note the html part of the responses is not needed for the OpenC2 API.
It does help with debugging and the vulnerabilities were left in
for the comply-to-connect use case.

See
https://github.com/oasis-open/openc2-lycan-beam/network/alerts
for the vulnerability alerts.

### 3.5 OpenC2 PiHole
See https://pi-hole.net/.
First step is to set up one of Duncan's Raspberry Pi's to be a PiHole
(DNS sinkhole to block malicious ads).
Next step is to figure out the OpenC2 commands. Then we need to "openc2-ize"
the raspberry pi which would probably
be via python lycan since pihole is in python.


### 3.6 OpenC2 Raspberry Pi Firewall and IDS

See https://www.instructables.com/id/Raspberry-Pi-Firewall-and-Intrusion-Detection-Syst/
and then figure out how to make it work via OpenC2 commands.
First step is figure out the OpenC2 commands. Then we need to "openc2-ize"
the raspberry pi which could be via either python, java, or elixir lycans.

## 4. Hardware
add links of sfractal (and others if have) raspberry pi's, lights, buzzers etc.

Duncan is bring various Raspberry Pi's and peripherals
(blinky lights, buzzer, breadboard kits, soldering iron, etc).
He's happy to let people help out making them do demo-ey things
using OpenC2 (probably more work with the hardware than the OC2 part).

See https://github.com/elixir-circuits/circuits_quickstart for a good place to
start. It can be hooked to the elixir HaHa in 3.4

## 5. Software
make subsections for python/java/beam and link to various projects

make list of things that could help other inflight integrations going on

## 6. Learning/Teaching
walk around and learn, teach others about what you are doing.

read use cases, make more use cases

## 7. Issues & Problems
### 7.1 Identify Issues
### 7.2 Correct Errors, Fix Problems, Resolve Issues

## 8. Documentation
### 8.1 Plugfest/Hackathon
help document what going on here
### 8.1 OpenC2
THIS IS NOT AN OASIS MEETING!

That said - you can still look over the documents.
If you see errors/issues/problems - document them as part of the
hackathon and OASIS members will likely see your great Documentation
and bring the error/issue/problem
(and any proposed corrections/resolutions/fixes)
to an OpenC2 meeting to resolve
### 8.2 website
Cold eyes welcome.
Where can we improve?
Concrete suggestions welcome.

- OpenC2 public webpage https://www.oasis-open.org/committees/tc_home.php?wg_abbrev=openc2
- OpenC2 Member webpage https://www.oasis-open.org/apps/org/workgroup/openc2/index.php
- OASIS OpenC2 TC GitHub repos - https://github.com/oasis-open?q=openc2
- OASIS OpenC2 Open GitHub repos - https://github.com/oasis-open?q=openc2
- Google Doc Index - https://docs.google.com/document/d/1Bz_WXOiYc9vmMS8rNEP1-ZZgPzdeGoZMN6W5W9GSmdU/edit?usp=sharing
- OpenC2 Wiki https://wiki.oasis-open.org/openc2/FrontPage#preview

Contribute to clean up OBE or to add new content.
Some these anyone can write to.
Some only Oasis members can write directly.
Non-Oasis members can send email to public comment list and/or add to
these meeting notes.
