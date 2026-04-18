# Chapter 4.5: Applications in Renewable-Energy Systems

## Chapter opening

In Chapters 4.1 to 4.4, we built the language of DC-DC conversion step by step. We began with the chopper idea, then studied the major non-isolated converters, then looked at isolated converters and bidirectional power flow. Those chapters answered an important engineering question: what can each converter topology do? This chapter asks a more application-centered question: how do we choose and use those topologies in renewable-energy systems that must deal with variable sources, batteries, and changing operating conditions?

This is where power electronics starts to feel very practical. A solar panel does not behave like an ideal DC source with fixed voltage. Its voltage and current change with sunlight, temperature, and load. A battery charger must not only transfer power but also respect battery-charging limits. An EV or hybrid storage system may need energy to move in one direction at one moment and in the opposite direction later. So the converter is not chosen only because it can step voltage up or down. It is chosen because it must make the source operate well, protect the storage element, and fit the larger system architecture [Mohan, Undeland, Robbins, *Power Electronics: Converters, Applications, and Design*, 3e], [Erickson and Maksimovic, *Fundamentals of Power Electronics*, 2e].

The chapter therefore focuses on three linked ideas named in the syllabus. First, we will understand **maximum power point tracking**, usually shortened to **MPPT**, and see why a solar PV source needs it. Second, we will study two common MPPT methods at algorithm level: **Perturb and Observe** and **Incremental Conductance**. Third, we will connect converter topologies to real applications such as solar PV charging, battery interfaces, and EV power stages. By the end, you should be able to look at a renewable-energy power path and explain not only what converter might be used, but why that converter is a sensible choice.

## Prerequisites check

- You should remember the basic buck, boost, buck-boost, Cuk, SEPIC, and bidirectional buck-boost ideas from Chapters 4.2 to 4.4.
- You should be comfortable with the power relation $P = VI$ and with the idea that voltage and current can vary together.
- You should remember that duty cycle changes the average behavior of a switching converter.
- You should know that a battery is charged with controlled current and voltage rather than by careless direct connection.
- You should have a simple physical picture of a solar PV module as a source whose output depends on sunlight and temperature.

If the operating principles of the buck and boost converters feel uncertain, it is worth revisiting Chapter 4.2 before continuing. MPPT makes much more sense once we are comfortable with how a DC-DC converter changes the operating point seen by a source.

## Core content

### 4.5.1 Maximum Power Point Tracking (MPPT): concept, P-V curve of solar panels, need for MPPT

#### Why a solar panel cannot be treated like an ideal battery

Suppose you connect a solar panel directly to a load. It will certainly deliver some power, but there is no guarantee that it will deliver the **maximum available** power for that sunlight and temperature condition. This is the first key idea of MPPT.

A battery is often modeled, at beginner level, as a source that stays in a moderate voltage range while its current depends on the load. A PV module behaves differently. It has an **I-V characteristic**, meaning that its current and voltage are tied together by a nonlinear curve. If you force the module to operate at one voltage, the current takes the value allowed by that curve. If you force a different voltage, the current changes accordingly. Since power is the product of voltage and current, different operating voltages give different power values [PVPMC, *Array Utilization*], [Esram and Chapman, IEEE Trans. Energy Conversion, 2007].

That is why a solar converter is not only a voltage converter. It is also an operating-point controller.

The basic electrical definition of output power is

$$\boxed{P = VI} \quad \text{(17.1)}$$

where $P$ is power in watts, $V$ is terminal voltage, and $I$ is terminal current.

For a PV source, $I$ is not independent of $V$. Instead, the current depends on the chosen operating voltage, so it is often helpful to think of power as a function of voltage:

$$\boxed{P(V) = V\,I(V)} \quad \text{(17.2)}$$

This means there is usually one special region on the curve where the product $VI$ is largest. That operating point is called the **maximum power point**, or **MPP**.

#### Reading the PV I-V and P-V curves physically

A solar module is commonly described with two related curves:

- the **I-V curve**, which shows current versus voltage
- the **P-V curve**, which shows power versus voltage

Two terms from PV practice appear again and again:

- **short-circuit current**, $I_{SC}$: the current when terminal voltage is essentially zero
- **open-circuit voltage**, $V_{OC}$: the voltage when output current is essentially zero

Between those two extremes lies the useful operating region. At low voltage, current is relatively high but voltage is too small for large power. At very high voltage near $V_{OC}$, the current collapses and power again becomes small. So the power curve rises, reaches a peak, and then falls. The peak occurs at:

- **maximum-power voltage**, $V_{MPP}$
- **maximum-power current**, $I_{MPP}$

and the maximum available power is

$$\boxed{P_{MPP} = V_{MPP}I_{MPP}} \quad \text{(17.3)}$$

This is the quantity MPPT is trying to obtain.

**Image prompt for Figure 17.1:** Create a clean textbook-style engineering figure showing the I-V and P-V characteristics of a solar PV module under one irradiance condition. Use two aligned plots versus module voltage. In the upper plot, show current staying nearly flat at first and then dropping steeply near open-circuit voltage. Mark $I_{SC}$, $V_{OC}$, and the operating point at maximum power. In the lower plot, show power rising from zero, reaching a clear peak at $V_{MPP}$, and then falling back to zero at $V_{OC}$. Label $V_{MPP}$, $I_{MPP}$, and $P_{MPP}$. Use monochrome textbook style with axes, units, and clean annotations.

#### A numerical picture before the formal discussion

Let us use an illustrative PV-module example. Imagine that under one sunlight condition a module can produce the approximate values in Table 17.1.

Table 17.1: Illustrative PV operating points under one fixed irradiance and temperature

| Module voltage $V$ | Module current $I$ | Power $P = VI$ |
| --- | --- | --- |
| $10 \text{ V}$ | $5.8 \text{ A}$ | $58 \text{ W}$ |
| $14 \text{ V}$ | $5.7 \text{ A}$ | $79.8 \text{ W}$ |
| $18 \text{ V}$ | $5.0 \text{ A}$ | $90 \text{ W}$ |
| $20 \text{ V}$ | $4.3 \text{ A}$ | $86 \text{ W}$ |
| $22 \text{ V}$ | $2.0 \text{ A}$ | $44 \text{ W}$ |

Here the largest power is about $90 \text{ W}$, occurring near $18 \text{ V}$. So in this condition:

- $V_{MPP} \approx 18 \text{ V}$
- $I_{MPP} \approx 5 \text{ A}$
- $P_{MPP} \approx 90 \text{ W}$

Now imagine that the module is directly connected to a battery that holds the module near $14 \text{ V}$. The module still works, but it now delivers only about $79.8 \text{ W}$ instead of $90 \text{ W}$. The missing power is not a fault in the panel. It is a mismatch between the panel's best operating point and the voltage imposed by the rest of the circuit.

This is the practical motivation for MPPT.

#### Why the maximum power point moves

The MPP is not fixed forever. It shifts because the PV source is affected by environmental conditions.

When **irradiance** increases, the available current generally rises, so the power capability also rises. When **cell temperature** increases, the module voltage generally tends to reduce, which shifts the best operating point [PVPMC, *Point-value models*], [Esram and Chapman, IEEE Trans. Energy Conversion, 2007].

For a beginner, the safe takeaway is:

- more sunlight usually means more current and more available power
- higher temperature usually tends to reduce the voltage at which the module operates best

So a fixed operating voltage is rarely optimal all day long. Morning, noon, cloud passage, and hot rooftop conditions can all move the MPP.

#### What MPPT really does

**Maximum Power Point Tracking** is the control process that keeps the PV source operating near the point where it can deliver maximum power for the present conditions [PVPMC, *Array Utilization*].

This does not mean the controller somehow creates extra solar energy. It means the controller adjusts the electrical operating point so the available solar power is extracted more effectively.

A very important sentence from Sandia's PV Performance Modeling Collaborative states that to harvest power from a PV system, the voltage must be adjusted to maximize the power, and that this MPPT function is typically performed by the inverter or a DC-DC converter [PVPMC, *Array Utilization*]. That sentence connects perfectly with our DC-DC converter study. The converter is the actuator; the MPPT algorithm is the decision-maker.

#### How the converter helps the PV source

Let us place a DC-DC converter between the PV module and a load or battery. By changing duty cycle, the converter changes the relationship between its input side and output side. That means the PV terminal voltage and current can be shifted even while the load or battery on the other side remains the same.

So the MPPT controller does not usually command the sun, the panel, or the battery directly. Instead, it commands the converter's duty ratio or reference. The converter then causes the PV module to move to a different point on its I-V curve.

This is why a direct PV-to-battery connection is often electrically simple but energetically limited. It gives the panel very little freedom to sit at its best operating point.

#### A simple renewable-energy example

