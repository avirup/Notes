# Chapter 2.2: Snubber Circuits

## Chapter opening

Correct gate or base drive is only part of reliable switching. Real power circuits also contain stray inductance, device capacitance, stored magnetic energy, and abrupt current change. These non-idealities produce voltage overshoot, current surge, ringing, false triggering, electromagnetic interference, and additional switching loss.

A **snubber circuit** is auxiliary circuitry placed around a switch, transformer, diode, or inductive path to control those transients and redirect stored energy in a controlled way [Rashid, *Power Electronics: Circuits, Devices and Applications, 4e*], [onsemi AN1048/D]. This chapter explains why snubbers are needed, distinguishes turn-ON and turn-OFF stress, and introduces the three foundational protective networks used throughout the subject: the **RC snubber**, the **RCD snubber**, and the **freewheeling diode**. These networks recur in rectifiers, choppers, inverters, battery chargers, PV converters, UPS systems, and auxiliary power supplies.

## Prerequisites check

- You should remember from Chapter 1.2 that an SCR can false-trigger if the voltage across it changes too quickly.
- You should remember from Chapters 1.4 and 1.5 that MOSFETs and IGBTs do not switch instantaneously and that parasitic capacitances influence their switching behavior.
- You should be comfortable with the basic inductor relation that current through an inductor cannot jump suddenly.
- You should know that the energy stored in an inductor is $\tfrac{1}{2}LI^2$.
- You should remember from Chapter 2.1 that driver strength affects $dv/dt$ and $di/dt$, but layout and external protection components matter too.

If the ideas of leakage inductance, Miller effect, or reverse recovery feel weak, a short review of Chapters 1.2, 1.4, 1.5, and 2.1 will make this chapter easier to absorb.

## Core content

### 2.2.1 Need for snubbers; turn-ON and turn-OFF snubbers

#### Why switching stress appears even in a "simple" circuit

Consider a MOSFET switching current through an inductive load in a 48 V battery charger, or an IGBT switching a few amperes in an inverter leg fed from a rectified 230 V, 50 Hz supply. In an ideal circuit, turn-OFF would interrupt current and establish the blocking voltage. In practice, wiring, package leads, PCB traces, transformer leakage paths, and the load all contribute inductance, while the switch node and device terminals contribute capacitance. When the current path is interrupted, the stored magnetic energy in that inductance appears as overvoltage and ringing.

The magnetic energy stored in stray or leakage inductance is

$$\boxed{E_L = \frac{1}{2}L_{\sigma} I^2} \quad \text{(7.1)}$$

where $E_L$ is the energy stored in the stray or leakage inductance, $L_{\sigma}$ is that inductance, and $I$ is the current flowing just before the switching event.

Even a small inductance can store enough energy to produce a severe transient. Suppose the effective stray or leakage inductance is only $2\,\mu\text{H}$ and the current just before turn-OFF is $12 \text{ A}$. Then

$$E_L = \frac{1}{2}\times 2\times 10^{-6}\times 12^2 = 144\times 10^{-6}\text{ J} = 144\,\mu\text{J}.$$

If, for a brief moment, this energy can charge only about $200 \text{ pF}$ of effective node capacitance, the equivalent voltage associated with that energy is

$$V \approx \sqrt{\frac{2E}{C}} = \sqrt{\frac{2\times 144\times 10^{-6}}{200\times 10^{-12}}} \approx 1200 \text{ V}.$$

The exact spike in a practical converter depends on the available parasitic and intentional paths, so the circuit does not necessarily reach $1200 \text{ V}$. The estimate nevertheless shows why a converter operating from a few hundred volts can generate a much larger transient if the stored energy is left to the parasitics alone.

A **snubber circuit** is added to shape this transient by providing a controlled alternative path. Depending on topology, a snubber can

- limit the rate of rise of voltage across a device,
- limit peak overvoltage,
- limit turn-ON current surge,
- reduce ringing,
- reduce false triggering of thyristors,
- reduce stress caused by diode reverse recovery,
- trade a small controlled power loss for a large improvement in device safety [Rashid, *Power Electronics: Circuits, Devices and Applications, 4e*], [onsemi AN1048/D].

Table 7.1 summarizes the main reasons snubbers appear.

Table 7.1: Why snubber circuits are used

