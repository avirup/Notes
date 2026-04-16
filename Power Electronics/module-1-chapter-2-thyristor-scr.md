# Chapter 2: Thyristor (SCR)

## Chapter opening

A **thyristor**, or **silicon controlled rectifier (SCR)**, is a four-layer power semiconductor that can be triggered into conduction by a gate signal but cannot ordinarily be turned OFF by the gate. Once the device has latched, the current through it must fall below a critical value before blocking action is restored. This behavior made the SCR one of the foundational devices of power electronics.

Commercially introduced in 1957, the SCR moved power control away from electromechanical and gas-discharge devices toward reliable solid-state switching [IEEE Milestone: Silicon Controlled Rectifier (SCR/Thyristor), 1957]. Although MOSFETs and IGBTs dominate high-frequency PWM converters, SCRs remain important in controlled rectification, phase control, crowbar protection, inrush-current limiting, soft starters, and other high-power line-frequency applications where rugged current handling and low on-state loss are more important than fast turn-OFF [ST AN4607], [Littelfuse Phase Control].

## Prerequisites check

- forward and reverse bias of a PN junction
- basic transistor action from Chapter 1, especially current gain and switching operation
- RMS and peak values of AC quantities; for a sinusoid, $V_m = \sqrt{2}V_{rms}$
- the fact that an inductor resists sudden change of current and a capacitor resists sudden change of voltage
- the idea that semiconductor devices have electrical ratings and temperature limits

The chapter assumes familiarity with current paths, blocking states, and basic switching stress.

### 2.1.1 History of the Thyristor (SCR)

Before solid-state power control became practical, heaters, battery chargers, motors, and rectifier front ends were controlled by mechanical switches, rheostats, or bulky gas-filled devices. Engineers needed a semiconductor device that could block high voltage, carry high current, and be triggered by a small control signal. The SCR met that need.

IEEE's milestone document notes that General Electric introduced the silicon controlled rectifier in 1957 and that the device marked a turning point in electric-energy control [IEEE Milestone: Silicon Controlled Rectifier (SCR/Thyristor), 1957]. Its significance lay in a particular combination of properties: substantial OFF-state voltage blocking, large current capability, relatively low on-state drop, and electronic triggering by a gate signal. Its main limitation was equally important. A conventional SCR could be turned ON by the gate, but once latched it could not normally be turned OFF by the gate. Converter design therefore had to rely on natural or forced commutation.

The SCR also became the basis of a wider thyristor family. The IEEE milestone note identifies later devices such as the TRIAC and GTO as descendants of the SCR [IEEE Milestone: Silicon Controlled Rectifier (SCR/Thyristor), 1957]. The device remains important in line-frequency power control, static switches, soft starters, crowbar protection, high-power rectifiers, and applications where ruggedness and current handling matter more than very high switching frequency [ST AN4607], [Littelfuse MCR16NG Product Page], [Littelfuse Phase Control].

Table 2.1: Why the SCR became a foundational power device

| Reason | Why it mattered |
|---|---|
| High-voltage blocking capability | Made direct connection to power circuits practical |
| High current capability | Allowed real industrial loads to be controlled |
| Gate triggering | Enabled electronic control without a large mechanical actuator |
| Low on-state drop | Reduced conduction loss compared with many older control methods |
| Rugged construction | Suited industrial and utility environments |

SCRs are no longer the universal choice in power conversion, but they are not merely historical devices. They remain practical wherever line-frequency efficiency, surge tolerance, and latching behavior are useful.

### 2.1.2 Construction, two-transistor analogy, operating principle

An SCR is often described as a power device with memory. A transistor responds continuously to its control input, whereas an SCR responds to a trigger and then remains ON because of internal regenerative action until the external circuit reduces its current sufficiently.

#### Physical structure

An SCR is a **four-layer, three-junction, three-terminal** semiconductor device. Its terminals are:

- **Anode**
- **Cathode**
- **Gate**

The internal layers are arranged in **PNPN** order, forming three junctions labeled $J_1$, $J_2$, and $J_3$ [ST AN4607].

**Image prompt for Figure 2.1:** Create a clean textbook-style technical illustration of an SCR cross-section showing the four semiconductor layers in vertical order as P, N, P, N. Label the top terminal as anode and the bottom terminal as cathode. Show the gate connected near the cathode-side P-layer. Mark the three junctions as $J_1$, $J_2$, and $J_3$. Add two small side insets: one for forward blocking with anode positive, showing $J_1$ and $J_3$ forward biased and $J_2$ reverse biased, and one for reverse blocking with cathode positive, showing the appropriate reverse-biased junctions. Use monochrome engineering style, no decorative elements.

