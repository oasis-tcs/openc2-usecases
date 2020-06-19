# OpenC2 and Critical Infrastructure

OpenC2 is intended in part as a cybersecurity command language for Operational Technology (OT), sometimes known as the Internet of Things (IOT). Traditional cybersecurity commands are focused on the typical networks of file servers, database servers, web servers, and personal devices. Cybersecurity commands from firewall directives to interdiction of malware in documents have as their goal the protection of those administrative and data services. The communications requirements and systems architectures of OT are quite different than those of administrative systems, and the services provided by OT are far more diverse. The security directives for each type of OT system are just now being defined.

The services provided by OT may be critical to the performance of other systems. A cyber-threat to a power distribution system may create risks to every mission supported by that system. OpenC2 on OT systems may be able to provide critical situation awareness on threats to other missions.

OpenC2 commands are directed to discrete sets of functions grouped as a cyber-defense service, termed an Actuator Profile. A given system may offer multiple actuators. As an exampled from traditional cybersecurity, a network gateway might offer three actuator profiles: a stateless packet filter service, a stateful packet filter service, and a malware-blocking service.

So, too, an OT system may support multiple actuator profiles. An OT system may support a traditional Profile such as the Stateless Packet Filter Profile as well as OT specific services. 

In some circumstances, even revealing which Actuator Profiles are present may present security issues; the presence of certain profiles may reveal the location of the critical infrastructure which may catalog them for a physical attack rather than a cyberattack.

OpenC2 defines a Control interface for Actuators but does not define their Inputs and Outputs. See [Reporting Context](Reporting%20Context.jpg) for an example sensing/monitoring environment using OpenC2.
