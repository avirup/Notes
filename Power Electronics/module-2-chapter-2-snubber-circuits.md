# Chapter 2.2: Snubber Circuits

## Opening

Correct gate or base drive is only part of reliable switching. Real power circuits also contain stray inductance, device capacitance, stored magnetic energy, and abrupt current change. These non-idealities produce voltage overshoot, current surge, ringing, false triggering, electromagnetic interference, and additional switching loss.

A **snubber circuit** is auxiliary circuitry placed around a switch, transformer, diode, or inductive path to control such transients and provide a controlled destination for stored energy [Rashid, *Power Electronics: Circuits, Devices and Applications, 4e*], [onsemi AN1048/D]. This chapter explains why snubbers are needed, distinguishes turn-ON and turn-OFF stress, and introduces three foundational protective networks: the **RC snubber**, the **RCD snubber**, and the **freewheeling diode**.

## Prerequisites

Before reading this chapter, it is useful to recall the following points:

- From Chapter 1.2, an SCR can false-trigger if the voltage across it changes too quickly.
- From Chapters 1.4 and 1.5, MOSFETs and IGBTs do not switch instantaneously, and parasitic capacitances influence their switching behavior.
- Current through an inductor cannot change abruptly.
- The energy stored in an inductor is $\tfrac{1}{2}LI^2$.
- From Chapter 2.1, driver strength affects $dv/dt$ and $di/dt$, but layout and external protection components also matter.

If leakage inductance, Miller effect, or reverse recovery are not fresh, a brief review of Chapters 1.2, 1.4, 1.5, and 2.1 will make this chapter easier to follow.

## Core content

### 2.2.1 Need for snubbers; turn-ON and turn-OFF snubbers

#### Why switching stress appears even in a "simple" circuit

Consider a MOSFET switching current through an inductive load in a 48 V battery charger, or an IGBT switching a few amperes in an inverter leg fed from a rectified 230 V, 50 Hz supply. In an ideal circuit, turn-OFF would interrupt current and establish the blocking voltage across the device. In practice, wiring, package leads, PCB traces, transformer leakage paths, and the load all contribute inductance, while the switch node and device terminals contribute capacitance. When the current path is interrupted, the stored magnetic energy in that inductance appears as overvoltage and ringing.

The magnetic energy stored in stray or leakage inductance is

$$\boxed{E_L = \frac{1}{2}L_{\sigma} I^2} \quad \text{(7.1)}$$

where $E_L$ is the energy stored in the stray or leakage inductance, $L_{\sigma}$ is that inductance, and $I$ is the current flowing just before the switching event.

Even a small inductance can store enough energy to produce a severe transient. Suppose the effective stray or leakage inductance is only $2\,\mu\text{H}$ and the current just before turn-OFF is $12 \text{ A}$. Then

$$E_L = \frac{1}{2}\times 2\times 10^{-6}\times 12^2 = 144\times 10^{-6}\text{ J} = 144\,\mu\text{J}.$$

If, for a brief moment, this energy can charge only about $200 \text{ pF}$ of effective node capacitance, the equivalent voltage associated with that energy is

$$V \approx \sqrt{\frac{2E}{C}} = \sqrt{\frac{2\times 144\times 10^{-6}}{200\times 10^{-12}}} \approx 1200 \text{ V}.$$

The exact spike in a practical converter depends on the available parasitic and intentional paths, so the circuit does not necessarily reach $1200 \text{ V}$. The estimate nevertheless shows why a converter operating from a few hundred volts can generate a much larger transient if the stored energy is left to parasitics alone.

Snubber networks are introduced to limit $dv/dt$, clamp peak overvoltage, damp ringing, suppress false triggering of thyristors, and reduce stress associated with interrupted inductive current or diode reverse recovery [Rashid, *Power Electronics: Circuits, Devices and Applications, 4e*], [onsemi AN1048/D]. In each case, the objective is the same: the transient energy should enter a controlled auxiliary path rather than the parasitic network.

#### Turn-OFF stress and turn-OFF snubbers

