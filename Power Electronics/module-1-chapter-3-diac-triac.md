# Chapter 1.3: DIAC and TRIAC

## Chapter opening

Chapter 1.2 introduced the SCR as a gate-triggered power device that can block voltage, latch into conduction, and turn OFF only when current falls low enough. That was an important turning point, because it taught us that power-electronics switches are not all controlled in the same way. This chapter now takes that idea into the world of AC power control.

The two devices in this chapter are the **DIAC** and the **TRIAC**. They are closely related, but they do different jobs. A TRIAC is a three-terminal bidirectional thyristor-family device used to control power from an AC source. A DIAC is a two-terminal bidirectional trigger device that is often used to help fire a TRIAC more symmetrically. Together they form one of the classic building blocks of light dimmers, fan regulators, heater controls, and small AC load controllers.

This chapter matters for three reasons. First, it gives you a practical entry point into AC power control at 230 V, 50 Hz, which is the supply environment you are likely to meet in Indian homes, labs, and many field installations. Second, it teaches an important waveform idea: we can control delivered power not by wasting energy in a resistor, but by deciding when in each AC half-cycle a semiconductor switch begins to conduct. Third, it prepares your intuition for later converter chapters. Modern solar inverters, EV converters, and battery interfaces usually do not use TRIACs in their main PWM bridges, but the language of firing angle, commutation, latching, holding current, harmonics, and gate-drive strategy carries forward.

By the end of the chapter, you should be able to explain what a DIAC does, how a TRIAC conducts in both directions, why TRIAC triggering is described using quadrants, how a DIAC-TRIAC phase-control circuit delays conduction in each half-cycle, and why some loads behave well with TRIAC control while others do not.

## Prerequisites check

- You should know the basic SCR ideas from Chapter 1.2: latching, holding current, gate triggering, and natural turn-OFF at current zero.
- You should know the relation between RMS and peak value for a sinusoid. If needed, remember that $V_m = \sqrt{2}V_{rms}$.
- You should be comfortable with the difference between a **resistive load** and an **inductive load**.
- You should know the basic idea of an RC charging circuit, even if you are not yet fully confident with the mathematics.
- You should know that mains-connected circuits need voltage margin, current rating margin, and protection against unwanted transients.

If the SCR terms **latching current** and **holding current** feel weak, review Chapter 1.2 before going further. We will use them again here, because a TRIAC is also a latching device.

## Core content

### 1.3.1 History of DIAC and TRIAC

Let us begin with an everyday problem.

Suppose you want to control the brightness of a lamp or the speed of a small AC fan from a 230 V, 50 Hz supply. A mechanical switch gives only full ON or full OFF. A variable resistor can reduce power, but it wastes energy as heat. In older fan regulators, that wasted heat was easy to feel with your hand. Engineers wanted a compact solid-state device that could control AC power more efficiently and more quietly.

The SCR solved part of that problem, but not all of it. An SCR conducts mainly in one direction. So for AC control, one option is to use two SCRs in anti-parallel. That works, but it increases circuit complexity. A single device that could perform controlled conduction in both directions was much more attractive. That is the practical background from which the TRIAC became important.

STMicroelectronics describes the TRIAC as a semiconductor device “essential in controlling power from an AC source” and notes its wide use in home appliances, building automation, and industrial control [ST AN5114, Sec. 1.1]. That one sentence captures the historical role of the TRIAC very well. It is not mainly a high-frequency converter switch. It is a mains-frequency AC power-control device.

The **TRIAC** name is commonly understood as coming from “triode for alternating current.” Whether or not a source gives that expansion explicitly, the functional idea is clear: the device is meant for alternating-current switching in both directions. In a practical sense, the TRIAC became the convenient single-package answer to many low- and medium-power AC switching problems that would otherwise need two thyristors or a more complicated electromechanical solution [ST AN5114, Sec. 1.1-1.2], [ST AN4363, Sec. 3.1-3.2].

The **DIAC** appeared as the TRIAC’s natural companion in simple analog phase-control circuits. If we try to trigger a TRIAC directly from a resistor-capacitor network, it is easy to get uneven firing in the positive and negative half-cycles. The DIAC improves that situation by remaining OFF until a fairly definite breakover voltage is reached in either direction, then switching suddenly and delivering a sharp trigger pulse. ST’s DB3/DB4 datasheet describes the DIAC as a “trigger diode with a fixed voltage reference” intended for use with TRIACs in simplified gate-control circuits [ST DB3 Datasheet].

There is one point where we should be careful and honest. The manufacturer sources used for this chapter clearly explain what the DIAC and TRIAC do and where they are used, but they do not all give a clean, single historical date for first commercial introduction. So rather than repeating a date from an unverified secondary source, it is better to say the following:

- the SCR came first as the foundational thyristor-family controlled power device,
- the TRIAC followed as a bidirectional AC switch for simpler AC power control,
- the DIAC became a common trigger companion that improved symmetry and trigger sharpness in phase-control circuits.

That historical sequence is solid and matches the device family evolution presented by manufacturers and standard power-electronics texts [ST AN5114, Sec. 1.1-1.2], [ST AN4363, Sec. 3.1-3.2].

Table 3.1: Why DIAC and TRIAC became important

| Device | Practical need it addressed | Why it mattered |
|---|---|---|
| DIAC | Symmetrical triggering in both half-cycles | Helped simple RC control circuits fire more evenly |
| TRIAC | Controlled AC power with one device instead of two anti-parallel SCRs | Reduced component count in dimmers, regulators, and small AC controllers |
| DIAC + TRIAC pair | Low-cost phase-angle control from mains supply | Enabled compact light dimmers, fan regulators, heater controls, and small appliance controllers |

