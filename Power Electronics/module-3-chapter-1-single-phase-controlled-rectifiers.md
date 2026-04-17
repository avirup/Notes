# Chapter 3.1: Single-phase Controlled Rectifiers

## Chapter opening

Until now, most of our attention has been on the switch itself and on the circuits that help it survive. We studied the SCR as a latching power device, then learned how to trigger it, protect it, and cool it. This chapter is where those ideas begin to act together as a converter. A **controlled rectifier** uses a controllable device, usually an SCR in this beginner context, to convert AC into DC while allowing us to decide when conduction begins in each cycle [Rashid, *Power Electronics: Circuits, Devices and Applications*, 4e, Ch. 6], [Mohan, Undeland, Robbins, *Power Electronics: Converters, Applications and Design*, 3e, Ch. 6].

That control matters because many practical loads do not want a fixed DC voltage. A battery charger may need adjustable charging current. A DC motor drive may need variable armature voltage. A front-end stage may need a controlled soft start. A renewable-energy interface may need controllable power conversion between an AC source and a DC link. The SCR makes this possible at line frequency by delaying the instant at which current is allowed to flow. Littelfuse's phase-control note uses the terms **delay angle** and **conduction angle** for this idea, and those two ideas are at the heart of this whole chapter [Littelfuse AN1003].

We will begin with the simplest topology, the single-phase half-wave controlled rectifier, first with a resistive load and then with an R-L load. That will let us see clearly what the firing angle does and why an inductor changes everything. After that we will move to the single-phase fully controlled bridge and then the semi-controlled bridge. Along the way we will derive the main average- and RMS-voltage expressions you will use repeatedly in later chapters. These circuits also prepare us for the next step in the module, where three-phase controlled rectifiers become the natural extension.

## Prerequisites check

- You should remember from Chapter 1.2 that an SCR can be triggered by a gate pulse but does not turn OFF by gate control in ordinary operation.
- You should be comfortable with sinusoidal AC voltage, including the relation between RMS value and peak value.
- You should know that a resistor makes current follow voltage, while an inductor resists sudden change of current.
- You should remember from Chapter 2.1 that firing pulses must be synchronized correctly with the AC waveform.
- You should remember from Chapter 2.2 that an inductive load often needs a freewheeling path when the main source is removed.

If the SCR latching idea feels uncertain, review Chapter 1.2 first. If the difference between average value and RMS value feels weak, it is worth refreshing that now because both quantities appear throughout this chapter.

## Core content

### 3.1.1 Single-phase half-wave controlled rectifier with R and R-L loads; effect of freewheeling diode

#### The basic idea of phase control

Let us begin with the simplest physical picture. Suppose an SCR is placed in series with a load and a single-phase AC source. During each positive half-cycle, the SCR is forward biased. But being forward biased is not enough. It still waits for a gate pulse. If we delay that gate pulse, we delay conduction. That is why these circuits are called **phase-controlled rectifiers**. We are choosing a point on the AC phase at which the device starts conducting [Littelfuse AN1003], [Rashid, *Power Electronics: Circuits, Devices and Applications*, 4e, Ch. 6].

We will describe the supply as

$$\boxed{V_m = \sqrt{2}\,V_{s,rms}} \quad \text{(10.1)}$$

where $V_{s,rms}$ is the RMS value of the sinusoidal source and $V_m$ is its peak value.

For a 230 V, 50 Hz single-phase supply,

$$V_m = \sqrt{2}\times 230 \approx 325 \text{ V}.$$

This number will keep returning, so it is worth holding in mind. A 230 V mains source does not peak at 230 V. It peaks at about 325 V.

The instant at which the SCR is fired is described by the **firing angle** $\alpha$, measured from the zero crossing of the positive half-cycle. If the SCR is triggered at $\omega t = \alpha$, it conducts only from that point onward, provided the load current stays above the holding current [Mohan, Undeland, Robbins, *Power Electronics: Converters, Applications and Design*, 3e, Ch. 6], [ST AN4607].

**Image prompt for Figure 10.1:** Create a clean textbook-style technical illustration of a single-phase half-wave controlled rectifier using one SCR and a load. Include three vertically aligned waveform plots versus electrical angle $\omega t$: source voltage $v_s$, gate pulse train showing a pulse at firing angle $\alpha$ in each positive half-cycle, and output voltage $v_o$ for a resistive load that is zero from $0$ to $\alpha$ and follows the positive sine wave from $\alpha$ to $\pi$. Clearly mark $0$, $\alpha$, $\pi$, and $2\pi$. Use monochrome engineering style with axes and units.

