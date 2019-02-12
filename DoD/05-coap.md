RFC 7252 https://tools.ietf.org/html/rfc7252 says:
> The Constrained Application Protocol (CoAP) is a specialized web
> transfer protocol for use with constrained nodes and constrained
> (e.g., low-power, lossy) networks.  The nodes often have 8-bit
> microcontrollers with small amounts of ROM and RAM, while constrained
> networks such as IPv6 over Low-Power Wireless Personal Area Networks
> (6LoWPANs) often have high packet error rates and a typical
> throughput of 10s of kbit/s.  The protocol is designed for machine-
> to-machine (M2M) applications such as smart energy and building
> automation.

While it is true that many system-on-a-chip devices can support a full LAMP stack, CoAP is targeted for constrained **environments**, not rich environments provided in physically small packages.  CoAP runs over UDP, which means messages larger than a single UDP payload must be split and recombined using, e.g., https://tools.ietf.org/html/rfc7959.

"Saving a few bytes" is often insignificant in rich environments, though even extremely powerful devices such as core routers benefit from transmitting IP packets in binary format rather than as JSON strings.  But saving a few bytes in a constrained environment can mean the difference between fragmenting and not fragmenting, or retransmitting vs. receiving a message error-free the first time.  And as mentioned in https://www.omaspecworks.org/constrained-application-protocol-coap-is-iots-modern-protocol/:
> Being able to send many messages quickly is something that can come in handy.
> One of Octoblu’s developers used CoAP to control a robot at a BattleBot competition
> and was able to send three times more messages to his robot than the other
> competitors were able to do — ultimately allowing him to win the competition.
