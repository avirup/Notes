# Chapter 1.4: Power MOSFET

## Chapter opening

Chapters 1.1 to 1.3 introduced three important power-device families: the power BJT, the SCR, and the DIAC-TRIAC pair. Together they illustrated the essential requirements of a practical power switch: it must block voltage safely in the OFF state, conduct with acceptable loss in the ON state, and change state in a controlled manner.

The **power MOSFET**, or **power metal-oxide-semiconductor field-effect transistor**, became one of the main solutions to those requirements in high-frequency converters. Its insulated gate allows voltage control with negligible steady-state gate current, its majority-carrier operation supports rapid switching, and its vertical structure makes useful voltage and current ratings possible. For that reason, power MOSFETs are common in switch-mode power supplies, battery chargers, DC-DC converters, EV auxiliary power stages, solar charge controllers, telecom rectifiers, and many low- to medium-power inverter subsystems [onsemi AN-9010/D], [Vishay AN605].

This chapter examines the historical development of the power MOSFET, the V-DMOS structure and operating principle, the meaning of output and transfer characteristics, and the switching, body-diode, thermal, and datasheet issues that govern practical use.

## Prerequisites check

- You should know the basic idea of a semiconductor switch being either OFF and blocking voltage, or ON and carrying current.
- You should be comfortable with voltage, current, power, and the relation $P = VI$.
- You should know that a transistor has three terminals and that a control terminal can influence a larger power path.
- You should remember from Chapter 1.1 that power-semiconductor switching speed matters because voltage and current can overlap during transitions.
- You should know that a 230 V, 50 Hz single-phase supply has a peak value of about $325 \text{ V}$ after rectification.

If the distinction between conduction loss and switching loss feels weak, a quick review of Chapter 1.1 will help before going further.

## Core content

### 1.4.1 History of Power MOSFET

Before the power MOSFET became common, engineers already had usable power devices. BJTs could be turned ON and OFF, and thyristors could handle high power, but BJTs required continuous base current while conducting and conventional SCRs could not ordinarily be gate-turned-OFF. As switching frequencies increased and compact switched-mode converters became more important, industry needed a device that was faster and easier to drive.

The broader MOSFET story begins with the invention of the MOS transistor in 1959 by Mohamed Atalla and Dawon Kahng at Bell Labs [Computer History Museum, "MOS Transistor Demonstrated", 1959]. That invention was not yet the power MOSFET used in converters today, but it established the field-effect control principle that made later development possible. Instead of controlling collector current through continuous base current, as in a BJT, a MOSFET uses an electric field created by gate voltage to form a conducting channel.

For integrated circuits, the MOSFET became revolutionary because it could be scaled and fabricated densely. Power electronics, however, needed something different. A lateral MOSFET suitable for IC logic is not enough to block hundreds of volts or carry tens of amperes efficiently. A power device needs a geometry that can support high voltage in the OFF state and still offer a low-resistance current path in the ON state. That need led to **vertical power MOSFET** structures, often called **V-DMOS** or **vertical double-diffused MOS** structures [onsemi AN-9010/D], [IEEE TED, "The Trench Power MOSFET: Part I"].

The phrase "double-diffused" refers to how the channel region is formed by two diffusion steps in fabrication. The practical consequence is that current flows vertically through the silicon rather than only along the surface, which makes the device much more suitable for power conversion.

By the 1970s and 1980s, power MOSFETs became central to switch-mode power supplies, high-frequency choppers, and low-voltage motor-control systems. The onsemi application note on MOSFET basics describes the power MOSFET as a device with high input impedance, majority-carrier operation, and fast switching behavior that made it particularly attractive in power switching applications [onsemi AN-9010/D]. Later structural improvements such as trench gates further reduced ON resistance, especially in low-voltage devices [IEEE TED, "The Trench Power MOSFET: Part I"].

The comparison with other power devices clarifies where MOSFETs fit in the larger device family:

- Compared with a **power BJT**, a MOSFET is usually easier to drive because the gate ideally draws negligible steady-state current.
- Compared with an **SCR** or **TRIAC**, a MOSFET can be turned ON and OFF directly by its control signal.
- Compared with an **IGBT**, a MOSFET is usually preferred at lower voltages and higher switching frequencies because it is a majority-carrier device and therefore avoids minority-carrier storage delay [Vishay AN605], [onsemi AN-9010/D].