A common misconception is that DIACs and TRIACs are “old dimmer parts” and therefore not worth studying. That is too narrow a view. It is true that they are older devices and that they are not the main switches in modern PWM inverter bridges. But they still matter because they teach line-frequency power control, bidirectional conduction, latching behavior, commutation limits, and waveform chopping in a very direct way.

*Renewable-energy relevance.* In modern renewable-energy conversion, TRIACs are rarely the main switch in a PV inverter, battery DC-DC converter, or EV traction inverter. But they still appear in auxiliary AC switching, heater control, bypass functions, and some inrush-limiting or small-load control tasks. More importantly, the way they shape AC waveforms helps us understand why later renewable-energy converters care so much about harmonics, commutation, and switch selection.

### 1.3.2 Construction, operating principle, V-I characteristics

We will study the DIAC first, because it is the simpler device electrically. Then we will study the TRIAC, which is the actual AC power switch.

#### The DIAC

The **DIAC** is a two-terminal, bilateral trigger device. “Bilateral” means it behaves in both voltage polarities. Unlike the TRIAC, it has no gate terminal. It is not meant to carry large load current continuously. Instead, it is meant to stay in a blocking state until the voltage across it reaches a characteristic breakover level. Then it switches abruptly into conduction and delivers a pulse of current [ST AN2703, Table 2], [ST DB3 Datasheet].

At beginner level, the most useful way to think of the DIAC is not as a power switch, but as a trigger element with symmetry built into it.

If we apply a small positive or negative voltage across a DIAC, almost no current flows. The device blocks. If we keep increasing the magnitude of that voltage, a threshold is eventually reached. That threshold is the **breakover voltage**, written $V_{BO}$. Once the DIAC breaks over, current increases sharply and the voltage across the device drops to a lower value. ST’s parameter note explicitly states that DIACs have a **negative-resistance triggered characteristic** [ST AN2703, Table 2].

That phrase needs a careful explanation, because it can sound abstract.

In an ordinary resistor, more current means more voltage drop, according to Ohm’s law. In a DIAC near breakover, the opposite trend briefly appears. As conduction starts, the current rises while the device voltage falls from the breakover level toward a lower conduction voltage. That falling-voltage, rising-current behavior is why the trigger transition is sharp rather than gradual.

The ST DB3 datasheet gives a very useful real example [ST DB3 Datasheet]:

- typical breakover voltage for the DB3: $32 \text{ V}$
- guaranteed breakover range: $28 \text{ V}$ to $36 \text{ V}$
- breakover-voltage symmetry: within $3 \text{ V}$
- maximum breakover current: $50 \ \mu\text{A}$

These values immediately tell us why the DIAC is so useful in phase control. A capacitor can charge quietly through a resistor for much of the half-cycle. Then, when its voltage reaches about 32 V in magnitude, the DIAC suddenly conducts and dumps a pulse into the TRIAC gate circuit.

**Image prompt for Figure 3.1:** Create a clean textbook-style graph of the V-I characteristic of a DIAC. Use horizontal axis voltage $V_D$ in volts and vertical axis current $I_D$ in amperes. Show symmetrical positive and negative breakover behavior. Mark $+V_{BO}$ and $-V_{BO}$, the small leakage-current region near the origin, the abrupt turn-on point at $I_{BO}$, the negative-resistance transition where device voltage falls as current rises, and the lower on-state voltage region labeled $V_F$. Add brief annotations “blocking region,” “breakover,” and “conduction region.”

Two additional DIAC terms are worth knowing.

The first is **breakover current**, $I_{BO}$. This is the current flowing just before the device switches into breakover mode [ST AN2703, Table 2]. In plain language, it tells us the DIAC is about to snap ON, not yet fully conducting.

The second is **dynamic breakover voltage**, $\Delta V$. ST defines this as the difference between the DIAC breakover voltage and the DIAC voltage at 10 mA [ST AN2703, Table 2]. This parameter measures how sharply the device voltage collapses after triggering.

So the DIAC operating story is:

1. The applied voltage rises in either polarity.
2. The DIAC blocks and passes only tiny leakage current.
3. The voltage magnitude reaches $V_{BO}$.
4. The DIAC switches abruptly.
5. The device voltage falls while current rises.
6. A current pulse becomes available to trigger another device, usually a TRIAC.

That last step is the real purpose in most power-electronics circuits.

ST’s DB3 datasheet also tells us the intended use directly. It lists the DIAC as a “triggering device for Triac or SCR based motor / light dimmer” [ST DB3 Datasheet]. So when we read a DIAC datasheet, we should not think, “This is a miniature power switch.” We should think, “This is a symmetrical trigger generator.”

#### The TRIAC

The **TRIAC** is a three-terminal bidirectional AC switch. Its terminals are usually called:

- **A1**
- **A2**
- **G** for gate

Many books also call A1 and A2 **MT1** and **MT2**, meaning main terminal 1 and main terminal 2. In this chapter we will use **A1** and **A2**, because that is the notation commonly used in manufacturer datasheets such as the BTA16 series [ST BTA16 Datasheet].

The simplest physical intuition for the TRIAC is this: it is a single device that can be triggered into conduction in either current direction, and once triggered, it latches like a thyristor until current falls below the holding current.

