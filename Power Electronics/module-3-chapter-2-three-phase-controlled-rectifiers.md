# Chapter 3.2: Three-phase Controlled Rectifiers

## Chapter opening

Three-phase controlled rectifiers extend the phase-control ideas introduced with single-phase converters to the higher-power conditions found in industrial power systems. A three-phase source provides more frequent useful voltage segments, so the DC output is smoother, the ripple frequency is higher, and source utilization is better than in comparable single-phase circuits [Rashid, *Power Electronics: Circuits, Devices and Applications*, 4e, Ch. 6], [Mohan, Undeland, Robbins, *Power Electronics: Converters, Applications and Design*, 3e, Ch. 6].

This chapter begins with the **three-phase half-wave controlled rectifier** as an introductory topology and then develops the more important **three-phase fully controlled bridge rectifier**, also called the **three-phase full converter** or **six-pulse thyristor bridge**. The main objectives are to identify the conduction sequence, interpret the principal waveforms, derive the average output-voltage expression under continuous-current conditions, and examine the effect of the firing angle $\alpha$ on the DC output.

## Prerequisites check

- You should be comfortable with SCR behavior from Chapter 1.2, especially gate triggering, latching, and natural line commutation.
- You should remember from Chapter 3.1 that the **firing angle** $\alpha$ is measured from the natural turn-ON point of the relevant supply voltage.
- You should know the difference between an **R load** and an **R-L load**, and why an inductor tends to keep current continuous.
- You should be able to move between phase and line quantities in a balanced three-phase system.
- You should remember that a 415 V, 50 Hz three-phase supply usually means **415 V line-to-line RMS**, not phase RMS.

The discussion below assumes those relationships will be used without repeated review.

### 3.2.1 Three-phase half-wave controlled rectifier (overview)

#### Balanced three-phase supply and basic idea

In a three-phase source, the three phase voltages are displaced by $120^\circ$. For a balanced system,

$$v_{an} = V_m\sin\omega t$$

$$v_{bn} = V_m\sin\left(\omega t - \frac{2\pi}{3}\right)$$

$$v_{cn} = V_m\sin\left(\omega t - \frac{4\pi}{3}\right)$$

where $V_m$ is the peak phase voltage and $\omega = 2\pi f$ is the angular frequency.

For a balanced three-phase system,

$$\boxed{V_{ph,rms} = \frac{V_{LL,rms}}{\sqrt{3}}} \quad \text{(11.1)}$$

and

$$\boxed{V_m = \sqrt{2}\,V_{ph,rms}} \quad \text{(11.2)}$$

where $V_{ph,rms}$ is the phase RMS voltage and $V_{LL,rms}$ is the line-to-line RMS voltage.

For a 415 V, 50 Hz supply,

$$V_{ph,rms} = \frac{415}{\sqrt{3}} \approx 239.6 \text{ V}$$

and

$$V_m = \sqrt{2}\times 239.6 \approx 339 \text{ V}.$$

The **three-phase half-wave controlled rectifier** uses three SCRs, one connected to each phase, with the load returned through the neutral. Only one SCR conducts at a time. The conducting SCR must be both forward biased and triggered, so the output is formed from successive positive portions of the phase voltages.

**Image prompt for Figure 11.1:** Create a clean textbook-style technical illustration of a three-phase half-wave controlled rectifier using three SCRs connected from phase lines a, b, and c to a common positive load terminal, with the load returning to the neutral n. Show balanced phase voltages $v_{an}$, $v_{bn}$, and $v_{cn}$ displaced by $120^\circ$, and a lower waveform plot of output voltage $v_o$ showing successive positive segments from the three phases. Mark the firing angle $\alpha$, the conduction interval of one SCR, and the 120-degree phase displacement. Use monochrome engineering style with axes, labels, and units.

If the load current is sufficiently smooth, each SCR conducts for about $120^\circ$ electrical. The output therefore contains three pulses per AC cycle, and the ripple frequency is

$$\boxed{f_{ripple} = 3f} \quad \text{(11.3)}$$

so a 50 Hz supply produces a ripple frequency of

$$f_{ripple} = 3\times 50 = 150 \text{ Hz}.$$

#### Average output voltage and limitations

Under the usual ideal assumptions of continuous current and negligible device drops, the average output voltage is

$$\boxed{V_{o,avg} = \frac{3\sqrt{3}}{2\pi}V_m\cos\alpha} \quad \text{(11.4)}$$

or, in RMS form,

