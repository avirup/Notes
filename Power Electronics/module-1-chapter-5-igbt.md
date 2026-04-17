# Chapter 1.5: IGBT

## Chapter opening

In Chapters 1.1 to 1.4, we met three very different ideas about power switching. The power BJT showed us a current-controlled device with strong conduction capability but a heavy drive burden. The SCR and TRIAC family showed us latching behavior and the importance of commutation. The power MOSFET then introduced a voltage-controlled gate, fast switching, and the logic of a vertical power device. The **insulated-gate bipolar transistor**, or **IGBT**, brings many of these ideas together.

The IGBT matters because it became one of the most important switches in practical medium- and high-power converters. It offers a MOSFET-like insulated gate, so the drive circuit can be voltage-based rather than current-hungry. At the same time, it uses bipolar conduction inside the device, which helps it carry large current at high voltage with lower conduction loss than a comparable high-voltage silicon MOSFET in many applications [Infineon IGBT Basic Know-How], [Infineon IGBTs Overview].

That combination explains why IGBTs became central to industrial inverters, UPS systems, motor drives, battery chargers, traction systems, wind converters, and many solar PV power stages. Infineon describes the IGBT as the most used power-electronic component in industrial applications and notes its central role in drives, battery chargers, and solar and wind power plants [Infineon IGBT Basic Know-How]. For a learner of power electronics, this chapter is therefore a bridge. It connects the device physics we have already seen to the converter topologies we will study later.

We will begin with the historical role of the IGBT and why engineers needed a device between the MOSFET and the BJT. Then we will study the internal structure, the operating principle, and the meaning of output and transfer characteristics. After that we will look at switching behavior, the turn-off current tail, latch-up, and safe operating area. Finally, we will compare the power BJT, power MOSFET, and IGBT in the practical language of renewable-energy converters.

## Prerequisites check

- You should know from Chapter 1.1 that a power device must carry current, block voltage, switch between states, and stay within thermal limits.
- You should know from Chapter 1.4 that a MOS gate is insulated, so gate control is mainly a voltage-drive problem with capacitance and gate charge.
- You should remember that a rectified 230 V, 50 Hz single-phase supply produces a DC bus of about $325 \text{ V}$, and a 415 V three-phase system produces a much higher DC bus.
- You should know the difference between conduction loss and switching loss, even if your confidence with exact loss calculation is still developing.
- You should be comfortable with current, voltage, power, and the basic relation $P = VI$.

If MOSFET gate control or BJT saturation feels weak, a short review of Chapters 1.1 and 1.4 will help before continuing.

## Core content

### 1.5.1 History of IGBT

Let us begin with a practical design problem.

Suppose we need a switch for a three-phase inverter fed from a rectified 415 V supply. The DC link may be around $560 \text{ V}$ to $600 \text{ V}$ in many practical systems, and the switch must handle significant current. A high-voltage BJT can do this, but it demands continuous base current and suffers from stored-charge problems. A high-voltage MOSFET is easy to drive, but as voltage rating increases, its ON resistance rises strongly. Engineers therefore wanted a device that combined an insulated MOS gate with stronger high-voltage current conduction.

That is the problem the IGBT solved.

The IGBT was invented by B. Jayant Baliga while working at General Electric. NC State University, in a summary of his work, states that he was honored for inventing the IGBT and describes it as an energy-saving semiconductor switch used across many applications [NC State, Baliga Hall of Fame]. A later NC State report states more specifically that Baliga invented the IGBT in 1980 [NC State, Pack Power]. That date is useful because it places the IGBT after the power BJT era and after the MOSFET principle was already established.

The name **insulated-gate bipolar transistor** already tells us the central idea:

- **insulated-gate** means the control terminal is MOS-like and voltage-driven,
- **bipolar transistor** means the internal current conduction uses both carrier types, not only majority carriers as in a MOSFET.

So the IGBT is not merely "a better transistor." It is a hybrid power-device concept that tries to keep the easy gate drive of the MOSFET while gaining the high-voltage, high-current conduction advantages of bipolar behavior [Infineon IGBT Basic Know-How].

This historical context also explains where the IGBT sits among the devices we have already studied.

Table 5.1: The design gap that led to the IGBT

| Device | Main strength | Main limitation in power switching |
|---|---|---|
| Power BJT | Good conduction capability at high voltage | Needs continuous base current; turn-off slowed by stored charge |
| Power MOSFET | Easy voltage drive and fast switching | High-voltage devices suffer rising $R_{DS(\mathrm{on})}$ |
| IGBT | Combines insulated gate with strong high-voltage current conduction | Turn-off is slower than MOSFET because of stored charge and tail current |

When we say the IGBT became important, we should not imagine that it replaced every other device. That would be too simple. At lower voltages and very high frequencies, MOSFETs remain excellent. At line frequency and very high power, thyristor-family devices are still relevant. But in the large middle territory of industrial and renewable-energy conversion, the IGBT became one of the dominant switches.