Because a MOSFET is a **majority-carrier device**, it does not rely on large stored minority charge of the kind that slows a saturated BJT or a thyristor. This is one of the main reasons MOSFETs switch quickly.

Table 4.1: Why the power MOSFET became important

| Property | Why it mattered in practice |
|---|---|
| Voltage-controlled gate | Simplified the drive circuit compared with BJTs |
| Majority-carrier operation | Enabled fast switching and high-frequency use |
| Vertical structure | Allowed useful voltage blocking and current capability |
| Positive temperature coefficient of $R_{DS(\mathrm{on})}$ in normal operation | Helped current sharing in parallel devices |
| Built-in body diode | Made the device naturally compatible with many converter topologies, though not without tradeoffs |

In power electronics, the significance of the MOSFET lies not only in voltage control at the gate but in the combination of gate control, vertical structure, switching speed, ON-state resistance behavior, and reverse-current behavior through the body diode.

### 1.4.2 Vertical (V-DMOS) structure, operation, output and transfer characteristics

#### Why a vertical structure is needed

A 48 V to 12 V, 300 W DC-DC converter for an EV auxiliary bus requires a switch that can carry tens of amperes when ON while blocking the bus voltage when OFF. A current path confined to a thin surface region would be too resistive for efficient power conversion.

The **vertical MOSFET** solves this problem. In a V-DMOS device, current enters near the top surface and leaves through the bottom drain contact, so many parallel microscopic cells can share current across the die area while the vertical drift region supports OFF-state voltage [Vishay AN605], [onsemi AN-9010/D].

**Image prompt for Figure 4.1:** Create a clean textbook-style technical illustration of an N-channel vertical power MOSFET (V-DMOS) cross-section. Show source metallization at the top contacting repeated N+ source regions inside P-body regions. Show a polysilicon gate insulated by silicon dioxide over the channel area. Show the lightly doped N- drift region below the body and the N+ drain substrate at the bottom with drain metallization. Label source, gate, drain, P-body, N+ source, N- drift region, N+ drain substrate, oxide, inversion channel, and intrinsic body diode from body to drain. Use monochrome engineering style and no decorative background.

Figure 4.1 should make four structural features clear: the **gate** is insulated from the semiconductor by a thin oxide layer, the conduction channel forms near the surface under the gate when the gate-source voltage becomes sufficiently positive in an N-channel device, the main current path then continues vertically through the drift region to the drain, and the P-body with the N-drift region naturally creates the **body diode**.

#### Terminals and basic control idea

The main MOSFET terminals are:

- **Gate (G)**: the control terminal
- **Drain (D)**: one end of the main power path
- **Source (S)**: the other end of the main power path

Most power MOSFETs also have an internal body region tied to the source terminal in the package. Because of that internal connection, the body diode appears between source and drain with a fixed polarity determined by device type.

The discussion here focuses on the **N-channel enhancement-mode power MOSFET**, because it is the most common practical device in converters.

The basic operating sequence is as follows:

1. With $V_{GS} = 0$, there is no inversion channel between source and drift region, so the device is OFF and can block drain-source voltage.
2. As the gate-source voltage $V_{GS}$ increases, an electric field attracts carriers near the surface.
3. When $V_{GS}$ reaches the **threshold voltage**, written $V_{GS(\mathrm{th})}$, an inversion layer begins to form.
4. Once a sufficient channel exists, drain current can flow when a drain-source voltage is applied.

**Threshold voltage does not mean that the MOSFET is fully ON.** It marks the onset of inversion under specified test conditions. A power MOSFET with $V_{GS(\mathrm{th})} \approx 2 \text{ V}$ may still require $4.5 \text{ V}$, $5 \text{ V}$, $10 \text{ V}$, or another specified drive level to achieve low $R_{DS(\mathrm{on})}$ in practical power operation [FQP30N06L Datasheet], [Vishay AN605].

#### OFF state and voltage blocking

