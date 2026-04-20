# Chapter 4.5: Applications in Renewable-Energy Systems

## Chapter opening

Chapters 4.1 to 4.4 introduced the principal DC-DC converter families and the electrical tasks they perform. This chapter shifts from topology description to application choice. Renewable-energy systems do not operate from fixed, ideal sources; they must accommodate solar modules whose operating point changes with irradiance and temperature, batteries that require controlled charging, and storage systems in which power may flow in either direction.

Three topics organize the discussion. The first is **maximum power point tracking** (**MPPT**) for photovoltaic sources. The second is the logic of two common MPPT methods, **Perturb and Observe** and **Incremental Conductance**. The third is the selection of converter topologies for solar PV interfaces, battery chargers, and EV-related DC power paths. The goal is not only to identify which converter can step voltage up or down, but to explain why a particular topology fits a particular renewable-energy application [Mohan, Undeland, Robbins, *Power Electronics: Converters, Applications, and Design*, 3e], [Erickson and Maksimovic, *Fundamentals of Power Electronics*, 2e].

## Prerequisites check

- Basic operation of buck, boost, buck-boost, Cuk, SEPIC, and bidirectional buck-boost converters from Chapters 4.2 to 4.4
- The power relation $P = VI$
- The effect of duty cycle on the average behavior of a switching converter
- The idea that battery charging requires controlled current and voltage
- A simple physical picture of a PV module as a source whose output depends on sunlight and temperature

If the operating principles of buck and boost converters are still uncertain, Chapter 4.2 should be reviewed before proceeding. MPPT is easier to understand once the source-side effect of duty-cycle control is clear.

## Core content

### 4.5.1 Maximum Power Point Tracking (MPPT): concept, P-V curve of solar panels, need for MPPT

#### PV operating point and the need for MPPT

A solar PV module cannot be treated as an ideal battery-like source with nearly fixed voltage. Its terminal current and voltage are related by a nonlinear **I-V characteristic**. If the module is forced to operate at one voltage, the current takes the value allowed by that curve; at another voltage, a different current results. Since output power is the product of voltage and current, the delivered power depends on the chosen operating point [PVPMC, *Array Utilization*], [Esram and Chapman, IEEE Trans. Energy Conversion, 2007].

The electrical definition of output power is

$$\boxed{P = VI} \quad \text{(17.1)}$$

where $P$ is power in watts, $V$ is terminal voltage, and $I$ is terminal current.

For a PV source, current depends on voltage, so power may be written as

$$\boxed{P(V) = V\,I(V)} \quad \text{(17.2)}$$

The power curve therefore has a peak. The operating point at which the product $VI$ is greatest is the **maximum power point** (**MPP**).

PV behavior is commonly described with two related curves:

- the **I-V curve**, which shows current versus voltage
- the **P-V curve**, which shows power versus voltage

Two standard PV quantities appear repeatedly:

- **short-circuit current**, $I_{SC}$: current at approximately zero terminal voltage
- **open-circuit voltage**, $V_{OC}$: voltage at approximately zero output current

Between these limits lies the useful operating region. At low voltage, current is high but voltage is too small for large power. Near $V_{OC}$, voltage is high but current collapses. The power curve rises, reaches a peak, and then falls. The peak occurs at:

- **maximum-power voltage**, $V_{MPP}$
- **maximum-power current**, $I_{MPP}$

and the maximum available power is

$$\boxed{P_{MPP} = V_{MPP}I_{MPP}} \quad \text{(17.3)}$$

**Image prompt for Figure 17.1:** Create a clean textbook-style engineering figure showing the I-V and P-V characteristics of a solar PV module under one irradiance condition. Use two aligned plots versus module voltage. In the upper plot, show current staying nearly flat at first and then dropping steeply near open-circuit voltage. Mark $I_{SC}$, $V_{OC}$, and the operating point at maximum power. In the lower plot, show power rising from zero, reaching a clear peak at $V_{MPP}$, and then falling back to zero at $V_{OC}$. Label $V_{MPP}$, $I_{MPP}$, and $P_{MPP}$. Use monochrome textbook style with axes, units, and clean annotations.

