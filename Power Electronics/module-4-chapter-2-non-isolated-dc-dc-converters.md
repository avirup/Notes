# Chapter 4.2: Non-isolated DC-DC Converters

## Chapter opening

In Chapter 4.1, we studied the general idea of DC choppers. We learned that a power switch does not need to waste energy in a partly ON state to control DC power. Instead, it can switch rapidly between ON and OFF states, and the average output can be controlled by timing. That idea is the foundation. This chapter takes the next step and gives that foundation a set of practical circuit forms.

The most important non-isolated DC-DC converters are the **buck**, **boost**, **buck-boost**, **Cuk**, and **SEPIC** converters. Each one uses the same basic ingredients we already know: a controlled switch, a diode or synchronous switch, an inductor, a capacitor, and a load. But the way these parts are connected changes the converter's behavior in very useful ways. One topology steps voltage down. Another steps it up. Another can do either, but inverts polarity. Others improve current smoothness or allow both step-up and step-down action without output polarity inversion.

These circuits matter because real renewable-energy and electrified systems rarely operate at just one fixed DC level. A rooftop PV string voltage changes with sunlight and temperature. A battery pack voltage changes with state of charge. A control board may need 12 V, 5 V, and 3.3 V from a larger DC source. A UPS has DC buses, charging stages, and auxiliary supplies. An EV has a traction battery, but also many smaller internal DC rails. Non-isolated converters are often the first tools we use when we need efficient conversion between such DC levels [Mohan, Undeland, Robbins, *Power Electronics: Converters, Applications, and Design*, 3e], [Erickson and Maksimovic, *Fundamentals of Power Electronics*, 2e].

This chapter is written as a beginner-friendly bridge between the abstract idea of chopping and the more design-oriented converter study that comes later. We will begin each topology physically, not just algebraically. We will ask what the switch is doing, where the inductor current flows during ON and OFF intervals, and why the output becomes higher, lower, inverted, or smoother. Then we will derive the ideal continuous-conduction voltage gain step by step. By the end of the chapter, you should be able to look at a basic non-isolated converter and say what it does, why it does it, and where it is likely to be used.

## Prerequisites check

- You should remember the idea of duty cycle $D = T_{ON}/T$ from Chapter 4.1.
- You should know that an inductor opposes sudden change of current, and a capacitor opposes sudden change of voltage.
- You should remember why inductive current needs a path during the switch OFF interval.
- You should be comfortable with average value, instantaneous value, and the basic power relation $P = VI$.
- You should know that ideal converter equations are first approximations. Real devices have voltage drops, resistive losses, and finite switching times.

If duty cycle or the ON-interval/OFF-interval picture feels uncertain, it is worth revisiting Chapter 4.1 first. This chapter builds directly on that language.

## Core content

Before we study the topologies one by one, it helps to keep a simple map in mind. Table 14.1 gives a first comparison. We will justify each line of the table in the sections that follow.

Table 14.1: First comparison of common non-isolated DC-DC converters under ideal CCM assumptions

| Topology | Main function | Ideal voltage gain | Output polarity relative to input ground | A helpful practical note |
| --- | --- | --- | --- | --- |
| Buck | Step down | $\dfrac{V_o}{V_{in}} = D$ | Same polarity | Simple and widely used for point-of-load power supplies |
| Boost | Step up | $\dfrac{V_o}{V_{in}} = \dfrac{1}{1-D}$ | Same polarity | Common when a variable source must feed a higher DC bus |
| Buck-Boost | Step down or step up | $\dfrac{V_o}{V_{in}} = -\dfrac{D}{1-D}$ | Inverted | Useful when a negative output is acceptable or desired |
| Cuk | Step down or step up | $\dfrac{V_o}{V_{in}} = -\dfrac{D}{1-D}$ | Inverted | Input and output currents are smoother than in simple buck-boost |
| SEPIC | Step down or step up | $\dfrac{V_o}{V_{in}} = \dfrac{D}{1-D}$ | Same polarity | Useful when input may move above and below the target output |

Here, $V_{in}$ is the input voltage, $V_o$ is the average output voltage, and $D$ is the duty cycle. The table assumes **continuous conduction mode**, usually shortened to **CCM**, which means the inductor current does not fall to zero during a switching period [Erickson and Maksimovic, *Fundamentals of Power Electronics*, 2e], [NPTEL, Module 4: DC-DC Converters].

### 4.2.1 Buck converter - circuit, operation in CCM, voltage gain

#### Why the buck converter feels natural

