# Chapter 2.4: Thermal Management

## Chapter opening

So far in Module 2, we have asked three practical questions about a power semiconductor. How do we drive it? How do we soften its switching transients? How do we protect it during abnormal voltage and current conditions? Thermal management adds a fourth question, and in many ways it is the question that decides whether a converter survives everyday operation: **where does the heat go?**

This chapter matters because power semiconductors do not fail only during dramatic faults. They also suffer when they run too hot, too often, or with too little thermal margin. A converter may switch correctly, produce the right output voltage, and still age prematurely if the junction temperature stays too high. In a solar inverter on a hot afternoon, an EV auxiliary converter under bonnet heat, a battery charger inside a compact cabinet, or a UPS operating for long backup intervals, thermal stress is not a side issue. It is part of normal design.

There is also an important psychological shift here for the self-learner. Until now, many chapters have focused on electrical behavior: voltage, current, switching waveforms, and protection thresholds. Thermal management teaches us that electrical loss must finally appear as heat, and that heat must move through real materials such as silicon, copper, package molding, thermal grease, aluminum heat sinks, and air. Once you see that path clearly, many datasheet numbers that used to look abstract, such as junction temperature, thermal resistance, and power dissipation, begin to make physical sense.

In this chapter we will first study where power loss comes from inside semiconductor devices, especially **conduction loss** and **switching loss**. Then we will build the thermal-resistance model used for simple heat-sink selection, including the meaning of junction-to-case, case-to-sink, and sink-to-ambient thermal resistance [ST AN4783], [Infineon AN-1057]. Finally, we will look at **forced cooling** at overview level and ask when natural cooling stops being enough. These ideas prepare us for the converter chapters ahead, because every chopper, inverter, and rectifier chapter that follows assumes devices that can carry their electrical duty without exceeding their thermal limits.

## Prerequisites check

- You should remember from Chapters 1.4 and 1.5 that MOSFETs and IGBTs do not switch instantaneously, so voltage and current overlap during switching.
- You should remember from Chapter 2.1 that stronger or weaker gate drive changes switching speed, and therefore affects switching loss.
- You should remember from Chapter 2.2 that snubbers can reduce overshoot and ringing, but they may also dissipate power.
- You should be comfortable with basic power relation $P = VI$ and, for a resistor, $P = I^2R$.
- You should know the difference between ambient temperature and device temperature, even if the thermal-resistance model is still new.

If switching waveforms feel uncertain, review Chapter 2.1 before going deeper. If the idea of repetitive switching loss feels vague, Chapters 1.4, 1.5, and 2.2 will support this chapter well.

## Core content

### 2.4.1 Power losses in semiconductor devices: conduction and switching losses (qualitative)

#### Why a "high-efficiency" converter still gets hot

Let us begin with a small but realistic numerical picture.

Suppose a DC-DC converter in a battery charger processes $1 \text{ kW}$ at $95\%$ efficiency. That sounds excellent, and it is. But it still means that

$$P_{\text{loss}} = P_{\text{in}} - P_{\text{out}} = 1000 - 950 = 50 \text{ W}.$$

Fifty watts is not a small number inside a compact enclosure. It is the heat of a small soldering iron, continuously generated inside the converter. That heat does not disappear because the circuit is efficient. It must pass out of the semiconductor junctions, through the package and heat sink, and finally into the surrounding air.

This is the first key idea of thermal management:

Electrical loss becomes heat inside the device, and the device temperature rises unless that heat is removed fast enough [Rashid, *Power Electronics: Circuits, Devices and Applications, 4e*], [ST AN4783].

In power semiconductors, two loss categories dominate introductory thermal analysis:

- **Conduction loss**: loss while the device is carrying current in its ON state.
- **Switching loss**: loss during the finite interval in which the device is changing state.

Different devices express these losses differently. A MOSFET mainly shows conduction loss through its ON-state resistance. An IGBT or diode often shows it through an approximate ON-state voltage drop. A high-frequency converter may be limited mainly by switching loss. A low-frequency high-current converter may be limited mainly by conduction loss. Good thermal thinking begins by asking which of these losses is dominant in the intended operating condition [Mohan, Undeland, Robbins, *Power Electronics*].

#### Conduction loss

When a semiconductor is ON, it is never a perfect short circuit. There is always some voltage drop or resistance in the current path. So if current flows, power is dissipated.

For a MOSFET, the simplest introductory conduction-loss estimate is