Consider a small rooftop solar module charging a nominal $12 \text{ V}$ battery through a converter. Under one condition, the module's MPP is near $18 \text{ V}$ and $5 \text{ A}$, so

$$P_{MPP} = 18 \times 5 = 90 \text{ W}.$$

If an ideal buck converter is used to charge a $12 \text{ V}$ battery from that MPP power, the battery-side current would be approximately

$$I_{bat} \approx \frac{90}{12} = 7.5 \text{ A}.$$

If the same panel were instead forced to operate at $14 \text{ V}$ and about $5.7 \text{ A}$, the available power would be only about

$$14 \times 5.7 = 79.8 \text{ W},$$

and the ideal battery-side current would fall to

$$\frac{79.8}{12} \approx 6.65 \text{ A}.$$

The difference is not trivial. Over long sunshine hours, such differences matter greatly in energy harvest.

#### Common misconceptions

One misconception is that the maximum power point is the same as the highest voltage or highest current point. It is not. Maximum power is the point where the product $VI$ is maximum.

Another misconception is that MPPT always means a boost converter. It does not. MPPT is a control function. A buck, boost, buck-boost, SEPIC, or inverter stage may implement it, depending on the system.

A third misconception is that once $V_{MPP}$ is known from a datasheet, the problem is solved forever. Real PV operating conditions change continuously, so the best operating voltage also changes.

Renewable-energy relevance: MPPT is fundamental in rooftop solar charge controllers, string inverters, DC-coupled battery systems, solar water-pumping controllers, telecom solar backup units, and portable solar chargers. In all of them, the goal is the same: make the PV source operate near its best power-producing point rather than letting the downstream load choose that point accidentally [PVPMC, *Array Utilization*], [TI, BQ24650 product page].

### 4.5.2 Overview of MPPT techniques: Perturb & Observe (P&O) and Incremental Conductance

#### Why an algorithm is needed

Knowing that an MPP exists is not yet the same as finding it in real time. The controller must observe electrical quantities, decide whether the operating point should move left or right on the P-V curve, and then update the converter command.

At beginner level, we can think of the MPPT loop as having three jobs:

1. measure PV voltage and current
2. estimate whether the present operating point is before or after the MPP
3. change the converter command so the operating point moves in the helpful direction

The two most widely taught methods are **Perturb and Observe**, usually called **P&O**, and **Incremental Conductance** [Esram and Chapman, IEEE Trans. Energy Conversion, 2007].

**Image prompt for Figure 17.2:** Create a clean textbook-style block diagram of an MPPT-controlled PV power stage. Show a solar PV module feeding a DC-DC converter, then a battery or DC bus load. Add sensors measuring PV voltage and PV current, an MPPT controller block, and a PWM block driving the converter switch. Label the controller outputs as duty ratio or voltage reference. Add a small inset note that the converter shifts the PV operating point on the I-V curve. Use monochrome textbook style.

#### Perturb and Observe: the hill-climbing idea

The physical intuition of **Perturb and Observe** is very friendly. Imagine you are climbing a hill in fog and want to reach the top. You take a small step, then check whether you moved upward or downward. If the height increased, continue in the same direction. If the height decreased, reverse direction. MPPT uses similar logic on the power curve.

In P&O, the controller makes a small change in operating voltage, current reference, or duty ratio. That small deliberate change is the **perturbation**. It then measures the new power. That measurement is the **observation**.

If the power increased after the perturbation, the controller continues stepping in the same direction. If the power decreased, it reverses the direction of the perturbation [Esram and Chapman, IEEE Trans. Energy Conversion, 2007].

#### A short P&O example

Suppose a controller observes the following sequence:

- Sample 1: $V = 29 \text{ V}$, $I = 6.0 \text{ A}$, so $P = 174 \text{ W}$
- Sample 2: after a small increase in voltage, $V = 30 \text{ V}$, $I = 6.1 \text{ A}$, so $P = 183 \text{ W}$

The power increased, so the controller infers that moving to higher voltage was helpful. It perturbs further in the same direction.

Now suppose the next sample becomes:

- Sample 3: $V = 31 \text{ V}$, $I = 6.15 \text{ A}$, so $P = 190.65 \text{ W}$

Power increased again, so the controller keeps going.

But now suppose:

- Sample 4: $V = 32 \text{ V}$, $I = 5.85 \text{ A}$, so $P = 187.2 \text{ W}$

Power has fallen. So the previous perturbation moved the operating point away from the peak. The controller now reverses direction.

This is very intuitive. The controller does not need an exact mathematical model of the PV module. It only needs measurements and a simple rule.

