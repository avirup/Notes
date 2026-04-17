# Chapter 1.3: DIAC and TRIAC

## Chapter opening

DIACs and TRIACs extend the thyristor-family idea of controlled switching into the domain of line-frequency AC power control. A **TRIAC** is a three-terminal bidirectional switching device used to control power from an AC source. A **DIAC** is a two-terminal bilateral trigger device commonly used to fire a TRIAC with improved symmetry.

These devices became important in practical circuits such as light dimmers, heater regulators, fan controllers, and small appliance switches. This chapter examines their operating principles, V-I characteristics, TRIAC triggering quadrants, and the basic DIAC-TRIAC phase-control circuit. It also shows why resistive loads are easier to control than inductive loads, and why TRIACs remain useful in auxiliary AC control even though modern PWM converters use other switching devices.

## Prerequisites check

- You should know the basic SCR ideas from Chapter 1.2: latching, holding current, gate triggering, and natural turn-off at current zero.
- You should know the relation between RMS and peak value for a sinusoid: $V_m = \sqrt{2}V_{rms}$.
- You should be comfortable with the difference between a **resistive load** and an **inductive load**.
- You should know the basic idea of an RC charging circuit.
- You should know that mains-connected circuits require voltage margin, current margin, and transient protection.

If the SCR terms **latching current** and **holding current** are not yet clear, review Chapter 1.2 before continuing.

## Core content

### 1.3.1 History of DIAC and TRIAC

Early AC power control often relied on either mechanical switches or resistor-based regulators. A mechanical switch provides only full ON or full OFF operation. A series resistor can reduce the power delivered to a load, but it does so by dissipating power as heat. Older fan regulators make this limitation obvious: the control element itself becomes warm because it is wasting energy.

The SCR introduced controlled switching, but it is fundamentally a unidirectional device. AC control therefore required either two SCRs connected in anti-parallel or a single device capable of controlled conduction in both half-cycles. The TRIAC emerged as that single-device solution. Manufacturer literature describes the TRIAC as a semiconductor device used to control power from an AC source and notes its importance in domestic, building, and industrial applications [ST AN5114, Sec. 1.1].

The DIAC became important as a companion trigger device. In simple RC phase-control circuits, direct triggering of a TRIAC can lead to uneven firing in the positive and negative half-cycles. A DIAC remains in the blocking state until its breakover voltage is reached in either polarity and then switches abruptly, producing a sharp trigger pulse with reasonably good symmetry [ST DB3 Datasheet].

Table 3.1: Why DIAC and TRIAC became important

| Device | Practical need it addressed | Why it mattered |
|---|---|---|
| DIAC | Symmetrical triggering in both half-cycles | Helped simple RC control circuits fire more evenly |
| TRIAC | Controlled AC power with one device instead of two anti-parallel SCRs | Reduced component count in dimmers, regulators, and small AC controllers |
| DIAC + TRIAC pair | Low-cost phase-angle control from mains supply | Enabled compact light dimmers, fan regulators, heater controls, and small appliance controllers |

These devices are not the main switches in modern PWM inverter bridges, but their historical role remains instructive. They provide a clear introduction to bidirectional conduction, latching behavior, commutation limits, and waveform shaping at mains frequency.

### 1.3.2 Construction, operating principle, V-I characteristics

#### The DIAC

The **DIAC** is a two-terminal bilateral trigger device. It has no gate terminal and is not intended to carry the main load current continuously. Its usual function is to remain in the blocking state until the voltage across it reaches the breakover value $V_{BO}$, then switch abruptly and deliver a current pulse [ST AN2703, Table 2], [ST DB3 Datasheet].

At low applied voltage in either polarity, only a very small leakage current flows. As the magnitude of the applied voltage approaches $V_{BO}$, the device enters breakover. Once conduction begins, the DIAC voltage falls while the current rises. This negative-resistance triggered characteristic is what makes the transition sharp rather than gradual [ST AN2703, Table 2].

The ST DB3 datasheet gives representative values [ST DB3 Datasheet]:

- typical breakover voltage: $32 \text{ V}$
- guaranteed breakover range: $28 \text{ V}$ to $36 \text{ V}$
- breakover-voltage symmetry: within $3 \text{ V}$
- maximum breakover current: $50 \ \mu\text{A}$