$$\boxed{P_{\text{cond,MOSFET}} \approx I_{\text{rms}}^2 R_{DS(\text{on})}} \quad \text{(9.1)}$$

where $I_{\text{rms}}$ is the RMS current through the device during the interval of interest and $R_{DS(\text{on})}$ is the MOSFET ON-state resistance.

This equation is important because it shows a square-law effect with current. If current doubles, the conduction loss becomes roughly four times larger.

Consider a low-voltage MOSFET in a 48 V to 12 V converter carrying an RMS current of $10 \text{ A}$. If its effective ON resistance at operating temperature is $25 \text{ m}\Omega$, then

$$P_{\text{cond,MOSFET}} \approx 10^2 \times 0.025 = 2.5 \text{ W}.$$

If the RMS current rises to $20 \text{ A}$ under heavier load, the conduction loss becomes

$$P_{\text{cond,MOSFET}} \approx 20^2 \times 0.025 = 10 \text{ W}.$$

The current only doubled, but the loss quadrupled. That is why thermal design becomes much more demanding as current rises.

For an IGBT or a diode, a simple first estimate often uses ON-state voltage drop:

$$\boxed{P_{\text{cond}} \approx V_{\text{ON}} I_{\text{avg}}} \quad \text{(9.2)}$$

where $V_{\text{ON}}$ may be $V_{CE(\text{sat})}$ for an IGBT or $V_F$ for a diode, and $I_{\text{avg}}$ is the average current during conduction.

This is less exact than a full waveform calculation, but it is very useful at beginner level. If an IGBT in a small inverter leg has an average ON-state drop of about $1.8 \text{ V}$ at the relevant current and it carries an average current of $6 \text{ A}$ over its conduction interval, then its approximate conduction loss is

$$P_{\text{cond}} \approx 1.8 \times 6 = 10.8 \text{ W}.$$

Notice the contrast:

- MOSFET conduction loss is often thought of as "resistive."
- IGBT and diode conduction loss are often thought of as "voltage-drop times current."

That distinction is not absolute in advanced modeling, but it is a very helpful first mental model [Mohan, Undeland, Robbins, *Power Electronics*], [Rashid, *Power Electronics: Circuits, Devices and Applications, 4e*].

#### Why conduction loss usually rises with temperature

Thermal management is not only about loss causing temperature rise. Temperature can also change the loss itself.

For many power MOSFETs, $R_{DS(\text{on})}$ increases as junction temperature rises. For many IGBTs, $V_{CE(\text{sat})}$ also shifts with temperature. The STGWA40HP65FB datasheet, for example, shows $V_{CE(\text{sat})}$ increasing with junction temperature in its static characteristics and Figure 5, which means hotter operation tends to increase conduction loss further [STGWA40HP65FB Datasheet].

This produces an important practical loop:

1. Current causes loss.
2. Loss causes temperature rise.
3. Temperature rise often increases ON-state loss.

This is one reason thermal margin matters. A design that looks acceptable at room temperature may become less comfortable after the semiconductor has already heated up.

#### Switching loss

A beginner often imagines switching in an ideal way: current is zero, then suddenly nonzero; voltage is high, then suddenly low. In a real device, the change takes time. During that short interval, there is simultaneous voltage across the device and current through it. That overlap creates power loss.

The simplest physical estimate is

$$\boxed{P_{\text{sw,approx}} \approx \frac{1}{2} V I (t_{\text{on}} + t_{\text{off}}) f_s} \quad \text{(9.3)}$$

where $V$ is the approximate device voltage during switching, $I$ is the current being switched, $t_{\text{on}}$ and $t_{\text{off}}$ are the effective switching intervals, and $f_s$ is switching frequency.

This equation is only a first estimate, but it teaches the correct trends:

- higher voltage increases switching loss,
- higher current increases switching loss,
- slower switching increases switching loss,
- higher switching frequency increases switching loss directly.

Suppose an IGBT in a converter connected to a rectified 230 V, 50 Hz supply sees about $325 \text{ V}$ during the important switching interval, switches about $8 \text{ A}$, has total effective overlap time $(t_{\text{on}} + t_{\text{off}})$ of $200 \text{ ns}$, and operates at $20 \text{ kHz}$. Then

$$P_{\text{sw,approx}} \approx \frac{1}{2}\times 325 \times 8 \times 200 \times 10^{-9} \times 20 \times 10^3 \approx 5.2 \text{ W}.$$

