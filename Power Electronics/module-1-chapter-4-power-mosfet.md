# Chapter 1.4: Power MOSFET

## Chapter opening

In Chapters 1.1 to 1.3, we studied three important families of power devices: the power BJT, the SCR, and the DIAC-TRIAC pair. Those chapters taught a central lesson of power electronics: a useful power switch must do more than conduct current. It must block voltage safely, change state predictably, and fit the timing needs of the converter around it.

The **power MOSFET**, or **power metal-oxide-semiconductor field-effect transistor**, became one of the most important answers to that need. It is especially valuable when we want a switch that can turn ON and OFF rapidly, that does not require continuous drive current like a BJT, and that can be controlled conveniently by voltage at the gate terminal. For this reason, power MOSFETs are common in switch-mode power supplies, battery chargers, DC-DC converters, EV auxiliary power stages, solar charge controllers, telecom rectifiers, and many low- to medium-power inverter subsystems [onsemi AN-9010/D], [Vishay AN605].

This chapter matters because it marks a transition from line-frequency controlled power devices toward high-frequency self-commutated switching devices. Once you understand why a MOSFET is fast, why its gate behaves like a capacitor, why its ON-state loss is described by $R_{DS(\mathrm{on})}$ rather than a nearly fixed saturation voltage, and why the body diode matters, later chapters on choppers, SMPS, and PWM inverters become much easier to understand.

We will begin with the historical role of the MOSFET and why power electronics needed a vertical form of the device. Then we will study the V-DMOS structure, the basic operating principle, and the meaning of output and transfer characteristics. Finally, we will look at switching behavior, the body diode, and the most important datasheet specifications. By the end of the chapter, you should be able to read a power MOSFET datasheet in a practical way and judge why a MOSFET is suitable for one converter but not for another.

## Prerequisites check

- You should know the basic idea of a semiconductor switch being either OFF and blocking voltage, or ON and carrying current.
- You should be comfortable with voltage, current, power, and the relation $P = VI$.
- You should know that a transistor has three terminals and that a control terminal can influence a larger power path.
- You should remember from Chapter 1.1 that power-semiconductor switching speed matters because voltage and current can overlap during transitions.
- You should know that a 230 V, 50 Hz single-phase supply has a peak value of about $325 \text{ V}$ after rectification.

If the distinction between conduction loss and switching loss feels weak, a quick review of Chapter 1.1 will help before going further.

## Core content

### 1.4.1 History of Power MOSFET

Before the power MOSFET became common, engineers already had useful power devices. BJTs could be turned ON and OFF, and thyristors could handle high power. But both had practical limitations. A BJT is current-controlled, so the drive circuit must supply base current continuously while the device conducts. A thyristor is excellent in many line-frequency applications, but a conventional SCR cannot ordinarily be gate-turned-OFF. As switching frequencies increased and compact switched-mode converters became more important, industry needed a device that was easier to drive and faster to switch.

The broader MOSFET story begins with the invention of the MOS transistor in 1959 by Mohamed Atalla and Dawon Kahng at Bell Labs [Computer History Museum, "MOS Transistor Demonstrated", 1959]. That invention was not yet the power MOSFET used in converters today, but it established the field-effect control principle that made later development possible. Instead of controlling collector current through continuous base current, as in a BJT, a MOSFET uses an electric field created by gate voltage to form a conducting channel.

For integrated circuits, the MOSFET became revolutionary because it could be scaled and fabricated densely. Power electronics, however, needed something different. A lateral MOSFET suitable for IC logic is not enough to block hundreds of volts or carry tens of amperes efficiently. A power device needs a geometry that can support high voltage in the OFF state and still offer a low-resistance current path in the ON state. That need led to **vertical power MOSFET** structures, often called **V-DMOS** or **vertical double-diffused MOS** structures [onsemi AN-9010/D], [IEEE TED, "The Trench Power MOSFET: Part I"].

The phrase "double-diffused" refers to how the channel region is formed by two diffusion steps in fabrication. For us, the most important practical consequence is simpler: the current flows vertically through the silicon, not only along the surface. This makes the device much more suitable for power conversion.

By the 1970s and 1980s, power MOSFETs became central to switch-mode power supplies, high-frequency choppers, and low-voltage motor-control systems. The onsemi application note on MOSFET basics describes the power MOSFET as a device with high input impedance, majority-carrier operation, and fast switching behavior that made it particularly attractive in power switching applications [onsemi AN-9010/D]. Later structural improvements such as trench gates further reduced ON resistance, especially in low-voltage devices [IEEE TED, "The Trench Power MOSFET: Part I"].