In a DIAC-TRIAC phase-control circuit, these values mean that the capacitor in the trigger network can charge for much of the half-cycle and then discharge suddenly into the TRIAC gate when the DIAC reaches breakover. The DIAC therefore acts as a symmetrical trigger element rather than as the main power switch.

**Image prompt for Figure 3.1:** Create a clean textbook-style graph of the V-I characteristic of a DIAC. Use horizontal axis voltage $V_D$ in volts and vertical axis current $I_D$ in amperes. Show symmetrical positive and negative breakover behavior. Mark $+V_{BO}$ and $-V_{BO}$, the small leakage-current region near the origin, the abrupt turn-on point at $I_{BO}$, the negative-resistance transition where device voltage falls as current rises, and the lower on-state voltage region labeled $V_F$. Add brief annotations "blocking region," "breakover," and "conduction region."

Two additional parameters are commonly used. The **breakover current**, $I_{BO}$, is the current flowing just before switching [ST AN2703, Table 2]. The **dynamic breakover voltage**, $\Delta V$, is the difference between the DIAC breakover voltage and the DIAC voltage at $10 \text{ mA}$ [ST AN2703, Table 2]. Together they describe how abruptly the device enters conduction.

#### The TRIAC

The **TRIAC** is a three-terminal bidirectional AC switch with terminals **A1**, **A2**, and **G** for gate. In some texts A1 and A2 are written **MT1** and **MT2**. This chapter uses A1 and A2 to match common manufacturer notation [ST BTA16 Datasheet].

A useful conceptual model is two thyristor-like conduction paths connected back-to-back and controlled by a common gate region. ST AN437 uses this comparison to explain bidirectional conduction and latching behavior [ST AN437, Sec. 1.1.1]. The model is simplified, but it captures the essential operating idea: the TRIAC can be triggered in either current direction and, once triggered, remains ON until its current falls below the holding current.

**Image prompt for Figure 3.2:** Create a textbook-style technical illustration of a TRIAC. On the left, show the circuit symbol with terminals labeled A1, A2, and G. On the right, show a simplified internal-conduction concept: two thyristor-like conduction paths arranged back-to-back sharing a common gate region. Add a note that the figure is a simplified conceptual model, not a literal silicon cross-section. Include arrows showing possible current flow from A2 to A1 and from A1 to A2 when triggered.

#### TRIAC blocking and conduction behavior

When a TRIAC is connected in series with an AC load, it blocks voltage in both polarities until an adequate gate signal is applied. After triggering, the voltage across the device falls to a low on-state value and load current flows. The device then latches and remains ON until the main current falls below the **holding current**, $I_H$ [ST AN302], [ST AN2703, Table 2].

At turn-on there is a related parameter called the **latching current**, $I_L$, defined as the minimum A2-to-A1 current required to maintain conduction after the gate signal is removed [ST AN303], [ST AN2703, Table 2]. As with the SCR,

$$\boxed{I_L > I_H} \quad \text{(3.1)}$$

Low-power loads can therefore be troublesome. If the load current does not rise high enough after the gate pulse, the TRIAC may fail to latch or may drop out prematurely. ST AN303 gives the practical example of a $10 \text{ W}$ signal lamp on European $230 \text{ V}$ mains, where the peak current can be close to the latching-current range of some devices [ST AN303, Sec. 1.1].

#### TRIAC V-I characteristic

The TRIAC V-I characteristic is approximately symmetrical in the first and third quadrants. In normal use the main operating regions are:

- off-state blocking for positive voltage
- off-state blocking for negative voltage
- on-state conduction for positive current
- on-state conduction for negative current

Unlike the DIAC, the TRIAC is not ordinarily used by allowing uncontrolled breakover; it is normally triggered by its gate. Once triggered, its on-state voltage is low. The ST BTA16 datasheet gives a maximum peak on-state voltage of about $1.55 \text{ V}$ at the stated test condition, together with threshold and dynamic-resistance parameters that describe conduction [ST BTA16 Datasheet]. This low on-state drop explains why TRIAC control is usually much more efficient than resistor-based control.

