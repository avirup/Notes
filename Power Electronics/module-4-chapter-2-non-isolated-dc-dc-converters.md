# Chapter 4.2: Non-isolated DC-DC Converters

## Chapter opening

Chapter 4.1 introduced the general idea of DC choppers: a power switch controls the average output by alternating between ON and OFF states rather than by operating in a lossy partially conducting region. Non-isolated DC-DC converters are the practical circuit forms built on that idea.

The principal non-isolated topologies are the **buck**, **boost**, **buck-boost**, **Cuk**, and **SEPIC** converters. All use the same basic elements, namely a controlled switch, a diode or synchronous switch, an inductor, a capacitor, and a load. Their behavior differs because these elements are connected in different ways. One topology steps voltage down, another steps it up, another can do either while inverting polarity, and others improve current smoothness or provide both step-up and step-down action without polarity inversion.

These converters are fundamental in renewable-energy and electrified systems because DC voltage is rarely fixed at a single useful value. PV voltage varies with irradiance and temperature, battery voltage varies with state of charge, and electronic subsystems often require several lower regulated rails from a larger DC source. Non-isolated converters provide efficient conversion between such levels [Mohan, Undeland, Robbins, *Power Electronics: Converters, Applications, and Design*, 3e], [Erickson and Maksimovic, *Fundamentals of Power Electronics*, 2e].

## Prerequisites check

- Duty cycle: $D = T_{ON}/T$
- Basic inductor behavior: current cannot change instantaneously
- Basic capacitor behavior: voltage cannot change instantaneously
- Need for a current path during the OFF interval in inductive circuits
- Distinction between instantaneous and average quantities
- Ideal converter equations as first approximations rather than exact hardware models

If the ON-interval/OFF-interval picture from Chapter 4.1 is not yet comfortable, that chapter should be reviewed before continuing.

## Core content

Table 14.1 provides a first comparison of the common non-isolated converters under ideal CCM conditions.

Table 14.1: First comparison of common non-isolated DC-DC converters under ideal CCM assumptions

| Topology | Main function | Ideal voltage gain | Output polarity relative to input ground | Practical note |
| --- | --- | --- | --- | --- |
| Buck | Step down | $\dfrac{V_o}{V_{in}} = D$ | Same polarity | Widely used for point-of-load and auxiliary supplies |
| Boost | Step up | $\dfrac{V_o}{V_{in}} = \dfrac{1}{1-D}$ | Same polarity | Common when a lower source must feed a higher DC bus |
| Buck-Boost | Step down or step up | $\dfrac{V_o}{V_{in}} = -\dfrac{D}{1-D}$ | Inverted | Useful when a negative output is acceptable or required |
| Cuk | Step down or step up | $\dfrac{V_o}{V_{in}} = -\dfrac{D}{1-D}$ | Inverted | Input and output currents are smoother than in the simple buck-boost |
| SEPIC | Step down or step up | $\dfrac{V_o}{V_{in}} = \dfrac{D}{1-D}$ | Same polarity | Useful when the input can move above and below the target output |

Here, $V_{in}$ is the input voltage, $V_o$ is the average output voltage, and $D$ is the duty cycle. The table assumes **continuous conduction mode (CCM)**, meaning that inductor current does not fall to zero within a switching period [Erickson and Maksimovic, *Fundamentals of Power Electronics*, 2e], [NPTEL, Module 4: DC-DC Converters].

### 4.2.1 Buck converter - circuit, operation in CCM, voltage gain

The **buck converter** is the basic step-down converter. It is used when the required output voltage is lower than the available input voltage, as in deriving a low-voltage control rail from a higher DC bus or charging a lower-voltage battery from a larger source [Mohan, Undeland, Robbins, *Power Electronics: Converters, Applications, and Design*, 3e], [TI, Buck Converter Basics].

During the ON interval, the source is connected to the inductor and load. Inductor current rises because the source applies a positive voltage across the inductor. During the OFF interval, the main switch opens, but inductor current continues through the diode or synchronous switch and the load. The output capacitor smooths the pulsating energy transfer into a nearly steady output voltage.

**Image prompt for Figure 14.1:** Create a clean textbook-style technical illustration of an ideal buck converter. Show a DC input source $V_{in}$, controlled switch $S$, freewheeling diode $D$, inductor $L$, output capacitor $C$, and resistive load $R$. Beside the circuit, show aligned waveforms versus time for gate command, switch-node voltage, inductor current $i_L$, and output voltage $v_o$. Mark the ON interval, OFF interval, duty cycle $D$, and indicate that $i_L$ never reaches zero in CCM. Use monochrome engineering style with axes, labels, and units.