That is already comparable to the conduction loss of many practical devices.

In real design, datasheets often give switching energy directly, which is even more useful:

$$\boxed{P_{\text{sw}} \approx f_s (E_{\text{on}} + E_{\text{off}})} \quad \text{(9.4)}$$

where $E_{\text{on}}$ and $E_{\text{off}}$ are the turn-ON and turn-OFF energy values per switching event, measured under stated test conditions. This form is common in IGBT and SiC MOSFET practice because energy per event is easy to scale with frequency.

The STGWA40HP65FB datasheet gives a typical turn-off energy of about $363\,\mu\text{J}$ at $V_{CC}=400 \text{ V}$, $I_C=40 \text{ A}$, $R_G=5\,\Omega$, and $T_J=25^\circ\text{C}$, rising to about $764\,\mu\text{J}$ at $175^\circ\text{C}$ under the same nominal electrical test conditions [STGWA40HP65FB Datasheet]. That one comparison alone teaches a deep lesson: switching loss is not fixed. It depends on temperature, current, voltage, and gate resistance.

#### The balance between conduction loss and switching loss

At this stage, it helps to pause and compare the two loss mechanisms.

Table 9.1: Conduction and switching losses compared

| Loss type | When it appears | Main physical cause | Usually worsens with |
|---|---|---|---|
| Conduction loss | While the device is ON | ON-state resistance or ON-state voltage drop | Higher current, higher device temperature |
| Switching loss | During turn-ON and turn-OFF | Voltage-current overlap during finite switching time | Higher voltage, higher current, higher frequency, slower switching |

This table explains several design choices we have already seen in earlier chapters.

A stronger gate driver from Chapter 2.1 can reduce switching time and therefore reduce switching loss, but it may increase $dv/dt$, $di/dt$, and EMI if taken too far. A snubber from Chapter 2.2 can reduce overshoot and stress, but it may dissipate additional power. A protection feature from Chapter 2.3 can save the device during faults, but even in normal operation the device still needs a thermal path that can continuously remove its ordinary losses.

So thermal management is not separate from the rest of power electronics. It is where the consequences of many earlier design decisions finally accumulate.

#### Common misconceptions about semiconductor loss

Three misconceptions are especially worth removing here.

The first is that only inefficient converters need thermal design. Even a highly efficient converter can generate tens of watts or hundreds of watts of heat at useful power levels.

The second is that switching loss matters only at very high frequency. In practice, even tens of kilohertz can make switching loss important when bus voltage and current are large.

The third is that datasheet current rating can be read without thermal context. A device current rating is always tied to some temperature condition, such as case temperature or mounting condition. The STGWA40HP65FB datasheet, for example, gives continuous collector current values at specified case temperatures, not in a thermal vacuum [STGWA40HP65FB Datasheet].

**Image prompt for Figure 9.1:** Create a clean textbook-style technical figure showing power loss in a switching semiconductor. Use three aligned time plots versus time: device voltage, device current, and instantaneous power. Mark one conduction interval where current flows with low but nonzero ON-state voltage, and a switching interval where voltage and current overlap to create a clear power pulse. Label "conduction loss," "turn-ON switching loss," and "turn-OFF switching loss." Use monochrome engineering style with clear axes, units, and annotations.

*Renewable-energy relevance.* In PV MPPT converters and battery chargers, high current often makes conduction loss important. In PV inverters, wind converters, and EV auxiliary power stages, switching loss becomes especially important because switching frequency and bus voltage are both significant. Thermal management begins by knowing which loss mechanism is dominating the application.

### 2.4.2 Thermal resistance, heat-sink selection - simple design approach

#### The thermal path from junction to ambient

Let us start with a physical picture rather than a formula.

Inside a power device, the silicon **junction** is where heat is generated. That heat then travels outward through the package to the **case**, then across some mounting interface such as thermal grease or an insulating pad, then into the **heat sink**, and finally into the surrounding **ambient** air. If any part of that path is poor, the junction temperature rises.

ST describes thermal analysis through an electrical analogy: temperature difference behaves like voltage difference, heat flow behaves like current, and thermal resistance behaves like electrical resistance [ST AN4783]. That analogy leads to the most important beginner equation in this chapter:

$$\boxed{\Delta T = P_{\text{loss}} R_{\text{th}}} \quad \text{(9.5)}$$

where $\Delta T$ is temperature rise across a thermal path, $P_{\text{loss}}$ is the heat flow in watts, and $R_{\text{th}}$ is thermal resistance in $^\circ\text{C}/\text{W}$.

