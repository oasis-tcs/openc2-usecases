# Scenario 1.1.1 Comply-to-connect in lab, human handwaving
add toc

## 1 - Intro
blah blah

sFractak Scenario 1.1.1 is:
- Flow/Architecture sFractal 1 i.e.
   - [Flow 1 - Comply to Connect](./sFractal.1.png)
- Architecture Components sFractal 1.1
   - see section 2
   - need to add picture
   - on one lan in sFractal lab
- Configuration sFractal 1.1.1-n
   - 1.1.1 is sunny day
      - Precheck passes
      - SBOM exists
      - SBOM passes license checks
      - SBOM passes vulnerability checks (ie has no known vulnerabilities)
    - 1.1.2-n various rainy days - precheck fails, sbom nonexistent, licensing issue, sbom vulnerabilities, exercise the different risk detection mitigations (trouble ticket, deny access, extra IDS monitoring, sandbox, initiate investigation). Main configuration change is different SBOMs.

Staying with same flow but with different components (e.g. OPEN sensor replacing blinkyhaha or orchestrator being software in cloud instead human) is a different "second digit" scenario e.g.{add link}

## 2 - As-Built Architecture
need a picture with just a human, a laptop, and a blinkyhaha

## 3 - Flow

<p align="center">
![Comply to Connect Flow](./sFractal.1.png)
Figure 3.1-1:
</p>

## 4 - Configuration
- human as orchestrator
- blinkyhaha#? as device
- SBOM version ? at {need link}
- OpenC2 as SBOM discovery, access
- OpenC2 for security actions
- HTTP (ie not HTTPS, save that for later)
- ...

## 5 - Playbook
- CACAO playbook at [sFractal playbook 1](./cacaoPlaybook.01.json)

## 6 - Status
As of 6/10/20

Still planning

## 7 - Next Steps and Schedule
still planning

## 8 - Results

None yet