ST’s AN437 gives a useful structural comparison. It says that a TRIAC “can be compared to two thyristors mounted in back-to-back and coupled with a single control area” [ST AN437, Sec. 1.1.1]. That is not a perfect internal-physics model of every detail, but it is an excellent beginner model. It explains two essential facts:

- the TRIAC can conduct current in both directions,
- the TRIAC behaves like a latching thyristor device, not like a continuously controlled transistor.

ST AN4363 adds another useful structural insight. It explains that the TRIAC can be switched on by either positive or negative gate current because of the way the gate region is connected into the internal structure [ST AN4363, Sec. 3.1]. This is the foundation of TRIAC quadrant triggering, which we will study in the next section.

**Image prompt for Figure 3.2:** Create a textbook-style technical illustration of a TRIAC. On the left, show the circuit symbol with terminals labeled A1, A2, and G. On the right, show a simplified internal-conduction concept: two thyristor-like conduction paths arranged back-to-back sharing a common gate region. Add a note that the figure is a simplified conceptual model, not a literal silicon cross-section. Include arrows showing possible current flow from A2 to A1 and from A1 to A2 when triggered.

#### TRIAC blocking and conduction behavior

Suppose we connect a TRIAC in series with a 230 V, 50 Hz load. The supply voltage is sinusoidal. If no gate signal is applied, the TRIAC blocks in both polarities, except for a small leakage current. Once a suitable gate signal is applied, the TRIAC enters conduction. The voltage across it collapses to a relatively low on-state value, and load current flows. After that, the gate no longer needs to keep driving the device continuously. The TRIAC remains ON until its main current falls below the **holding current**, $I_H$ [ST AN302], [ST AN2703, Table 2].

Just after triggering, there is a related but slightly higher requirement called **latching current**, $I_L$. ST defines $I_L$ as the minimum A2-to-A1 current needed to keep the device conducting after gate current is removed [ST AN303], [ST AN2703, Table 2]. As in the SCR case, we usually have

$$\boxed{I_L > I_H} \quad \text{(3.1)}$$

That means the TRIAC needs a little extra current to establish conduction initially, but once conduction is well established it can continue at a somewhat lower current.

This is exactly why very light loads, especially some small electronic loads, can behave badly with TRIAC circuits. The device may trigger, but if the load current does not rise enough, the TRIAC may fail to latch or may drop out unexpectedly.

ST’s AN303 gives a particularly useful low-power example. For a 10 W signal lamp on European 230 V mains, the peak load current is only about 61 mA, which can be uncomfortably close to the latching-current limit of some TRIACs [ST AN303, Sec. 1.1]. That is a very practical warning: low-power AC control can be harder than it first appears.

#### TRIAC V-I characteristic

A TRIAC V-I characteristic is broadly symmetrical in the first and third quadrants, because the device is intended to conduct in both directions. The main operating regions are:

- **off-state blocking** in positive polarity
- **off-state blocking** in negative polarity
- **on-state conduction** in positive polarity
- **on-state conduction** in negative polarity

Unlike a DIAC, the TRIAC does not normally rely on uncontrolled breakover in ordinary use. It is usually triggered by its gate. Once triggered, the device voltage falls to a low on-state value.

The ST BTA16 datasheet gives a maximum peak on-state voltage of about $1.55 \text{ V}$ at a specified test current and pulse width, and a threshold-type on-state parameter $V_{T0}$ of about $0.85 \text{ V}$ with a dynamic resistance parameter $R_D$ of about $25 \text{ m}\Omega$ at high junction temperature [ST BTA16 Datasheet].

Those are important practical numbers. They show why TRIAC control is usually much more efficient than old resistor-type regulators. When the TRIAC is ON, the device itself drops only a small voltage compared with the hundreds of volts on the mains side. That does not mean loss is zero, but it means the control method does not work by deliberately burning large power in a series resistor.

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

A common misconception is that the DIAC is just a “small TRIAC without a gate.” That is not a good description. The DIAC is not meant to replace the TRIAC as the main load switch. It is meant to help the TRIAC trigger in a controlled and symmetrical way.

Another misconception is that the TRIAC behaves like a voltage-controlled resistor. It does not. It is better thought of as a switch that is OFF for part of each half-cycle and ON for the remaining part.

*Renewable-energy relevance.* The DIAC and TRIAC teach an important distinction between line-frequency AC control and high-frequency conversion. In a TRIAC circuit, we shape the delivered power by delaying conduction inside each mains half-cycle. In a modern PV inverter or battery converter, we usually control power with high-frequency PWM using MOSFETs or IGBTs. Understanding the TRIAC helps you see why these are different classes of control problem.

### 1.3.3 Modes of operation of TRIAC; DIAC-TRIAC based phase control (concept)

This section is the heart of the chapter. We will first understand TRIAC triggering quadrants, and then we will use that knowledge to understand the classic DIAC-TRIAC phase-control circuit.

#### TRIAC triggering quadrants

Because a TRIAC can conduct in both directions and can be triggered by different gate-current polarities, we describe its triggering conditions using **quadrants**.

The two signs that matter are:

- the polarity of the main-terminal voltage $V_{A2A1}$
- the polarity of the gate current with respect to A1

This gives four possible combinations [ST AN4363, Sec. 3.1], [ST AN2703, Table 2]:

Table 3.3: TRIAC triggering quadrants