Suppose a solar charge controller has a regulated DC bus of $48 \text{ V}$, but it must charge a $12 \text{ V}$ battery. Or suppose a control board inside a converter cabinet needs $5 \text{ V}$ from a $12 \text{ V}$ auxiliary rail. In both cases, the required output voltage is lower than the available input voltage. The most direct switching converter for this job is the **buck converter**, also called a **step-down converter** [Mohan, Undeland, Robbins, *Power Electronics: Converters, Applications, and Design*, 3e], [TI, Buck Converter Basics].

The physical picture is straightforward. During the ON interval, the source is connected to the inductor and load. The inductor current rises because the source is pushing energy into it. During the OFF interval, the main switch opens, but the inductor current cannot suddenly stop. The current continues through the diode or synchronous switch and the load. Because the inductor now helps sustain the load, its current falls more gently. If this process repeats fast enough, the output capacitor smooths the voltage and the average output becomes lower than the input but reasonably steady.

**Image prompt for Figure 14.1:** Create a clean textbook-style technical illustration of an ideal buck converter. Show a DC input source $V_{in}$, controlled switch $S$, freewheeling diode $D$, inductor $L$, output capacitor $C$, and resistive load $R$. Beside the circuit, show aligned waveforms versus time for gate command, switch-node voltage, inductor current $i_L$, and output voltage $v_o$. Mark the ON interval, OFF interval, duty cycle $D$, and indicate that $i_L$ never reaches zero in CCM. Use monochrome engineering style with axes, labels, and units.

#### What continuous conduction mode means here

In the buck converter, the inductor current rises during the ON interval and falls during the OFF interval. If the current remains positive throughout the entire cycle, the converter is in CCM. That condition matters because the most familiar gain equation is derived for CCM.

CCM is not a mysterious operating mode. It simply means the inductor is carrying enough average current, or the inductance is large enough, or the switching frequency is high enough, that the falling current does not reach zero before the next switching cycle begins.

#### ON-state and OFF-state voltages across the inductor

Let us use the ideal circuit and assume steady operation in CCM. We will neglect switch drop, diode drop, and winding resistance for the moment.

During the ON interval, the switch is closed. The diode is reverse biased, and the input source feeds the inductor-load path. The inductor voltage is

$$v_{L,\text{ON}} = V_{in} - V_o \quad \text{(14.1)}$$

Here, $V_{in}$ is input voltage and $V_o$ is average output voltage.

During the OFF interval, the switch is open. The inductor current freewheels through the diode into the load. The left side of the inductor is then near ground through the diode path, so the inductor voltage becomes

$$v_{L,\text{OFF}} = -V_o \quad \text{(14.2)}$$

This negative voltage explains why the inductor current falls in the OFF interval.

#### Using volt-second balance

In steady-state periodic operation, the average voltage across an inductor over one complete switching period must be zero. If it were not zero, the current would keep drifting upward or downward cycle after cycle. This is the **volt-second balance** condition [Erickson and Maksimovic, *Fundamentals of Power Electronics*, 2e].

Applying volt-second balance to the buck converter,

$$D(V_{in} - V_o) + (1-D)(-V_o) = 0 \quad \text{(14.3)}$$

Now expand the expression:

$$DV_{in} - DV_o - V_o + DV_o = 0$$

so

$$DV_{in} - V_o = 0$$

Therefore,

$$\boxed{V_o = D\,V_{in}} \quad \text{(14.4)}$$

Equation (14.4) is the key CCM voltage-gain relation for the ideal buck converter. It says the output is a fraction of the input. Since $0 < D < 1$, the output is lower than the input.

#### A numerical example

Suppose we want to obtain $12 \text{ V}$ from a $48 \text{ V}$ DC source in an ideal buck converter. From Equation (14.4),

$$D = \frac{V_o}{V_{in}} = \frac{12}{48} = 0.25$$

So the switch should be ON for $25\%$ of each cycle.

If the switching frequency is $50 \text{ kHz}$, then the period is

$$T = \frac{1}{f_s} = \frac{1}{50\,000} = 20 \,\mu\text{s}$$

Hence,

$$T_{ON} = DT = 0.25 \times 20 \,\mu\text{s} = 5 \,\mu\text{s}$$

and

$$T_{OFF} = 20 - 5 = 15 \,\mu\text{s}$$

This example is simple, but it teaches an important lesson. The converter does not waste the missing $36 \text{ V}$ as a continuously dropped voltage. It creates a lower average output by controlling the timing of power flow.

#### Inductor ripple in plain language

Although the syllabus emphasizes voltage gain, we should briefly note how the inductor current ripple is estimated. During the ON interval, the current rise is approximately