#### Operation and voltage gain

In CCM, the inductor current remains positive throughout the switching cycle. For the ideal buck converter, the inductor voltage during the ON interval is

$$v_{L,\text{ON}} = V_{in} - V_o \quad \text{(14.1)}$$

During the OFF interval, the inductor freewheels through the diode path, giving

$$v_{L,\text{OFF}} = -V_o \quad \text{(14.2)}$$

In steady-state periodic operation, the average voltage across an inductor over one switching period is zero. Applying volt-second balance,

$$D(V_{in} - V_o) + (1-D)(-V_o) = 0 \quad \text{(14.3)}$$

which reduces to

$$\boxed{V_o = D\,V_{in}} \quad \text{(14.4)}$$

Since $0 < D < 1$, the ideal buck output is always lower than the input.

#### Example

To obtain $12 \text{ V}$ from a $48 \text{ V}$ DC source,

$$D = \frac{V_o}{V_{in}} = \frac{12}{48} = 0.25$$

If the switching frequency is $50 \text{ kHz}$, the switching period is

$$T = \frac{1}{f_s} = \frac{1}{50\,000} = 20 \,\mu\text{s}$$

Hence,

$$T_{ON} = DT = 0.25 \times 20 \,\mu\text{s} = 5 \,\mu\text{s}$$

and

$$T_{OFF} = 20 - 5 = 15 \,\mu\text{s}$$

The reduction in output voltage is achieved by timing the energy transfer, not by continuously dissipating the difference between input and output voltage.

#### Practical note

The inductor current ripple during the ON interval is approximately

$$\Delta i_{L,\text{ON}} = \frac{(V_{in}-V_o)DT}{L} \quad \text{(14.5)}$$

Larger inductance or higher switching frequency reduces ripple. In practice, the ideal gain of Equation (14.4) is modified by switch drop, diode drop, winding resistance, capacitor ESR, and possible departure from CCM at light load. Buck converters are widely used wherever a higher DC source must feed a lower rail, especially in auxiliary and control supplies.

### 4.2.2 Boost converter - circuit, operation in CCM, voltage gain

The **boost converter** is the basic step-up converter. It is used when the available input voltage is lower than the required output voltage, as in raising PV voltage to a higher DC link or generating an internal rail above the battery voltage [NPTEL, Module 4 Lecture 10], [Mohan, Undeland, Robbins, *Power Electronics: Converters, Applications, and Design*, 3e].

Its essential feature is the role of the inductor. During the ON interval, the source stores energy in the inductor. During the OFF interval, the inductor reverses its terminal voltage as required to maintain current, and its voltage adds to the source voltage through the diode path. The output can therefore exceed the input. This does not imply energy creation; for a given power level, output current is correspondingly lower in the ideal case.

**Image prompt for Figure 14.2:** Create a clean textbook-style technical illustration of an ideal boost converter. Show a DC input source $V_{in}$ feeding an inductor $L$, a controlled switch $S$ from the inductor-switch node to ground, a diode from the switch node to the output, an output capacitor $C$, and load $R$. Beside the circuit, show aligned waveforms for gate command, inductor current $i_L$, switch-node voltage, and output voltage $v_o$. Mark ON and OFF intervals and indicate that inductor current stays above zero in CCM. Use monochrome engineering style with clear labels.

#### Operation and voltage gain

When the switch is ON, the diode is reverse biased and the inductor stores energy from the source. The inductor voltage is

$$v_{L,\text{ON}} = V_{in} \quad \text{(14.6)}$$

When the switch turns OFF, the inductor current flows through the diode into the output network, so

$$v_{L,\text{OFF}} = V_{in} - V_o \quad \text{(14.7)}$$

Because $V_o > V_{in}$ in boost operation, Equation (14.7) is negative, and the inductor current falls during the OFF interval.

Applying volt-second balance,

$$D(V_{in}) + (1-D)(V_{in} - V_o) = 0 \quad \text{(14.8)}$$

which gives

$$\boxed{V_o = \frac{V_{in}}{1-D}} \quad \text{(14.9)}$$

As $D$ increases, the ideal output voltage rises.

#### Example

Suppose a PV source operates at $200 \text{ V}$ and a later stage requires an idealized $400 \text{ V}$ DC bus. Using Equation (14.9),

$$400 = \frac{200}{1-D}$$

so

$$1-D = \frac{200}{400} = 0.5$$

and therefore

$$D = 0.5$$

If the PV voltage later falls to $160 \text{ V}$ while the target remains $400 \text{ V}$ ideally, then

$$D = 1 - \frac{160}{400} = 0.6$$

The required duty cycle increases as the source voltage falls.