| Quadrant | Main-terminal voltage | Gate-current polarity | Practical note |
|---|---|---|---|
| QI | $V_{A2A1} > 0$ | Gate current positive with respect to A1 | Common and usually sensitive |
| QII | $V_{A2A1} > 0$ | Gate current negative with respect to A1 | Valid, but latching behavior can be less favorable |
| QIII | $V_{A2A1} < 0$ | Gate current negative with respect to A1 | Common and usually sensitive |
| QIV | $V_{A2A1} < 0$ | Gate current positive with respect to A1 | Often the least sensitive quadrant in standard TRIACs |

Manufacturer data shows that the quadrants are not equally easy to trigger. The ST BTA16 datasheet, for example, gives a higher maximum gate-trigger current in QIV than in the other quadrants for standard 4-quadrant devices, and many snubberless TRIACs are specified only for QI, QII, and QIII rather than QIV [ST BTA16 Datasheet], [ST AN4363, Table 2].

This is a very practical point. A TRIAC is not just “on” or “off.” The way you drive its gate determines which triggering quadrant you are using, and that affects sensitivity and reliable operation.

ST AN4363 also makes an especially useful statement for this chapter: control circuits using a **DIAC** or an **opto-triac** naturally operate in **QI and QIII**, because the gate-current polarity follows the line-voltage polarity [ST AN4363, Sec. 3.2]. This is one reason DIAC-triggered circuits are so convenient. They avoid the least attractive quadrant in many TRIAC types.

**Image prompt for Figure 3.4:** Create a clean textbook-style diagram of TRIAC triggering quadrants. Show the TRIAC symbol with A1, A2, and G. Around it, place four small labeled panels: QI with $V_{A2A1}>0$ and positive gate current, QII with $V_{A2A1}>0$ and negative gate current, QIII with $V_{A2A1}<0$ and negative gate current, and QIV with $V_{A2A1}<0$ and positive gate current. Use clear arrows for current direction and add a note that many DIAC-triggered circuits operate in QI and QIII.

#### The firing-angle idea

Now let us move from device behavior to waveform control.

Take a sinusoidal mains voltage:

$$\boxed{v_s(t) = V_m \sin(\omega t)} \quad \text{(3.2)}$$

Here,

- $v_s(t)$ is the instantaneous supply voltage,
- $V_m$ is the peak value of the sinusoid,
- $\omega = 2\pi f$ is angular frequency,
- $f$ is the mains frequency.

For a 230 V, 50 Hz supply,

$$\boxed{V_m = \sqrt{2}V_{rms}} \quad \text{(3.3)}$$

so

$$V_m = \sqrt{2}\times 230 \approx 325 \text{ V}.$$

If a TRIAC were triggered exactly at the beginning of each half-cycle, it would conduct through almost the full half-cycle, and the load would receive nearly the full mains waveform. But if we delay the trigger, the TRIAC stays OFF during the early part of the half-cycle and only turns ON later. That delay is described by the **firing angle**, usually written $\alpha$.

For a resistive load:

- from the zero crossing to angle $\alpha$, the TRIAC is OFF and the load voltage is zero,
- from angle $\alpha$ to $\pi$, the TRIAC is ON and the load receives the supply voltage,
- the same pattern repeats in the negative half-cycle.

So the TRIAC does not reduce the peak of the supply. It reduces the time during which the load is connected.

That distinction is very important. The load sees a chopped waveform, not a smaller sine wave.

#### How the DIAC helps create firing angle

In the classic DIAC-TRIAC control circuit, an RC network charges during each half-cycle. The TRIAC gate is not driven directly from the mains at all times. Instead, the capacitor charges gradually through a resistor or potentiometer. When the capacitor voltage magnitude reaches the DIAC breakover voltage, the DIAC switches ON and the capacitor discharges through the DIAC into the TRIAC gate. That produces a sharp gate pulse.

If the resistance is small, the capacitor charges quickly and the DIAC fires early. Then the TRIAC firing angle $\alpha$ is small and the load receives more power.

If the resistance is large, the capacitor charges more slowly and the DIAC fires later. Then $\alpha$ is larger and the load receives less power.

The DIAC helps in two important ways:

1. It produces a sharper pulse than a soft direct RC feed into the gate.
2. Its breakover symmetry helps keep positive- and negative-half-cycle triggering more nearly balanced [ST DB3 Datasheet], [ST AN308, Sec. 1.3].

ST’s AN308 makes this second point very clearly for inductive-load control. It explains that the capacitor charges from zero, and the DIAC triggers the TRIAC as soon as the capacitor voltage reaches the DIAC breakover voltage $V_{BO}$, adding that this timing is the same for both half-waves because it depends on the DIAC breakover symmetry [ST AN308, Sec. 1.3].

That is exactly why the DIAC is so useful. Without it, direct gate triggering can be less symmetrical and more sensitive to gate-threshold differences and waveform distortion.

#### RMS output for a resistive load

Now let us quantify what phase control does to a resistive load.

For a purely resistive load, if the TRIAC fires at angle $\alpha$ in each half-cycle, the output voltage is present only from $\alpha$ to $\pi$ in the positive half-cycle and from $\pi+\alpha$ to $2\pi$ in the negative half-cycle.

The RMS value is obtained from the square-law definition:

$$V_{o,rms}^2 = \frac{1}{2\pi}\left[2\int_{\alpha}^{\pi} V_m^2 \sin^2\theta \, d\theta\right] \quad \text{(3.4)}$$

where $\theta = \omega t$.

We now use the standard integral

$$\int \sin^2\theta \, d\theta = \frac{\theta}{2} - \frac{\sin 2\theta}{4}.$$

Substituting into Equation (3.4),

$$V_{o,rms}^2 = \frac{V_m^2}{\pi}\left[\frac{\pi-\alpha}{2} + \frac{\sin 2\alpha}{4}\right].$$

