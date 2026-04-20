# Chapter 4.3: Isolated DC-DC Converters (Overview)

## Chapter opening

Chapter 4.2 examined non-isolated DC-DC converters such as buck, boost, buck-boost, Cuk, and SEPIC converters. Those circuits are indispensable, but they share one basic feature: the input and output are connected by a continuous conducting path. In many applications that arrangement is acceptable. In others, voltage conversion is required together with electrical separation between the two sides.

That separation is provided by **galvanic isolation**. An isolated DC-DC converter inserts an isolation barrier between source and load while still transferring power from one side to the other. This chapter introduces the purpose of galvanic isolation, the role of the transformer in isolated conversion, the operating ideas of the **flyback** and **forward** converters, and the topology-level differences among **push-pull**, **half-bridge**, and **full-bridge** converters. The emphasis is on clear topology understanding rather than detailed magnetic design or advanced control [Erickson and Maksimovic, *Fundamentals of Power Electronics*, 2e], [Mohan, Undeland, Robbins, *Power Electronics: Converters, Applications, and Design*, 3e].

## Prerequisites check

- duty cycle, switching period, and ON-state/OFF-state operation from Chapter 4.1
- non-isolated buck and buck-boost operation from Chapter 4.2
- the basic behavior of inductors and capacitors in switching circuits
- the ideal-transformer turns-ratio relation
- the fact that a transformer cannot transfer steady DC directly

## Core content

### 4.3.1 Need for galvanic isolation in renewable-energy and battery-charging systems

#### A first physical picture

Consider a battery energy storage system with a DC bus around $400 \text{ V}$ and a control board that requires an isolated $15 \text{ V}$ auxiliary supply for gate drivers, sensing circuits, or protection hardware. Numerically, this appears to be an ordinary step-down task. Electrically, it is not. The low-voltage electronics may need to remain separated from the high-voltage bus for safety, ground-reference control, noise management, or system-architecture reasons. The problem is therefore not merely "400 V to 15 V," but "400 V to 15 V across an isolation barrier."

**Galvanic isolation** means that there is no direct conducting path for DC current between two circuits. Analog Devices defines it as a design technique that separates electrical circuits so that stray currents are blocked even though signals or power may still cross the barrier by a non-conductive coupling method [Analog Devices, "Galvanic Isolation" glossary]. In isolated power converters, that coupling method is usually magnetic coupling through a transformer.

#### What isolation does and does not do

Isolation provides several useful functions:

- it removes a direct conductive path between input and output
- it improves safety when one side may be at hazardous potential
- it helps break ground loops and reduce unwanted common-ground coupling
- it allows the output to float with respect to the input when required
- it allows the transformer turns ratio to assist voltage conversion
- it can support multiple isolated outputs from one switching stage

Isolation does not guarantee ideal behavior. It does not eliminate parasitic capacitance, all noise coupling, or the need for proper creepage, clearance, shielding, and insulation design. Nor does the mere presence of a transformer automatically satisfy safety requirements. The barrier must be designed correctly in the finished hardware.

#### Why a transformer appears in isolated DC-DC conversion

In ordinary power systems, a transformer transfers energy by magnetic coupling between windings. For an ideal transformer,

$$\boxed{\frac{V_s}{V_p} = \frac{N_s}{N_p}} \quad \text{(15.1)}$$

where $V_p$ and $V_s$ are the primary-side and secondary-side voltages, and $N_p$ and $N_s$ are the corresponding numbers of turns.

The turns-ratio relation is familiar, but it comes with an important condition: the transformer requires changing magnetic flux. A steady DC voltage applied directly to the primary does not produce normal transformer action; instead, it drives magnetizing current toward a dangerous condition. For that reason, an isolated DC-DC converter cannot feed a transformer from an unchanging DC source.

The converter therefore performs three distinct functions:

1. it converts the DC input into a high-frequency switched waveform
2. it transfers energy across the isolation barrier through the transformer
3. it rectifies and filters the secondary-side waveform back into DC

This sequence is the basic conceptual model for isolated DC-DC conversion [MIT OCW, 6.334 *Power Electronics*, ch7 notes], [Erickson and Maksimovic, *Fundamentals of Power Electronics*, 2e].