Infineon notes that IGBTs can withstand voltages up to several kilovolts and operate at switching frequencies from a few kilohertz into the tens of kilohertz range depending on type [Infineon IGBTs Overview]. That is exactly the operating region of many inverter-fed motors, UPS systems, PV inverters, battery chargers, and wind-converter stages.

A common misconception is that the IGBT is simply a MOSFET with higher current. That is not correct. The IGBT has a different internal conduction mechanism. This is why its ON-state drop behaves more like a saturation voltage than a resistance, and why it shows a turn-off current tail that a MOSFET does not show in the same way.

*Renewable-energy relevance.* In solar string inverters, wind power converters, EV traction inverters, industrial motor drives used in pumping systems, and large UPS systems, the IGBT became important because it serves the medium-voltage, medium-to-high-power range very effectively [Infineon IGBT Basic Know-How], [Infineon TRENCHSTOP IGBT6].

### 1.5.2 Structure, operating principle, output and transfer characteristics

#### Why the IGBT structure is different from a MOSFET

We already learned in Chapter 1.4 that a vertical MOSFET uses a drift region to block voltage. But the price of high blocking voltage in a silicon MOSFET is a large increase in ON resistance. The IGBT changes that story by adding bipolar carrier injection into the drift region.

At beginner level, the most useful mental picture is this:

- the IGBT uses a MOS gate at the input,
- the gate forms a channel much like a MOSFET,
- that channel then allows bipolar conduction through the vertical device,
- bipolar conduction reduces the effective resistance of the drift region.

This reduction happens because injected carriers increase the conductivity of the drift region, a phenomenon commonly called **conductivity modulation** in power-device literature [Infineon IGBT Basic Know-How]. You do not need advanced semiconductor physics to understand the practical result: a high-voltage IGBT can conduct large current with a smaller ON-state penalty than a comparable high-voltage silicon MOSFET in many applications.

**Image prompt for Figure 5.1:** Create a clean textbook-style technical illustration of a vertical N-channel IGBT cross-section. Show emitter metallization at the top contacting repeated N+ emitter regions inside P-body regions. Show a gate insulated by silicon dioxide over the channel area. Below the body, show an N- drift region and a P+ collector layer at the bottom with collector metallization. Label emitter, gate, collector, N+ emitter, P-body, inversion channel, N- drift region, P+ collector, oxide, and indicate electron flow from emitter toward drift region and hole injection from collector toward drift region during conduction. Use monochrome engineering style with no decorative background.

Figure 5.1 should make three key ideas visible.

First, the **gate** is insulated from the semiconductor by oxide, just as in the MOSFET. That means the input has very high steady-state impedance. Second, the current path is vertical, so the die can support high current and high voltage. Third, the bottom **P+ collector** layer injects carriers into the drift region during conduction. That is the step that makes the device bipolar.

#### Basic operating principle

The main terminals of an IGBT are:

- **Gate (G)**
- **Collector (C)**
- **Emitter (E)**

For the common **N-channel IGBT**, the collector is usually at the high-potential side and the emitter at the lower-potential side.

The sequence of operation is:

1. With $V_{GE} = 0$, where $V_{GE}$ is gate-emitter voltage, no conducting channel exists in the body region, so the device is OFF and blocks collector-emitter voltage.
2. As $V_{GE}$ rises and exceeds the threshold value, a channel forms under the gate.
3. Electrons can now flow from emitter into the drift region.
4. This channel action supports bipolar carrier injection inside the vertical structure, which strongly improves conduction.

The threshold voltage is written as $V_{GE(\mathrm{th})}$. Like MOSFET threshold voltage, it marks the beginning of conduction, not the condition for strong low-loss operation [Infineon Discrete IGBT Datasheet Explanation].

This is very important. An IGBT with threshold voltage around $5 \text{ V}$ is not intended to be run as a power switch at only 5 V gate drive. Many discrete IGBTs are characterized at about $15 \text{ V}$ gate drive for normal switching use [Infineon Discrete IGBT Datasheet Explanation], [Infineon IKW40N120H3 Datasheet].

#### ON-state behavior and saturation voltage

In power-circuit language, the IGBT ON-state is usually described by its **collector-emitter saturation voltage**, written $V_{CE(\mathrm{sat})}$.

This already tells us the IGBT behaves differently from a MOSFET. A MOSFET in the ON state is usually described by $R_{DS(\mathrm{on})}$. An IGBT is usually described by a voltage drop.

A first practical conduction-loss estimate is

$$\boxed{P_{\mathrm{cond}} \approx V_{CE(\mathrm{sat})} I_C} \quad \text{(5.1)}$$

where $P_{\mathrm{cond}}$ is conduction loss, $V_{CE(\mathrm{sat})}$ is the collector-emitter saturation voltage, and $I_C$ is collector current.

