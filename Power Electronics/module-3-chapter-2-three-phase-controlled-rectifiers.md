# Chapter 3.2: Three-phase Controlled Rectifiers

## Chapter opening

Single-phase controlled rectifiers are the right place to begin, because they let us see phase control clearly. But real power systems often do not stop at single-phase supply. Industrial feeders, large motor drives, battery-forming systems, renewable-energy interfaces, and classical HVDC converters commonly work from a three-phase source. Once we move from one phase to three phases, several things improve at once: power transfer becomes smoother, the ripple frequency rises, transformer and source utilization improve, and higher power levels become practical [Rashid, *Power Electronics: Circuits, Devices and Applications*, 4e, Ch. 6], [Mohan, Undeland, Robbins, *Power Electronics: Converters, Applications and Design*, 3e, Ch. 6].

This chapter develops that next step carefully. We first look at the **three-phase half-wave controlled rectifier** as an introductory topology. It helps us understand how thyristors take turns following the most positive phase. We then move to the more important **three-phase fully controlled bridge rectifier**, also called the **three-phase full converter** or, in practical power-converter language, a **six-pulse thyristor bridge**. That circuit is one of the most important classical AC-to-DC converters in power electronics [Mohan, Undeland, Robbins, *Power Electronics: Converters, Applications and Design*, 3e, Ch. 6].

By the end of the chapter, you should be comfortable with the main waveforms, the meaning of continuous conduction, the average-output-voltage expression, and the effect of firing angle $\alpha$ on the DC output. These ideas matter beyond the classroom. They reappear in classical wind-energy front ends, large DC drives, controlled battery charging, and line-commutated HVDC systems that transmit bulk power over long distances [Hitachi Energy, *HVDC converter stations*], [NPTEL, *Line Commutated and PWM Rectifiers*].

## Prerequisites check

- You should be comfortable with the SCR behavior studied in Chapter 1.2, especially gate triggering, latching, and natural line commutation.
- You should remember from Chapter 3.1 that the **firing angle** $\alpha$ is measured from the natural turn-ON point of the supply waveform.
- You should know the difference between an **R load** and an **R-L load**, and why an inductor tends to keep current continuous.
- You should be able to move between phase and line quantities in a balanced three-phase system, even if only at a basic level.
- You should remember that a 415 V, 50 Hz three-phase supply usually means **415 V line-to-line RMS**, not phase RMS.

If three-phase RMS quantities are not yet comfortable, pause here and quickly review that idea before going on. It will make the waveform discussion much easier.

### 3.2.1 Three-phase half-wave controlled rectifier (overview)

#### Why three-phase rectification feels different from single-phase rectification

In a single-phase rectifier, the source voltage rises and falls once in each half-cycle, and the output contains large gaps unless the load inductance is strong enough to keep current flowing. A three-phase source gives us three sinusoidal phase voltages displaced by $120^\circ$. That means when one phase is falling, another may be rising toward a useful value. The converter therefore finds a better path to the load more often.

Let the three balanced phase voltages be

$$v_{an} = V_m\sin\omega t$$

$$v_{bn} = V_m\sin\left(\omega t - \frac{2\pi}{3}\right)$$

$$v_{cn} = V_m\sin\left(\omega t - \frac{4\pi}{3}\right)$$

where $V_m$ is the peak phase voltage and $\omega = 2\pi f$ is the angular frequency [Rashid, *Power Electronics: Circuits, Devices and Applications*, 4e, Ch. 6].

For a balanced three-phase system,

$$\boxed{V_{ph,rms} = \frac{V_{LL,rms}}{\sqrt{3}}} \quad \text{(11.1)}$$

and

$$\boxed{V_m = \sqrt{2}\,V_{ph,rms}} \quad \text{(11.2)}$$

where $V_{ph,rms}$ is phase RMS voltage and $V_{LL,rms}$ is line-to-line RMS voltage.

For a 415 V, 50 Hz three-phase supply,

$$V_{ph,rms} = \frac{415}{\sqrt{3}} \approx 239.6 \text{ V}$$

and

$$V_m = \sqrt{2}\times 239.6 \approx 339 \text{ V}.$$