When the anode is positive with respect to the cathode, the outer junctions $J_1$ and $J_3$ are forward biased while the middle junction $J_2$ remains reverse biased. The device is then in **forward blocking**: it is forward biased overall but does not yet conduct strongly. When the cathode is positive with respect to the anode, the device is in **reverse blocking**. Only a small leakage current flows until reverse breakdown is reached, which is outside normal operating conditions [ST AN4607], [ST AN4608].

This ability to remain OFF under forward bias and then remain ON after triggering distinguishes the SCR from both a diode and an ordinary transistor.

#### The two-transistor analogy

The internal PNPN structure can be represented by the **two-transistor analogy**. In this model, the SCR is viewed as two tightly coupled transistor actions:

- a **PNP transistor** near the anode side
- an **NPN transistor** near the cathode side

These are not two separate packaged transistors. They are a conceptual representation of the internal structure [ST AN4607], [Teccor Thyristor Design Guide].

**Image prompt for Figure 2.2:** Create a textbook-style diagram of the SCR two-transistor analogy. Show one PNP transistor on the left and one NPN transistor on the right. Connect the collector of each transistor to the base of the other to illustrate regenerative feedback. Label the anode at the emitter of the PNP transistor, the cathode at the emitter of the NPN transistor, and the gate entering the base of the NPN transistor. Add current arrows and annotate “regenerative feedback” between the two collector-base cross-connections.

Let the PNP section be $T_1$ and the NPN section be $T_2$. Their coupling is the essential feature:

- the emitter of $T_1$ is connected to the anode
- the emitter of $T_2$ is connected to the cathode
- the collector of $T_1$ feeds the base of $T_2$
- the collector of $T_2$ feeds the base of $T_1$
- the gate injects current into the base region of $T_2$

The latching process can then be described in a short sequence:

1. With the anode positive, the SCR is forward biased but still OFF. The internal transistor actions are weak and only leakage currents exist.
2. A gate pulse supplies current to the NPN section $T_2$, which begins to conduct.
3. The collector current of $T_2$ becomes base drive for the PNP section $T_1$, so $T_1$ also begins to conduct.
4. The collector current of $T_1$ feeds additional base drive back into $T_2$. Positive feedback therefore builds rapidly between the two internal transistor actions.
5. Once the feedback is strong enough, conduction becomes self-sustaining. The SCR **latches** and remains ON until the anode current falls low enough for the regenerative loop to collapse.

A simplified current relation from the two-transistor model is [ST AN4607]

$$\boxed{I_A = \frac{I_{CBO1} + I_{CBO2} + \alpha_2 I_G}{1 - (\alpha_1 + \alpha_2)}} \quad \text{(2.1)}$$

where

- $I_A$ is the anode current
- $I_G$ is the gate current
- $\alpha_1$ is the common-base current gain of the PNP section
- $\alpha_2$ is the common-base current gain of the NPN section
- $I_{CBO1}$ and $I_{CBO2}$ are leakage-current terms of the two sections

The denominator shows the essential behavior. As $\alpha_1 + \alpha_2$ approaches 1, the denominator becomes small and the anode current rises sharply. The latching condition is therefore expressed conceptually as

$$\boxed{\alpha_1 + \alpha_2 \rightarrow 1} \quad \text{(2.2)}$$

Equation (2.2) is not used as a direct design formula. It explains why the SCR turns ON through regenerative feedback rather than by gradual, continuously controllable conduction.

#### A simple numerical intuition

For a 230 V, 50 Hz AC supply,

$$\boxed{V_m = \sqrt{2}V_{rms}} \quad \text{(2.3)}$$

so

$$V_m = \sqrt{2}\times 230 \approx 325 \text{ V}.$$

An SCR connected to this supply may remain in forward blocking during part of a positive half-cycle even while the instantaneous anode voltage is rising toward 325 V. Conduction begins only when a gate pulse arrives or forward breakover is reached. This controllable delay is the basis of phase control.

#### What makes the SCR attractive

The SCR combines low conduction loss in the ON state with high voltage blocking in the OFF state. That combination makes thyristors effective in high-current, line-frequency applications [ST AN4607].