This history also explains where MOSFETs fit in the larger device family:

- Compared with a **power BJT**, a MOSFET is usually easier to drive because the gate ideally draws negligible steady-state current.
- Compared with an **SCR** or **TRIAC**, a MOSFET can be turned ON and OFF directly by its control signal.
- Compared with an **IGBT**, which we will meet later, a MOSFET is usually preferred at lower voltages and higher switching frequencies because it is a majority-carrier device and therefore avoids minority-carrier storage delay [Vishay AN605], [onsemi AN-9010/D].

That last phrase, **majority-carrier device**, matters. In a MOSFET, current is carried by majority carriers only. There is no large stored minority charge of the kind that slows a saturated BJT or a thyristor. This is one of the main reasons MOSFETs switch quickly.

Table 4.1: Why the power MOSFET became important

| Property | Why it mattered in practice |
|---|---|
| Voltage-controlled gate | Simplified the drive circuit compared with BJTs |
| Majority-carrier operation | Enabled fast switching and high-frequency use |
| Vertical structure | Allowed useful voltage blocking and current capability |
| Positive temperature coefficient of $R_{DS(\mathrm{on})}$ in normal operation | Helped current sharing in parallel devices |
| Built-in body diode | Made the device naturally compatible with many converter topologies, though not without tradeoffs |

A common misconception is that a MOSFET is simply "a transistor that turns ON with voltage." That statement is not wrong, but it is too incomplete for power electronics. What makes the power MOSFET special is the combination of gate control, vertical structure, switching speed, ON-state resistance behavior, and reverse-current behavior through the body diode.

*Renewable-energy relevance.* Power MOSFETs appear everywhere in renewable-energy systems where voltage levels are moderate and switching frequency is significant: MPPT buck or boost converters in PV systems, battery chargers, 12 V or 48 V EV auxiliary converters, battery-management precharge paths, and many small inverter and control-supply stages.

### 1.4.2 Vertical (V-DMOS) structure, operation, output and transfer characteristics

#### Why a vertical structure is needed

Let us begin with a practical thought experiment.

Suppose you want to build a 48 V to 12 V, 300 W DC-DC converter for an EV auxiliary bus. The switch may need to carry tens of amperes when ON, yet it must block the bus voltage when OFF. If the current path existed only along a thin surface channel, the conduction path would be too resistive and too small for efficient power conversion. A power device therefore uses the silicon volume more effectively.

That is the logic behind the **vertical MOSFET**. In a V-DMOS device, the current enters near the top surface and leaves through the bottom drain contact, so many parallel microscopic cells can share current across the die area while the vertical drift region supports OFF-state voltage [Vishay AN605], [onsemi AN-9010/D].

**Image prompt for Figure 4.1:** Create a clean textbook-style technical illustration of an N-channel vertical power MOSFET (V-DMOS) cross-section. Show source metallization at the top contacting repeated N+ source regions inside P-body regions. Show a polysilicon gate insulated by silicon dioxide over the channel area. Show the lightly doped N- drift region below the body and the N+ drain substrate at the bottom with drain metallization. Label source, gate, drain, P-body, N+ source, N- drift region, N+ drain substrate, oxide, inversion channel, and intrinsic body diode from body to drain. Use monochrome engineering style and no decorative background.

Figure 4.1 should make four ideas visible at once.

First, the **gate** is insulated from the semiconductor by a thin oxide layer. That is why the MOSFET gate has very high input resistance in steady state. Second, the conduction channel forms near the surface under the gate when the gate-source voltage becomes sufficiently positive in an N-channel device. Third, the main current path then continues vertically through the drift region to the drain. Fourth, the P-body and N-drift regions naturally create a **body diode**, which is an inherent part of the device structure.

#### Terminals and basic control idea

The main MOSFET terminals are:

- **Gate (G)**: the control terminal
- **Drain (D)**: one end of the main power path
- **Source (S)**: the other end of the main power path

Most power MOSFETs also have an internal body region tied to the source terminal in the package. Because of that internal connection, the body diode appears between source and drain with a fixed polarity determined by device type.

In this chapter we focus on the **N-channel enhancement-mode power MOSFET**, because it is the most common practical device in converters.

The physical idea of operation is as follows:

1. With $V_{GS} = 0$, there is no inversion channel between source and drift region, so the device is OFF and can block drain-source voltage.
2. As the gate-source voltage $V_{GS}$ increases, an electric field attracts carriers near the surface.
3. When $V_{GS}$ reaches the **threshold voltage**, written $V_{GS(\mathrm{th})}$, an inversion layer begins to form.
4. Once a sufficient channel exists, drain current can flow when a drain-source voltage is applied.

At beginner level, it is very important to interpret the threshold voltage correctly. **Threshold voltage does not mean the MOSFET is fully ON.** It means the channel is just beginning to form under specified test conditions. A power MOSFET that has $V_{GS(\mathrm{th})} \approx 2 \text{ V}$ may still require $4.5 \text{ V}$, $5 \text{ V}$, $10 \text{ V}$, or another specified drive level to achieve a low $R_{DS(\mathrm{on})}$ in practical power operation [FQP30N06L Datasheet], [Vishay AN605].

This point is one of the most common beginner mistakes in reading MOSFET datasheets.

#### OFF state and voltage blocking

When the MOSFET is OFF, the drain-source voltage appears mainly across the lightly doped drift region. This is the same design tradeoff we saw in another form with the power BJT: a lightly doped region helps support high voltage, but it also tends to increase ON-state resistance.

This tradeoff is one of the defining facts of power MOSFET design. As voltage rating increases, the drift region must become thicker and lighter doped, and $R_{DS(\mathrm{on})}$ rises significantly. That is why very high-voltage silicon MOSFETs are available, but their ON resistance is much higher than that of low-voltage MOSFETs of similar die size [Vishay AN605], [onsemi AN-9010/D].

So even before we write equations, we already know an engineering truth:

- low-voltage MOSFETs can be made very low in resistance and are excellent for high-current, high-frequency converters,
- high-voltage MOSFETs switch well but pay a conduction-loss penalty through higher $R_{DS(\mathrm{on})}$.

#### ON state and channel formation

Once the gate voltage is high enough, a channel forms in the P-body under the oxide, connecting the N+ source region to the N-drift region. For small drain-source voltage, the MOSFET behaves approximately like a controlled resistance.

In that low-$V_{DS}$ ON region, a simple practical relation is

$$\boxed{V_{DS} \approx I_D R_{DS(\mathrm{on})}} \quad \text{(4.1)}$$

where $V_{DS}$ is the drain-source voltage, $I_D$ is the drain current, and $R_{DS(\mathrm{on})}$ is the drain-source ON resistance under stated gate-drive and temperature conditions.

Equation (4.1) is one of the most useful power-electronics relations in the whole chapter. It tells us that, unlike a BJT in saturation, a MOSFET ON-state drop is not approximately fixed. It grows in proportion to current.

So if a MOSFET has $R_{DS(\mathrm{on})} = 35 \text{ m}\Omega$ at the chosen gate drive, and it carries $20 \text{ A}$, then

$$V_{DS} \approx 20 \times 0.035 = 0.70 \text{ V}.$$

The instantaneous conduction loss is then

$$P_{\mathrm{cond}} = I_D^2 R_{DS(\mathrm{on})}. \quad \text{(4.2)}$$

Substituting the same current,

$$P_{\mathrm{cond}} = 20^2 \times 0.035 = 14 \text{ W}.$$

This example is useful because it shows both the strength and limitation of the MOSFET. At moderate current and low voltage, the ON-state drop can be small. But because the loss varies as $I^2$, conduction loss rises quickly as current increases.

#### Linear region and saturation region: careful terminology

MOSFET terminology can be confusing because words used in analog electronics and words used in power electronics do not always match everyday intuition.

In many device texts, when $V_{GS} > V_{GS(\mathrm{th})}$ and $V_{DS}$ is small, the MOSFET is said to operate in the **ohmic region** or **linear region**. Here it behaves approximately like a voltage-controlled resistor. As $V_{DS}$ increases beyond a certain point, the channel pinches near the drain, and the device enters what device physics texts call the **saturation region**.

For a long-channel ideal MOSFET, the boundary is commonly written as

$$\boxed{V_{DS} = V_{GS} - V_{GS(\mathrm{th})}} \quad \text{(4.3)}$$

and the idealized saturation-region current is written as

$$\boxed{I_D \approx \frac{k}{2}\left(V_{GS} - V_{GS(\mathrm{th})}\right)^2} \quad \text{(4.4)}$$

where $k$ is a device-dependent constant.

For power-electronics switching, however, we usually do not operate the MOSFET as an analog amplifier. We want either:

- the OFF state, where the device blocks voltage, or
- the strongly ON state, where $R_{DS(\mathrm{on})}$ is low.