Taking square root gives the commonly used result:

$$\boxed{V_{o,rms} = V_m\sqrt{\frac{1}{2\pi}\left[(\pi-\alpha)+\frac{\sin 2\alpha}{2}\right]}} \quad \text{(3.5)}$$

For a resistive load $R_L$, the power is then

$$\boxed{P_L = \frac{V_{o,rms}^2}{R_L}} \quad \text{(3.6)}$$

These equations are worth pausing over.

- If $\alpha = 0$, then the TRIAC conducts for the whole half-cycle, and Equation (3.5) reduces to the full RMS value of the supply.
- If $\alpha$ increases, the conduction interval becomes shorter, so $V_{o,rms}$ decreases.
- If $\alpha$ approaches $\pi$, almost no conduction occurs, so the output power approaches zero.

This is the mathematical expression of dimming or power reduction by phase control.

#### Numerical example: 1 kW heater on 230 V mains

Suppose a heater is rated at $1 \text{ kW}$ on $230 \text{ V}$, so its resistance is approximately

$$R_L = \frac{V^2}{P} = \frac{230^2}{1000} = 52.9 \ \Omega.$$

Now suppose we trigger the TRIAC at $\alpha = 90^\circ = \pi/2$.

In Equation (3.5),

- $\pi - \alpha = \pi/2$
- $\sin 2\alpha = \sin \pi = 0$

So

$$V_{o,rms} = 325\sqrt{\frac{1}{2\pi}\cdot\frac{\pi}{2}} = 325\sqrt{\frac{1}{4}} = 162.5 \text{ V}.$$

Then the load power is

$$P_L = \frac{162.5^2}{52.9} \approx 499 \text{ W}.$$

So a firing angle of $90^\circ$ reduces the heater power from about $1000 \text{ W}$ to about $500 \text{ W}$.

This example is physically useful because it shows that phase control changes **effective RMS voltage and power**, even though the load still sees full mains peaks during the part of the half-cycle when the TRIAC is ON.

#### What changes with an inductive load

Inductive loads are more difficult.

For a resistive load, current and voltage are in phase, so when the voltage crosses zero, the current also crosses zero. That makes TRIAC turn-OFF straightforward.

For an inductive load, the current lags the voltage. AN308 writes the phase relation in the familiar form

$$\boxed{\tan\phi = \frac{\omega L}{R}} \quad \text{(3.7)}$$

where $\phi$ is the current lag angle, $L$ is load inductance, and $R$ is load resistance [ST AN308, Sec. 1.2].

If the current lags, the TRIAC may continue conducting beyond the voltage zero crossing. That changes everything:

- the TRIAC may still be ON when the next trigger pulse arrives,
- the next half-cycle may not start symmetrically,
- commutation stress becomes important,
- audible noise, torque ripple, flicker, or DC bias can appear in some loads.

AN308 shows that simple triggering circuits can become asymmetrical or even unacceptable for strongly inductive loads if the trigger strategy is too simple [ST AN308, Sec. 1.1-1.3]. This is why textbook dimmer circuits work best with resistive or only slightly inductive loads, and why motor-control TRIAC circuits need more care.

#### Turn-off, commutation, and snubbers

A TRIAC usually turns OFF naturally at current zero, but that does not mean turn-OFF is always easy. When the current falls to zero and the supply voltage is reapplied, remaining charge inside the device can cause unwanted retriggering, especially with inductive loads. ST AN437 explains this in detail and notes that the slope of the decreasing current and the slope of the reapplied voltage both matter [ST AN437, Sec. 1.1-1.3].

That is why inductive-load TRIAC circuits often need:

- a **snubber circuit** across the TRIAC,
- a **snubberless TRIAC** with better commutation capability,
- a better trigger strategy such as pulse-train gating.

These are not decorative additions. They are what separates a neat-looking circuit from a reliable circuit.

#### Common misconceptions about DIAC-TRIAC phase control

- **Mistake 1:** “The TRIAC reduces AC voltage like a transformer tap.”  
  No. It chops the waveform by delaying conduction.

- **Mistake 2:** “The DIAC controls power directly.”  
  No. The DIAC mainly provides a symmetrical trigger pulse.

- **Mistake 3:** “If the average load current is low, the TRIAC will always work fine.”  
  Not necessarily. Latching current, holding current, and quadrant sensitivity still matter.

- **Mistake 4:** “A simple dimmer circuit should work the same for a lamp and for a motor.”  
  No. Inductive loads change current timing, commutation stress, and symmetry.

- **Mistake 5:** “A TRIAC is suitable anywhere AC must be controlled.”  
  No. It is excellent in some line-frequency AC control problems and a poor choice in many high-performance converter problems.

*Renewable-energy relevance.* This section gives a first taste of why converter engineers care so much about waveforms. A phase-controlled TRIAC load draws chopped, non-sinusoidal current from the grid. That may be acceptable for a lamp dimmer or small heater, but it is not what we want at the AC interface of a modern solar inverter or grid-tied battery converter. There, current quality, harmonic performance, and controllability are much more demanding.

### 1.3.4 Applications: light dimmers, fan regulators, small AC loads

The best way to understand applications is to divide them by load type.

#### Light dimmers and heater control

This is the classic TRIAC application.

With an incandescent lamp or resistive heater, the current is roughly in phase with voltage. That means:

- the TRIAC triggers predictably,
- it turns OFF naturally at each current zero,
- the firing-angle idea maps cleanly into RMS voltage and delivered power.

