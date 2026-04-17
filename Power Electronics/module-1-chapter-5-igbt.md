# Chapter 1.5: IGBT

## Chapter opening

The **insulated-gate bipolar transistor**, or **IGBT**, combines a MOS insulated gate with bipolar current conduction. That combination made it one of the standard switches in medium- and high-power converters: the gate can be driven as a voltage-controlled input, while the conduction path avoids much of the high-voltage ON-resistance penalty of a comparable silicon MOSFET [Infineon IGBT Basic Know-How], [Infineon IGBTs Overview]. For that reason, IGBTs became common in industrial inverters, UPS systems, motor drives, traction converters, battery chargers, and many solar and wind power stages. This chapter examines the origin of the device, its internal structure, its static and switching characteristics, and its practical position relative to the power BJT and the power MOSFET.

## Core content

### 1.5.1 History of IGBT

The IGBT emerged from a specific limitation in high-voltage switching. In a three-phase inverter fed from a rectified 415 V supply, the DC link is often around $560 \text{ V}$ to $600 \text{ V}$. A high-voltage BJT can operate in this range, but it needs continuous base current and suffers from stored charge during turn-OFF. A high-voltage silicon MOSFET is easier to drive, but its ON resistance rises strongly as voltage rating increases. Designers therefore needed a device that combined an insulated gate with stronger high-voltage current conduction.

The IGBT provided that combination. It was invented by B. Jayant Baliga while he was working at General Electric. NC State University notes both the importance of the invention and the 1980 date commonly associated with it [NC State, Baliga Hall of Fame], [NC State, Pack Power].

The name itself describes the device. **Insulated-gate** indicates that control is applied through a MOS-like gate separated from the semiconductor by oxide. **Bipolar transistor** indicates that the vertical current path uses bipolar carrier action rather than majority-carrier conduction alone. The result is a hybrid device that keeps the high-input-impedance gate of the MOSFET while gaining the conduction advantage of bipolar behavior [Infineon IGBT Basic Know-How].

Table 5.1: The design gap that led to the IGBT

| Device | Main strength | Main limitation in power switching |
| --- | --- | --- |
| Power BJT | Good conduction capability at high voltage | Needs continuous base current; turn-off slowed by stored charge |
| Power MOSFET | Easy voltage drive and fast switching | High-voltage devices suffer rising $R_{DS(\mathrm{on})}$ |
| IGBT | Combines insulated gate with strong high-voltage current conduction | Turn-off is slower than MOSFET because of stored charge and tail current |

The IGBT did not replace every other power device. MOSFETs remain excellent at lower voltage and higher switching frequency, while thyristor-family devices remain important in very high-power or line-frequency applications. The IGBT instead became dominant in a wide middle range of industrial conversion. Infineon describes this range as extending into kilovolt classes and switching frequencies from a few kilohertz to the tens of kilohertz, which matches many motor-drive, UPS, PV-inverter, battery-charger, and wind-converter applications [Infineon IGBTs Overview]. The different conduction mechanism also explains why the ON state is described by $V_{CE(\mathrm{sat})}$ rather than by an ON resistance, and why turn-OFF exhibits tail current.

### 1.5.2 Structure, operating principle, output and transfer characteristics

#### Why the IGBT structure is different from a MOSFET

Like a vertical MOSFET, an IGBT uses a drift region to block voltage. Unlike a MOSFET, it introduces carrier injection into that drift region during conduction. The gate forms a channel in the body region, electrons enter from the emitter side, and the P+ collector injects holes into the drift region. The additional carriers raise the conductivity of the drift region, a phenomenon called **conductivity modulation** in power-device literature [Infineon IGBT Basic Know-How]. In practical terms, a high-voltage IGBT can conduct large current with a smaller ON-state penalty than a comparable high-voltage silicon MOSFET in many applications.