| Problem in the power stage | What the snubber tries to do | Typical consequence if no snubber is used |
| --- | --- | --- |
| Stray or leakage inductance stores energy | Provide a controlled path for that energy | Overvoltage spike at turn-OFF |
| Device or load capacitances resonate with inductance | Add damping or clamp voltage | Ringing, EMI, repeated stress |
| SCR or TRIAC sees rapid voltage rise | Reduce effective $dv/dt$ across device | False turn-ON |
| Inductive load current has nowhere to go when switch opens | Provide recirculation path | Very large voltage spike or device avalanche |
| Diode reverse recovery interacts with switch turn-ON | Soften or absorb part of the transient | High turn-ON current stress and noise |

#### What a snubber is

A **snubber circuit** is an auxiliary network placed around a switching element or energy-storage element to control transient voltage, transient current, or oscillation during switching.

The term covers several behaviors. Some snubbers are mainly **dissipative**, absorbing transient energy and converting it into heat in a resistor. Others are mainly **clamping** networks, steering the energy into a capacitor first and removing it later. Some are connected directly across the switch; others are associated mainly with the diode or the inductive load. The freewheeling diode is usually discussed alongside snubbers because it addresses the same switching problem from a different angle: it preserves a current path when the main switch changes state.

In every case, the essential question is the same: where does the stored energy go during the switching interval? If it is forced through a controlled auxiliary path, the stress is usually manageable. If it is left to parasitic inductance and capacitance, the resulting voltage spike and ringing determine the behavior.

#### Turn-OFF stress and turn-OFF snubbers

A **turn-OFF snubber** acts during the interval when the power device is being turned OFF and the current through a stray inductive path attempts to continue flowing. The associated voltage is governed by the inductor relation

$$v_L = L\frac{di}{dt}.$$

If $\tfrac{di}{dt}$ is large and no alternative path exists, the voltage across the switch rises sharply. A turn-OFF snubber softens that event by giving the current a temporary destination. In practice, an RC snubber lets a capacitor absorb part of the sudden voltage rise while the resistor damps the oscillation, an RCD snubber conducts selectively above a clamp condition and diverts the spike into a capacitor, and a clamp or freewheel path can keep the switch from seeing the full stress directly [onsemi AN1048/D], [onsemi AN4137].

The role of the snubber capacitor follows from

$$\boxed{i_C = C\frac{dv}{dt}} \quad \text{(7.2)}$$

or

$$\frac{dv}{dt} = \frac{i_C}{C}.$$

If a transient current must charge a capacitor, a larger capacitance produces a slower voltage rise. That is why a capacitor across a switch can reduce $dv/dt$. The tradeoff is equally important: increasing $C$ lowers $dv/dt$, but it also increases stored energy, dissipation, and the current that may appear when the device turns ON again. Snubber design is therefore always a compromise among stress reduction, loss, cost, and switching behavior [onsemi AN1048/D].

#### Turn-ON stress and turn-ON snubbers

A **turn-ON snubber** acts during the interval when the device is being turned ON. The stress can come from discharge current in a previously charged snubber capacitor, reverse-recovery current in a diode that had been conducting, current surge into a capacitive node, or a large $di/dt$ set by parasitics rather than by the load alone.

ST's application note on gate and base drive emphasizes that, in many inductive-load applications, turn-ON occurs while the freewheeling diode is conducting, so the diode's reverse recovery directly influences current rise and switching loss [ST AN509/1293]. Turn-ON snubbers therefore address current surge rather than turn-OFF overvoltage. Across practical topologies, the detail varies, but the conceptual distinction is stable:

- a turn-OFF snubber mainly restrains voltage rise and turn-OFF spike,
- a turn-ON snubber mainly restrains current surge and turn-ON stress.

**Image prompt for Figure 7.1:** Create a clean textbook-style technical illustration comparing unsnubbed and snubbed switch turn-OFF in an inductive circuit. Show a power switch carrying inductive current, a small stray inductance in the loop, and two aligned voltage waveforms across the switch: one with a sharp overshoot and ringing, one with a slower controlled rise and lower peak due to a snubber. Label stored energy in stray inductance, voltage overshoot, ringing, and controlled transient. Use monochrome engineering style with axes, units, and clear labels.

The remainder of the chapter is organized around three practical networks: the RC snubber, the RCD snubber, and the freewheeling diode.

### 2.2.2 RC and RCD snubber circuits; freewheeling diode

#### RC snubber circuits

The simplest named snubber is the **RC snubber**, a resistor and capacitor connected in series and placed across a device or across a problematic node. The capacitor slows the voltage change because the transient current must charge it first, while the resistor damps oscillation and limits the current that would otherwise flow too sharply into or out of the capacitor.

If only a capacitor were used, the circuit might reduce the initial $dv/dt$ but could also create heavy current pulses and strong resonant ringing with the stray inductance. If only a resistor were used, the voltage spike would usually remain too sharp. The series RC combination is used because it addresses both the first transient and the oscillation that follows.