That is why phase-angle dimmers and heater controllers became such a natural use for DIAC-TRIAC circuits. ST’s application material explicitly lists light dimmers, heating regulation, and appliance motor speed control among common TRIAC uses [ST BTA16 Datasheet], [ST AN5114, Sec. 1.1].

In practical terms, a TRIAC heater controller works far more efficiently than a series resistor controller, because the TRIAC is either blocking or conducting with a relatively low on-state drop. The control does introduce harmonic current, but for small standalone loads this tradeoff has often been acceptable.

One subtle point is worth adding. Modern LED lamps are often not simple resistive loads. They may contain rectifiers, capacitors, and control electronics. That means an old TRIAC dimmer that works beautifully with an incandescent lamp may flicker or behave poorly with some LED lamps. This is one reason modern lighting compatibility can be more complicated than the older lamp-dimmer examples in introductory textbooks.

#### Fan regulators and small motor control

In the Indian context, the electronic ceiling-fan regulator is one of the most familiar TRIAC applications. It replaced the older resistor-based regulator because it wastes less power as heat.

But we should be careful not to oversimplify. A fan motor is not a resistive heater. It is an inductive machine. So although phase control can reduce effective applied voltage and therefore reduce speed, the motor current, torque, heating, hum, and waveform quality all become more complicated.

AN302 and AN308 give practical warnings here. AN302 shows that holding-current issues can reduce conduction time or create asymmetry in small motor circuits if the designer relies on sample behavior rather than worst-case datasheet limits [ST AN302, Sec. 1.2-1.3]. AN308 shows that simple TRIAC trigger circuits can become asymmetrical with inductive loads, especially when phase lag is significant [ST AN308, Sec. 1.1-1.3].

So the practical lesson is:

- TRIAC fan regulators are common and useful,
- but they are not ideal motor drives,
- and they need proper component selection, layout, and suppression.

They reduce voltage, not frequency. That is a major difference from a modern variable-frequency motor drive.

#### Small AC loads, static relays, and appliance switching

TRIACs are also widely used as compact AC switches in:

- static relays,
- small pumps,
- solenoids,
- heating elements,
- appliance control boards,
- induction-motor starting functions,
- inrush-current limiting functions.

The BTA16 datasheet explicitly lists static relays, heating regulation, induction motor starting circuits, light dimmers, and appliance motor speed controllers as intended application areas [ST BTA16 Datasheet].

For these applications, the designer must match the TRIAC type to the load:

- **Resistive load:** simple phase control usually works well.
- **Slightly inductive load:** often workable, but EMI and commutation need attention.
- **Strongly inductive load:** use better trigger strategy, snubber network, or a snubberless device; sometimes use a different topology altogether.

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

#### Why the DIAC still matters in these applications

A student may ask: if the TRIAC is the main power device, why do we still care about the DIAC?

Because the quality of triggering strongly affects the quality of control.

The ST DB3 datasheet gives a breakover symmetry of about 3 V [ST DB3 Datasheet]. That does not mean perfect symmetry in the entire circuit, but it does mean the trigger element itself is designed not to favor one half-cycle strongly over the other. In a light dimmer or fan regulator, that is helpful because asymmetrical firing can create DC content, visible flicker, extra heating, or acoustic noise.

The DIAC is therefore small, but not unimportant. It is the part that turns a vague charging waveform into a clean trigger event.

#### A 230 V / 50 Hz intuition check

Here is a helpful way to visualize a common household regulator.

At 50 Hz, one full cycle lasts $20 \text{ ms}$. Each half-cycle lasts $10 \text{ ms}$.

If a DIAC-TRIAC regulator fires at:

- $\alpha = 30^\circ$, the TRIAC conducts through most of the half-cycle,
- $\alpha = 90^\circ$, it conducts through about half of the half-cycle,
- $\alpha = 150^\circ$, it conducts only near the end of the half-cycle.

So phase control is really time control inside each 10 ms half-cycle.

That time-domain picture is often easier to understand than starting with formulas.

*Renewable-energy relevance.* Auxiliary loads inside renewable-energy systems are still often ordinary AC loads: cabinet fans, pumps, heaters, contactor auxiliaries, or bypass loads. TRIAC-based control may still appear there, especially where cost and simplicity matter more than waveform perfection. But for the main energy-conversion path, renewable systems usually move to transistor-based PWM converters because they need precise control, better harmonic performance, and bidirectional power flow.

## Worked interpretation exercise

We will now read two real device artifacts together:

- the [ST DB3 Datasheet](https://www.st.com/resource/en/datasheet/db3.pdf)
- the [ST BTA16 Datasheet](https://www.st.com/resource/en/datasheet/bta16.pdf)

This is a good exercise because a practical analog mains controller often uses exactly this kind of pair: a DIAC as trigger device and a TRIAC as the main AC switch.

### Step 1: Start from the mains voltage, not from the part number

For a 230 V, 50 Hz single-phase supply,

$$V_m = \sqrt{2}\times 230 \approx 325 \text{ V}.$$

So a TRIAC in the OFF state must withstand at least that peak value, plus margin for tolerance and transients.

ST AN4363 states that 600 V devices fit most single-phase applications, while 800 V devices are required for many three-phase line-to-line applications because the peak voltage is close to or above 600 V [ST AN4363, Sec. 2.1]. This already teaches a very important datasheet-reading habit:

- for **230 V single-phase** control, a 600 V TRIAC is often a reasonable starting point,
- for **415 V three-phase** line-to-line conditions, the peak is about $415\sqrt{2} \approx 587 \text{ V}$, so an 800 V class is the sensible minimum and often more margin is preferred.

That one calculation prevents a common mistake: choosing a device based only on the RMS mains value.

### Step 2: Read the DIAC as a trigger part, not as a load switch

The DB3 datasheet tells us the essentials immediately [ST DB3 Datasheet]:

- breakover voltage range: $28 \text{ V}$ to $36 \text{ V}$
- typical breakover voltage: $32 \text{ V}$
- breakover symmetry: $3 \text{ V}$ maximum
- breakover current: $50 \ \mu\text{A}$ maximum
- repetitive peak on-state current: up to $2 \text{ A}$ for DB3/DB4 under stated short-pulse conditions

How should we interpret these?

The $32 \text{ V}$ typical breakover tells us the capacitor in the RC trigger network must charge to only about one-tenth of the 325 V mains peak before the DIAC fires. So in a 230 V dimmer circuit, available voltage is not the limiting issue. The timing is determined by the RC charging process, not by lack of amplitude.

The 3 V breakover symmetry matters because it means positive and negative half-cycle triggering can be fairly similar. That helps reduce half-cycle imbalance.

The short-pulse current capability tells us the DIAC can survive the brief trigger discharge, but it is not intended to carry the main load current continuously.

This is exactly how we want to read the part: it is a pulse-trigger element with reasonably symmetrical breakover.

### Step 3: Read the TRIAC as the real load-current device

From the BTA16 datasheet, key headline values are [ST BTA16 Datasheet]:

- $I_{T(RMS)} = 16 \text{ A}$
- $V_{DRM}/V_{RRM} = 600 \text{ V}$ or $800 \text{ V}$ depending on variant
- on-state surge current $I_{TSM} = 160 \text{ A}$ for one 20 ms half-cycle at 50 Hz
- maximum peak on-state voltage around $1.55 \text{ V}$ at the stated test condition

That already tells us the BTA16 is far beyond the needs of a small lamp dimmer, but it may be a good rugged choice for heater control or small motor control where surge and thermal margin matter.

Now read the gate and current-threshold parameters carefully.

For standard 4-quadrant BTA16 types, the datasheet gives maximum gate-trigger current values that depend on quadrant, with QIV requiring the largest current. It also gives holding current and latching current values that vary with variant and quadrant [ST BTA16 Datasheet].

For snubberless variants, ST gives only 3-quadrant triggering data, not QIV. That might sound like a limitation until we remember what AN4363 says: DIAC-triggered circuits operate in QI and QIII [ST AN4363, Sec. 3.2]. So for a DIAC-triggered mains controller, a 3-quadrant snubberless TRIAC can still be a perfectly good choice.

This is an excellent example of why datasheet reading is not only about reading one table. It is about connecting:

- the circuit type,
- the operating quadrants,
- the load type,
- and the device family.

### Step 4: Check latching and holding current against the real load

The BTA16 datasheet gives holding-current and latching-current values in the tens of milliamperes range, depending on the exact type and quadrant [ST BTA16 Datasheet].

That tells us a 100 W incandescent lamp on 230 V, which draws about

$$I_{rms} = \frac{100}{230} \approx 0.435 \text{ A},$$

is not likely to present a holding-current problem once conduction is established.

But a very small electronic load can be much less forgiving. This is consistent with AN303’s warning that even a 10 W lamp can bring latching behavior uncomfortably close to device limits in some cases [ST AN303, Sec. 1.1].

So if a dimmer behaves badly only at very low load, that is not “mysterious.” It often points directly to $I_L$, $I_H$, gate-pulse width, or quadrant sensitivity.

### Step 5: Decide whether the load is inductive

The BTA16 datasheet explicitly says snubberless versions are especially recommended for inductive loads because of their high commutation performance [ST BTA16 Datasheet].

That immediately tells us something practical:

- for a heater or incandescent lamp, a standard TRIAC may be entirely adequate,
- for a fan motor or pump, the inductive nature of the load makes commutation tougher, so a snubberless type or an RC snubber may be the safer choice.

This interpretation is reinforced by AN437, which explains how inductive loads create turn-off stress and why a snubber may be needed to limit reapplied $dV/dt$ [ST AN437, Sec. 1.1-1.3].

### Step 6: Put the two devices together as a design conversation

Table 3.5: Interpreting the DB3 and BTA16 together

| Data item | What it says | What it means for a DIAC-TRIAC controller |
|---|---|---|
| DB3 $V_{BO}$ typ. $32 \text{ V}$ | DIAC fires at a moderate capacitor voltage | RC timing can create variable firing angle well within a 230 V mains half-cycle |
| DB3 symmetry 3 V max | Positive and negative firing thresholds are close | Better half-cycle balance |
| BTA16 600 V / 800 V classes | Different blocking-voltage options | 600 V suits most 230 V single-phase cases; 800 V is preferred for higher-stress cases |
| BTA16 quadrant-dependent $I_{GT}$ | Trigger sensitivity depends on quadrant | Gate-drive circuit and chosen control topology matter |
| BTA16 $I_H$ and $I_L$ in tens of mA | Device needs enough current to latch and stay ON | Very small or difficult loads may misbehave |
| Snubberless versions recommended for inductive loads | Turn-off stress matters | Fan and motor loads need more care than heaters |

This is the design-reading habit we want to develop. A datasheet is not only a list of numbers. It is telling us how the device expects to be used.

## How this matters in renewable-energy systems

DIACs and TRIACs are not the main workhorses of modern solar PV inverters, battery energy storage converters, wind-turbine back-to-back converters, or EV traction inverters. Those systems usually need self-commutated, high-frequency, PWM-capable devices such as MOSFETs, IGBTs, or wide-bandgap switches.

But the ideas in this chapter still matter in renewable-energy systems in several ways.

First, TRIAC-class AC switches still appear in **auxiliary AC functions**. Examples include small cabinet heaters, cooling fans, pumps, solenoids, or bypass loads inside renewable-energy installations and UPS systems. These are not glamorous circuits, but real systems depend on them.

Second, TRIACs and SCR-family devices remain relevant in **inrush-limiting and AC-side switching** roles. Some inverter-chargers, UPS bypass arrangements, and mains-interface auxiliaries still use thyristor-family devices where line-frequency switching is acceptable.

Third, this chapter teaches why **phase-angle control is not enough** for the main renewable-energy conversion path. A TRIAC controller chops the mains waveform and can inject harmonic current. That may be acceptable for a lamp dimmer or heater controller, but not for a grid-connected converter that must regulate sinusoidal current, power factor, bidirectional flow, and harmonic limits.

Finally, the chapter strengthens the language we will keep using later:

- firing angle,
- latching current,
- holding current,
- commutation,
- $dV/dt$ stress,
- load-dependent waveform behavior.

Those ideas reappear, even when the devices later change.

## Chapter summary

- A **DIAC** is a two-terminal bilateral trigger device used mainly to generate a sharp trigger pulse for a TRIAC or SCR.
- A **TRIAC** is a three-terminal bidirectional thyristor-family AC switch with terminals A1, A2, and gate G.
- The TRIAC became important because it allowed controlled AC switching with one device instead of two anti-parallel SCRs [ST AN5114, Sec. 1.1-1.2].
- ST’s DB3 datasheet presents the DIAC as a fixed-voltage trigger device for TRIAC- and SCR-based dimmer and motor-control circuits [ST DB3 Datasheet].
- DIACs are characterized by **breakover voltage** $V_{BO}$, **breakover current** $I_{BO}$, and a **negative-resistance triggered characteristic** [ST AN2703, Table 2].
- For the ST DB3, the typical breakover voltage is about $32 \text{ V}$ and the breakover symmetry is about $3 \text{ V}$ maximum [ST DB3 Datasheet].
- A TRIAC latches after triggering, so normally $I_L > I_H$:
  $\boxed{I_L > I_H}$.
- Sinusoidal mains voltage can be written as
  $\boxed{v_s(t)=V_m\sin(\omega t)}$.
- Peak and RMS voltage are related by
  $\boxed{V_m=\sqrt{2}V_{rms}}$.
- For 230 V RMS mains, the peak value is about $325 \text{ V}$.
- TRIAC triggering is described using four quadrants based on the polarity of $V_{A2A1}$ and the gate current.
- Standard TRIACs may be specified for 4-quadrant triggering, while many snubberless TRIACs are specified for only 3 quadrants [ST BTA16 Datasheet], [ST AN4363, Table 2].
- DIAC-triggered circuits naturally operate in quadrants QI and QIII [ST AN4363, Sec. 3.2].
- For a resistive load under phase-angle control, the RMS output voltage is
  $\boxed{V_{o,rms} = V_m\sqrt{\frac{1}{2\pi}\left[(\pi-\alpha)+\frac{\sin 2\alpha}{2}\right]}}$.
- Load power for a resistive load is
  $\boxed{P_L = \frac{V_{o,rms}^2}{R_L}}$.
- Inductive loads complicate TRIAC control because current lags voltage; a useful relation is
  $\boxed{\tan\phi=\frac{\omega L}{R}}$.
- Simple DIAC-TRIAC control works best for resistive or only slightly inductive loads.
- Fan regulators and small motor controllers can use TRIACs, but they are more sensitive to commutation problems, asymmetry, and snubber requirements [ST AN302], [ST AN308], [ST AN437].
- TRIACs are very useful for line-frequency AC control, but they are not appropriate as the main switching device for modern PWM-based renewable-energy converters.

## Further reading

- [ST AN5114: Controlling a Triac with a phototriac](https://www.st.com/resource/en/application_note/an5114-controlling-a-triac-with-a-phototriac-stmicroelectronics.pdf) — A clear manufacturer introduction to what TRIACs do in mains AC control and how their triggering and isolation are handled in practice.
- [ST AN4363: How to select the triac, ACS, or ACST that fits your application](https://www.st.com/resource/en/application_note/dm00096037-how-to-select-the-triac-acs-or-acst-that-fits-your-application-stmicroelectronics.pdf) — Very useful for learning about triggering quadrants, voltage-class selection, and the link between circuit type and device choice.
- [ST DB3 / DB4 / SMDB3 Datasheet](https://www.st.com/resource/en/datasheet/db3.pdf) — A compact DIAC datasheet that clearly shows breakover voltage, symmetry, breakover current, and typical trigger applications.
- [ST BTA16 Datasheet](https://www.st.com/resource/en/datasheet/bta16.pdf) — A practical TRIAC datasheet that is excellent for studying current rating, voltage rating, quadrant trigger current, holding current, latching current, and commutation capability.
- [ST AN308: TRIAC analog control circuits for inductive loads](https://www.st.com/resource/en/application_note/an308-triac-analog-control-circuits-for-inductive-loads-stmicroelectronics.pdf) — A valuable application note showing why simple TRIAC circuits behave differently with inductive loads and how better triggering strategies improve symmetry and reliability.