#### Practical note

Equation (14.9) suggests very large gain as $D \to 1$, but real converters do not sustain unlimited output voltage. Switch resistance, diode drop, winding resistance, parasitics, current stress, and control limits all constrain high-duty-cycle operation. Boost converters are therefore most effective within a practical operating range rather than near the ideal limit.

### 4.2.3 Buck-Boost converter - circuit, operation, voltage gain, polarity inversion

The classical **buck-boost converter** can produce an output magnitude either lower or higher than the input, depending on duty cycle. Its defining drawback is that the output polarity is inverted with respect to the input ground [NPTEL, Module 4 Lecture 10], [Erickson and Maksimovic, *Fundamentals of Power Electronics*, 2e].

This polarity inversion is central rather than incidental. In the classical single-switch form, a positive input referenced to ground produces a negative output with respect to the same reference. The topology is therefore useful when a negative rail is acceptable or required, but not when the load must share the same positive ground reference as the source.

**Image prompt for Figure 14.3:** Create a clean textbook-style technical illustration of the classical inverting buck-boost converter. Show input source $V_{in}$, inductor $L$, controlled switch $S$ to ground, diode to the output network, output capacitor $C$, and load $R$ arranged so that the output voltage is negative relative to the input ground. Include aligned waveforms for gate command, inductor current, switch-node voltage, and output voltage polarity marking. Clearly label that the output polarity is inverted. Use monochrome engineering style with axes, labels, and units.

#### Operation and voltage gain

When the switch is ON, the diode is reverse biased and the source applies voltage across the inductor:

$$v_{L,\text{ON}} = V_{in} \quad \text{(14.10)}$$

When the switch turns OFF, the inductor current flows through the diode into the output network. If the output magnitude is written as $|V_o|$, then

$$v_{L,\text{OFF}} = -|V_o| \quad \text{(14.11)}$$

Applying volt-second balance,

$$D(V_{in}) + (1-D)(-|V_o|) = 0 \quad \text{(14.12)}$$

so

$$|V_o| = \frac{D}{1-D}V_{in}$$

Since the output polarity is inverted,

$$\boxed{\frac{V_o}{V_{in}} = -\frac{D}{1-D}} \quad \text{(14.13)}$$

If $D < 0.5$, then $|V_o| < V_{in}$. If $D > 0.5$, then $|V_o| > V_{in}$.

#### Example

To obtain $-18 \text{ V}$ from a $12 \text{ V}$ source, use Equation (14.13) in magnitude form:

$$18 = \frac{D}{1-D} \times 12$$

Thus,

$$\frac{18}{12} = \frac{D}{1-D} = 1.5$$

which gives

$$D = 1.5(1-D) = 1.5 - 1.5D$$

Hence,

$$2.5D = 1.5$$

and

$$D = 0.6$$

An ideal duty cycle of $60\%$ produces the required magnitude, with negative polarity.

#### Practical note

The most common introductory error in this topology is to focus on gain magnitude and overlook the sign. That omission leads directly to incorrect topology selection. The classical buck-boost is more suitable for negative auxiliary rails, instrumentation supplies, and similar functions than for main positive-output power stages.

### 4.2.4 Cuk converter - circuit, operation, voltage gain, advantages

The **Cuk converter** may be viewed as a refinement of the inverting buck-boost converter. It also provides step-down or step-up operation in magnitude and also inverts output polarity, but it uses two inductors and a coupling capacitor as the main energy-transfer element. Its main practical advantage is smoother current at both input and output [Mohan, Undeland, Robbins, *Power Electronics: Converters, Applications, and Design*, 3e], [TI, LM2611 product page], [TI, PMP30487 reference design].

This feature matters because ripple current affects EMI, source stress, capacitor heating, and load-side filtering requirements.

**Image prompt for Figure 14.4:** Create a clean textbook-style technical illustration of a Cuk converter. Show input source $V_{in}$, input inductor $L_1$, controlled switch $S$, diode $D$, energy-transfer capacitor $C_1$, output inductor $L_2$, output capacitor $C_o$, and load $R$. Include a polarity label showing the output is negative with respect to input ground. Beside the circuit, show smoothed input current and output current waveforms to emphasize that both are relatively continuous. Use monochrome engineering style with labels and units.

#### Operation and voltage gain

In a Cuk converter, one inductor is placed on the input side and another on the output side. Between them is an energy-transfer capacitor $C_1$. During one switching interval, that capacitor is charged; during the other, it transfers energy into the output side. The two inductors make the input and output currents comparatively continuous.

For introductory analysis, the most important point is that $C_1$ is not merely a small ripple filter. It is the principal energy-transfer element between input and output stages.

