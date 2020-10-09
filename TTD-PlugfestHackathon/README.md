# Table Of Contents
need to do this
- [1. Intro](#1---intro)
   * [1.1](#11-openc2)
   * [1.1](#1?-impact-of-covid)
- [2. ](#2-)
- [3. ](#3-)

# 1 - Intro

There is no better time
to be in the cyber-security profession than today.
We are faced with interesting problems
and we address the needs of new functionality
within evolving cyber-ecosystems.
We are seeing an expansion in the
cyber-physical (such as robotics and self driving cars)
and an increase in the abstract (such as cloud migration,
artificial intelligence and machine learning).
Cyber-security is a most rewarding profession to be in,
but there are associated challenges.
We need the experts to be able
to focus their efforts and permit their innovations
to be applied to a range of uses regardless of the cyber-ecosystem.

This is where efforts such as
OpenC2, SBOM, IACD, OCA, SCAPv2 come in.
The OpenC2 Plugfest/SBOM PoC/Hackathon
is a mashup of combining all these concepts
to demonstrate usecases showing the value of automated defense.

## 1.1 OpenC2
OpenC2 is a standardized language
for the command and control of technologies
that provide or support cyber defenses.
By providing a common language for
machine-to-machine communication,
OpenC2 is vendor and application agnostic,
enabling interoperability across a range of cyber security tools
and applications.
The use of standardized interfaces and protocols enables
interoperability of different tools,
regardless of the vendor that developed them,
the programming language they are written in
or the function they are designed to fulfill.
OpenC2 has an initial suite of specifications written
and we are at the point where we are applying it to
real world use cases on real cyber security products.

## 1.2 SBOM
blah blah to be filled in
## 1.3 IACD
blah blah to be filled in
## 1.4 OCA
blah blah to be filled in
## 1.5 SCAPv2
blah blah to be filled in
## 1.6 CACAO
blah blah to be filled in

## 1.7 Impact of Covid
OpenC2 organized a Plug Fest that was to take place
in conjunction with
[Technology Transfer Days](https://techtransferdays.org/).
The Plug Fest was intended to encourage participation
beyond the individuals from 39 different organizations
that are on the OpenC2 effort within OASIS,
and to include the larger ecosystems
OpenC2 operates in (IACD, OCAS, SCAPv2, OCA, …).

The physical OpenC2 plugfest was cancelled
when TechTransferDays
was cancelled due to the pandemic.
It is being replaced with a virtual Meetup on October 28th.
More details will be published here as they are determined.
The details will be worked out as part of the SBOM-PoC.
See [SBOM Proof of Concept](../SBOM-PoC/)
for details on the work leading up to the plugfest..

SBOM-PoC will be used as the shortened version of the
SBOM/SCAPv2/IACD/OCA/CACAO/...
virtual PoC/plugfest/hackathon
that is occurring up until 27-Oct.
Plugfest will be shorthand for the
SBOM/SCAPv2/IACD/OCA/CACAO/...
virtual PoC/plugfest/hackathon
event on Oct 28th
but realistically it will probably be called SBOM-PoC as well.

For organizations participating, see [here](../SBOM-Poc/README.md##2---organizations-participating).

# 2 - Agenda
The draft agenda is [here](./poc_agenda.md)

# 3 - Registration
Registration will be via Eventbrite.
You may register at link-to-be-provided beginning 12-October.
You can register as a participant
(i.e. you have software for interworking/hackathon)
or as an attendee
(i.e. you will be listening to plenary sessions but
do not plan to be hands-on).
There are several questions that need to be answered to register.
This will help us with planning.


# 3 - Meetup Logistics
## 3.1 - Conference Tools
The plenary sessions will via zoom and
access to zoom will be provided via the Eventbrite tickets.
Breakout sessions for the hands-on breakout sessions
will be using Discord.
Participants (and attendees if they request) will be provided
Discord information after they register.

## 3.2 Ecosystems
Unlike previous OpenC2 plugfests,
we will not be physically in the same room
and therefore will not be on the same network.
Therefore we will need to interwork our devices remotely.

At the moment, 3 ecosystems are planned:
- HTTP HTTPS - OpenC2 producers interact with OpenC2 consumers virtual HTTP or HTTPS.
This may be challenging for consumers behind firewalls
since the consumer performs the sever role
so it would require opening up either port 80 (HTTP) or port 443 (HTTPS).
For HTTPS, participants should work our certificates
prior to the plugfest.
- MQTT MQTT/TLS - This is the preferred ecosystem.
Since MQTT is a simple pub/sub protocol,
it avoids the firewall issues of HTTP/HTTPS.
See (add link) for broker details.
- OpenDXL - an OpenDXL broker has been established in GCP for the SBOM PoC.
See (add link) for broker details.

## 3.3 Projects to interwork
- [Huntington Ingalls OIF](needtoaddlink)
- [Huntington Ingalls Yuuki](needtoaddlink)
- [sFractal Blinky et al](needtoaddlink)
- [DoD JADN](needtoaddlink)
- [DoD Actuator Profile Tool](needtoaddlink)
- [MoD/CACI  whatisname](needtoaddlink)
- [New Context whatisname](needtoaddlink)
- [Ion Channel SaaS](needtoaddlink)
- [BTS Centurion](needtoaddlink)
- [BTS Legion](needtoaddlink)
- [UNC Honeypots?](needtoaddlink)
- [Univ of Oslo fw?](needtoaddlink)

## 3.4 Open Source Repos of interest
- fill in with repos from ATT lycan-python/lycan-java, New Context AWS/newp, HII yuuki, DoD tools, Google, etc