**Image prompt for Figure 15.1:** Create a clean textbook-style block-level technical illustration of an isolated DC-DC converter. Show a DC input source on the left, a switching stage that converts DC into a high-frequency pulsating waveform, a transformer in the center with a clearly marked isolation barrier between primary and secondary, and a rectifier plus output filter on the right producing DC output. Add arrows showing energy flow left to right. Label the primary side, secondary side, isolation barrier, turns ratio $N_p:N_s$, and indicate that the output may float with respect to the input ground. Use monochrome textbook engineering style with clear labels.

#### Why renewable-energy and battery systems need isolation

The need for isolation becomes clearer in real systems. In a **battery charger**, the battery side or user-accessible side may need to remain separated from a higher-voltage input side. In a **solar inverter**, isolated auxiliary supplies often power control and gate-drive circuits that operate near a high-voltage DC link. In an **EV**, high-voltage traction hardware coexists with low-voltage control and measurement electronics, making isolated supplies and isolated sensing channels essential [TI, TIDA-01513 reference design], [TI, PMP22288 reference design].

Isolation also serves measurement and noise-control purposes. Renewable-energy hardware contains fast switching transitions, long cable runs, common-mode voltage swings, and sensitive low-level electronics. Functional isolation can prevent one noisy ground domain from directly disturbing another [Analog Devices, "Easy Galvanic Isolation"], [Analog Devices, "Galvanic Isolation" glossary].

Transformers add another practical advantage: one switching stage can produce multiple outputs by means of additional secondary windings. That feature is particularly useful in auxiliary-supply design, where several isolated rails may be required from a single converter stage.

#### A numerical reminder about turns ratio

Suppose a transformer in an isolated converter has $N_p = 40$ turns and $N_s = 10$ turns. Then

$$\frac{N_s}{N_p} = \frac{10}{40} = 0.25.$$

If the primary-side applied waveform has an ideal amplitude of $80 \text{ V}$ during one interval, the corresponding ideal secondary-side amplitude during that interval is

$$V_s = 0.25 \times 80 = 20 \text{ V}.$$

This value is not the final DC output. The rectifier arrangement, duty cycle, filter, and converter topology also affect the average output voltage. The example simply shows why isolated converters are attractive for large conversion ratios: turns ratio and duty cycle can share the conversion task instead of leaving it entirely to duty cycle [Analog Devices, "Isolated Switch-Mode Power Supplies: How to Choose a Forward vs. a Flyback Converter", 2024].

### 4.3.2 Flyback converter - topology and applications

#### Topology idea

The **flyback converter** is usually the first isolated topology studied in detail because it combines galvanic isolation, step-up or step-down capability, and relatively low circuit count. At an introductory level, it is best understood as the isolated relative of the buck-boost converter. Like the buck-boost converter, it stores energy during one part of the switching cycle and delivers that energy during another part. The difference is that the magnetic element is a coupled structure with isolated windings rather than a single inductor [Erickson and Maksimovic, *Fundamentals of Power Electronics*, 2e], [MIT OCW, 6.334 *Power Electronics*, ch7 notes].

Analog Devices summarizes the essential behavior concisely: energy is stored during the ON interval and transferred to the output during the OFF interval [Analog Devices, "Isolated Switch-Mode Power Supplies: How to Choose a Forward vs. a Flyback Converter", 2024].

#### The ON interval

During the switch ON interval, the primary winding is connected to the input source. Because of the winding polarity and rectifier arrangement, the secondary diode is reverse biased. The secondary therefore does not deliver power directly to the load in the simplest flyback model.

Instead, current builds in the transformer's **magnetizing inductance**, and energy is stored in the magnetic field. During this interval the output capacitor supports the load.

#### The OFF interval

When the switch turns OFF, the primary current can no longer continue through the switch path. The magnetic field begins to collapse, the winding voltages reverse as required to maintain current continuity, and the secondary diode becomes forward biased. The stored energy is then delivered to the output capacitor and the load.

The operating idea is therefore simple:

- ON interval: energy storage
- OFF interval: energy transfer to the output

That timing is the defining difference between the flyback and the forward converter. In a flyback converter, the main transfer to the output occurs during the OFF interval.

**Image prompt for Figure 15.2:** Create a clean textbook-style technical illustration of an isolated flyback converter. Show an input DC source, a primary-side controlled switch, a flyback transformer with dotted polarity marks, a secondary-side diode, output capacitor, and load. Beside the circuit, show two operating states labeled ON interval and OFF interval. In the ON interval, indicate increasing primary magnetizing current and reverse-biased secondary diode. In the OFF interval, indicate reversed winding polarity, forward-biased secondary diode, and current flowing to the output capacitor and load. Add aligned waveforms for gate signal, primary current, and secondary diode current. Use monochrome engineering style with clear labels.