#### Illustrative operating points

Table 17.1 gives approximate operating points for one PV module under fixed irradiance and temperature.

Table 17.1: Illustrative PV operating points under one fixed irradiance and temperature

| Module voltage $V$ | Module current $I$ | Power $P = VI$ |
| --- | --- | --- |
| $10 \text{ V}$ | $5.8 \text{ A}$ | $58 \text{ W}$ |
| $14 \text{ V}$ | $5.7 \text{ A}$ | $79.8 \text{ W}$ |
| $18 \text{ V}$ | $5.0 \text{ A}$ | $90 \text{ W}$ |
| $20 \text{ V}$ | $4.3 \text{ A}$ | $86 \text{ W}$ |
| $22 \text{ V}$ | $2.0 \text{ A}$ | $44 \text{ W}$ |

The largest power is approximately $90 \text{ W}$ at about $18 \text{ V}$, so

- $V_{MPP} \approx 18 \text{ V}$
- $I_{MPP} \approx 5 \text{ A}$
- $P_{MPP} \approx 90 \text{ W}$

If the same module is constrained to operate near $14 \text{ V}$, it delivers only about $79.8 \text{ W}$. The lost output is not caused by a fault in the module; it results from operation away from the maximum power point. This is the practical reason MPPT is required.

The maximum power point is not fixed. Increasing irradiance generally increases available current and power, while increasing cell temperature generally reduces the voltage at which the module operates best [PVPMC, *Point-value models*], [Esram and Chapman, IEEE Trans. Energy Conversion, 2007]. A fixed operating voltage is therefore rarely optimal over an entire day.

#### Role of the converter in MPPT

**Maximum Power Point Tracking** is the control process that keeps the PV source near the operating point at which it can deliver maximum power under present conditions [PVPMC, *Array Utilization*]. The controller does not create additional solar energy; it adjusts the electrical operating point so that the available energy is extracted more effectively.

A DC-DC converter or inverter stage provides the required control action. By changing duty ratio or a related control reference, the converter changes the relationship between its input side and output side. The PV terminal voltage and current therefore move to a different point on the I-V curve even if the battery or load on the output side remains unchanged. In this sense, the converter is the power-processing stage and the MPPT algorithm is the decision process that tells it where to operate.

A direct PV-to-battery connection is electrically simple but gives the PV module little freedom to remain at its best operating point. Inserting a converter between the module and the battery allows the PV side and battery side to operate at different voltages while still exchanging power.

#### A simple PV-battery example

Consider a PV module whose MPP under one condition is near $18 \text{ V}$ and $5 \text{ A}$. Then

$$P_{MPP} = 18 \times 5 = 90 \text{ W}.$$

If an ideal buck converter transfers this power to a $12 \text{ V}$ battery, the battery-side current is approximately

$$I_{bat} \approx \frac{90}{12} = 7.5 \text{ A}.$$

If the same module is instead held near $14 \text{ V}$ and $5.7 \text{ A}$, the available power becomes

$$14 \times 5.7 = 79.8 \text{ W},$$

and the ideal battery-side current falls to

$$\frac{79.8}{12} \approx 6.65 \text{ A}.$$

This difference is significant in cumulative energy harvest over many hours of operation.

#### Common misconceptions

Maximum power does not occur at the highest voltage or the highest current point; it occurs where the product $VI$ is maximum. MPPT is also not tied to any single converter family. A buck, boost, buck-boost, SEPIC, or inverter stage may implement MPPT, depending on the required electrical relationship. Finally, a datasheet value of $V_{MPP}$ is not sufficient for all operating conditions, because irradiance and temperature move the optimum point continuously.

### 4.5.2 Overview of MPPT techniques: Perturb & Observe (P&O) and Incremental Conductance

#### Why an algorithm is needed

The existence of an MPP does not by itself solve the control problem. The system must measure electrical quantities, infer whether the operating point should move to the left or right on the P-V curve, and then update the converter command.