#### Half-wave controlled rectifier with R load

When the load is purely resistive, current and voltage are in phase. That makes the first analysis pleasantly simple. Once the SCR is triggered at angle $\alpha$, the output voltage equals the source voltage until the source crosses zero at $\omega t = \pi$. At that instant the current also falls to zero, so the SCR turns OFF naturally. This is **line commutation**, because the AC line itself forces the current to zero [Rashid, *Power Electronics: Circuits, Devices and Applications*, 4e, Ch. 6].

So for an R load:

- from $0$ to $\alpha$, the SCR blocks and $v_o = 0$,
- from $\alpha$ to $\pi$, the SCR conducts and $v_o = V_m\sin\omega t$,
- from $\pi$ to $2\pi$, the source is negative, the SCR is reverse biased, and $v_o = 0$.

The average output voltage over one full cycle is therefore

$$\boxed{V_{o,avg} = \frac{V_m}{2\pi}(1+\cos\alpha)} \quad \text{(10.2)}$$

This equation is one of the most important introductory results in controlled rectifiers [Rashid, *Power Electronics: Circuits, Devices and Applications*, 4e, Ch. 6], [Mohan, Undeland, Robbins, *Power Electronics: Converters, Applications and Design*, 3e, Ch. 6].

Let us work through a numerical example slowly.

Suppose the source is 230 V RMS, so $V_m \approx 325 \text{ V}$, and the firing angle is $\alpha = 60^\circ$.

Then $\cos 60^\circ = 0.5$, so

$$V_{o,avg} = \frac{325}{2\pi}(1+0.5) \approx 77.6 \text{ V}.$$

That one result already shows the purpose of phase control. We began with a sinusoid peaking at about 325 V, but by delaying the trigger to $60^\circ$, the average DC output becomes only about 77.6 V.

Notice something subtle here. The circuit does not reduce the peak of the source itself. The source still reaches 325 V. What changes is the portion of each half-cycle that we allow through to the load. This is an important beginner distinction.

#### Why an R-L load behaves differently

Now let us replace the purely resistive load with a series **R-L load**. This is a much more realistic situation. A smoothing reactor, motor armature, filter inductance, or transformer-related load rarely behaves like a pure resistor.

The inductor changes the story because current through an inductor cannot change abruptly. Even when the source voltage has fallen to zero, the inductor still carries stored energy and tries to keep the current flowing. During SCR conduction, the load current satisfies

$$\boxed{L\frac{di_o}{dt} + Ri_o = V_m\sin\omega t} \quad \text{(10.3)}$$

where $L$ is the inductance, $R$ is the resistance, and $i_o$ is the load current.

You do not need to solve Equation (10.3) fully right now to understand the main effect. The important physical point is this: current no longer stops exactly at $\omega t=\pi$. It continues for some time into the negative half-cycle. The SCR therefore conducts from $\alpha$ up to an **extinction angle** $\beta$, where $\beta$ is greater than $\pi$ [Rashid, *Power Electronics: Circuits, Devices and Applications*, 4e, Ch. 6].

This leads to two important consequences:

- the output voltage becomes negative during part of the negative half-cycle because the SCR is still conducting,
- the average output voltage becomes smaller than in the resistive-load case for the same firing angle.

If we neglect device drops, the average output voltage over one cycle is

$$\boxed{V_{o,avg} = \frac{V_m}{2\pi}(\cos\alpha - \cos\beta)} \quad \text{(10.4)}$$

where $\beta$ depends on $R$, $L$, the source frequency, and the firing angle [Mohan, Undeland, Robbins, *Power Electronics: Converters, Applications and Design*, 3e, Ch. 6].

This equation makes physical sense. If the current persists too long into the negative half-cycle, the negative part of the output voltage grows, and the average DC output drops.

A common misconception appears here. Beginners sometimes think that the inductor always helps because it "smooths" current. It does smooth current, but in this topology it also makes the SCR keep conducting after the source has turned negative. That can reduce average output voltage and can worsen the reactive character of the source current.

#### The effect of a freewheeling diode

This is why the **freewheeling diode** is so important with inductive loads. We place a diode across the R-L load so that when the source voltage tries to go negative, the load current has another path. Instead of forcing current through the source and SCR into the negative half-cycle, the current circulates through the load and diode. This is called **freewheeling** [Rashid, *Power Electronics: Circuits, Devices and Applications*, 4e, Ch. 6], [Mohan, Undeland, Robbins, *Power Electronics: Converters, Applications and Design*, 3e, Ch. 6].

The output-voltage picture now changes:

- from $0$ to $\alpha$, $v_o = 0$,
- from $\alpha$ to $\pi$, the SCR conducts and $v_o = V_m\sin\omega t$,
- from $\pi$ onward, the freewheeling diode conducts, current continues through the load, but the load voltage is approximately zero.

So the average output voltage becomes

$$\boxed{V_{o,avg} = \frac{V_m}{2\pi}(1+\cos\alpha)} \quad \text{(10.5)}$$

which is the same average-voltage expression as the half-wave resistive case, even though the current behavior is very different.

That result is worth pausing over. The diode does not increase the source voltage. What it does is prevent the negative portion of the output voltage that would otherwise appear while the inductor forces current to continue. In other words, the freewheeling diode protects the load from being driven negative after the source half-cycle has ended.

**Image prompt for Figure 10.2:** Create a clean textbook-style technical illustration comparing a single-phase half-wave controlled rectifier with an R-L load, first without and then with a freewheeling diode across the load. Show two output-voltage waveforms versus $\omega t$: in the first, the output follows the source from $\alpha$ to $\beta$ and becomes negative between $\pi$ and $\beta$; in the second, the output follows the source from $\alpha$ to $\pi$ and becomes approximately zero during the freewheeling interval. Also show corresponding load-current waveforms that continue after $\pi$. Label $\alpha$, $\pi$, $\beta$, and the freewheeling interval clearly. Use monochrome engineering style.

The freewheeling diode gives several practical benefits:

- it improves the average output voltage for an inductive load,
- it reduces negative load voltage,
- it reduces reactive power burden on the source,
- it usually smooths the load current further,
- it reduces the risk of undesirable operating stress in some practical circuits.

*Renewable-energy relevance.* An inductive current path is common in battery chargers, DC-link smoothing stages, and low-frequency power-conditioning circuits. The freewheeling idea also appears later in choppers and inverter legs. Once you understand why the inductor needs an alternate path here, many later converter waveforms become much easier to read.

### 3.1.2 Single-phase full-wave fully controlled bridge rectifier with R and R-L loads

#### Why we move beyond half-wave circuits

The half-wave controlled rectifier is an excellent teaching circuit, but it uses only one half of the AC supply effectively. In practice we usually want better utilization of the transformer or mains source, lower ripple frequency at the output, and greater control flexibility. That leads us to the **single-phase fully controlled bridge rectifier**, often simply called the **single-phase full converter** [Rashid, *Power Electronics: Circuits, Devices and Applications*, 4e, Ch. 6].

This bridge uses four SCRs. During one half-cycle, one diagonal pair conducts. During the next half-cycle, the other diagonal pair conducts. Because the bridge reverses the connection of the source to the load during alternate half-cycles, the load voltage can stay positive even though the source changes sign.

#### Fully controlled bridge with R load

Let the SCR pairs be $(T_1,T_2)$ and $(T_3,T_4)$. If the load is resistive, each pair conducts from the firing instant until the natural current zero of that half-cycle:

- $T_1$ and $T_2$ conduct from $\alpha$ to $\pi$,
- $T_3$ and $T_4$ conduct from $\pi+\alpha$ to $2\pi$.

The output therefore contains two positive pulses per source cycle. The average output voltage is

$$\boxed{V_{o,avg} = \frac{V_m}{\pi}(1+\cos\alpha)} \quad \text{(10.6)}$$

which is exactly twice the half-wave resistive-load result, as you would expect from using both half-cycles [Mohan, Undeland, Robbins, *Power Electronics: Converters, Applications and Design*, 3e, Ch. 6].

Let us test Equation (10.6) with the same 230 V supply and $\alpha = 60^\circ$:

$$V_{o,avg} = \frac{325}{\pi}(1+0.5) \approx 155.2 \text{ V}.$$

Compare that with the half-wave result of about 77.6 V. The full bridge uses both half-cycles, so the average DC output doubles.

#### Fully controlled bridge with R-L load and continuous current

Now we come to one of the central circuits of classical power electronics: the single-phase full converter with an R-L load and sufficiently large inductance that the load current is nearly continuous.

The phrase **continuous current** means the load current never falls to zero within the cycle. That usually happens when the load inductance is large enough, sometimes together with a back-emf source such as a DC motor or battery. In this case, each SCR pair conducts for $180^\circ$ electrical, and commutation from one pair to the next happens when the next pair is fired [Rashid, *Power Electronics: Circuits, Devices and Applications*, 4e, Ch. 6].

The average output voltage then becomes