When the MOSFET is OFF, the drain-source voltage appears mainly across the lightly doped drift region. The same tradeoff appears in other power devices: a lightly doped region helps support high voltage, but it also tends to increase ON-state resistance.

This tradeoff is one of the defining facts of power MOSFET design. As voltage rating increases, the drift region must become thicker and lighter doped, and $R_{DS(\mathrm{on})}$ rises significantly. That is why very high-voltage silicon MOSFETs are available, but their ON resistance is much higher than that of low-voltage MOSFETs of similar die size [Vishay AN605], [onsemi AN-9010/D].

This tradeoff defines the voltage classes of MOSFETs: low-voltage devices can be made very low in resistance and are well suited to high-current, high-frequency converters, whereas high-voltage devices retain good switching performance but pay a conduction-loss penalty through higher $R_{DS(\mathrm{on})}$.

#### ON state and channel formation

Once the gate voltage is high enough, a channel forms in the P-body under the oxide, connecting the N+ source region to the N-drift region. For small drain-source voltage, the MOSFET behaves approximately like a controlled resistance.

In that low-$V_{DS}$ ON region, a useful practical relation is

$$\boxed{V_{DS} \approx I_D R_{DS(\mathrm{on})}} \quad \text{(4.1)}$$

where $V_{DS}$ is the drain-source voltage, $I_D$ is the drain current, and $R_{DS(\mathrm{on})}$ is the drain-source ON resistance under stated gate-drive and temperature conditions.

Unlike a BJT in saturation, a MOSFET ON-state drop is not approximately fixed. It increases roughly in proportion to current.

So if a MOSFET has $R_{DS(\mathrm{on})} = 35 \text{ m}\Omega$ at the chosen gate drive, and it carries $20 \text{ A}$, then

$$V_{DS} \approx 20 \times 0.035 = 0.70 \text{ V}.$$

The instantaneous conduction loss is then

$$P_{\mathrm{cond}} = I_D^2 R_{DS(\mathrm{on})}. \quad \text{(4.2)}$$

Substituting the same current,

$$P_{\mathrm{cond}} = 20^2 \times 0.035 = 14 \text{ W}.$$

At moderate current and low voltage, the ON-state drop can be small. Because the loss varies as $I^2$, however, conduction loss rises quickly as current increases.

#### Linear region and saturation region: careful terminology

MOSFET terminology can be confusing because words used in analog electronics and words used in power electronics do not always match everyday intuition.

In many device texts, when $V_{GS} > V_{GS(\mathrm{th})}$ and $V_{DS}$ is small, the MOSFET is said to operate in the **ohmic region** or **linear region**. Here it behaves approximately like a voltage-controlled resistor. As $V_{DS}$ increases beyond a certain point, the channel pinches near the drain, and the device enters what device physics texts call the **saturation region**.

For a long-channel ideal MOSFET, the boundary is commonly written as

$$\boxed{V_{DS} = V_{GS} - V_{GS(\mathrm{th})}} \quad \text{(4.3)}$$

and the idealized saturation-region current is written as

$$\boxed{I_D \approx \frac{k}{2}\left(V_{GS} - V_{GS(\mathrm{th})}\right)^2} \quad \text{(4.4)}$$

where $k$ is a device-dependent constant.

For power-electronics switching, however, the MOSFET is usually not operated as an analog amplifier. The desired states are:

- the OFF state, where the device blocks voltage, or
- the strongly ON state, where $R_{DS(\mathrm{on})}$ is low.

In converter language, "fully ON" usually means that the gate is driven well above threshold so the device enters a low-resistance state, not merely the onset of the textbook saturation region. Device-physics **saturation** is therefore not the same as the "hard saturation" idea used for BJTs.

#### Output characteristics

The **output characteristics** of a MOSFET plot drain current $I_D$ against drain-source voltage $V_{DS}$ for several fixed values of gate-source voltage $V_{GS}$.