The RC pair introduces a time constant

$$\boxed{\tau = RC} \quad \text{(7.3)}$$

where $\tau$ is the RC time constant, $R$ is the snubber resistance, and $C$ is the snubber capacitance.

This equation does not by itself design the snubber, but it indicates the basic trend: larger $C$ slows the voltage rise, larger $R$ limits the current pulse and increases damping, and excessive values increase loss or slow the transition more than desired.

##### RC snubbers across thyristors

One classical use of the RC snubber is across an SCR or TRIAC. onsemi's application note AN1048/D describes the simple snubber as a series resistor and capacitor placed around the thyristor, and explains that RC networks are used to control voltage transients that could falsely turn on a thyristor [onsemi AN1048/D].

This remains an important application because the SCR is sensitive to rapid $dv/dt$. If the anode-cathode voltage rises too quickly, the internal junction capacitances can drive enough current into the regenerative structure to trigger the device even without an intentional gate command. In this setting, the RC snubber is used primarily to prevent unwanted turn-ON and control transient behavior, not to improve efficiency.

**Image prompt for Figure 7.2:** Create a textbook-style figure showing an SCR with a series RC snubber connected across anode and cathode. Include a corresponding waveform panel that compares voltage across the SCR with and without the snubber during a transient. Label anode, cathode, gate, snubber resistor, snubber capacitor, false-triggering risk, and reduced $dv/dt$. Use monochrome engineering style with clear engineering labels.

##### RC snubbers across transistor switches

RC snubbers are also used with MOSFETs, IGBTs, and diodes to reduce ringing on a switch node or across a device. In these applications the main objectives are limiting overshoot, damping resonance caused by stray inductance and node capacitance, reducing EMI, and lowering repetitive stress on the semiconductor.

The price is power loss. Every cycle, the snubber capacitor is charged and discharged. A useful first estimate for the average power associated with that repetitive charging is

$$\boxed{P_{RC,\text{approx}} \approx \frac{1}{2}CV^2 f_s} \quad \text{(7.4)}$$

where $P_{RC,\text{approx}}$ is the approximate average snubber-related power, $C$ is the snubber capacitance, $V$ is the voltage swing across it, and $f_s$ is switching frequency.

This is a first estimate rather than a complete exact model, because the real loss distribution depends on topology, waveform, and the extent to which the capacitor charges and discharges in each cycle. It is nevertheless a useful warning sign.

Consider a converter switching at $20 \text{ kHz}$ with an RC snubber capacitor of $1 \text{ nF}$ that experiences about $325 \text{ V}$ each cycle in an off-line stage. Then

$$P_{RC,\text{approx}} \approx \frac{1}{2}\times 1\times 10^{-9}\times 325^2\times 20\times 10^3 \approx 1.06 \text{ W}.$$

This level of dissipation is not negligible. The resistor must be chosen and mounted so that the heat can be removed safely. Because the resistor ultimately absorbs the transient energy, RC snubbers are most suitable where the stress is moderate and the objective is waveform shaping rather than heavy energy clamping.

#### RCD snubber circuits

An **RCD snubber** adds a diode to the resistor-capacitor network so that the clamp acts mainly in one direction. Instead of participating equally in both voltage-rise and voltage-fall events, the network conducts primarily when the node attempts to exceed the safe level in the dangerous direction.

This makes the RCD snubber especially useful in circuits such as the flyback converter primary switch, where transformer leakage inductance produces a turn-OFF spike at the switch drain or collector. In that situation, the switch turns OFF, the leakage inductance attempts to keep current flowing, the switch-node voltage rises, the snubber diode conducts when the clamp condition is reached, the capacitor receives the diverted energy, and the resistor dissipates that energy between switching events. The RCD snubber is therefore a **clamp-plus-dissipation** network rather than a lossless solution [onsemi AN4137].

##### First energy estimate for an RCD snubber

If most of the transformer leakage energy each cycle is dissipated through the RCD network, a useful first estimate is

$$\boxed{P_{RCD,\text{approx}} \approx \frac{1}{2}L_{lk} I_{pk}^2 f_s} \quad \text{(7.5)}$$

where $L_{lk}$ is the leakage inductance, $I_{pk}$ is the peak current present when the switch turns OFF, and $f_s$ is switching frequency.

This estimate shows that the average snubber burden scales directly with leakage inductance, the square of current, and switching frequency. Consider a small isolated auxiliary supply in a wind-converter control cabinet or a PV inverter control board with