So in converter language, "fully ON" usually corresponds to driving the gate well above threshold so the device enters a low-resistance state, not merely the onset of the textbook saturation region.

That is another place where beginners can get tripped up. Device-physics **saturation** is not the same as the "hard saturation" idea used for BJTs.

#### Output characteristics

The **output characteristics** of a MOSFET plot drain current $I_D$ against drain-source voltage $V_{DS}$ for several fixed values of gate-source voltage $V_{GS}$.

**Image prompt for Figure 4.2:** Create a textbook-style graph of N-channel power MOSFET output characteristics. Use horizontal axis $V_{DS}$ in volts and vertical axis $I_D$ in amperes. Draw a family of curves for increasing $V_{GS}$ values such as 4 V, 5 V, 6 V, 8 V, and 10 V. Show an initial near-linear ohmic region near the origin, then a bend into a current-flattening active region. Mark the boundary approximately as $V_{DS}=V_{GS}-V_{GS(th)}$. Label the low-$V_{DS}$ region as "ohmic/low-resistance region" and the higher-$V_{DS}$ region as "current-controlled region (device-text saturation)." Use monochrome engineering style.

How should we read such a graph?

If $V_{GS}$ is small, the channel is weak and only a limited current can flow. As $V_{GS}$ rises, the channel becomes stronger and the whole output curve moves upward. Near the origin, the curves are almost straight because the MOSFET behaves like a low resistance. At larger $V_{DS}$, the current levels off more.

For converter design, the leftmost part of the graph is often the most useful because that is the region associated with low conduction loss.

Suppose a datasheet graph shows that at $V_{GS} = 5 \text{ V}$ the current curve is much lower than at $V_{GS} = 10 \text{ V}$. The correct conclusion is not merely that "10 V is better." The deeper lesson is that MOSFET performance depends strongly on the actual gate-drive voltage. If the datasheet guarantees $R_{DS(\mathrm{on})}$ only at $V_{GS} = 10 \text{ V}$, then a 5 V gate-drive design may produce much higher conduction loss unless the device is specifically rated as a logic-level MOSFET [FQP30N06L Datasheet].

#### Transfer characteristics

The **transfer characteristic** plots drain current $I_D$ versus gate-source voltage $V_{GS}$ at a stated drain-source voltage and temperature.

**Image prompt for Figure 4.3:** Create a clean textbook-style graph of N-channel power MOSFET transfer characteristics. Use horizontal axis gate-source voltage $V_{GS}$ in volts and vertical axis drain current $I_D$ in amperes. Show a curve that begins near zero current below threshold, then rises steeply after $V_{GS(th)}$. Mark threshold voltage, indicate that threshold is defined at a small test current, and add a second curve at higher junction temperature shifted slightly to illustrate temperature dependence. Use monochrome engineering style.

This graph answers a different question from the output characteristics. The output characteristics ask, "For a chosen gate voltage, how much current can flow as $V_{DS}$ changes?" The transfer characteristic asks, "As I increase gate voltage, how strongly does the device turn ON?"

The slope of the transfer curve is related to **transconductance**, written $g_m$, which is the change in drain current per change in gate-source voltage:

$$\boxed{g_m = \frac{\Delta I_D}{\Delta V_{GS}}} \quad \text{(4.5)}$$

High transconductance means the drain current responds strongly to gate-voltage change.

Again, the threshold-voltage interpretation matters. The threshold is defined at a very small specified current, often in the milliampere range. So a MOSFET with a threshold near $2 \text{ V}$ is not a "2 V fully ON switch." It is a device that begins conduction around that voltage. Practical low-loss operation requires consulting the guaranteed $R_{DS(\mathrm{on})}$ values and the transfer or output curves at the actual intended gate drive [FQP30N06L Datasheet], [Vishay AN605].

#### Temperature effect on ON resistance

Power MOSFET datasheets usually show that $R_{DS(\mathrm{on})}$ increases with junction temperature. That matters because a device that is excellent at $25^\circ\text{C}$ may run much hotter in real equipment.

If the normalized resistance at operating temperature is denoted by a factor $K_T$, we may write

$$\boxed{R_{DS(\mathrm{on}),T} \approx K_T \, R_{DS(\mathrm{on}),25^\circ\mathrm{C}}} \quad \text{(4.6)}$$

where $K_T$ is greater than 1 at elevated temperature.