The same structure also creates the device's main limitation. Charge is stored deeply in the silicon, and a conventional SCR cannot ordinarily be gate-turned-OFF. It is therefore most useful where natural commutation is available or where a separate commutation circuit can be justified.

### 2.1.3 Static V-I characteristics: latching current, holding current, break-over voltage, forward and reverse blocking

The static V-I characteristic identifies the main operating regions of an SCR: reverse blocking, reverse breakdown, forward blocking, and forward conduction.

**Image prompt for Figure 2.3:** Create a clean engineering plot of the static V-I characteristic of an SCR. Horizontal axis: anode-cathode voltage $V_{AK}$ in volts. Vertical axis: anode current $I_A$ in amperes. Show reverse blocking in the third quadrant, forward blocking in the first quadrant, forward breakover voltage $V_{BO}$, the sudden transition to ON state, and the low-voltage high-current on-state branch. Mark latching current $I_L$ on the rising current path just after triggering and holding current $I_H$ on the falling current path, with $I_L > I_H$. Label reverse breakdown, forward blocking, on-state, and leakage regions clearly.

#### The main regions

Table 2.2: Main regions of the SCR static characteristic

| Region | External condition | Device behavior | Practical meaning |
|---|---|---|---|
| Reverse blocking | Cathode positive with respect to anode | Very small reverse leakage current | SCR is OFF in reverse direction |
| Reverse breakdown | Reverse voltage too high | Large reverse current | Abnormal and unsafe operating region |
| Forward blocking | Anode positive but not yet triggered | Only a small forward leakage current | SCR is forward biased but still OFF |
| Forward conduction | Device triggered or broken over | Large anode current with small on-state voltage | SCR is ON |

In **forward blocking**, the SCR is ready to conduct but has not yet been triggered. In **forward conduction**, it behaves approximately like a closed switch with a small forward voltage drop.

#### Forward breakover voltage

If the forward anode-cathode voltage is increased sufficiently without a gate pulse, the SCR can enter conduction at the **forward breakover voltage** $V_{BO}$ [ST AN4607]. This is a real turn-ON mechanism, but it is not the normal design method. Breakover triggering gives poor timing control, increases stress, and depends strongly on device condition and temperature. In practical circuits, the SCR is normally triggered by the gate at a lower and controlled voltage.

#### Latching current and holding current

Two current levels are particularly important:

- **Latching current**, $I_L$
- **Holding current**, $I_H$

The **latching current** is the minimum anode current that must be reached immediately after turn-ON so that the SCR remains ON when the gate signal is removed [ST AN303], [ST TYN612 Datasheet]. The **holding current** is the minimum anode current below which the SCR returns to the OFF state after conduction is already established [ST AN302], [ST TYN612 Datasheet].

In normal devices,

$$\boxed{I_L > I_H} \quad \text{(2.4)}$$

The difference arises because conduction is not yet fully established at the instant of triggering. The device needs a higher current to latch firmly than it needs to remain in conduction afterward.

Datasheet values make the distinction concrete. The ST TYN612 family lists maximum holding-current values such as 15 mA, 30 mA, or 40 mA, and latching-current values such as 30 mA, 60 mA, or 80 mA depending on the sensitivity class [ST TYN612 Datasheet]. A lightly loaded circuit may therefore trigger an SCR and still fail to keep it ON reliably.

#### A 50 Hz intuition

At 50 Hz, one full AC cycle lasts

$$T = \frac{1}{f} = \frac{1}{50} = 20 \text{ ms}.$$

One half-cycle therefore lasts $10 \text{ ms}$. In AC phase control, the load current usually decreases near the end of each half-cycle. If it falls below $I_H$, the SCR turns OFF and must be triggered again in the next positive half-cycle. This repeated turn-ON and natural turn-OFF makes phase-controlled rectifiers and AC voltage controllers possible.

#### Reverse and forward leakage

In the blocking states, the SCR still carries a small **leakage current**. The TYN612 datasheet specifies off-state leakage in the microampere range at 25 °C, with much larger values at higher junction temperature [ST TYN612 Datasheet]. The OFF state therefore means strong blocking, not zero current.

#### On-state branch

When the SCR is ON, the anode-cathode voltage does not fall to zero. Practical thyristors show an on-state drop on the order of 1 V to 2 V at useful current densities [ST AN4607]. The TYN612 datasheet gives a maximum on-state voltage $V_{TM}$ of about 1.6 V at a specified pulsed-current test point [ST TYN612 Datasheet]. This relatively low drop is one reason SCRs remain efficient in high-current line-frequency systems.