#### A simple ideal gain relation

For the ideal flyback converter operating in continuous-conduction mode,

$$\boxed{\frac{V_o}{V_{in}} = \frac{N_s}{N_p}\frac{D}{1-D}} \quad \text{(15.2)}$$

where $V_{in}$ is the input voltage, $V_o$ is the average output voltage, $N_p$ and $N_s$ are the primary and secondary turns, and $D$ is the duty cycle.

The relation follows from volt-second balance on the magnetizing inductance. During the ON interval,

$$v_{Lm,\text{ON}} = V_{in}. \quad \text{(15.3)}$$

During the OFF interval, the output voltage is reflected to the primary side through the turns ratio, giving

$$v_{Lm,\text{OFF}} = -\frac{N_p}{N_s}V_o. \quad \text{(15.4)}$$

In steady periodic operation, the average voltage across the magnetizing inductance over one switching period must be zero:

$$D(V_{in}) + (1-D)\left(-\frac{N_p}{N_s}V_o\right) = 0. \quad \text{(15.5)}$$

Rearranging,

$$DV_{in} = (1-D)\frac{N_p}{N_s}V_o$$

and therefore

$$\boxed{V_o = V_{in}\frac{N_s}{N_p}\frac{D}{1-D}} \quad \text{(15.6)}$$

The equation shows that both the transformer turns ratio and the duty cycle contribute to the voltage conversion.

#### A numerical example

Suppose an auxiliary isolated supply must produce $15 \text{ V}$ from a $48 \text{ V}$ DC source, and the flyback transformer has

$$\frac{N_s}{N_p} = \frac{1}{3}.$$

Using Equation (15.6),

$$15 = 48 \times \frac{1}{3} \times \frac{D}{1-D}.$$

Since $48 \times \dfrac{1}{3} = 16$,

$$15 = 16\frac{D}{1-D}.$$

Thus,

$$\frac{D}{1-D} = \frac{15}{16} = 0.9375.$$

Solving for $D$,

$$D = 0.9375(1-D)$$

$$D = 0.9375 - 0.9375D$$

$$1.9375D = 0.9375$$

$$D \approx 0.484.$$

The ideal duty cycle is therefore about $48.4\%$. The result is moderate because the turns ratio already contributes substantially to the conversion.

#### Applications and design perspective

At introductory level, the flyback converter is attractive because it uses relatively few components, provides isolation, accommodates step-up or step-down conversion, and extends naturally to multiple outputs through additional secondary windings. Those features make it particularly common in low-power and auxiliary supplies [Analog Devices, "Isolated Switch-Mode Power Supplies: How to Choose a Forward vs. a Flyback Converter", 2024].

TI's **PMP22288** reference design is a representative example: a 15 W isolated flyback supply for automotive inverter power, with a wide $40 \text{ V}$ to $550 \text{ V}_{DC}$ input range and an isolated $15 \text{ V}$ output at up to $1 \text{ A}$ [TI, PMP22288 reference design]. This is not a main traction power stage. It is the kind of isolated auxiliary supply used to support the electronics around the main power stage.

The main conceptual caution is that the flyback magnetic element should not be imagined as an ordinary transformer delivering power continuously from primary to secondary. In flyback operation, energy is stored during one interval and released during another. The output capacitor remains essential for output smoothing.

### 4.3.3 Forward converter - topology and applications

#### Topology idea

The **forward converter** also uses a transformer for isolation, but its energy-transfer mechanism differs fundamentally from the flyback converter. In the forward converter, the transformer is not the main energy-storage element. Energy is transferred directly to the secondary during the ON interval [Analog Devices, "Isolated Switch-Mode Power Supplies: How to Choose a Forward vs. a Flyback Converter", 2024].

At introductory level, the forward converter is best viewed as the isolated relative of the buck converter. The transformer provides isolation and turns-ratio scaling, while the output inductor and capacitor smooth the transferred energy on the secondary side [MIT OCW, 6.334 *Power Electronics*, ch7 notes], [Mohan, Undeland, Robbins, *Power Electronics: Converters, Applications, and Design*, 3e].

#### ON interval

When the primary switch turns ON, the transformer primary is excited and the output-side rectifier becomes forward biased. Energy is transferred immediately through the transformer to the secondary side. The output inductor stores part of that energy and helps smooth the load current.

In contrast with the flyback converter, the load is supplied during the ON interval itself.

#### OFF interval