This temperature rise increases conduction loss. But it also gives MOSFETs a useful practical feature in parallel operation. If one MOSFET in a parallel group begins to carry more current, it heats more, its $R_{DS(\mathrm{on})}$ increases, and some current tends to shift to the cooler devices. This is not a perfect cure for current imbalance, but it is much friendlier than the negative temperature behavior that can make BJTs hard to parallel.

*Renewable-energy relevance.* This combination of low-voltage efficiency and easy paralleling is one reason MOSFETs are common in battery converters and low-voltage renewable-energy interfaces where currents are large but voltages are modest.

### 1.4.3 Switching behaviour, body diode, specifications

#### Why the gate is easy to drive, but not effortless to drive

We often say that a MOSFET is voltage-driven. That is true in steady state, but it can mislead if interpreted too casually.

Because the gate is insulated by oxide, the gate ideally draws negligible DC current. But the gate still presents capacitance that must be charged and discharged each switching cycle. So the driver does not supply steady current as a BJT base driver does, yet it must deliver pulse current quickly if fast switching is desired [onsemi AN-9010/D], [Vishay AN605].

Manufacturers usually describe this dynamic behavior through capacitances such as:

- **$C_{iss}$**: input capacitance
- **$C_{oss}$**: output capacitance
- **$C_{rss}$**: reverse transfer capacitance

and through total gate charge **$Q_g$**.

A very practical gate-drive relation is

$$\boxed{I_{G,\mathrm{avg}} \approx Q_g f_s} \quad \text{(4.7)}$$

where $I_{G,\mathrm{avg}}$ is the average current needed from the driver over time, $Q_g$ is the total gate charge for one turn-ON event, and $f_s$ is the switching frequency.

If the driver swings the gate by a voltage $V_{GG}$ each cycle, the approximate gate-drive power is

$$\boxed{P_G \approx Q_g V_{GG} f_s} \quad \text{(4.8)}$$

This power is not dissipated mainly in the MOSFET channel as conduction loss. It is associated with charging and discharging the gate and with losses in the driver path.

These equations reveal an important tradeoff. A MOSFET can be easy to command, but a large MOSFET with low $R_{DS(\mathrm{on})}$ often has substantial gate charge. So very low ON resistance and very fast switching do not always come together for free.

#### Turn-ON and turn-OFF intervals

A MOSFET switching waveform is usually described through delay and transition intervals, similar in spirit to a BJT but with different physical causes:

- turn-ON delay time
- rise time
- turn-OFF delay time
- fall time

The distinctive MOSFET feature is the **Miller plateau**. During part of the switching transition, the gate voltage stops rising much even though gate current is still flowing, because that charge is being used mainly to change the drain voltage through the reverse-transfer capacitance $C_{rss}$ [onsemi AN-9010/D].

**Image prompt for Figure 4.4:** Create a textbook-style set of switching waveforms for an N-channel power MOSFET. Show three aligned plots versus time: gate-source voltage $V_{GS}$, drain-source voltage $V_{DS}$, and drain current $I_D$. In the gate-voltage plot, clearly show initial charging, threshold crossing, a Miller plateau, then the final rise to full gate drive. In the drain-voltage plot, show $V_{DS}$ starting high, then falling during the Miller plateau. In the drain-current plot, show $I_D$ rising after threshold and reaching load current before $V_{DS}$ fully falls. Label turn-on delay, rise time, turn-off delay, fall time, and Miller plateau. Use monochrome engineering style with units on axes.

The physical story of turn-ON is:

1. The gate capacitance charges from zero toward threshold.
2. When threshold is crossed, drain current begins to rise.
3. Once the current reaches the load current, the drain-source voltage begins to fall.
4. During that drain-voltage fall, the gate voltage stays near the Miller plateau.
5. After the drain voltage has mostly settled, the gate voltage rises to the final drive value.

Turn-OFF is the reverse story. The gate is discharged, the device passes through the Miller plateau while $V_{DS}$ rises, and the current then falls away.

A common first estimate of switching energy is

$$\boxed{E_{\mathrm{sw,approx}} \approx \frac{1}{2}V_{DS} I_D (t_r + t_f)} \quad \text{(4.9)}$$

and the corresponding average switching loss is

$$\boxed{P_{\mathrm{sw,approx}} \approx f_s E_{\mathrm{sw,approx}}} \quad \text{(4.10)}$$

These are only first estimates, but they are useful for intuition. They remind us that switching loss grows with voltage, current, transition time, and switching frequency.

#### The body diode

The **body diode** is an intrinsic diode created by the P-body and N-drift structure of the MOSFET. It is not an optional external part. It comes with the device.