$$\boxed{V_{o,avg} = 1.17\,V_{ph,rms}\cos\alpha = 0.675\,V_{LL,rms}\cos\alpha} \quad \text{(11.5)}$$

[Rashid, *Power Electronics: Circuits, Devices and Applications*, 4e, Ch. 6], [Mohan, Undeland, Robbins, *Power Electronics: Converters, Applications and Design*, 3e, Ch. 6].

For a 415 V supply and $\alpha = 30^\circ$,

$$V_{o,avg} = 0.675\times 415\times \cos 30^\circ$$

$$= 0.675\times 415\times 0.866 \approx 242.6 \text{ V}.$$

This circuit is mainly useful as an introductory topology. It requires a neutral return, its output is built from phase voltages rather than the larger line voltages, and its source utilization is poorer than that of the six-pulse bridge. It also illustrates an important operating point: a gate pulse alone does not determine conduction. The SCR must also be forward biased by the instantaneous phase voltages.

### 3.2.2 Three-phase fully controlled bridge rectifier with R-L load; continuous conduction

#### Circuit structure and continuous conduction

The **three-phase fully controlled bridge rectifier** uses six SCRs arranged in a bridge. Three devices form the upper group and connect the positive DC terminal to phases $a$, $b$, and $c$. Three devices form the lower group and connect the negative DC terminal to the same three phases. At any instant, one upper SCR and one lower SCR conduct, so the load is connected across a line-to-line voltage rather than a phase-to-neutral voltage [Rashid, *Power Electronics: Circuits, Devices and Applications*, 4e, Ch. 6].

This arrangement increases the available output voltage, eliminates the neutral connection, and produces six output pulses per cycle. The ripple frequency is therefore

$$\boxed{f_{ripple} = 6f = 300 \text{ Hz}} \quad \text{(11.6)}$$

for a 50 Hz supply.

The important operating case is an **R-L load with continuous conduction**. Continuous conduction means that the load current does not fall to zero between successive conduction intervals. The DC-side voltage equation is

$$\boxed{v_o = Ri_d + L\frac{di_d}{dt} + E} \quad \text{(11.7)}$$

where $v_o$ is the instantaneous converter output voltage, $R$ is the effective DC-side resistance, $L$ is the smoothing inductance, $i_d$ is the load current, and $E$ represents any opposing DC-side source such as motor back EMF. When $L$ is sufficiently large, the ripple in $i_d$ is small and the current may be treated as nearly constant over one ripple period.

#### Conduction sequence and output waveform

Let the upper devices be labeled $T_{a+}$, $T_{b+}$, and $T_{c+}$, and the lower devices $T_{a-}$, $T_{b-}$, and $T_{c-}$.

Under continuous-current conditions:

- one upper SCR conducts for $120^\circ$,
- one lower SCR conducts for $120^\circ$,
- the conducting pair changes every $60^\circ$,
- the DC load current continues without interruption.

The pair sequence over one cycle is

- $(T_{a+}, T_{b-})$
- $(T_{a+}, T_{c-})$
- $(T_{b+}, T_{c-})$
- $(T_{b+}, T_{a-})$
- $(T_{c+}, T_{a-})$
- $(T_{c+}, T_{b-})$

and then repeats. Each pair applies one line-to-line voltage to the load. For example, $(T_{a+}, T_{b-})$ applies $v_{ab}$ and $(T_{a+}, T_{c-})$ applies $v_{ac}$.

**Image prompt for Figure 11.2:** Create a clean textbook-style technical illustration of a three-phase fully controlled bridge rectifier with six SCRs, labeled $T_{a+}$, $T_{b+}$, $T_{c+}$ in the upper group and $T_{a-}$, $T_{b-}$, $T_{c-}$ in the lower group, feeding an R-L load with nearly constant current. Beside the circuit, show aligned waveforms of three phase voltages, gate pulses displaced by 60 degrees, output voltage made of successive line-to-line segments, and load current that is almost constant. Clearly mark that each SCR conducts for 120 degrees and each conducting pair lasts for 60 degrees. Use monochrome engineering style.

The output voltage is therefore a stepped waveform composed of successive line-to-line sinusoidal segments. Because six segments occur in each cycle, the ripple frequency is higher than in the half-wave circuit, and a smaller inductance is required for the same current ripple.

For a 415 V line-to-line RMS supply, the peak line-to-line voltage is

$$\boxed{V_{LL,peak} = \sqrt{2}\,V_{LL,rms}} \quad \text{(11.8)}$$

so