### 2.1.4 Turn-ON methods: gate triggering, $dv/dt$, thermal, light, forward-voltage

An SCR may turn ON by several mechanisms, but only one of them is the normal control method. In design practice, gate triggering is intentional; the others are either special cases or effects to be avoided.

#### 1. Gate triggering

**Gate triggering** is the preferred turn-ON method in most controlled circuits [ST AN4607], [Teccor Thyristor Design Guide]. A positive gate current with respect to the cathode injects carriers into the device and initiates regenerative action. In design, the gate drive is chosen with margin over the minimum trigger requirement so that the SCR turns ON reliably across temperature, manufacturing spread, and noise.

If a gate source of voltage $V_s$ drives the gate through a resistor $R_G$, a first estimate of gate current is

$$\boxed{I_G \approx \frac{V_s - V_{GK}}{R_G}} \quad \text{(2.5)}$$

where $V_{GK}$ is the gate-cathode drop during triggering.

For example, with a 12 V gate pulse, a desired gate current of 20 mA, and $V_{GK} \approx 1.3 \text{ V}$,

$$R_G \approx \frac{12 - 1.3}{0.02} = 535 \ \Omega.$$

A practical design would then examine nearby standard values such as $510 \ \Omega$ or $560 \ \Omega$ and verify gate-current, pulse-width, and gate-power limits against the actual datasheet. The gate pulse need only last long enough for anode current to rise above the latching-current requirement.

#### 2. Forward-voltage triggering

If the anode-cathode voltage rises to the **breakover voltage**, the SCR can turn ON without gate drive [ST AN4607]. This **forward-voltage** or **breakover** triggering is real, but it is not preferred in controlled circuits because it gives poor timing accuracy and adds electrical stress.

#### 3. $dv/dt$ triggering

The SCR junctions have capacitance, so a rapid change in forward voltage can create a displacement current through the internal capacitances. The capacitor relation is

$$\boxed{i = C_j \frac{dv}{dt}} \quad \text{(2.6)}$$

where $C_j$ is the effective junction capacitance.

If $\frac{dv}{dt}$ is large enough, the resulting displacement current can trigger the SCR unintentionally [ST AN4608], [Teccor Thyristor Design Guide]. This is one of the main reasons for using an RC snubber across the device.

#### 4. Thermal triggering

As junction temperature rises, leakage current increases. In a four-layer structure this increase can strengthen the internal regenerative mechanism and reduce blocking stability [ST AN4607], [ST AN4608]. Thermal triggering is therefore a stress or failure mechanism, not a normal operating method.

#### 5. Light triggering

Some thyristors are designed so that light generates the carriers needed to start conduction. These **light-activated SCRs**, or **LASCRs**, are useful where high-voltage isolation is required between control and power circuits [Teccor Thyristor Design Guide]. The underlying turn-ON mechanism is still regenerative.

#### Which methods are good engineering practice?

Table 2.3: SCR turn-ON methods in practice

| Turn-ON method | Physical basis | Used intentionally? | Typical design view |
|---|---|---|---|
| Gate triggering | Carrier injection through gate | Yes | Normal and preferred |
| Forward-voltage breakover | Exceeding $V_{BO}$ | Rarely | Avoid as routine control method |
| $dv/dt$ triggering | Junction-capacitance displacement current | No | Prevent with protection |
| Thermal triggering | Leakage increase and loss of blocking stability | No | Prevent by thermal design |
| Light triggering | Optical carrier generation | Yes, in special devices | Useful where isolation is important |

#### A practical timing picture

In AC phase control, turn-ON is usually described by the **firing angle** $\alpha$, measured from the start of the positive half-cycle to the instant of gate triggering.

At 50 Hz:

- half-cycle duration = $10 \text{ ms}$
- $\alpha = 90^\circ$ corresponds to a delay of $5 \text{ ms}$
- $\alpha = 150^\circ$ corresponds to a delay of about $8.33 \text{ ms}$

The SCR therefore allows the start of conduction to be placed at a controlled point within each half-cycle. The mathematical consequences of firing angle are taken up in Chapter 3.

### 2.1.5 Turn-OFF and commutation methods: natural (line) commutation and forced commutation

A conventional SCR turns OFF only when the anode current falls below the holding current and the device is given enough time to recover its blocking capability. The recovery interval is described by the **turn-off time** $t_q$ [ST AN4608], [Teccor Thyristor Design Guide], so a basic requirement is