In an N-channel MOSFET used as a low-side switch, the body diode is oriented so that it conducts when the source becomes more positive than the drain by about a diode drop. In many converter circuits this diode provides a natural path for **freewheeling current**, especially with inductive loads.

That sounds entirely beneficial, but the full story is more careful.

The body diode is useful because:

- it provides a reverse-current path in many topologies,
- it can carry current during dead time in bridge circuits,
- it makes the MOSFET naturally compatible with inductive switching arrangements.

But it also brings limitations:

- its forward drop may be significant,
- its reverse-recovery behavior may create extra loss and stress,
- in some high-performance converters, an external Schottky diode or synchronous rectification strategy may still be preferred.

Datasheets therefore often specify body-diode or reverse-recovery parameters such as reverse-recovery time $t_{rr}$ and recovered charge $Q_{rr}$. These become very important in hard-switched converters.

For a buck converter in a solar charge controller, for example, current in the inductor must continue when the main switch turns OFF. If the freewheel path is through the body diode of another MOSFET, then that diode's recovery behavior affects efficiency and EMI. So the body diode is not merely a "bonus diode." It is part of the switching design.

#### Safe operating area and avalanche ruggedness

Although MOSFETs avoid second breakdown in the same severe way as BJTs, they still have important operating limits. Datasheets commonly specify:

- maximum drain-source voltage
- continuous drain current
- pulsed drain current
- power dissipation
- thermal resistance
- safe operating area
- avalanche energy or avalanche ruggedness

The **avalanche** topic deserves a short explanation. If an inductive circuit forces the drain-source voltage beyond the rated blocking condition, the MOSFET may enter avalanche. Some devices are designed to survive a stated single-pulse avalanche energy under specified conditions, but this should not be treated as a normal everyday operating mode unless the application is designed for it [Vishay AN605], [FQP30N06L Datasheet].

#### Thermal specification

Like every power semiconductor, the MOSFET ultimately lives or dies by junction temperature. A simple thermal estimate is

$$\boxed{T_J \approx T_C + P_D R_{\theta JC}} \quad \text{(4.11)}$$

where $T_J$ is junction temperature, $T_C$ is case temperature, $P_D$ is dissipation, and $R_{\theta JC}$ is junction-to-case thermal resistance.

If ambient-based thermal data are being used instead, a similar form applies:

$$\boxed{T_J \approx T_A + P_D R_{\theta JA}} \quad \text{(4.12)}$$

where $T_A$ is ambient temperature and $R_{\theta JA}$ is junction-to-ambient thermal resistance under stated mounting conditions.

These equations are simple but powerful. They tell us immediately why a MOSFET that looks safe electrically may still fail thermally in a compact battery charger or inverter auxiliary supply.

#### The most important MOSFET datasheet specifications

Table 4.2: Practical meaning of major power-MOSFET specifications

| Datasheet item | What it means | Why it matters |
|---|---|---|
| $V_{DSS}$ or BVDSS | Maximum drain-source blocking voltage | Must exceed worst-case circuit voltage with margin |
| $V_{GS(\mathrm{th})}$ | Threshold voltage at small test current | Indicates turn-on onset, not full enhancement |
| $R_{DS(\mathrm{on})}$ | ON resistance at stated $V_{GS}$ and temperature | Sets conduction loss |
| $I_D$ | Continuous drain current | Limited by package and thermal conditions |
| $Q_g$ | Total gate charge | Influences gate-drive requirement and switching speed |
| $C_{iss}$, $C_{oss}$, $C_{rss}$ | Dynamic capacitances | Affect switching transitions and EMI |
| $t_d$, $t_r$, $t_f$ | Switching times | Useful for timing and first loss estimates |
| Body-diode and $t_{rr}$ data | Reverse-conduction and recovery behavior | Important in inductive and bridge circuits |
| $R_{\theta JC}$, $R_{\theta JA}$ | Thermal resistances | Needed to estimate temperature rise |

When reading a MOSFET datasheet, the two most common interpretation mistakes are:

1. assuming threshold voltage tells you the proper gate-drive voltage,
2. reading $R_{DS(\mathrm{on})}$ without checking the gate voltage and temperature at which it is specified.

*Renewable-energy relevance.* These parameters appear directly in real design decisions: low $R_{DS(\mathrm{on})}$ for battery current, low $Q_g$ for high-frequency MPPT converters, suitable body-diode behavior for synchronous buck stages, and sufficient voltage rating for DC buses derived from 230 V or 415 V AC systems.

## Worked interpretation exercise

We will now read a real device artifact together:

- the [onsemi FQP30N06L Datasheet](https://www.onsemi.com/pdf/datasheet/fqp30n06l-d.pdf)

This is a good beginner-friendly example because it is a widely used logic-level N-channel MOSFET. Its datasheet includes headline ratings, $R_{DS(\mathrm{on})}$ values, threshold data, output characteristics, transfer characteristics, and gate-charge information.

### Step 1: Read the voltage rating before anything else

The datasheet gives a drain-source voltage rating of $V_{DSS} = 60 \text{ V}$ [FQP30N06L Datasheet].

That single number already tells us where the device belongs and where it does not belong.

It is suitable for circuits such as:

- 12 V battery systems
- 24 V battery systems
- 48 V nominal battery systems with careful surge analysis
- low-voltage DC-DC converters and battery chargers

It is not suitable as a direct switch on a rectified 230 V mains DC bus, because that bus is about $325 \text{ V}$ under nominal conditions. Nor is it suitable for a 415 V three-phase rectified bus, which is much higher still.

This first step is very important. Always place the part into the correct voltage class before getting excited about low ON resistance.

### Step 2: Interpret the current rating carefully

The datasheet headline gives a continuous drain current of $32 \text{ A}$ at a specified case condition [FQP30N06L Datasheet].

A beginner may read that and conclude, "This is a 32 A switch." That is too simplistic. The current rating depends strongly on package temperature and heat removal. In a real PCB without excellent thermal design, the usable continuous current may be much lower.

So the right reading is:

- electrically, the device can carry large current,
- thermally, the actual safe current depends on mounting and cooling.

### Step 3: Read $R_{DS(\mathrm{on})}$ together with gate-drive voltage

The datasheet specifies maximum $R_{DS(\mathrm{on})}$ values at different gate-drive conditions, including a lower resistance at $V_{GS} = 10 \text{ V}$ and a somewhat higher value at $V_{GS} = 5 \text{ V}$ [FQP30N06L Datasheet].

That tells us two things immediately.

First, the device really is intended to work with logic-level drive. Second, it still performs better with stronger gate drive. So if a converter controller can provide only 5 V at the gate, we must use the 5 V resistance value in our loss estimate, not the 10 V value.

Suppose we use the conservative value $R_{DS(\mathrm{on})} = 45 \text{ m}\Omega$ at $V_{GS} = 5 \text{ V}$ for a low-voltage converter switch carrying $I_D = 12 \text{ A}$.

Then the conduction loss estimate is

$$P_{\mathrm{cond}} = I_D^2 R_{DS(\mathrm{on})}
= 12^2 \times 0.045
= 6.48 \text{ W}. $$

This is already substantial for a TO-220 device without strong cooling. So even in low-voltage circuits, current must be respected.

### Step 4: Read threshold voltage correctly

The datasheet gives a threshold-voltage range roughly around the few-volt level under a very small drain-current test condition [FQP30N06L Datasheet].

This does **not** mean the MOSFET is a low-loss switch at that voltage. It only means measurable channel conduction has started. The guaranteed $R_{DS(\mathrm{on})}$ values at 5 V and 10 V are much more important for power-switching design.

This one comparison between threshold data and ON-resistance data is one of the best habits you can build while reading MOSFET datasheets.

### Step 5: Use the curves, not only the table

The datasheet includes:

- output characteristics,
- transfer characteristics,
- normalized ON-resistance versus temperature,
- gate-charge information,
- body-diode and reverse-recovery data [FQP30N06L Datasheet].

Each of these tells a different story.

The output characteristics show how much current is available at a given gate drive. The transfer characteristic shows how strongly conduction rises as $V_{GS}$ increases. The normalized-resistance plot reminds us that resistance increases at high temperature. The gate-charge plot tells us how demanding fast switching may be for the driver. The body-diode data tell us what happens when current commutates through the intrinsic diode.

A good engineer does not stop at the summary table.

### Step 6: Connect the part to a realistic renewable-energy task

Imagine a 24 V battery-powered solar street-light controller using a synchronous buck converter to charge a battery from a PV module. A 60 V MOSFET is in the right general voltage class for this type of low-voltage system. The logic-level gate feature is helpful if the controller IC drives 5 V gates directly. But the designer must still check:

- worst-case PV open-circuit voltage and surges,
- conduction loss at hot temperature,
- body-diode behavior during dead time,
- thermal path through the PCB or heat sink.

So the datasheet does not merely tell us "what the part is." It tells us how the part must be used.

## How this matters in renewable-energy systems

Power MOSFETs are deeply embedded in renewable-energy hardware, especially where voltage is moderate and switching frequency is high.

In **solar PV systems**, MOSFETs are common in MPPT buck, boost, and buck-boost stages for module-level power electronics, battery charging, and low-power DC optimizers. In **battery-energy-storage systems**, they appear in bidirectional DC-DC converters, precharge circuits, and protection switches. In **EVs**, low-voltage MOSFETs are used heavily in 12 V and 48 V auxiliary converters, battery disconnect paths, and onboard power management. In **UPS systems**, they are common in auxiliary SMPS stages, battery chargers, and low-voltage DC buses.

This chapter's ideas are directly visible in those systems:

- voltage rating determines whether the MOSFET belongs on a battery bus or a high-voltage DC link,
- $R_{DS(\mathrm{on})}$ determines conduction loss at large battery currents,
- gate charge affects switching loss and driver design,
- body-diode behavior affects bridge dead time and synchronous rectification,
- thermal resistance determines whether a compact enclosure can survive summer operation.

As renewable-energy systems aim for higher efficiency, smaller size, and faster control, these MOSFET details stop being "device theory" and become design reality.

## Chapter summary

- The **power MOSFET** became important because it combines voltage-controlled gate drive, fast majority-carrier switching, and practical vertical power-device structure [onsemi AN-9010/D], [Vishay AN605].
- The MOS transistor principle dates back to 1959, while power-electronics usefulness depended on later vertical structures such as V-DMOS [Computer History Museum, "MOS Transistor Demonstrated", 1959], [IEEE TED, "The Trench Power MOSFET: Part I"].
- In a **vertical MOSFET**, current flows vertically through the die, while a lightly doped drift region supports OFF-state voltage.
- The gate is insulated by oxide, so the MOSFET has very high steady-state input resistance.
- For an N-channel enhancement MOSFET, conduction begins when $V_{GS}$ exceeds the threshold voltage $V_{GS(\mathrm{th})}$, but threshold voltage is only the start of conduction, not the condition for low-loss full enhancement.
- In the ON state, a practical relation is
  $\boxed{V_{DS} \approx I_D R_{DS(\mathrm{on})}}$ from Equation (4.1).
- Conduction loss is commonly estimated by
  $\boxed{P_{\mathrm{cond}} = I_D^2 R_{DS(\mathrm{on})}}$ from Equation (4.2).
- The ideal long-channel boundary between ohmic and device-text saturation regions is
  $\boxed{V_{DS} = V_{GS} - V_{GS(\mathrm{th})}}$ from Equation (4.3).
- The transfer characteristic shows how drain current rises with gate voltage; transconductance is
  $\boxed{g_m = \Delta I_D / \Delta V_{GS}}$ from Equation (4.5).
- MOSFET gate drive is voltage-controlled but dynamic, because the gate capacitances and gate charge must be moved every switching cycle.
- Average gate-drive current and power can be estimated from
  $\boxed{I_{G,\mathrm{avg}} \approx Q_g f_s}$ and
  $\boxed{P_G \approx Q_g V_{GG} f_s}$ from Equations (4.7) and (4.8).
- Switching loss grows with voltage, current, switching time, and frequency, with a first estimate from Equations (4.9) and (4.10).
- The **body diode** is intrinsic to the device structure and is important in inductive circuits, synchronous rectifiers, and bridge legs.
- MOSFET datasheets must be read carefully with attention to $V_{DSS}$, $R_{DS(\mathrm{on})}$ at the actual gate drive, gate charge, thermal resistance, and body-diode behavior.

## Further reading

- B. Jayant Baliga, "The Trench Power MOSFET: Part I. History, Technology, and Prospects," *IEEE Transactions on Electron Devices*, vol. 55, no. 12, 2008. Useful for understanding how vertical and trench MOSFET technology developed and why structure matters.
- onsemi, *AN-9010/D: MOSFET Basics*. A practical manufacturer note that explains structure, operation, capacitances, switching, and the Miller effect in power-switching terms.
- Vishay Siliconix, *AN605: Power MOSFET Basics*. A clear application-oriented reference on V-DMOS structure, ratings, ON resistance, body diode, and safe use in circuits.
- onsemi, *FQP30N06L Datasheet*. A good real datasheet for learning how to interpret threshold voltage, ON resistance, gate charge, transfer curves, and body-diode data together.
- Computer History Museum, "MOS Transistor Demonstrated, 1959." Useful for the historical origin of the MOS transistor that later enabled the power MOSFET family.