$$V_{LL,peak} = \sqrt{2}\times 415 \approx 587 \text{ V}.$$

This is the peak available line voltage, not the average DC output. The average output depends on the firing angle $\alpha$, which determines the portion of each line-voltage segment applied to the load.

Real supplies and transformers also have inductance. Commutation therefore requires a finite interval, and current transfers gradually from one SCR to the next. This **commutation overlap** reduces the average DC output below the ideal value and introduces notches in the source voltage. The ideal analysis below neglects overlap and device voltage drops.

### 3.2.3 Average output voltage expression; effect of firing angle on DC output

#### Derivation of the average output voltage

Under ideal conditions:

- the source is balanced,
- device drops are neglected,
- commutation overlap is neglected,
- load current is continuous.

During any one $60^\circ$ conduction interval, the load is connected to one line-to-line voltage. Suppose the active segment is

$$v_{ab} = \sqrt{3}\,V_m\sin\left(\omega t + \frac{\pi}{6}\right)$$

where $V_m$ is the peak phase voltage [Rashid, *Power Electronics: Circuits, Devices and Applications*, 4e, Ch. 6].

Because the same waveform shape appears six times in each cycle,

$$V_{o,avg} = \frac{6}{2\pi}\int_{\pi/6+\alpha}^{\pi/2+\alpha}\sqrt{3}\,V_m\sin\left(\theta + \frac{\pi}{6}\right)d\theta$$

where $\theta = \omega t$.

Therefore,

$$V_{o,avg} = \frac{3\sqrt{3}V_m}{\pi}\int_{\pi/6+\alpha}^{\pi/2+\alpha}\sin\left(\theta + \frac{\pi}{6}\right)d\theta.$$

Let

$$x = \theta + \frac{\pi}{6}.$$

Then the limits become $x = \pi/3+\alpha$ to $x = 2\pi/3+\alpha$, and

$$V_{o,avg} = \frac{3\sqrt{3}V_m}{\pi}\int_{\pi/3+\alpha}^{2\pi/3+\alpha}\sin x\,dx.$$

Carrying out the integration,

$$V_{o,avg} = \frac{3\sqrt{3}V_m}{\pi}\left[-\cos x\right]_{\pi/3+\alpha}^{2\pi/3+\alpha}.$$

Hence,

$$V_{o,avg} = \frac{3\sqrt{3}V_m}{\pi}\left[\cos\left(\frac{\pi}{3}+\alpha\right)-\cos\left(\frac{2\pi}{3}+\alpha\right)\right].$$

The bracketed term reduces to $\cos\alpha$, giving

$$\boxed{V_{o,avg} = \frac{3\sqrt{3}}{\pi}V_m\cos\alpha} \quad \text{(11.9)}$$

Using

$$V_m = \sqrt{2}\,V_{ph,rms} = \sqrt{\frac{2}{3}}\,V_{LL,rms},$$

Equation (11.9) becomes

$$\boxed{V_{o,avg} = \frac{3\sqrt{2}}{\pi}V_{LL,rms}\cos\alpha} \quad \text{(11.10)}$$

or numerically,

$$\boxed{V_{o,avg} \approx 1.35\,V_{LL,rms}\cos\alpha} \quad \text{(11.11)}$$

[Rashid, *Power Electronics: Circuits, Devices and Applications*, 4e, Ch. 6], [Mohan, Undeland, Robbins, *Power Electronics: Converters, Applications and Design*, 3e, Ch. 6].

#### Interpretation, examples, and load-side relation

Equation (11.11) shows that the average DC output is governed by $\cos\alpha$:

- at $\alpha = 0^\circ$, the output is maximum and positive,
- at $\alpha = 90^\circ$, the ideal average output is zero,
- for $\alpha > 90^\circ$, the ideal average output becomes negative.

A negative average output does not by itself imply inversion with an ordinary passive load. Inversion requires a DC-side source capable of sustaining current, such as a motor back EMF or another active DC system.

**Image prompt for Figure 11.3:** Create a clean textbook-style technical figure showing the ideal average DC output of a three-phase fully controlled bridge rectifier as firing angle changes. Include one plot of output-voltage waveform segments for $\alpha = 30^\circ$, one for $\alpha = 75^\circ$, and one for $\alpha = 105^\circ$, each with the average-value line marked. Add a second plot below of normalized average voltage $V_{o,avg}/V_{o,max}$ versus firing angle $\alpha$ from $0^\circ$ to $180^\circ$, showing the cosine trend, zero crossing at $90^\circ$, and negative region beyond $90^\circ$. Use monochrome textbook engineering style with axes, labels, and units.