These numbers are worth keeping in mind because 415 V is a very common three-phase supply value in Indian industry and educational laboratories.

#### Circuit idea and mode of operation

The **three-phase half-wave controlled rectifier** uses three SCRs, one connected to each phase. The load is returned through the neutral. Only one SCR conducts at a time. The conducting SCR is the one whose phase is both:

- forward biased with respect to the load return, and
- triggered by its gate pulse.

In physical terms, the converter keeps selecting the phase that can presently deliver positive voltage to the load. Because the phases are shifted by $120^\circ$, the output becomes a sequence of positive segments taken from phase voltages rather than from line voltages.

**Image prompt for Figure 11.1:** Create a clean textbook-style technical illustration of a three-phase half-wave controlled rectifier using three SCRs connected from phase lines a, b, and c to a common positive load terminal, with the load returning to the neutral n. Show balanced phase voltages $v_{an}$, $v_{bn}$, and $v_{cn}$ displaced by $120^\circ$, and a lower waveform plot of output voltage $v_o$ showing successive positive segments from the three phases. Mark the firing angle $\alpha$, the conduction interval of one SCR, and the 120-degree phase displacement. Use monochrome engineering style with axes, labels, and units.

If the load current is sufficiently smooth, each SCR conducts for about $120^\circ$ electrical. The output then has three pulses per AC cycle, so the ripple frequency is

$$\boxed{f_{ripple} = 3f} \quad \text{(11.3)}$$

For a 50 Hz supply, that means a ripple frequency of

$$f_{ripple} = 3\times 50 = 150 \text{ Hz}.$$

That is already an improvement over a single-phase half-wave rectifier, whose ripple occurs only at 50 Hz.

#### Average output voltage in the continuous-current picture

Because the syllabus treats this circuit as an overview topic, we will not spend long on every operating mode. The most useful introductory result is the average DC output under the usual idealized assumption that current remains continuous and device drops are neglected. In that case,

$$\boxed{V_{o,avg} = \frac{3\sqrt{3}}{2\pi}V_m\cos\alpha} \quad \text{(11.4)}$$

This can also be written in RMS form as

$$\boxed{V_{o,avg} = 1.17\,V_{ph,rms}\cos\alpha = 0.675\,V_{LL,rms}\cos\alpha} \quad \text{(11.5)}$$

[Rashid, *Power Electronics: Circuits, Devices and Applications*, 4e, Ch. 6], [Mohan, Undeland, Robbins, *Power Electronics: Converters, Applications and Design*, 3e, Ch. 6], [IIT Bombay SequelApp, *Three-Phase Half-Wave Controlled Rectifier - 1*].

The coefficient $0.675$ is helpful because it lets us work directly from the common line-to-line rating.

For a 415 V supply and $\alpha = 30^\circ$,

$$V_{o,avg} = 0.675\times 415\times \cos 30^\circ$$

$$= 0.675\times 415\times 0.866 \approx 242.6 \text{ V}.$$

So even before we reach the full bridge, a three-phase source can provide a reasonably high average DC output with smoother ripple than the comparable single-phase circuit.

#### What this topology teaches us, and why it is not the final answer

The three-phase half-wave controlled rectifier is useful because it makes the conduction sequence easy to understand. But it also has limitations:

- it needs a neutral return,
- it uses only one controlled device at a time,
- its output comes from phase voltages rather than the larger line voltages,
- its ripple is higher than single-phase half-wave but lower than the full bridge,
- its transformer and source utilization are poorer than in the six-pulse bridge [Mohan, Undeland, Robbins, *Power Electronics: Converters, Applications and Design*, 3e, Ch. 6].

That is why the half-wave circuit is usually treated as a learning topology rather than the preferred high-power practical one.

One common misconception is worth naming clearly. The phrase "three-phase rectifier" does not automatically mean "full bridge." Three-phase half-wave and three-phase full-wave rectifiers are different circuits with different output levels and different device counts.

Another misconception is that gating alone decides which SCR conducts. Gating is necessary, but it is not sufficient. The SCR must also be forward biased by the phase voltages present at that instant.

