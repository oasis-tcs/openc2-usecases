# Table Of Contents
- [1. Intro](#1---intro)
- [1.1 SBOM-PoC#11-vision](SBOM-PoC#11-vision)
- [2. Organizations Participating](#2---organizations-participating)
- [3. Goals and Objectives](#3---goals-and-objectives)
- [4. Work Plan](4---work-plan)
- 5. ...

# 1 - Intro
The Software Bill Of Materials (SBOM) Proof of Concept (PoC)
sets out to prove several concepts e.g.
- SBOMs
   - may be used in protecting organizational systems, networks, data, and users
   - may be created
   - may be obtained
   - may be used to make security decisions
- Openc2
   - may be used in protecting organizational systems, networks, data, and users
   - may be used to obtain SBOMs
   - may be used to command and control security functions
- CACAO playbooks
   - may be used in protecting organizational systems, networks, data, and users
   - may be used to identify, create, document, and test detection, investigation, prevention, mitigation, and remediation steps

This SBOM PoC is a combination of several efforts:
- OpenC2 virtual plugfest/hackathon
- NTIA SBOM Transfer PoC - see [here](https://www.ntia.gov/sbom) and [here](https://www.ntia.gov/SoftwareTransparency)
- others TBD including potentially
   - [Integrated Adaptive Cyber Defense or IACD](https://www.iacdautomate.org/) SOAR PoC showing playbooks and automated orchestration
  - [CACAO](https://www.oasis-open.org/committees/tc_home.php?wg_abbrev=cacao) playbook PoC
  - [Open Cybersecurity Alliance](https://opencybersecurityalliance.org/) PoC

See [Section 2](#2---organizations-participating)
for organizations participating
and how their goals tie to these efforts.

See [Section 3](#3---goals-and-objectives)
for goals and objectives of each of these.

See [Section 4](#4-work-plan) 4 on how the work will be organized

See Sections 5 - N on blah blah with the details

## 1.1 Vision
The vision of this activity is that it will prove several concepts
associated with several independent efforts (e.g. OpenC2, NTIA SBOM, ...).
This work is intended to be virtual
(ie no physical meetings needed)
and consist of many pairwise
interworking steps growing to larger many-party working scenarios or use cases.
Examples of scenarios include:
- an automated response to an attack on a device which did not create an SBOM. See https://youtu.be/9KnagMQ6SNI at ~3 min 10 sec as example
- a device coming online in a network, it's SBOM being queried with OpenC2, and:
    - device does not have SBOM, so orchestrator denies access to network
    - device has SBOM, sense making looks up components and discovers vulnerabilities exist, so orchestrator:
       - sandboxes device,
       - automagically installs component updates (including updating SBOM,
       - allows access to network
    - device has SBOM, sense making looks up components and discovers vulnerabilities exist, so orchestrator allows access
- ditto previous with mud (either standalone or in combination with OpenC2)
- an automated response to an attack on a device which did create an SBOM, and had automated update when CVE annouced . See  https://youtu.be/9KnagMQ6SNI at ~4 min 50 sec as example
- the Denver Airport Scenarios from Jan Plugfest
- the firewall scenarios from the Jan Plugfest
- setting up the (multi-)cloud instances using OpenC2 (using New Context and AT&T opensource)
- some megascenario combining them all

Scenarios will have plans (e.g. see
[sFractal Scenario 1 work plan](./sFractalScenarios/workPlan.1.md))
including flowchart (e.g.
<p align="center">
![Comply to Connect Flow](./sFractalScenarios/sFractal.1.png) 
sFractal Scenario 1
Figure 3.1-1:
</p>

with draw.io
[source](./sFractalScenarios/sFractal.1.drawio)),
human readable scenario (e.g.
[sFractal Scenario 1](./sFractalScenarios/README.md#31---comply-to-connect))
and CACAO playbooks (e.g.
[sFractal playbook 1](./sFractalScenarios/cacaoPlaybook.01.json)).

This effort is scheduled from June thru October 25, 2020
and will terminate just prior to
[TTD-PlugfestHackathon](https://github.com/sparrell/openc2-lsc-usecases/tree/master/TTD-PlugfestHackathon)
at
[Tech Transfer Days](https://techtransferdays.org/)
where a physical in-person meetup/mashup will
hopefully repeat the virtual accomplishments
and further advance the work with aspects that require being on the same LAN.
The effort from now until October
is being called Phase 1 with the hope
there will be follow on work after TDD that can be accomplished virtually.

# 2 - Organizations Participating
Here is the list of organizations who have agreed to participate,
in order of volunteering to participate in PoC,
hotlinked to pages showing what they are interested in
and what they plan to contribute to this effort:
- [sFractal Consulting](./sFractalGoals.md)
- [NSA](./NSAGoals.md)
- [Huntington Ingalls Industries](./HIIGoals.md)
- [New Context](./NewContextGoals.md)
- [NineFx](./NineFx.md)
- [One Planet Education Network](./OnePlanetGoals.md)
- [AT&T](AttGoals.md)


# 3 - Goals and Objectives
This effort is a mashup of several efforts
by a combination of many organizations,
all with goals related to one or more of the efforts.
The organization goals/objectives pages (see [Section 2](#2-organizations-participating))
will be combined into individual pages per effort:
- [OpenC2 Plugfest/Hackathon Goals & Objectives](./Oc2Goals.md)
- [NTIA SBOM Transfer PoC Goals & Objectives](./SbomGoals.md)
- [IACD Goals & Objectives](./IacdGoals.md)
- [CACAO Goals & Objectives](./CacaoGoals.md)
- [Opencyber Security Alliance Goals & Objectives](./OcaGoals.md)

# 4 - Work Plan
The work will be organized using the following terms,
mostly cribbed from SBOM Healthcare PoC:
- Phase 1- The work done virtually from now until [TTD-PlugfestHackathon](https://github.com/sparrell/openc2-lsc-usecases/tree/master/TTD-PlugfestHackathon)
- Sprint - the interval between the biweekly status meeting (e.g 4-June-2020 to 18-June-2020)
- Interval - An interval consists of several sprints. Phase 1 will be broken into at least 3 intervals described [here](./WorkPlanIntervals.md) with discrete objectives (e.g. interval 1 focus is on 'within an organization', interval 2 on between an organization lab and a cloud, interval 3 on org1-cloud-org2, ...)
- Wave - a subset of an interval meeting a subset of the objectives. An Interval is broken into waves usually due to different organizations having deliverables arriving at different times. E.g. in the Healthcare SBOM PoC, Interval 1 was broken into two waves so the initial 13 MDD SBOMs could start being evaluated by the HDOs without having to wait for the 'wave 2' SBOMs.
- Use case/Scenario - for this effort, the terms will be used somewhat interchangeably to describe the scenarios being simulated in this PoC to simulate the real life uses of the concepts trying to be proved. The expectation is the scenarios will start out simply in pair-wise interactions and grow to complex scenarios involving all aspects of the IACD architecture (ie sensing, sense-making, decision making, acting) showing cyber defense at machine speed.

See the [Work Plan](./WorkPlan.md) for more details.

# 5 -
.