When the switch turns OFF, the direct primary-to-secondary transfer stops. The output inductor current cannot collapse instantly, so it continues through a freewheeling path on the secondary side and supports the load during the OFF interval. In that respect, the forward converter closely resembles a buck converter.

There is also an important magnetic requirement: the transformer core must be reset or demagnetized properly before the next cycle. Without a reset mechanism, flux can build from cycle to cycle and eventually drive the core toward saturation. At this stage, it is enough to recognize that practical forward converters require a reset arrangement.

#### Ideal gain relation

For the ideal forward converter operating in continuous-conduction mode,

$$\boxed{\frac{V_o}{V_{in}} = D\frac{N_s}{N_p}} \quad \text{(15.7)}$$

This resembles the buck-converter gain relation, scaled by the transformer turns ratio.

The relation follows from volt-second balance on the output inductor. During the ON interval, the applied secondary-side voltage is approximately

$$V_{sec} = \frac{N_s}{N_p}V_{in}. \quad \text{(15.8)}$$

So the output inductor sees

$$v_{L,\text{ON}} = \frac{N_s}{N_p}V_{in} - V_o. \quad \text{(15.9)}$$

During the OFF interval, the freewheeling path maintains inductor current and the inductor voltage is approximately

$$v_{L,\text{OFF}} = -V_o. \quad \text{(15.10)}$$

Applying volt-second balance,

$$D\left(\frac{N_s}{N_p}V_{in} - V_o\right) + (1-D)(-V_o) = 0. \quad \text{(15.11)}$$

Expanding the expression,

$$D\frac{N_s}{N_p}V_{in} - DV_o - V_o + DV_o = 0.$$

Hence

$$D\frac{N_s}{N_p}V_{in} - V_o = 0,$$

and therefore

$$\boxed{V_o = D\frac{N_s}{N_p}V_{in}} \quad \text{(15.12)}$$

#### A numerical example

Suppose an isolated forward converter must produce $12 \text{ V}$ from a $48 \text{ V}$ input, and the transformer turns ratio is

$$\frac{N_s}{N_p} = \frac{1}{2}.$$

Using Equation (15.12),

$$12 = D \times \frac{1}{2} \times 48.$$

Since $\dfrac{1}{2} \times 48 = 24$,

$$12 = 24D,$$

so

$$D = \frac{12}{24} = 0.5.$$

This example again shows that turns ratio and duty cycle share the voltage-conversion task.

#### Applications and design perspective

The forward converter is often chosen when higher output current or higher output power is required than a simple flyback can comfortably provide. Because energy is transferred directly to the output during the ON interval rather than being stored and released in flyback fashion, the topology is usually better suited to increased load current and power [Analog Devices, "Isolated Switch-Mode Power Supplies: How to Choose a Forward vs. a Flyback Converter", 2024].

The improvement comes with greater circuit complexity. A forward converter typically requires an output inductor and a transformer reset arrangement in addition to the isolation transformer itself.

Forward converters therefore occupy an important middle region: more capable than the simplest flyback implementations, but not yet in the highest-power bridge family. They appear in isolated industrial power supplies, charger subassemblies, telecom-style supplies, and auxiliary stages that require tighter output behavior and stronger current capability [TI, UCC28250 product page].

The main conceptual mistake is to treat the forward converter as a flyback converter with an added output inductor. The timing of energy transfer is different, and the reset requirement is fundamental to the topology.

### 4.3.4 Push-Pull, Half-Bridge and Full-Bridge isolated converters - topology-level comparison

#### Why these topologies are grouped together

Flyback and forward converters are **single-ended** isolated topologies. Their active interval mainly excites the primary in one direction, and the remainder of the cycle handles energy release or magnetic reset. **Push-pull**, **half-bridge**, and **full-bridge** converters are commonly introduced together because they are **double-ended** topologies: the transformer primary is driven in alternating polarities over the switching cycle. This tends to use the magnetic core more effectively and makes these topologies suitable for higher power than the simplest isolated single-ended converters [MIT OCW, 6.334 *Power Electronics*, ch7 notes], [TI, UCC28250 product page].

The discussion here remains at topology-comparison level.

#### Push-pull converter

In the **push-pull converter**, two switches alternately drive a center-tapped primary or an equivalent arrangement. During one interval one half of the primary is energized; during the next interval the other half is energized with opposite polarity.

Its main attraction is that the transformer is driven in both directions, improving core utilization. The active half-winding also sees the full input voltage, which can be useful at comparatively low DC input voltages.