Renewable-energy relevance: in modern renewable-energy hardware, this half-wave topology is rarely the final converter of choice. But it is still a useful stepping stone because it shows how phase selection works and prepares us for the six-pulse bridge and, later, for more advanced rectifier topologies.

### 3.2.2 Three-phase fully controlled bridge rectifier with R-L load; continuous conduction

#### Why the full bridge matters so much

The **three-phase fully controlled bridge rectifier** is the main classical thyristor rectifier. It uses six SCRs arranged in a bridge. Three devices belong to the upper group and connect the positive DC terminal to phases $a$, $b$, and $c$. Three devices belong to the lower group and connect the negative DC terminal to phases $a$, $b$, and $c$. At any instant, one upper-group SCR and one lower-group SCR conduct. The load is therefore connected across a line-to-line voltage, not just a phase-to-neutral voltage [Rashid, *Power Electronics: Circuits, Devices and Applications*, 4e, Ch. 6].

That single idea has big consequences:

- the output voltage is higher,
- the ripple frequency becomes $6f$,
- the neutral is not required,
- source utilization improves,
- high-power conversion becomes much more practical.

For a 50 Hz supply, the ripple frequency is

$$\boxed{f_{ripple} = 6f = 300 \text{ Hz}} \quad \text{(11.6)}$$

which is twice the ripple frequency of the three-phase half-wave circuit.

#### Continuous conduction and the role of the inductive load

The syllabus specifies the important case of an **R-L load with continuous conduction**. This means the load current does not fall to zero between conduction intervals. In practice, that usually requires appreciable inductance on the DC side. The inductance may come from the load itself, from a smoothing reactor, or from the effective inductive behavior of a motor armature or DC link [Mohan, Undeland, Robbins, *Power Electronics: Converters, Applications and Design*, 3e, Ch. 6].

The DC-side voltage equation may be written as

$$\boxed{v_o = Ri_d + L\frac{di_d}{dt} + E} \quad \text{(11.7)}$$

where:

- $v_o$ is the instantaneous converter output voltage,
- $R$ is the effective DC-side resistance,
- $L$ is the smoothing inductance,
- $i_d$ is the load current,
- $E$ is any DC-side back electromotive force, such as the back EMF of a motor or a battery-like opposing source.

When $L$ is large enough, $di_d/dt$ stays relatively small over one ripple period. The current then becomes nearly constant, which simplifies analysis and is also a realistic high-power operating condition.

#### Conduction sequence without getting lost in labels

To keep the notation clear, let us label the upper devices as $T_{a+}$, $T_{b+}$, and $T_{c+}$, and the lower devices as $T_{a-}$, $T_{b-}$, and $T_{c-}$.

With continuous current:

- one upper SCR conducts for $120^\circ$,
- one lower SCR conducts for $120^\circ$,
- the conducting pair changes every $60^\circ$,
- the DC load current continues to flow without interruption.

The pair sequence over one cycle is

- $(T_{a+}, T_{b-})$
- $(T_{a+}, T_{c-})$
- $(T_{b+}, T_{c-})$
- $(T_{b+}, T_{a-})$
- $(T_{c+}, T_{a-})$
- $(T_{c+}, T_{b-})$

Then the sequence repeats.

Each pair connects the load to one line-to-line voltage. For example, when $(T_{a+},T_{b-})$ conducts, the load sees $v_{ab}$. When $(T_{a+},T_{c-})$ conducts, the load sees $v_{ac}$. This is the key physical reason the full bridge gives a larger output than the half-wave circuit.

**Image prompt for Figure 11.2:** Create a clean textbook-style technical illustration of a three-phase fully controlled bridge rectifier with six SCRs, labeled $T_{a+}$, $T_{b+}$, $T_{c+}$ in the upper group and $T_{a-}$, $T_{b-}$, $T_{c-}$ in the lower group, feeding an R-L load with nearly constant current. Beside the circuit, show aligned waveforms of three phase voltages, gate pulses displaced by 60 degrees, output voltage made of successive line-to-line segments, and load current that is almost constant. Clearly mark that each SCR conducts for 120 degrees and each conducting pair lasts for 60 degrees. Use monochrome engineering style.

#### Visualizing the output waveform