**Image prompt for Figure 5.1:** Create a clean textbook-style technical illustration of a vertical N-channel IGBT cross-section. Show emitter metallization at the top contacting repeated N+ emitter regions inside P-body regions. Show a gate insulated by silicon dioxide over the channel area. Below the body, show an N- drift region and a P+ collector layer at the bottom with collector metallization. Label emitter, gate, collector, N+ emitter, P-body, inversion channel, N- drift region, P+ collector, oxide, and indicate electron flow from emitter toward drift region and hole injection from collector toward drift region during conduction. Use monochrome engineering style with no decorative background.

Three structural features deserve emphasis. The **gate** is insulated from the semiconductor by oxide, so the steady-state input impedance is very high. The current path is vertical, which supports high current density and high blocking voltage. The bottom **P+ collector** layer injects carriers into the drift region during conduction, and that injection gives the device its bipolar character.

#### Basic operating principle

The main terminals of an IGBT are:

- **Gate (G)**
- **Collector (C)**
- **Emitter (E)**

For the common **N-channel IGBT**, the collector is usually at the high-potential side and the emitter at the lower-potential side.

The sequence of operation is:

1. With $V_{GE} = 0$, where $V_{GE}$ is gate-emitter voltage, no conducting channel exists in the body region, so the device is OFF and blocks collector-emitter voltage.
2. As $V_{GE}$ rises and exceeds the threshold value, a channel forms under the gate.
3. Electrons can then flow from emitter into the drift region.
4. This channel action supports bipolar carrier injection inside the vertical structure and greatly improves conduction.

The threshold voltage is written as $V_{GE(\mathrm{th})}$. As in the MOSFET, it marks the onset of conduction rather than the recommended drive condition for low-loss switching [Infineon Discrete IGBT Datasheet Explanation]. Many discrete IGBTs are characterized at about $15 \text{ V}$ gate drive in normal switching use [Infineon Discrete IGBT Datasheet Explanation], [Infineon IKW40N120H3 Datasheet].

#### ON-state behavior and saturation voltage

In power-circuit language, the IGBT ON state is usually described by its **collector-emitter saturation voltage**, written $V_{CE(\mathrm{sat})}$.

This already marks a difference from the MOSFET. A MOSFET in the ON state is usually described by $R_{DS(\mathrm{on})}$, whereas an IGBT is usually described by a voltage drop.

A first practical conduction-loss estimate is

$$\boxed{P_{\mathrm{cond}} \approx V_{CE(\mathrm{sat})} I_C} \quad \text{(5.1)}$$

where $P_{\mathrm{cond}}$ is conduction loss, $V_{CE(\mathrm{sat})}$ is the collector-emitter saturation voltage, and $I_C$ is collector current.

If the device conducts only for duty ratio $D$, then a simple average estimate is

$$\boxed{P_{\mathrm{cond,avg}} \approx D\,V_{CE(\mathrm{sat})} I_C} \quad \text{(5.2)}$$

Consider a medium-power inverter leg in which an IGBT has $V_{CE(\mathrm{sat})} = 2.1 \text{ V}$ at the operating current and carries $20 \text{ A}$ for 40% of the average switching cycle. Then

$$P_{\mathrm{cond,avg}} \approx 0.40 \times 2.1 \times 20 = 16.8 \text{ W}.$$

This estimate shows why the IGBT is attractive in medium-voltage converters: a few volts of ON-state drop may be acceptable at large current even when a comparable high-voltage MOSFET would incur a substantial resistance penalty. It also shows that an IGBT is not a zero-loss switch. A few volts at tens of amperes produces significant heat.

#### Output characteristics

The **output characteristics** plot collector current $I_C$ versus collector-emitter voltage $V_{CE}$ for several fixed values of gate-emitter voltage $V_{GE}$.

**Image prompt for Figure 5.2:** Create a textbook-style graph of N-channel IGBT output characteristics. Use horizontal axis collector-emitter voltage $V_{CE}$ in volts and vertical axis collector current $I_C$ in amperes. Draw a family of curves for increasing gate-emitter voltages such as 7 V, 9 V, 11 V, 13 V, and 15 V. Show that higher $V_{GE}$ allows higher collector current. Mark a low-$V_{CE}$ region labeled "on-state / saturation region in power-switching use" and a higher-$V_{CE}$ region labeled "active region." Use monochrome engineering style with clear curve labels.