#### Why P&O never sits perfectly still

P&O is simple, but it has an important limitation. Near the MPP, the controller usually continues to perturb slightly, so the operating point tends to oscillate around the peak rather than staying exactly at it. That means a small amount of power loss is normal.

There is a tradeoff:

- a larger perturbation step reaches the neighborhood of the MPP more quickly but causes more oscillation
- a smaller perturbation step reduces oscillation but can make the tracking slower

This tradeoff is one reason why P&O is easy to understand but not always the best performer under rapidly changing irradiance [Esram and Chapman, IEEE Trans. Energy Conversion, 2007].

#### Incremental Conductance: using the slope of the power curve

The **Incremental Conductance** method begins from a slightly more analytical idea. At the maximum power point, the power curve has zero slope with respect to voltage.

So at the MPP,

$$\boxed{\frac{dP}{dV} = 0} \quad \text{(17.4)}$$

Starting from Equation (17.2), where $P = VI$, differentiate with respect to $V$:

$$\frac{dP}{dV} = I + V\frac{dI}{dV} \quad \text{(17.5)}$$

At the MPP, combine Equations (17.4) and (17.5):

$$I + V\frac{dI}{dV} = 0$$

Therefore,

$$\boxed{\frac{dI}{dV} = -\frac{I}{V}} \quad \text{(17.6)}$$

Equation (17.6) is the central idea of incremental conductance MPPT.

Here:

- $\dfrac{dI}{dV}$ is the **incremental conductance**, meaning the slope of the I-V curve at the present point
- $-\dfrac{I}{V}$ is the negative of the **instantaneous conductance**

The controller compares these two quantities.

#### How the slope tells us where we are

Using Equation (17.5), we can divide the curve into three regions:

- left of the MPP: $\dfrac{dP}{dV} > 0$
- at the MPP: $\dfrac{dP}{dV} = 0$
- right of the MPP: $\dfrac{dP}{dV} < 0$

Therefore, in conductance form:

$$\boxed{\frac{dI}{dV} > -\frac{I}{V} \Rightarrow \text{left of MPP}} \quad \text{(17.7)}$$

$$\boxed{\frac{dI}{dV} = -\frac{I}{V} \Rightarrow \text{at MPP}} \quad \text{(17.8)}$$

$$\boxed{\frac{dI}{dV} < -\frac{I}{V} \Rightarrow \text{right of MPP}} \quad \text{(17.9)}$$

In digital control, the derivative is approximated with measured changes:

$$\boxed{\frac{dI}{dV} \approx \frac{\Delta I}{\Delta V}} \quad \text{(17.10)}$$

where $\Delta I$ and $\Delta V$ are small measured changes between sampling instants.

#### A numerical incremental-conductance example

Suppose at one instant:

- $V = 30 \text{ V}$
- $I = 6 \text{ A}$

Then

$$-\frac{I}{V} = -\frac{6}{30} = -0.2 \text{ A/V}.$$

Now suppose a small change in operating point gives:

- $\Delta V = +1 \text{ V}$
- $\Delta I = -0.1 \text{ A}$

Then

$$\frac{\Delta I}{\Delta V} = \frac{-0.1}{1} = -0.1 \text{ A/V}.$$

Comparing the two,

$$-0.1 > -0.2.$$

So by Equation (17.7), the operating point is to the left of the MPP. The controller should continue moving toward higher voltage.

Now imagine instead that

- $\Delta V = +1 \text{ V}$
- $\Delta I = -0.35 \text{ A}$

Then

$$\frac{\Delta I}{\Delta V} = -0.35 \text{ A/V}.$$

Since

$$-0.35 < -0.2,$$

the operating point is to the right of the MPP, so the controller should move toward lower voltage.

#### Comparing the two methods

Table 17.2 summarizes the beginner-level difference between P&O and incremental conductance.

Table 17.2: Conceptual comparison of two common MPPT methods

| Method | Core idea | Main strength | Main limitation |
| --- | --- | --- | --- |
| Perturb and Observe | Make a small change and see whether power rises or falls | Simple, widely used, low conceptual complexity | Tends to oscillate around MPP and can be confused by rapidly changing irradiance |
| Incremental Conductance | Use the slope condition $\dfrac{dP}{dV}=0$ or $\dfrac{dI}{dV} = -\dfrac{I}{V}$ | Better ability to identify the true MPP direction under changing conditions | More measurement and computation effort than basic P&O |