$$\Delta i_{L,\text{ON}} = \frac{(V_{in}-V_o)DT}{L} \quad \text{(14.5)}$$

where $L$ is the inductance. A larger $L$ or higher switching frequency reduces current ripple. This is one reason filters and switching frequency matter so much in practical converters.

#### Common misconceptions

One common misconception is that the buck converter simply "drops" voltage like a resistor. It does not. It transfers energy in pulses and smooths the result with energy-storage elements.

Another misconception is that the switch-node voltage is the same thing as the output voltage. It is not. The switch node is a pulsed waveform. The output capacitor and inductor action make the average output smoother.

A third misconception is that Equation (14.4) stays exact in all conditions. It is an ideal CCM result. Real drops in the switch, diode, winding resistance, and capacitor ESR make the real output slightly lower. At very light load, the converter may also leave CCM.

Renewable-energy relevance: buck converters are common wherever a higher DC source must feed a lower DC rail. Examples include stepping down a DC link to a battery-charging stage, creating 12 V or 5 V auxiliary rails inside inverters, and powering control electronics from a larger storage or PV-derived DC source. In EVs, the main high-voltage to low-voltage converter is often isolated for safety, but many lower-voltage internal rails are then created by non-isolated buck stages [Power Integrations, Main DC-DC Converters], [TI, TPS566235 product page].

### 4.2.2 Boost converter - circuit, operation in CCM, voltage gain

#### Why boost conversion is not just "adding voltage"

The **boost converter** is the basic step-up converter. It is used when the available input voltage is lower than the desired output voltage. A familiar renewable-energy example is a PV source whose operating voltage must be raised before feeding a DC link or another regulated stage. Another example is a battery-powered system that must create a higher internal rail than the battery itself provides [NPTEL, Module 4 Lecture 10], [Mohan, Undeland, Robbins, *Power Electronics: Converters, Applications, and Design*, 3e].

At first this may seem puzzling. How can a converter produce an output voltage greater than the source if no transformer is present? The answer lies in the inductor. During the ON interval, the source stores energy in the inductor. During the OFF interval, the inductor reverses its terminal voltage in whatever way is necessary to keep current flowing. Its voltage then adds to the source voltage through the diode path, so the load sees a higher voltage.

This is not free energy. The output voltage rises, but the output current is generally lower than the input current for a given power level, because power is approximately conserved aside from losses.

**Image prompt for Figure 14.2:** Create a clean textbook-style technical illustration of an ideal boost converter. Show a DC input source $V_{in}$ feeding an inductor $L$, a controlled switch $S$ from the inductor-switch node to ground, a diode from the switch node to the output, an output capacitor $C$, and load $R$. Beside the circuit, show aligned waveforms for gate command, inductor current $i_L$, switch-node voltage, and output voltage $v_o$. Mark ON and OFF intervals and indicate that inductor current stays above zero in CCM. Use monochrome engineering style with clear labels.

#### ON-state operation

When the switch is ON, the switch node is pulled near ground. The diode becomes reverse biased because the output capacitor holds a higher voltage at the output side. The load is then supplied mainly by the output capacitor for that brief interval, while the inductor stores energy from the source.

The inductor voltage during the ON interval is

$$v_{L,\text{ON}} = V_{in} \quad \text{(14.6)}$$

So the inductor current rises.

#### OFF-state operation

When the switch turns OFF, the inductor current cannot instantly fall to zero. The inductor therefore drives current through the diode into the output capacitor and load. The inductor voltage becomes

$$v_{L,\text{OFF}} = V_{in} - V_o \quad \text{(14.7)}$$

Since the boost output is higher than the input, $V_o > V_{in}$, so Equation (14.7) is negative. That negative inductor voltage makes the inductor current fall during the OFF interval.

#### Deriving the CCM gain

Using volt-second balance,

$$D(V_{in}) + (1-D)(V_{in} - V_o) = 0 \quad \text{(14.8)}$$

Expand the terms:

$$DV_{in} + V_{in} - DV_{in} - V_o + DV_o = 0$$

which becomes

$$V_{in} - V_o(1-D) = 0$$

So the ideal CCM gain is

$$\boxed{V_o = \frac{V_{in}}{1-D}} \quad \text{(14.9)}$$

This equation explains the name step-up converter. As $D$ increases, the denominator becomes smaller, so the ideal output voltage rises.

#### A numerical example

Suppose a PV source around its maximum power point is at $200 \text{ V}$, and a later stage requires an idealized $400 \text{ V}$ DC bus. Using Equation (14.9),

$$400 = \frac{200}{1-D}$$

