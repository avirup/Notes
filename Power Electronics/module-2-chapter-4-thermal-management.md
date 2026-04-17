# Chapter 2.4: Thermal Management

## Chapter opening

Thermal management addresses the physical consequence of semiconductor loss. Every watt lost in a MOSFET, IGBT, or diode appears as heat at the device junction, and converter reliability depends on how effectively that heat is conducted to the case, transferred to a heat sink, and rejected to the surrounding air. A converter may meet its electrical specifications and still age prematurely if the junction temperature remains too high during ordinary operation.

This chapter examines the two main sources of device loss, develops the thermal-resistance model used for first-pass heat-sink selection, and concludes with an overview of natural and forced cooling [ST AN4783], [Infineon AN-1057]. The aim is practical: to connect electrical loss, datasheet thermal data, and cooling hardware into one design picture.

## Prerequisites check

- You should remember from Chapters 1.4 and 1.5 that MOSFETs and IGBTs do not switch instantaneously, so voltage and current overlap during switching.
- You should remember from Chapter 2.1 that stronger or weaker gate drive changes switching speed, and therefore affects switching loss.
- You should remember from Chapter 2.2 that snubbers can reduce overshoot and ringing, but they may also dissipate power.
- You should be comfortable with the power relations $P = VI$ and, for a resistor, $P = I^2R$.
- You should know the difference between ambient temperature and device temperature, even if the thermal-resistance model is new.

If switching waveforms are unclear, Chapters 1.4, 1.5, and 2.1 should be reviewed before this chapter.

## Core content

### 2.4.1 Power losses in semiconductor devices: conduction and switching losses (qualitative)

#### Why a "high-efficiency" converter still gets hot

Consider a DC-DC converter in a battery charger that processes $1 \text{ kW}$ at $95\%$ efficiency. The efficiency is high, but the lost power is still

$$P_{\text{loss}} = P_{\text{in}} - P_{\text{out}} = 1000 - 950 = 50 \text{ W}.$$

Fifty watts is substantial inside a compact enclosure. It is comparable to the heat dissipated by a small soldering iron, and it is generated continuously inside the converter. That heat must move from the semiconductor junctions, through the package and heat sink, and finally into the surrounding air.

The first thermal-design question is therefore direct: how much power is being turned into heat inside the semiconductor devices?

For first-pass analysis, two loss categories dominate:

- **Conduction loss**: loss while the device carries current in its ON state.
- **Switching loss**: loss during the finite interval in which the device changes state.

Different devices express these losses differently. A MOSFET usually shows conduction loss through ON-state resistance. An IGBT or diode is often approximated by an ON-state voltage drop. At high switching frequency, switching loss may dominate. At lower frequency and high current, conduction loss may dominate. Thermal analysis starts by identifying which loss mechanism is likely to be larger under the intended operating condition [Mohan, Undeland, Robbins, *Power Electronics*].

#### Conduction loss

When a semiconductor is ON, it is not an ideal short circuit. Current flows through a nonzero resistance or across a nonzero voltage drop, so power is dissipated.

For a MOSFET, a first conduction-loss estimate is

$$\boxed{P_{\text{cond,MOSFET}} \approx I_{\text{rms}}^2 R_{DS(\text{on})}} \quad \text{(9.1)}$$

where $I_{\text{rms}}$ is the RMS current through the device over the interval of interest and $R_{DS(\text{on})}$ is the ON-state resistance.

This relation shows the square dependence on current. If current doubles, conduction loss becomes approximately four times larger.

Consider a low-voltage MOSFET in a 48 V to 12 V converter carrying an RMS current of $10 \text{ A}$. If its effective ON resistance at operating temperature is $25 \text{ m}\Omega$, then

$$P_{\text{cond,MOSFET}} \approx 10^2 \times 0.025 = 2.5 \text{ W}.$$

If the RMS current rises to $20 \text{ A}$, the conduction loss becomes

$$P_{\text{cond,MOSFET}} \approx 20^2 \times 0.025 = 10 \text{ W}.$$

