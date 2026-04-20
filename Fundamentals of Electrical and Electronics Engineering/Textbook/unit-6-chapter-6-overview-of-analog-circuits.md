# Unit 6: Overview of Analog Circuits

## Chapter Opening

The previous chapter introduced semiconductor devices such as diodes and transistors. Those devices showed how solid-state electronics can control current. This chapter takes the next step and introduces one of the most important analog building blocks in electronics: the **operational amplifier**, usually called the **op-amp**.

An op-amp is a very high-gain differential amplifier that becomes useful when we apply **negative feedback** around it. With only a few resistors, the same op-amp can be made to invert a signal, amplify it without inversion, add several signals together, buffer a weak sensor source, or shift a low-level signal into a more useful range. This flexibility is the reason op-amps appear throughout analog electronics, instrumentation, signal conditioning, control circuits, and interface stages.

This chapter stays within the syllabus boundary. We focus on the ideal op-amp idea, the representative **741C** pin configuration, the concept of **virtual ground**, the inverting and non-inverting amplifier, gain calculation, the op-amp adder, and a few typical low-level signal-conditioning uses. The treatment is deeper than a short overview, but it remains diploma-entry and application-oriented.

## Prerequisites Check

- Current, voltage, polarity, and resistor-network ideas from Chapter 1.
- Basic transistor and semiconductor-device familiarity from Chapter 5.
- Ability to use Ohm’s law and solve simple resistor current paths.
- Confidence with algebraic ratio forms such as `$A = V_o / V_i$`.
- Familiarity with the idea that a circuit output may be fed back to an input.

If resistor current paths or polarity signs still feel uncertain, review Chapter 1 before studying inverting and summing op-amp circuits.

## Core Content

### 6.1 Op-Amp Fundamentals

#### Why an op-amp is useful

Suppose a sensor gives a signal of only `50 mV`, but the next stage of the system works much better if it receives about `1 V`. Or suppose one part of a circuit must measure a signal without loading it heavily. Or suppose two low-level analog signals need to be added together before measurement. A transistor can help in some cases, but circuit design becomes easier if we use a ready-made amplifier block whose behavior is predictable.

That block is the op-amp.