This does not mean one method is always superior in every product. Practical choices depend on cost, controller capability, sampling quality, required response, and how aggressively the system must react to changing weather [Esram and Chapman, IEEE Trans. Energy Conversion, 2007].

#### Where the converter topology enters the algorithm

The MPPT algorithm itself does not replace the converter topology. The algorithm still needs a power stage.

For example:

- a **buck** converter may implement MPPT when PV voltage is above the battery or bus voltage
- a **boost** converter may implement MPPT when PV voltage must be raised
- a **buck-boost** or **SEPIC** stage may implement MPPT when the PV voltage may move above and below the required output
- an inverter front end may perform MPPT directly in grid-tied systems [PVPMC, *Array Utilization*]

So when engineers say "the system has MPPT," they are usually describing a control function built around an actual switching converter.

#### Common misconceptions

One misconception is that P&O directly measures the maximum power point itself. It does not. It infers the direction of movement from repeated perturbations and measurements.

Another misconception is that incremental conductance requires advanced semiconductor physics. It does not. At chapter level, it is simply a way of using the slope of the power curve more explicitly.

A third misconception is that MPPT and battery charging are identical tasks. They are related but different. MPPT tries to make the PV source operate near its best power point. Battery charging tries to keep battery current and voltage within safe limits. A practical solar charger must often do both, and whichever limit is more restrictive at a given moment may dominate.

Renewable-energy relevance: the choice between P&O and incremental conductance appears in solar charge controllers, portable solar systems, PV-fed telecom backup units, and DC-coupled PV storage systems. Under slowly varying sunlight, simple P&O may be fully adequate. Under faster environmental change, designers often prefer more deliberate slope-based tracking behavior [Esram and Chapman, IEEE Trans. Energy Conversion, 2007], [TI, BQ24650 product page].

### 4.5.3 Selection of DC-DC converter topology for solar PV, battery charging and EV drivetrain applications

#### Why topology selection matters

By now we know several converter families. The beginner may reasonably ask: if all of them transfer DC power efficiently, how do we decide which one to use?

The answer is that topology selection begins with system questions, not with favorite circuits. We ask:

- Is the source voltage usually above, below, or sometimes above and sometimes below the required output?
- Is power flow one-way or bidirectional?
- Is galvanic isolation required for safety, grounding, or standards compliance?
- Does the source prefer smooth input current?
- Does the load require the same polarity as the source?
- Are size, efficiency, cost, or controllability the main priorities?

Those questions matter more than memorizing topology names.

#### Selecting a converter for solar PV applications

##### Case 1: PV voltage is reliably above battery voltage

If the PV source operates at a voltage that remains above the battery or DC-bus voltage, a **buck converter** is often the simplest and most natural choice.

This is common in small and medium solar battery chargers. For example, Texas Instruments describes the BQ24650 as a solar battery charge controller with MPPT implemented by input-voltage regulation, and it is specifically a synchronous **buck** controller [TI, BQ24650 product page]. That makes good engineering sense. If the panel voltage is already above the battery voltage, stepping down is enough.

A simple example is a module whose MPP is near $18 \text{ V}$ charging a nominal $12 \text{ V}$ battery. In that situation, a buck stage can let the PV side remain near $18 \text{ V}$ while the battery sees the lower charging voltage it requires.

##### Case 2: PV voltage is below the required DC bus

If the PV source voltage is below the target output voltage, a **boost converter** is the natural first candidate.

Suppose a small PV source operates near $30 \text{ V}$ but must feed a regulated $48 \text{ V}$ DC bus. Then the converter must step the voltage up. A boost converter can perform that task while the controller adjusts duty cycle to keep the PV module near its MPP [Mohan, Undeland, Robbins, *Power Electronics: Converters, Applications, and Design*, 3e], [Erickson and Maksimovic, *Fundamentals of Power Electronics*, 2e].

This arrangement is common whenever a relatively low PV voltage must support a higher DC-link voltage for a later inverter or storage interface.

##### Case 3: PV voltage may move above and below the desired output

This is where **buck-boost**-family converters become attractive. If the source may be above the target at one moment and below it at another, a converter that can both step down and step up is much more flexible.

Two beginner-friendly non-isolated options from Chapter 4.2 are:

- the **buck-boost** converter, if output polarity inversion is acceptable
- the **SEPIC** converter, if non-inverted output polarity is desired

