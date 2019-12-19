# OpenC2 v1.0.1 Test Data for Plugfest

These tests apply to the OpenC2 Language Specification CS02 (version 1.0.1).

OpenC2 test items (commands and responses) are organized by actuator type, which determines whether a given item
is considered good or bad. Each actuator implements a component schema that is derived from one or more profiles.
Example actuator types are:

**1. Language**

This component accepts every command and response defined in the OpenC2 Language Specification,
and no Actuator Profiles.

* oc2ls-v1.0.1: Component schema = OpenC2 Language Spec CS02

**2. SLPF**

This component accepts commands and responses defined in the OpenC2 Stateless Packet Filtering profile.  Language
elements not used by the SLPF profile are not accepted.

* oc2slpf-v1.0.1: Component schema = OpenC2 SLPF Profile

**3. Language + SLPF + Acme**

This component accepts every command and response defined in the Language Specification and SLPF profile,
plus some additional hypothetical actuator profiles.  Schema serves as an example of how
commands and responses needed to support new use cases (such as a Powerwall home battery) are integrated
into OpenC2.

* oc2ls-v1.0.1-acme: Component schema = OpenC2 LS CS02 + SLPF + Acme types, manually combined

4. <New Actuator A> ...

Commands and responses for plugfest use case A ...


## New tests
* **query_slpf_pairs_bad_action_rsp** - slpf/response/bad - action not supported in SLPF
* **query_slpf_pairs_bad_target_rsp** - slpf/response/bad - target not supported in SLPF
* **query_slpf_pairs_bad_pair_rsp** - slpf/response/bad - action and target both supported but combination not valid
* **long_name_x80** - language-anything/commands/bad - long property names - property names must be 1-32 characters.
* **long_name_x244** - language-anything/commands/bad - very long property names

## Implausible tests
These tests pass a generic Language+Anything schema, but there is no plausible use case for validating them
as correct OpenC2 commands and responses.
They illustrate the difference between a generic schema and profiles used by OpenC2 Producers and Consumers.
* **create_poetry** - slpf+acme/commands/bad - English literature
* **results_poetry** - slpf+acme/results/bad - English literature
* **set_castle** - slpf+acme/commands/bad - Online game*
* **results_castle** - slpf+acme/results/bad - Online game

\* *Actual data from an online game.  Without a profile there is no*
*clue to what purpose it serves or what benign or malicious operations might be intended,*
*and there are no limits on what is considered valid OpenC2.*