$$\boxed{t_{\text{available off}} > t_q} \quad \text{(2.7)}$$

Turn-OFF is therefore not only a matter of reducing current. Stored charge must also be removed before the device can block forward voltage again.

#### Natural or line commutation

In AC circuits, turn-OFF often occurs naturally. As the line current approaches zero near the end of a half-cycle, the anode current falls below $I_H$. When the supply reverses, the SCR becomes reverse biased and regains its blocking state. This is called **natural commutation**, **line commutation**, or, in some classifications, **Class F** [ST AN4607].

For 50 Hz mains, each half-cycle lasts 10 ms, so the circuit repeatedly offers a turn-OFF interval that is usually much longer than the recovery time of the device. This is why SCRs are particularly well suited to controlled rectifiers and other line-commutated converters.

#### Forced commutation

In DC circuits, there is no natural line-current zero crossing. A conducting SCR must therefore be turned OFF by circuit action that forces its current below the holding-current level and usually applies reverse bias for a sufficient interval. This is called **forced commutation**.

The implementation varies, but the principle is the same: an inductor, capacitor, auxiliary switch, or resonant network is used to create a current or voltage condition that drives the conducting SCR current to zero or reverse long enough for recovery.

#### Common Class A to E naming

Many power-electronics texts classify forced-commutation methods as Classes A to E. The names and definitions vary somewhat across books, so Table 2.4 should be read as a concept-level overview rather than a universal naming standard.

Table 2.4: Concept-level view of forced commutation classes

| Class | Concept | Main idea |
|---|---|---|
| Class A | Load or self commutation | The load itself forms an underdamped RLC path that naturally drives current to zero |
| Class B | Resonant-pulse commutation | An LC branch generates a resonant current pulse to oppose device current |
| Class C | Complementary commutation | One SCR helps turn OFF another SCR |
| Class D | Auxiliary commutation | An auxiliary SCR and capacitor apply reverse voltage across the main SCR |
| Class E | External-pulse commutation | An external pulse source forces reverse current or reverse voltage |

The essential distinction is simple. In **natural commutation**, the AC source provides the turn-OFF condition. In **forced commutation**, the circuit designer must create that condition.

This distinction explains why SCRs fit line-frequency rectifiers more naturally than high-frequency DC choppers. In the former, the line itself supplies current zero. In the latter, the converter must provide it.

### 2.1.6 Gate-triggering circuits: R, R-C and UJT-based triggering (overview)

Once gate triggering has been identified as the preferred turn-ON method, the practical question is how to generate the gate pulse. Classical power-electronics literature presents several traditional triggering circuits, especially for line-frequency phase control [Teccor Thyristor Design Guide]. Only an overview is needed here.

#### R triggering

In **resistor triggering**, gate current is supplied through a resistor from a source or from the AC line through a suitable network. Changing the resistor changes the available gate current and therefore the triggering condition. The method is simple and inexpensive, but it gives poor control of firing angle, offers little isolation, and does not produce a particularly sharp or repeatable gate pulse. It is mainly useful in simple low-power circuits and instructional examples.

#### R-C triggering

In **R-C triggering**, a capacitor charges through a resistor during each AC half-cycle. When the capacitor voltage reaches the effective trigger threshold, gate current flows and the SCR turns ON. Changing the resistance changes the capacitor charging time and therefore the firing angle $\alpha$.

At 50 Hz, a positive half-cycle lasts 10 ms. If the RC network reaches trigger level after about 5 ms, the firing angle is roughly $90^\circ$; if it reaches trigger level after about 8.33 ms, the firing angle is about $150^\circ$. This method appears in many classical phase-control circuits for dimmers, heater controls, and small fan regulators.

#### UJT-based triggering

A more refined classical trigger uses a **UJT**, or **unijunction transistor**, as a relaxation-oscillator pulse source [Teccor Thyristor Design Guide]. A capacitor charges gradually through a resistor. When its voltage reaches the UJT firing condition, the UJT switches and the capacitor discharges rapidly through the pulse path, producing a sharp trigger pulse for the SCR.

The value of the method is its pulse quality. A UJT trigger produces a clearer and more repeatable gate pulse than a slowly rising waveform, and it can be combined with pulse transformers where isolation is required.

#### High-level comparison

Table 2.5: Classical SCR triggering circuits