**Image prompt for Figure 4.2:** Create a textbook-style graph of N-channel power MOSFET output characteristics. Use horizontal axis $V_{DS}$ in volts and vertical axis $I_D$ in amperes. Draw a family of curves for increasing $V_{GS}$ values such as 4 V, 5 V, 6 V, 8 V, and 10 V. Show an initial near-linear ohmic region near the origin, then a bend into a current-flattening active region. Mark the boundary approximately as $V_{DS}=V_{GS}-V_{GS(th)}$. Label the low-$V_{DS}$ region as "ohmic/low-resistance region" and the higher-$V_{DS}$ region as "current-controlled region (device-text saturation)." Use monochrome engineering style.

If $V_{GS}$ is small, the channel is weak and only limited current can flow. As $V_{GS}$ rises, the channel becomes stronger and the entire output curve moves upward. Near the origin, the curves are almost straight because the MOSFET behaves like a low resistance. At larger $V_{DS}$, the current changes less strongly with voltage.

For converter design, the leftmost part of the graph is usually the most important because it corresponds to low conduction loss. If a datasheet graph shows that the current curve at $V_{GS} = 5 \text{ V}$ is much lower than at $V_{GS} = 10 \text{ V}$, gate-drive voltage must be treated as a design variable rather than a formality. A MOSFET with $R_{DS(\mathrm{on})}$ guaranteed only at $V_{GS} = 10 \text{ V}$ may dissipate much more power in a 5 V gate-drive circuit unless it is specifically intended for logic-level operation [FQP30N06L Datasheet].

#### Transfer characteristics

The **transfer characteristic** plots drain current $I_D$ versus gate-source voltage $V_{GS}$ at a stated drain-source voltage and temperature.

**Image prompt for Figure 4.3:** Create a clean textbook-style graph of N-channel power MOSFET transfer characteristics. Use horizontal axis gate-source voltage $V_{GS}$ in volts and vertical axis drain current $I_D$ in amperes. Show a curve that begins near zero current below threshold, then rises steeply after $V_{GS(th)}$. Mark threshold voltage, indicate that threshold is defined at a small test current, and add a second curve at higher junction temperature shifted slightly to illustrate temperature dependence. Use monochrome engineering style.

Whereas the output characteristics show how current varies with $V_{DS}$ at fixed $V_{GS}$, the transfer characteristic shows how strongly drain current rises as $V_{GS}$ increases at stated drain voltage and temperature.

The slope of the transfer curve is related to **transconductance**, written $g_m$, which is the change in drain current per change in gate-source voltage:

$$\boxed{g_m = \frac{\Delta I_D}{\Delta V_{GS}}} \quad \text{(4.5)}$$

High transconductance means the drain current responds strongly to gate-voltage change.

Because threshold is defined at a very small specified current, often in the milliampere range, the transfer curve should not be treated as proof of low-loss operation. Practical low-loss design still depends on the guaranteed $R_{DS(\mathrm{on})}$ values and the relevant curves at the intended gate drive [FQP30N06L Datasheet], [Vishay AN605].

#### Temperature effect on ON resistance

Power MOSFET datasheets usually show that $R_{DS(\mathrm{on})}$ increases with junction temperature. A device that is excellent at $25^\circ\text{C}$ may therefore exhibit much higher resistance in real equipment.

If the normalized resistance at operating temperature is denoted by a factor $K_T$, we may write

$$\boxed{R_{DS(\mathrm{on}),T} \approx K_T \, R_{DS(\mathrm{on}),25^\circ\mathrm{C}}} \quad \text{(4.6)}$$

where $K_T$ is greater than 1 at elevated temperature.

This temperature rise increases conduction loss, but it also gives MOSFETs a useful feature in parallel operation. If one MOSFET in a parallel group begins to carry more current, it heats more, its $R_{DS(\mathrm{on})}$ increases, and some current tends to shift to the cooler devices. This is not a complete cure for current imbalance, but it is much friendlier than the negative temperature behavior that can make BJTs hard to parallel.

### 1.4.3 Switching behaviour, body diode, specifications

#### Why the gate is easy to drive, but not effortless to drive

A MOSFET is voltage-driven in steady state, but that description is incomplete if it is interpreted too casually.

Because the gate is insulated by oxide, it ideally draws negligible DC current. The gate still presents capacitance that must be charged and discharged each switching cycle, so the driver does not supply steady current as a BJT base driver does, yet it must deliver pulse current quickly if fast switching is desired [onsemi AN-9010/D], [Vishay AN605].