For the ideal Cuk converter in CCM, the voltage gain is

$$\boxed{\frac{V_o}{V_{in}} = -\frac{D}{1-D}} \quad \text{(14.14)}$$

The ideal gain therefore matches that of the classical inverting buck-boost converter, even though the current waveforms and practical behavior differ significantly.

#### Example

Suppose the converter must produce $-12 \text{ V}$ from a $24 \text{ V}$ source. Using Equation (14.14) in magnitude form,

$$12 = \frac{D}{1-D}\times 24$$

so

$$\frac{12}{24} = \frac{D}{1-D} = 0.5$$

which gives

$$D = 0.5(1-D) = 0.5 - 0.5D$$

Hence,

$$1.5D = 0.5$$

and therefore

$$D \approx 0.333$$

A duty cycle of about $33.3\%$ produces an ideal output of $-12 \text{ V}$ from $24 \text{ V}$.

#### Practical note

The Cuk converter is not simply a buck-boost converter with unnecessary extra parts. The additional reactive elements materially change the current waveforms and improve current smoothness. The tradeoff is increased component count, substantial ripple current in the energy-transfer capacitor, and continued polarity inversion in the classical form.

### 4.2.5 SEPIC converter - circuit, operation, applications in PV systems

The **SEPIC converter** or **Single-Ended Primary Inductor Converter** can step the output voltage up or down while maintaining the same output polarity as the input [Analog Devices, SEPIC glossary]. It is especially useful when the input may move above and below the desired regulated output.

Such conditions occur in variable-input systems. Battery voltage changes during charge and discharge, PV voltage changes with irradiance and temperature, and industrial or automotive DC rails may sag or surge. When the required output must remain at a fixed positive value while the input crosses above and below that value, SEPIC is a natural candidate [Analog Devices, High Efficiency Synchronous SEPIC for Automotive and Industrial Installations], [TI, TIDA-00781 reference design].

**Image prompt for Figure 14.5:** Create a clean textbook-style technical illustration of a SEPIC converter. Show input source $V_{in}$, input inductor $L_1$, coupling capacitor $C_1$, second inductor $L_2$ or coupled-inductor equivalent, controlled switch $S$, diode $D$, output capacitor $C_o$, and load $R$. Include a note that the output polarity is the same as the input polarity. Beside the circuit, show two example operating cases: one with $V_{in} < V_o$ and one with $V_{in} > V_o$, both producing a regulated positive output. Use monochrome engineering style with clear labels.

#### Operation and voltage gain

The SEPIC converter uses two inductors, a series coupling capacitor, a switch, a diode, and an output capacitor. As in the Cuk converter, the coupling capacitor participates actively in energy transfer, but the output remains non-inverted.

During the ON interval, the switch conducts, the diode is reverse biased, and energy is stored in the inductive elements. During the OFF interval, the switch opens, the diode conducts, and energy is delivered to the output capacitor and load. In the ideal CCM model, the average voltage across the coupling capacitor is approximately equal to the input voltage. Using that result with volt-second balance gives

$$\boxed{\frac{V_o}{V_{in}} = \frac{D}{1-D}} \quad \text{(14.15)}$$

The gain magnitude matches the classical buck-boost converter, but the polarity remains positive.

If $D < 0.5$, then $V_o < V_{in}$. If $D = 0.5$, then $V_o = V_{in}$ ideally. If $D > 0.5$, then $V_o > V_{in}$.

#### Example

Suppose a PV-powered controller must maintain $24 \text{ V}$ output from a source that may vary between $18 \text{ V}$ and $36 \text{ V}$.

When $V_{in} = 18 \text{ V}$,

$$24 = \frac{18D}{1-D}$$

$$24(1-D) = 18D$$

$$24 = 42D$$

$$D \approx 0.571$$

When $V_{in} = 36 \text{ V}$,

$$24 = \frac{36D}{1-D}$$

$$24(1-D) = 36D$$

$$24 = 60D$$

$$D = 0.4$$

The same converter can therefore regulate the same positive output while the input moves both below and above the target value.

#### Practical note

SEPIC is flexible, but that flexibility has a cost. It requires more components than a buck or boost converter, and the coupling capacitor and semiconductors may experience appreciable stress. If the input is almost always above the output, a buck converter is often simpler and more efficient. If the input is almost always below the output, a boost converter is often preferable. SEPIC is most attractive when both operating regions are genuinely required.

## Worked interpretation exercise

### Reading a real buck-converter product page

As a practical example, consider the TI **TPS566235**, described by TI as a 4.5 V to 18 V, 6 A synchronous buck converter [TI, TPS566235 product page].