$$\boxed{V_{o,avg} = \frac{2V_m}{\pi}\cos\alpha} \quad \text{(10.7)}$$

This is a famous result, and it deserves careful interpretation.

If $\alpha = 0^\circ$, then

$$V_{o,avg} = \frac{2V_m}{\pi},$$

which is the same average as an uncontrolled full-wave diode bridge.

If $\alpha = 90^\circ$, then $\cos\alpha = 0$, so the average output voltage is zero.

If $\alpha > 90^\circ$, then $\cos\alpha$ becomes negative, and the average output voltage becomes negative.

That last statement often surprises beginners. How can a rectifier produce a negative average output voltage? The answer is that with a continuous-current DC side containing stored energy or an active DC source, the bridge can move from rectifier behavior toward **line-commutated inverter** behavior. We are not going deeply into inverter operation in this chapter, but it is important to notice that the full converter is inherently more capable than the half-wave circuit or the semi-converter [Mohan, Undeland, Robbins, *Power Electronics: Converters, Applications and Design*, 3e, Ch. 6].

Let us do a quick numerical comparison for a 230 V source:

- at $\alpha = 30^\circ$, $V_{o,avg} \approx \dfrac{2\times 325}{\pi}\times 0.866 \approx 179.3 \text{ V}$,
- at $\alpha = 75^\circ$, $V_{o,avg} \approx \dfrac{2\times 325}{\pi}\times 0.259 \approx 53.5 \text{ V}$,
- at $\alpha = 105^\circ$, $V_{o,avg} \approx \dfrac{2\times 325}{\pi}\times (-0.259) \approx -53.5 \text{ V}$.

So by moving the firing angle across $90^\circ$, the converter moves across the zero-average boundary.

**Image prompt for Figure 10.3:** Create a clean textbook-style technical illustration of a single-phase fully controlled bridge rectifier using four SCRs. Include two waveform sets. In the first set, show the R-load case with gate pulses for the two SCR pairs and output voltage pulses from $\alpha$ to $\pi$ and from $\pi+\alpha$ to $2\pi$. In the second set, show the R-L continuous-current case with nearly constant positive load current and output voltage that alternates between positive and negative segments according to the firing angle. Clearly label SCR pairs, $\alpha$, $\pi$, and the conduction intervals. Use monochrome textbook engineering style.

Two common misconceptions should be corrected here.

The first is that a larger firing angle always means "less current everywhere." That is not generally true with inductive loads. The inductor stores energy, and current can stay continuous even when average output voltage is small.

The second is that the full converter is just the half-wave converter used twice. That is too simple. The full converter with continuous current can operate in both rectification and inversion regions, which the half-wave circuit cannot do in the same useful way.

*Renewable-energy relevance.* A full-controlled bridge is historically important because it introduces the idea of controlled AC-to-DC conversion with both half-cycles utilized and with the possibility of power-flow control. Those are stepping stones toward higher-power front ends and toward the HVDC and converter-control ideas that appear later in the book.

### 3.1.3 Single-phase semi-controlled (half-controlled) bridge rectifier - concept

#### Why a semi-controlled bridge exists

A **semi-controlled bridge rectifier**, also called a **half-controlled bridge** or **semi-converter**, uses two SCRs and two diodes. It sits between the diode bridge and the full SCR bridge:

- it is more controllable than a pure diode bridge,
- but simpler and cheaper to trigger than a fully controlled bridge.

This topology is especially useful when we need only one-way power flow from AC to DC. Many battery chargers and older DC-drive front ends fit that description [Rashid, *Power Electronics: Circuits, Devices and Applications*, 4e, Ch. 6], [Mohan, Undeland, Robbins, *Power Electronics: Converters, Applications and Design*, 3e, Ch. 6].

In one half-cycle, one SCR and one diode conduct. In the next half-cycle, the other SCR and the other diode conduct. With an inductive load, the diode arrangement naturally provides a freewheeling path. This is one of the most attractive practical features of the semi-converter.

#### Average output voltage of the semi-converter

For the standard inductive-load case with continuous current and ideal devices, the average output voltage is

$$\boxed{V_{o,avg} = \frac{V_m}{\pi}(1+\cos\alpha)} \quad \text{(10.8)}$$

This looks similar to Equation (10.6), and that is not an accident. The output contains two positive source-connected intervals per cycle, while the remaining interval is filled by freewheeling rather than by negative output voltage.

This one equation tells us two important things immediately.

First, $V_{o,avg}$ is always nonnegative for $0^\circ \le \alpha \le 180^\circ$ because $(1+\cos\alpha)$ never becomes negative.