The doubled current produces four times the loss, which is why current rating and thermal design are closely linked.

For an IGBT or diode, a first estimate often uses the ON-state voltage drop:

$$\boxed{P_{\text{cond}} \approx V_{\text{ON}} I_{\text{avg}}} \quad \text{(9.2)}$$

where $V_{\text{ON}}$ may be $V_{CE(\text{sat})}$ for an IGBT or $V_F$ for a diode, and $I_{\text{avg}}$ is the average current during conduction.

If an IGBT in an inverter leg has an average ON-state drop of about $1.8 \text{ V}$ at the relevant current and carries an average current of $6 \text{ A}$ during its conduction interval, then

$$P_{\text{cond}} \approx 1.8 \times 6 = 10.8 \text{ W}.$$

In first-pass calculations, MOSFET conduction loss is usually treated as resistive, while IGBT and diode conduction loss is often treated as voltage-drop times current. More detailed models are possible, but these forms are adequate for thermal estimates [Mohan, Undeland, Robbins, *Power Electronics*], [Rashid, *Power Electronics: Circuits, Devices and Applications, 4e*].

#### Why conduction loss usually rises with temperature

Temperature affects the loss as well as the temperature rise. For many power MOSFETs, $R_{DS(\text{on})}$ increases as junction temperature increases. For many IGBTs, $V_{CE(\text{sat})}$ also changes with temperature. The STGWA40HP65FB datasheet, for example, shows $V_{CE(\text{sat})}$ increasing with junction temperature in its static characteristics and Figure 5 [STGWA40HP65FB Datasheet].

The result is a reinforcing loop:

1. Current causes loss.
2. Loss raises junction temperature.
3. Higher junction temperature often increases ON-state loss.

Thermal margin is needed partly because the loss calculated at room temperature may understate the loss after the device has heated in service.

#### Switching loss

Ideal switching assumes an instantaneous transition from blocking state to conducting state. Real devices require finite turn-ON and turn-OFF times, so voltage across the device and current through the device overlap during switching. That overlap produces power loss.

A simple physical estimate is

$$\boxed{P_{\text{sw,approx}} \approx \frac{1}{2} V I (t_{\text{on}} + t_{\text{off}}) f_s} \quad \text{(9.3)}$$

where $V$ is the approximate device voltage during switching, $I$ is the current being switched, $t_{\text{on}}$ and $t_{\text{off}}$ are the effective switching intervals, and $f_s$ is the switching frequency.

The dependence is direct: higher voltage, higher current, slower switching, or higher switching frequency all increase switching loss.

Suppose an IGBT in a converter connected to a rectified 230 V, 50 Hz supply sees about $325 \text{ V}$ during the important switching interval, switches about $8 \text{ A}$, has a total effective overlap time $(t_{\text{on}} + t_{\text{off}})$ of $200 \text{ ns}$, and operates at $20 \text{ kHz}$. Then

$$P_{\text{sw,approx}} \approx \frac{1}{2}\times 325 \times 8 \times 200 \times 10^{-9} \times 20 \times 10^3 \approx 5.2 \text{ W}.$$

This is already comparable to the conduction loss of many practical devices.

Datasheets often provide switching energy directly, leading to a more practical design relation:

$$\boxed{P_{\text{sw}} \approx f_s (E_{\text{on}} + E_{\text{off}})} \quad \text{(9.4)}$$

where $E_{\text{on}}$ and $E_{\text{off}}$ are the turn-ON and turn-OFF energies per switching event, measured under stated test conditions.

The STGWA40HP65FB datasheet gives a typical turn-off energy of about $363\,\mu\text{J}$ at $V_{CC}=400 \text{ V}$, $I_C=40 \text{ A}$, $R_G=5\,\Omega$, and $T_J=25^\circ\text{C}$, rising to about $764\,\mu\text{J}$ at $175^\circ\text{C}$ under the same nominal electrical test conditions [STGWA40HP65FB Datasheet]. Switching loss is therefore not fixed; it varies with temperature, current, voltage, and gate resistance.