Manufacturers usually describe this dynamic behavior through capacitances such as:

- **$C_{iss}$**: input capacitance
- **$C_{oss}$**: output capacitance
- **$C_{rss}$**: reverse transfer capacitance

and through total gate charge **$Q_g$**.

A practical average gate-drive relation is

$$\boxed{I_{G,\mathrm{avg}} \approx Q_g f_s} \quad \text{(4.7)}$$

where $I_{G,\mathrm{avg}}$ is the average current needed from the driver over time, $Q_g$ is the total gate charge for one turn-ON event, and $f_s$ is the switching frequency.

If the driver swings the gate by a voltage $V_{GG}$ each cycle, the approximate gate-drive power is

$$\boxed{P_G \approx Q_g V_{GG} f_s} \quad \text{(4.8)}$$

This power is not dissipated mainly in the MOSFET channel as conduction loss. It is associated with charging and discharging the gate and with losses in the driver path.

These relations show an important tradeoff. A large MOSFET may achieve low $R_{DS(\mathrm{on})}$ at the cost of substantial gate charge, so low conduction loss and easy high-speed switching do not automatically coincide.

#### Turn-ON and turn-OFF intervals

A MOSFET switching waveform is usually described through delay and transition intervals, similar in spirit to a BJT but with different physical causes:

- turn-ON delay time
- rise time
- turn-OFF delay time
- fall time

The distinctive MOSFET feature is the **Miller plateau**. During part of the switching transition, the gate voltage stops rising much even though gate current is still flowing, because that charge is being used mainly to change the drain voltage through the reverse-transfer capacitance $C_{rss}$ [onsemi AN-9010/D].

**Image prompt for Figure 4.4:** Create a textbook-style set of switching waveforms for an N-channel power MOSFET. Show three aligned plots versus time: gate-source voltage $V_{GS}$, drain-source voltage $V_{DS}$, and drain current $I_D$. In the gate-voltage plot, clearly show initial charging, threshold crossing, a Miller plateau, then the final rise to full gate drive. In the drain-voltage plot, show $V_{DS}$ starting high, then falling during the Miller plateau. In the drain-current plot, show $I_D$ rising after threshold and reaching load current before $V_{DS}$ fully falls. Label turn-on delay, rise time, turn-off delay, fall time, and Miller plateau. Use monochrome engineering style with units on axes.

During turn-ON, gate charge first raises $V_{GS}$ to threshold, then $I_D$ rises, then $V_{DS}$ falls while the gate remains near the Miller plateau, and finally $V_{GS}$ rises to the full drive value. During turn-OFF, the sequence reverses: the gate is discharged, the device passes through the Miller plateau while $V_{DS}$ rises, and the current then falls away.

A first estimate of switching energy is

$$\boxed{E_{\mathrm{sw,approx}} \approx \frac{1}{2}V_{DS} I_D (t_r + t_f)} \quad \text{(4.9)}$$

and the corresponding average switching loss is

$$\boxed{P_{\mathrm{sw,approx}} \approx f_s E_{\mathrm{sw,approx}}} \quad \text{(4.10)}$$

These are first estimates, but they capture the main trend: switching loss grows with voltage, current, transition time, and switching frequency.

#### The body diode

The **body diode** is an intrinsic diode created by the P-body and N-drift structure of the MOSFET. In an N-channel MOSFET used as a low-side switch, it is oriented so that it conducts when the source becomes more positive than the drain by about a diode drop. In many converter circuits this diode provides a natural path for **freewheeling current**, carries current during dead time in bridge circuits, and makes the MOSFET compatible with inductive switching arrangements.

The body diode also brings limitations. Its forward drop may be significant, and its reverse-recovery behavior may create extra loss and stress. In some high-performance converters, an external Schottky diode or a synchronous rectification strategy may still be preferred.

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

If an inductive circuit forces the drain-source voltage beyond the rated blocking condition, the MOSFET may enter avalanche. Some devices are designed to survive a stated single-pulse avalanche energy under specified conditions, but this should not be treated as a normal everyday operating mode unless the application is designed for it [Vishay AN605], [FQP30N06L Datasheet].