The listed product details include:

- topology: Buck
- input voltage range: $4.5 \text{ V}$ to $18 \text{ V}$
- output voltage range: $0.6 \text{ V}$ to $7 \text{ V}$
- output current: up to $6 \text{ A}$
- switching frequency: $600 \text{ kHz}$
- maximum duty cycle: $88\%$
- integrated power FETs and protection features such as overcurrent, overtemperature, and UVLO [TI, TPS566235 product page]

These entries can be read directly in terms of converter behavior. The topology identifies the device as a step-down converter. The input and output ranges confirm that intended use. The 6 A rating shows that the device serves substantial low-voltage rails rather than only very small loads. The term **synchronous** indicates that the freewheeling diode of the basic textbook circuit is replaced by an actively controlled MOSFET to reduce loss. The listed switching frequency suggests smaller magnetic and capacitive components than a lower-frequency design, though switching loss becomes more important. The protection features show the distinction between topology analysis and practical product design: the topology explains the conversion mechanism, while the product integrates the circuitry needed for safe and reliable operation.

When reading a converter datasheet or product page, the first questions are therefore straightforward: What topology is it? What input range does it accept? What output range and current can it provide? Those initial entries often determine whether the device is relevant to the design problem.

## How this matters in renewable-energy systems

Non-isolated DC-DC converters appear throughout renewable-energy and electrified systems, though not always in the same role.

In solar PV, the **boost converter** is a natural choice when a lower and variable PV voltage must feed a higher DC link. The **SEPIC converter** becomes attractive when an auxiliary source may move above and below the required output. In battery systems, the **buck converter** is common when a higher DC bus must charge a lower-voltage battery or supply lower-voltage electronics. The **buck-boost** and **SEPIC** families become important when battery voltage varies widely while the output must remain regulated.

In wind-energy, EV, and power-conversion equipment, these converters often serve auxiliary rather than main power paths. Control boards, sensors, communication modules, gate-drive support rails, and measurement circuits all require regulated DC supplies. Even when the major traction or charger stage is isolated, many internal rails are still generated by non-isolated buck, boost, Cuk, or SEPIC stages.

The recurring design issue is variability. Source voltage changes with operating conditions, while the required load voltage is often much less variable. Non-isolated DC-DC converters provide the means to reconcile those two facts efficiently.

## Chapter summary

- A **buck converter** is a step-down converter with ideal CCM gain $\dfrac{V_o}{V_{in}} = D$.
- A **boost converter** is a step-up converter with ideal CCM gain $\dfrac{V_o}{V_{in}} = \dfrac{1}{1-D}$.
- A classical **buck-boost converter** can step down or step up in magnitude, but it inverts output polarity. Its ideal CCM gain is $\dfrac{V_o}{V_{in}} = -\dfrac{D}{1-D}$.
- A **Cuk converter** has the same ideal CCM gain as the classical buck-boost converter, but uses two inductors and an energy-transfer capacitor to obtain smoother input and output currents.
- A **SEPIC converter** can step down or step up while preserving output polarity. Its ideal CCM gain is $\dfrac{V_o}{V_{in}} = \dfrac{D}{1-D}$.
- **CCM** means the inductor current does not fall to zero during a switching cycle.
- **Volt-second balance** states that the average voltage across an inductor over one complete switching period is zero in steady-state periodic operation.
- Converter choice depends not only on voltage gain, but also on polarity, ripple behavior, component count, current stress, and application range.

## Further reading

1. Robert W. Erickson and Dragan Maksimovic, *Fundamentals of Power Electronics*, 2nd ed.  
   A rigorous but still readable reference for volt-second balance, CCM analysis, and the deeper behavior of basic converters.

2. Ned Mohan, Tore M. Undeland, and William P. Robbins, *Power Electronics: Converters, Applications, and Design*, 3rd ed.  
   A classic power-electronics text that explains the operation and applications of the main DC-DC topologies in a systematic way.

3. NPTEL, "Module 4: DC-DC Converters" and "Lecture 10: Boost and Buck-Boost Converters," archive.nptel.ac.in.  
   Useful introductory material with topology-level explanations and waveform-focused discussion suitable for self-study.

4. Texas Instruments, "TPS566235 4.5-V to 18-V Input, 6-A Synchronous Step-Down Converter" product page and datasheet.  
   A good real-world example of how an ideal buck concept appears in a modern commercial regulator.

5. Analog Devices, "High Efficiency Synchronous SEPIC for Automotive and Industrial Installations," and TI, "TIDA-00781 12W SEPIC Power Supply Reference Design."  
   Useful references for variable-input applications in which SEPIC topology is relevant.