- $L_{lk} = 3\,\mu\text{H}$,
- $I_{pk} = 2.5 \text{ A}$,
- $f_s = 65 \text{ kHz}$.

Then

$$P_{RCD,\text{approx}} \approx \frac{1}{2}\times 3\times 10^{-6}\times 2.5^2\times 65\times 10^3 \approx 0.61 \text{ W}.$$

This again is substantial enough to matter thermally, and it shows directly that reducing transformer leakage inductance reduces snubber burden.

##### Selective clamping in practice

Compared with a simple RC network across a switch, the RCD clamp need not participate equally in the benign part of the cycle. The diode makes the response directional, reduces unnecessary current, and improves control of peak voltage in one-sided turn-OFF transients. This selectivity is why RCD networks are common around flyback primary switches, while simple RC networks are more often used for $dv/dt$ control or damping across SCRs, TRIACs, MOSFETs, or diodes [Fairchild AN-6014].

**Image prompt for Figure 7.3:** Create a textbook-style schematic of a flyback converter primary showing a MOSFET switch, transformer primary, leakage inductance indicated, and an RCD snubber made of diode $D_{sn}$, capacitor $C_{sn}$, and resistor $R_{sn}$ connected as a clamp from the switch node to the DC input rail. Add a waveform panel showing drain voltage rising to reflected output voltage plus input voltage, then a leakage-induced spike, with the RCD clamp limiting the peak. Label all parts, polarities, and current path during turn-OFF. Use monochrome engineering style.

##### Reading an RCD snubber in a flyback schematic

In a flyback converter schematic, the group $R_{sn}$, $C_{sn}$, and $D_{sn}$ placed near the primary switch node immediately identifies the problem being addressed: primary-side turn-OFF overvoltage rather than low-voltage output ripple. The orientation of $D_{sn}$ shows that the network is a directional clamp, not a continuously active RC damper. During the spike, $C_{sn}$ receives the diverted leakage energy; between switching events, $R_{sn}$ dissipates it. The network is therefore a controlled destination for leakage-inductance energy when the primary switch turns OFF [onsemi AN4137].

This arrangement appears frequently in small isolated auxiliary supplies inside PV inverters, wind converters, EV chargers, and UPS hardware, where the main system may operate from a high-voltage bus but the control electronics still require low-voltage isolated rails.

#### The freewheeling diode

The **freewheeling diode**, also called a **flyback diode** or **freewheel diode**, provides a recirculating path for inductive current when the controlled switch turns OFF. Its function differs from that of an RC or RCD snubber. A snubber primarily shapes or clamps a transient; a freewheeling diode primarily preserves current continuity in an inductive path.

When the switch controlling an inductive current turns OFF, the inductor current cannot instantly become zero. If a diode is connected so that it becomes forward-biased at that moment, the current continues through the load and diode instead of forcing the switch voltage to rise destructively. This function is fundamental in DC choppers, buck converters, motor drives, relay and solenoid circuits, inverter legs during dead time, and other commutation paths [Mohan, Undeland, Robbins, *Power Electronics*], [ST STTH60AC06C Product Page].

Manufacturer literature commonly identifies ultrafast and SiC devices for freewheeling service, which reflects how standard this role is in practical converter design [ST STTH60AC06C Product Page], [ST STPSC40065C Product Page].

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

Selection of the diode itself depends on repetitive reverse-voltage rating, average and peak forward current, reverse-recovery behavior, and thermal capability. At high switching frequency, ultrafast, Schottky, and silicon-carbide diodes are often preferred because reverse recovery directly affects switching stress and ringing [ST STPSC40065C Product Page]. ST's drive note makes the same point from the transistor side: at turn-ON, the switching device often encounters the recovery behavior of the conducting freewheeling diode [ST AN509/1293].

Table 7.2 summarizes the three main protective networks in this chapter.

Table 7.2: RC snubber, RCD snubber, and freewheeling diode compared

| Network | Main purpose | Main strength | Main tradeoff | Typical place |
| --- | --- | --- | --- | --- |
| RC snubber | Reduce $dv/dt$ and damp ringing | Simple and widely applicable | Continuous loss and extra turn-ON burden | Across SCR, TRIAC, switch, or diode |
| RCD snubber | Clamp overvoltage more selectively | Better suited to leakage-spike control | Dissipates leakage energy and needs tuning | Flyback primary switch, clamp node |
| Freewheeling diode | Provide path for inductive current after switch state change | Strong reduction of voltage stress from interrupted load current | Slow current decay if clamp voltage is low | Across inductive load or as recirculation path in converter leg |