Second, the semi-converter cannot produce negative average output voltage in normal operation. So it is a **one-quadrant converter** in the usual introductory sense.

That is the crucial contrast with the fully controlled bridge.

#### A battery-charger style example

Suppose an isolated secondary provides 18 V RMS to a single-phase semi-converter used in a small battery charger. Then

$$V_m = \sqrt{2}\times 18 \approx 25.5 \text{ V}.$$

If the firing angle is $\alpha = 60^\circ$,

$$V_{o,avg} = \frac{25.5}{\pi}(1+0.5) \approx 12.2 \text{ V}.$$

This simple arithmetic explains why the semi-converter became popular in variable DC-supply and charger applications. By changing $\alpha$, we change the average DC output without needing four controlled devices.

#### Why the semi-converter is gentler on the load

Because freewheeling occurs naturally in the semi-converter, the load voltage does not become negative in the way it can for the full-controlled bridge under continuous-current conditions. That makes the current smoother and the operating behavior friendlier for many one-directional loads. The price is reduced control authority: we lose the ability to produce negative average output voltage.

Table 10.1 compares the three main single-phase topologies we have met so far.

Table 10.1: Comparing single-phase controlled-rectifier topologies

| Topology | Controlled devices used | Uses both half-cycles? | Natural freewheeling path with inductive load? | Can average output become negative? | Typical beginner application picture |
|---|---|---|---|---|---|
| Half-wave controlled rectifier | 1 SCR | No | No, unless a freewheeling diode is added | No practical inversion mode | Simple teaching circuit, low-cost power control |
| Fully controlled bridge | 4 SCRs | Yes | No inherent freewheeling path | Yes, when current is continuous and $\alpha > 90^\circ$ | Controlled DC supplies, classical drives, line-commutated converters |
| Semi-controlled bridge | 2 SCRs + 2 diodes | Yes | Yes | No | Battery chargers, one-way variable DC front ends |

**Image prompt for Figure 10.4:** Create a clean textbook-style technical illustration of a single-phase semi-controlled bridge rectifier with two SCRs and two diodes feeding an R-L load. Show gate pulses only for the SCRs. Include output-voltage and load-current waveforms for continuous-current operation. Mark source-connected intervals where output follows the rectified sine wave, and freewheeling intervals where load voltage is approximately zero while current continues. Use monochrome engineering style with clear device labels and conduction intervals.

One misconception is especially common here. Because the semi-converter uses only two SCRs, beginners sometimes assume it is simply an economical version of the full converter with all the same capabilities. It is not. The loss of negative average-output capability is not a small detail. It fundamentally changes the type of power-flow control the circuit can provide.

*Renewable-energy relevance.* The semi-converter is a useful mental bridge toward controlled charger front ends. In renewable and storage systems, many practical interfaces only need power flow from AC to a DC battery or DC link, not back from the battery into the AC source. The semi-controlled bridge captures that one-directional logic very clearly.

### 3.1.4 Expressions for average and RMS output voltage; effect of firing angle

#### Why we care about both average and RMS values

At this point we should pause and organize the mathematics.

The **average output voltage** tells us the DC-producing ability of the rectifier. If the output feeds a battery, a smoothing inductor, or the armature of a DC machine, the average value is usually the first number we care about.

The **RMS output voltage** tells us about heating and effective power delivery to resistive parts of the load. A circuit can have the same average value as another circuit and still have a very different RMS value. That is why both must be treated seriously [Littelfuse AN1003], [Mohan, Undeland, Robbins, *Power Electronics: Converters, Applications and Design*, 3e, Ch. 6].

#### RMS output voltage for half-wave controlled rectifier with R load

For the half-wave controlled rectifier with a resistive load,

$$V_{o,rms} = \sqrt{\frac{1}{2\pi}\int_{\alpha}^{\pi} V_m^2\sin^2\theta\,d\theta}.$$

Carrying out the integration gives

$$\boxed{V_{o,rms} = \frac{V_m}{2}\sqrt{1-\frac{\alpha}{\pi}+\frac{\sin 2\alpha}{2\pi}}} \quad \text{(10.9)}$$

This equation passes two useful checks.

If $\alpha = 0^\circ$, then $V_{o,rms} = V_m/2$, which is the known RMS value of an uncontrolled half-wave rectified sine wave.

If $\alpha$ increases toward $180^\circ$, the term inside the square root approaches zero, so the RMS value collapses toward zero, which also makes physical sense.

For our earlier 230 V example with $\alpha = 60^\circ$,