The graph shows that the current capability rises strongly as $V_{GE}$ increases. In converter service, the important distinction is practical rather than purely device-theoretic: the IGBT must block voltage in the OFF state, carry current with acceptable loss in the ON state, and move safely between those states during switching.

#### Transfer characteristics

The **transfer characteristic** plots collector current $I_C$ as a function of gate-emitter voltage $V_{GE}$ at stated test conditions.

**Image prompt for Figure 5.3:** Create a clean textbook-style graph of IGBT transfer characteristics. Use horizontal axis gate-emitter voltage $V_{GE}$ in volts and vertical axis collector current $I_C$ in amperes. Show a curve with negligible current below threshold, then rapidly increasing current after threshold. Mark $V_{GE(th)}$, and add a note that practical power switching commonly uses gate drive around 15 V, not merely threshold voltage. Use monochrome engineering style.

The transfer characteristic shows how strongly the device turns ON as the gate voltage increases. It reinforces the distinction between threshold and full gate drive: threshold voltage marks the onset of measurable conduction under specified test conditions, whereas efficient power switching requires the intended drive level from the datasheet.

#### Input behavior and transconductance

Because the gate is insulated, the input behaves primarily as a capacitive load rather than a steady current load. Current is therefore required mainly during transitions, while charging or discharging the gate.

A useful quantity here is **transconductance**, written $g_{fs}$, which relates change in collector current to change in gate-emitter voltage under stated conditions:

$$\boxed{g_{fs} = \frac{\Delta I_C}{\Delta V_{GE}}} \quad \text{(5.3)}$$

This is not usually the first parameter used for converter loss estimation, but it shows that the gate still controls the output strongly even though the output current path itself is bipolar.

#### Positive temperature coefficient and paralleling

Modern IGBTs often show a **positive temperature coefficient** of $V_{CE(\mathrm{sat})}$ above a certain current range. Infineon notes that with newer Trenchstop technology, a 40 A device shows a positive temperature coefficient starting from about 10 A, which helps current sharing when devices are paralleled [Infineon Discrete IGBT Datasheet Explanation].

This behavior is useful in parallel operation because a hotter device tends to develop a higher ON-state drop and therefore give up some current to a cooler device. The effect is more favorable than the current-crowding tendency that makes parallel BJTs harder to manage. It is still not a license for careless paralleling: layout, gate resistance, stray inductance, and thermal matching remain important.

### 1.5.3 Switching characteristics, latch-up, SOA

#### Why IGBT switching is different from MOSFET switching

The IGBT gate is MOS-like, but the output conduction path is bipolar. Its switching behavior therefore combines familiar MOS-gate behavior with limits set by stored charge in the drift region.

Turn-ON begins when the gate is charged, a channel forms, and collector current rises. Turn-OFF is more difficult because stored charge remains in the device after the gate drive is removed. That stored charge produces the well-known **tail current**.

The standard switching intervals are:

- **Turn-on delay time $t_{d(\mathrm{on})}$**
- **Rise time $t_r$**
- **Turn-off delay time $t_{d(\mathrm{off})}$**
- **Fall time $t_f$**

These quantities are used in datasheets and follow IEC/JEDEC-style definitions under specified test circuits [Infineon Discrete IGBT Datasheet Explanation].

#### The turn-off tail current

The **tail current** is the slowly decaying current that persists during turn-OFF because stored charge in the bipolar conduction path must be removed. Infineon's datasheet-explanation note explicitly states that switching-loss timing for the IGBT takes the tail-current effect into account [Infineon Discrete IGBT Datasheet Explanation].

This is a fundamental tradeoff. A MOSFET can switch very fast because it is a majority-carrier device. An IGBT benefits from conductivity modulation during conduction, but the price is stored charge and a slower turn-OFF waveform.