The output of the full bridge is not a smooth DC line. It is a stepped waveform made from successive pieces of line-to-line sinusoids. But because there are six such pieces in each cycle, the ripple is much faster than in single-phase rectifiers.

That matters physically. A higher ripple frequency means the current-smoothing inductor has an easier job. For the same target current ripple, the required inductance is generally less than in a lower-ripple-frequency rectifier. This is one reason three-phase rectification is attractive at moderate and high power.

A very helpful intuition is this: the converter is always trying to connect the load between the most positive available phase and the most negative available phase, but only through the SCRs that have been triggered at the proper firing instants.

#### Numerical picture for a 415 V supply

For a 415 V line-to-line RMS system, the peak line-to-line voltage is

$$\boxed{V_{LL,peak} = \sqrt{2}\,V_{LL,rms}} \quad \text{(11.8)}$$

so

$$V_{LL,peak} = \sqrt{2}\times 415 \approx 587 \text{ V}.$$

This does not mean the average DC output is 587 V. That 587 V is the peak of the available line voltage. The average output depends on how much of each line-voltage segment we allow through, which is controlled by $\alpha$.

If $\alpha$ is small, the converter starts each conduction interval early, and the average DC output is high. If $\alpha$ is increased, the output segments shift to the right on the waveform, and the average DC output falls.

#### Practical note: what continuous conduction does and does not mean

Continuous conduction does **not** mean the output voltage is constant. It means the **current** stays above zero. The voltage can still ripple significantly while the current remains smooth because the inductor opposes rapid current change.

This is a common point of confusion. Students often see a nearly constant current and assume the voltage must also be nearly constant. In rectifiers, that is often not true.

#### Practical note: source inductance and overlap

Real three-phase supplies and transformers have inductance. Real commutation therefore takes a finite time, and current transfers gradually from one SCR to the next instead of instantaneously. That effect is called **commutation overlap**. It reduces the average DC output below the ideal formula and produces notches in source voltages [NPTEL, *Line Commutated and PWM Rectifiers*], [IIT Bombay SequelApp, *Three Phase Thyristor Controlled Rectifier*].

We will not derive overlap equations here because they are outside the present syllabus depth. But it is important to know that the ideal formula we derive next is an idealized result, not the last word in practical design.

Renewable-energy relevance: the six-pulse bridge is historically important in high-power conversion. Even where modern systems use PWM active rectifiers instead, the ideas of line commutation, continuous DC current, and DC-link formation remain essential background for wind, storage, and HVDC power stages [NPTEL, *Line Commutated and PWM Rectifiers*].

### 3.2.3 Average output voltage expression; effect of firing angle on DC output

#### Building the average-voltage formula from one conduction interval

Now we derive the most important result of the chapter. Under ideal conditions:

- the source is balanced,
- device drops are neglected,
- commutation overlap is neglected,
- load current is continuous.

During any one $60^\circ$ conduction interval, the load is connected to one line-to-line voltage. Suppose the active segment is

$$v_{ab} = \sqrt{3}\,V_m\sin\left(\omega t + \frac{\pi}{6}\right)$$

where $V_m$ is the peak phase voltage [Rashid, *Power Electronics: Circuits, Devices and Applications*, 4e, Ch. 6], [IIT Bombay SequelApp, *Three-Phase Full Wave Controlled Rectifier - 2*].

Because the same shape repeats six times per cycle, shifted in angle, we can average one interval and scale it over the full cycle:

$$V_{o,avg} = \frac{6}{2\pi}\int_{\pi/6+\alpha}^{\pi/2+\alpha}\sqrt{3}\,V_m\sin\left(\theta + \frac{\pi}{6}\right)d\theta$$

where $\theta = \omega t$.

Simplifying,

$$V_{o,avg} = \frac{3\sqrt{3}V_m}{\pi}\int_{\pi/6+\alpha}^{\pi/2+\alpha}\sin\left(\theta + \frac{\pi}{6}\right)d\theta.$$

Let

$$x = \theta + \frac{\pi}{6}.$$

Then the limits become $x = \pi/3+\alpha$ to $x = 2\pi/3+\alpha$, and