So

$$1-D = \frac{200}{400} = 0.5$$

and therefore

$$D = 0.5$$

The switch must be ON for half the period in this ideal CCM case.

If the PV voltage later falls to $160 \text{ V}$ and we still want $400 \text{ V}$ ideally, then

$$D = 1 - \frac{160}{400} = 0.6$$

This tells us something important for renewable systems: when the source voltage falls, the converter often compensates by increasing duty cycle.

#### A caution about high duty cycle

Equation (14.9) suggests that $V_o$ becomes extremely large as $D$ approaches $1$. In real converters, that does not happen without limit. Switch resistance, diode drop, winding resistance, parasitics, control limits, and rising current stress all prevent that ideal behavior. High-duty-cycle boost operation can become difficult, lossy, and electrically stressful. So we should read Equation (14.9) as a clean first model, not a promise of unlimited gain.

#### Common misconceptions

The most frequent misconception is that the inductor produces energy by itself. It does not. It stores energy from the source and then releases it in a different time interval.

Another misconception is that the load receives power only when the switch is OFF. In the simple diode-based boost picture, direct energy transfer to the load indeed occurs during the OFF interval, but the output capacitor helps supply the load through the whole cycle.

Renewable-energy relevance: boost converters are widely used when the source voltage is below the required bus voltage. A classic example is a PV front end feeding a higher DC link for an inverter. They also appear in battery-powered systems and LED drivers where a higher regulated DC rail is needed [NPTEL, Module 4 Lecture 10], [TI, Buck-boost & SEPIC product category].

### 4.2.3 Buck-Boost converter - circuit, operation, voltage gain, polarity inversion

#### The key new idea: one converter, two gain directions

The **buck-boost converter** combines the two basic gain possibilities in one topology. It can produce an output magnitude that is either lower or higher than the input, depending on duty cycle. But there is an important price: in the classical single-switch form, the output polarity is inverted with respect to the input ground [NPTEL, Module 4 Lecture 10], [Erickson and Maksimovic, *Fundamentals of Power Electronics*, 2e].

That last point is easy to miss, so let us state it clearly. If the input source is referenced to one ground point, the output voltage of the classical buck-boost converter is negative with respect to that same point.

This makes the buck-boost converter useful for generating negative rails, but less convenient when the load requires the same ground polarity as the source.

**Image prompt for Figure 14.3:** Create a clean textbook-style technical illustration of the classical inverting buck-boost converter. Show input source $V_{in}$, inductor $L$, controlled switch $S$ to ground, diode to the output network, output capacitor $C$, and load $R$ arranged so that the output voltage is negative relative to the input ground. Include aligned waveforms for gate command, inductor current, switch-node voltage, and output voltage polarity marking. Clearly label that the output polarity is inverted. Use monochrome engineering style with axes, labels, and units.

#### ON interval

When the switch is ON, the diode is reverse biased. The source applies voltage across the inductor, and the inductor current rises. During that interval, the load is supplied by the output capacitor.

For the inductor,

$$v_{L,\text{ON}} = V_{in} \quad \text{(14.10)}$$

#### OFF interval

When the switch turns OFF, the inductor current continues and now flows through the diode into the output network. Because of the circuit connection, the output capacitor charges with opposite polarity relative to the input ground.

If we denote the magnitude of the output voltage by $|V_o|$, then the inductor voltage in the OFF interval is approximately

$$v_{L,\text{OFF}} = -|V_o| \quad \text{(14.11)}$$

Applying volt-second balance,

$$D(V_{in}) + (1-D)(-|V_o|) = 0 \quad \text{(14.12)}$$

Therefore,

$$|V_o| = \frac{D}{1-D}V_{in}$$

Since the actual output polarity is inverted,

$$\boxed{\frac{V_o}{V_{in}} = -\frac{D}{1-D}} \quad \text{(14.13)}$$

This equation shows both features at once:

- the magnitude can be less than or greater than the input
- the sign is negative

If $D < 0.5$, then $|V_o| < V_{in}$ and the converter behaves as a step-down-in-magnitude stage. If $D > 0.5$, then $|V_o| > V_{in}$ and it behaves as a step-up-in-magnitude stage.

#### A numerical example

Suppose we need $-18 \text{ V}$ from a $12 \text{ V}$ source. Using Equation (14.13) in magnitude form,

$$18 = \frac{D}{1-D} \times 12$$

So

$$\frac{18}{12} = \frac{D}{1-D} = 1.5$$

which gives

$$D = 1.5(1-D) = 1.5 - 1.5D$$

Hence,