**Image prompt for Figure 3.3:** Create a clean engineering graph of the V-I characteristic of a TRIAC. Use horizontal axis $V_{A2A1}$ in volts and vertical axis $I_T$ in amperes. Show first- and third-quadrant blocking regions, first- and third-quadrant conduction regions, a note that practical operation uses gate triggering rather than breakover, and mark the low on-state voltage region. Add labels for holding current $I_H$ and indicate that current must fall below this magnitude for the TRIAC to turn OFF.

#### DIAC and TRIAC compared

Table 3.2: DIAC and TRIAC at a glance

| Feature | DIAC | TRIAC |
|---|---|---|
| Number of terminals | 2 | 3 |
| Main role | Trigger device | AC power switch |
| Gate terminal | No | Yes |
| Direction of use | Bilateral | Bilateral |
| Typical use | Triggering a TRIAC or SCR | Switching or phase-controlling AC load current |
| Important parameter | Breakover voltage $V_{BO}$ | Gate trigger current $I_{GT}$, latching current $I_L$, holding current $I_H$ |
| Current capability | Small trigger current pulses | Load current capability from small fractions of an ampere to many amperes depending on part |

The DIAC and TRIAC serve different functions in the same circuit. The DIAC shapes the trigger event; the TRIAC carries the load current.

### 1.3.3 Modes of operation of TRIAC; DIAC-TRIAC based phase control (concept)

TRIAC phase control depends on two linked ideas: quadrant-sensitive gate triggering and delayed conduction within each half-cycle. The DIAC-TRIAC pair combines these ideas in a simple line-frequency control circuit.

#### TRIAC triggering quadrants

Because TRIAC operation depends on both main-terminal polarity and gate-current polarity, triggering is described by **quadrants**. The relevant quantities are the sign of the main-terminal voltage $V_{A2A1}$ and the sign of the gate current with respect to A1 [ST AN4363, Sec. 3.1], [ST AN2703, Table 2].

Table 3.3: TRIAC triggering quadrants

| Quadrant | Main-terminal voltage | Gate-current polarity | Practical note |
|---|---|---|---|
| QI | $V_{A2A1} > 0$ | Gate current positive with respect to A1 | Common and usually sensitive |
| QII | $V_{A2A1} > 0$ | Gate current negative with respect to A1 | Valid, but latching behavior can be less favorable |
| QIII | $V_{A2A1} < 0$ | Gate current negative with respect to A1 | Common and usually sensitive |
| QIV | $V_{A2A1} < 0$ | Gate current positive with respect to A1 | Often the least sensitive quadrant in standard TRIACs |

Trigger sensitivity is not the same in all four quadrants. Standard four-quadrant devices often require the largest gate current in QIV, and many snubberless TRIACs are specified only for QI, QII, and QIII [ST BTA16 Datasheet], [ST AN4363, Table 2]. This matters because DIAC-triggered circuits naturally operate in QI and QIII, where the gate-current polarity follows the line-voltage polarity [ST AN4363, Sec. 3.2].

**Image prompt for Figure 3.4:** Create a clean textbook-style diagram of TRIAC triggering quadrants. Show the TRIAC symbol with A1, A2, and G. Around it, place four small labeled panels: QI with $V_{A2A1}>0$ and positive gate current, QII with $V_{A2A1}>0$ and negative gate current, QIII with $V_{A2A1}<0$ and negative gate current, and QIV with $V_{A2A1}<0$ and positive gate current. Use clear arrows for current direction and add a note that many DIAC-triggered circuits operate in QI and QIII.

#### Firing angle and the DIAC trigger network

For a sinusoidal mains supply,

$$\boxed{v_s(t) = V_m \sin(\omega t)} \quad \text{(3.2)}$$

where $V_m$ is the peak value and $\omega = 2\pi f$ is the angular frequency. For a $230 \text{ V}$, $50 \text{ Hz}$ supply,

$$\boxed{V_m = \sqrt{2}V_{rms}} \quad \text{(3.3)}$$

so

$$V_m = \sqrt{2}\times 230 \approx 325 \text{ V}.$$

