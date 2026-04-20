# Unit 5: Overview of Basic Semiconductor Devices

## Chapter Opening

Up to this point, the book has focused mainly on electrical quantities, magnetic effects, AC circuits, transformers, and motors. Those topics explain how electrical energy is produced, transferred, measured, and converted into motion. This chapter begins the electronics side of the subject. Here the central question changes. Instead of only asking how current flows in wires and machines, we now ask how a material can be engineered so that current is allowed, opposed, controlled, or amplified inside a tiny solid device.

That is the role of the **semiconductor**. From a semiconductor, engineers build **diodes**, **transistors**, and eventually integrated circuits. At diploma-entry level, the goal is not semiconductor fabrication science in full detail. The goal is to understand why materials such as silicon are special, how **doping** changes their behavior, how a **p-n junction** forms, why a diode conducts mainly in one direction, and how a transistor can act as a switch or amplifier.

This chapter connects strongly to what has already been learned. Chapter 1 introduced current, voltage, resistance, and waveforms. Chapter 3 showed AC rectification contexts where diodes naturally appear. Chapter 4 ended with practical control and conversion equipment that often contains semiconductor devices. Later chapters on analog circuits, op-amps, and digital logic depend directly on the ideas introduced here.

## Prerequisites Check

- Meaning of current, voltage, polarity, and resistance from Chapter 1.
- Basic idea of electric field and current direction.
- Familiarity with simple circuit symbols and the idea of source, load, and current path.
- Elementary algebra, especially rearranging formulas and working with units such as mA, µA, and V.
- Comfortable reading small device ratings such as `100 mA`, `40 V`, or `0.7 V`.

If current direction, voltage polarity, or unit conversion feels weak, review Chapter 1 before studying diode and transistor bias conditions.

## Core Content

### 5.1 Semiconductor Fundamentals

#### Why semiconductors are different

Suppose we compare three materials placed in a circuit:

- copper wire,
- glass,
- and silicon.