If the device conducts only for duty ratio $D$, then a simple average estimate is

$$\boxed{P_{\mathrm{cond,avg}} \approx D\,V_{CE(\mathrm{sat})} I_C} \quad \text{(5.2)}$$

Consider a practical example from a medium-power inverter leg. Suppose an IGBT has $V_{CE(\mathrm{sat})} = 2.1 \text{ V}$ at the operating current, and it carries $20 \text{ A}$ for 40% of the switching cycle average.

Then the average conduction loss estimate is

$$P_{\mathrm{cond,avg}} \approx 0.40 \times 2.1 \times 20 = 16.8 \text{ W}.$$

This number is useful for intuition. It shows why the IGBT is attractive in medium-voltage converters: the ON-state drop may be acceptable at large current even when a comparable high-voltage MOSFET would have a substantial resistance penalty. At the same time, it also shows that the IGBT is not a zero-loss switch. A few volts at tens of amperes produces real heat.

#### Output characteristics

The **output characteristics** plot collector current $I_C$ versus collector-emitter voltage $V_{CE}$ for several fixed values of gate-emitter voltage $V_{GE}$.

**Image prompt for Figure 5.2:** Create a textbook-style graph of N-channel IGBT output characteristics. Use horizontal axis collector-emitter voltage $V_{CE}$ in volts and vertical axis collector current $I_C$ in amperes. Draw a family of curves for increasing gate-emitter voltages such as 7 V, 9 V, 11 V, 13 V, and 15 V. Show that higher $V_{GE}$ allows higher collector current. Mark a low-$V_{CE}$ region labeled "on-state / saturation region in power-switching use" and a higher-$V_{CE}$ region labeled "active region." Use monochrome engineering style with clear curve labels.

How do we read this graph?

If $V_{GE}$ is low, the device can support only limited current. As $V_{GE}$ rises, the collector current capability rises strongly. Near the ON-state operating region used in converters, the IGBT shows a relatively small voltage drop compared with the large blocked voltage in the OFF state.

At beginner level, you should not get trapped by terminology here. Device texts may discuss **active region** and **saturation region**, but in power electronics our practical interest is simpler:

- OFF and blocking,
- ON and carrying current with acceptable loss,
- switching between those two states quickly and safely.

#### Transfer characteristics

The **transfer characteristic** plots collector current $I_C$ as a function of gate-emitter voltage $V_{GE}$ at stated test conditions.

**Image prompt for Figure 5.3:** Create a clean textbook-style graph of IGBT transfer characteristics. Use horizontal axis gate-emitter voltage $V_{GE}$ in volts and vertical axis collector current $I_C$ in amperes. Show a curve with negligible current below threshold, then rapidly increasing current after threshold. Mark $V_{GE(th)}$, and add a note that practical power switching commonly uses gate drive around 15 V, not merely threshold voltage. Use monochrome engineering style.

The transfer characteristic helps answer the question: how strongly does the device turn ON as the gate voltage increases?

Suppose the threshold is about $5.8 \text{ V}$. This does not mean the device is ready for efficient inverter service at 6 V. It means measurable conduction has started under a small test current. Practical power operation still needs the datasheet’s recommended gate-drive condition.

This is one of the most common beginner mistakes with IGBTs, just as it is with MOSFETs: confusing **turn-on onset** with **proper drive level**.

#### Input behavior and transconductance

Because the gate is insulated, the input behaves primarily as a capacitive load rather than a steady current load. The device therefore needs current mainly during transitions, while charging or discharging the gate.

A useful quantity here is **transconductance**, written $g_{fs}$, which relates change in collector current to change in gate-emitter voltage under stated conditions:

$$\boxed{g_{fs} = \frac{\Delta I_C}{\Delta V_{GE}}} \quad \text{(5.3)}$$

This is not usually the first parameter used for converter loss estimation, but it helps us understand that the gate still controls the output strongly even though the output current path itself is bipolar.

#### Positive temperature coefficient and paralleling

Modern IGBTs often show a **positive temperature coefficient** of $V_{CE(\mathrm{sat})}$ above a certain current range. Infineon notes that with newer Trenchstop technology, a 40 A device shows a positive temperature coefficient starting from about 10 A, which helps current sharing when devices are paralleled [Infineon Discrete IGBT Datasheet Explanation].

This matters because if one device in a parallel group heats and its ON-state drop rises, it tends to give up some current to the cooler device. That behavior is friendlier than the strong current-crowding tendency that makes parallel BJTs harder to manage.

We should still be careful. Positive temperature coefficient does not mean we may parallel devices casually. Layout, gate resistance, stray inductance, and thermal matching still matter.

*Renewable-energy relevance.* These static characteristics appear directly in solar inverter and UPS design. The engineer asks: what gate drive is required, what ON-state drop will I get at operating current, and can parallel devices share current reasonably? Those are not academic questions. They determine heat-sink size, efficiency, and cost.