$$V_{o,avg} = \frac{3\sqrt{3}V_m}{\pi}\int_{\pi/3+\alpha}^{2\pi/3+\alpha}\sin x\,dx.$$

Carrying out the integration,

$$V_{o,avg} = \frac{3\sqrt{3}V_m}{\pi}\left[-\cos x\right]_{\pi/3+\alpha}^{2\pi/3+\alpha}.$$

So

$$V_{o,avg} = \frac{3\sqrt{3}V_m}{\pi}\left[\cos\left(\frac{\pi}{3}+\alpha\right)-\cos\left(\frac{2\pi}{3}+\alpha\right)\right].$$

Using the trigonometric identity, the bracketed term reduces to $\cos\alpha$. Therefore,

$$\boxed{V_{o,avg} = \frac{3\sqrt{3}}{\pi}V_m\cos\alpha} \quad \text{(11.9)}$$

This is the standard ideal result in terms of peak phase voltage.

Now express it in terms of the line-to-line RMS supply. Since

$$V_m = \sqrt{2}\,V_{ph,rms} = \sqrt{\frac{2}{3}}\,V_{LL,rms},$$

Equation (11.9) becomes

$$\boxed{V_{o,avg} = \frac{3\sqrt{2}}{\pi}V_{LL,rms}\cos\alpha} \quad \text{(11.10)}$$

or numerically,

$$\boxed{V_{o,avg} \approx 1.35\,V_{LL,rms}\cos\alpha} \quad \text{(11.11)}$$

[Rashid, *Power Electronics: Circuits, Devices and Applications*, 4e, Ch. 6], [Mohan, Undeland, Robbins, *Power Electronics: Converters, Applications and Design*, 3e, Ch. 6], [IIT Bombay SequelApp, *Three-Phase Full Wave Controlled Rectifier - 2*].

Equation (11.11) is one of the most useful formulas in introductory power electronics.

#### Interpreting the formula physically

The formula says something very important: in the ideal continuous-current full converter, the DC output depends on the cosine of the firing angle.

That gives three immediate operating regions:

- if $\alpha = 0^\circ$, then $\cos\alpha = 1$, so the output is maximum positive;
- if $\alpha = 90^\circ$, then $\cos\alpha = 0$, so the average output is zero;
- if $\alpha > 90^\circ$, then $\cos\alpha$ becomes negative, so the average output becomes negative.

But that third statement needs careful interpretation. A negative average output does **not** mean an ordinary passive R-L load will somehow push power back to the source by itself. For inversion operation, the DC side must have an active source such as a motor back EMF or another DC system able to maintain current [Mohan, Undeland, Robbins, *Power Electronics: Converters, Applications and Design*, 3e, Ch. 6].

#### Example: average output at several firing angles

Let the supply be 415 V line-to-line RMS. Then from Equation (11.11),

$$V_{o,avg} \approx 1.35\times 415\times \cos\alpha.$$

Since $1.35\times 415 \approx 560.25$, we get

$$V_{o,avg} \approx 560.25\cos\alpha.$$

Table 11.1 shows the result for several firing angles.

Table 11.1: Effect of firing angle on ideal average DC output for a 415 V three-phase full converter

| Firing angle $\alpha$ | $\cos\alpha$ | $V_{o,avg}$ |
| --- | --- | --- |
| $0^\circ$ | 1.000 | $560.3 \text{ V}$ |
| $30^\circ$ | 0.866 | $485.1 \text{ V}$ |
| $60^\circ$ | 0.500 | $280.1 \text{ V}$ |
| $75^\circ$ | 0.259 | $145.1 \text{ V}$ |
| $90^\circ$ | 0.000 | $0 \text{ V}$ |
| $105^\circ$ | -0.259 | $-145.1 \text{ V}$ |
| $120^\circ$ | -0.500 | $-280.1 \text{ V}$ |

This table is very revealing. A moderate increase in firing angle produces a strong reduction in average DC voltage. That is why SCR rectifiers were so useful in older adjustable-speed DC drives and in large controllable DC supplies.

#### Example: finding the firing angle from a required DC output

Suppose a three-phase full converter is fed from 415 V, 50 Hz mains and supplies a DC side that, on average, requires $V_{o,avg} = 350 \text{ V}$. What firing angle is needed under ideal continuous-current conditions?

