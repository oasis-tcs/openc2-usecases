## SCAP v2

[SCAP v2 Data Collection Architecture](https://docs.google.com/document/d/1DwT4noHSEfKYmg1qvySk8ufS5eJ4q19LUVbsaAXlC8w/)
June 10, 2020

[SCAP Prototype Architecture](https://docs.google.com/presentation/d/11EtTqBsSlfGVnjmudNrTSTpk3-tUUxn90AuucZpenD8)
July 8, 2020

[SCAP v2 Prototype Schema](scap-dca.jidl)

### 5 August meeting
Architecture defines two main use cases:
1. Point-in-time information collection
2. Ongoing monitoring against a baseline

Key Supporting Data Sets:
1. Assessment Instructions
2. Bound Asset Lists
3. Assessment Results
4. Collector Scopes
5. Collector/PCX Capabilities

Schema names and defines data objects exchanged across the architecture.  Goal is to develop
a sequence diagram of Application interactions, with every data object named.

Questions:

* What is the difference between ReportRequest and QueryRequest shown on slides?
    * Assessment Instructions/Results vs Collection Instructions/Results
    * Time-bound request vs. Setup ongoing monitoring?

* Is it a valid scenario for Application to talk only to Manager
(instead of getting replies from Collector)?
    * Looking for initial experiment, but not over-simplify to something with no future
    * Application flows can be expanded to repository and collector later.

* What are examples of Check System and Check Type (from Collection Method and Collector Capabilities)
    * Enumerated values?