This equation is wonderfully simple. If a device dissipates more power, the temperature rise becomes larger. If the thermal resistance is reduced, the temperature rise becomes smaller.

For example, if a certain part of the thermal path has $R_{\text{th}} = 2^\circ\text{C}/\text{W}$ and the power flowing through it is $10 \text{ W}$, then the temperature rise across that part is

$$\Delta T = 10 \times 2 = 20^\circ\text{C}.$$

That is the whole logic of heat-sink selection in its simplest form.

#### The main thermal-resistance terms

The terms used in datasheets and heat-sink notes can look intimidating at first, so let us slow them down.

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

Infineon AN-1057 uses the same series-path idea and defines junction-to-case, case-to-sink, and sink-to-ambient thermal resistances in a very practical way [Infineon AN-1057]. ST AN4783 makes the same point and gives the combined relation:

$$\boxed{R_{\text{thJA}} = R_{\text{thJC}} + R_{\text{thCS}} + R_{\text{thSA}}} \quad \text{(9.6)}$$

for the simple series thermal path when a device is mounted on a heat sink [ST AN4783].

That leads directly to the steady-state junction-temperature estimate

$$\boxed{T_j \approx T_a + P_{\text{tot}}(R_{\text{thJC}} + R_{\text{thCS}} + R_{\text{thSA}})} \quad \text{(9.7)}$$

where $P_{\text{tot}}$ is total average device loss.

Equation (9.7) is the heart of introductory heat-sink selection.

**Image prompt for Figure 9.2:** Create a clean textbook-style thermal-path illustration for a power semiconductor mounted on a heat sink. Show, from left to right, semiconductor junction at temperature $T_j$, package case at $T_c$, thermal interface material, heat sink, and ambient air at $T_a$. Mark the thermal resistances $R_{\text{thJC}}$, $R_{\text{thCS}}$, and $R_{\text{thSA}}$. Add arrows showing heat flow outward and include the equation $T_j = T_a + P_{\text{tot}}(R_{\text{thJC}} + R_{\text{thCS}} + R_{\text{thSA}})$. Use monochrome engineering style.

#### A simple heat-sink selection method

Now we can turn the ideas above into a beginner-friendly design procedure.

1. Estimate the worst-case total power loss in the device, $P_{\text{tot}}$.
2. Decide the highest junction temperature you are willing to allow in design.
3. Decide the worst-case ambient temperature around the heat sink.
4. Read the device thermal data from the datasheet, especially $R_{\text{thJC}}$ and maximum $T_j$.
5. Estimate the interface thermal resistance $R_{\text{thCS}}$.
6. Solve for the largest allowable sink-to-ambient thermal resistance.

Rearranging Equation (9.7), we obtain

$$\boxed{R_{\text{thSA,max}} \approx \frac{T_{j,\text{target}} - T_a}{P_{\text{tot}}} - R_{\text{thJC}} - R_{\text{thCS}}} \quad \text{(9.8)}$$

This is the most useful equation in a first heat-sink calculation.

#### Numerical example: choosing a heat sink for a single IGBT

Suppose a 650 V IGBT in a small UPS inverter or PV auxiliary converter is expected to dissipate about $20 \text{ W}$ at worst case. Let us use a conservative design target of $T_{j,\text{target}} = 125^\circ\text{C}$, even though some devices allow a higher absolute maximum. Let the ambient air near the heat sink be $45^\circ\text{C}$, which is realistic for a warm enclosure in Indian summer conditions. Suppose the device datasheet gives $R_{\text{thJC}} = 0.53^\circ\text{C}/\text{W}$, as the STGWA40HP65FB datasheet does for the IGBT junction-to-case path [STGWA40HP65FB Datasheet]. Let us assume $R_{\text{thCS}} = 0.5^\circ\text{C}/\text{W}$ for the interface layer.

Using Equation (9.8),

$$R_{\text{thSA,max}} \approx \frac{125 - 45}{20} - 0.53 - 0.5.$$

First calculate the total allowable junction-to-ambient resistance:

$$\frac{80}{20} = 4^\circ\text{C}/\text{W}.$$

Now subtract the device and interface contributions:

$$R_{\text{thSA,max}} \approx 4 - 0.53 - 0.5 = 2.97^\circ\text{C}/\text{W}.$$

So we need a heat sink whose sink-to-ambient thermal resistance is roughly $3^\circ\text{C}/\text{W}$ or lower under the actual airflow condition.

