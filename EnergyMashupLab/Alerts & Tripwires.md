Alerts & Tripwires
=========

In Cyberphysical systems (CPS), there is always a blending of data and physical
activity and physically adjacent systems. In a trivial example, a pedestrian
stepping in front of an autonomous car may be a data event the sets an alarm and
a trigger. How fast the car can brake is a physical activity that is always
finite in duration, but that may be different on a wet road or an icy one. In
any case, stopping faster than the car behind can do may also result in
cataclysmic failure.

Tripwires name small systems, often appliances that provide early warning of
events that could indicate a cyberincident. Many Cyber-tripwires could use
firewall events, or the presence of certain files over the network to launch a
larger response by means of an Alert. The diversity of CPS implies a plethora 
of tripwire appliances, each purpose-built for the CPS in question.

-   Current work in power distribution systems suggest that synchrophasor data
    collection and analysis could be used as a tripwire.

-   Transactive Resource Management (TRM) systems use internal markets to
    balance supply and demand of a commodity resource over time—meaning an
    internal market is the internal coordination mechanism. Security appliances,
    borrowed form the world of finance, use AI to detect market gaming and
    market health.

-   Traditional firewalls can support Alerts natively.

-   Intrusion detection systems can support Alerts.

-   Vibration analysis systems act as tripwires to send Alerts in manufacturing plants.

It would be a long and thankless task to attempt to catalog all tripwires that
might be used in a CPS.

There is a general pattern for interacting with tripwires and alert-capable devices which should be
standardized across OpenC2. Some tripwires may be software defined as “Reports”
from existing appliances.

This pattern may be based on the common model for PUB/SUB as is being defined in
other specifications at this time.