Copper allows current to pass very easily. Glass practically blocks it. Silicon lies between these two extremes. But the important point is not only that silicon has intermediate conductivity. The more important point is that its conductivity can be changed strongly by temperature, light, electric field, and tiny amounts of impurity atoms called dopants [Britannica, *semiconductor*](https://www.britannica.com/science/semiconductor).

This makes semiconductors useful for electronics. A copper wire is excellent for carrying current, but it is not easy to use copper itself as a current-controlling electronic device. A semiconductor can be shaped and doped so that it acts as a rectifier, switch, amplifier, sensor, or logic element.

#### Conductor, insulator, and semiconductor

A **conductor** is a material in which charge carriers can move easily. Metals such as copper and aluminum are common conductors.

An **insulator** is a material in which charge carriers are not free to move under ordinary conditions. Glass, mica, rubber, and many plastics are insulators.

A **semiconductor** is a material whose conductivity lies between that of a conductor and an insulator [Britannica, *semiconductor*](https://www.britannica.com/science/semiconductor).

The three classes are not merely labels of "good," "bad," and "medium" conductors. Their internal energy structure is different. To understand semiconductor devices, we must first understand that internal structure at a simple level.

**Image prompt for Figure 5.1:** Create a clean textbook-style three-panel energy-band diagram comparing a conductor, semiconductor, and insulator. In each panel show a valence band, conduction band, and band gap. For the conductor, show overlap or zero gap between valence and conduction bands. For the semiconductor, show a small band gap. For the insulator, show a large band gap. Label each panel clearly and keep the illustration simple and engineering-oriented.

#### Energy bands: valence band, conduction band, and band gap

Inside a crystal, electrons do not behave as if each atom were fully isolated. When many atoms come together to form a solid, the discrete energy levels spread into **energy bands**. The highest filled band is called the **valence band**. The next higher band is the **conduction band**. Between them there may be an **energy gap**, also called the **band gap** [Britannica, *semiconductor*](https://www.britannica.com/science/semiconductor).

The basic picture is:

- In a **conductor**, electrons can move easily because the valence and conduction situations effectively allow free conduction.
- In a **semiconductor**, the band gap is small enough that some electrons can move to the conduction band under suitable conditions.
- In an **insulator**, the band gap is so large that ordinary conduction is strongly prevented.

Britannica notes that when many atoms form a crystal, discrete levels spread into energy bands and the conduction band is separated from the valence band by an energy gap. It also notes that important semiconductors have band gaps in roughly the range `0.25 eV` to `2.5 eV`, with silicon around `1.12 eV` [Britannica, *semiconductor*](https://www.britannica.com/science/semiconductor). At this level, you do not need to memorize all numerical band-gap values. The key idea is that the band gap of a semiconductor is small enough to allow controlled conduction.

#### Covalent bonding in silicon

Silicon is the most important semiconductor material in basic electronics. A silicon atom has four outer electrons. In a silicon crystal, each atom shares electrons with neighboring atoms, forming **covalent bonds** [Britannica, *semiconductor*](https://www.britannica.com/science/semiconductor).

At low temperature, these electrons are largely tied up in bonds, so conduction is weak. As temperature rises, some bonds break. Then some electrons gain enough energy to move into the conduction band. Once an electron leaves a bond, it leaves behind an electron vacancy called a **hole**.

This is a central semiconductor idea:

- the free **electron** can carry negative charge,
- the **hole** behaves like a mobile positive charge carrier.

Both electrons and holes contribute to current in semiconductors.

#### Intrinsic semiconductor

A very pure semiconductor is called an **intrinsic semiconductor**. In an intrinsic semiconductor, the number of free electrons equals the number of holes [Britannica, *semiconductor*](https://www.britannica.com/science/semiconductor).

This equality is physically reasonable. Every time a covalent bond breaks and releases one electron, one hole is left behind. So carriers are generated in pairs:

- one electron,
- one hole.

Pure silicon and pure germanium are the usual introductory examples.

Intrinsic semiconductors conduct only weakly at room temperature compared with metals. That is why pure semiconductor material alone is not enough for most practical electronic devices. The conductivity must be controlled more strongly. This is done by doping.

#### Extrinsic semiconductor and doping

An impurity-added semiconductor is called an **extrinsic semiconductor**. The deliberate addition of suitable impurity atoms is called **doping** [Britannica, *semiconductor*](https://www.britannica.com/science/semiconductor).

Britannica notes that adding tiny amounts of impurity atoms can greatly increase conductivity, and gives the idea that even about 10 boron atoms per million silicon atoms can increase conductivity by a large factor [Britannica, *semiconductor*](https://www.britannica.com/science/semiconductor). This shows how sensitive semiconductor behavior is to very small changes in composition.

Doping does not mean "contaminating the material carelessly." It means introducing carefully chosen impurity atoms in controlled amounts so that charge carriers of the desired type become dominant.

Two important dopant categories are:

- **Donor impurities:** provide extra electrons.
- **Acceptor impurities:** create holes.

These lead to n-type and p-type material, which are studied in the next section.

#### Why doping matters physically

Without doping, the semiconductor is too weakly conducting for many practical electronic purposes. With doping, the number of useful charge carriers can be increased strongly. More importantly, the engineer can choose whether electrons or holes become the dominant carriers.

This gives a powerful design advantage:

- if we want electron-dominated conduction, we create n-type material,
- if we want hole-dominated conduction, we create p-type material,
- and if we join p-type and n-type regions together, we create the basis of the diode and transistor.

#### Temperature effect in semiconductors

Beginners often carry an intuition from metals into semiconductors and become confused. In many metals, heating increases resistance. In semiconductors, increasing temperature can increase the number of available charge carriers, so conductivity tends to increase.

At this level, the most useful teaching point is simple:

- in a semiconductor, temperature strongly affects carrier concentration,
- and semiconductor devices must therefore be used within rated temperature limits.

This is one reason datasheets always include temperature ratings.

#### Worked Example 5.1

A pure semiconductor sample at a certain temperature has created `8 × 10^12` free electrons by thermal energy. Assuming it remains intrinsic, how many holes are present?

In an intrinsic semiconductor, electrons and holes are generated in equal numbers.

So:

$$
\text{Number of holes} = \text{Number of electrons}
$$

Therefore,

$$
\text{Number of holes} = 8 \times 10^{12}
$$

So the sample contains **`8 × 10^12` holes**.

This simple question is important because it reinforces the idea that intrinsic carriers are created in electron-hole pairs.

#### Common misconceptions

- A semiconductor is not just a "poor conductor." Its importance lies in controllable conductivity.
- A hole is not a physical particle like an electron; it is a useful way to describe an electron vacancy behaving as a positive carrier.
- Doping does not mean making the material dirty in a casual sense. It is a controlled process used to shape electrical behavior.
- Intrinsic and extrinsic semiconductors are not different base materials only; they differ in purity and carrier control.

#### Practical note

When a real datasheet says a device is made from silicon and gives leakage current, forward voltage, gain, and temperature limits, it is the band structure and doping of the semiconductor that make those ratings possible.

### 5.2 P-Type and N-Type Semiconductor

#### From pure silicon to useful material

A pure silicon crystal is important for understanding, but practical devices need more control than intrinsic silicon provides. We now deliberately insert impurity atoms into the crystal. The result is still mostly silicon, but its electrical behavior changes greatly.

The two basic results are:

- **n-type semiconductor**
- **p-type semiconductor**

These are not two unrelated materials. They are two differently doped forms of semiconductor material.

#### N-type semiconductor

If a pentavalent impurity atom such as phosphorus, arsenic, or antimony is added to silicon, four of its outer electrons form covalent bonds with neighboring silicon atoms. One extra electron remains weakly bound and can become a conduction electron. The dopant acts as a **donor** [Britannica, *semiconductor*](https://www.britannica.com/science/semiconductor).

This creates an **n-type semiconductor**, where electrons are the majority carriers.

The name "n-type" does not mean the whole material has net negative charge. The material remains electrically neutral overall. It means the dominant mobile charge carriers are negative electrons.

#### P-type semiconductor

If a trivalent impurity atom such as boron, aluminum, or gallium is added to silicon, only three covalent bonds can be completed directly. One bond position lacks an electron. This creates a hole. The impurity acts as an **acceptor** [Britannica, *semiconductor*](https://www.britannica.com/science/semiconductor).

This creates a **p-type semiconductor**, where holes are the majority carriers.

Again, "p-type" does not mean the entire material is positively charged. It means the dominant mobile carriers are positive holes.

#### Majority and minority carriers

This vocabulary is very important in all semiconductor devices.

In n-type material:

- **majority carriers** are electrons,
- **minority carriers** are holes.

In p-type material:

- **majority carriers** are holes,
- **minority carriers** are electrons.

These minority carriers are still important. They become especially important in reverse-biased diodes and transistor operation.

#### How to picture the carrier situation

One useful beginner picture is this:

- intrinsic semiconductor: balanced but weak conduction,
- n-type semiconductor: many useful electrons added,
- p-type semiconductor: many useful holes created.

So the engineer is not only increasing conductivity. The engineer is choosing which carrier type will dominate.

**Image prompt for Figure 5.2:** Create a clean textbook-style two-panel illustration comparing n-type and p-type silicon crystals. In the n-type panel, show a silicon lattice with one pentavalent donor atom, four covalent bonds, and one extra free electron. Label donor impurity, free electron, majority carriers, and minority holes. In the p-type panel, show a silicon lattice with one trivalent acceptor atom, one incomplete bond represented as a hole, and label acceptor impurity, hole, majority carriers, and minority electrons.

#### Properties of n-type and p-type material

At diploma-entry level, the practical properties may be summarized as follows.

#### Table 5.1 Comparison of n-type and p-type semiconductors

| Property | n-type | p-type |
|---|---|---|
| Dopant type | pentavalent donor | trivalent acceptor |
| Typical dopants | P, As, Sb | B, Al, Ga |
| Majority carriers | electrons | holes |
| Minority carriers | holes | electrons |
| Dominant current mechanism | electron conduction | hole conduction |

This table is compact, but students should understand the physical reason behind each row, not merely memorize the words.

#### Worked Example 5.2

A silicon sample is doped with phosphorus. Identify:

1. whether it becomes p-type or n-type,
2. the majority carriers,
3. the minority carriers.

Phosphorus is a pentavalent impurity. Pentavalent impurities act as donors and create n-type material.

So:

- type = **n-type**
- majority carriers = **electrons**
- minority carriers = **holes**

#### Practical uses of p-type and n-type material

By themselves, p-type and n-type materials are already useful concepts, but their greatest importance appears when they are combined.

Applications based on p-type and n-type regions include:

- p-n junction diodes,
- bipolar transistors,
- many sensor structures,
- rectifiers,
- switching devices,
- logic and integrated circuits.

At diploma-entry level, the main point is that p-type and n-type materials are the building blocks from which junction devices are formed.

#### Common misconceptions

- N-type material is not negatively charged as a block, and p-type material is not positively charged as a block. Both remain electrically neutral overall.
- Majority carriers are not the only carriers present. Minority carriers are still present and become important in device behavior.
- Donor atoms do not “inject current” by themselves. They change the carrier population of the crystal.

#### Practical note

When a device is described as silicon, NPN, PNP, or p-n junction, that description is really telling you how p-type and n-type semiconductor regions have been arranged.

### 5.3 PN Junction Diode

#### From two regions to one junction

Now imagine joining p-type material and n-type material in one crystal. At the instant they are joined, the carrier concentrations are very different on the two sides:

- many holes on the p-side,
- many electrons on the n-side.

Nature does not leave this imbalance unchanged. Carriers begin to diffuse across the boundary. This leads to the most important structure in basic electronics: the **p-n junction**.

#### Formation of the p-n junction

When p-type and n-type semiconductors are joined, electrons from the n-side and holes from the p-side diffuse toward the junction. Near the boundary, they recombine. As a result, a region forms where there are no mobile charge carriers. This is the **depletion layer** [Toshiba, *1-3. pn junction*](https://toshiba.semicon-storage.com/us/semiconductor/knowledge/e-learning/basics-of-schottky-barrier-diodes/chap1/chap1-4.html).

Toshiba explains that near the junction, electrons in the n-type region and holes in the p-type region disappear by recombination, creating a depletion layer where no carrier exists [Toshiba, *1-3. pn junction*](https://toshiba.semicon-storage.com/us/semiconductor/knowledge/e-learning/basics-of-schottky-barrier-diodes/chap1/chap1-4.html).

This region is electrically very important because it produces a barrier to further majority-carrier diffusion. The junction therefore does not allow free two-way current like an ordinary metal conductor.

#### Barrier potential and depletion region

The depletion region contains fixed charged ions left behind after mobile carriers diffuse away and recombine. This creates an internal electric field and a built-in potential difference often called the **barrier potential** or **built-in potential**.

At diploma-entry level, the exact semiconductor physics of the built-in field need not be developed mathematically. What matters is this:

- the junction creates a natural barrier,
- forward bias reduces its effective opposition,
- reverse bias increases its effective opposition.

This one idea explains the basic operation of the diode.

**Image prompt for Figure 5.3:** Create a clean textbook-style illustration of a silicon p-n junction before and after equilibrium. Show p-type region on the left and n-type region on the right. Label holes, electrons, the depletion region, fixed acceptor ions, fixed donor ions, and the built-in electric field direction. Include a simple energy-barrier indication and keep the diagram clear for diploma beginners.

#### What is a diode

A **diode** is a semiconductor device with two terminals, an **anode** and a **cathode**, that allows current mainly in one direction [Toshiba, *What is a diode?*](https://toshiba.semicon-storage.com/us/semiconductor/knowledge/faq/diode/what-are-diodes.html).

Toshiba states that a diode has two terminals, anode and cathode, and allows current to flow only in one direction under ordinary operation [Toshiba, *What is a diode?*](https://toshiba.semicon-storage.com/us/semiconductor/knowledge/faq/diode/what-are-diodes.html).

This one-way behavior is called **rectification**.

#### Forward bias

If the p-side is connected to the positive terminal of a source and the n-side to the negative terminal, the diode is **forward biased**.

In forward bias:

- the external voltage opposes the barrier,
- the depletion region becomes narrower,
- majority carriers can cross the junction more easily,
- current increases strongly after the forward voltage becomes sufficient.

Toshiba notes that for a silicon p-n junction diode, conduction begins around a forward voltage of roughly `0.7 V` [Toshiba, *How do diodes work?*](https://toshiba.semicon-storage.com/us/semiconductor/knowledge/faq/diode/how-do-diodes-work.html).

This does not mean the diode has exactly `0.700 V` under all conditions. The actual forward voltage depends on current, temperature, and device type. But `0.7 V` is a very useful beginner value for an ordinary silicon junction diode.

#### Reverse bias

If the p-side is connected to the negative terminal and the n-side to the positive terminal, the diode is **reverse biased**.

In reverse bias:

- the external voltage supports the barrier,
- the depletion region widens,
- majority carriers are pulled away from the junction,
- only a very small reverse leakage current flows under normal conditions.

If the reverse voltage becomes too large, breakdown occurs and large current can flow. In ordinary p-n diodes this is usually an unwanted condition unless the diode is specifically designed for breakdown operation, as in a Zener diode.

#### V-I characteristics of a p-n junction diode

The **V-I characteristic** of a diode tells how current changes with applied voltage.

In forward bias:

- current remains very small at first,
- then rises rapidly after the knee region,
- this is why a diode is often approximated as having a forward drop.

In reverse bias:

- current remains very small over a wide voltage range,
- then rises sharply at breakdown.

Toshiba gives a typical beginner statement that forward voltage for a silicon p-n diode is around `700 mV`, while reverse breakdown occurs at a product-dependent voltage that may be tens to hundreds of volts [Toshiba, *What is a diode?*](https://toshiba.semicon-storage.com/us/semiconductor/knowledge/faq/diode/what-are-diodes.html).

#### Static approximation for basic circuits

In first-year problems, we often use a simplified model:

- diode off in reverse bias,
- diode on in forward bias with about `0.7 V` drop for silicon.

This approximation is not the whole truth, but it is very useful for introductory circuit analysis.

#### Worked Example 5.3

A silicon diode is forward biased in a simple circuit. Using the basic constant-drop approximation, what forward voltage may be assumed across the diode?

For an ordinary silicon p-n junction diode at beginner level, we use:

$$
V_D \approx 0.7\ \text{V}
$$

So the assumed forward voltage is **about `0.7 V`**.

#### Worked Example 5.4

A silicon diode is connected in series with a resistor and a `5 V` DC source. Assume the diode is forward biased and has a constant drop of `0.7 V`. Find the voltage across the resistor.

The source voltage is:

$$
V_S = 5\ \text{V}
$$

The diode drop is:

$$
V_D = 0.7\ \text{V}
$$

So the resistor voltage is:

$$
V_R = V_S - V_D = 5 - 0.7 = 4.3\ \text{V}
$$

So the resistor has **`4.3 V`** across it.

#### Common diode applications

Even at introductory level, several applications are worth knowing.

**Rectification:** A diode passes one half of an AC waveform more easily than the other. This is the basis of rectifier circuits [Toshiba, *What is a diode?*](https://toshiba.semicon-storage.com/us/semiconductor/knowledge/faq/diode/what-are-diodes.html).

**Clipping and limiting:** Diodes can limit signal amplitude and protect circuit inputs from excessive voltage [Toshiba, *What is a diode?*](https://toshiba.semicon-storage.com/us/semiconductor/knowledge/faq/diode/what-are-diodes.html).

**Reverse battery protection:** A series diode can protect a circuit if battery polarity is connected incorrectly [Toshiba, *What is a diode?*](https://toshiba.semicon-storage.com/us/semiconductor/knowledge/faq/diode/what-are-diodes.html).

**Signal switching:** Fast diodes such as the 1N4148 are used in small-signal switching and logic-related circuits [Nexperia, *1N4148; 1N4448 High-speed diodes*](https://assets.nexperia.com/documents/data-sheet/1N4148_1N4448.pdf).

#### Real diode ratings students should recognize

A real diode datasheet may include:

- maximum reverse voltage,
- continuous forward current,
- forward voltage,
- reverse leakage current,
- package type,
- switching speed or recovery characteristics,
- power dissipation.

These ratings matter because a diode is not "just one-way." It must also survive the applied voltage, carry the required current, and operate fast enough for the intended circuit.

#### Common misconceptions

- A diode does not behave like a perfect short circuit in forward bias. It still has forward voltage drop.
- A diode does not block all reverse current absolutely. A small leakage current exists.
- `0.7 V` is a useful silicon approximation, not a universal exact value for every diode and every current.
- Breakdown in a normal diode is not usually meant for ordinary operation unless the device is designed for that purpose.

#### Practical note

When students first see a diode symbol in a charger or adapter circuit, they should immediately think of three questions:

- which side is the anode and which is the cathode,
- is it forward biased or reverse biased,
- and what current path is it allowing or blocking?

### 5.4 Transistor

#### Why the transistor matters

The diode allows or blocks current mainly in one direction. The **transistor** goes further. It allows a small input current or voltage condition to control a larger current. This made modern electronics possible.

At diploma-entry level, we focus on the **bipolar junction transistor** or **BJT**, because the syllabus asks for NPN and PNP concept and **common-emitter (CE)** operation.

#### NPN and PNP concept

A BJT is formed from two p-n junctions and has three regions:

- **emitter**
- **base**
- **collector**

There are two types:

- **NPN transistor**
- **PNP transistor**

Toshiba explains that a bipolar transistor consists of collector, base, and emitter regions, with a very thin base region between emitter and collector [Toshiba, *How do npn and pnp transistors operate?*](https://toshiba.semicon-storage.com/us/semiconductor/knowledge/faq/mosfet_bipoler-transistors/how-do-npn-and-pnp-transistors-operate.html).

**Image prompt for Figure 5.4:** Create a clean textbook-style comparison of NPN and PNP transistor symbols and simplified layer structures. Show the three terminals emitter, base, and collector for each. Label the emitter arrow direction clearly, and place a simple note that arrow out indicates NPN and arrow in indicates PNP. Include the layer order for each device.

#### Identification of emitter, base, and collector

Each transistor terminal has a different role.

**Emitter:** emits the main charge carriers into the base region.

**Base:** very thin central region that controls the transistor action.

**Collector:** collects most of the carriers that pass through the base region.

Students must not assume collector and emitter are interchangeable. Toshiba explicitly notes that a transistor does not function properly if collector and emitter are reversed, because the internal dopant concentrations are intentionally different [Toshiba, *Are the collector and emitter terminals of a bipolar transistor interchangeable?*](https://toshiba.semicon-storage.com/us/semiconductor/knowledge/faq/mosfet_bipoler-transistors/are-the-collector-and-emitter-terminals-of-a-bipolar-transistor.html).

This is an important practical warning. Pin identification matters.

#### How a transistor works physically

Consider an NPN transistor. If the base-emitter junction is forward biased and the base-collector junction is reverse biased, carriers injected from the emitter cross the thin base region and are collected by the collector. Because the base is very thin and lightly doped compared with the emitter, most injected carriers reach the collector rather than recombining in the base [Toshiba, *How do npn and pnp transistors operate?*](https://toshiba.semicon-storage.com/us/semiconductor/knowledge/faq/mosfet_bipoler-transistors/how-do-npn-and-pnp-transistors-operate.html).

This leads to the central transistor idea:

- a small base current controls a much larger collector current.

Toshiba also states that BJTs are current-driven devices and that when a small base current flows, collector current of approximately $I_B \times h_{FE}$ flows [Toshiba, *Bipolar Transistors (BJTs)*](https://toshiba.semicon-storage.com/us/semiconductor/knowledge/e-learning/discrete/chap3/chap3-2.html).

#### Current relations in a BJT

At concept level, the basic current relation is:

$$
\boxed{I_E = I_B + I_C} \tag{5.1}
$$

where:

- $I_E$ is emitter current,
- $I_B$ is base current,
- $I_C$ is collector current.

The DC current gain is often written as:

$$
\boxed{\beta = h_{FE} = \frac{I_C}{I_B}} \tag{5.2}
$$

So, approximately:

$$
\boxed{I_C = \beta I_B} \tag{5.3}
$$

This is a simplified relation suitable for introductory CE calculations. In real devices, $\beta$ changes with operating conditions and is never a perfectly fixed constant.

#### Common-emitter configuration

In the **common-emitter (CE)** configuration, the emitter is the terminal common to the input and output circuits. The input is applied between base and emitter. The output is taken between collector and emitter.

This configuration is widely used because:

- it can provide current gain,
- it can provide voltage gain in amplifier circuits,
- and it is very common in switching applications.

At beginner level, CE mode is best understood in three operating regions.

#### Cut-off region

In **cut-off**, the base-emitter junction is not sufficiently forward biased. Base current is very small or zero, and collector current is nearly zero. The transistor behaves like an open switch.

#### Active region

In the **active region**, the base-emitter junction is forward biased and the base-collector junction is reverse biased. Here the transistor acts as an amplifier. Collector current is controlled by base current.

#### Saturation region

In **saturation**, the transistor is driven hard on. Collector-emitter voltage becomes low, and the transistor behaves like a closed switch.

For switching applications, the practical goal is usually to move the transistor clearly between cut-off and saturation.

#### CE operation of an NPN transistor

For a typical silicon NPN transistor in CE mode:

- base is about `0.7 V` higher than emitter when the transistor is on in the basic approximation,
- collector is usually connected to the supply through a load resistor,
- a small base current allows a larger collector current.

This is why CE circuits are used for:

- LED driving,
- relay driving,
- small-signal amplification,
- sensor interfacing,
- switching logic-level signals to larger currents.

#### Worked Example 5.5

A transistor in CE mode has current gain $\beta = 100$. If the base current is `20 µA`, find the collector current using the basic gain relation.

Use Equation (5.3):

$$
I_C = \beta I_B
$$

Substitute:

$$
I_C = 100 \times 20\ \mu\text{A}
$$

$$
I_C = 2000\ \mu\text{A} = 2\ \text{mA}
$$

So the collector current is **`2 mA`**.

#### Worked Example 5.6

A transistor in CE mode carries collector current `4 mA` when the base current is `40 µA`. Find the DC current gain.

Use Equation (5.2):

$$
\beta = \frac{I_C}{I_B}
$$

Substitute:

$$
\beta = \frac{4\ \text{mA}}{40\ \mu\text{A}}
$$

Convert `4 mA` to `4000 µA`:

$$
\beta = \frac{4000}{40} = 100
$$

So the DC current gain is **100**.

#### CE transistor as a switch

In a simple switching circuit:

- if base current is absent, transistor is off and collector current is nearly zero,
- if enough base current is provided, transistor saturates and current flows through the collector load.

This makes the transistor an electronically controlled switch.

Practical examples include:

- switching an LED,
- operating a relay from a small control signal,
- driving a buzzer,
- controlling a sensor output stage.

#### CE transistor as a simple amplifier

In the active region, a small change in base current causes a larger change in collector current. With a collector resistor, this change in current produces a change in output voltage.

This is the basis of amplification. At diploma-entry level, the key idea is enough:

- small signal at the base,
- larger controlled variation at the collector,
- CE mode can therefore provide useful amplification.

Detailed small-signal transistor amplifier design belongs to a later electronics course.

#### Real transistor ratings students should recognize

A transistor datasheet may include:

- collector-emitter voltage rating,
- collector current rating,
- power dissipation,
- package type,
- DC current gain range,
- saturation voltages,
- pin order.

These ratings tell whether the transistor is suitable for switching or amplification in a given circuit.

#### Common misconceptions

- A transistor is not just “two diodes back to back.” The three-region transistor action depends on geometry, doping, and carrier flow through the thin base.
- Current gain is not infinite and not perfectly fixed.
- Collector and emitter are not interchangeable in ordinary transistor use.
- A transistor does not automatically amplify every signal just because three terminals exist. Proper biasing is required.
- In switching use, the transistor should be clearly driven toward cut-off or saturation instead of remaining uncertain between them.

#### Practical note

If a circuit diagram shows a transistor controlling a relay coil or LED from a weak sensor signal, the transistor is almost certainly being used in CE mode as a switch. That is one of the first real uses students should learn to recognize.

## Worked Interpretation Exercise

Consider the [onsemi P2N2222A transistor datasheet](https://www.onsemi.com/download/data-sheet/pdf/p2n2222a-d.pdf) [onsemi, *P2N2222A Amplifier Transistors NPN Silicon*].

From the first page and electrical-characteristics table, we can read these values:

- package: `TO-92`
- terminal order shown on the package drawing: `1 = Collector`, `2 = Base`, `3 = Emitter`
- collector-emitter voltage rating `VCEO = 40 V`
- continuous collector current `IC = 600 mA`
- total device dissipation at `25°C` ambient: `625 mW`
- a typical DC current gain range is listed under various conditions, for example `hFE` minimum `100` at `IC = 150 mA`, `VCE = 10 V`

Now interpret these values carefully.

First, the pin identification matters immediately. The datasheet drawing shows:

- pin 1 = collector
- pin 2 = base
- pin 3 = emitter

This tells us the transistor cannot be wired correctly by guessing the pin order. In a laboratory breadboard circuit, that one detail is often the difference between proper operation and a non-working circuit.

Second, `VCEO = 40 V` means the collector-emitter path must not be subjected to more than `40 V` under the stated rating condition. So this transistor is suitable for many low-voltage circuits but not for arbitrary high-voltage switching.

Third, `IC = 600 mA` is the continuous collector current rating. That does not mean every circuit should operate right at `600 mA`. The actual safe circuit also depends on power dissipation, temperature, and saturation conditions.

Fourth, the datasheet gives a current-gain value `hFE`, but not as one fixed universal number. Instead it gives gain under specified test conditions. This reminds us that transistor gain varies with current and operating point. So in beginner calculations we may use a nominal value, but practical design always respects datasheet ranges.

Fifth, the datasheet also lists saturation values such as `VCE(sat)`. That directly supports the switching idea from this chapter: when driven hard on, the transistor does not become a perfect short circuit, but the collector-emitter voltage becomes low.

This one artifact ties several chapter ideas together:

- identification of collector, base, and emitter,
- current gain,
- switching use,
- voltage and current limits,
- and the difference between a conceptual transistor model and a real component.

## How This Matters in Practice

In household and industrial electrical systems, semiconductors appear in chargers, adapters, inverters, motor controllers, protection circuits, sensor interfaces, and control panels. Even when the main load is a motor or transformer, semiconductor devices often control or rectify the electrical energy around it.

In transformers and motors, Chapter 4 showed large electromechanical devices. Semiconductor devices now provide the small control and conversion functions around them. Diodes are used in rectifier inputs and protection paths. Transistors are used in switching, low-level amplification, and control interfaces.

In battery charging, diodes are central because charging circuits usually need rectification or reverse-current protection. In solar PV and inverter-based systems, semiconductor junctions form the basis of rectifiers, regulators, and switching stages. Even when the detailed power electronics is outside this syllabus, the basic diode and transistor ideas are already present.

In instrumentation and control circuits, transistors are often used to amplify weak signals from sensors or to switch relays, buzzers, and indicators. In digital systems and automation, semiconductor devices become the foundation of logic gates, integrated circuits, and microcontrollers. This chapter is therefore the bridge between basic electrical engineering and practical electronics.

## Chapter Summary

- A **semiconductor** has conductivity between that of a conductor and an insulator, but its conductivity can be controlled strongly.
- In crystals, electron energies form **bands**. The highest filled band is the **valence band**, the next is the **conduction band**, and the separation is the **band gap**.
- Silicon forms **covalent bonds** in its crystal structure.
- In an **intrinsic semiconductor**, the number of free electrons equals the number of holes.
- **Doping** creates an **extrinsic semiconductor** by adding controlled impurity atoms.
- Pentavalent donor impurities create **n-type** material; trivalent acceptor impurities create **p-type** material.
- In **n-type** material, electrons are majority carriers and holes are minority carriers.
- In **p-type** material, holes are majority carriers and electrons are minority carriers.
- Joining p-type and n-type material forms a **p-n junction**.
- Carrier recombination near the junction creates the **depletion region** and barrier effect.
- A **diode** is a two-terminal semiconductor device with **anode** and **cathode** that mainly allows current in one direction.
- In **forward bias**, the diode conducts; in **reverse bias**, it blocks except for small leakage until breakdown.
- For a silicon p-n junction diode, a forward drop of about `0.7 V` is a useful beginner approximation.
- The diode V-I characteristic shows rapid current rise in forward bias and very small current in reverse bias until breakdown.
- Common diode applications include rectification, clipping/limiting, and protection.
- A **bipolar junction transistor (BJT)** has three terminals: **emitter**, **base**, and **collector**.
- BJTs come in **NPN** and **PNP** forms.
- In a BJT, $I_E = I_B + I_C$.
- DC current gain may be written as $\beta = h_{FE} = I_C/I_B$.
- In **common-emitter (CE)** mode, the emitter is common to input and output circuits.
- CE transistor operation is commonly understood through **cut-off**, **active**, and **saturation** regions.
- In CE mode, a transistor can be used as a **switch** or as a **simple amplifier**.
- Real semiconductor devices must always be chosen using datasheet limits such as voltage, current, package, and dissipation.

## Further Reading

1. [Britannica, *semiconductor*](https://www.britannica.com/science/semiconductor)  
   Useful for a clear overview of intrinsic and extrinsic semiconductors, energy bands, and doping.

2. [Toshiba, *1-3. pn junction*](https://toshiba.semicon-storage.com/us/semiconductor/knowledge/e-learning/basics-of-schottky-barrier-diodes/chap1/chap1-4.html)  
   Useful for depletion layer formation and the physical meaning of the p-n junction.

3. [Toshiba, *What is a diode?*](https://toshiba.semicon-storage.com/us/semiconductor/knowledge/faq/diode/what-are-diodes.html)  
   Useful for diode structure, forward and reverse behavior, and simple practical applications.

4. [Toshiba, *How do npn and pnp transistors operate?*](https://toshiba.semicon-storage.com/us/semiconductor/knowledge/faq/mosfet_bipoler-transistors/how-do-npn-and-pnp-transistors-operate.html)  
   Useful for a practical explanation of emitter, base, collector, transistor bias, and current amplification.

5. [onsemi, *P2N2222A Amplifier Transistors NPN Silicon*](https://www.onsemi.com/download/data-sheet/pdf/p2n2222a-d.pdf)  
   A real transistor datasheet that helps students connect textbook ideas about terminal identification, gain, current, and voltage limits with an actual device.