| Trigger circuit | Main idea | Advantage | Limitation |
|---|---|---|---|
| R triggering | Gate current through a resistor | Very simple | Poor timing control, little isolation |
| R-C triggering | RC charging delay sets firing angle | Useful for AC phase control | Pulse quality and repeatability are limited |
| UJT-based triggering | Relaxation oscillator generates sharp pulses | Better timing and cleaner pulse generation | More components and extra circuit complexity |

#### Isolation and modern practice

Traditional texts often show these trigger circuits connected directly to the line. Historically that is important, but modern practice increasingly favors isolated gate-drive arrangements using pulse transformers, optocouplers, or dedicated driver stages when power level, safety requirements, or control sophistication increase. The classical circuits remain useful because they reveal the origin of firing-angle control and the logic of pulse generation.

Gate drive must still stay within datasheet limits. Trigger pulses should exceed the minimum requirements with suitable margin, but gate current, gate power, and pulse duration must remain within the specified ratings [ST TYN612 Datasheet], [ST AN4608].

### 2.1.7 SCR ratings and specifications; $di/dt$ and $dv/dt$ protection

An SCR datasheet does not describe only one voltage rating and one current rating. A workable design must satisfy a set of limits covering blocking, conduction, triggering, surge survival, switching stress, and temperature.

#### The main datasheet parameters

Table 2.6: Key SCR ratings and what they mean

| Symbol | Meaning | Why it matters |
|---|---|---|
| $V_{DRM}$ | Repetitive peak off-state voltage | Forward blocking limit under repetitive conditions |
| $V_{RRM}$ | Repetitive peak reverse voltage | Reverse blocking limit |
| $I_T(RMS)$ | On-state RMS current | Continuous current capability for AC conduction |
| $I_T(AV)$ | Average on-state current | Useful in rectifier service |
| $I_{TSM}$ | Non-repetitive surge peak on-state current | Surge withstand, especially for faults and inrush |
| $I^2 t$ | Fusing or surge-energy measure | Useful for coordination with protective fuses |
| $I_{GT}$, $V_{GT}$ | Gate trigger current and voltage | Gate-drive design |
| $I_L$, $I_H$ | Latching current and holding current | Reliable turn-ON and turn-OFF behavior |
| $V_{TM}$ | On-state voltage drop | Conduction loss |
| $(di/dt)_{crit}$ | Critical rate of rise of on-state current | Prevents local hot-spot damage during turn-ON |
| $(dv/dt)_{crit}$ | Critical rate of rise of off-state voltage | Prevents unwanted triggering |
| $R_{\theta JC}$ | Junction-to-case thermal resistance | Thermal design |

The TYN612 datasheet provides a representative example set: $I_T(RMS)=12 \text{ A}$, $V_{DRM}/V_{RRM}$ variants of 600 V, 800 V, and 1000 V, gate-trigger options as low as 5 mA or 15 mA depending on version, critical $di/dt$ around $50 \text{ A}/\mu\text{s}$ under stated conditions, critical $dv/dt$ values such as 40 V/$\mu$s or 200 V/$\mu$s depending on sensitivity class, and junction-to-case thermal resistance about $1.3^\circ\text{C/W}$ [ST TYN612 Datasheet].

#### Choosing the voltage class

For a 230 V, 50 Hz single-phase supply,

$$V_m = \sqrt{2}\times 230 \approx 325 \text{ V}.$$

A 600 V SCR belongs to the correct general class for such a line when suitable margin and transient protection are provided.

For a 415 V three-phase system, the line-to-line peak value is

$$V_{LL,peak} = \sqrt{2}\times 415 \approx 587 \text{ V}. \quad \text{(2.8)}$$

This immediately shows why a 600 V device is often too close for comfort in three-phase line-to-line blocking situations once switching spikes and mains disturbances are considered. In such cases, 800 V or 1000 V classes are much more realistic.

#### Why $di/dt$ is dangerous

When an SCR first turns ON, conduction does not spread across the full silicon area instantaneously. The process begins near the gate region and then expands. If anode current rises too quickly, a small part of the device can carry excessive current before the entire junction area is conducting, leading to local overheating and possible failure [ST AN4608], [Teccor Thyristor Design Guide].

The basic inductor relation is

$$\boxed{\frac{di}{dt} = \frac{V}{L}} \quad \text{(2.9)}$$