Starting with Equation (11.11),

$$350 = 1.35\times 415 \times \cos\alpha.$$

So

$$\cos\alpha = \frac{350}{560.25} \approx 0.625.$$

Therefore,

$$\alpha = \cos^{-1}(0.625) \approx 51.3^\circ.$$

That is a very practical kind of calculation. In real equipment, a controller often determines the firing instant needed to achieve a desired average DC output.

#### Connecting the average converter voltage to the load

The converter output voltage is not the same as the load current requirement unless we include the load equation. For steady current, the average inductor voltage over one period is zero, so the average DC-side balance becomes

$$\boxed{V_{o,avg} = E + I_dR} \quad \text{(11.12)}$$

where $I_d$ is the average load current [IIT Bombay SequelApp, *Three-Phase Full Wave Controlled Rectifier - 2*].

This is extremely useful. It tells us that the converter must provide not just the opposing EMF $E$, but also the resistive drop $I_dR$.

As a short example, suppose a converter must supply a DC side with

- $E = 240 \text{ V}$,
- $R = 2\,\Omega$,
- $I_d = 80 \text{ A}$.

Then

$$V_{o,avg} = 240 + 80\times 2 = 400 \text{ V}.$$

Using Equation (11.11),

$$400 = 560.25\cos\alpha$$

so

$$\cos\alpha = 0.714$$

and

$$\alpha \approx 44.4^\circ.$$

This example has the feel of a controlled battery interface or a classical DC machine armature supply.

#### How firing angle affects the AC side too

The firing angle does not only change the DC average output. It also changes the AC-side current waveform and the power factor.

Here is the intuition:

- larger $\alpha$ delays current transfer,
- delayed current means the fundamental current component lags the supply voltage more,
- the source current remains non-sinusoidal because the converter is a switching circuit,
- therefore both **displacement** and **distortion** affect power factor [Mohan, Undeland, Robbins, *Power Electronics: Converters, Applications and Design*, 3e, Ch. 6], [NPTEL, *Line Commutated and PWM Rectifiers*].

At this stage, it is enough to remember that increasing $\alpha$ generally reduces average DC output and also worsens the input-side power-quality picture.

This is one reason modern EV chargers, battery-storage interfaces, and many renewable-energy grid converters increasingly use PWM rectifiers rather than line-commutated SCR front ends [NPTEL, *Line Commutated and PWM Rectifiers*].

#### Comparing the three-phase half-wave and full-wave circuits

Table 11.2 collects the most important contrasts.

Table 11.2: Comparison of introductory three-phase controlled rectifiers

| Feature | Three-phase half-wave controlled rectifier | Three-phase fully controlled bridge rectifier |
| --- | --- | --- |
| Controlled devices | 3 SCRs | 6 SCRs |
| Neutral required | Yes | No |
| Output built from | Phase voltages | Line-to-line voltages |
| Pulse number | 3-pulse | 6-pulse |
| Ripple frequency at 50 Hz | $150 \text{ Hz}$ | $300 \text{ Hz}$ |
| Ideal average output | $0.675\,V_{LL,rms}\cos\alpha$ | $1.35\,V_{LL,rms}\cos\alpha$ |
| Practical importance | Mainly instructional and limited applications | Major classical high-power rectifier topology |

#### A final caution about the meaning of negative average voltage

It is tempting to think that once $\alpha$ goes above $90^\circ$, the converter simply becomes a negative power supply. That is not the right beginner picture.

The safer way to say it is this: for continuous current, the converter is **capable** of negative average output voltage. Whether real inversion occurs depends on the DC side. There must be a source of DC power that keeps current flowing in the required direction. This is why line-commutated inversion appears naturally in HVDC links and regenerative DC-drive systems, not in an ordinary resistor load.