A **turn-OFF snubber** acts when the power device is being turned OFF and current in a stray inductive path attempts to continue flowing. The associated voltage is governed by the inductor relation

$$v_L = L\frac{di}{dt}.$$

If $\tfrac{di}{dt}$ is large and no alternative path exists, the voltage across the switch rises sharply. A turn-OFF snubber softens that event by giving the current a temporary destination. An RC snubber lets a capacitor absorb part of the sudden voltage rise while the resistor damps the oscillation; an RCD snubber conducts selectively above a clamp condition and diverts the spike into a capacitor; other clamp or freewheel paths can keep the switch from seeing the full stress directly [onsemi AN1048/D], [onsemi AN4137].

The role of the snubber capacitor follows from

$$\boxed{i_C = C\frac{dv}{dt}} \quad \text{(7.2)}$$

or

$$\frac{dv}{dt} = \frac{i_C}{C}.$$

If a transient current must charge a capacitor, a larger capacitance produces a slower voltage rise. A capacitor across a switch therefore reduces $dv/dt$. The tradeoff is that increasing $C$ also increases stored energy, dissipation, and the current that may appear when the device turns ON again. Snubber design is therefore a compromise among stress reduction, loss, cost, and switching behavior [onsemi AN1048/D].

#### Turn-ON stress and turn-ON snubbers

A **turn-ON snubber** acts during the interval when the device is being turned ON. The stress can arise from discharge current in a previously charged snubber capacitor, reverse-recovery current in a diode that had been conducting, current surge into a capacitive node, or a large $di/dt$ set by parasitics rather than by the load alone.

ST's application note on gate and base drive emphasizes that, in many inductive-load applications, turn-ON occurs while the freewheeling diode is conducting, so the diode's reverse recovery directly influences current rise and switching loss [ST AN509/1293]. The distinction is therefore straightforward: turn-OFF snubbers mainly control voltage rise and overvoltage, whereas turn-ON snubbers mainly control current surge and reverse-recovery-related stress.

**Image prompt for Figure 7.1:** Create a clean textbook-style technical illustration comparing unsnubbed and snubbed switch turn-OFF in an inductive circuit. Show a power switch carrying inductive current, a small stray inductance in the loop, and two aligned voltage waveforms across the switch: one with a sharp overshoot and ringing, one with a slower controlled rise and lower peak due to a snubber. Label stored energy in stray inductance, voltage overshoot, ringing, and controlled transient. Use monochrome engineering style with axes, units, and clear labels.

### 2.2.2 RC and RCD snubber circuits; freewheeling diode

#### RC snubber circuits

The simplest named snubber is the **RC snubber**, a resistor and capacitor connected in series and placed across a device or across a problematic node. The capacitor slows the voltage change because the transient current must charge it first, while the resistor damps oscillation and limits the current that would otherwise flow too sharply into or out of the capacitor.

A capacitor alone may reduce the initial $dv/dt$ but can also create heavy current pulses and strong resonant ringing with the stray inductance. A resistor alone seldom limits the spike sufficiently. The series RC combination is used because it addresses both the first transient and the oscillation that follows.

The RC pair introduces a time constant

$$\boxed{\tau = RC} \quad \text{(7.3)}$$

where $\tau$ is the RC time constant, $R$ is the snubber resistance, and $C$ is the snubber capacitance.

The time constant does not by itself determine the design, but it indicates the basic trend: larger $C$ slows the voltage rise, larger $R$ limits the current pulse and increases damping, and excessive values increase loss or slow the transition more than desired.

##### RC snubbers across thyristors

One classical use of the RC snubber is across an SCR or TRIAC. onsemi's application note AN1048/D describes the simple snubber as a series resistor and capacitor placed around the thyristor, and explains that RC networks are used to control voltage transients that could falsely turn on a thyristor [onsemi AN1048/D].

This remains an important application because the SCR is sensitive to rapid $dv/dt$. If the anode-cathode voltage rises too quickly, the internal junction capacitances can drive enough current into the regenerative structure to trigger the device even without an intentional gate command. In this setting, the RC snubber is used primarily to prevent unwanted turn-ON and control transient behavior, not to improve efficiency.