#### The balance between conduction loss and switching loss

Table 9.1 compares the two loss mechanisms.

Table 9.1: Conduction and switching losses compared

| Loss type | When it appears | Main physical cause | Usually worsens with |
|---|---|---|---|
| Conduction loss | While the device is ON | ON-state resistance or ON-state voltage drop | Higher current, higher device temperature |
| Switching loss | During turn-ON and turn-OFF | Voltage-current overlap during finite switching time | Higher voltage, higher current, higher frequency, slower switching |

This comparison explains several earlier design tradeoffs. A stronger gate driver can reduce switching time and therefore switching loss, but excessive drive strength may increase $dv/dt$, $di/dt$, and EMI. A snubber can reduce overshoot and stress, but it may also dissipate additional power. Protection circuitry can save the device during faults, but it does not remove the need for a thermal path that continuously carries away ordinary operating loss.

A converter can therefore be thermally limited even when its efficiency is high. Switching loss can become important at moderate switching frequencies when voltage and current are large, and datasheet current ratings only have meaning under their stated thermal conditions.

**Image prompt for Figure 9.1:** Create a clean textbook-style technical figure showing power loss in a switching semiconductor. Use three aligned time plots versus time: device voltage, device current, and instantaneous power. Mark one conduction interval where current flows with low but nonzero ON-state voltage, and a switching interval where voltage and current overlap to create a clear power pulse. Label "conduction loss," "turn-ON switching loss," and "turn-OFF switching loss." Use monochrome engineering style with clear axes, units, and annotations.

### 2.4.2 Thermal resistance, heat-sink selection - simple design approach

#### The thermal path from junction to ambient

Heat is generated at the semiconductor junction. It then travels through the package to the case, across the mounting interface, into the heat sink, and finally to the ambient air. Any weak section in that path raises the junction temperature.

ST describes this with an electrical analogy: temperature difference corresponds to voltage difference, heat flow to current, and thermal resistance to electrical resistance [ST AN4783]. The basic relation is

$$\boxed{\Delta T = P_{\text{loss}} R_{\text{th}}} \quad \text{(9.5)}$$

where $\Delta T$ is the temperature rise across a thermal path, $P_{\text{loss}}$ is the heat flow in watts, and $R_{\text{th}}$ is thermal resistance in $^\circ\text{C}/\text{W}$.

If a section of the thermal path has $R_{\text{th}} = 2^\circ\text{C}/\text{W}$ and carries $10 \text{ W}$, the temperature rise across that section is

$$\Delta T = 10 \times 2 = 20^\circ\text{C}.$$

This is the basis of first-pass heat-sink selection.

#### The main thermal-resistance terms

Table 9.2 lists the main thermal terms used in datasheets and heat-sink notes.

Table 9.2: Main thermal-management terms

| Symbol | Meaning | Plain-language interpretation |
|---|---|---|
| $T_j$ | Junction temperature | Temperature of the semiconductor silicon where heat is generated |
| $T_c$ | Case temperature | Temperature at the package case or specified mounting surface |
| $T_a$ | Ambient temperature | Temperature of the surrounding air |
| $R_{\text{thJC}}$ | Junction-to-case thermal resistance | How hard it is for heat to move from silicon to package case |
| $R_{\text{thCS}}$ | Case-to-sink thermal resistance | Thermal resistance of interface layer between case and heat sink |
| $R_{\text{thSA}}$ | Sink-to-ambient thermal resistance | How hard it is for the heat sink to give heat to the air |
| $R_{\text{thJA}}$ | Junction-to-ambient thermal resistance | Overall junction-to-air thermal path under a stated condition |
| TIM | Thermal interface material | Grease, pad, mica, ceramic sheet, or similar interface used between device and heat sink |
| $Z_{\text{th}}(t)$ | Transient thermal impedance | Time-dependent thermal behavior for short or pulsed heating |

For a device mounted on a heat sink, the simple series thermal path is written as [ST AN4783], [Infineon AN-1057]