In a small isolated flyback auxiliary supply inside a grid-tied PV inverter, an RCD snubber is commonly used to keep the primary-switch drain spike within safe limits. In a buck converter charging a battery, the freewheeling diode is part of the basic current path after the main switch turns OFF. If switching frequency is high and ringing remains problematic, an additional RC snubber may still be required. The correct choice follows the transient problem being solved in that topology.

## How this matters in renewable-energy systems

Snubber circuits are closely tied to renewable-energy reliability because these converters switch substantial current repeatedly, often for many hours each day and under demanding thermal conditions. In solar PV systems, snubbers appear in isolated auxiliary supplies, DC-DC stages, and inverter legs to keep switching stress within device limits and to reduce ringing that would otherwise worsen EMI. In battery chargers and battery-energy-storage converters, freewheeling paths and snubbers determine how safely inductor current commutates when switches change state. In wind-energy converters, transformer leakage inductance and converter-leg stray inductance make overvoltage control essential.

The system-level issue is not only efficiency. Robustness, service life, and electromagnetic behavior are equally important. A converter that is slightly more efficient on paper but suffers repeated overshoot, diode-recovery stress, or false triggering is not a better converter in practice. Snubbers are one of the main points at which transient control, reliability, and electromagnetic performance meet.

## Chapter summary

- A **snubber circuit** is auxiliary circuitry used to control transient voltage, transient current, or oscillation during switching [Rashid, *Power Electronics: Circuits, Devices and Applications, 4e*].
- Snubbers are needed because real power circuits contain stray or leakage inductance, capacitance, stored energy, and non-instantaneous switching transitions.
- The energy stored in stray or leakage inductance is $\boxed{E_L=\tfrac{1}{2}L_{\sigma}I^2}$ from Equation (7.1).
- A capacitor can reduce voltage-rise rate because $\boxed{i_C=C\,dv/dt}$ from Equation (7.2).
- A **turn-OFF snubber** mainly reduces voltage overshoot and turn-OFF stress, whereas a **turn-ON snubber** mainly reduces current surge and turn-ON stress.
- A series **RC snubber** uses the capacitor to slow the transient and the resistor to damp it; its time constant is $\boxed{\tau=RC}$ from Equation (7.3).
- A useful first estimate of repetitive RC-snubber power is $\boxed{P_{RC,\text{approx}}\approx \tfrac{1}{2}CV^2f_s}$ from Equation (7.4).
- An **RCD snubber** adds a diode so that the clamp acts more selectively, which is especially useful for leakage-induced turn-OFF spikes in flyback converters [onsemi AN4137].
- A useful first estimate of RCD-snubber dissipation is $\boxed{P_{RCD,\text{approx}}\approx \tfrac{1}{2}L_{lk}I_{pk}^2f_s}$ from Equation (7.5).
- A **freewheeling diode** provides a safe recirculating path for inductive current when the main switch changes state.
- A first current-decay estimate in a diode freewheel path is $\boxed{di/dt\approx -V_F/L}$ from Equation (7.6).
- Freewheeling diodes reduce voltage stress strongly, but the low clamp voltage leads to slower current decay; diode reverse recovery therefore remains an important part of switch stress.

## Further reading

- [onsemi, *AN1048/D: RC Snubber Networks for Thyristor Power Control and Transient Suppression*](https://www.onsemi.com/download/application-notes/pdf/an1048-d.pdf) - A very useful classic reference for understanding why snubbers are needed, especially for SCR $dv/dt$ control and the tradeoffs involved.
- [onsemi, *AN4137: Design Guidelines for Off-line Flyback Converters Using Fairchild Power Switch*](https://www.onsemi.com/pub/Collateral/AN-4137.pdf) - Helpful for seeing an RCD snubber in a real flyback schematic and understanding its place in practical converter design.
- [Fairchild Semiconductor, *AN-6014: Green Current Mode PWM Controller FAN7602*](https://www.onsemi.com/download/application-notes/pdf/an-6014.pdf) - Useful because it distinguishes diode RC snubber design from MOSFET RCD snubber design in a real SMPS design context.
- [STMicroelectronics, *Influence of gate and base drive on power switch behaviour*](https://www.st.com/resource/en/application_note/cd00003914-influence-of-gate-and-base-drive-on-power-switch-behaviour-stmicroelectronics.pdf) - Especially useful for the link between switch turn-ON stress and the reverse recovery of the conducting freewheeling diode.
- M. H. Rashid, *Power Electronics: Circuits, Devices and Applications*, 4th ed. - A strong textbook reference for the broader role of snubbers, freewheeling diodes, and switching-stress control across converter families.