**Image prompt for Figure 7.2:** Create a textbook-style figure showing an SCR with a series RC snubber connected across anode and cathode. Include a corresponding waveform panel that compares voltage across the SCR with and without the snubber during a transient. Label anode, cathode, gate, snubber resistor, snubber capacitor, false-triggering risk, and reduced $dv/dt$. Use monochrome engineering style with clear engineering labels.

##### RC snubbers across transistor switches

RC snubbers are also used with MOSFETs, IGBTs, and diodes to reduce ringing on a switch node or across a device. In these applications the main objectives are limiting overshoot, damping resonance caused by stray inductance and node capacitance, reducing EMI, and lowering repetitive stress on the semiconductor.

The price is power loss. Every cycle, the snubber capacitor is charged and discharged. A useful first estimate for the average power associated with that repetitive charging is

$$\boxed{P_{RC,\text{approx}} \approx \frac{1}{2}CV^2 f_s} \quad \text{(7.4)}$$

where $P_{RC,\text{approx}}$ is the approximate average snubber-related power, $C$ is the snubber capacitance, $V$ is the voltage swing across it, and $f_s$ is switching frequency.

The actual loss depends on topology, waveform, and the extent to which the capacitor charges and discharges in each cycle, but the estimate is sufficient for preliminary sizing.

Consider a converter switching at $20 \text{ kHz}$ with an RC snubber capacitor of $1 \text{ nF}$ that experiences about $325 \text{ V}$ each cycle in an off-line stage. Then

$$P_{RC,\text{approx}} \approx \frac{1}{2}\times 1\times 10^{-9}\times 325^2\times 20\times 10^3 \approx 1.06 \text{ W}.$$

This level of dissipation is not negligible. The resistor must be chosen and mounted so that the heat can be removed safely. Because the resistor ultimately absorbs the transient energy, RC snubbers are best suited to moderate stress where waveform shaping and damping are the main objectives.

#### RCD snubber circuits

An **RCD snubber** adds a diode to the resistor-capacitor network so that the clamp acts mainly in one direction. Instead of participating equally in both voltage-rise and voltage-fall events, the network conducts primarily when the node attempts to exceed a safe level in the dangerous direction.

This makes the RCD snubber especially useful in circuits such as the flyback converter primary switch, where transformer leakage inductance produces a turn-OFF spike at the switch drain or collector. When the switch turns OFF, the leakage inductance attempts to keep current flowing, the switch-node voltage rises, the snubber diode conducts when the clamp condition is reached, the capacitor receives the diverted energy, and the resistor dissipates that energy between switching events. The RCD snubber is therefore a **clamp-plus-dissipation** network rather than a lossless solution [onsemi AN4137].

##### First energy estimate for an RCD snubber

If most of the transformer leakage energy each cycle is dissipated through the RCD network, a useful first estimate is

$$\boxed{P_{RCD,\text{approx}} \approx \frac{1}{2}L_{lk} I_{pk}^2 f_s} \quad \text{(7.5)}$$

where $L_{lk}$ is the leakage inductance, $I_{pk}$ is the peak current present when the switch turns OFF, and $f_s$ is switching frequency.

This estimate shows that the average snubber burden scales directly with leakage inductance, the square of current, and switching frequency. Consider a small isolated auxiliary supply with

- $L_{lk} = 3\,\mu\text{H}$,
- $I_{pk} = 2.5 \text{ A}$,
- $f_s = 65 \text{ kHz}$.

Then

$$P_{RCD,\text{approx}} \approx \frac{1}{2}\times 3\times 10^{-6}\times 2.5^2\times 65\times 10^3 \approx 0.61 \text{ W}.$$

This is substantial enough to matter thermally, and it shows directly that reducing transformer leakage inductance reduces snubber burden.

**Image prompt for Figure 7.3:** Create a textbook-style schematic of a flyback converter primary showing a MOSFET switch, transformer primary, leakage inductance indicated, and an RCD snubber made of diode $D_{sn}$, capacitor $C_{sn}$, and resistor $R_{sn}$ connected as a clamp from the switch node to the DC input rail. Add a waveform panel showing drain voltage rising to reflected output voltage plus input voltage, then a leakage-induced spike, with the RCD clamp limiting the peak. Label all parts, polarities, and current path during turn-OFF. Use monochrome engineering style.