$$\boxed{R_{\text{thJA}} = R_{\text{thJC}} + R_{\text{thCS}} + R_{\text{thSA}}} \quad \text{(9.6)}$$

which leads to the steady-state junction-temperature estimate

$$\boxed{T_j \approx T_a + P_{\text{tot}}(R_{\text{thJC}} + R_{\text{thCS}} + R_{\text{thSA}})} \quad \text{(9.7)}$$

where $P_{\text{tot}}$ is the total average device loss.

**Image prompt for Figure 9.2:** Create a clean textbook-style thermal-path illustration for a power semiconductor mounted on a heat sink. Show, from left to right, semiconductor junction at temperature $T_j$, package case at $T_c$, thermal interface material, heat sink, and ambient air at $T_a$. Mark the thermal resistances $R_{\text{thJC}}$, $R_{\text{thCS}}$, and $R_{\text{thSA}}$. Add arrows showing heat flow outward and include the equation $T_j = T_a + P_{\text{tot}}(R_{\text{thJC}} + R_{\text{thCS}} + R_{\text{thSA}})$. Use monochrome engineering style.

#### A simple heat-sink selection method

First-pass heat-sink selection can be written as a short procedure:

1. Estimate the worst-case total device loss, $P_{\text{tot}}$.
2. Choose the highest junction temperature acceptable for the design.
3. Choose the worst-case ambient temperature around the heat sink.
4. Read the device thermal data from the datasheet, especially $R_{\text{thJC}}$ and maximum $T_j$.
5. Estimate the interface thermal resistance $R_{\text{thCS}}$.
6. Solve for the largest allowable sink-to-ambient thermal resistance.

Rearranging Equation (9.7) gives

$$\boxed{R_{\text{thSA,max}} \approx \frac{T_{j,\text{target}} - T_a}{P_{\text{tot}}} - R_{\text{thJC}} - R_{\text{thCS}}} \quad \text{(9.8)}$$

This equation gives the largest sink-to-ambient thermal resistance acceptable for the design.

#### Numerical example: choosing a heat sink for a single IGBT

Suppose a 650 V IGBT in a small UPS inverter or PV auxiliary converter is expected to dissipate about $20 \text{ W}$ at worst case. Use a design target of $T_{j,\text{target}} = 125^\circ\text{C}$, let the ambient air near the heat sink be $45^\circ\text{C}$, and assume the device datasheet gives $R_{\text{thJC}} = 0.53^\circ\text{C}/\text{W}$, as the STGWA40HP65FB datasheet does [STGWA40HP65FB Datasheet]. Let $R_{\text{thCS}} = 0.5^\circ\text{C}/\text{W}$ for the interface layer.

Using Equation (9.8),

$$R_{\text{thSA,max}} \approx \frac{125 - 45}{20} - 0.53 - 0.5.$$

First calculate the total allowable junction-to-ambient resistance:

$$\frac{80}{20} = 4^\circ\text{C}/\text{W}.$$

Now subtract the device and interface contributions:

$$R_{\text{thSA,max}} \approx 4 - 0.53 - 0.5 = 2.97^\circ\text{C}/\text{W}.$$

The design therefore requires a heat sink whose sink-to-ambient thermal resistance is approximately $3^\circ\text{C}/\text{W}$ or lower under the actual airflow condition. A natural-convection heat sink rated at $5^\circ\text{C}/\text{W}$ would be insufficient. If forced air reduces the effective sink-to-ambient thermal resistance to about $2^\circ\text{C}/\text{W}$, the design gains clear margin.

The target junction temperature is set below the absolute maximum because tolerance, aging, dust, airflow uncertainty, thermal-cycling stress, and overload reduce the real operating margin. Long-life equipment is rarely designed for continuous operation at the absolute thermal limit.

#### The role of the interface layer