At a basic level, every MPPT loop performs three functions:

1. measure PV voltage and current
2. determine whether the present operating point is before or after the MPP
3. modify the converter command so the operating point moves toward the peak

Two widely taught methods are **Perturb and Observe** (**P&O**) and **Incremental Conductance** [Esram and Chapman, IEEE Trans. Energy Conversion, 2007].

**Image prompt for Figure 17.2:** Create a clean textbook-style block diagram of an MPPT-controlled PV power stage. Show a solar PV module feeding a DC-DC converter, then a battery or DC bus load. Add sensors measuring PV voltage and PV current, an MPPT controller block, and a PWM block driving the converter switch. Label the controller outputs as duty ratio or voltage reference. Add a small inset note that the converter shifts the PV operating point on the I-V curve. Use monochrome textbook style.

#### Perturb and Observe

The **Perturb and Observe** method uses a simple hill-climbing rule. The controller introduces a small change in operating voltage, current reference, or duty ratio, then measures the resulting power. If the power increases, the next step is taken in the same direction. If the power decreases, the perturbation direction is reversed [Esram and Chapman, IEEE Trans. Energy Conversion, 2007].

Suppose the controller measures the following sequence:

- Sample 1: $V = 29 \text{ V}$, $I = 6.0 \text{ A}$, so $P = 174 \text{ W}$
- Sample 2: after a small increase in voltage, $V = 30 \text{ V}$, $I = 6.1 \text{ A}$, so $P = 183 \text{ W}$

Since power increased, the controller continues in the same direction. If the next sample is

- Sample 3: $V = 31 \text{ V}$, $I = 6.15 \text{ A}$, so $P = 190.65 \text{ W}$

the same decision is repeated. If a later sample becomes

- Sample 4: $V = 32 \text{ V}$, $I = 5.85 \text{ A}$, so $P = 187.2 \text{ W}$

the power has decreased, so the controller reverses direction.

The main attraction of P&O is that it requires no detailed mathematical model of the PV module. Its main limitation is that it usually continues to perturb near the peak, so the operating point oscillates around the MPP rather than remaining exactly at it. A larger perturbation step improves speed but increases oscillation; a smaller step reduces oscillation but slows tracking.

#### Incremental Conductance

The **Incremental Conductance** method is based on the slope of the power curve. At the maximum power point,

$$\boxed{\frac{dP}{dV} = 0} \quad \text{(17.4)}$$

Starting from Equation (17.2), where $P = VI$, differentiation with respect to $V$ gives

$$\frac{dP}{dV} = I + V\frac{dI}{dV} \quad \text{(17.5)}$$

At the MPP,

$$I + V\frac{dI}{dV} = 0$$

so

$$\boxed{\frac{dI}{dV} = -\frac{I}{V}} \quad \text{(17.6)}$$

This relation is the basis of incremental conductance MPPT. Here, $\dfrac{dI}{dV}$ is the **incremental conductance**, or local slope of the I-V curve, and $-\dfrac{I}{V}$ is the negative of the **instantaneous conductance**.

From Equation (17.5), three operating regions follow:

$$\boxed{\frac{dI}{dV} > -\frac{I}{V} \Rightarrow \text{left of MPP}} \quad \text{(17.7)}$$

$$\boxed{\frac{dI}{dV} = -\frac{I}{V} \Rightarrow \text{at MPP}} \quad \text{(17.8)}$$

$$\boxed{\frac{dI}{dV} < -\frac{I}{V} \Rightarrow \text{right of MPP}} \quad \text{(17.9)}$$

In digital control, the derivative is approximated by measured differences:

$$\boxed{\frac{dI}{dV} \approx \frac{\Delta I}{\Delta V}} \quad \text{(17.10)}$$

where $\Delta I$ and $\Delta V$ are small changes between sampling instants.

Suppose at one instant

- $V = 30 \text{ V}$
- $I = 6 \text{ A}$

Then

$$-\frac{I}{V} = -\frac{6}{30} = -0.2 \text{ A/V}.$$

If a nearby measurement gives