##### RCD snubbers in flyback converters

In a flyback schematic, the group $R_{sn}$, $C_{sn}$, and $D_{sn}$ placed near the primary switch node identifies a primary-side turn-OFF clamp rather than an output filter or ripple network. The orientation of $D_{sn}$ shows that the network is directional, not a continuously active RC damper. During the leakage-induced spike, $C_{sn}$ receives the diverted energy; between switching events, $R_{sn}$ dissipates it. Compared with a simple RC network across the switch, the RCD clamp participates less in the benign part of the cycle and gives tighter control of one-sided overvoltage [Fairchild AN-6014], [onsemi AN4137].

#### The freewheeling diode

The **freewheeling diode**, also called a **flyback diode** or **freewheel diode**, provides a recirculating path for inductive current when the controlled switch turns OFF. Its function differs from that of an RC or RCD snubber. A snubber primarily shapes or clamps a transient; a freewheeling diode primarily preserves current continuity in an inductive path.

When the switch controlling an inductive current turns OFF, the inductor current cannot instantly become zero. If a diode is connected so that it becomes forward-biased at that moment, the current continues through the load and diode instead of forcing the switch voltage to rise destructively. This function is fundamental in DC choppers, buck converters, motor drives, relay and solenoid circuits, and inverter legs during dead time [Mohan, Undeland, Robbins, *Power Electronics*], [ST STTH60AC06C Product Page].

At high switching frequency, ultrafast, Schottky, and silicon-carbide diodes are often preferred for freewheeling service because reverse recovery directly affects switching stress and ringing [ST STTH60AC06C Product Page], [ST STPSC40065C Product Page].

##### Current decay with a freewheeling diode

When the current freewheels through a diode, the inductor sees only a small reverse voltage, roughly the diode forward drop plus any resistive drops in the loop. A useful first approximation is

$$\boxed{\frac{di}{dt} \approx -\frac{V_F}{L}} \quad \text{(7.6)}$$

where $V_F$ is the effective forward drop of the recirculating path and $L$ is the inductance.

Suppose a $2 \text{ mH}$ inductor is carrying $5 \text{ A}$ when the main switch turns OFF, and the freewheeling path imposes about $1 \text{ V}$ across the inductor. Then

$$\frac{di}{dt} \approx -\frac{1}{2\times 10^{-3}} = -500 \text{ A/s}.$$

The current therefore takes about

$$t \approx \frac{5}{500} = 0.01 \text{ s} = 10 \text{ ms}$$

to fall to zero in this simplified estimate.

The tradeoff is clear: a diode freewheel path gives low voltage stress, but it also causes slow current decay because the reverse voltage across the inductor is small. If a higher clamp voltage were allowed, the current would fall faster. The designer therefore balances voltage stress, current-decay rate, control requirements, efficiency, and EMI.

##### Selection and relation to snubbers

The presence of a freewheeling diode does not automatically remove the need for an RC or RCD snubber. In many circuits, the diode carries the main inductive current after commutation, while a separate snubber still controls ringing and stray-inductance stress.

Selection of the diode depends on repetitive reverse-voltage rating, average and peak forward current, reverse-recovery behavior, and thermal capability. ST's drive note makes the same point from the transistor side: at turn-ON, the switching device often encounters the recovery behavior of the conducting freewheeling diode [ST AN509/1293].

Table 7.1 compares the three main protective networks in this chapter.

Table 7.1: RC snubber, RCD snubber, and freewheeling diode compared

| Network | Main purpose | Main strength | Main tradeoff | Typical place |
| --- | --- | --- | --- | --- |
| RC snubber | Reduce $dv/dt$ and damp ringing | Simple and widely applicable | Continuous loss and extra turn-ON burden | Across SCR, TRIAC, switch, or diode |
| RCD snubber | Clamp overvoltage more selectively | Better suited to leakage-spike control | Dissipates leakage energy and needs tuning | Flyback primary switch, clamp node |
| Freewheeling diode | Provide path for inductive current after switch state change | Strong reduction of voltage stress from interrupted load current | Slow current decay if clamp voltage is low | Across inductive load or as recirculation path in converter leg |

