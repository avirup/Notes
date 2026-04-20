# Unit 1: Basic Electrical Quantities, Components, and Sources

## Chapter Opening

A student usually meets electrical engineering through ordinary objects: a torch powered by a dry cell, a ceiling fan connected to the 230 V supply, a mobile charger, a water pump, or a table lamp. These devices look different, but the same basic questions arise in all of them. What pushes charge through a circuit? What actually flows? Why does a component become hot? Why does one device need DC and another work from AC? Why does a battery voltage fall when a load is connected?

This chapter answers those first questions. It introduces the basic quantities used throughout electrical and electronics engineering: **EMF**, **current**, **potential difference**, **power**, and **energy**. It then explains the three most important passive components, namely the **resistor**, **capacitor**, and **inductor**. After that, it studies simple signal ideas such as **DC**, **AC**, **periodic**, and **non-periodic** waveforms. Finally, it introduces ideal and practical sources and shows how one source model can be transformed into another for circuit analysis.

This is the foundation for everything that follows. Later chapters on magnetic circuits, AC circuits, transformers, machines, semiconductor devices, op-amps, and digital electronics all depend on the vocabulary and physical understanding built here.

## Prerequisites Check

- Basic arithmetic with decimals and fractions.
- Simple algebraic rearrangement such as $I = \frac{V}{R}$ from $V = IR$.
- Familiarity with a battery, lamp, switch, and wire as simple circuit elements.
- School-level idea that a circuit must be closed for current to flow.
- Basic unit conversion such as mA to A, k$\Omega$ to $\Omega$, and h to s.

If any of these points feel weak, review them before moving too far ahead. This chapter does not need advanced mathematics, but it does require careful attention to units and meaning.

## Core Content

### 1.1 Basic Electrical Quantities

Consider a simple circuit with a battery and a small lamp. The battery supplies energy. The lamp receives that energy and converts it mainly into light and heat. To describe this process properly, we need a few precise quantities.

#### EMF

A source such as a cell, battery, or generator gives energy to electric charges. The energy supplied per unit charge is called **electromotive force**, usually shortened to **EMF**. The name is historical. EMF is not a mechanical force. It is measured in volts [V. K. Mehta and Rohit Mehta, *Principles of Electrical Engineering and Electronics*].

If a source supplies energy $W$ joules to a charge $Q$ coulombs, the voltage associated with that transfer is

$$
V = \frac{W}{Q} \tag{1.1}
$$

In Equation (1.1), $V$ is in volts, $W$ is in joules, and $Q$ is in coulombs.

This equation gives the meaning of one volt: one volt means one joule of energy per coulomb of charge.

#### Potential difference

The **potential difference** between two points is the difference in electric potential between them. In practical circuit work, when a voltmeter is connected across a bulb, a resistor, or the terminals of a battery, it measures potential difference between those two points [S. K. Bhattacharya, *Basic Electricals and Electronics*].

At this level, it is useful to keep the distinction simple:

- **EMF** usually refers to the source value.
- **Potential difference** refers to the voltage between any two points in a circuit.

In many beginner problems the numerical value may be the same, but the words do not mean exactly the same thing.

#### Electric current

**Electric current** is the rate of flow of electric charge. If a charge $Q$ passes through a cross-section of a conductor in time $t$, then

$$
I = \frac{Q}{t} \tag{1.2}
$$

In Equation (1.2), $I$ is current in amperes, $Q$ is charge in coulombs, and $t$ is time in seconds [V. K. Mehta and Rohit Mehta, *Principles of Electrical Engineering and Electronics*].

One ampere means one coulomb of charge passing a point in one second.

It is easy to say that current is the “flow of electricity”, but it is better to be more precise. Current is the flow of charge through a conducting path. In metallic conductors, the moving charges are electrons. In other media, such as electrolytes, the charge carriers are different. For basic circuit calculations, we usually focus on the amount of current rather than on the detailed motion of the carriers.

#### Power

A lamp glows, a heater becomes hot, and a motor rotates because electrical energy is converted into other forms. The rate at which this conversion happens is called **electric power**.

For a simple DC circuit,

$$
P = VI \tag{1.3}
$$