A SEPIC can be especially attractive in PV work because it allows step-up or step-down action without output polarity inversion, and its input current can be smoother than that of some simpler alternatives [Erickson and Maksimovic, *Fundamentals of Power Electronics*, 2e], [Mohan, Undeland, Robbins, *Power Electronics: Converters, Applications, and Design*, 3e].

This matters in systems where the PV voltage crosses above and below the battery or regulated bus over the day, temperature range, or module-configuration range.

##### Case 4: PV plus battery storage on a shared DC bus

Once a battery is added, the selection problem can change completely. If energy must flow from PV to battery during charging and from battery back to the bus during support mode, a **bidirectional buck-boost** stage often becomes appropriate, as we saw in Chapter 4.4.

If safety or grounding requires isolation, then the appropriate answer may move toward the isolated converter families of Chapter 4.3 rather than remaining non-isolated.

#### Selecting a converter for battery-charging systems

Battery charging is not determined only by source and battery voltages. It is also shaped by charging method. Most rechargeable batteries are charged with some form of **constant-current / constant-voltage** behavior, often shortened to **CC-CV**.

At beginner level, the safe interpretation is:

- in the earlier charging stage, current is deliberately limited
- later, voltage is deliberately limited

The converter must therefore do two jobs:

1. match the source side properly
2. meet the battery-side charging requirement

If the source is a solar panel and its voltage is above the battery voltage, a buck solar charger is often a good fit. If the source voltage may be above or below the battery voltage, a buck-boost charger becomes more attractive. Texas Instruments describes the BQ25756 as a bidirectional buck-boost charge controller with MPPT for solar charging, which is exactly the sort of product one expects when voltage relationships and power-flow needs are wider and less predictable [TI, BQ25756 product page].

If the source is isolated mains-derived DC, safety or regulatory design may push the engineer toward an isolated charger rather than a non-isolated one. That is why real charger design cannot be reduced to only the voltage-gain equation.

#### Selecting a converter for EV and electrified transport applications

The phrase **EV drivetrain** can mean several different power paths, so we should separate them carefully.

The main traction energy path in an EV usually involves:

- the high-voltage battery
- the traction inverter
- the motor

Regenerative braking energy normally returns through the motor and inverter path rather than through a small auxiliary DC-DC converter. That is an important correction to a common oversimplification.

However, EVs and hybrid vehicles still use DC-DC converters extensively:

- to connect a high-voltage battery to a low-voltage auxiliary bus
- to link 48 V and 12 V boardnets
- to manage storage subsystems
- to support backup and transient power exchange

For a **48 V / 12 V dual-battery system**, Analog Devices describes the LTC3871 as a bidirectional buck or boost controller intended for automotive dual-battery systems [Analog Devices, LTC3871 product page]. That tells us something important about topology selection: when two positive-voltage buses must exchange power in either direction, a bidirectional buck-boost approach is very natural.

For a **high-voltage traction battery to 12 V auxiliary rail**, isolation is often required in real vehicle platforms, so an isolated DC-DC converter family is common. In other words, the electrical function may look like step-down conversion, but the real design choice is driven not only by voltage ratio but also by safety isolation.

#### A topology-selection table

Table 17.3 collects the main application logic in one place.

Table 17.3: First-pass topology selection for common renewable-energy and electrified applications

| Application situation | Typical voltage relation | Power-flow direction | First topology to consider | Why it fits |
| --- | --- | --- | --- | --- |
| Small PV module charging a lower-voltage battery | $V_{PV} > V_{bat}$ most of the time | One-way | Buck | Simple step-down action while holding PV near MPP |
| PV source feeding a higher-voltage DC bus | $V_{PV} < V_{bus}$ | One-way | Boost | Raises PV voltage to the required bus level |
| PV source whose operating voltage may be above or below target output | Variable relative to output | One-way | Buck-boost or SEPIC | Handles both step-up and step-down cases |
| PV plus battery on a common DC bus | Variable | Two-way | Bidirectional buck-boost | Supports charging and discharging |
| Solar charger with wide source and battery range | Variable | Usually one-way, sometimes two-way | Buck-boost | Wide voltage flexibility; MPPT can still be implemented |
| 48 V / 12 V EV auxiliary system | One bus above the other | Two-way | Bidirectional buck-boost | Supports power exchange between boardnets |
| High-voltage battery to low-voltage auxiliary rail with safety isolation need | Usually step-down | Often one-way | Isolated DC-DC converter | Electrical isolation dominates the choice |

#### A compact decision process

A beginner-friendly selection process looks like this:

1. Decide whether power flow is one-way or bidirectional.
2. Decide whether isolation is mandatory.
3. Compare the source-voltage range with the required output-voltage range.
4. Check whether output polarity must remain non-inverted.
5. Consider whether the source prefers smoother input current, as PV sources often do.
6. Only then compare finer details such as efficiency, switch stress, and component count.

This process is not fancy, but it prevents many bad first choices.

#### Common misconceptions

One misconception is that the "best" topology is the one with the highest theoretical efficiency in a table. In practice, the best topology is the one that fits the real voltage range, power-flow direction, safety needs, and control task.

Another misconception is that MPPT determines topology automatically. It does not. MPPT tells the converter where the PV source should operate. The topology determines what electrical relationships are possible.

A third misconception is that EV regenerative braking automatically means a bidirectional DC-DC converter in the main traction path. The principal regenerative path is usually through the motor drive inverter. Bidirectional DC-DC converters are still important in EVs, but usually in battery-interface or auxiliary-bus roles.

Renewable-energy relevance: topology selection directly affects energy harvest, battery life, safety architecture, and cost. In Indian and South-Asian settings, this appears in rooftop PV battery chargers, rural backup systems, telecom solar supplies, e-rickshaw and light-EV auxiliary buses, and mixed solar-storage DC systems where the voltage range is rarely fixed for the whole day [TI, BQ24650 product page], [TI, BQ25756 product page], [Analog Devices, LTC3871 product page].

## Worked interpretation exercise

### Reading real product pages to infer topology choice

This chapter is especially well served by comparing real commercial devices, because topology selection is one of the chapter's main goals. We will read three product pages and translate their feature lists into textbook reasoning.