**Image prompt for Figure 11.3:** Create a clean textbook-style technical figure showing the ideal average DC output of a three-phase fully controlled bridge rectifier as firing angle changes. Include one plot of output-voltage waveform segments for $\alpha = 30^\circ$, one for $\alpha = 75^\circ$, and one for $\alpha = 105^\circ$, each with the average-value line marked. Add a second plot below of normalized average voltage $V_{o,avg}/V_{o,max}$ versus firing angle $\alpha$ from $0^\circ$ to $180^\circ$, showing the cosine trend, zero crossing at $90^\circ$, and negative region beyond $90^\circ$. Use monochrome textbook engineering style with axes, labels, and units.

Renewable-energy relevance: the cosine law of Equation (11.11) is part of the intellectual foundation for line-commutated conversion. Even when newer renewable-energy interfaces use PWM active rectifiers, engineers still compare them against this classical benchmark for controllability, power factor, and harmonic performance.

## Worked interpretation exercise

An official product page from Hitachi Energy for **phase controlled thyristors (PCT)** lists representative device ratings used in line-frequency AC/DC conversion. For example, the table includes device **5STP 07D1800** with $V_{DRM} = 1800 \text{ V}$, $I_{TAV} = 760 \text{ A}$, and $I_{TSM} = 9.0 \text{ kA}$, and higher-power parts such as **5STP 45Q2800** with $V_{DRM} = 2800 \text{ V}$ and $I_{TAV} = 5710 \text{ A}$ [Hitachi Energy, *Phase controlled thyristors (PCT)*].

The point of this exercise is not to memorize those numbers. It is to learn what such a rating table is telling you about a three-phase controlled rectifier.

Table 11.3: Reading an official phase-control thyristor rating table

| Datasheet or catalog field | What it means in plain language | Why it matters in a three-phase rectifier |
| --- | --- | --- |
| $V_{DRM}$ | Repetitive peak forward blocking voltage | Each SCR must safely block the off-state voltage, including margin for transients and commutation effects |
| $I_{TAV}$ | Average on-state current under stated thermal conditions | Helps judge current-carrying ability and cooling requirement of each valve position |
| $I_{TSM}$ | Non-repetitive surge current capability | Important for fault survival and coordination with fuses and protection |
| Press-pack construction | Device is clamped between cooling/electrical contact surfaces | Common in very high-power rectifiers and HVDC valves because thermal and mechanical performance matter greatly |

Now connect this to the chapter.

For a 415 V line-to-line RMS supply, the peak line-to-line voltage is about

$$V_{LL,peak} \approx 587 \text{ V}.$$

So if you see a thyristor with $V_{DRM} = 1800 \text{ V}$, you should immediately think: this device can block far more than the ideal line peak of a 415 V system. That does **not** automatically mean it is the correct device, because real selection also depends on transients, safety margin, thermal design, fault duty, commutation overlap, snubbers, isolation requirements, and mechanical packaging. But it does tell you that the blocking-voltage capability is in a suitable order of magnitude for serious line-frequency power conversion [Hitachi Energy, *Phase controlled thyristors (PCT)*].

Likewise, if you see $I_{TAV}$ values in the hundreds or thousands of amperes, you are looking at devices intended for much larger systems than a small laboratory charger. That is your clue that three-phase controlled rectifiers scale all the way from teaching rigs to very high-power converter valves.

This reading exercise also prepares you for the application note on HVDC. Hitachi Energy states that converter stations perform AC/DC conversion using high-power, high-voltage semiconductor valves, and that classical HVDC and HVDC Light use different semiconductor technologies [Hitachi Energy, *HVDC converter stations*]. In other words, the humble three-phase rectifier chapter connects directly to grid-scale conversion hardware.

## How this matters in renewable-energy systems

Three-phase controlled rectifiers appear in renewable-energy study in two main ways.

First, they are part of the classical route from AC generation to a DC link. In older or more classical wind-energy conversion schemes, generator output or grid-side three-phase AC can be rectified to DC and then processed further. The specific industrial implementation may use a diode bridge, an SCR bridge, or a PWM active rectifier depending on the need for controllability, power factor, harmonics, and bidirectional operation. But the idea of forming a DC link from a three-phase source is fundamental across all of them [NPTEL, *Line Commutated and PWM Rectifiers*].