An op-amp is an active circuit element designed with characteristics such as very high input resistance, low output resistance, and large differential gain, which make it a very useful building block in many analog circuits [Analog Devices, *ADALM1000 SMU Training Topic 17: Basic Op Amp Configurations*](https://www.analog.com/en/resources/analog-dialogue/studentzone/studentzone-may-2019.html).

#### The op-amp as a differential amplifier

An op-amp has two input terminals:

- **non-inverting input**, usually marked `+`
- **inverting input**, usually marked `−`

and one output terminal.

It responds to the **difference** between the two input voltages. If we call the non-inverting input voltage $V_+$ and the inverting input voltage $V_-$, then the open-loop output idea is

$$
V_o = A_{OL}(V_+ - V_-) \tag{6.1}
$$

where $A_{OL}$ is the **open-loop gain**.

This one equation explains why the op-amp is so powerful and also why it is usually not used in open loop for ordinary linear amplification. If $A_{OL}$ is very large, even a tiny difference between the input terminals can drive the output strongly.

#### Open-loop and closed-loop idea

If an op-amp is used **open loop**, there is no feedback path from output to input. Since the open-loop gain is very large, the output usually saturates near one supply limit or the other even for a very small input difference.

If the op-amp is used with **negative feedback**, part of the output is fed back in such a way that an increase in output tends to reduce the effective input difference. This makes the circuit stable and predictable for linear analog work [Toshiba, *What is the virtual short-circuit (virtual ground) of an op-amp?*](https://toshiba.semicon-storage.com/us/semiconductor/knowledge/faq/linear_opamp/what-is-the-virtual-short-of-an-op-amp.html).

At diploma-entry level, this is one of the most important ideas in the whole chapter:

- open loop gives huge gain but poor linear usefulness,
- closed loop with negative feedback gives controlled, usable gain.

**Image prompt for Figure 6.1:** Create a clean textbook-style diagram comparing an open-loop op-amp and a negative-feedback op-amp. In the left panel, show an op-amp with inputs $V_+$ and $V_-$ and no feedback, with the output saturating high or low for a tiny input difference. In the right panel, show an op-amp with a feedback resistor path from output to the inverting input and indicate stable closed-loop operation. Label non-inverting input, inverting input, output, and negative feedback clearly.

#### Features of an ideal op-amp

The ideal op-amp is a teaching model. Toshiba summarizes the ideal assumptions for op-amp gain analysis as:

1. infinite open-loop gain,
2. infinite input impedance,
3. zero output impedance [Toshiba, *What is the virtual short-circuit (virtual ground) of an op-amp?*](https://toshiba.semicon-storage.com/us/semiconductor/knowledge/faq/linear_opamp/what-is-the-virtual-short-of-an-op-amp.html).

These assumptions are extremely useful because they simplify circuit analysis. Many textbooks also add two more ideal ideas:

- infinite bandwidth,
- zero input current.

We can summarize the most useful ideal properties this way:

#### Table 6.1 Ideal op-amp assumptions

| Ideal property | Meaning in simple words |
|---|---|
| Infinite open-loop gain | Even a very tiny input difference can produce a large output response |
| Infinite input impedance | The op-amp inputs draw no current ideally |
| Zero output impedance | The output behaves like an ideal voltage source |
| Infinite bandwidth | Gain does not fall with frequency in the ideal model |
| Infinite CMRR and infinite PSRR | Common-mode signals and supply changes do not affect the ideal output |

At first-year level, the first three are the most important and are enough for most gain derivations in this chapter.

#### What high input impedance means physically

If the input impedance is very high, the source connected to the input does not need to supply much current into the op-amp input. This means the op-amp does not heavily **load** the source. Analog Devices explains that the high input resistance of an op-amp means very little loading on the source, so the op-amp can act as a buffer [Analog Devices, *ADALM1000 SMU Training Topic 17: Basic Op Amp Configurations*](https://www.analog.com/en/resources/analog-dialogue/studentzone/studentzone-may-2019.html).

This is especially important in signal conditioning. Many sensors do not like to be loaded by a low-resistance circuit.

#### What low output impedance means physically

If the output impedance is low, the op-amp can drive the next stage more easily without the output voltage dropping badly because of internal resistance. This is one reason a voltage follower or buffer is useful even though its gain may be only 1.

#### Real op-amp versus ideal op-amp

Real op-amps are not ideal. They have:

- finite gain,
- finite bandwidth,
- finite slew rate,
- nonzero offset voltage,
- nonzero input bias current,
- limited output swing,
- and limited supply range.

This chapter still uses the ideal model for most calculations because it helps you understand the circuit structure first. Then the representative 741C is used to show how a real op-amp is specified.

#### The 741C as a representative op-amp IC

The syllabus specifically asks for the **741C** pin configuration. The important point is that the 741C should be treated as a representative historical and educational op-amp, not as the only modern choice. TI’s product page describes the LM741 as a single, 44-V, 1-MHz operational amplifier and notes that newer alternatives exist with better characteristics [Texas Instruments, *LM741 product page*](https://www.ti.com/product/LM741).

So the 741C remains useful for learning:

- symbol and pin identification,
- dual-supply operation idea,
- general-purpose op-amp behavior,
- and classic analog-circuit examples.

But in modern practical design, many newer op-amps are preferred for lower power, wider input range, rail-to-rail operation, lower offset, or single-supply use.

#### 741C pin configuration

The TI LM741 datasheet gives the following pin functions for the 8-pin package [Texas Instruments, *LM741 Operational Amplifier datasheet*](https://www.ti.com/lit/gpn/lm741):

#### Table 6.2 LM741C representative pin functions

| Pin number | Function |
|---|---|
| 1 | Offset null |
| 2 | Inverting input |
| 3 | Non-inverting input |
| 4 | Negative supply $V_-$ |
| 5 | Offset null |
| 6 | Output |
| 7 | Positive supply $V_+$ |
| 8 | No connection |

The pinout immediately tells us something important: the op-amp needs supply pins in addition to signal pins. A beginner sometimes looks only at the triangle symbol and forgets that the device must be powered.

**Image prompt for Figure 6.2:** Create a clean textbook-style top-view pin diagram of the LM741C in an 8-pin DIP package. Label pin 1 offset null, pin 2 inverting input, pin 3 non-inverting input, pin 4 negative supply, pin 5 offset null, pin 6 output, pin 7 positive supply, and pin 8 no connection. Include the notch orientation clearly.

#### Typical 741C characteristics students should notice

From the TI LM741 product page and datasheet:

- gain-bandwidth product is typically `1 MHz`,
- slew rate is typically `0.5 V/µs`,
- input offset voltage is a few millivolts,
- typical supply current is about `1.7 mA`,
- LM741C recommended operating temperature range is `0°C to 70°C`,
- recommended supply is typically dual supply around `±15 V`, though the device can operate over a range [Texas Instruments, *LM741 product page*](https://www.ti.com/product/LM741) [Texas Instruments, *LM741 Operational Amplifier datasheet*](https://www.ti.com/lit/gpn/lm741).

At this level, you do not need to master every specification. But you should learn to recognize that a real op-amp is defined by many limits beyond just "gain."

#### Power supply idea for op-amps

The classical 741 is usually shown with a positive and a negative supply, such as `+15 V` and `−15 V`. This allows the output to swing both positive and negative around ground.

Modern op-amps may also work on a single supply, such as `0 V` and `+5 V`. That is very common in sensor and microcontroller circuits. The general op-amp concept remains the same, but biasing and allowable input/output ranges must then be handled carefully.

#### Virtual short and virtual ground

This is one of the most useful concepts in op-amp analysis.

Toshiba defines a **virtual short** as the condition in which the non-inverting and inverting inputs have almost the same voltage when a high-gain op-amp is used with negative feedback [Toshiba, *What is the virtual short-circuit (virtual ground) of an op-amp?*](https://toshiba.semicon-storage.com/us/semiconductor/knowledge/faq/linear_opamp/what-is-the-virtual-short-of-an-op-amp.html).

So under ideal negative-feedback operation:

$$
V_+ \approx V_- \tag{6.2}
$$

This does **not** mean the two inputs are physically connected together. It means the input difference becomes extremely small because the op-amp’s large open-loop gain and feedback force the circuit to that condition.

If one of the inputs is actually connected to ground, and the other input becomes almost equal to it because of the virtual short condition, that other node is called a **virtual ground** [Toshiba, *What is the virtual short-circuit (virtual ground) of an op-amp?*](https://toshiba.semicon-storage.com/us/semiconductor/knowledge/faq/linear_opamp/what-is-the-virtual-short-of-an-op-amp.html).

So for an inverting amplifier with the non-inverting input grounded:

$$
V_+ = 0 \quad \Rightarrow \quad V_- \approx 0
$$

but the inverting node is still not physically tied to ground.

This concept makes gain derivation much easier.

#### Virtual open idea

Because the ideal op-amp has infinite input impedance, no current enters either input terminal:

$$
I_+ = I_- = 0 \tag{6.3}
$$

Students often use the phrase **virtual open** for this input-current idea. Together, the ideal op-amp rules most often used in circuit analysis are:

- input currents are zero,
- input voltages are nearly equal under negative feedback.

Those two rules will now be used repeatedly.

#### Worked Example 6.1

An ideal op-amp with negative feedback has its non-inverting input connected to ground. If the circuit is operating linearly, what voltage may be assumed at the inverting input for first-level analysis?

Under negative feedback, ideal op-amp analysis uses the virtual short:

$$
V_- \approx V_+
$$

Since

$$
V_+ = 0
$$

therefore

$$
V_- \approx 0
$$

So the inverting input is treated as being at **virtual ground**, approximately `0 V`.

#### Common misconceptions

- The 741C is not the only op-amp in modern electronics. It is a representative teaching device.
- Virtual ground is not a physical wire connection to ground.
- High gain alone does not make an op-amp useful; negative feedback is usually needed for controlled analog amplification.
- An op-amp must be powered. The triangle symbol in a schematic does not show all practical details unless the supply pins are understood.

#### Practical note

Whenever you start analyzing an op-amp circuit, first ask:

- is negative feedback present,
- which input is receiving the signal,
- and is one input fixed at ground or a reference voltage?

These three observations usually reveal the basic circuit type immediately.

### 6.2 Basic Op-Amp Configurations

#### Why a few resistor circuits matter so much

The most striking thing about op-amps is that many useful functions come from only a few external resistors. In this section we study the two most important basic forms:

- the **inverting amplifier**
- the **non-inverting amplifier**

If these are understood clearly, later applications such as adders, filters, level shifters, and sensor interfaces become much easier to understand.

#### Inverting amplifier

In an **inverting amplifier**, the signal is applied through an input resistor to the inverting input. The non-inverting input is usually connected to ground or to a reference level. A feedback resistor connects the output back to the inverting input.

TI describes an inverting amplifier circuit as one that inverts the input signal and applies a defined gain set by the resistor network [Texas Instruments, *CIRCUIT060020 Inverting amplifier circuit*](https://www.ti.com/tool/CIRCUIT060020).

**Image prompt for Figure 6.3:** Create a clean textbook-style schematic of an inverting op-amp amplifier using an ideal op-amp. Show input voltage $V_i$ connected through resistor $R_1$ to the inverting input, feedback resistor $R_f$ from output to the inverting input, the non-inverting input grounded, output labeled $V_o$, and dual supplies indicated separately. Label the inverting input node as virtual ground.

Let:

- input resistor = $R_1$
- feedback resistor = $R_f$
- input voltage = $V_i$
- output voltage = $V_o$

Because of virtual ground,

$$
V_- \approx 0
$$

Since no current enters the op-amp input, the current through $R_1$ equals the current through $R_f$.

Current through input resistor:

$$
I_1 = \frac{V_i - 0}{R_1} = \frac{V_i}{R_1}
$$

Current through feedback resistor:

$$
I_f = \frac{0 - V_o}{R_f} = -\frac{V_o}{R_f}
$$

Since $I_1 = I_f$,

$$
\frac{V_i}{R_1} = -\frac{V_o}{R_f}
$$

Therefore,

$$
\boxed{\frac{V_o}{V_i} = -\frac{R_f}{R_1}} \tag{6.4}
$$

So the **voltage gain** of the inverting amplifier is

$$
\boxed{A_v = -\frac{R_f}{R_1}} \tag{6.5}
$$

The negative sign means the output is `180°` out of phase with the input. A positive input change produces a negative output change, and vice versa.

#### Physical meaning of the inverting amplifier

The inverting amplifier does two things at once:

- it changes the signal magnitude according to the resistor ratio,
- it reverses the polarity or phase of the signal.

This circuit is very common when signal inversion is acceptable or desired, and when multiple input signals must later be summed into one node, as in the adder circuit.

#### Input impedance of the inverting amplifier

TI notes that the input signal of an inverting amplifier typically comes from a low-impedance source because the input impedance of this circuit is determined mainly by the input resistor [Texas Instruments, *CIRCUIT060020 Inverting amplifier circuit*](https://www.ti.com/tool/CIRCUIT060020).

At beginner level, this means the source connected to the inverting amplifier "sees" approximately:

$$
Z_{in} \approx R_1
$$

That is different from the non-inverting amplifier, which has much higher input resistance.

#### Worked Example 6.2

An inverting amplifier has $R_1 = 10\ \text{k}\Omega$ and $R_f = 50\ \text{k}\Omega$. Find the voltage gain.

Use Equation (6.5):

$$
A_v = -\frac{R_f}{R_1} = -\frac{50\ \text{k}\Omega}{10\ \text{k}\Omega}
$$

$$
A_v = -5
$$

So the voltage gain is **`−5 V/V`**.

This means the output magnitude is five times the input magnitude, but with inversion.

#### Worked Example 6.3

An inverting amplifier has gain `−4`. If the input signal is `0.3 V`, find the output voltage.

Use:

$$
V_o = A_v V_i
$$

So:

$$
V_o = -4 \times 0.3 = -1.2\ \text{V}
$$

So the output voltage is **`−1.2 V`**.

#### Non-inverting amplifier

In a **non-inverting amplifier**, the input signal is applied directly to the non-inverting input. The inverting input is connected to a feedback divider formed by two resistors.

Analog Devices notes that the non-inverting amplifier has the desirable property of high input resistance, making it useful for buffering nonideal sources while also providing gain greater than one [Analog Devices, *ADALM1000 SMU Training Topic 17: Basic Op Amp Configurations*](https://www.analog.com/en/resources/analog-dialogue/studentzone/studentzone-may-2019.html).

**Image prompt for Figure 6.4:** Create a clean textbook-style schematic of a non-inverting op-amp amplifier using an ideal op-amp. Show input voltage $V_i$ connected to the non-inverting input, resistor $R_1$ from inverting input to ground, feedback resistor $R_f$ from output to the inverting input, and output labeled $V_o$. Indicate the resistor divider at the inverting input clearly.

For the non-inverting amplifier, the inverting input voltage is the divided version of the output:

$$
V_- = V_o \cdot \frac{R_1}{R_1 + R_f}
$$

Using the virtual short under negative feedback:

$$
V_- \approx V_+ = V_i
$$

So:

$$
V_i = V_o \cdot \frac{R_1}{R_1 + R_f}
$$

Rearranging,

$$
V_o = V_i \cdot \frac{R_1 + R_f}{R_1}
$$

Therefore,

$$
\boxed{\frac{V_o}{V_i} = 1 + \frac{R_f}{R_1}} \tag{6.6}
$$

and the voltage gain is

$$
\boxed{A_v = 1 + \frac{R_f}{R_1}} \tag{6.7}
$$

Notice that the gain is positive. So the output stays in phase with the input.

#### Physical meaning of the non-inverting amplifier

This circuit is especially useful when:

- the source should not be loaded much,
- the output should keep the same polarity as the input,
- and a moderate or large gain is required.

Because the input signal is connected directly to the op-amp non-inverting input, the source benefits from the op-amp’s high input resistance.

#### Worked Example 6.4

A non-inverting amplifier has $R_1 = 5\ \text{k}\Omega$ and $R_f = 45\ \text{k}\Omega$. Find the voltage gain.

Using Equation (6.7):

$$
A_v = 1 + \frac{R_f}{R_1}
= 1 + \frac{45}{5}
$$

$$
A_v = 1 + 9 = 10
$$

So the voltage gain is **`+10 V/V`**.

#### Worked Example 6.5

A non-inverting amplifier has gain `+6`. If the input signal is `0.2 V`, find the output voltage.

Use:

$$
V_o = A_v V_i
$$

So:

$$
V_o = 6 \times 0.2 = 1.2\ \text{V}
$$

So the output voltage is **`+1.2 V`**.

#### Inverting and non-inverting amplifiers compared

#### Table 6.3 Comparison of basic amplifier configurations

| Feature | Inverting amplifier | Non-inverting amplifier |
|---|---|---|
| Input terminal used | inverting input via resistor | non-inverting input directly |
| Output phase | inverted | same phase |
| Gain formula | $-R_f/R_1$ | $1 + R_f/R_1$ |
| Input resistance seen by source | approximately $R_1$ | very high |
| Good use | scaling with inversion, summing | buffering and scaling without inversion |

This table is worth understanding deeply because many practical analog circuits are built from these two patterns.

#### Virtual ground revisited in the inverting amplifier

Students often see the inverting-input node labeled `0 V` and mistakenly think it is directly grounded. It is not. It is at approximately zero volts because of negative feedback and the op-amp’s large gain. If the circuit saturates or the feedback conditions fail, the virtual-ground assumption also fails.

So virtual ground is a **working condition**, not a physical connection.

#### Output saturation

Real op-amps cannot produce arbitrarily large output voltage. The output is limited by the supply rails and internal voltage drops. Analog Devices explicitly points out that the output voltage is ultimately limited by the supply voltages, and in many cases the actual limits are smaller because of internal drops [Analog Devices, *ADALM1000 SMU Training Topic 17: Basic Op Amp Configurations*](https://www.analog.com/en/resources/analog-dialogue/studentzone/studentzone-may-2019.html).

So even if the gain formula predicts a certain output, the real circuit may clip or saturate if the required output exceeds the allowed range.

#### Common misconceptions

- The gain formulas apply under normal negative-feedback linear operation, not when the op-amp is saturated.
- In the inverting amplifier, the inverting-input node is at virtual ground only under proper operating conditions.
- A non-inverting amplifier does not have gain equal only to `$R_f/R_1$`; the correct formula includes the `1`.
- The resistor ratio sets the closed-loop gain, not the op-amp’s huge open-loop gain directly.

#### Practical note

If a weak source must not be loaded, the non-inverting amplifier is often the safer first choice. If signal inversion is acceptable and resistor-based summing is needed, the inverting structure is often more convenient.

### 6.3 Op-Amp Applications

#### Why applications grow naturally from the basic forms

Most beginner op-amp applications are only slight variations of the circuits already studied. The adder, subtractor, active filter, comparator interface, buffer, and many sensor-conditioning circuits all grow from the same negative-feedback ideas.

The syllabus asks specifically for:

- **adder using op-amp**
- **typical low-level signal conditioning applications**

So we now study those in a practical but still beginner-friendly way.

#### Summing amplifier or adder

If several input voltages are connected to the inverting input through separate resistors, while feedback is provided from output to that same node, the op-amp can produce an output proportional to the sum of the input currents. This is called a **summing amplifier** or **adder**.

Analog Devices describes the summing amplifier as a basic inverting amplifier with multiple inputs, where the output is a linear sum of the input contributions, each weighted by its resistor ratio [Analog Devices, *ADALM1000 SMU Training Topic 17: Basic Op Amp Configurations*](https://www.analog.com/en/resources/analog-dialogue/studentzone/studentzone-may-2019.html).

**Image prompt for Figure 6.5:** Create a clean textbook-style schematic of an inverting summing amplifier. Show three input voltages $V_1$, $V_2$, and $V_3$ applied through resistors $R_1$, $R_2$, and $R_3$ to the inverting input of an ideal op-amp. Show feedback resistor $R_f$ from output to the inverting input. Show the non-inverting input grounded. Label the inverting node as virtual ground and the output as $V_o$.

Using virtual ground, the current through each input resistor is:

$$
I_1 = \frac{V_1}{R_1}, \quad
I_2 = \frac{V_2}{R_2}, \quad
I_3 = \frac{V_3}{R_3}
$$

Since no current enters the op-amp input, these currents add and flow through the feedback resistor:

$$
I_f = I_1 + I_2 + I_3
$$

The feedback current is also:

$$
I_f = -\frac{V_o}{R_f}
$$

Therefore,

$$
-\frac{V_o}{R_f} = \frac{V_1}{R_1} + \frac{V_2}{R_2} + \frac{V_3}{R_3}
$$

So the general output is:

$$
\boxed{V_o = -R_f\left(\frac{V_1}{R_1} + \frac{V_2}{R_2} + \frac{V_3}{R_3}\right)} \tag{6.8}
$$

If all input resistors are equal, say

$$
R_1 = R_2 = R_3 = R
$$

then

$$
\boxed{V_o = -\frac{R_f}{R}(V_1 + V_2 + V_3)} \tag{6.9}
$$

If also $R_f = R$, then the circuit becomes a simple inverting adder:

$$
\boxed{V_o = -(V_1 + V_2 + V_3)} \tag{6.10}
$$

#### Worked Example 6.6

An op-amp adder has three equal input resistors of `10 kΩ` and a feedback resistor of `10 kΩ`. The input voltages are:

- $V_1 = 0.2\ \text{V}$
- $V_2 = 0.5\ \text{V}$
- $V_3 = 0.1\ \text{V}$

Find the output voltage.

Since all input resistors are equal and $R_f = R$, use Equation (6.10):

$$
V_o = -(V_1 + V_2 + V_3)
$$

So:

$$
V_o = -(0.2 + 0.5 + 0.1) = -0.8\ \text{V}
$$

So the output voltage is **`−0.8 V`**.

#### Weighted adder idea

If the input resistors are not equal, then each signal contributes a different weight to the output. That is useful in:

- mixing signals,
- combining sensor channels,
- creating analog computing functions,
- and digital-to-analog style resistor-weighted circuits.

At this level, you do not need a full analog-computing treatment. It is enough to understand that resistor values set how strongly each input affects the output.

#### Typical low-level signal conditioning

**Signal conditioning** means preparing a signal so that the next stage can use it properly. In practice, op-amps are often used to:

- buffer a weak sensor output,
- amplify a low-level signal,
- shift a signal into a desired range,
- filter unwanted noise together with suitable RC networks,
- combine more than one signal.

TI describes op-amp circuits that translate low-level sensor outputs into ranges suitable for ADC inputs, using inverting or non-inverting amplifier forms with reference levels [Texas Instruments, *CIRCUIT060064*](https://www.ti.com/tool/CIRCUIT060064) [Texas Instruments, *CIRCUIT060019*](https://www.ti.com/tool/CIRCUIT060019).

At syllabus level, the most natural low-level signal-conditioning uses to understand are buffering and scaling.

#### Buffering a weak source

A **buffer** or **voltage follower** has gain approximately equal to 1:

$$
V_o \approx V_i \tag{6.11}
$$

This may look useless at first because it does not increase signal amplitude. But because of high input resistance and low output resistance, it isolates the source from the load.

A sensor that cannot supply much current may be able to feed a buffer successfully. The next stage then receives the same voltage but from a stronger output source.

#### Scaling a small sensor signal

Suppose a temperature sensor, pressure sensor, photodiode conditioner, or bridge output stage gives only a few millivolts or a few hundred millivolts. The signal may be too small for the next measuring or processing stage. An op-amp amplifier can scale it upward.

For example, TI shows practical circuits in which an op-amp translates a sensor output to a more usable range for an ADC [Texas Instruments, *CIRCUIT060064*](https://www.ti.com/tool/CIRCUIT060064) [Texas Instruments, *CIRCUIT060019*](https://www.ti.com/tool/CIRCUIT060019).

At beginner level, the key physical idea is:

- the sensor provides the information,
- the op-amp reshapes the electrical level into a more useful form.

#### Worked Example 6.7

A low-level sensor gives an output of `50 mV`. The next stage works best with about `1.0 V`. Design a simple non-inverting gain value that would scale `50 mV` to `1.0 V`.

Required gain:

$$
A_v = \frac{V_o}{V_i} = \frac{1.0}{0.05} = 20
$$

For a non-inverting amplifier:

$$
A_v = 1 + \frac{R_f}{R_1}
$$

So:

$$
20 = 1 + \frac{R_f}{R_1}
$$

$$
\frac{R_f}{R_1} = 19
$$

One simple resistor choice is:

- $R_1 = 1\ \text{k}\Omega$
- $R_f = 19\ \text{k}\Omega$

So a **non-inverting gain of 20** will scale `50 mV` to `1.0 V`.

#### Why the 741C is only illustrative

The syllabus correctly notes that the 741C is an illustrative example, not the only modern device. This matters in practice because the 741:

- is not rail-to-rail,
- often prefers dual supplies,
- has modest speed,
- and has characteristics that are ordinary compared with many modern op-amps.

TI’s product page even highlights a newer alternative with lower quiescent current and better performance [Texas Instruments, *LM741 product page*](https://www.ti.com/product/LM741).

So the correct learning attitude is:

- understand the 741C well,
- but understand the **general op-amp concept** even more deeply.

#### Common misconceptions

- An adder is not a completely new op-amp theory; it is an extension of the inverting amplifier idea.
- A voltage follower is not pointless. It is valuable because of buffering.
- Signal conditioning is not only "making the signal bigger." It can also mean buffering, shifting, limiting, or preparing the signal for the next stage.
- A real op-amp circuit must respect supply limits, output swing limits, and saturation.

#### Practical note

In a laboratory or field instrument, the op-amp you see near the sensor is very often not doing something mysterious. It is usually buffering, amplifying, adding, or level-shifting a signal so that the rest of the system can use it more reliably.

## Worked Interpretation Exercise

Consider the [TI LM741 datasheet](https://www.ti.com/lit/gpn/lm741) and product page [Texas Instruments, *LM741 Operational Amplifier datasheet*](https://www.ti.com/lit/gpn/lm741) [Texas Instruments, *LM741 product page*](https://www.ti.com/product/LM741).

From the pin-configuration and specification tables, we can read:

- pin 2 = inverting input
- pin 3 = non-inverting input
- pin 4 = negative supply
- pin 6 = output
- pin 7 = positive supply
- recommended LM741C operating temperature range = `0°C to 70°C`
- typical gain-bandwidth product = `1 MHz`
- typical slew rate = `0.5 V/µs`
- typical supply current = about `1.7 mA`

Now interpret these values in a practical way.

First, the pin table tells us the 741 cannot be wired just by knowing the triangle symbol. The physical IC package must be connected correctly. If the supply pins are forgotten, the amplifier will not operate at all.

Second, the presence of both positive and negative supply pins shows the classical dual-supply style of many textbook op-amp circuits. This helps explain why so many introductory examples use `+15 V`, `−15 V`, and ground.

Third, the `1 MHz` gain-bandwidth value tells us the 741 is not a high-speed modern op-amp. It is suitable for learning and for many low-frequency analog tasks, but not for every modern fast-signal application.

Fourth, the `0.5 V/µs` slew rate reminds us that the output cannot change infinitely fast. Even if the ideal model suggests an instantaneous response, the real device has a finite rate of change.

Fifth, the `0°C to 70°C` range associated with the 741C version explains the meaning of the “C” grade in basic educational use. This is one reason the chapter treats the 741C as a representative device, not a universal solution for all environments.

This short interpretation exercise connects textbook ideas with a real op-amp component:

- symbol versus package pinout,
- ideal model versus real specifications,
- and why datasheet reading matters before circuit use.

## How This Matters in Practice

In household and industrial electrical systems, analog circuits often sit between the real world and the control system. A sensor measuring temperature, pressure, current, vibration, or light often produces a small and imperfect signal. An op-amp stage is then used to buffer, amplify, combine, or shift that signal before measurement or control.

In transformers and motors, op-amps may appear in monitoring and protection circuits rather than in the power path itself. They can amplify current-sense voltages, condition tachometer signals, detect overload conditions, or combine feedback signals in control hardware.

In battery charging and solar PV systems, analog circuits help in voltage sensing, current sensing, reference generation, and feedback conditioning. Even when the main power conversion is done by semiconductor switches, op-amps often handle the lower-level analog information that tells the system what to do.

In instrumentation and control circuits, op-amps are everywhere. They are used for strain-gauge interfaces, sensor amplification, filtering, reference scaling, and summing of analog signals. In digital systems and automation, analog circuits often prepare real-world signals so that ADCs, microcontrollers, PLCs, or comparators can interpret them correctly.

## Chapter Summary

- An **op-amp** is a high-gain differential amplifier that becomes very useful when used with negative feedback.
- The two input terminals are the **non-inverting** (`+`) input and the **inverting** (`−`) input.
- Open-loop operation is usually not suitable for ordinary linear amplification because the gain is very large.
- Negative feedback makes the closed-loop behavior controlled and predictable.
- The ideal op-amp assumptions commonly used in beginner analysis are:
- infinite open-loop gain,
- infinite input impedance,
- zero output impedance.
- In a negative-feedback op-amp, the two input voltages are approximately equal: $V_+ \approx V_-$.
- If one input is at ground and the other becomes approximately equal to it under feedback, that node is called **virtual ground**.
- For an ideal op-amp, input currents are approximately zero: $I_+ = I_- = 0$.
- The **LM741C** is a representative op-amp used for teaching, with an 8-pin package and separate supply pins.
- In the **inverting amplifier**, the gain is $A_v = -R_f/R_1$.
- In the **non-inverting amplifier**, the gain is $A_v = 1 + R_f/R_1$.
- The inverting amplifier reverses phase; the non-inverting amplifier keeps the same phase.
- The non-inverting amplifier is especially useful when high input resistance is needed.
- A **summing amplifier** adds several input signals through resistor weighting, usually in an inverting form.
- Op-amp applications often involve **signal conditioning**, which includes buffering, amplification, level shifting, and combining signals.
- A voltage follower has gain approximately 1 but is still useful because it buffers the source.
- Real op-amps have finite bandwidth, finite slew rate, finite output swing, and other limits, so datasheet reading matters.

## Further Reading

1. [Texas Instruments, *LM741 Operational Amplifier datasheet*](https://www.ti.com/lit/gpn/lm741)  
   Useful for the representative 741C pinout, supply pins, and practical electrical limits.

2. [Texas Instruments, *LM741 product page*](https://www.ti.com/product/LM741)  
   Useful for quick specification reading and for seeing how the classic 741 compares with newer op-amps.

3. [Toshiba, *What is the virtual short-circuit (virtual ground) of an op-amp?*](https://toshiba.semicon-storage.com/us/semiconductor/knowledge/faq/linear_opamp/what-is-the-virtual-short-of-an-op-amp.html)  
   Useful for a clear explanation of virtual short and virtual ground in negative-feedback circuits.

4. [Toshiba, *2.5. Virtual short (virtual ground)*](https://toshiba.semicon-storage.com/tw/semiconductor/knowledge/e-learning/basics-of-op-amps/chap2/chap2-6.html)  
   Useful for deriving inverting and non-inverting amplifier gains from the ideal op-amp assumptions.

5. [Analog Devices, *ADALM1000 SMU Training Topic 17: Basic Op Amp Configurations*](https://www.analog.com/en/resources/analog-dialogue/studentzone/studentzone-may-2019.html)  
   Useful for beginner-friendly descriptions of op-amp buffering, inverting and non-inverting amplifiers, and summing-amplifier ideas in practical lab form.