That result already tells us something useful. If a candidate natural-convection heat sink is rated at $5^\circ\text{C}/\text{W}$, it is not good enough for this design. If a forced-air arrangement reduces the effective sink-to-ambient thermal resistance to about $2^\circ\text{C}/\text{W}$, then the design becomes much more comfortable.

This is why thermal design is often an exercise in subtraction. The semiconductor and interface already consume part of the allowable temperature rise. The heat sink must fit into whatever thermal budget remains.

#### Why design margin matters

The equation above invites a practical question. Why did we choose $125^\circ\text{C}$ rather than the absolute maximum junction temperature?

The answer is that a practical design usually wants margin for tolerance, aging, dust, airflow uncertainty, thermal-cycling stress, and unexpected overload. This is engineering practice rather than a universal single-number rule. Running continuously very near the absolute limit may be technically possible but rarely feels wise in long-life renewable-energy equipment.

#### The role of the interface layer

Beginners sometimes focus only on the heat sink and forget the case-to-sink interface. That is a mistake.

Real device packages and real heat sinks are not perfectly flat, and air trapped between them is a poor thermal conductor. A **thermal interface material**, or TIM, fills surface gaps and lowers thermal resistance. ST notes that grease or insulating layers such as mica, ceramic, or silicone can be used, and that contact pressure matters because the case-to-heat-sink resistance is introduced by real, nonideal contact surfaces [ST AN4783].

So a large heat sink can still perform badly if:

- the mounting surface is uneven,
- the TIM is poor or badly applied,
- the mounting pressure is inadequate,
- the designer assumes an optimistic $R_{\text{thCS}}$ without checking the real interface.

The heat sink is only one piece of the thermal path.

#### Steady-state thermal resistance versus transient thermal impedance

Until now we have used steady-state resistance. That is correct for continuous average heating. But semiconductor heating is not always steady. Fault pulses, startup surges, current bursts, and intermittent overloads can be short compared with the thermal time constant of the package and heat sink.

For those cases, datasheets provide **transient thermal impedance**, usually written as $Z_{\text{th}}(t)$. ST AN4783 explains that short pulses should be evaluated with thermal-impedance curves rather than only steady thermal resistance, because the thermal capacitance of the structure delays the temperature rise [ST AN4783]. The STGWA40HP65FB datasheet makes the same point with its Figure 25, where the transient thermal response is shown using a normalized relation $Z_{\text{th}} = k \cdot R_{\text{thJC}}$ for different duty conditions [STGWA40HP65FB Datasheet].

At beginner level, the safest conclusion is this:

- use $R_{\text{th}}$ for steady or average heating,
- use $Z_{\text{th}}(t)$ when short pulses matter.

You do not need advanced thermal simulation to appreciate that distinction.

#### Common misconceptions in heat-sink selection

Several misconceptions cause confusion in early thermal study.

The first is that $R_{\text{thJA}}$ from a datasheet always describes the finished product. It does not. ST specifically notes that junction-to-ambient values are tied to stated conditions and that real heat-sink mounting introduces separate case-to-heat-sink and heat-sink-to-ambient terms [ST AN4783].

The second is that a datasheet power-dissipation rating can be read without looking at the temperature condition. A device might be listed as being able to dissipate a large number of watts, but that number is often tied to a low case temperature that already assumes strong cooling.

The third is that heat sinks are universal objects with fixed performance. In reality, heat-sink thermal resistance depends on orientation, surface area, finish, airflow, and enclosure condition [ST AN4783], [Infineon AN-1057].

*Renewable-energy relevance.* Heat-sink selection is central in PV string inverters, battery chargers, DC-DC MPPT converters, and EV auxiliary converters because these systems often run for long hours at elevated ambient temperature. A design that is electrically correct but thermally under-designed may work on the lab bench and fail in the field.

### 2.4.3 Forced cooling - overview

#### Why natural cooling is sometimes not enough

Natural cooling is attractive because it is simple, silent, and has no moving parts. If the semiconductor losses are modest and the available heat-sink area is generous, natural convection may be enough.

But power-electronic equipment is often compact, enclosed, and required to operate in warm surroundings. In such a case, the allowable heat-sink size may be limited, and the sink-to-ambient thermal resistance may not become low enough without moving air. That is when **forced cooling** enters the design.

ST AN4783 explains convection as one of the main heat-transfer modes and distinguishes:

- **natural convection**, where airflow is created by buoyancy due to temperature differences,
- **forced convection**, where airflow is created by external means such as a fan or pump [ST AN4783].

The basic convection relation is

$$\boxed{R_{\text{th}} \approx \frac{1}{h_c A_s}} \quad \text{(9.9)}$$

where $h_c$ is the heat-transfer coefficient and $A_s$ is the effective heat-transfer surface area [ST AN4783].

Equation (9.9) is useful even if you never calculate with it numerically. It tells us that thermal resistance becomes smaller when:

- the surface area becomes larger,
- the heat-transfer coefficient becomes larger.

A fan mainly improves the second factor. It increases the heat-transfer coefficient by pushing more air past the fins.

#### What forced-air cooling changes in practice

When airflow increases, the heat sink can reject more heat for the same temperature rise. This means one of two things becomes possible:

- the same heat sink can carry more power,
- or a smaller heat sink can carry the same power.

That is why forced-air cooling is common in compact UPS systems, EV chargers, telecom rectifiers, and medium-power PV inverter cabinets.

But forced cooling is not free. Once we add a fan, new engineering questions appear:

- What happens if the fan fails?
- How much dust will accumulate on the fins?
- What is the acoustic noise?
- Is the airflow path blocked by wiring or cabinet geometry?
- Does the design need airflow monitoring or thermal shutdown backup?

So a fan improves thermal performance, but it also introduces maintenance and reliability questions that natural convection avoids.

#### Layout and enclosure details still matter

A beginner might think forced cooling solves everything. It does not.

ST gives practical recommendations that are easy to remember [ST AN4783]:

- fins should be vertically aligned for natural-convection cooling,
- airflow should not be blocked,
- heat-generating devices should not be placed where hot air accumulates without escape,
- forced-air flow should be arranged to follow sensible natural-convection paths.

These are simple observations, but they matter a great deal in real converter cabinets. A good heat sink can perform badly inside a poor airflow path.

#### Beyond forced air: a brief word on liquid cooling

At this syllabus level, we do not need detailed liquid-cooling design. But it is useful to know where the idea fits.

When power density becomes very high, as in larger EV chargers, traction inverters, and some high-power battery or renewable-energy converters, liquid cooling may be used because it can remove heat more effectively than air in a compact volume. The thermal logic is the same as before: lower the thermal resistance from the device to the environment. Only the final heat-removal medium changes.

For this chapter, the important lesson is simply that cooling method is part of converter architecture, not only afterthought hardware.

#### Comparing the main cooling approaches

Table 9.3: Cooling approaches at beginner level

| Cooling approach | Main strengths | Main limitations | Typical fit |
|---|---|---|---|
| Natural convection | Simple, quiet, no moving parts, higher mechanical reliability | Larger heat sink often needed, performance falls in cramped hot enclosures | Small chargers, low-power converters, open enclosures |
| Forced-air cooling | Better heat removal for size, lower effective sink-to-ambient thermal resistance | Fan failure, dust, noise, extra power use | UPS systems, inverter cabinets, compact medium-power converters |
| Liquid cooling | Very high heat-removal capability in compact space | Higher cost, complexity, pump and sealing concerns | High-power EV and industrial converters |

#### Common misconceptions about forced cooling

The first misconception is that a fan means the heat sink no longer matters. In reality, the heat sink and airflow path must be designed together.

The second is that airflow is a purely thermal issue. It is also a reliability issue because fans age, filters clog, and dust changes cooling performance over time.

The third is that ambient temperature means outdoor weather alone. In converter practice, the local ambient around the heat sink may be much higher than room temperature because the enclosure already contains other hot components.

**Image prompt for Figure 9.3:** Create a clean textbook-style comparison figure showing the same finned heat sink under natural convection and forced-air cooling. On the left, show warm air rising naturally between vertical fins. On the right, show a fan pushing air across the fins. Label "natural convection," "forced convection," "airflow direction," "heat sink fins," and "lower effective sink-to-ambient thermal resistance with stronger airflow." Use monochrome engineering style with arrows and temperature labels, not decorative graphics.

*Renewable-energy relevance.* Forced cooling appears in many practical renewable-energy systems because compact packaging and high ambient temperature are common. PV inverter cabinets, battery-energy-storage converters, EV chargers, and UPS systems often rely on controlled airflow to keep semiconductor junction temperatures within safe margin.

## Worked interpretation exercise