$$2.5D = 1.5$$

and

$$D = 0.6$$

So an ideal duty cycle of $60\%$ gives the required magnitude, and the polarity is negative.

#### Why polarity inversion matters practically

Many beginners first focus only on the gain magnitude and forget the sign. That causes real design errors. If a load expects a positive 12 V rail with respect to system ground, the classical inverting buck-boost converter is not the right direct choice. But if an op-amp stage, sensor interface, or gate-drive support rail needs a negative supply, the topology can be very useful.

Renewable-energy relevance: the classical inverting buck-boost converter is less common as the main power stage in PV and battery systems than buck or boost converters, because many main loads do not want inverted polarity. However, it remains important for auxiliary negative rails, instrumentation supplies, and as a conceptual bridge to more advanced buck-boost families [TI, PMP15026 reference design], [TI, TIDA-01423 reference design].

### 4.2.4 Cuk converter - circuit, operation, voltage gain, advantages

#### Why the Cuk converter was introduced

The **Cuk converter** can be understood as a refinement of the inverting buck-boost idea. It also allows step-down or step-up operation in magnitude, and it also inverts output polarity in its basic form. But instead of transferring energy in the simplest single-inductor way, it uses two inductors and a coupling capacitor as the main energy-transfer element. The result is one of its biggest practical advantages: input current and output current are both smoother than in the classical buck-boost converter [Mohan, Undeland, Robbins, *Power Electronics: Converters, Applications, and Design*, 3e], [TI, LM2611 product page], [TI, PMP30487 reference design].

That smoothness matters in power electronics because ripple current affects EMI, source stress, capacitor heating, and sometimes the behavior of the energy source itself.

#### Circuit intuition

In a Cuk converter, one inductor sits on the input side and another on the output side. Between the switching network and the load path sits an energy-transfer capacitor. During one switching interval, that capacitor is charged. During the other, it discharges energy into the output side. The two inductors help keep both the input current and output current comparatively continuous.

**Image prompt for Figure 14.4:** Create a clean textbook-style technical illustration of a Cuk converter. Show input source $V_{in}$, input inductor $L_1$, controlled switch $S$, diode $D$, energy-transfer capacitor $C_1$, output inductor $L_2$, output capacitor $C_o$, and load $R$. Include a polarity label showing the output is negative with respect to input ground. Beside the circuit, show smoothed input current and output current waveforms to emphasize that both are relatively continuous. Use monochrome engineering style with labels and units.

#### Operation at a beginner level

We do not need to follow every branch current in full symbolic detail to understand the converter physically.

During the ON interval, the switch conducts. The diode is reverse biased. The input inductor $L_1$ stores energy from the source, while the capacitor $C_1$ transfers energy into the output side through $L_2$ and the load in the pattern allowed by the circuit.

During the OFF interval, the switch opens and the diode conducts. The input-side energy and the capacitor's transferred energy continue supporting the output path.

What matters most at this stage is the role of the capacitor $C_1$. In the Cuk converter, it is not merely a small ripple filter. It is the main energy-transfer element between input and output sides.

#### Voltage gain

For the ideal Cuk converter in CCM, the voltage-gain relation is the same as that of the classical inverting buck-boost converter:

$$\boxed{\frac{V_o}{V_{in}} = -\frac{D}{1-D}} \quad \text{(14.14)}$$

So the output magnitude can be lower or higher than the input, and the polarity is inverted.

This often surprises beginners because the Cuk circuit looks more complicated than the buck-boost converter. But different circuits can share the same ideal gain relation while differing strongly in current ripple, component stress, and practical behavior.

#### A numerical example

Suppose a converter must create $-12 \text{ V}$ from a $24 \text{ V}$ source. Using Equation (14.14) in magnitude form,

$$12 = \frac{D}{1-D}\times 24$$

So

$$\frac{12}{24} = \frac{D}{1-D} = 0.5$$

which gives

$$D = 0.5(1-D) = 0.5 - 0.5D$$

Hence,

$$1.5D = 0.5$$

and therefore

$$D \approx 0.333$$

So a duty cycle of about $33.3\%$ produces an ideal output of $-12 \text{ V}$ from $24 \text{ V}$.

#### Why continuous input and output currents are valuable

This is the central advantage of the Cuk converter in introductory study.

If the source current is highly pulsating, the source side may need stronger filtering and may suffer larger ripple-related stress. If the load current is highly pulsating, the output capacitor and load current ripple may become more difficult to manage. Because the Cuk converter uses inductors on both sides, both currents can be comparatively smooth [TI, LM2611 product page], [TI, PMP30487 reference design].