If the TRIAC is triggered exactly at the beginning of each half-cycle, the load receives almost the full sinusoidal waveform. If triggering is delayed, the TRIAC remains OFF during the early part of the half-cycle and turns ON only later. This delay is the **firing angle**, $\alpha$.

For a resistive load:

- from the zero crossing to angle $\alpha$, the TRIAC is OFF and the load voltage is zero
- from angle $\alpha$ to $\pi$, the TRIAC is ON and the load receives the supply voltage
- the same pattern repeats in the negative half-cycle

Phase control therefore changes the conduction interval, not the peak value of the supply. The load receives chopped sinusoidal segments rather than a reduced-amplitude sine wave.

In the classic DIAC-TRIAC control circuit, an RC network charges during each half-cycle. When the capacitor voltage magnitude reaches the DIAC breakover voltage, the DIAC switches ON and discharges the capacitor into the TRIAC gate. A small resistance gives early firing and a small value of $\alpha$; a large resistance gives later firing and a larger value of $\alpha$. The DIAC sharpens the gate pulse and improves half-cycle symmetry [ST DB3 Datasheet], [ST AN308, Sec. 1.3].

For $50 \text{ Hz}$ mains, one full cycle lasts $20 \text{ ms}$ and one half-cycle lasts $10 \text{ ms}$. A firing angle of $30^\circ$ begins conduction early in that $10 \text{ ms}$ interval, $90^\circ$ begins near the midpoint, and $150^\circ$ allows conduction only near the end. This time-domain interpretation is often useful in understanding household dimmers and fan regulators.

#### RMS output for a resistive load

For a purely resistive load, if the TRIAC fires at angle $\alpha$ in each half-cycle, the output voltage is present only from $\alpha$ to $\pi$ in the positive half-cycle and from $\pi+\alpha$ to $2\pi$ in the negative half-cycle. The RMS value is

$$V_{o,rms}^2 = \frac{1}{2\pi}\left[2\int_{\alpha}^{\pi} V_m^2 \sin^2\theta \, d\theta\right] \quad \text{(3.4)}$$

where $\theta = \omega t$. Using

$$\int \sin^2\theta \, d\theta = \frac{\theta}{2} - \frac{\sin 2\theta}{4},$$

we obtain

$$V_{o,rms}^2 = \frac{V_m^2}{\pi}\left[\frac{\pi-\alpha}{2} + \frac{\sin 2\alpha}{4}\right].$$

Taking the square root gives

$$\boxed{V_{o,rms} = V_m\sqrt{\frac{1}{2\pi}\left[(\pi-\alpha)+\frac{\sin 2\alpha}{2}\right]}} \quad \text{(3.5)}$$

For a resistive load $R_L$, the power is

$$\boxed{P_L = \frac{V_{o,rms}^2}{R_L}} \quad \text{(3.6)}$$

Equation (3.5) gives the expected limits. When $\alpha = 0$, the output is the full supply waveform. As $\alpha$ increases, the conduction interval shortens and the RMS output decreases. As $\alpha \to \pi$, the output power approaches zero.

#### Numerical example: 1 kW heater on 230 V mains

Suppose a heater is rated at $1 \text{ kW}$ on $230 \text{ V}$, so its resistance is approximately

$$R_L = \frac{V^2}{P} = \frac{230^2}{1000} = 52.9 \ \Omega.$$

Now suppose the TRIAC is triggered at $\alpha = 90^\circ = \pi/2$. In Equation (3.5),

- $\pi - \alpha = \pi/2$
- $\sin 2\alpha = \sin \pi = 0$

Therefore,

$$V_{o,rms} = 325\sqrt{\frac{1}{2\pi}\cdot\frac{\pi}{2}} = 325\sqrt{\frac{1}{4}} = 162.5 \text{ V}.$$

The load power is then

$$P_L = \frac{162.5^2}{52.9} \approx 499 \text{ W}.$$

A firing angle of $90^\circ$ therefore reduces the heater power from about $1000 \text{ W}$ to about $500 \text{ W}$. The load still sees full mains peaks during the conducting interval, but its effective RMS voltage and power are lower.

#### Inductive loads, commutation, and snubbers

Inductive loads complicate TRIAC control because the current lags the voltage. For an $R$-$L$ load,