We will read a real artifact closely matched to this chapter:

- the [STGWA40HP65FB datasheet](https://www.st.com/resource/en/datasheet/stgwa40hp65fb.pdf)

This is a good learning artifact because it brings together thermal limit, thermal resistance, conduction behavior, switching energy, and transient thermal information in one real power-device datasheet [STGWA40HP65FB Datasheet].

### Step 1: Read the thermal limit before reading the current rating

The datasheet states a maximum operating junction temperature of $175^\circ\text{C}$ and gives thermal data including $R_{\text{thJC}} = 0.53^\circ\text{C}/\text{W}$ for the IGBT junction-to-case path [STGWA40HP65FB Datasheet].

Those two numbers immediately tell us the device is not only an electrical switch. It is also a thermal system. The junction can only be allowed to rise by a limited amount above the case, and the allowed power dissipation depends on that temperature rise.

For example, if the case is held at $90^\circ\text{C}$, the available junction rise to the absolute maximum is

$$175 - 90 = 85^\circ\text{C}.$$

Using the simple steady relation from Equation (9.5), the corresponding approximate allowable steady dissipation across the junction-to-case path would be

$$P \approx \frac{85}{0.53} \approx 160 \text{ W}.$$

That is not a recommended operating target. It is a thermal interpretation of the datasheet numbers. The main lesson is that the case temperature matters enormously.

### Step 2: Do not misread the power-dissipation rating

The same datasheet lists total power dissipation of $283 \text{ W}$ at $T_C = 25^\circ\text{C}$ [STGWA40HP65FB Datasheet]. A beginner may read that and think, "This device can always dissipate 283 W."

That is the wrong reading.

The correct reading is that this number is tied to a case temperature of only $25^\circ\text{C}$. In other words, strong cooling is already assumed. The device is not promising that a bare TO-247 package in still air can safely burn 283 W continuously.

This is exactly why Figure 1 in the datasheet, "Power dissipation vs case temperature," is so educational [STGWA40HP65FB Datasheet]. As the case temperature rises, the allowable dissipation falls. Thermal rating is therefore conditional, not absolute.

### Step 3: Connect electrical loss to thermal behavior

The datasheet gives typical static and switching data that help estimate loss:

- $V_{CE(\text{sat})}$ is around $1.6 \text{ V}$ typ. at one stated operating point,
- typical turn-off energy is given for stated current, voltage, gate resistance, and temperature,
- Figure 17 shows switching energy increasing with junction temperature [STGWA40HP65FB Datasheet].

This means the thermal story is not separate from the electrical story. If junction temperature rises, switching energy can rise too. So the device may heat more strongly once it is already hot. That is exactly the sort of coupling thermal management tries to keep under control.

### Step 4: Use the thermal-impedance curve correctly

Figure 25 in the datasheet presents thermal impedance in normalized form, showing that transient thermal response depends on pulse duration and duty ratio [STGWA40HP65FB Datasheet]. This is a reminder not to use only one static number for every situation.

If the device sees short overload pulses, the immediate junction temperature rise is governed by transient thermal impedance, not only by the steady-state heat-sink resistance. This is why transient curves appear in serious power-device datasheets.

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

The most important learning habit is not to memorize this part number. The real habit is to ask, whenever you read any power-device datasheet:

- What is the maximum junction temperature?
- What is the junction-to-case thermal resistance?
- Under what temperature condition is the power-dissipation rating stated?
- Do the electrical loss parameters change with temperature?
- Is there a transient thermal-impedance curve for pulsed operation?

If you can answer those questions, you are already reading the datasheet like a power-electronics designer rather than only a component buyer.

## How this matters in renewable-energy systems

Thermal management is deeply connected to renewable-energy hardware because renewable-energy converters often operate for long hours, at significant current, and in warm outdoor or semi-enclosed environments.

In **solar PV systems**, the DC-DC MPPT stage and the inverter stage both generate semiconductor loss continuously while rooftop temperature may already be high. In **battery chargers** and **battery-energy-storage converters**, thermal design affects efficiency, current capability, and charging reliability. In **wind-energy interfaces**, converter cabinets may face both power-cycling stress and enclosure-temperature rise. In **EV auxiliary converters** and **on-board chargers**, compact packaging pushes designers toward careful heat-sink selection, forced air, or liquid cooling. In **UPS systems**, long backup operation can turn a short thermal event into a sustained one, so average-loss and airflow assumptions must be realistic.

There is also a larger lesson here. Renewable-energy systems are expected to be efficient, but they are also expected to be dependable. Good thermal design is one of the places where those two goals meet. It protects semiconductor lifetime, stabilizes electrical performance, and often determines whether a converter remains reliable in real climate and enclosure conditions.

## Chapter summary

- Power-semiconductor losses finally appear as heat, so every converter needs a thermal path from junction to ambient [ST AN4783].
- The two main beginner-level loss categories are **conduction loss** and **switching loss**.
- For a MOSFET, a useful first conduction-loss estimate is
  $\boxed{P_{\text{cond,MOSFET}} \approx I_{\text{rms}}^2 R_{DS(\text{on})}}$ from Equation (9.1).
- For an IGBT or diode, a useful first estimate is
  $\boxed{P_{\text{cond}} \approx V_{\text{ON}} I_{\text{avg}}}$ from Equation (9.2).
- A simple first switching-loss estimate is
  $\boxed{P_{\text{sw,approx}} \approx \tfrac{1}{2}VI(t_{\text{on}}+t_{\text{off}})f_s}$ from Equation (9.3).
- When datasheet switching energies are available, a practical estimate is
  $\boxed{P_{\text{sw}} \approx f_s(E_{\text{on}} + E_{\text{off}})}$ from Equation (9.4).
- Many electrical loss parameters worsen as junction temperature rises, so thermal and electrical behavior are coupled [STGWA40HP65FB Datasheet].
- Thermal analysis uses the relation
  $\boxed{\Delta T = P_{\text{loss}}R_{\text{th}}}$ from Equation (9.5).
- In a simple heat-sink path,
  $\boxed{R_{\text{thJA}} = R_{\text{thJC}} + R_{\text{thCS}} + R_{\text{thSA}}}$ from Equation (9.6) [ST AN4783].
- A useful steady-state junction-temperature estimate is
  $\boxed{T_j \approx T_a + P_{\text{tot}}(R_{\text{thJC}} + R_{\text{thCS}} + R_{\text{thSA}})}$ from Equation (9.7).
- A useful beginner heat-sink-selection equation is
  $\boxed{R_{\text{thSA,max}} \approx \frac{T_{j,\text{target}} - T_a}{P_{\text{tot}}} - R_{\text{thJC}} - R_{\text{thCS}}}$ from Equation (9.8).
- Thermal interface quality matters because poor contact or poor TIM increases case-to-sink thermal resistance [ST AN4783], [Infineon AN-1057].
- Short power pulses should be judged with **transient thermal impedance** $Z_{\text{th}}(t)$ rather than steady-state resistance alone [ST AN4783], [STGWA40HP65FB Datasheet].
- **Natural convection** uses buoyancy-driven airflow; **forced convection** uses a fan or pump and reduces effective sink-to-ambient thermal resistance [ST AN4783].
- The convection relation
  $\boxed{R_{\text{th}} \approx \frac{1}{h_c A_s}}$ from Equation (9.9) shows why more area and stronger airflow both help [ST AN4783].
- Thermal design in renewable-energy systems affects not only efficiency, but also reliability, lifetime, and safe operating margin.

## Further reading

- M. H. Rashid, *Power Electronics: Circuits, Devices and Applications*, 4th ed. - A strong textbook source for introductory treatment of device losses, power conversion efficiency, and practical semiconductor behavior.
- Ned Mohan, Tore M. Undeland, and William P. Robbins, *Power Electronics: Converters, Applications and Design* - Especially useful for connecting device-loss concepts to converter operation and design tradeoffs.
- [STMicroelectronics, *AN4783: Thermal effects and junction temperature evaluation of Power MOSFETs*](https://www.st.com/resource/en/application_note/dm00241971-thermal-effects-and-junction-temperature-evaluation-of-power-mosfets-stmicroelectronics.pdf) - A very helpful application note on thermal resistance, thermal impedance, convection, and practical heat-sink thinking.
- [Infineon, *AN-1057: Heatsink Characteristics*](https://www.infineon.com/assets/row/public/documents/60/42/an-1057.pdf) - A concise practical reference for heat-sink terminology, interface resistance, and first-pass heat-sink selection.
- [STMicroelectronics, *STGWA40HP65FB Datasheet*](https://www.st.com/resource/en/datasheet/stgwa40hp65fb.pdf) - A real device datasheet that is especially useful for learning how thermal ratings, power dissipation, switching energy, and transient thermal impedance are presented in practice.