TI's LM2611 product description explicitly notes that the use of an input and output inductor enables low ripple and RMS current on both input and output sides [TI, LM2611 product page]. TI's PMP30487 reference design similarly highlights continuous currents at input and output and connects that feature to lower conducted emissions [TI, PMP30487 reference design].

#### The tradeoff

The Cuk converter is not automatically "better" than simpler topologies. It uses more passive components, the energy-transfer capacitor carries significant ripple current, and the classical form still inverts polarity. So its advantages must be weighed against added complexity and component stress.

#### Common misconceptions

One misconception is that the Cuk converter is just a buck-boost converter with extra parts that do not change much. In fact, those added parts change current waveform quality in an important way.

Another misconception is that smooth current means the converter has no ripple. That is not true. Ripple still exists, but its shape and severity are different from those of simpler topologies.

Renewable-energy relevance: the Cuk converter is attractive when current smoothness matters. Low input current ripple can be desirable when interfacing with sensitive sources, and low output ripple can help certain loads or measurement circuits. TI's automotive and industrial reference designs explicitly emphasize low reflected ripple and good EMI behavior for Cuk-based solutions [TI, PMP30487 reference design], [TI, PMP30602 reference design].

### 4.2.5 SEPIC converter - circuit, operation, applications in PV systems

#### Why SEPIC is so useful with variable inputs

The **SEPIC converter**, whose name expands to **Single-Ended Primary Inductor Converter**, is a non-isolated topology that can step the output voltage up or down while keeping the output polarity the same as the input polarity [Analog Devices, SEPIC glossary]. This makes it especially useful when the input may move above and below the desired regulated output.

That situation appears often in real systems. A battery voltage changes as it charges and discharges. A PV module voltage changes with irradiance, temperature, and operating point. An automotive or industrial DC rail may sag or surge. If the required output must remain, for example, at $12 \text{ V}$ while the input sometimes falls below $12 \text{ V}$ and sometimes rises above it, the SEPIC converter becomes a natural candidate [Analog Devices, High Efficiency Synchronous SEPIC for Automotive and Industrial Installations], [TI, TIDA-00781 reference design].

#### Circuit intuition

The SEPIC converter uses two inductors, a series coupling capacitor, a switch, a diode, and an output capacitor. Like the Cuk converter, it contains a capacitor that plays an active role in energy transfer. But unlike the basic Cuk converter, the SEPIC keeps the output non-inverted.

In beginner terms, we can view the SEPIC as a converter that stores energy in magnetic elements during one interval and releases it in a way that can either raise or lower the output, depending on duty cycle.

**Image prompt for Figure 14.5:** Create a clean textbook-style technical illustration of a SEPIC converter. Show input source $V_{in}$, input inductor $L_1$, coupling capacitor $C_1$, second inductor $L_2$ or coupled-inductor equivalent, controlled switch $S$, diode $D$, output capacitor $C_o$, and load $R$. Include a note that the output polarity is the same as the input polarity. Beside the circuit, show two example operating cases: one with $V_{in} < V_o$ and one with $V_{in} > V_o$, both producing a regulated positive output. Use monochrome engineering style with clear labels.

#### A simple operating picture

During the ON interval, the switch conducts, the diode is reverse biased, and energy is stored in the inductive elements. The coupling capacitor is also part of the energy movement between stages.

During the OFF interval, the switch opens, the diode conducts, and energy is delivered to the output capacitor and load.

A very useful steady-state fact is that the average voltage across the series coupling capacitor is approximately equal to the input voltage in the ideal CCM model. Using that fact together with volt-second balance leads to the SEPIC gain relation [Analog Devices, SEPIC glossary], [Analog Devices, High Efficiency Synchronous SEPIC for Automotive and Industrial Installations].

#### Voltage gain

For the ideal SEPIC converter in CCM,

$$\boxed{\frac{V_o}{V_{in}} = \frac{D}{1-D}} \quad \text{(14.15)}$$

This is the same magnitude relation as the classical buck-boost converter, but with positive polarity.

That means:

- if $D < 0.5$, then $V_o < V_{in}$ and the converter acts in a step-down sense
- if $D = 0.5$, then $V_o = V_{in}$ ideally
- if $D > 0.5$, then $V_o > V_{in}$ and the converter acts in a step-up sense

#### A numerical example for a PV-relevant case

Suppose a small PV-powered controller must maintain a regulated $24 \text{ V}$ output from a PV source that may vary between $18 \text{ V}$ and $36 \text{ V}$ depending on sunlight and operating point.

