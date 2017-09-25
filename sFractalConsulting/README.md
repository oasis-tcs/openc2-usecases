# sFractal Consulting Use Cases 

This directory contains use cases for the OpenC2 language as contributed by sFractal Consulting.
These use cases are of particular interest to sFractal Consulting.
Other members are welcome to utilize these use cases as they fit, 
including modifying them to fit their organization's interests.

## C4 - Collective Code Construction Contract 
Please read README in parent directory for groundrules on LSC use cases.

## Licensing
All text contributed here by sFractal Consulting is released under the Creative Commons CC0 Liscense.

put cc0 image here

## Contact 
Contact Duncan Sparrell, Chief Cyber Curmudgeon, sFractal Consulting with any comments or suggestions.


## Style 
Use Case is a very overloaded term and means different things to different people.
A scenario approach will be used for what is presented here.
Each file will contain one scenario, sometimes based on initial conditions
set up in previous scenarios, but intending to stand on it's own
to show a particular desire.
Each scenario will be told in narrative (like chapters in a book)
and will have endnotes for:
 * references
 * explanatory text, asides
 * "stories"
The narrative will attempt to be from an OpenC2 paroachial viewpoint - glossing over details
not relevant to OpenC2 and diving deeper into requirements on OpenC2.
OpenC2 requirements and examples will attempt to be shown on separate referenced pages in
Agile SDLC (Software Development Life Cycle) 'user story' fomat 
(see http://www.agilemodeling.com/artifacts/userStory.htm)
eg
> As a {role}, I want {feature} so that {reason}.
> As sFractal's  orchestrator, I want to use an OpenC2 command to tell the firewall to block ip=whaterver so that the hacker can't get in.
> As the Small Business Administration, I want to use OpenC2 to tell sFractal to mitigate evildomain.com so that evildomainowner can be thwarted in attacking small buinsess webservers.

## Description and  Organization 
The scenarios are:
 * 00.websvr_basecase.md
  + the intial condition to start the narrative 
  + TL;DR - some resources in a cloud which is accessed from internet via an API
 * 01.xx 
  + TL;DR - allow second user access from internet
 * 02.xx 
  + TL;DR - increase logging for a particular event
 * 03.xx 
  + TL;DR - some more base case info (more machines not needed for previous use cases)
 * 04.xx 
  + TL;DR - request metadata about suspicious ip attempting wierd stuff
 * 05.xx 
  + TL;DR - query risk manager about effect of current state on loss exceedance curves
 * 06.xx 
  + TL;DR - spin up new fw vendor to replace old due to some new attack
 * 07.xx 
  + TL;DR - some more base case info (more machines not needed for previous use cases)
 * 08.xx 
  + TL;DR - SBA stix COA to sFractal to mitigate evildomain.com
 * 09.xx 
  + TL;DR - some more base case info (more machines not needed for previous use cases)
 * 10.xx 
  + TL;DR - some neat deception stuff that needs to be thought up