so a series inductance can limit current rise. If the maximum allowable $di/dt$ is $50 \text{ A}/\mu\text{s}$ and the worst-case applied voltage at turn-ON is about $325 \text{ V}$, the minimum inductance required is approximately

$$L \ge \frac{V}{di/dt} = \frac{325}{50\times 10^6} = 6.5 \ \mu\text{H}.$$

Even a small inductance can therefore reduce turn-ON stress significantly.

#### Why $dv/dt$ is dangerous

In the OFF state, a rapidly rising voltage can create displacement current through the internal junction capacitances, as described by Equation (2.6). If that current becomes large enough, the SCR may trigger unintentionally [ST AN4608], [Littelfuse MCR16NG Product Page].

The most common protection is an **RC snubber** across the SCR. The capacitor slows the voltage rise across the device, and the resistor limits snubber current and damps oscillation. If a capacitor initially charged to voltage $V$ discharges through the snubber resistor at turn-ON, the initial current is approximately

$$\boxed{i_C(0^+) = \frac{V}{R}} \quad \text{(2.10)}$$

The resistor is therefore essential. Without it, the snubber capacitor itself could introduce a large current pulse at turn-ON.

#### On-state loss and thermal design

Even though the SCR has a relatively low on-state drop, the drop is not zero. The TYN612 datasheet gives an on-state model of the form [ST TYN612 Datasheet]

$$\boxed{V_T \approx V_{T0} + I_T r_T} \quad \text{(2.11)}$$

where $V_{T0}$ is a threshold-type on-state voltage parameter and $r_T$ is a dynamic resistance parameter.

The on-state power loss can then be estimated as

$$\boxed{P_{on} \approx V_T I_T} \quad \text{(2.12)}$$

Using approximate values $V_{T0}=0.85 \text{ V}$, $r_T=30 \text{ m}\Omega$, and $I_T = 8 \text{ A}$,

$$V_T \approx 0.85 + 8\times 0.03 = 1.09 \text{ V}$$

and therefore

$$P_{on} \approx 1.09 \times 8 = 8.72 \text{ W}.$$

With junction-to-case thermal resistance $R_{\theta JC}\approx 1.3^\circ\text{C/W}$, the junction temperature can be estimated by

$$\boxed{T_J \approx T_C + P_D R_{\theta JC}} \quad \text{(2.13)}$$

so the simplified rise above case temperature is

$$8.72\times 1.3 \approx 11.3^\circ\text{C}.$$

If the case temperature is already $85^\circ\text{C}$, the junction temperature is then about $96.3^\circ\text{C}$ by this first estimate. Real design must also consider waveform shape, conduction angle, heat sink performance, thermal cycling, and ambient conditions, but the example shows that thermal design cannot be separated from electrical design.

#### Surge and protection interpretation

SCR datasheets also specify **non-repetitive surge current** $I_{TSM}$ and often an **$I^2 t$** value. These ratings matter in faults, capacitor-charging surges, and fuse coordination. In a crowbar circuit, for example, the SCR may be required to conduct a very large current briefly while upstream protection clears the fault. In such cases, surge-current and $I^2 t$ capability may matter more than the normal RMS current rating.

Two rating errors are common in practice. One is to select the device from RMS mains voltage rather than peak voltage plus transient margin. The other is to check only average current while ignoring RMS current, surge capability, conduction angle, thermal resistance, and dynamic limits such as $di/dt$ and $dv/dt$. Gate sensitivity must likewise be interpreted alongside noise immunity and trigger robustness.

#### Worked datasheet interpretation: TYN612