$$\boxed{\tan\phi = \frac{\omega L}{R}} \quad \text{(3.7)}$$

where $\phi$ is the current lag angle, $L$ is load inductance, and $R$ is load resistance [ST AN308, Sec. 1.2].

If the current lags, the TRIAC may continue conducting after the voltage crosses zero. The next half-cycle may then begin before the previous conduction interval has fully ended. The result can be asymmetrical operation, increased commutation stress, audible noise, torque ripple, flicker, or unwanted DC components in some loads.

This is why simple DIAC-TRIAC phase-control circuits work best with resistive or only mildly inductive loads [ST AN308, Sec. 1.1-1.3]. Inductive-load applications often require an RC snubber, a snubberless TRIAC with stronger commutation capability, or a more deliberate gate-drive strategy such as pulse-train triggering [ST AN437, Sec. 1.1-1.3].

### 1.3.4 Applications: light dimmers, fan regulators, small AC loads

DIAC-TRIAC control is most effective where the operating frequency is the mains frequency, the load current is moderate, and waveform-quality requirements are not severe.

#### Light dimmers and heater control

Incandescent lamps and resistive heaters are the classic applications. Because current is nearly in phase with voltage, triggering is predictable and turn-off occurs naturally at each current zero. The relation between firing angle, RMS voltage, and delivered power is therefore straightforward. Manufacturer literature lists light dimmers and heating regulators among standard TRIAC applications [ST BTA16 Datasheet], [ST AN5114, Sec. 1.1].

Modern LED lamps are more complicated because many contain rectifiers, capacitors, and control electronics. A TRIAC dimmer designed for incandescent loads may therefore flicker or behave poorly with some LED lamps.

#### Fan regulators and small motor control

Electronic ceiling-fan regulators are familiar examples of TRIAC phase control. They replaced resistor-based regulators largely because they waste less power as heat. The load, however, is inductive. Motor current, torque, heating, acoustic noise, and symmetry therefore depend more strongly on commutation behavior and trigger quality than in a resistive heater circuit [ST AN302, Sec. 1.2-1.3], [ST AN308, Sec. 1.1-1.3].

TRIAC control in such circuits reduces effective voltage, not supply frequency. It is therefore not equivalent to a modern variable-frequency drive.

#### Small AC loads, static relays, and appliance switching

TRIACs are also used in static relays, small pumps, solenoids, appliance control boards, induction-motor starting functions, and inrush-limiting functions [ST BTA16 Datasheet]. In these applications, load type determines how simple the control circuit can be.

Table 3.4: Where DIAC-TRIAC control fits well and where it does not

| Load or application | Suitability of simple DIAC-TRIAC phase control | Reason |
|---|---|---|
| Incandescent lamp | Very good | Load is mostly resistive |
| Resistive heater | Very good | Current follows voltage closely |
| Small ceiling fan regulator | Moderate | Works in practice, but motor is inductive and may hum or heat |
| Small induction motor with varying load | Limited | Phase lag and commutation issues become important |
| Transformer primary control | Use with caution | Magnetizing current and asymmetry can create stress |
| Main switch of a modern PV inverter | Poor choice | High-quality PWM control is needed instead |
| Grid-tied battery inverter AC bridge | Poor choice | Harmonics and control requirements are far more demanding |

When simple phase-control circuits are used, the DIAC remains valuable because breakover symmetry helps reduce half-cycle imbalance. In practice this can reduce flicker, acoustic noise, and unwanted DC bias in the load current.

## Worked interpretation exercise

The following condensed exercise shows how a DIAC datasheet and a TRIAC datasheet are read together for a simple $230 \text{ V}$ mains controller.

### Step 1: Check the mains-voltage class

For a $230 \text{ V}$, $50 \text{ Hz}$ single-phase supply,

$$V_m = \sqrt{2}\times 230 \approx 325 \text{ V}.$$

The OFF-state device must withstand at least this peak value, plus margin for tolerance and transients. ST AN4363 indicates that $600 \text{ V}$ TRIACs suit most single-phase mains applications, while $800 \text{ V}$ classes are preferred for higher-voltage or higher-stress situations [ST AN4363, Sec. 2.1]. The key design habit is to compare the device blocking-voltage rating with the **peak** line voltage, not with the RMS value alone.