The topology demands careful balance. Timing mismatch or transformer asymmetry can drive the flux toward saturation, and practical switch voltage stress can be substantial when leakage-induced spikes are included.

#### Half-bridge converter

In the **half-bridge converter**, two switches drive the transformer primary from a split bus or midpoint arrangement. The primary typically sees approximately $+\dfrac{V_{in}}{2}$ and $-\dfrac{V_{in}}{2}$ in alternating intervals.

The half-bridge offers double-ended transformer excitation with fewer primary switches than a full bridge. It is often a compromise among component count, device stress, transformer utilization, and power capability. TI's LM5036 product page identifies half-bridge, full-bridge, and push-pull as supported topologies for high-density DC-DC conversion [TI, LM5036 product page].

Because only half the bus is applied across the primary during each active interval, transformer turns ratio and current levels must be selected accordingly.

#### Full-bridge converter

In the **full-bridge converter**, four switches drive the transformer primary so that the full input voltage can be applied across the primary in both polarities: $+V_{in}$ in one interval and $-V_{in}$ in another.

This gives strong transformer utilization and makes the full bridge a common choice for higher-power isolated conversion. The tradeoff is increased hardware and control complexity: more switches, more gate-drive circuitry, and tighter control of dead time and switching transitions.

TI's **PMP8877** reference design illustrates the kind of application in which a full bridge becomes attractive. TI describes it as an isolated DC/DC power module using a hard-switching full-bridge topology to deliver about $180 \text{ W}$ nominally, with tabulated values of $12 \text{ V}$ output, up to $18 \text{ A}$, and about $216 \text{ W}$ maximum output from a $36 \text{ V}$ to $75 \text{ V}$ input range [TI, PMP8877 reference design].

#### Comparison table

Table 15.1 organizes the topology-level differences discussed in this chapter.

Table 15.1: Topology-level comparison of isolated converter families in this chapter

| Topology | Beginner mental model | Main energy-transfer idea | Relative complexity | Typical role in a system |
| --- | --- | --- | --- | --- |
| Flyback | Isolated buck-boost | Store during ON, deliver during OFF | Low | Low-power or auxiliary isolated supplies |
| Forward | Isolated buck | Transfer during ON, freewheel during OFF | Moderate | Isolated supplies with better current capability |
| Push-pull | Double-ended transformer drive with two switches | Alternate primary excitation using two halves | Moderate to high | Medium-power isolated conversion, often with lower-voltage input |
| Half-bridge | Double-ended bridge using two switches and split bus | Alternate $\pm V_{in}/2$ across primary | Moderate to high | Medium- to higher-power isolated supplies |
| Full-bridge | Double-ended bridge using four switches | Alternate $\pm V_{in}$ across primary | High | Higher-power isolated conversion |

These are early selection guidelines rather than rigid rules. Real design choices also depend on input-voltage range, output power, efficiency target, EMI limits, cost, control method, magnetic design, and safety requirements.

**Image prompt for Figure 15.3:** Create a clean textbook-style comparison figure for isolated converter topologies. Show simplified labeled circuit blocks for push-pull, half-bridge, and full-bridge isolated converters side by side. For each topology, include a small accompanying primary-voltage waveform sketch showing the transformer primary excitation polarity over time. Clearly label the number of active switches, whether the transformer sees approximately $\pm V_{in}$ or $\pm V_{in}/2$, and note that these are topology-level conceptual views, not complete detailed schematics. Use monochrome engineering style with consistent layout and annotations.

Bridge-family converters should not be viewed as merely larger flybacks. Their primary excitation pattern, magnetic utilization, and hardware requirements are different. More switches also do not automatically guarantee higher efficiency; the result depends on the complete design.

## Worked interpretation exercise

### Reading a real isolated flyback reference design

TI's **PMP22288** reference design, titled *15-W flyback reference design for automotive inverter power*, provides a useful example of how topology, rating, and application context fit together [TI, PMP22288 reference design].

TI lists the following key items:

- topology: **Flyback - DCM**
- input range: $40 \text{ V}$ to $550 \text{ V}$
- output: isolated $15 \text{ V}$, up to $1 \text{ A}$
- output power: $15 \text{ W}$
- peak efficiency: $86\%$
- application note: automotive inverter power

These specifications point clearly to an **auxiliary isolated supply**, not a main propulsion or main inverter power stage. The 15 W rating is modest, the isolated 15 V output is typical of bias and support functions, and the very wide input range indicates operation in a harsh high-voltage electrical environment.