- $\Delta V = +1 \text{ V}$
- $\Delta I = -0.1 \text{ A}$

then

$$\frac{\Delta I}{\Delta V} = -0.1 \text{ A/V}.$$

Since $-0.1 > -0.2$, Equation (17.7) indicates that the operating point is to the left of the MPP, so the controller should move toward higher voltage. If instead

- $\Delta V = +1 \text{ V}$
- $\Delta I = -0.35 \text{ A}$

then

$$\frac{\Delta I}{\Delta V} = -0.35 \text{ A/V},$$

and because $-0.35 < -0.2$, the operating point lies to the right of the MPP, so the controller should move toward lower voltage.

#### Comparison and implementation

Table 17.2 summarizes the basic difference between the two methods.

Table 17.2: Conceptual comparison of two common MPPT methods

| Method | Core idea | Main strength | Main limitation |
| --- | --- | --- | --- |
| Perturb and Observe | Make a small change and check whether power rises or falls | Simple, widely used, low conceptual complexity | Oscillates around MPP and can be misled by rapidly changing irradiance |
| Incremental Conductance | Use the slope condition $\dfrac{dP}{dV}=0$ or $\dfrac{dI}{dV} = -\dfrac{I}{V}$ | Better identification of MPP direction under changing conditions | Greater measurement and computation effort than basic P&O |

The MPPT method does not replace the power stage. The algorithm must still act through a converter:

- a **buck** converter when PV voltage is above the battery or bus voltage
- a **boost** converter when PV voltage must be raised
- a **buck-boost** or **SEPIC** converter when PV voltage may be above or below the required output
- an inverter front end in grid-connected systems [PVPMC, *Array Utilization*]

The choice between P&O and incremental conductance is therefore a control decision layered onto a topology decision. MPPT and battery charging are also distinct functions. MPPT seeks the best operating point for the PV source, while battery charging enforces acceptable battery current and voltage limits. In a practical solar charger, both functions may be active.

### 4.5.3 Selection of DC-DC converter topology for solar PV, battery charging and EV drivetrain applications

#### Topology-selection logic

Converter selection begins with system constraints rather than with topology names. The first questions are straightforward:

- Is the source voltage generally above, below, or sometimes above and sometimes below the required output?
- Is power flow unidirectional or bidirectional?
- Is galvanic isolation required for safety, grounding, or standards compliance?
- Must output polarity remain the same as input polarity?
- Does the source benefit from smoother input current?
- Which practical priorities dominate: efficiency, size, cost, or controllability?

These questions determine the useful converter family more reliably than a comparison of theoretical efficiency alone.

#### Solar PV interfaces

If the PV operating voltage remains above the battery or DC-bus voltage, a **buck converter** is often the natural choice. This is a common arrangement in solar battery chargers. Texas Instruments describes the BQ24650 as a solar charge controller with MPPT by input-voltage regulation and specifically as a synchronous **buck** controller, which matches the case in which the useful PV voltage is above the battery voltage [TI, BQ24650 product page].

If the PV voltage is below the target DC bus, a **boost converter** is the first candidate. A PV source operating near $30 \text{ V}$ and feeding a regulated $48 \text{ V}$ bus requires step-up action. The converter must raise voltage while the MPPT controller keeps the PV source near its optimum operating point [Mohan, Undeland, Robbins, *Power Electronics: Converters, Applications, and Design*, 3e], [Erickson and Maksimovic, *Fundamentals of Power Electronics*, 2e].

If the PV voltage may lie above the required output in one condition and below it in another, a **buck-boost** family becomes more appropriate. Two familiar non-isolated options are the inverting **buck-boost** converter and the non-inverting **SEPIC** converter. The SEPIC is often attractive when polarity must be preserved and the application benefits from relatively smooth input current [Erickson and Maksimovic, *Fundamentals of Power Electronics*, 2e], [Mohan, Undeland, Robbins, *Power Electronics: Converters, Applications, and Design*, 3e].