### Step 2: Read the DIAC as a trigger device

The DB3 datasheet gives the essential DIAC data directly [ST DB3 Datasheet]:

- breakover voltage range: $28 \text{ V}$ to $36 \text{ V}$
- typical breakover voltage: $32 \text{ V}$
- breakover symmetry: $3 \text{ V}$ maximum
- breakover current: $50 \ \mu\text{A}$ maximum

These values show that the capacitor in the trigger network needs only a modest fraction of the mains peak voltage to fire the DIAC, and that positive and negative half-cycle triggering can be reasonably well balanced. The DIAC is therefore read as a symmetrical pulse-trigger element, not as the main load switch.

### Step 3: Read the TRIAC against the load

The BTA16 family provides $600 \text{ V}$ or $800 \text{ V}$ blocking classes, an $I_{T(RMS)}$ rating of $16 \text{ A}$, and quadrant-dependent gate-trigger current [ST BTA16 Datasheet]. Its latching and holding currents are in the tens of milliamperes range, so ordinary lamps and heaters are usually easy loads, while very small electronic loads can be problematic. For inductive loads, the datasheet recommendation for snubberless variants or an external snubber becomes important.

In practical design, the DIAC and TRIAC must be chosen together. The DIAC determines the trigger event; the TRIAC must match the load current, voltage class, triggering quadrant, and commutation duty.

## How this matters in renewable-energy systems

TRIACs are rarely the main switches in modern solar PV inverters, battery converters, wind-turbine converters, or EV traction drives. Those systems rely on self-commutated, PWM-capable devices such as MOSFETs, IGBTs, or wide-bandgap switches. The chapter nevertheless remains relevant because auxiliary AC functions inside larger systems may still use line-frequency switching, and because ideas such as firing angle, latching current, holding current, commutation, and waveform distortion carry forward to later converter topics.

## Chapter summary

- A **DIAC** is a two-terminal bilateral trigger device characterized mainly by breakover behavior.
- A **TRIAC** is a three-terminal bidirectional latching AC switch with terminals A1, A2, and G.
- In simple phase-control circuits, the DIAC produces a sharp and reasonably symmetrical trigger pulse for the TRIAC.
- TRIAC triggering is described by quadrants; DIAC-triggered circuits commonly operate in QI and QIII.
- Phase-angle control delays conduction within each half-cycle, so the load receives chopped sinusoidal segments rather than a reduced-amplitude sine wave.
- For a resistive load, Equation (3.5) gives the RMS output voltage as a function of firing angle $\alpha$.
- Inductive loads complicate TRIAC control because current lags voltage and commutation becomes more demanding.
- DIAC-TRIAC control is well suited to line-frequency control of resistive and mildly inductive loads, but not to the main switching function in modern PWM-based converters.

## Further reading

- [ST AN5114: Controlling a Triac with a phototriac](https://www.st.com/resource/en/application_note/an5114-controlling-a-triac-with-a-phototriac-stmicroelectronics.pdf) - A clear manufacturer introduction to TRIAC use in mains AC control and practical triggering methods.
- [ST AN4363: How to select the triac, ACS, or ACST that fits your application](https://www.st.com/resource/en/application_note/dm00096037-how-to-select-the-triac-acs-or-acst-that-fits-your-application-stmicroelectronics.pdf) - Useful for learning about triggering quadrants, voltage-class selection, and the link between circuit type and device choice.
- [ST DB3 / DB4 / SMDB3 Datasheet](https://www.st.com/resource/en/datasheet/db3.pdf) - A compact DIAC datasheet showing breakover voltage, symmetry, breakover current, and typical trigger applications.
- [ST BTA16 Datasheet](https://www.st.com/resource/en/datasheet/bta16.pdf) - A practical TRIAC datasheet for studying current rating, voltage rating, quadrant trigger current, holding current, latching current, and commutation capability.
- [ST AN308: TRIAC analog control circuits for inductive loads](https://www.st.com/resource/en/application_note/an308-triac-analog-control-circuits-for-inductive-loads-stmicroelectronics.pdf) - A valuable application note on inductive-load behavior, trigger symmetry, and reliable analog control.