The heat sink is only one part of the thermal path. Real device packages and real heat sinks are not perfectly flat, and air trapped between them is a poor thermal conductor. A **thermal interface material**, or TIM, fills surface gaps and lowers thermal resistance. ST notes that grease or insulating layers such as mica, ceramic, or silicone can be used, and that contact pressure matters because the case-to-heat-sink resistance is introduced by real, nonideal contact surfaces [ST AN4783].

Even a large heat sink can perform poorly if

- the mounting surface is uneven,
- the TIM is poor or badly applied,
- the mounting pressure is inadequate,
- the assumed $R_{\text{thCS}}$ is too optimistic for the actual interface.

#### Steady-state thermal resistance versus transient thermal impedance

Steady-state thermal resistance is appropriate for continuous average heating. Semiconductor heating is not always steady, however. Fault pulses, startup surges, current bursts, and intermittent overloads may be short compared with the thermal time constant of the package and heat sink.

For such cases, datasheets provide **transient thermal impedance**, usually written as $Z_{\text{th}}(t)$. ST AN4783 explains that short pulses should be evaluated with thermal-impedance curves rather than only steady thermal resistance, because the thermal capacitance of the structure delays the temperature rise [ST AN4783]. The STGWA40HP65FB datasheet makes the same point with its Figure 25, where the transient thermal response is shown using a normalized relation $Z_{\text{th}} = k \cdot R_{\text{thJC}}$ for different duty conditions [STGWA40HP65FB Datasheet].

The distinction is simple: use $R_{\text{th}}$ for steady or average heating, and use $Z_{\text{th}}(t)$ when pulse duration matters.

Datasheet values such as $R_{\text{thJA}}$ and total power dissipation must always be read with their stated mounting and temperature conditions. Heat-sink performance is not a fixed property either; orientation, airflow, surface area, and enclosure conditions all change the effective sink-to-ambient thermal resistance [ST AN4783], [Infineon AN-1057].

### 2.4.3 Forced cooling - overview

#### Natural and forced convection

Natural cooling is attractive because it is simple, silent, and contains no moving parts. If semiconductor losses are modest and sufficient heat-sink area is available, natural convection may be adequate.

Compact power-electronic equipment, however, is often enclosed and operated in warm surroundings. Under those conditions, the allowable heat-sink size may be limited and the sink-to-ambient thermal resistance may not become low enough without moving air. ST AN4783 distinguishes

- **natural convection**, where airflow is created by buoyancy due to temperature differences,
- **forced convection**, where airflow is created by external means such as a fan or pump [ST AN4783].

The basic convection relation is

$$\boxed{R_{\text{th}} \approx \frac{1}{h_c A_s}} \quad \text{(9.9)}$$

where $h_c$ is the heat-transfer coefficient and $A_s$ is the effective heat-transfer surface area [ST AN4783].

This relation shows that thermal resistance decreases when either the surface area increases or the heat-transfer coefficient increases. A fan mainly improves the second factor by moving more air past the fins.

With stronger airflow, either the same heat sink can carry more power or a smaller heat sink can carry the same power. That is why forced-air cooling is common in compact UPS systems, EV chargers, telecom rectifiers, and medium-power PV inverter cabinets.

#### Layout and enclosure details still matter

Airflow does not remove the need for good mechanical layout. ST gives several practical recommendations [ST AN4783]:

- fins should be vertically aligned for natural-convection cooling,
- airflow should not be blocked,
- heat-generating devices should not be placed where hot air accumulates without escape,
- forced-air flow should be arranged to follow sensible natural-convection paths.

These points matter because a good heat sink can perform poorly inside a poor airflow path. Forced cooling also introduces reliability questions that natural convection avoids: fan failure, dust accumulation, acoustic noise, blocked passages, and the possible need for airflow monitoring or thermal shutdown backup.

#### Comparing the main cooling approaches

At higher power density, the cooling method becomes part of the converter architecture rather than a packaging detail. Liquid cooling is not treated in detail at this level, but it should be placed beside natural and forced-air cooling in the overall design picture.

Table 9.3: Cooling approaches at beginner level