When a PV source and battery share a DC bus and energy must move in both directions, a **bidirectional buck-boost** stage often becomes necessary. If isolation is required, the correct choice may shift from the non-isolated families to the isolated converters studied earlier.

#### Battery-charging systems

Battery charging is determined not only by voltage conversion but also by charging method. Most rechargeable batteries are charged with some form of **constant-current / constant-voltage** (**CC-CV**) behavior: current is limited in the earlier stage and voltage is limited later. The converter must therefore match the source appropriately while also enforcing the battery-side charging requirements.

If a solar source remains above battery voltage, a buck charger is often sufficient. If the source may be above or below battery voltage, a buck-boost charger is more flexible. Texas Instruments describes the BQ25756 as a bidirectional buck-boost charge controller with MPPT for solar charging, which is consistent with applications that combine wide voltage ranges, solar input, and possible reverse power flow [TI, BQ25756 product page].

#### EV and electrified transport applications

In EV systems, the main traction energy path usually involves the high-voltage battery, the traction inverter, and the motor. Regenerative braking normally returns energy through the motor and inverter path rather than through a small auxiliary DC-DC converter.

DC-DC converters are nevertheless essential in EVs and hybrid vehicles. They are used to connect a high-voltage battery to a low-voltage auxiliary bus, to interface 48 V and 12 V systems, and to manage energy exchange among storage subsystems. For a **48 V / 12 V dual-battery system**, Analog Devices describes the LTC3871 as a bidirectional buck or boost controller for automotive dual-battery applications [Analog Devices, LTC3871 product page]. This is a typical case in which two positive-voltage buses must exchange power in either direction.

For conversion from a high-voltage traction battery to a 12 V auxiliary rail, isolation is often required in practice. In that situation, the decisive factor is not only voltage ratio but also safety architecture.

#### Topology-selection table

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

#### Product-page interpretation

Commercial product pages often express topology logic in practical rather than textbook language. A solar charger described as a **buck controller with MPPT by input-voltage regulation** implies a PV input that usually operates above the battery voltage. A **bidirectional buck-boost charge controller with MPPT** implies wider source and battery ranges, together with the possibility of reverse power flow. A controller intended for **48 V/12 V dual-battery systems** points directly to a bidirectional interface between unequal DC buses. Product literature does not usually spell out the full topology-selection argument, but it often contains enough information to reconstruct it.

#### A compact decision process

A practical selection sequence is:

1. determine whether power flow is one-way or bidirectional
2. determine whether isolation is mandatory
3. compare the source-voltage range with the required output-voltage range
4. check whether polarity must remain non-inverted
5. consider input-current behavior, especially for sources such as PV
6. then compare efficiency, switch stress, and component count

This sequence keeps topology choice tied to system requirements rather than to a single voltage-gain expression.

#### Common misconceptions

The best topology is not simply the one with the highest theoretical efficiency in an isolated comparison table. The correct choice is the one that matches the actual voltage range, power-flow direction, safety requirements, and control task. MPPT also does not determine topology automatically; it specifies the desired PV operating point, while the converter topology determines which electrical relationships can be realized. In EV applications, regenerative braking does not imply that the principal traction path uses a bidirectional DC-DC converter, because the main regenerative path is usually through the motor drive inverter.

## Chapter summary

- A PV module has a nonlinear I-V characteristic, so its delivered power depends on operating voltage.
- The maximum power point is the operating point at which $P = VI$ is greatest.
- Because irradiance and temperature change, the MPP moves and must be tracked rather than assumed fixed.
- MPPT is implemented through a converter or inverter stage that shifts the PV operating point.
- Perturb and Observe is simple and widely used but tends to oscillate around the MPP.
- Incremental Conductance uses the slope condition $\dfrac{dI}{dV} = -\dfrac{I}{V}$ at the MPP and is often more deliberate under changing conditions.
- Topology selection depends on voltage range, direction of power flow, isolation, polarity, and source behavior.
- Buck, boost, buck-boost, SEPIC, bidirectional buck-boost, and isolated converters each occupy distinct application roles in PV, battery-charging, and EV-related systems.

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