**Image prompt for Figure 5.4:** Create a textbook-style switching waveform figure for an IGBT. Show three aligned plots versus time: gate-emitter voltage $V_{GE}$, collector current $I_C$, and collector-emitter voltage $V_{CE}$. Mark turn-on delay time $t_{d(on)}$, rise time $t_r$, turn-off delay time $t_{d(off)}$, and fall time $t_f$. In the turn-off current waveform, show a clear current tail after the main current fall and label it "tail current due to stored charge." Use monochrome engineering style and clear timing markers.

#### First estimate of switching loss

Because voltage and current overlap during switching, the device dissipates energy during each transition. A simple introductory approximation is

$$\boxed{E_{\mathrm{sw,approx}} \approx \frac{1}{2}V_{CC} I_C (t_r + t_f)} \quad \text{(5.4)}$$

where $V_{CC}$ is the DC-link or blocking voltage, $I_C$ is the switched current, and $t_r$ and $t_f$ are the rise and fall times.

The corresponding average switching-loss estimate is

$$\boxed{P_{\mathrm{sw,approx}} \approx f_s E_{\mathrm{sw,approx}}} \quad \text{(5.5)}$$

where $f_s$ is switching frequency.

These equations provide a useful first estimate, but they can understate turn-OFF loss when tail current is significant. For that reason, datasheets often provide measured switching energies directly:

- **turn-on energy $E_{\mathrm{on}}$**
- **turn-off energy $E_{\mathrm{off}}$**
- sometimes total switching energy $E_{\mathrm{ts}} = E_{\mathrm{on}} + E_{\mathrm{off}}$

Those values are measured under specified test conditions. They change with current, voltage, temperature, gate resistance, layout, and parasitics [Infineon Discrete IGBT Datasheet Explanation].

#### Gate charge and driver effort

Like the MOSFET, the IGBT gate must be charged and discharged. A useful first estimate for average gate-drive current is

$$\boxed{I_{G,\mathrm{avg}} \approx Q_G f_s} \quad \text{(5.6)}$$

where $Q_G$ is total gate charge.

If the gate swings through voltage $V_{GG}$, then a simple gate-drive power estimate is

$$\boxed{P_G \approx Q_G V_{GG} f_s} \quad \text{(5.7)}$$

Although the IGBT is voltage-driven, the driver is not effortless. Large devices and high switching frequencies still demand a capable gate driver.

#### Latch-up in the IGBT

The IGBT contains a parasitic thyristor structure because of its layered semiconductor arrangement. Under improper conditions, that parasitic structure can turn on. This unwanted condition is called **latch-up**.

Latch-up is not normal gate-controlled turn-ON. It is loss of normal control caused by triggering of the internal parasitic thyristor path. Research literature on IGBT structures analyzes this behavior explicitly [Solid-State Electronics, 1990, latch-up phenomena in IGBT structures].

Conditions that encourage latch-up include:

- excessive current density
- excessive $dI/dt$
- local hot spots
- insufficient latch-up immunity in the structure
- severe short-circuit or fault stress

Modern IGBTs are designed to be highly latch-up resistant in normal operation, but the concept remains important because it explains why current limits, short-circuit ratings, and safe operating area must be respected.

#### Safe operating area

The **safe operating area**, or **SOA**, gives the voltage-current combinations within which the device can operate safely under stated conditions.

For IGBTs, Infineon's datasheet-explanation note distinguishes two main forms [Infineon Discrete IGBT Datasheet Explanation]:

- **Forward-bias safe operating area (FBSOA)**
- **Reverse-bias safe operating area (RBSOA)**

FBSOA refers to safe conditions during forward-biased operation. RBSOA is especially relevant during turn-OFF with an inductive load, when the device experiences rising voltage and falling current at the same time.

Infineon notes that for state-of-the-art IGBTs, the RBSOA is often approximately square-shaped and bounded mainly by breakdown voltage and pulse current capability [Infineon Discrete IGBT Datasheet Explanation]. Even so, IGBT SOA remains limited by breakdown voltage, pulse current, junction temperature, stray inductance, gate-drive conditions, and switching overshoot.

#### Short-circuit withstand time