#### Thermal specification

Like every power semiconductor, the MOSFET is ultimately limited by junction temperature. A simple thermal estimate is

$$\boxed{T_J \approx T_C + P_D R_{\theta JC}} \quad \text{(4.11)}$$

where $T_J$ is junction temperature, $T_C$ is case temperature, $P_D$ is dissipation, and $R_{\theta JC}$ is junction-to-case thermal resistance.

If ambient-based thermal data are being used instead, a similar form applies:

$$\boxed{T_J \approx T_A + P_D R_{\theta JA}} \quad \text{(4.12)}$$

where $T_A$ is ambient temperature and $R_{\theta JA}$ is junction-to-ambient thermal resistance under stated mounting conditions.

These equations show why a MOSFET that appears safe electrically may still fail thermally in a compact battery charger or inverter auxiliary supply.

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

Two common interpretation mistakes are:

1. assuming threshold voltage tells you the proper gate-drive voltage,
2. reading $R_{DS(\mathrm{on})}$ without checking the gate voltage and temperature at which it is specified.

## Worked interpretation exercise

The [onsemi FQP30N06L Datasheet](https://www.onsemi.com/pdf/datasheet/fqp30n06l-d.pdf) provides a useful low-voltage example. It includes blocking-voltage rating, current rating, $R_{DS(\mathrm{on})}$ values at different gate-drive conditions, threshold data, characteristic curves, and gate-charge information.

### Step 1: Read the voltage rating before anything else

The datasheet gives a drain-source voltage rating of $V_{DSS} = 60 \text{ V}$ [FQP30N06L Datasheet].

This places the device in the low-voltage class. It is suitable for circuits such as:

- 12 V battery systems
- 24 V battery systems
- 48 V nominal battery systems with careful surge analysis
- low-voltage DC-DC converters and battery chargers

It is not suitable as a direct switch on a rectified 230 V mains DC bus, because that bus is about $325 \text{ V}$ under nominal conditions. Nor is it suitable for a 415 V three-phase rectified bus, which is much higher still.

### Step 2: Interpret the current rating carefully

The datasheet headline gives a continuous drain current of $32 \text{ A}$ at a specified case condition [FQP30N06L Datasheet].

This is a conditional thermal rating, not a universal statement that the device can carry $32 \text{ A}$ in any PCB assembly. The allowable continuous current depends strongly on case temperature, package mounting, copper area, and heat removal. In a practical converter, the thermal environment may reduce the usable current substantially.

### Step 3: Read $R_{DS(\mathrm{on})}$ together with gate-drive voltage

The datasheet specifies maximum $R_{DS(\mathrm{on})}$ values at different gate-drive conditions, including a lower resistance at $V_{GS} = 10 \text{ V}$ and a somewhat higher value at $V_{GS} = 5 \text{ V}$ [FQP30N06L Datasheet].

This indicates that the device can be used with logic-level drive, but it still performs better with stronger gate drive. If a converter controller can provide only 5 V at the gate, the 5 V resistance value must be used in the loss estimate, not the 10 V value.

Using the conservative value $R_{DS(\mathrm{on})} = 45 \text{ m}\Omega$ at $V_{GS} = 5 \text{ V}$ for a low-voltage converter switch carrying $I_D = 12 \text{ A}$, the conduction loss estimate is:

$$P_{\mathrm{cond}} = I_D^2 R_{DS(\mathrm{on})}
= 12^2 \times 0.045
= 6.48 \text{ W}. $$

This is already substantial for a TO-220 device without strong cooling. So even in low-voltage circuits, current must be respected.

### Step 4: Read threshold voltage correctly

The datasheet gives a threshold-voltage range roughly around the few-volt level under a very small drain-current test condition [FQP30N06L Datasheet].

This marks the onset of channel formation, not low-loss switching. For power-switching design, the guaranteed $R_{DS(\mathrm{on})}$ values at 5 V and 10 V are more informative than the threshold figure.

### Step 5: Use the curves, not only the table

The curves complement the summary table. The output characteristics show current capability at a given gate drive, the transfer characteristic shows how strongly conduction rises with $V_{GS}$, the normalized-resistance plot shows the temperature dependence of $R_{DS(\mathrm{on})}$, the gate-charge plot indicates driver demand during switching, and the body-diode plus reverse-recovery data show the cost of current commutation through the intrinsic diode [FQP30N06L Datasheet].

### Step 6: Connect the part to a realistic renewable-energy task

Consider a 24 V battery-powered solar street-light controller using a synchronous buck converter to charge a battery from a PV module. A 60 V MOSFET is in the correct general voltage class for this type of low-voltage system, and the logic-level gate feature is useful if the controller IC drives 5 V gates directly. The final choice still depends on worst-case PV open-circuit voltage and surges, conduction loss at elevated temperature, body-diode behavior during dead time, and the thermal path through the PCB or heat sink.

## How this matters in renewable-energy systems

Power MOSFETs are deeply embedded in renewable-energy hardware wherever voltage is moderate and switching frequency is high. In **solar PV systems**, they are common in MPPT buck, boost, and buck-boost stages, battery chargers, and low-power DC optimizers. In **battery-energy-storage systems**, they appear in bidirectional DC-DC converters, protection switches, and precharge circuits. In **EVs** and **UPS systems**, they are widely used in auxiliary converters, battery chargers, and low-voltage DC buses.

Selection in these systems depends directly on the parameters discussed in this chapter. Voltage rating determines whether the MOSFET belongs on a battery bus or a higher-voltage DC link, $R_{DS(\mathrm{on})}$ sets conduction loss at large current, gate charge and switching times shape driver demand and switching loss, body-diode behavior affects dead time and synchronous rectification, and thermal resistance limits performance in compact enclosures.

## Chapter summary

- The **power MOSFET** combines an insulated, voltage-controlled gate with majority-carrier switching and a vertical structure suited to power conversion [onsemi AN-9010/D], [Vishay AN605].
- The MOS transistor principle dates back to 1959, while power-electronics usefulness depended on later vertical structures such as V-DMOS [Computer History Museum, "MOS Transistor Demonstrated", 1959], [IEEE TED, "The Trench Power MOSFET: Part I"].
- In a **vertical MOSFET**, current flows vertically through the die, while the drift region supports OFF-state voltage. Higher voltage rating generally increases $R_{DS(\mathrm{on})}$.
- For an N-channel enhancement MOSFET, threshold voltage marks the start of channel formation, not the gate-drive condition for low-loss operation.
- In the ON state, the practical relations $V_{DS} \approx I_D R_{DS(\mathrm{on})}$ and $P_{\mathrm{cond}} = I_D^2 R_{DS(\mathrm{on})}$ are central to conduction-loss estimation.
- Output and transfer characteristics show how strongly MOSFET behavior depends on actual gate-drive voltage and temperature.
- Gate drive is voltage-controlled in steady state but dynamic in switching, because capacitances and gate charge determine current demand and the Miller plateau.
- The intrinsic body diode, safe operating limits, and thermal resistance are part of normal device selection, not secondary details.
- In low- and medium-voltage renewable-energy converters, MOSFET choice is governed by the combined requirements of voltage rating, conduction loss, switching behavior, and heat removal.

## Further reading

- B. Jayant Baliga, "The Trench Power MOSFET: Part I. History, Technology, and Prospects," *IEEE Transactions on Electron Devices*, vol. 55, no. 12, 2008. Useful for understanding how vertical and trench MOSFET technology developed and why structure matters.
- onsemi, *AN-9010/D: MOSFET Basics*. A practical manufacturer note that explains structure, operation, capacitances, switching, and the Miller effect in power-switching terms.
- Vishay Siliconix, *AN605: Power MOSFET Basics*. A clear application-oriented reference on V-DMOS structure, ratings, ON resistance, body diode, and safe use in circuits.
- onsemi, *FQP30N06L Datasheet*. A good real datasheet for learning how to interpret threshold voltage, ON resistance, gate charge, transfer curves, and body-diode data together.
- Computer History Museum, "MOS Transistor Demonstrated, 1959." Useful for the historical origin of the MOS transistor that later enabled the power MOSFET family.