When $V_{in} = 18 \text{ V}$, Equation (14.15) gives

$$24 = \frac{18D}{1-D}$$

So

$$24(1-D) = 18D$$

$$24 = 42D$$

$$D \approx 0.571$$

When $V_{in} = 36 \text{ V}$,

$$24 = \frac{36D}{1-D}$$

$$24(1-D) = 36D$$

$$24 = 60D$$

$$D = 0.4$$

So the same converter can regulate the same positive output while the input moves both below and above the output value. That is exactly why SEPIC converters attract attention in variable-input systems.

#### Why SEPIC is often mentioned in PV and automotive contexts

TI's TIDA-00781 SEPIC reference design states plainly that the topology allows both voltage step-up and step-down conversion over a wide input range [TI, TIDA-00781 reference design]. Analog Devices highlights SEPIC's value when the input may fall far below or rise above the output, such as in cold-crank and load-dump situations [Analog Devices, High Efficiency Synchronous SEPIC for Automotive and Industrial Installations]. TI also offers a solar-panel-related SEPIC reference design for auxiliary outputs, which shows that the topology is not merely theoretical in energy systems [TI, PMP21883 reference design].

For PV systems, the attraction is easy to understand. A solar source is variable. If a downstream stage or storage element needs a fairly constant voltage, a topology that can both raise and lower voltage without reversing polarity becomes very convenient.

#### The practical tradeoff

SEPIC is flexible, but flexibility comes with cost. There are more components than in a buck or boost converter. The coupling capacitor and semiconductors can see appreciable stress. Efficiency may be lower than a simpler topology when the operating range does not actually require both buck and boost capability. So engineers choose SEPIC when its flexibility is genuinely needed, not merely because it is versatile.

#### Common misconceptions

One misconception is that SEPIC is "just a non-inverting buck-boost" and therefore all practical details are the same. The gain intuition is related, but device stress, current waveforms, and implementation details are not identical.

Another misconception is that because SEPIC can produce $V_o = V_{in}$ ideally at $D = 0.5$, it must be the best converter whenever input and output are similar. That is not necessarily true. If the input is almost always above the output, a buck converter may be simpler and more efficient. If the input is almost always below the output, a boost converter may be the better choice.

Renewable-energy relevance: SEPIC converters are especially appealing in variable-input systems such as PV-powered auxiliaries, battery-operated electronics, and automotive rails that can wander above and below the desired output [TI, TIDA-00781 reference design], [Analog Devices, High Efficiency Synchronous SEPIC for Automotive and Industrial Installations].

## Worked interpretation exercise

### Reading a real buck-converter product page

To make the chapter practical, let us read a real converter artifact. We will use the TI product page for the **TPS566235**, which TI describes as a 4.5 V to 18 V, 6 A synchronous buck converter [TI, TPS566235 product page].

From the product details, TI lists these important items:

- topology: Buck
- input voltage range: $4.5 \text{ V}$ to $18 \text{ V}$
- output voltage range: $0.6 \text{ V}$ to $7 \text{ V}$
- output current: up to $6 \text{ A}$
- switching frequency: $600 \text{ kHz}$
- maximum duty cycle: $88\%$
- integrated power FETs and protection features such as overcurrent, overtemperature, and UVLO [TI, TPS566235 product page]

Now let us interpret what those numbers are telling us.

First, the topology field says **Buck**. So even before reading the rest, we know the IC is meant for step-down conversion. That means it is the right family for converting a higher DC rail to a lower one, not for boosting a low source to a higher output.

Second, the input range is $4.5 \text{ V}$ to $18 \text{ V}$, while the output range is $0.6 \text{ V}$ to $7 \text{ V}$. This immediately matches the buck-converter role. The intended output is below the input in normal use.

Third, the $6 \text{ A}$ rating tells us the device is not just for tiny logic loads. It can serve substantial low-voltage rails such as processor, FPGA, or embedded-controller supplies. In a renewable-energy product, a converter of this class might appear in the control electronics, communication board, sensor subsystem, or low-voltage auxiliary stages, not as the main PV-power-processing front end.

Fourth, the product page says the converter is **synchronous**. That means the simple diode of the introductory buck converter is replaced in practice by an actively controlled MOSFET for lower loss. This is a good reminder that the textbook buck circuit is the conceptual starting point, while modern efficient implementations often use synchronous rectification.

Fifth, the listed $600 \text{ kHz}$ switching frequency suggests smaller magnetic and capacitive components than a much lower-frequency design would require, though switching loss considerations also become important. Even without full design equations yet, we can already see how datasheet frequency relates to the size-efficiency tradeoff.