Many IGBTs specify a **short-circuit withstand time**, often written $t_{SC}$. This rating states how long the device can survive a specified short-circuit condition under stated gate drive, voltage, and temperature.

If a datasheet gives $t_{SC} = 10 \,\mu\text{s}$, the meaning is narrow and practical: under the specified test conditions, the protection system must clear the fault before that survival limit is exceeded. This rating directly influences gate-driver protection and fault-detection design in inverter systems.

#### Thermal relation

As with all power semiconductors, switching and conduction losses appear as heat. A basic thermal relation is

$$\boxed{T_J \approx T_C + P_D R_{\theta JC}} \quad \text{(5.8)}$$

where $T_J$ is junction temperature, $T_C$ is case temperature, $P_D$ is power dissipation, and $R_{\theta JC}$ is junction-to-case thermal resistance.

If ambient-based estimation is used instead, then

$$\boxed{T_J \approx T_A + P_D R_{\theta JA}} \quad \text{(5.9)}$$

where $T_A$ is ambient temperature and $R_{\theta JA}$ is junction-to-ambient thermal resistance.

Infineon's application note also reminds us that the full thermal path includes junction-to-case, case-to-heatsink, and heatsink-to-ambient terms, so a low chip thermal resistance alone does not guarantee cool operation [Infineon Discrete IGBT Datasheet Explanation].

### 1.5.4 Comparison of power BJT, power MOSFET, and IGBT

Device selection in power electronics depends on voltage class, current, switching frequency, efficiency target, thermal conditions, and control burden. No single transistor is best in every regime.

Table 5.2: Practical comparison of power BJT, power MOSFET, and IGBT

| Feature | Power BJT | Power MOSFET | IGBT |
| --- | --- | --- | --- |
| Control type | Current-controlled | Voltage-controlled | Voltage-controlled |
| Input burden in steady state | Significant base current | Very small ideal steady-state current | Very small ideal steady-state current |
| Main ON-state description | $V_{CE(\mathrm{sat})}$ | $R_{DS(\mathrm{on})}$ | $V_{CE(\mathrm{sat})}$ |
| Switching speed | Moderate to slow | Fast | Moderate; slower than MOSFET at turn-OFF |
| Stored-charge problem | Strong | Low compared with bipolar devices | Present; causes tail current |
| High-voltage suitability in silicon | Reasonable, but drive is difficult | ON resistance rises strongly with voltage | Strong practical range at medium and high voltage |
| Typical modern role | Mostly legacy or specialized | Low- to medium-voltage, high-frequency converters | Medium- to high-power inverters and converters |

#### Selection by voltage and frequency

As a first design rule, MOSFETs are often favored at lower voltage and higher switching frequency, whereas IGBTs are often favored at higher voltage and moderate switching frequency. BJTs are no longer the first choice in most mainstream new converter designs.

The reason follows directly from device physics. For silicon MOSFETs, high blocking voltage tends to increase drift-region resistance. The IGBT avoids the same resistance penalty by conductivity modulation, but it accepts slower turn-OFF and tail current. In practice, that makes the IGBT attractive in the 600 V, 1200 V, and higher classes when switching frequency is still in the range normally used for PWM conversion [Infineon IGBT Basic Know-How], [Infineon TRENCHSTOP IGBT6].

#### Application ranges

In **solar PV systems**, low-voltage MPPT buck or boost stages often favor MOSFETs, while several-kilowatt string inverters and larger central inverter stages often use IGBTs in the inverter bridge. Infineon specifically identifies 1200 V TRENCHSTOP IGBT families for solar applications [Infineon TRENCHSTOP IGBT6].

In **wind-energy converters**, the machine-side and grid-side power stages operate at substantial DC-link voltage and significant power, so IGBT modules are common in practical industrial designs. Their voltage capability, current handling, switching range, and mature module packaging suit this operating region well.

In **EV power stages**, low-voltage auxiliary DC-DC converters commonly use MOSFETs, while high-power traction inverters have long used IGBT modules in many silicon-based platforms. Silicon carbide devices now compete strongly in this area, but the IGBT remains a central reference for traction-class inverter design.