The listing of **flyback - DCM** is also instructive. It matches the chapter's description of the flyback converter as a practical choice for low-power isolated supplies, and it shows that real designs often use discontinuous-conduction-mode operation at lower power levels. Detailed DCM analysis is beyond the present chapter, but the reference design shows how the topology appears in practice.

The broader interpretive point is straightforward: when reading an isolated-converter design, first identify the power level, the electrical environment, the reason isolation is required, and whether the chosen topology suits that role. For PMP22288, the answer is yes. It is a wide-input isolated auxiliary supply for inverter electronics, and a flyback topology is a sensible choice for that application.

## How this matters in renewable-energy systems

Isolated DC-DC converters appear throughout renewable-energy and electrified systems even when they are not the most visible part of the product. In **solar PV inverters**, isolated auxiliary supplies power control boards, sensing circuits, communication hardware, and gate drivers. In **battery chargers**, isolation supports safety, grounding strategy, and separation between a higher-voltage input side and battery-side electronics. In **battery energy storage systems**, isolated low-power rails support monitoring, balancing, and supervisory electronics. In **EV power stages**, isolated converters support gate-drive supplies, measurement domains, and high-voltage-to-low-voltage control interfaces [TI, PMP22288 reference design], [TI, TIDA-01513 reference design].

Topology choice is strongly linked to system role and power level. A **flyback** converter is often appropriate for a low-power isolated bias supply. A **forward** converter becomes more attractive as output-current demand rises. **Half-bridge** and **full-bridge** converters become increasingly attractive when isolated power increases and transformer utilization becomes more important. TI's PMP8877 full-bridge module is a useful example of that progression [TI, PMP8877 reference design].

The main system-level point is that renewable-energy hardware is not defined only by its main kilowatt-scale power path. It also depends on smaller isolated supplies that allow the main system to switch, sense, communicate, protect itself, and remain electrically safe.

## Chapter summary

- **Galvanic isolation** removes the direct conductive DC path between input and output while still allowing power transfer across a barrier, usually through a transformer.
- An isolated DC-DC converter works by switching DC into a high-frequency waveform, transferring energy through a transformer, and rectifying and filtering the secondary-side waveform back into DC.
- A transformer cannot transfer steady DC directly; isolated DC-DC conversion therefore requires switching action.
- The ideal transformer relation is $\dfrac{V_s}{V_p} = \dfrac{N_s}{N_p}$.
- A **flyback converter** stores energy during the ON interval and delivers it to the output during the OFF interval.
- For an ideal CCM flyback converter, $\dfrac{V_o}{V_{in}} = \dfrac{N_s}{N_p}\dfrac{D}{1-D}$.
- A **forward converter** transfers energy to the output during the ON interval and uses an output-inductor freewheeling path during the OFF interval.
- For an ideal CCM forward converter, $\dfrac{V_o}{V_{in}} = D\dfrac{N_s}{N_p}$.
- **Push-pull**, **half-bridge**, and **full-bridge** converters are double-ended isolated topologies that drive the transformer primary in alternating polarities.
- Isolated converter choice depends strongly on role, output power, current demand, and required complexity.
- In renewable-energy and EV systems, isolated converters commonly support gate drivers, measurement domains, communication hardware, control boards, and charger auxiliaries.

## Further reading

1. Robert W. Erickson and Dragan Maksimovic, *Fundamentals of Power Electronics*, 2nd ed.  
   A strong foundational text for understanding flyback, forward, and bridge converters from first principles.

2. Ned Mohan, Tore M. Undeland, and William P. Robbins, *Power Electronics: Converters, Applications, and Design*, 3rd ed.  
   A classic text that connects topology operation to practical application choices very well.

3. MIT OpenCourseWare, 6.334 *Power Electronics*, ch7 lecture notes.  
   Useful notes specifically covering isolated DC/DC converters, flyback converters, single-ended forward converters, and double-ended converters.

4. Analog Devices, "Isolated Switch-Mode Power Supplies: How to Choose a Forward vs. a Flyback Converter" (2024), and "Galvanic Isolation" glossary entry.  
   Good modern, readable references for the practical differences between isolation, flyback, and forward approaches.

5. Texas Instruments, PMP22288 reference design, PMP8877 reference design, and UCC28250 / LM5036 product pages.  
   These are excellent real-world examples showing how isolated flyback, half-bridge, and full-bridge ideas appear in commercial and reference hardware.