### 1.5.3 Switching characteristics, latch-up, SOA

#### Why IGBT switching is different from MOSFET switching

The IGBT gate is MOS-like, but the output conduction is bipolar. So its switching behavior is partly familiar from the MOSFET and partly limited by stored charge.

Turn-ON usually feels quite convenient: the gate is charged, a channel forms, current rises, and the device enters conduction. Turn-OFF is more subtle. Even after the gate drive is removed, stored charge remains in the drift region. That produces the well-known **tail current**.

The standard switching intervals are:

- **Turn-on delay time $t_{d(\mathrm{on})}$**
- **Rise time $t_r$**
- **Turn-off delay time $t_{d(\mathrm{off})}$**
- **Fall time $t_f$**

These are used in datasheets and follow IEC/JEDEC style definitions under specified test circuits [Infineon Discrete IGBT Datasheet Explanation].

#### The turn-off tail current

The **tail current** is the slowly decaying current that persists during turn-OFF because stored charge in the bipolar conduction path must be removed. Infineon’s datasheet-explanation note explicitly states that switching-loss timing for the IGBT takes the tail-current effect into account [Infineon Discrete IGBT Datasheet Explanation].

This one point explains a major practical difference between IGBTs and MOSFETs:

- a MOSFET is a majority-carrier device and can switch very fast,
- an IGBT benefits from conductivity modulation in conduction,
- but the price is stored charge and a turn-off tail.

So the IGBT is not "slower because it is older." It is slower for a specific physical reason.

**Image prompt for Figure 5.4:** Create a textbook-style switching waveform figure for an IGBT. Show three aligned plots versus time: gate-emitter voltage $V_{GE}$, collector current $I_C$, and collector-emitter voltage $V_{CE}$. Mark turn-on delay time $t_{d(on)}$, rise time $t_r$, turn-off delay time $t_{d(off)}$, and fall time $t_f$. In the turn-off current waveform, show a clear current tail after the main current fall and label it "tail current due to stored charge." Use monochrome engineering style and clear timing markers.

#### First estimate of switching loss

Because voltage and current overlap during switching, the device dissipates energy during each transition. A simple introductory approximation is

$$\boxed{E_{\mathrm{sw,approx}} \approx \frac{1}{2}V_{CC} I_C (t_r + t_f)} \quad \text{(5.4)}$$

where $V_{CC}$ is the DC-link or blocking voltage, $I_C$ is the switched current, and $t_r$ and $t_f$ are the rise and fall times.

Then the corresponding average switching-loss estimate is

$$\boxed{P_{\mathrm{sw,approx}} \approx f_s E_{\mathrm{sw,approx}}} \quad \text{(5.5)}$$

where $f_s$ is switching frequency.

These equations are useful for first intuition, but for IGBTs we must say something important: they can underestimate turn-off loss if the tail current is significant. That is why datasheets often provide measured switching energies directly:

- **turn-on energy $E_{\mathrm{on}}$**
- **turn-off energy $E_{\mathrm{off}}$**
- sometimes total switching energy $E_{\mathrm{ts}} = E_{\mathrm{on}} + E_{\mathrm{off}}$

Infineon notes that these energies are derived from a specified test setup and may differ from the final user application because switching behavior depends strongly on current, voltage, temperature, gate resistance, board design, and parasitics [Infineon Discrete IGBT Datasheet Explanation].

That warning matters a lot. A datasheet energy value is not a universal constant. It is a measured value under stated conditions.

#### Gate charge and driver effort

Like the MOSFET, the IGBT gate must be charged and discharged. A useful first estimate for average gate-drive current is

$$\boxed{I_{G,\mathrm{avg}} \approx Q_G f_s} \quad \text{(5.6)}$$

where $Q_G$ is total gate charge.

If the gate swings through voltage $V_{GG}$, then a simple gate-drive power estimate is

$$\boxed{P_G \approx Q_G V_{GG} f_s} \quad \text{(5.7)}$$

Although the IGBT is voltage-driven, the driver is not effortless. Large devices and high switching frequencies still demand a capable gate driver.

#### Latch-up in the IGBT

The IGBT contains a parasitic thyristor structure because of its layered semiconductor arrangement. Under improper conditions, that parasitic structure can turn on. This unwanted condition is called **latch-up**.

At beginner level, the safest way to think of latch-up is this: the IGBT contains internal transistor action that is useful when controlled properly, but if the internal parasitic thyristor is triggered, the device can lose normal gate control and enter a destructive condition. Research literature on latch-up in IGBT structures analyzes precisely this parasitic-thyristor behavior [Solid-State Electronics, 1990, latch-up phenomena in IGBT structures].

What can encourage latch-up?

- excessive current density
- excessive $dI/dt$
- local hot spots
- improper structure or insufficient latch-up immunity
- severe short-circuit or fault stress