#### A realistic numeric selection example

Consider a three-phase inverter running from a rectified 415 V supply. The DC-link voltage may be around $600 \text{ V}$ after margin and variation are considered.

A 60 V MOSFET is clearly unsuitable. A 600 V MOSFET may still be usable in some cases, but its conduction loss can become substantial unless the current is modest or the chosen technology is especially favorable. A 1200 V IGBT, by contrast, is a common practical class because it provides blocking-voltage margin and is designed for inverter switching in the tens-of-kilohertz range [Infineon IKW40N120H3 Datasheet], [Infineon TRENCHSTOP IGBT6].

This example does not prove that the IGBT is always the best choice. It shows why the IGBT belongs naturally in the design space of medium-voltage, medium- to high-power PWM converters.

## Worked datasheet interpretation

The [Infineon IKW40N120H3 datasheet](https://www.infineon.com/assets/row/public/documents/60/49/infineon-ikw40n120h3-datasheet-en.pdf) provides a useful example of an inverter-class device: a 1200 V, 40 A IGBT with an anti-parallel diode in a TO-247 package [Infineon IKW40N120H3 Datasheet].

### Step 1: Read the voltage class first

The datasheet gives collector-emitter voltage rating

$$V_{CE} = 1200 \text{ V}.$$

This rating places the device in the high-voltage inverter class rather than the low-voltage battery-converter class. It is suited to converter systems such as off-line industrial inverters, PV inverter stages, UPS bridges, and motor drives on 230 V or 415 V AC systems after rectification.

### Step 2: Read current rating together with temperature

The datasheet lists

- $I_C = 80 \text{ A}$ at $T_C = 25^\circ\text{C}$
- $I_C = 40 \text{ A}$ at $T_C = 100^\circ\text{C}$

The current rating therefore depends directly on thermal condition. A headline current number is incomplete unless the associated temperature is also stated [Infineon IKW40N120H3 Datasheet].

### Step 3: Interpret ON-state and gate-drive data together

The datasheet gives a typical value around

- $V_{CE(\mathrm{sat})} = 2.05 \text{ V}$ at $I_C = 40 \text{ A}$, $V_{GE} = 15 \text{ V}$, $T_{vj} = 25^\circ\text{C}$

with higher values at elevated junction temperature [Infineon IKW40N120H3 Datasheet].

This immediately links conduction behavior to the intended drive condition. The device is characterized for power operation at about 15 V gate drive, and conduction loss rises with both current and temperature.

If a first estimate is made at $20 \text{ A}$ using the fixed-drop model, then

$$P_{\mathrm{cond}} \approx V_{CE(\mathrm{sat})} I_C \approx 2.05 \times 20 = 41 \text{ W}.$$

The estimate is crude because $V_{CE(\mathrm{sat})}$ varies with current and temperature, but it is sufficient to show that an IGBT at significant current is a serious thermal device.

The same datasheet gives gate-emitter threshold voltage in the approximate range

$$V_{GE(\mathrm{th})} = 5 \text{ V to } 6.5 \text{ V}$$

under a small test current [Infineon IKW40N120H3 Datasheet].

That value marks the onset of conduction, not the recommended gate-drive level for inverter operation. The saturation-voltage data are specified at 15 V, which identifies the intended drive condition.

### Step 4: Read switching and protection data as test-condition data

The datasheet provides switching times and switching energies under specified conditions such as:

- $V_{CC} = 600 \text{ V}$
- $I_C = 40 \text{ A}$
- $V_{GE} = 0/15 \text{ V}$
- gate resistances of $12 \,\Omega$

It gives typical values such as

- $E_{\mathrm{on}} = 3.2 \text{ mJ}$ at $25^\circ\text{C}$
- $E_{\mathrm{off}} = 1.2 \text{ mJ}$ at $25^\circ\text{C}$

with higher values at elevated temperature [Infineon IKW40N120H3 Datasheet].

These are measured values under stated conditions, not fixed switching losses for every circuit.

The datasheet also lists turn-off safe operating area up to rated voltage, short-circuit withstand time $t_{SC} = 10 \,\mu\text{s}$ under stated conditions, and a gate-emitter voltage rating of $\pm 20 \text{ V}$ with transient allowance to $\pm 30 \text{ V}$ under specific conditions [Infineon IKW40N120H3 Datasheet]. Together, these ratings show that the device is intended for serious inverter duty and must be used with a proper driver, proper layout, and fast protection.

### Step 5: Place the device in an application context

Consider a 5 kW to 10 kW solar string inverter or a UPS inverter operating from a several-hundred-volt DC link. A 1200 V IGBT of this class fits that environment naturally. The voltage rating provides margin, the anti-parallel diode supports bridge operation, and the switching-energy and short-circuit data are directly relevant to the design of a PWM inverter leg.

The datasheet is therefore more than a list of device limits. It identifies the voltage class, current capability, drive condition, switching behavior, protection requirements, and likely application range of the part.

## Chapter summary

- The **IGBT** combines a MOS insulated gate with bipolar conduction, giving it voltage-driven input behavior and strong high-voltage current conduction [Infineon IGBT Basic Know-How].
- Its internal structure includes an N- drift region for voltage blocking and a P+ collector layer that enables conductivity modulation during conduction.
- The ON state is usually described by $V_{CE(\mathrm{sat})}$ rather than by an ON resistance, and a first conduction-loss estimate is $P_{\mathrm{cond}} \approx V_{CE(\mathrm{sat})} I_C$.
- Threshold voltage $V_{GE(\mathrm{th})}$ marks the onset of conduction, not the recommended drive level for power switching.
- The major switching limitation of the IGBT relative to the MOSFET is tail current during turn-OFF due to stored charge.
- Practical switching evaluation relies heavily on datasheet values such as $E_{\mathrm{on}}$, $E_{\mathrm{off}}$, SOA, and short-circuit withstand time.
- In broad selection terms, MOSFETs dominate lower-voltage high-frequency converters, while IGBTs are often preferred in medium- to high-voltage moderate-frequency inverter applications.
- The IGBT remains one of the key devices for understanding industrial drives, UPS systems, solar inverters, wind converters, and other medium- to high-power PWM systems.

## Further reading

- [Infineon, "IGBT-basic know-how - IGBT: how does an Insulated Gate Bipolar Transistor work?"](https://www.infineon.com/gated/infineon-igbt-basics-how-does-an-igbt-work-additionaltechnicalinformation-en_cbbe773b-19c5-43ab-8c9d-a5cd3550c158) - A practical manufacturer overview of IGBT operation, applications, and comparison with MOSFETs.
- [Infineon, "Application Note: Discrete IGBT - Explanation of discrete IGBTs' datasheets"](https://www.infineon.com/dgdl/Infineon-ApplicationNote_DiscreteIGBT_DatasheetExplanation-AN-v02_00-EN.pdf?fileId=5546d462501ee6fd015023070b8b306d) - Useful for threshold voltage, $V_{CE(\mathrm{sat})}$, switching energies, SOA, and thermal interpretation.
- [Infineon, "IKW40N120H3 Datasheet"](https://www.infineon.com/assets/row/public/documents/60/49/infineon-ikw40n120h3-datasheet-en.pdf) - A representative inverter-class discrete IGBT datasheet with switching energy, SOA, short-circuit, and diode information.
- [Infineon, "IGBTs - Insulated gate bipolar transistors overview"](https://www.infineon.com/cms/en/product/power/igbt/igbt-stacks-igbt-assemblies/2ls20017e42w36702/) - Useful for the present-day voltage and application range of industrial IGBTs.
- [NC State University, "Baliga inducted into Electronic Design Engineering Hall of Fame"](https://engr.ncsu.edu/news/2010/12/02/baliga-inducted-into-electronic-design-engineering-hall-of-fame/) - A concise source for the invention significance of the IGBT and its broad real-world impact.