Second, the same line-commutated conversion ideas scale to bulk-power transmission. Hitachi Energy notes that HVDC converter stations convert AC to DC and back using high-power semiconductor valves [Hitachi Energy, *HVDC converter stations*]. Classical **line-commutated converter HVDC** is built from thyristor valve groups whose elementary behavior is rooted in the same controlled-rectifier principles studied in this chapter. This is highly relevant to renewable energy because large wind, hydro, and solar resources are often remote from major load centers.

At the same time, modern converter practice has moved forward. NPTEL's recent course description on line-commutated and PWM rectifiers notes that diode- and thyristor-based rectifier technology is mature, but newer applications such as EV charging and modern battery charging increasingly shift toward PWM converters for improved size and efficiency [NPTEL, *Line Commutated and PWM Rectifiers*]. So this chapter should be understood both as a practical converter topic and as a foundation for understanding why newer rectifier technologies were developed.

## Chapter summary

- A three-phase source provides more frequent useful voltage segments than a single-phase source, so rectification becomes smoother and more suitable for higher power.
- For a balanced three-phase system, $V_{ph,rms} = V_{LL,rms}/\sqrt{3}$ and $V_m = \sqrt{2}V_{ph,rms}$.
- The three-phase half-wave controlled rectifier uses three SCRs and a neutral return. With continuous current, its ideal average output is $V_{o,avg} = \dfrac{3\sqrt{3}}{2\pi}V_m\cos\alpha = 0.675\,V_{LL,rms}\cos\alpha$.
- The three-phase fully controlled bridge uses six SCRs. One upper and one lower SCR conduct at a time, and the conducting pair changes every $60^\circ$.
- In the full bridge, each SCR conducts for $120^\circ$ under continuous-current conditions.
- The output of the full bridge is built from line-to-line voltage segments, not phase voltages.
- The ripple frequency is $3f$ for the three-phase half-wave rectifier and $6f$ for the full bridge.
- For the ideal three-phase fully controlled bridge with continuous current, the most important result is

$$\boxed{V_{o,avg} = \frac{3\sqrt{3}}{\pi}V_m\cos\alpha = \frac{3\sqrt{2}}{\pi}V_{LL,rms}\cos\alpha \approx 1.35\,V_{LL,rms}\cos\alpha} \quad \text{(11.11 revisited)}$$

- Increasing firing angle $\alpha$ reduces average DC output. At $\alpha = 90^\circ$, the ideal average output is zero.
- Negative average output for $\alpha > 90^\circ$ is meaningful only when the DC side can sustain current, as in inversion-capable systems.
- Real converters deviate from the ideal formula because of source inductance, overlap, device drops, and non-ideal current ripple.
- Phase-controlled thyristor rating tables should be read in terms of blocking voltage, average current, surge current, thermal conditions, and package style, not just part number.
- The chapter connects directly to classical wind-energy front ends, large DC supplies, controlled charging, and line-commutated HVDC.

## Further reading

- M. H. Rashid, *Power Electronics: Circuits, Devices and Applications*, 4th ed. This is a strong textbook source for the waveforms, average-value derivations, and operating regions of three-phase controlled rectifiers.
- Ned Mohan, Tore M. Undeland, and William P. Robbins, *Power Electronics: Converters, Applications and Design*, 3rd ed. This text is especially helpful for understanding continuous conduction, source-current behavior, and the practical interpretation of firing angle.
- [IIT Bombay SequelApp, *Three-Phase Full Wave Controlled Rectifier - 2*](https://www.ee.iitb.ac.in/~sequel/sequelapp/PE_rectifier_7.pdf) - A concise worked example for the six-pulse bridge, including the standard average-voltage expression and a load-side interpretation.
- [Hitachi Energy, *Phase controlled thyristors (PCT)*](https://www.hitachienergy.com/us/en/products-and-solutions/semiconductors/thyristors/phase-controlled-thyristors-pct) - Useful for learning how real line-frequency thyristor ratings are presented and how device voltage and current classes scale toward very high-power rectifier applications.
- [NPTEL, *Line Commutated and PWM Rectifiers*](https://onlinecourses.nptel.ac.in/noc25_ee151/preview) - Useful for seeing how classical thyristor rectifiers fit into the broader transition toward modern PWM rectifiers in EV, battery, and grid-connected applications.