Modern IGBTs are designed to be highly latch-up resistant in normal operation, but the concept remains important because it explains why current limits, short-circuit ratings, and SOA must be respected.

A common misconception is that latch-up means ordinary turn-ON. It does not. Ordinary turn-ON is the intended MOS-gate-controlled operation. Latch-up is an unwanted triggering of the parasitic thyristor path.

#### Safe operating area

The **safe operating area**, or **SOA**, gives the voltage-current combinations within which the device can operate safely under stated conditions.

For IGBTs, Infineon’s datasheet-explanation note distinguishes two main forms [Infineon Discrete IGBT Datasheet Explanation]:

- **Forward-bias safe operating area (FBSOA)**
- **Reverse-bias safe operating area (RBSOA)**

FBSOA refers to safe conditions during forward-biased operation. RBSOA is especially relevant during turn-OFF, usually with an inductive load, when the device experiences rising voltage and falling current at the same time.

Infineon notes that for state-of-the-art IGBTs, the RBSOA is often approximately square-shaped and bounded mainly by breakdown voltage and pulse current capability [Infineon Discrete IGBT Datasheet Explanation]. That is one important difference from classic BJTs, whose SOA is strongly restricted by second breakdown.

Still, we should not turn that into an oversimplification. Even though the IGBT generally avoids the severe second-breakdown behavior of BJTs, its SOA is still limited by:

- breakdown voltage
- pulse current
- junction temperature
- stray inductance
- gate-drive conditions
- switching speed and overshoot

#### Short-circuit withstand time

Many IGBTs specify a **short-circuit withstand time**, often written $t_{SC}$. This tells us how long the device can survive a specified short-circuit condition under stated gate drive, voltage, and temperature. That number is extremely important in inverter protection design.

If a datasheet gives $t_{SC} = 10 \,\mu\text{s}$, that does not mean the device may be shorted casually for 10 microseconds in any circuit. It means that under the specified test conditions, protection must act quickly enough to remove the fault before this survival limit is exceeded.

For inverter legs in solar, UPS, and motor-drive service, this rating influences the design of gate-driver protection and fault detection.

#### Thermal relation

As with all power semiconductors, switching and conduction losses become heat. A basic thermal relation is

$$\boxed{T_J \approx T_C + P_D R_{\theta JC}} \quad \text{(5.8)}$$

where $T_J$ is junction temperature, $T_C$ is case temperature, $P_D$ is power dissipation, and $R_{\theta JC}$ is junction-to-case thermal resistance.

If ambient-based estimation is used instead, then

$$\boxed{T_J \approx T_A + P_D R_{\theta JA}} \quad \text{(5.9)}$$

where $T_A$ is ambient temperature and $R_{\theta JA}$ is junction-to-ambient thermal resistance.

Infineon’s application note also reminds us that the full thermal path includes junction-to-case, case-to-heatsink, and heatsink-to-ambient parts, so a low chip thermal resistance alone does not guarantee cool operation [Infineon Discrete IGBT Datasheet Explanation].

*Renewable-energy relevance.* Tail current, switching energy, RBSOA, and short-circuit survival are not small details. They determine whether an IGBT survives commutation in a solar inverter, a wind converter, an EV auxiliary inverter, or a UPS output bridge.

### 1.5.4 Comparison of Power BJT, Power MOSFET and IGBT - selection for solar, wind and EV converters

#### A practical selection mindset

By now, we have studied three transistor-type power switches:

- power BJT
- power MOSFET
- IGBT

A beginner often asks, "Which one is best?" That is not the right question. The better question is, "Best for what voltage, current, frequency, and application?"

The useful comparison is not based on one single feature. It must include:

- control method
- conduction behavior
- switching speed
- voltage range
- current capability
- thermal behavior
- application frequency range

Table 5.2: Practical comparison of power BJT, power MOSFET, and IGBT

| Feature | Power BJT | Power MOSFET | IGBT |
|---|---|---|---|
| Control type | Current-controlled | Voltage-controlled | Voltage-controlled |
| Input burden in steady state | Significant base current | Very small ideal steady-state current | Very small ideal steady-state current |
| Main ON-state description | $V_{CE(\mathrm{sat})}$ | $R_{DS(\mathrm{on})}$ | $V_{CE(\mathrm{sat})}$ |
| Switching speed | Moderate to slow | Fast | Moderate; slower than MOSFET at turn-OFF |
| Stored-charge problem | Strong | Low compared with bipolar devices | Present; causes tail current |
| High-voltage suitability in silicon | Reasonable, but drive is difficult | ON resistance rises strongly with voltage | Strong practical range at medium and high voltage |
| Typical modern role | Mostly legacy or specialized | Low- to medium-voltage, high-frequency converters | Medium- to high-power inverters and converters |

#### Selection by voltage and frequency

A very useful first rule is this:

- at lower voltage and higher switching frequency, MOSFETs are often favored,
- at higher voltage and moderate switching frequency, IGBTs are often favored,
- BJTs are usually not the first choice in new mainstream converter designs.

