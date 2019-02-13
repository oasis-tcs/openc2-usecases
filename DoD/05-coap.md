# Use Case for Machine-to-Machine Serialization
DoD has a requirement to operate in contested network environments:

> **Commanders should be prepared to conduct operations under degraded conditions in
cyberspace.** -- https://www.jcs.mil/Portals/36/Documents/Doctrine/pubs/jp3_12.pdf

One purpose of OpenC2 is to support that requirement by enabling response to cyber events at network speed.  Conducting command and control operations using efficient communication protocols enhances the ability of network defenders to fight through degraded conditions.  Protocols such as CoAP (RFC 7252, https://tools.ietf.org/html/rfc7252) that are designed for inherently constrained environments are also useful when network constraints are transient or externally imposed:

> The Constrained Application Protocol (CoAP) is a specialized web
> transfer protocol for use with constrained nodes and constrained
> (e.g., low-power, lossy) networks.  The nodes often have 8-bit
> microcontrollers with small amounts of ROM and RAM, while constrained
> networks such as IPv6 over Low-Power Wireless Personal Area Networks
> (6LoWPANs) often have high packet error rates and a typical
> throughput of 10s of kbit/s.  The protocol is designed for machine-
> to-machine (M2M) applications such as smart energy and building
> automation.

It has been suggested that many system-on-a-chip devices support a full LAMP stack, therefore there is no need for OpenC2 to operate in constrained environments. However the existence of rich environments provided in physically small devices does not negate the simultaneous existence of the constrained environments for which CoAP is designed.

"Saving a few bytes" is often insignificant in rich environments, though even extremely powerful devices such as core routers benefit from transmitting IP packets in binary format rather than as JSON strings.  But saving a few bytes in a constrained environment can mean the difference between fragmenting and not fragmenting, or retransmitting vs. receiving a message error-free the first time. CoAP runs over UDP, which means messages larger than a single UDP payload must be split and recombined using, e.g., https://tools.ietf.org/html/rfc7959. Protocols that are designed for efficiency in machine-to-machine communication, like IP itself, are more robust in both high volume and bandwidth-constrained environments.

Efficiency can also be a significant advantage in competition:
> Being able to send many messages quickly is something that can come in handy. One of Octoblu’s developers used CoAP to control a robot at a BattleBot competition and was able to send three times more messages to his robot than the other competitors were able to do — ultimately allowing him to win the competition. - https://www.omaspecworks.org/constrained-application-protocol-coap-is-iots-modern-protocol/

The schema mechanism used to define OpenC2 data types is designed explicitly to support more than one transmission format, accommodating both developers who prefer to send human-friendly strings over the wire and those who optimize for m2m communication and rely on tools such as Wireshark to display m2m data in human-friendly format.  The serialization rules defined in version 1.0 of the OpenC2 language spec cater to the first group.  But for both operation in constrained environments and application to OT/ICS environments, m2m serialization is also required.

> SCADA protocols are designed to be very compact. Many are designed to send information only when the master station polls the RTU. Typical legacy SCADA protocols include Modbus RTU, RP-570, Profibus and Conitel. These communication protocols, with the exception of Modbus (Modbus has been made open by Schneider Electric), are all SCADA-vendor specific but are widely adopted and used. Standard protocols are IEC 60870-5-101 or 104, IEC 61850 and DNP3. - https://en.wikipedia.org/wiki/SCADA