In a flyback auxiliary supply, an RCD snubber is commonly used to keep the primary-switch spike within safe limits. In a buck converter, the freewheeling diode is part of the basic current path after the main switch turns OFF. If switching frequency is high and ringing remains problematic, an additional RC snubber may still be required. The choice follows the transient mechanism being controlled in that topology.

## How this matters in renewable-energy systems

Renewable-energy converters operate repeatedly under significant electrical and thermal stress, so transient control has direct consequences for reliability and electromagnetic behavior. In PV inverters, battery chargers, and wind-converter auxiliaries, snubbers and freewheeling paths keep leakage-inductance energy and commutation transients within device limits. Their value is not limited to efficiency; they also affect service life, EMI, and the margin between normal operation and repetitive overstress.

## Chapter summary

- A **snubber circuit** provides a controlled path for transient energy that would otherwise produce overvoltage, ringing, false triggering, or excessive switching stress.
- The stored energy that drives many turn-OFF spikes is $\boxed{E_L=\tfrac{1}{2}L_{\sigma}I^2}$ from Equation (7.1).
- A capacitor limits voltage-rise rate because $\boxed{i_C=C\,dv/dt}$ from Equation (7.2), so turn-OFF snubbers mainly control voltage rise and overvoltage.
- A series **RC snubber** slows the transient and damps oscillation; its basic time constant is $\boxed{\tau=RC}$ from Equation (7.3), and its repetitive power can be estimated by $\boxed{P_{RC,\text{approx}}\approx \tfrac{1}{2}CV^2f_s}$ from Equation (7.4).
- An **RCD snubber** adds a diode so that clamping is directional, which is especially useful for leakage-induced turn-OFF spikes in flyback converters; a first dissipation estimate is $\boxed{P_{RCD,\text{approx}}\approx \tfrac{1}{2}L_{lk}I_{pk}^2f_s}$ from Equation (7.5).
- A **freewheeling diode** preserves current continuity when the main switch changes state; the corresponding current-decay estimate is $\boxed{di/dt\approx -V_F/L}$ from Equation (7.6), and the low clamp voltage that protects the switch also slows current decay.
- The choice among RC snubbers, RCD snubbers, and freewheeling diodes depends on whether the dominant problem is $dv/dt$, one-sided overvoltage from leakage inductance, or interruption of load current.

## Further reading

- [onsemi, *AN1048/D: RC Snubber Networks for Thyristor Power Control and Transient Suppression*](https://www.onsemi.com/download/application-notes/pdf/an1048-d.pdf) - A very useful classic reference for understanding why snubbers are needed, especially for SCR $dv/dt$ control and the tradeoffs involved.
- [onsemi, *AN4137: Design Guidelines for Off-line Flyback Converters Using Fairchild Power Switch*](https://www.onsemi.com/pub/Collateral/AN-4137.pdf) - Helpful for seeing an RCD snubber in a real flyback schematic and understanding its place in practical converter design.
- [Fairchild Semiconductor, *AN-6014: Green Current Mode PWM Controller FAN7602*](https://www.onsemi.com/download/application-notes/pdf/an-6014.pdf) - Useful because it distinguishes diode RC snubber design from MOSFET RCD snubber design in a real SMPS design context.
- [STMicroelectronics, *Influence of gate and base drive on power switch behaviour*](https://www.st.com/resource/en/application_note/cd00003914-influence-of-gate-and-base-drive-on-power-switch-behaviour-stmicroelectronics.pdf) - Especially useful for the link between switch turn-ON stress and the reverse recovery of the conducting freewheeling diode.
- M. H. Rashid, *Power Electronics: Circuits, Devices and Applications*, 4th ed. - A strong textbook reference for the broader role of snubbers, freewheeling diodes, and switching-stress control across converter families.