$$V_{o,rms} = \frac{325}{2}\sqrt{1-\frac{60^\circ}{180^\circ}+\frac{\sin 120^\circ}{2\pi}} \approx 145.8 \text{ V}.$$

So in that case the average output is about 77.6 V, but the RMS output is much larger, about 145.8 V. This is exactly why average and RMS must not be confused.

#### RMS output voltage for full-wave R-load and semi-converter waveforms

For the single-phase fully controlled bridge with an R load, or for the semi-converter output-voltage waveform during source-connected intervals with ideal freewheeling, the RMS output becomes

$$\boxed{V_{o,rms} = \frac{V_m}{\sqrt{2}}\sqrt{1-\frac{\alpha}{\pi}+\frac{\sin 2\alpha}{2\pi}}} \quad \text{(10.10)}$$

This expression is larger than the half-wave RMS value because both half-cycles contribute.

Again, the limiting cases help us trust the result:

- at $\alpha = 0^\circ$, $V_{o,rms} = V_m/\sqrt{2} = V_{s,rms}$,
- at $\alpha \to 180^\circ$, $V_{o,rms}\to 0$.

#### RMS output voltage for full-controlled bridge with continuous current

For the ideal single-phase fully controlled bridge with continuous current and negligible overlap, the output voltage at every instant is either $+v_s$ or $-v_s$. When we square it for RMS calculation, the sign disappears. So the RMS output voltage equals the source RMS voltage:

$$\boxed{V_{o,rms} = V_{s,rms}} \quad \text{(10.11)}$$

This result often surprises learners because the average output varies strongly with $\alpha$, yet the RMS output voltage stays fixed in the ideal continuous-current case.

That is not a contradiction. It simply tells us that the waveform shape is changing sign and timing, not reducing its squared magnitude over the cycle.

#### What the firing angle really changes

The firing angle $\alpha$ changes several things at once.

First, it reduces the average DC output.

Second, it usually reduces the RMS output for pulsed-output cases such as the half-wave resistive circuit and the full-wave resistive circuit.

Third, it changes the source-current timing. As $\alpha$ becomes larger, the current is drawn later in the sinusoidal cycle. This generally worsens power factor and increases waveform distortion compared with an uncontrolled rectifier [Rashid, *Power Electronics: Circuits, Devices and Applications*, 4e, Ch. 6], [Mohan, Undeland, Robbins, *Power Electronics: Converters, Applications and Design*, 3e, Ch. 6].

Fourth, with inductive loads it changes whether current is discontinuous, continuous, or close to the boundary between them.

Table 10.2 collects the most useful beginner-level expressions from this chapter.

Table 10.2: Summary of important average and RMS expressions

| Circuit and load condition | Average output voltage | RMS output voltage | Main note |
|---|---|---|---|
| Half-wave controlled rectifier, R load | $\dfrac{V_m}{2\pi}(1+\cos\alpha)$ | $\dfrac{V_m}{2}\sqrt{1-\dfrac{\alpha}{\pi}+\dfrac{\sin 2\alpha}{2\pi}}$ | Conduction from $\alpha$ to $\pi$ |
| Half-wave controlled rectifier, R-L load without freewheeling diode | $\dfrac{V_m}{2\pi}(\cos\alpha-\cos\beta)$ | Depends on $\beta$ and exact current continuity | Negative output interval can appear |
| Half-wave controlled rectifier, R-L load with freewheeling diode | $\dfrac{V_m}{2\pi}(1+\cos\alpha)$ | Depends on current waveform | Freewheeling prevents negative output voltage |
| Fully controlled bridge, R load | $\dfrac{V_m}{\pi}(1+\cos\alpha)$ | $\dfrac{V_m}{\sqrt{2}}\sqrt{1-\dfrac{\alpha}{\pi}+\dfrac{\sin 2\alpha}{2\pi}}$ | Two positive pulses per cycle |
| Fully controlled bridge, R-L load, continuous current | $\dfrac{2V_m}{\pi}\cos\alpha$ | $V_{s,rms}$ | Average becomes negative for $\alpha>90^\circ$ |
| Semi-controlled bridge, continuous current | $\dfrac{V_m}{\pi}(1+\cos\alpha)$ | Same waveform trend as full-wave pulsed case when freewheeling intervals are ideal | One-quadrant operation |

One last misconception is worth naming explicitly. The firing angle does not directly "set the output to a chosen DC value" in a precise regulator sense. It sets the conduction timing. The resulting average DC value then depends on source voltage, load type, continuity of current, and whether freewheeling occurs. Good power-electronics thinking always keeps the load in the picture.

## Worked interpretation exercise