This is not an absolute law, but it is a strong starting heuristic.

Why does this happen?

For silicon MOSFETs, high blocking voltage tends to increase drift-region resistance. So at hundreds of volts, conduction loss can become significant. The IGBT avoids the same resistance penalty by conductivity modulation, but it accepts slower turn-OFF and tail current. Therefore, at moderate switching frequencies such as many kilohertz to a few tens of kilohertz, the IGBT often becomes attractive in the 600 V, 1200 V, or higher class [Infineon IGBT Basic Know-How], [Infineon TRENCHSTOP IGBT6].

#### Selection for solar PV systems

In **solar PV**, device selection depends strongly on converter location and power level.

For example:

- a low-voltage MPPT buck or boost stage inside a module-level optimizer may prefer MOSFETs,
- a several-kilowatt string inverter connected to a 230 V or 415 V AC system often uses IGBTs in the inverter stage,
- medium-voltage or high-power central inverter architecture may use IGBT modules.

Infineon specifically identifies 1200 V TRENCHSTOP IGBT families for solar applications [Infineon TRENCHSTOP IGBT6]. This is a strong clue: when the DC bus and power level move upward, the IGBT becomes a natural choice.

#### Selection for wind-energy converters

In **wind-energy systems**, the converter often handles substantial DC-link voltage and significant power. The machine-side and grid-side converters in variable-speed wind systems therefore commonly use IGBT modules in practical industrial designs. The reason is not mystery or tradition. It is the combination of:

- strong voltage capability
- large current handling
- practical switching frequency for PWM conversion
- mature module packaging and thermal capability

#### Selection for EV power stages

In **EV systems**, the choice depends on which part of the vehicle we mean.

For **low-voltage auxiliary converters**, such as 12 V or 48 V DC-DC converters, MOSFETs are very common because the voltage is moderate and switching frequency may be high.

For **traction inverters** in many traditional silicon-based EV and hybrid systems, IGBT modules have long been widely used because traction buses are high and power is large. In newer systems, silicon carbide devices increasingly compete in this space, but that does not reduce the importance of learning the IGBT. The IGBT remains one of the central historical and practical references for traction-class inverter design.

#### A realistic numeric selection example

Imagine we are choosing a switch for a three-phase inverter running from a rectified 415 V supply. The DC-link voltage may be around $600 \text{ V}$ in a practical design after margin and variation are considered.

Would a 60 V MOSFET work? Clearly not.

Would a 600 V MOSFET always be ideal? Not necessarily. At this voltage class, conduction loss may be substantial unless the current is small or the chosen technology is especially suitable.

Would a 1200 V IGBT be reasonable? Yes, this is a common practical class because it provides blocking-voltage margin and is designed for inverter switching in the tens-of-kilohertz range [Infineon IKW40N120H3 Datasheet], [Infineon TRENCHSTOP IGBT6].

That does not prove the IGBT is always best. It shows why the IGBT is often in the correct design conversation for medium-voltage inverter work.

#### Comparison as a design sentence

We can summarize the comparison in one practical sentence:

The BJT taught power switching, the MOSFET dominates where voltage-drive simplicity and high frequency matter most, and the IGBT became the standard workhorse where converter voltage and power are high enough that the MOSFET's resistance penalty becomes costly but switching frequency is still moderate enough that the IGBT's tail current remains acceptable.

*Renewable-energy relevance.* This comparison is the reason different renewable-energy subsystems use different devices. A battery-side low-voltage converter may use MOSFETs, while a grid-tied inverter stage may use IGBTs. Device choice follows bus voltage, power level, switching frequency, and efficiency target.

## Worked interpretation exercise

We will now read a real artifact:

- the [Infineon IKW40N120H3 datasheet](https://www.infineon.com/assets/row/public/documents/60/49/infineon-ikw40n120h3-datasheet-en.pdf)

This is a useful beginner datasheet because it is clearly an inverter-class device: a 1200 V, 40 A IGBT with an anti-parallel diode in a TO-247 package [Infineon IKW40N120H3 Datasheet].

### Step 1: Read the voltage class first

The datasheet gives collector-emitter voltage rating

$$V_{CE} = 1200 \text{ V}.$$

This immediately tells us the device belongs to the high-voltage inverter family. It is not a low-voltage battery MOSFET-class device. It is suited to converter systems such as:

- off-line industrial inverters,
- PV inverter stages,
- UPS bridges,
- motor drives on 230 V or 415 V AC systems after rectification.

It would be completely oversized for a 24 V battery charger, but very much in the correct class for a 600 V DC-link inverter.

### Step 2: Read current rating with temperature

The datasheet lists

- $I_C = 80 \text{ A}$ at $T_C = 25^\circ\text{C}$
- $I_C = 40 \text{ A}$ at $T_C = 100^\circ\text{C}$

This is a very important lesson. The same device does not have one single current rating independent of thermal condition. The current capability falls as case temperature rises. So a headline current number is only meaningful together with the thermal condition [Infineon IKW40N120H3 Datasheet].

### Step 3: Interpret $V_{CE(\mathrm{sat})}$ correctly

The datasheet gives typical values around

- $V_{CE(\mathrm{sat})} = 2.05 \text{ V}$ at $I_C = 40 \text{ A}$, $V_{GE} = 15 \text{ V}$, $T_{vj} = 25^\circ\text{C}$

with higher values at elevated junction temperature [Infineon IKW40N120H3 Datasheet].

This tells us that the device is intended to be driven at about 15 V gate voltage for proper power operation. It also tells us that conduction loss rises with current and temperature.

If we estimate conduction loss at $20 \text{ A}$ using the simple fixed-drop model and approximately the 25°C typical drop as a rough first approximation, then

$$P_{\mathrm{cond}} \approx V_{CE(\mathrm{sat})} I_C \approx 2.05 \times 20 = 41 \text{ W}.$$

This estimate is crude because $V_{CE(\mathrm{sat})}$ varies with current and temperature, but it makes one point very clearly: an IGBT at significant current is a serious thermal device. It needs real thermal design.

### Step 4: Do not confuse threshold with drive voltage

The same datasheet gives gate-emitter threshold voltage in the rough range

$$V_{GE(\mathrm{th})} = 5 \text{ V to } 6.5 \text{ V}$$

under a small test current [Infineon IKW40N120H3 Datasheet].

This does **not** mean we should drive the IGBT at 5 V in a power inverter. It means conduction begins around that value under light test conditions. The saturation-voltage data are specified at 15 V, which tells us the intended gate-drive level.

This comparison between threshold voltage and actual drive condition is one of the most useful datasheet-reading habits you can develop.

### Step 5: Read switching information as test-condition data

The datasheet provides switching times and switching energies under specified conditions such as:

- $V_{CC} = 600 \text{ V}$
- $I_C = 40 \text{ A}$
- $V_{GE} = 0/15 \text{ V}$
- gate resistances of $12 \,\Omega$

It gives typical values such as

- $E_{\mathrm{on}} = 3.2 \text{ mJ}$ at $25^\circ\text{C}$
- $E_{\mathrm{off}} = 1.2 \text{ mJ}$ at $25^\circ\text{C}$

with higher values at elevated temperature [Infineon IKW40N120H3 Datasheet].

The right interpretation is not "the switching loss is always 4.4 mJ." The right interpretation is:

- under this stated test condition, total switching energy is about $4.4 \text{ mJ}$,
- in another circuit with different current, gate resistance, layout inductance, or temperature, the value will change.

### Step 6: Read protection-oriented ratings

The datasheet also lists:

- turn-off safe operating area up to rated voltage,
- short-circuit withstand time $t_{SC} = 10 \,\mu\text{s}$ under stated conditions,
- gate-emitter voltage rating of $\pm 20 \text{ V}$ with transient allowance to $\pm 30 \text{ V}$ under specific conditions [Infineon IKW40N120H3 Datasheet].

These values tell us the device is intended for serious inverter duty, but also that it must be used with a proper driver, proper layout, and fast protection.

### Step 7: Connect it to a renewable-energy context

Imagine a 5 kW to 10 kW solar string inverter or a UPS inverter operating from a several-hundred-volt DC link. A 1200 V IGBT of this class makes immediate practical sense. The voltage rating fits the bus class with margin. The anti-parallel diode supports bridge operation. The switching-energy and short-circuit data are exactly the kind of information needed by the designer of a PWM inverter leg.

So this datasheet is not just a list of numbers. It is a compact description of where the part belongs in the power-electronics world.

## How this matters in renewable-energy systems

The IGBT appears most naturally when renewable-energy converters move beyond low-voltage, small-power switching and enter the region of substantial DC-link voltage and meaningful power flow.

In **solar PV systems**, IGBTs are widely used in string and central inverter stages that convert a DC bus into grid-quality AC. In **wind-energy systems**, they are common in back-to-back converter structures that interface the generator and the grid. In **battery charging and storage systems**, they appear in medium- and high-power inverter and rectifier sections. In **EV-related systems**, they have long been central to traction-class inverters and other high-power motor-drive stages, even as newer wide-bandgap devices increasingly enter this space.

This chapter's ideas show up very directly in those systems:

- the insulated gate makes digital control practical,
- the bipolar conduction mechanism keeps high-voltage conduction loss reasonable,
- the tail current limits switching frequency compared with MOSFETs,
- SOA and short-circuit ratings shape protection design,
- the anti-parallel diode matters in bridge commutation,
- thermal design becomes inseparable from electrical design.

Once you see an inverter leg in a solar, wind, or UPS system, you are no longer just looking at "a switch." You are looking at a device choice shaped by voltage class, current, switching frequency, control method, and thermal survival. The IGBT is one of the clearest examples of that engineering tradeoff.

## Chapter summary

- The **IGBT** was invented by B. Jayant Baliga and became one of the key power-semiconductor switches for industrial and renewable-energy converters [NC State, Baliga Hall of Fame], [NC State, Pack Power].
- The IGBT combines a **MOS insulated gate** with **bipolar conduction**, so it behaves like a voltage-driven device at the input but not like a simple MOSFET at the output [Infineon IGBT Basic Know-How].
- A vertical IGBT includes an N- drift region for voltage blocking and a P+ collector layer that enables conductivity modulation during conduction.
- The gate-emitter threshold voltage $V_{GE(\mathrm{th})}$ indicates the start of conduction, not the recommended full gate-drive voltage.
- In practical switching service, the ON-state is commonly described by the collector-emitter saturation voltage $V_{CE(\mathrm{sat})}$ rather than by an ON resistance.
- A first conduction-loss estimate is
  $\boxed{P_{\mathrm{cond}} \approx V_{CE(\mathrm{sat})} I_C}$ from Equation (5.1).
- For duty ratio $D$, a simple average conduction-loss estimate is
  $\boxed{P_{\mathrm{cond,avg}} \approx D\,V_{CE(\mathrm{sat})} I_C}$ from Equation (5.2).
- The transfer characteristic shows how collector current rises with gate-emitter voltage, and transconductance is expressed by
  $\boxed{g_{fs} = \Delta I_C / \Delta V_{GE}}$ from Equation (5.3).
- The major switching limitation of the IGBT compared with the MOSFET is **tail current** at turn-OFF due to stored charge [Infineon Discrete IGBT Datasheet Explanation].
- First switching-loss intuition can be built from
  $\boxed{E_{\mathrm{sw,approx}} \approx \frac{1}{2}V_{CC}I_C(t_r+t_f)}$ and
  $\boxed{P_{\mathrm{sw,approx}} \approx f_s E_{\mathrm{sw,approx}}}$ from Equations (5.4) and (5.5), but real datasheet values for $E_{\mathrm{on}}$ and $E_{\mathrm{off}}$ are usually more useful.
- The IGBT is voltage-driven, but the gate still requires dynamic drive effort. Average gate-drive current and power can be estimated using
  $\boxed{I_{G,\mathrm{avg}} \approx Q_G f_s}$ and
  $\boxed{P_G \approx Q_G V_{GG} f_s}$ from Equations (5.6) and (5.7).
- **Latch-up** refers to unwanted triggering of the parasitic thyristor structure inside the IGBT and is a fault-related reliability concern [Solid-State Electronics, 1990, latch-up phenomena in IGBT structures].
- IGBT SOA includes **FBSOA** and **RBSOA**, and modern devices often specify short-circuit withstand time, turn-off SOA, and switching-energy data [Infineon Discrete IGBT Datasheet Explanation], [Infineon IKW40N120H3 Datasheet].
- In practical selection, MOSFETs tend to dominate lower-voltage high-frequency converters, while IGBTs often dominate medium- to high-voltage moderate-frequency inverter applications.

## Further reading

- [Infineon, "IGBT-basic know-how - IGBT: how does an Insulated Gate Bipolar Transistor work?"](https://www.infineon.com/gated/infineon-igbt-basics-how-does-an-igbt-work-additionaltechnicalinformation-en_cbbe773b-19c5-43ab-8c9d-a5cd3550c158) - A practical manufacturer overview of why IGBTs matter, where they are used, and how they compare with MOSFETs.
- [Infineon, "Application Note: Discrete IGBT - Explanation of discrete IGBTs' datasheets"](https://www.infineon.com/dgdl/Infineon-ApplicationNote_DiscreteIGBT_DatasheetExplanation-AN-v02_00-EN.pdf?fileId=5546d462501ee6fd015023070b8b306d) - Very useful for understanding threshold voltage, $V_{CE(\mathrm{sat})}$, switching energies, SOA, and thermal interpretation.
- [Infineon, "IKW40N120H3 Datasheet"](https://www.infineon.com/assets/row/public/documents/60/49/infineon-ikw40n120h3-datasheet-en.pdf) - A real inverter-class discrete IGBT datasheet with switching energy, SOA, short-circuit, and diode information.
- [Infineon, "IGBTs - Insulated gate bipolar transistors overview"](https://www.infineon.com/cms/en/product/power/igbt/igbt-stacks-igbt-assemblies/2ls20017e42w36702/) - Useful for the present-day voltage and application range of industrial IGBTs.
- [NC State University, "Baliga inducted into Electronic Design Engineering Hall of Fame"](https://engr.ncsu.edu/news/2010/12/02/baliga-inducted-into-electronic-design-engineering-hall-of-fame/) - A concise source for the invention significance of the IGBT and its broad real-world impact.