For a 415 V line-to-line RMS supply,

$$V_{o,avg} \approx 1.35\times 415\times \cos\alpha.$$

Since $1.35\times 415 \approx 560.25$,

$$V_{o,avg} \approx 560.25\cos\alpha.$$

Table 11.1 gives the ideal average output for several firing angles.

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

If the required average output is 350 V, then

$$350 = 1.35\times 415 \times \cos\alpha,$$

so

$$\cos\alpha = \frac{350}{560.25} \approx 0.625$$

and

$$\alpha = \cos^{-1}(0.625) \approx 51.3^\circ.$$

The converter voltage must also satisfy the load-side average relation. Since the average inductor voltage over one period is zero in steady operation,

$$\boxed{V_{o,avg} = E + I_dR} \quad \text{(11.12)}$$

where $I_d$ is the average load current.

Suppose

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

Increasing $\alpha$ also affects the AC side. It reduces the average DC output, shifts the fundamental component of source current further behind the supply voltage, and worsens the input power factor because both displacement and distortion are involved.

#### Comparison of half-wave and full-wave circuits

Table 11.2 summarizes the main differences between the two introductory three-phase controlled rectifiers.

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

## How this matters in renewable-energy systems

Three-phase rectifiers matter in renewable-energy study because they establish the link between three-phase AC systems and DC links. In classical wind-energy conversion, large DC drives, controlled charging systems, and line-commutated HVDC, the rectifier stage converts AC power to a controllable DC quantity that can then be transmitted, stored, or processed further.

The same chapter also provides historical and technical context for modern converter practice. Many present-day grid, storage, and charging systems use PWM rectifiers rather than line-commutated SCR bridges, but the underlying questions remain the same: how the AC side is connected to the DC side, how current is controlled, how the firing or switching pattern affects average output, and how converter action influences power quality.

## Chapter summary

- A balanced three-phase source provides more frequent useful voltage segments than a single-phase source, so rectification is smoother and better suited to higher power.
- The three-phase half-wave controlled rectifier uses three SCRs and a neutral return. Under continuous-current conditions, its ideal average output is $V_{o,avg} = \dfrac{3\sqrt{3}}{2\pi}V_m\cos\alpha = 0.675\,V_{LL,rms}\cos\alpha$.
- The three-phase fully controlled bridge uses six SCRs. One upper and one lower device conduct at a time, each device conducts for $120^\circ$, and the conducting pair changes every $60^\circ$.
- For the ideal full converter with continuous current, the central result is

$$\boxed{V_{o,avg} = \frac{3\sqrt{3}}{\pi}V_m\cos\alpha = \frac{3\sqrt{2}}{\pi}V_{LL,rms}\cos\alpha \approx 1.35\,V_{LL,rms}\cos\alpha} \quad \text{(11.11 revisited)}$$

- Increasing $\alpha$ reduces the average DC output and also worsens the AC-side power-factor conditions.
- Real converters deviate from the ideal result because of source inductance, commutation overlap, device drops, and current ripple.

## Further reading

- M. H. Rashid, *Power Electronics: Circuits, Devices and Applications*, 4th ed. This is a strong textbook source for the waveforms, average-value derivations, and operating regions of three-phase controlled rectifiers.
- Ned Mohan, Tore M. Undeland, and William P. Robbins, *Power Electronics: Converters, Applications and Design*, 3rd ed. This text is especially helpful for understanding continuous conduction, source-current behavior, and the practical interpretation of firing angle.
- [IIT Bombay SequelApp, *Three-Phase Full Wave Controlled Rectifier - 2*](https://www.ee.iitb.ac.in/~sequel/sequelapp/PE_rectifier_7.pdf) - A concise worked example for the six-pulse bridge, including the standard average-voltage expression and a load-side interpretation.
- [Hitachi Energy, *Phase controlled thyristors (PCT)*](https://www.hitachienergy.com/us/en/products-and-solutions/semiconductors/thyristors/phase-controlled-thyristors-pct) - Useful for learning how real line-frequency thyristor ratings are presented and how device voltage and current classes scale toward very high-power rectifier applications.
- [NPTEL, *Line Commutated and PWM Rectifiers*](https://onlinecourses.nptel.ac.in/noc25_ee151/preview) - Useful for seeing how classical thyristor rectifiers fit into the broader transition toward modern PWM rectifiers in EV, battery, and grid-connected applications.