The [ST TYN612 product page](https://www.st.com/en/thyristors-scr-and-ac-switches/tyn612.html) is a useful real artifact for learning how to read an SCR choice for a beginner-level controlled-rectifier circuit.

ST describes the TYN612 family as a **12 A standard SCR** series and lists three especially relevant ratings on the product page: **on-state RMS current $I_{T(RMS)} = 12 \text{ A}$**, **repetitive peak off-state voltage $V_{DRM}$ and $V_{RRM}$ of 600 V, 800 V and 1000 V**, and **triggering gate current $I_{GT}$ of 5 mA or 15 mA** [ST TYN612 Product Page].

Let us read these numbers as a power-electronics learner rather than only as a component shopper.

The **600 V, 800 V, and 1000 V blocking classes** tell us first that this device family is meant to block line-related voltages, not only low-voltage DC. For a 230 V RMS single-phase source, the sine-wave peak is about 325 V from Equation (10.1). So even the 600 V version can block the ideal steady-state mains peak with margin. But that does not automatically make 600 V the correct final design choice. Real circuits also face line transients, switching spikes, and safety margin decisions. That is an engineering inference based on the rating and on the transient-protection ideas from Chapter 2.3.

The **12 A RMS on-state current** rating tells us this is not a small signal SCR. It is appropriate for meaningful power conversion. However, that number must never be read in isolation. The final usable current depends on case temperature, heat sinking, surge current duty, and waveform shape.

The **5 mA or 15 mA gate-trigger current** rating tells us the trigger circuit does not need to provide amperes, but it does need to provide reliable synchronized firing pulses with enough gate current margin. In a controlled rectifier, this matters because missing a firing pulse does not merely weaken conduction slightly. It can skip an entire conduction interval.

Table 10.3 translates the product-page data into rectifier-design meaning.

Table 10.3: Reading the TYN612 as a controlled-rectifier artifact

| Product-page item | Plain-language meaning | Why it matters in this chapter |
|---|---|---|
| $V_{DRM}/V_{RRM}$ of 600 V, 800 V, 1000 V | The SCR can block substantial line-related voltage repeatedly | Blocking capability must exceed the worst repetitive voltage seen by the rectifier |
| $I_{T(RMS)} = 12 \text{ A}$ | The SCR can carry meaningful line-frequency current if thermal conditions are respected | Useful for small and medium controlled-rectifier front ends |
| $I_{GT} = 5 \text{ mA}$ or $15 \text{ mA}$ | The gate drive must deliver a real, not merely symbolic, pulse current | Firing-circuit design must guarantee reliable triggering at the chosen firing angle |
| "Standard SCR" family description | Device is intended for practical control functions such as voltage regulation and inrush control | Confirms that phase-controlled power circuits are a normal application, not an edge case |

The important habit is to connect the device ratings back to the waveform. In a single-phase controlled rectifier, the SCR must block when not fired, trigger when commanded, conduct for a substantial interval, and then recover before the next relevant half-cycle. A rating table becomes much easier to understand once you can picture the waveform it is serving.

## How this matters in renewable-energy systems

Single-phase controlled rectifiers are not the newest AC-DC technology, but they remain important for two reasons.

The first reason is conceptual. Many later renewable-energy converters still depend on the same ideas you met here: firing angle, natural commutation, current continuity, freewheeling, and the relation between AC phase and average DC output. If those ideas are clear now, later study of PWM rectifiers, battery chargers, and grid converters becomes much easier.

The second reason is practical. Thyristor-based AC-DC conversion still appears in line-frequency and high-power contexts. Hitachi Energy notes that high-power thyristors are used from soft starters up to HVDC stations rated in the gigawatt range, and its HVDC converter-station overview states that AC is converted to DC and back in converter stations using high-power semiconductor valves [Hitachi Energy Thyristors], [Hitachi Energy HVDC Converter Stations]. ST also lists modern SCR products for **battery charger**, **renewable energy generator**, and **AC-DC controlled rectifier bridge** applications, which shows that controlled-rectifier thinking is still relevant in present-day equipment [ST TN5050H-12WY Product Page].

At the same time, it is important to see the direction of newer designs. NPTEL's current course on line-commutated and PWM rectifiers notes that diode- and thyristor-based rectifiers are mature technologies, but many newer EV and battery-charging applications are moving toward PWM rectifiers for improved size and efficiency [NPTEL Line Commutated and PWM Rectifiers]. That does not make controlled rectifiers obsolete as a learning topic. It makes them foundational. They are the classical starting point from which modern AC-DC conversion is best understood.

## Chapter summary

- A **controlled rectifier** converts AC to DC while allowing the conduction start instant to be controlled by the firing angle $\alpha$ [Rashid, *Power Electronics: Circuits, Devices and Applications*, 4e, Ch. 6].
- For a sinusoidal source, the peak value is $V_m = \sqrt{2}V_{s,rms}$ from Equation (10.1).
- In a single-phase half-wave controlled rectifier with R load, conduction occurs from $\alpha$ to $\pi$ and
  $\boxed{V_{o,avg} = \dfrac{V_m}{2\pi}(1+\cos\alpha)}$ from Equation (10.2).
- In a half-wave controlled rectifier with R-L load, the inductor keeps current flowing beyond $\pi$, so conduction may continue to extinction angle $\beta$.
- During SCR conduction with an R-L load, the current satisfies
  $\boxed{L\dfrac{di_o}{dt}+Ri_o = V_m\sin\omega t}$ from Equation (10.3).
- For the half-wave R-L case without a freewheeling diode,
  $\boxed{V_{o,avg} = \dfrac{V_m}{2\pi}(\cos\alpha-\cos\beta)}$ from Equation (10.4).
- Adding a **freewheeling diode** lets inductive current circulate when the source goes negative and changes the average output to
  $\boxed{V_{o,avg} = \dfrac{V_m}{2\pi}(1+\cos\alpha)}$ from Equation (10.5).
- In a single-phase fully controlled bridge with R load,
  $\boxed{V_{o,avg} = \dfrac{V_m}{\pi}(1+\cos\alpha)}$ from Equation (10.6).
- In a single-phase fully controlled bridge with continuous current,
  $\boxed{V_{o,avg} = \dfrac{2V_m}{\pi}\cos\alpha}$ from Equation (10.7).
- For the full-controlled bridge with continuous current, the average output becomes negative when $\alpha > 90^\circ$.
- In a single-phase semi-controlled bridge with continuous current,
  $\boxed{V_{o,avg} = \dfrac{V_m}{\pi}(1+\cos\alpha)}$ from Equation (10.8).
- The semi-converter is a one-quadrant converter in the usual introductory sense because its average output does not become negative.
- The half-wave controlled rectifier with R load has RMS output
  $\boxed{V_{o,rms} = \dfrac{V_m}{2}\sqrt{1-\dfrac{\alpha}{\pi}+\dfrac{\sin 2\alpha}{2\pi}}}$ from Equation (10.9).
- The full-wave R-load or equivalent pulsed full-wave output has RMS value
  $\boxed{V_{o,rms} = \dfrac{V_m}{\sqrt{2}}\sqrt{1-\dfrac{\alpha}{\pi}+\dfrac{\sin 2\alpha}{2\pi}}}$ from Equation (10.10).
- For the ideal full-controlled bridge with continuous current,
  $\boxed{V_{o,rms} = V_{s,rms}}$ from Equation (10.11).
- Increasing the firing angle reduces average DC output and generally worsens source-side power factor and waveform quality.

## Further reading

- M. H. Rashid, *Power Electronics: Circuits, Devices and Applications*, 4th ed. - A strong textbook source for first-principles treatment of single-phase controlled rectifiers, waveforms, and average-value derivations.
- Ned Mohan, Tore M. Undeland, and William P. Robbins, *Power Electronics: Converters, Applications and Design*, 3rd ed. - Especially useful for building intuition about continuous current, semi-converters, and the meaning of $\alpha$ and $\beta$.
- [Littelfuse, *AN1003: Phase Control Using Thyristors*](https://www.littelfuse.com/~/media/electronics/application_notes/switching_thyristors/littelfuse_thyristor_phase_control_using_thyristors_application_note.pdf.pdf) - A practical note that is very helpful for understanding delay angle, conduction angle, and how output voltage changes with phase control.
- [STMicroelectronics, *AN4607: Basics on the thyristor (SCR) structure and its application*](https://www.st.com/content/ccc/resource/technical/document/application_note/group0/8b/89/db/e6/0d/a1/49/fa/DM00140123/files/DM00140123.pdf/jcr%3Acontent/translations/en.DM00140123.pdf) - A concise refresher on SCR behavior and on where thyristors still appear in UPS, photovoltaic, and related power circuits.
- [Hitachi Energy, *HVDC converter stations*](https://www.hitachienergy.com/us/en/products-and-solutions/hvdc/hvdc-converter-stations) - A useful high-level reading link for seeing how controlled AC-DC conversion scales from textbook rectifiers to grid-scale converter stations.