The first artifact is the [TI BQ24650 product page](https://www.ti.com/product/BQ24650). TI describes it as a solar battery charge controller with **Maximum Power Point Tracking capability by input voltage regulation** and specifically as a **600-kHz synchronous buck controller** [TI, BQ24650 product page].

The second artifact is the [TI BQ25756 product page](https://www.ti.com/product/BQ25756). TI describes it as a **70-V bidirectional buck-boost charge controller with MPPT**, with **automatic MPPT for solar charging** and **bidirectional converter operation** [TI, BQ25756 product page].

The third artifact is the [Analog Devices LTC3871 product page](https://www.analog.com/en/products/ltc3871.html). ADI describes it as a **bidirectional buck or boost controller** intended for **48V/12V automotive dual battery systems** [Analog Devices, LTC3871 product page].

Let us now interpret these artifacts with the chapter concepts.

Table 17.4: Interpreting real product pages using topology-selection logic

| Product-page statement | What it tells us | Chapter interpretation |
| --- | --- | --- |
| BQ24650: solar charger with MPPT by input-voltage regulation | The source is expected to be a PV panel and the controller deliberately regulates PV-side voltage | MPPT is being done by a DC-DC converter |
| BQ24650: synchronous buck controller | Output voltage is expected to be lower than the useful PV operating voltage | Good fit for PV charging a lower-voltage battery |
| BQ25756: bidirectional buck-boost charge controller | Power may move in either direction and voltage relation may vary | Suitable when source/battery range is wider and charging/discharging both matter |
| BQ25756: automatic MPPT for solar charging | The same converter family can perform PV-side MPPT while also acting as a charger | MPPT is a control function layered onto the chosen topology |
| LTC3871: bidirectional buck or boost for 48V/12V automotive systems | Two DC buses of different voltage must exchange power | Natural use case for bidirectional buck-boost logic |

Now let us reason one step further.

Why is the BQ24650 a buck device rather than a boost device? Because it is intended for cases where the PV input is above the battery charging voltage. In such a system, a step-down stage is the simplest answer.

Why does the BQ25756 move to buck-boost and bidirectional language? Because the application space is broader. The input and battery ranges are both wide, solar MPPT is present, and reverse power flow is supported. That combination tells us the designer expects varying voltage relationships and more flexible power movement.

Why does the LTC3871 emphasize 48 V and 12 V dual-battery systems? Because that is a classic situation in which one bus may support the other in either direction, depending on operating condition. The electrical problem is not just regulation. It is managed energy exchange.

This comparison is useful because it shows that product literature often hides textbook ideas inside practical language. A manufacturer may not say, "choose this because the source sometimes lies above and sometimes below the target while power may reverse." Instead it says "buck," "buck-boost," "bidirectional," or "48V/12V dual-battery." Our task as engineers is to read those phrases and reconstruct the system logic behind them.

## How this matters in renewable-energy systems

This chapter sits very close to real renewable-energy practice. In a rooftop PV system, MPPT is what helps the array produce strong power through changing sunlight and roof temperature. In a solar battery charger, topology selection decides whether the charger can still operate well when panel voltage and battery voltage move relative to one another. In a wind or hybrid DC system, the same thinking appears when storage must support a shared bus. In EV and battery-backed systems, bidirectional DC-DC stages help different voltage domains exchange energy in a controlled way.

The larger lesson is that renewable-energy power electronics is not only about conversion efficiency. It is about matching source behavior, storage behavior, and system requirements. MPPT tells us how to extract available PV power. Converter selection tells us what electrical behavior is even possible. When those two decisions are made well, the system harvests more energy, charges storage more intelligently, and behaves more reliably in the field.

## Chapter summary

- A **PV module** has a nonlinear I-V characteristic, so the power it delivers depends strongly on operating voltage.
- The basic power relation is $P = VI$.
- The **maximum power point** is the operating point where the product $VI$ is largest.
- The main PV terms are **short-circuit current** $I_{SC}$, **open-circuit voltage** $V_{OC}$, **maximum-power voltage** $V_{MPP}$, and **maximum-power current** $I_{MPP}$.
- The maximum available power is $P_{MPP} = V_{MPP}I_{MPP}$.
- The MPP changes with irradiance and temperature, so a fixed operating voltage is rarely optimal all day.
- **MPPT** is the control process that keeps the PV source near its maximum power point for present conditions.
- In practice, MPPT is often performed by a DC-DC converter or inverter stage [PVPMC, *Array Utilization*].
- **Perturb and Observe (P&O)** changes the operating point slightly and checks whether power increases or decreases.
- P&O is simple and widely used, but it tends to oscillate around the MPP.
- **Incremental Conductance** uses the slope condition $\dfrac{dP}{dV}=0$ at the MPP.
- Starting from $P = VI$, the slope relation becomes $\dfrac{dP}{dV} = I + V\dfrac{dI}{dV}$.
- At the MPP, $\dfrac{dI}{dV} = -\dfrac{I}{V}$.
- A **buck converter** is often a good choice when PV voltage is above battery voltage.
- A **boost converter** is often used when PV voltage must be raised to a higher DC bus.
- A **buck-boost** or **SEPIC** stage is helpful when the source voltage may lie above or below the required output.
- A **bidirectional buck-boost** stage is a strong candidate when a battery must both charge and discharge into a DC bus.
- Topology selection depends on voltage range, direction of power flow, isolation need, polarity, current-ripple preference, and application context.
- Product pages such as TI's BQ24650 and BQ25756 and ADI's LTC3871 show how textbook topology choices appear in real solar-charging and dual-battery systems.

## Further reading

1. Ned Mohan, Tore M. Undeland, and William P. Robbins, *Power Electronics: Converters, Applications, and Design*, 3rd ed.  
   A dependable textbook source for converter topology choice, PV interface intuition, and the broader converter-application viewpoint.

2. Robert W. Erickson and Dragan Maksimovic, *Fundamentals of Power Electronics*, 2nd ed.  
   Especially useful for understanding non-isolated converter families, CCM behavior, and why some topologies suit variable source conditions better than others.

3. Trishan Esram and Patrick L. Chapman, "Comparison of Photovoltaic Array Maximum Power Point Tracking Techniques," *IEEE Transactions on Energy Conversion*, vol. 22, no. 2, 2007.  
   A classic reference for the logic, strengths, and limitations of common MPPT methods including P&O and incremental conductance.

4. [PV Performance Modeling Collaborative (Sandia), "Array Utilization"](https://pvpmc.sandia.gov/modeling-guide/3-dc-array-iv/array-utilization/) and [PVPMC, "Point-value models"](https://pvpmc.sandia.gov/modeling-guide/2-dc-module-iv/point-value-models/).  
   Helpful official educational references for the changing PV operating point, the meaning of the MPP, and the role of MPPT in real PV systems.

5. [Texas Instruments, BQ24650 product page](https://www.ti.com/product/BQ24650), [Texas Instruments, BQ25756 product page](https://www.ti.com/product/BQ25756), and [Analog Devices, LTC3871 product page](https://www.analog.com/en/products/ltc3871.html).  
   These real product pages are valuable for seeing how buck, buck-boost, MPPT, and bidirectional power-flow concepts appear in commercial solar-charging and 48 V/12 V battery-interface hardware.