In Equation (1.3), $P$ is power in watts, $V$ is voltage in volts, and $I$ is current in amperes [S. K. Bhattacharya, *Basic Electricals and Electronics*].

If a device operates at high voltage but draws very little current, its power may still be moderate. If a device draws a large current even at low voltage, its power can also be significant. Power depends on both voltage and current.

#### Energy

**Electrical energy** is the total electrical work done over a period of time. If a device consumes power $P$ for a time $t$, then the energy transferred is

$$
W = Pt \tag{1.4}
$$

Combining Equation (1.3) with Equation (1.4), we also get

$$
W = VIt \tag{1.5}
$$

When $P$ is in watts and $t$ is in seconds, the energy is in joules [BIPM, *The International System of Units (SI) Brochure*](https://www.bipm.org/en/publications/si-brochure/).

In homes and industries, energy is often measured in watt-hour or kilowatt-hour because those units are convenient for longer durations:

$$
1\ \text{Wh} = 3600\ \text{J} \tag{1.6}
$$

and

$$
1\ \text{kWh} = 3.6 \times 10^6\ \text{J} \tag{1.7}
$$

The unit kWh appears on electricity bills. It is a unit of energy, not power.

#### Table 1.1 Basic electrical quantities

| Quantity | Symbol | SI unit | Meaning |
|---|---:|---:|---|
| EMF / voltage | $V$ or $\mathcal{E}$ | volt (V) | energy per unit charge |
| Current | $I$ | ampere (A) | rate of flow of charge |
| Power | $P$ | watt (W) | rate of energy transfer |
| Energy | $W$ or $E$ | joule (J) | total electrical work done |
| Charge | $Q$ | coulomb (C) | quantity of electricity |

#### Worked Example 1.1

A 12 V battery supplies a current of 0.5 A to a lamp for 3 hours. Find the power and the energy consumed.

First find the power using Equation (1.3):

$$
P = VI = 12 \times 0.5 = 6\ \text{W}
$$

Now find the energy. If we want the answer in joules, time must be in seconds:

$$
3\ \text{h} = 3 \times 3600 = 10800\ \text{s}
$$

Using Equation (1.4),

$$
W = Pt = 6 \times 10800 = 64800\ \text{J}
$$

In watt-hour form,

$$
W = 6 \times 3 = 18\ \text{Wh}
$$

So the lamp consumes **6 W** of power and **64800 J** or **18 Wh** of energy.

#### Worked Example 1.2

A small 230 V table fan draws 0.25 A from the supply. Estimate its power using the simple relation $P = VI$.

$$
P = VI = 230 \times 0.25 = 57.5\ \text{W}
$$

So the estimated input power is **57.5 W**.

This is a first estimate only. Later, in the AC chapter, we will see that for many AC loads the actual power depends on power factor as well.

#### Common misconceptions

- Voltage does not flow. Current flows.
- Power and energy are not the same quantity. Power is a rate. Energy is the total amount transferred.
- A component usually does not “use up current”. It draws current while converting electrical energy.
- EMF and potential difference are related ideas, but the terms are not fully interchangeable.

#### Practical note

When using a digital multimeter, voltage is measured across a component, while current is measured by placing the meter in series with the circuit. Reversing these connections is a common beginner mistake and can damage the meter or blow its fuse [Fluke, *How to Measure DC Voltage with a Digital Multimeter*](https://www.fluke.com/en-in/learn/blog/digital-multimeters/how-to-measure-dc-voltage-with-a-digital-multimeter).

### 1.2 Passive Components

A source alone is not enough to make a useful circuit. We need elements that control current, store energy, delay response, filter signals, or help build timing and measurement networks. The three most important passive components are the resistor, capacitor, and inductor.

They are called **passive** because they do not generate electrical energy by themselves.

#### Resistor

A **resistor** is a component that opposes current in a circuit. This opposition is called **resistance**, and its SI unit is the ohm, written as $\Omega$.

For many practical resistors operating in their normal region, voltage and current are related by **Ohm’s law**:

$$
V = IR \tag{1.8}
$$

In Equation (1.8), $V$ is the voltage across the resistor, $I$ is the current through it, and $R$ is the resistance [S. K. Bhattacharya, *Basic Electricals and Electronics*].

The physical meaning is direct:

- if resistance stays fixed and current increases, the voltage drop increases,
- if voltage stays fixed and resistance increases, the current decreases.

In an ordinary circuit, a resistor also converts electrical energy mainly into heat. The power in a resistor can be written in three equivalent ways:

$$
P = VI \tag{1.9}
$$

$$
P = I^2R \tag{1.10}
$$

$$
P = \frac{V^2}{R} \tag{1.11}
$$

Equation (1.10) and Equation (1.11) follow from Equation (1.9) together with Ohm’s law.

Resistors are used for current limiting, voltage division, biasing electronic devices, and heat generation in appliances such as irons and electric heaters.

#### Worked Example 1.3

A 10 V source is connected across a 2 k$\Omega$ resistor. Find the current and the power dissipated.

Using Equation (1.8),

$$
I = \frac{V}{R} = \frac{10}{2000} = 0.005\ \text{A}
$$

So,

$$
I = 5\ \text{mA}
$$

Now use Equation (1.9):

$$
P = VI = 10 \times 0.005 = 0.05\ \text{W}
$$

So the resistor current is **5 mA** and the power dissipation is **0.05 W**.

In practice, a resistor with a rating higher than 0.05 W should be selected. A common safe choice would be a **0.25 W** resistor.

#### Capacitor

A **capacitor** stores charge and energy in an electric field. It consists of two conducting surfaces separated by an insulating material called a dielectric [Murata, *Basics of Capacitors*](https://article.murata.com/en-us/article/basics-of-capacitors).

The basic relation is

$$
C = \frac{Q}{V} \tag{1.12}
$$

Here, $C$ is capacitance in farads, $Q$ is charge in coulombs, and $V$ is the voltage across the capacitor.

This equation means that capacitance tells how much charge is stored per volt.

The energy stored in a capacitor is

$$
W_C = \frac{1}{2}CV^2 \tag{1.13}
$$

In Equation (1.13), $W_C$ is the stored energy in joules, $C$ is the capacitance in farads, and $V$ is the voltage across the capacitor [V. K. Mehta and Rohit Mehta, *Principles of Electrical Engineering and Electronics*].

To understand capacitor behavior, think first about charging from a battery. At the moment of connection, the capacitor is uncharged. Current flows and charge builds up on the plates. As the capacitor voltage rises, the charging current reduces. After some time, in an ideal DC circuit, charging stops and the capacitor behaves like an open circuit.

This is why a capacitor does not pass steady DC continuously. It responds mainly when voltage is changing.

In AC circuits, the voltage changes continuously, so the capacitor keeps charging and discharging. Because of that repeated charge movement, current exists in the circuit branch.

Common applications of capacitors include:

- smoothing the output of rectifiers,
- coupling AC signals between circuit stages,
- bypassing unwanted noise,
- timing circuits,
- power factor correction in suitable systems.

#### Worked Example 1.4

A capacitor of $1000\ \mu\text{F}$ is charged to 12 V. Find the energy stored.

First convert the capacitance:

$$
1000\ \mu\text{F} = 1000 \times 10^{-6}\ \text{F} = 0.001\ \text{F}
$$

Now use Equation (1.13):

$$
W_C = \frac{1}{2}CV^2
$$

$$
W_C = \frac{1}{2} \times 0.001 \times 12^2
$$

$$
W_C = 0.0005 \times 144 = 0.072\ \text{J}
$$

So the capacitor stores **0.072 J** of energy.

This value is small compared with the energy in a battery, but it is very useful in electronic circuits that need short-term storage and smoothing.

#### Inductor

An **inductor** is usually made by winding wire into a coil. When current flows through the coil, a magnetic field is produced. Because of this field, the inductor stores energy in magnetic form [Coilcraft, *Inductance and Inductors*](https://www.coilcraft.com/en-us/resources/tools/what-is-inductance/).

The voltage across an inductor is related to the rate of change of current by

$$
v = L\frac{di}{dt} \tag{1.14}
$$

In Equation (1.14), $v$ is the voltage across the inductor, $L$ is inductance in henry, and $\frac{di}{dt}$ is the rate of change of current with time [S. K. Bhattacharya, *Basic Electricals and Electronics*].

This equation gives the real physical meaning of an inductor. It opposes change in current. If the current tries to change rapidly, the inductor produces a voltage that resists that change.

The energy stored in an inductor is

$$
W_L = \frac{1}{2}LI^2 \tag{1.15}
$$

In Equation (1.15), $W_L$ is in joules, $L$ is in henry, and $I$ is the current through the inductor.

Inductors are common in filters, relays, transformer windings, motor windings, and switching power supplies.

#### Worked Example 1.5

An inductor of 20 mH carries a current of 2 A. Find the energy stored in it.

First convert the inductance:

$$
20\ \text{mH} = 20 \times 10^{-3}\ \text{H} = 0.02\ \text{H}
$$

Using Equation (1.15),

$$
W_L = \frac{1}{2}LI^2 = \frac{1}{2} \times 0.02 \times 2^2
$$

$$
W_L = 0.01 \times 4 = 0.04\ \text{J}
$$

So the inductor stores **0.04 J** of energy.

#### Table 1.2 Comparison of the three passive components

| Component | Main effect | Unit | Stores energy in | Simple steady-DC behavior | Common use |
|---|---|---:|---|---|---|
| Resistor | opposes current | $\Omega$ | none ideally | allows current according to $V=IR$ | current limiting, voltage division |
| Capacitor | opposes change in voltage | F | electric field | charges, then ideally blocks steady current | filtering, coupling, timing |
| Inductor | opposes change in current | H | magnetic field | resists sudden current change | chokes, coils, filters |

#### Common misconceptions

- A resistor does not “consume voltage”. It causes a voltage drop while carrying current.
- A capacitor does not pass steady DC after charging is complete, but it does allow charging current.
- An inductor is not just a long piece of wire. Its important property is inductance, which is linked to magnetic field and changing current.
- Capacitors and inductors both store energy, but not in the same way. A capacitor stores energy in an electric field, while an inductor stores it in a magnetic field.

#### Practical note

The value of a resistor can often be read from its colour bands and then checked with a multimeter. Capacitance and inductance are measured more reliably with an LCR meter, which is why such an instrument appears in the laboratory syllabus for this course.

### 1.3 Signal Waveforms

When voltage or current changes with time, the pattern of that change is called a **waveform**. A waveform tells us whether a signal is constant, alternating, pulsed, slowly changing, or irregular.

It is helpful to begin with what you might see in practice:

- a battery gives nearly steady DC,
- a rectifier output before filtering gives pulsating DC,
- the mains supply gives AC,
- a switch opening or closing may produce a short transient that is not periodic.

#### DC and AC signals

A **DC signal** has one polarity. In the simplest case, its value remains constant with time. A battery is the standard example.

An **AC signal** changes with time and reverses direction periodically. The domestic supply in India is a common example: the nominal single-phase supply is 230 V at 50 Hz.

At beginner level, it helps to classify signals carefully:

- **steady DC**: constant magnitude and one polarity,
- **pulsating DC**: magnitude changes with time but polarity remains the same,
- **AC**: magnitude changes and polarity reverses.

This distinction matters. A rectifier output before filtering is not pure AC. It is also not steady DC. It is pulsating DC.

#### Periodic and non-periodic waveforms

A waveform is **periodic** if it repeats after a fixed interval of time. That interval is called the **time period**, represented by $T$.

The number of cycles completed in one second is called the **frequency**, represented by $f$:

$$
f = \frac{1}{T} \tag{1.16}
$$

In Equation (1.16), $f$ is in hertz and $T$ is in seconds.

If the supply frequency is 50 Hz, the period is

$$
T = \frac{1}{50} = 0.02\ \text{s} = 20\ \text{ms} \tag{1.17}
$$

So one complete cycle of the 50 Hz supply takes 20 ms.

A waveform is **non-periodic** if it does not repeat regularly. A sudden switching pulse, a one-time discharge event, or an irregular sensor signal can be non-periodic.

#### Amplitude and time variation

The **amplitude** of a waveform is its maximum value measured from the reference level. If a sine wave varies from +10 V to -10 V, its amplitude is 10 V and its peak-to-peak value is 20 V.

When observing a waveform on an oscilloscope:

- the horizontal axis represents time,
- the vertical axis represents voltage,
- the shape shows how voltage varies with time [Keysight, *Basic Oscilloscope Fundamentals*](https://www.keysight.com/zz/en/assets/7018-01761/application-notes/5989-8064.pdf).

An oscilloscope is therefore very different from a multimeter. A multimeter usually gives one numerical reading. An oscilloscope shows the actual shape.

#### Worked Example 1.6

A waveform repeats every 5 ms. Find its frequency.

First convert the time period:

$$
T = 5\ \text{ms} = 5 \times 10^{-3}\ \text{s} = 0.005\ \text{s}
$$

Now use Equation (1.16):

$$
f = \frac{1}{T} = \frac{1}{0.005} = 200\ \text{Hz}
$$

So the waveform frequency is **200 Hz**.

#### Worked Example 1.7

A DSO is set to $5\ \text{ms/div}$. One complete waveform cycle occupies 4 horizontal divisions. Find the frequency.

The period is

$$
T = 4 \times 5\ \text{ms} = 20\ \text{ms} = 0.02\ \text{s}
$$

Therefore,

$$
f = \frac{1}{0.02} = 50\ \text{Hz}
$$

So the waveform frequency is **50 Hz**.

#### Table 1.3 Simple waveform classification

| Signal type | Repeats regularly? | Polarity | Example |
|---|---|---|---|
| Steady DC | no time variation | one polarity | dry cell, regulated 5 V supply |
| Pulsating DC | often repeating | one polarity | rectifier output before smoothing |
| AC periodic | yes | changes polarity | 230 V, 50 Hz mains |
| Non-periodic | not necessarily | may vary | transient pulse, switching event |

#### Common misconceptions

- AC does not always mean sinusoidal. A square wave that alternates in polarity is also AC.
- DC does not always mean perfectly flat and constant. A signal may vary with time and still be DC if its polarity does not reverse.
- Frequency and amplitude describe different things. Frequency tells how often the waveform repeats; amplitude tells how large it is.

#### Practical note

Before interpreting any oscilloscope display, check both the vertical scale and the time base. A correct waveform can look misleading if the scale settings are not understood.

### 1.4 Sources

Every practical circuit needs a source of energy. In real life that source may be a battery, a DC supply, a rectifier, a generator, a solar module, or a signal generator. For analysis, however, we use simplified source models.

These models are useful because real sources are never perfect.

#### Ideal and practical voltage sources

An **ideal voltage source** maintains a fixed terminal voltage no matter how much current is drawn from it. Its internal resistance is zero.

No actual battery or power supply behaves exactly this way. A real source always has some internal resistance. So a **practical voltage source** is represented as an ideal voltage source of EMF $\mathcal{E}$ in series with a small internal resistance $r_s$.

If the source delivers a current $I$, the terminal voltage becomes

$$
V = \mathcal{E} - Ir_s \tag{1.18}
$$

Equation (1.18) shows why a battery voltage drops under load. Some of the source voltage is lost inside the source itself [V. K. Mehta and Rohit Mehta, *Principles of Electrical Engineering and Electronics*].

#### Worked Example 1.8

A battery has an EMF of 12 V and internal resistance $0.5\ \Omega$. It supplies 2 A to a load. Find the terminal voltage.

Using Equation (1.18),

$$
V = 12 - (2 \times 0.5) = 12 - 1 = 11\ \text{V}
$$

So the terminal voltage is **11 V**.

If the current increases further, the terminal voltage will fall further. This explains why a weak battery may show a good voltage with no load but perform poorly when connected to a device.

#### Ideal and practical current sources

An **ideal current source** maintains a fixed current regardless of the voltage across its terminals. Its internal resistance is infinite.

In practice, a real current source is modeled as an ideal current source in parallel with a large internal resistance $R_p$ [S. K. Bhattacharya, *Basic Electricals and Electronics*].

Why is the resistance parallel in this model? Because a large parallel resistance allows most of the source current to pass through the load instead of being lost internally.

Current sources are common in electronic circuits, transistor bias networks, current mirrors, and sensor interfaces, even though beginner students meet voltage sources more often at first.

#### Worked Example 1.9

An ideal current source of 10 mA is connected to a load resistor of $500\ \Omega$. Find the load voltage.

The current is fixed:

$$
I = 10\ \text{mA} = 0.01\ \text{A}
$$

So the load voltage is

$$
V = IR = 0.01 \times 500 = 5\ \text{V}
$$

So the load voltage is **5 V**.

This example shows the important idea of a current source model: current is specified first, and the circuit voltage adjusts according to the load.

#### Source transformation

A practical voltage source can be converted into an equivalent practical current source, and vice versa. This process is called **source transformation**.

If a voltage source of value $\mathcal{E}$ is in series with resistance $R$, its equivalent current-source form is a current source $I_s$ in parallel with the same resistance $R$, where

$$
I_s = \frac{\mathcal{E}}{R} \tag{1.19}
$$

Conversely, if a current source $I_s$ is in parallel with a resistance $R$, the equivalent voltage-source form has value

$$
\mathcal{E} = I_sR \tag{1.20}
$$

The resistance value remains unchanged in the transformation.

Source transformation does not mean the physical source has changed. It only means we are using a mathematically equivalent model that may make the circuit easier to analyze.

#### Worked Example 1.10

Transform a 12 V source in series with $6\ \Omega$ into an equivalent current source.

Using Equation (1.19),

$$
I_s = \frac{\mathcal{E}}{R} = \frac{12}{6} = 2\ \text{A}
$$

So the equivalent current-source form is a **2 A current source in parallel with $6\ \Omega$**.

#### Worked Example 1.11

The 12 V source with $6\ \Omega$ series resistance from Example 1.10 is connected to a load of $3\ \Omega$. Find the load current using the voltage-source form.

The total resistance is

$$
R_{total} = 6 + 3 = 9\ \Omega
$$

Therefore, the current is

$$
I = \frac{12}{9} = 1.333\ \text{A}
$$

So the load current is **1.333 A**.

Now verify the same result using the current-source form.

The source is 2 A in parallel with $6\ \Omega$, and the load $3\ \Omega$ is also in parallel. First find the equivalent resistance of the parallel branch:

$$
R_{eq} = \frac{6 \times 3}{6 + 3} = \frac{18}{9} = 2\ \Omega
$$

The voltage across the parallel network is

$$
V = I_sR_{eq} = 2 \times 2 = 4\ \text{V}
$$

Hence the load current is

$$
I_L = \frac{V}{R_L} = \frac{4}{3} = 1.333\ \text{A}
$$

The same answer appears in both forms, as it must.

#### Table 1.4 Ideal and practical source models

| Source type | Internal resistance in ideal case | Practical form | Main behavior |
|---|---:|---|---|
| Voltage source | $0\ \Omega$ | ideal voltage source in series with small resistance | tries to keep voltage constant |
| Current source | infinite | ideal current source in parallel with large resistance | tries to keep current constant |

#### Common misconceptions

- An ideal voltage source is not defined by high voltage. It is defined by constant terminal voltage.
- An ideal current source is not defined by large current. It is defined by constant current.
- Source transformation changes the model used for analysis, not the actual hardware on the table.
- A real source cannot usually maintain its rated value under every condition because internal resistance and other limits exist.

#### Practical note

Many batteries and bench DC supplies are treated first as practical voltage sources. In electronics, transistor circuits and sensor interfaces often use current-source ideas even when no separate current-source symbol is visible in the final circuit diagram.

## Worked Interpretation Exercise

One of the first real component markings a beginner learns to interpret is the resistor colour code. Vishay provides a standard manufacturer reference for this coding system [Vishay, *Color Code and Standard Resistance Series*](https://www.vishay.com/docs/20143/colorcod.pdf).

Suppose a resistor has the following four colour bands:

**Brown - Black - Red - Gold**

Using the Vishay chart:

- Brown gives the first digit: 1
- Black gives the second digit: 0
- Red gives the multiplier: $10^2$
- Gold gives the tolerance: $\pm 5\%$

So the nominal resistance is

$$
R = 10 \times 10^2 = 1000\ \Omega = 1\ \text{k}\Omega
$$

Now interpret the tolerance. A tolerance of $\pm 5\%$ means the actual value can differ by 5 percent above or below the nominal value.

The lower limit is

$$
R_{min} = 1000 - 0.05 \times 1000 = 950\ \Omega
$$

The upper limit is

$$
R_{max} = 1000 + 0.05 \times 1000 = 1050\ \Omega
$$

So a resistor marked Brown-Black-Red-Gold should normally measure somewhere between **950 $\Omega$ and 1050 $\Omega$**.

If a digital multimeter reads, for example, **0.99 k$\Omega$** when the resistor is measured correctly outside the circuit, the reading agrees well with the colour code. This small exercise links component marking, nominal value, tolerance, and actual instrument reading in one practical task.

## How This Matters in Practice

The ideas in this chapter appear in almost every electrical and electronics system.

In household and industrial systems, the language of voltage, current, power, and energy is used for supply ratings, appliance labels, fuse selection, and electricity billing. Without these quantities, even a simple load calculation is not possible.

In transformers and motors, windings behave partly as resistive and partly as inductive elements. The meaning of EMF, current, and stored magnetic energy becomes essential in later study.

In battery charging and solar PV systems, source models matter. A battery or PV panel does not behave like a perfect source under all load conditions. Terminal voltage changes with load, internal effects, and operating condition.

In instrumentation and control circuits, resistors set operating points, capacitors smooth and filter signals, and inductors appear in relays, coils, and power converters. A technician who cannot distinguish DC, pulsating DC, and AC may misread the whole circuit.

In digital systems and automation, clean DC supply, proper current limiting, and correct interpretation of pulse waveforms are basic requirements for reliable operation.

## Chapter Summary

- **EMF** is the energy supplied per unit charge by a source.
- **Potential difference** is the voltage between two points in a circuit.
- **Current** is the rate of flow of charge: $I = \frac{Q}{t}$.
- **Power** is the rate of electrical energy transfer: $P = VI$.
- **Energy** transferred in time $t$ is $W = Pt = VIt$.
- $1\ \text{Wh} = 3600\ \text{J}$ and $1\ \text{kWh} = 3.6 \times 10^6\ \text{J}$.
- A **resistor** opposes current and follows Ohm’s law in ordinary linear operation: $V = IR$.
- Resistor power may be written as $P = VI$, $P = I^2R$, or $P = \frac{V^2}{R}$.
- A **capacitor** stores energy in an electric field: $C = \frac{Q}{V}$ and $W_C = \frac{1}{2}CV^2$.
- An ideal capacitor blocks steady DC after charging is complete, but it responds to changing voltage.
- An **inductor** stores energy in a magnetic field and opposes change in current: $v = L\frac{di}{dt}$ and $W_L = \frac{1}{2}LI^2$.
- A **DC signal** has one polarity. An **AC signal** changes polarity periodically.
- A **periodic waveform** repeats after time period $T$, and its frequency is $f = \frac{1}{T}$.
- An **ideal voltage source** has zero internal resistance; a practical one has small series resistance.
- An **ideal current source** has infinite internal resistance; a practical one has large parallel resistance.
- Source transformation uses the relations $I_s = \frac{\mathcal{E}}{R}$ and $\mathcal{E} = I_sR$.
- Resistor colour code reading is a basic practical skill that links theory with laboratory identification and measurement.

## Further Reading

- [BIPM, *The International System of Units (SI) Brochure*](https://www.bipm.org/en/publications/si-brochure/)  
  Useful for correct SI units, symbols, prefixes, and unit relationships used throughout engineering.

- [Keysight, *Basic Oscilloscope Fundamentals*](https://www.keysight.com/zz/en/assets/7018-01761/application-notes/5989-8064.pdf)  
  A clear practical introduction to waveform display, amplitude, time base, and oscilloscope interpretation.

- [Vishay, *Color Code and Standard Resistance Series*](https://www.vishay.com/docs/20143/colorcod.pdf)  
  A real manufacturer reference for resistor colour bands, resistance values, and tolerance interpretation.

- [S. K. Bhattacharya, *Basic Electricals and Electronics*]  
  A diploma-friendly introductory text covering basic quantities, passive components, and source models at an accessible level.

- [V. K. Mehta and Rohit Mehta, *Principles of Electrical Engineering and Electronics*]  
  A useful foundational text for first-year students, especially for circuit quantities, passive elements, and practical source concepts.