| Cooling approach | Main strengths | Main limitations | Typical fit |
|---|---|---|---|
| Natural convection | Simple, quiet, no moving parts, higher mechanical reliability | Larger heat sink often needed, performance falls in cramped hot enclosures | Small chargers, low-power converters, open enclosures |
| Forced-air cooling | Better heat removal for size, lower effective sink-to-ambient thermal resistance | Fan failure, dust, noise, extra power use | UPS systems, inverter cabinets, compact medium-power converters |
| Liquid cooling | Very high heat-removal capability in compact space | Higher cost, complexity, pump and sealing concerns | High-power EV and industrial converters |

Local ambient temperature must also be interpreted correctly. In converter practice, the air around the heat sink may be far hotter than the room or outdoor temperature because the enclosure already contains other heat-generating components.

**Image prompt for Figure 9.3:** Create a clean textbook-style comparison figure showing the same finned heat sink under natural convection and forced-air cooling. On the left, show warm air rising naturally between vertical fins. On the right, show a fan pushing air across the fins. Label "natural convection," "forced convection," "airflow direction," "heat sink fins," and "lower effective sink-to-ambient thermal resistance with stronger airflow." Use monochrome engineering style with arrows and temperature labels, not decorative graphics.

## Worked interpretation exercise

The following exercise uses the [STGWA40HP65FB datasheet](https://www.st.com/resource/en/datasheet/stgwa40hp65fb.pdf), which combines thermal limit, thermal resistance, conduction behavior, switching energy, and transient thermal information in one device [STGWA40HP65FB Datasheet].

### Step 1: Read the thermal limit before reading the current rating

The datasheet states a maximum operating junction temperature of $175^\circ\text{C}$ and gives thermal data including $R_{\text{thJC}} = 0.53^\circ\text{C}/\text{W}$ for the IGBT junction-to-case path [STGWA40HP65FB Datasheet].

Those two numbers immediately show that the device rating is thermal as well as electrical. The junction can rise only a limited amount above the case, and the allowable power dissipation depends on that temperature rise.

If the case is held at $90^\circ\text{C}$, the available junction rise to the absolute maximum is

$$175 - 90 = 85^\circ\text{C}.$$

Using Equation (9.5), the corresponding approximate allowable steady dissipation across the junction-to-case path is

$$P \approx \frac{85}{0.53} \approx 160 \text{ W}.$$

This is an interpretation of the junction-to-case limit, not a recommended operating target. It simply shows how strongly the allowable dissipation depends on case temperature.

### Step 2: Do not misread the power-dissipation rating

The same datasheet lists total power dissipation of $283 \text{ W}$ at $T_C = 25^\circ\text{C}$ [STGWA40HP65FB Datasheet].

That number is conditional. It assumes a very cool case and therefore strong heat removal. It does not mean that a bare TO-247 package in still air can dissipate 283 W continuously.

Figure 1 in the datasheet, "Power dissipation vs case temperature," makes the condition explicit [STGWA40HP65FB Datasheet]. As case temperature rises, the allowable dissipation falls. Thermal rating is therefore conditional, not absolute.

### Step 3: Connect electrical loss to thermal behavior

The datasheet gives static and switching data that can be used in loss estimation:

- $V_{CE(\text{sat})}$ is around $1.6 \text{ V}$ typ. at one stated operating point,
- typical turn-off energy is given for stated current, voltage, gate resistance, and temperature,
- Figure 17 shows switching energy increasing with junction temperature [STGWA40HP65FB Datasheet].

Electrical loss and thermal behavior are therefore coupled. If junction temperature rises, switching energy may rise as well, which increases dissipation and further raises device temperature.

### Step 4: Use the thermal-impedance curve correctly

Figure 25 in the datasheet presents thermal impedance in normalized form, showing that transient thermal response depends on pulse duration and duty ratio [STGWA40HP65FB Datasheet]. One static resistance value is not sufficient for every operating condition.

If the device sees short overload pulses, the immediate junction temperature rise is governed by transient thermal impedance, not only by the steady-state heat-sink resistance.

### Step 5: Translate the datasheet into design questions

Table 9.4: Reading the STGWA40HP65FB for thermal meaning

| Datasheet item | What it means in plain language | Why it matters thermally |
|---|---|---|
| $T_J = 175^\circ\text{C}$ max | The silicon cannot safely exceed this limit | Sets the absolute ceiling for thermal design |
| $R_{\text{thJC}} = 0.53^\circ\text{C}/\text{W}$ | Heat still sees resistance even before leaving the package | Affects junction rise for every watt dissipated |
| $P_{\text{TOT}} = 283 \text{ W}$ at $T_C = 25^\circ\text{C}$ | Large dissipation is possible only with a cool case | Prevents misreading the package as self-cooling |
| Figure 1: power dissipation vs case temperature | Hotter case means less allowable dissipation | Shows why heat sink and airflow are decisive |
| Figure 17: switching energy vs temperature | Switching loss changes with junction temperature | Electrical and thermal design interact |
| Figure 25: thermal impedance | Short pulses heat the die differently from steady power | Needed for pulsed-stress judgment |

The same questions should be asked of any power-device datasheet, not only this one.

## How this matters in renewable-energy systems

Thermal management is closely tied to renewable-energy hardware because these converters often operate for long hours, at significant current, and in warm outdoor or semi-enclosed environments. In solar PV systems, the MPPT stage and inverter stage both generate semiconductor loss continuously while rooftop temperature may already be high. In battery chargers and battery-energy-storage converters, thermal design affects efficiency, current capability, and charging reliability. Wind-energy interfaces, EV auxiliary converters, on-board chargers, and UPS systems all place similar pressure on junction temperature because power density, operating duration, and enclosure heating act together.

The larger design lesson is that efficiency and reliability meet in the thermal design. Junction temperature influences semiconductor lifetime, loss, allowable current, and safe operating margin. For many practical converters, the thermal design determines whether an electrically correct circuit remains reliable under real climate and enclosure conditions.

## Chapter summary

Thermal management begins with loss estimation. Conduction loss depends on ON-state resistance or ON-state voltage drop, switching loss depends on voltage-current overlap and switching energy, and both often increase as junction temperature rises. Electrical behavior and thermal behavior are therefore coupled rather than separate design problems.

Thermal design then converts loss into temperature rise through the path from junction to ambient. Equations (9.5) to (9.8) provide a first-pass method for steady-state junction-temperature estimation and heat-sink selection, while transient thermal impedance extends the analysis to pulsed operation. Natural convection, forced-air cooling, and liquid cooling differ mainly in how effectively they reduce the effective device-to-environment thermal resistance.

## Further reading

- M. H. Rashid, *Power Electronics: Circuits, Devices and Applications*, 4th ed. - A strong textbook source for introductory treatment of device losses, power conversion efficiency, and practical semiconductor behavior.
- Ned Mohan, Tore M. Undeland, and William P. Robbins, *Power Electronics: Converters, Applications and Design* - Especially useful for connecting device-loss concepts to converter operation and design tradeoffs.
- [STMicroelectronics, *AN4783: Thermal effects and junction temperature evaluation of Power MOSFETs*](https://www.st.com/resource/en/application_note/dm00241971-thermal-effects-and-junction-temperature-evaluation-of-power-mosfets-stmicroelectronics.pdf) - A very helpful application note on thermal resistance, thermal impedance, convection, and practical heat-sink thinking.
- [Infineon, *AN-1057: Heatsink Characteristics*](https://www.infineon.com/assets/row/public/documents/60/42/an-1057.pdf) - A concise practical reference for heat-sink terminology, interface resistance, and first-pass heat-sink selection.
- [STMicroelectronics, *STGWA40HP65FB Datasheet*](https://www.st.com/resource/en/datasheet/stgwa40hp65fb.pdf) - A real device datasheet that is especially useful for learning how thermal ratings, power dissipation, switching energy, and transient thermal impedance are presented in practice.