The [ST TYN612 datasheet](https://www.st.com/resource/en/datasheet/tyn612.pdf) is a useful compact example because it presents the essential SCR ratings without excessive detail. Read as a design document, it immediately shows the intended role of the device: line-frequency control and protection rather than high-frequency PWM switching.

The voltage classes, gate-trigger variants, latching and holding currents, dynamic limits, and thermal data collectively describe how the device must be used. The point of the exercise is not to memorize a table of numbers, but to convert those numbers into circuit choices.

Table 2.7: Interpreting the TYN612 datasheet

| Datasheet item | What it says | What it means in design |
|---|---|---|
| 600 V, 800 V, 1000 V versions | Several blocking classes in one family | Choose based on actual line peak plus transient margin |
| $I_T(RMS)=12 \text{ A}$ | Medium-current SCR family | Suitable for many control and protection roles, not arbitrarily for any current |
| $I_{GT}=5 \text{ mA}$ or $15 \text{ mA}$ versions | Different trigger sensitivities | Drive-circuit design and noise margin depend on variant |
| $I_H$ and $I_L$ given explicitly | Conduction persistence is not automatic at low current | Load current must support both turn-ON and continued conduction |
| Critical $di/dt$ and $dv/dt$ ratings | Dynamic stress limits matter | Layout and protection network are part of SCR design |
| $R_{\theta JC}$ provided | Thermal path is quantified | Heat sinking and junction-temperature checks are required |

## How this matters in renewable-energy systems

SCRs are not the main switching devices in modern high-frequency solar PV inverters, battery DC-DC converters, or EV traction inverters. Their continuing relevance in renewable-energy systems lies elsewhere.

They remain valuable in protection and line-frequency auxiliary functions. A crowbar SCR can protect a DC bus or battery-connected load by deliberately shorting the output during an overvoltage fault until a fuse or breaker clears the condition. Inrush-current limiting, soft-start functions, static bypass paths, and some controlled-rectifier interfaces likewise benefit from the SCR's rugged current handling and low line-frequency conduction loss [ST AN4607], [Littelfuse Phase Control].

The device also remains part of the wider power-conversion ecosystem, especially in large industrial power-conditioning systems and high-power line-commutated equipment. More broadly, the SCR trains the designer to ask the right questions about turn-ON, turn-OFF, transient stress, and datasheet interpretation. Those questions remain central even when later chapters move to MOSFETs and IGBTs.

## Chapter summary

- A **thyristor** or **SCR** is a four-layer PNPN power semiconductor with anode, cathode, and gate terminals.
- A conventional SCR can be triggered ON by the gate, but it normally turns OFF only when anode current falls below the holding current and the device has time to recover blocking capability.
- The **two-transistor analogy** explains SCR latching as regenerative feedback between coupled PNP and NPN transistor actions.
- In the static V-I characteristic, the main regions are reverse blocking, reverse breakdown, forward blocking, and forward conduction.
- The **latching current** $I_L$ is the current needed just after triggering to sustain conduction without the gate; the **holding current** $I_H$ is the current below which an already conducting SCR turns OFF. Normally, $I_L > I_H$.
- Practical turn-ON mechanisms include gate triggering, forward-voltage breakover, $dv/dt$ triggering, thermal triggering, and light triggering, but gate triggering is the normal control method.
- In AC circuits, SCRs often turn OFF by **natural or line commutation**. In DC circuits, **forced commutation** is required.
- Classical line-frequency trigger circuits include R triggering, R-C triggering, and UJT-based triggering.
- Important ratings include blocking voltage, RMS and average current, surge current, $I^2 t$, gate-trigger requirements, latching and holding current, on-state voltage, critical $di/dt$, critical $dv/dt$, and thermal resistance.
- Safe SCR design requires voltage margin, current and thermal checks, attention to $di/dt$ and $dv/dt$, and appropriate protective elements such as series inductance, snubbers, and coordinated fault protection.

## Further reading

- [IEEE Milestone brochure: Silicon Controlled Rectifier (SCR/Thyristor), 1957](https://ethw.org/w/images/e/e2/2017-15_SCR_Thyristor_brochure.pdf) - A concise historical source explaining why the SCR was a milestone in electric-power control.
- [ST AN4607: Basics on the thyristor (SCR) structure and its application](https://www.st.com/resource/en/application_note/dm00071938-basics-on-the-thyristor-scr-structure-and-its-application-stmicroelectronics.pdf) - A strong manufacturer introduction to SCR structure, operation, and application context.
- [ST TYN612 Datasheet](https://www.st.com/resource/en/datasheet/tyn612.pdf) - A compact real SCR datasheet that is excellent for learning ratings, trigger parameters, $I_L$, $I_H$, $di/dt$, $dv/dt$, and thermal data.
- [ST AN4608: How to select the right thyristor](https://www.st.com/resource/en/application_note/dm00071959-how-to-select-the-right-thyristor-for-crowbar-overvoltage-protection-stmicroelectronics.pdf) - Useful for understanding real selection logic, overvoltage protection use, and dynamic-stress considerations.
- [Teccor Thyristor Design Guide (legacy manufacturer guide, mirrored copy)](https://pe2bz.philpem.me.uk/Parts-Active/SCR-Triac/00_thyristor_design_guide.pdf) - A classic practical guide covering triggering methods, phase control, and application-oriented SCR design ideas.