Finally, the page lists protections such as UVLO, overcurrent, and overtemperature. This shows the difference between topology study and product study. The topology explains how voltage conversion happens. The product page adds the practical engineering needed to make that topology robust in real hardware.

The main lesson from this exercise is simple: when you read a converter datasheet or product page, first identify the topology, then compare the input range and output range, then check current capability, switching frequency, and protections. Those first few entries already tell you whether the device belongs to the problem you are trying to solve.

## How this matters in renewable-energy systems

Non-isolated DC-DC converters appear everywhere in renewable-energy and electrified systems, but not always in the same role.

In solar PV, the **boost converter** is a natural choice when a lower and variable PV voltage must feed a higher DC link. The **SEPIC converter** becomes attractive when the PV or auxiliary input may move above and below the desired output, especially in smaller support supplies or wide-range intermediate stages. In some low-power PV subsystems, low ripple and wide-range regulation can matter more than minimum part count [TI, TIDA-00781 reference design], [TI, PMP21883 reference design].

In battery systems, the **buck converter** is common when a higher DC bus must charge a lower-voltage battery or power lower-voltage electronics. The **buck-boost** and **SEPIC** families become important when battery voltage varies widely over state of charge and the required output must remain regulated. A topology that works only as pure step-down or pure step-up is sometimes not enough.

In wind-energy and EV-related electronics, these converters often appear in auxiliary power processing rather than only in the main energy path. Control boards, sensors, communication modules, gate-drive support rails, and measurement stages all need reliable low-voltage DC rails. Even when the major traction or charger stage is isolated, many internal secondary rails are still generated by non-isolated buck, boost, Cuk, or SEPIC stages.

The larger lesson is that renewable-energy systems are variable by nature. Sunlight changes. Wind changes. Battery voltage changes. Load demand changes. Non-isolated DC-DC converters are one of the main ways we shape that variable electrical reality into the voltage levels that useful equipment actually needs.

## Chapter summary

- A **buck converter** is a step-down converter. In ideal CCM, its gain is $\dfrac{V_o}{V_{in}} = D$.
- A **boost converter** is a step-up converter. In ideal CCM, its gain is $\dfrac{V_o}{V_{in}} = \dfrac{1}{1-D}$.
- A **buck-boost converter** can step down or step up in magnitude, but its classical form inverts polarity. In ideal CCM, $\dfrac{V_o}{V_{in}} = -\dfrac{D}{1-D}$.
- A **Cuk converter** has the same ideal CCM gain as the classical buck-boost converter, but uses two inductors and an energy-transfer capacitor to obtain smoother input and output currents.
- A **SEPIC converter** can step down or step up while keeping output polarity the same as input polarity. In ideal CCM, $\dfrac{V_o}{V_{in}} = \dfrac{D}{1-D}$.
- **Continuous conduction mode (CCM)** means inductor current does not fall to zero during a switching cycle.
- **Volt-second balance** is the steady-state idea that the average voltage across an inductor over one switching period is zero.
- The converter topology affects not only voltage gain, but also current ripple, polarity, EMI behavior, component count, and application suitability.
- Buck converters are often best when the output is always below the input.
- Boost converters are often best when the output is always above the input.
- Buck-boost, Cuk, and SEPIC converters are useful when the operating range crosses both sides of the target output level or when ripple and polarity constraints matter.

## Further reading

1. Robert W. Erickson and Dragan Maksimovic, *Fundamentals of Power Electronics*, 2nd ed.  
   A rigorous but still readable reference for volt-second balance, CCM analysis, and the deeper behavior of basic converters.

2. Ned Mohan, Tore M. Undeland, and William P. Robbins, *Power Electronics: Converters, Applications, and Design*, 3rd ed.  
   A classic power-electronics text that explains the operation and applications of the main DC-DC topologies in a very systematic way.

3. NPTEL, "Module 4: DC-DC Converters" and "Lecture 10: Boost and Buck-Boost Converters," archive.nptel.ac.in.  
   Useful introductory material with topology-level explanations and waveform-focused discussion suitable for self-study.

4. Texas Instruments, "TPS566235 4.5-V to 18-V Input, 6-A Synchronous Step-Down Converter" product page and datasheet.  
   A good real-world example of how an ideal buck concept appears in a modern commercial regulator.

5. Analog Devices, "High Efficiency Synchronous SEPIC for Automotive and Industrial Installations," and TI, "TIDA-00781 12W SEPIC Power Supply Reference Design."  
   These sources are especially helpful for seeing why SEPIC converters matter when input voltage can move above and below the target output.
