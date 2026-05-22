# Unit 5: Overview of Basic Semiconductor Devices

Up to this point, the book has focused mainly on electrical quantities, magnetic effects, AC circuits, transformers, and motors. Those topics explain how electrical energy is produced, transferred, measured, and converted into motion. This chapter begins the electronics side of the subject. Here the central question changes. Instead of only asking how current flows in wires and machines, we now ask how a material can be engineered so that current is allowed, opposed, controlled, or amplified inside a tiny solid device.

That is the role of the **semiconductor**. From a semiconductor, engineers build **diodes**, **transistors**, and eventually integrated circuits. The aim here is not semiconductor fabrication science in full detail, but to understand why materials such as silicon are special, how **doping** changes their behavior, how a **p-n junction** forms, why a diode conducts mainly in one direction, and how a transistor can act as a switch or amplifier.

This chapter connects strongly to what has already been learned. Chapter 1 introduced current, voltage, resistance, and waveforms. Chapter 3 showed AC rectification contexts where diodes naturally appear. Chapter 4 ended with practical control and conversion equipment that often contains semiconductor devices. Later chapters on analog circuits, op-amps, and digital logic depend directly on the ideas introduced here.

## 5.1 Semiconductor Fundamentals

### Why semiconductors are different

Suppose we compare three materials placed in a circuit:

- copper wire,
- glass,
- and silicon.

Copper allows current to pass very easily. Glass practically blocks it. Silicon lies between these two extremes. Its value in electronics comes from the way its conductivity can be changed strongly by temperature, light, electric field, and tiny amounts of impurity atoms called dopants.

This makes semiconductors useful for electronics. A copper wire is excellent for carrying current, but it is not easy to use copper itself as a current-controlling electronic device. A semiconductor can be shaped and doped so that it acts as a rectifier, switch, amplifier, sensor, or logic element.

### Conductor, insulator, and semiconductor

A **conductor** is a material in which charge carriers can move easily. Metals such as copper and aluminum are common conductors.

An **insulator** is a material in which charge carriers are not free to move under ordinary conditions. Glass, mica, rubber, and many plastics are insulators.

A **semiconductor** is a material whose conductivity lies between that of a conductor and an insulator.

The three classes are not merely labels of "good," "bad," and "medium" conductors. Their internal energy structure is different, and semiconductor device behavior follows from that structure.

**Image prompt for Figure 5.1:** Create a clean textbook-style three-panel energy-band diagram comparing a conductor, semiconductor, and insulator. In each panel show a valence band, conduction band, and band gap. For the conductor, show overlap or zero gap between valence and conduction bands. For the semiconductor, show a small band gap. For the insulator, show a large band gap. Label each panel clearly and keep the illustration simple and engineering-oriented.

### Energy bands: valence band, conduction band, and band gap

Inside a crystal, electrons do not behave as if each atom were fully isolated. When many atoms come together to form a solid, the discrete energy levels spread into **energy bands**. The highest filled band is called the **valence band**. The next higher band is the **conduction band**. Between them there may be an **energy gap**, also called the **band gap**.

The basic picture is:

- In a **conductor**, electrons can move easily because the valence and conduction situations effectively allow free conduction.
- In a **semiconductor**, the band gap is small enough that some electrons can move to the conduction band under suitable conditions.
- In an **insulator**, the band gap is so large that ordinary conduction is strongly prevented.

Important semiconductors have relatively small band gaps compared with insulators. Silicon, for example, has a band gap of about `1.12 eV`. The value itself is less important here than the fact that a semiconductor band gap is small enough to allow controlled conduction.

### Covalent bonding in silicon

Silicon is the most important semiconductor material in basic electronics. A silicon atom has four outer electrons. In a silicon crystal, each atom shares electrons with neighboring atoms, forming **covalent bonds**.

At low temperature, these electrons are largely tied up in bonds, so conduction is weak. As temperature rises, some bonds break. Then some electrons gain enough energy to move into the conduction band. Once an electron leaves a bond, it leaves behind an electron vacancy called a **hole**.

This is a central semiconductor idea:

- the free **electron** can carry negative charge,
- the **hole** behaves like a mobile positive charge carrier.

Both electrons and holes contribute to current in semiconductors.

### Intrinsic semiconductor

A very pure semiconductor is called an **intrinsic semiconductor**. In an intrinsic semiconductor, the number of free electrons equals the number of holes.

This equality is physically reasonable. Every time a covalent bond breaks and releases one electron, one hole is left behind. So carriers are generated in pairs:

- one electron,
- one hole.

Pure silicon and pure germanium are standard examples.

Intrinsic semiconductors conduct only weakly at room temperature compared with metals. That is why pure semiconductor material alone is not enough for most practical electronic devices. The conductivity must be controlled more strongly. This is done by doping.

### Extrinsic semiconductor and doping

An impurity-added semiconductor is called an **extrinsic semiconductor**. The deliberate addition of suitable impurity atoms is called **doping**.

Even tiny amounts of suitable impurity atoms can greatly increase conductivity. This shows how sensitive semiconductor behavior is to very small changes in composition.

Doping does not mean "contaminating the material carelessly." It means introducing carefully chosen impurity atoms in controlled amounts so that charge carriers of the desired type become dominant.

Two important dopant categories are:

- **Donor impurities:** provide extra electrons.
- **Acceptor impurities:** create holes.

These lead to n-type and p-type material, which are studied in the next section.

### Why doping matters physically

Without doping, the semiconductor is too weakly conducting for many practical electronic purposes. With doping, the number of useful charge carriers can be increased strongly. More importantly, the engineer can choose whether electrons or holes become the dominant carriers.

This gives a powerful design advantage:

- if we want electron-dominated conduction, we create n-type material,
- if we want hole-dominated conduction, we create p-type material,
- and if we join p-type and n-type regions together, we create the basis of the diode and transistor.

### Temperature effect in semiconductors

An intuition from metals can be misleading in semiconductors. In many metals, heating increases resistance. In semiconductors, increasing temperature can increase the number of available charge carriers, so conductivity tends to increase.

The practical result is:

- in a semiconductor, temperature strongly affects carrier concentration,
- and semiconductor devices must therefore be used within rated temperature limits.

This is one reason datasheets always include temperature ratings.

::: {.worked-example title="Worked Example 5.1"}

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

:::

## 5.2 P-Type and N-Type Semiconductor

### From pure silicon to useful material

A pure silicon crystal is important for understanding, but practical devices need more control than intrinsic silicon provides. We now deliberately insert impurity atoms into the crystal. The result is still mostly silicon, but its electrical behavior changes greatly.

The two basic results are:

- **n-type semiconductor**
- **p-type semiconductor**

These are not two unrelated materials. They are two differently doped forms of semiconductor material.

### N-type semiconductor

If a pentavalent impurity atom such as phosphorus, arsenic, or antimony is added to silicon, four of its outer electrons form covalent bonds with neighboring silicon atoms. One extra electron remains weakly bound and can become a conduction electron. The dopant acts as a **donor**.

This creates an **n-type semiconductor**, where electrons are the majority carriers.

The name "n-type" does not mean the whole material has net negative charge. The material remains electrically neutral overall. It means the dominant mobile charge carriers are negative electrons.

### P-type semiconductor

If a trivalent impurity atom such as boron, aluminum, or gallium is added to silicon, only three covalent bonds can be completed directly. One bond position lacks an electron. This creates a hole. The impurity acts as an **acceptor**.

This creates a **p-type semiconductor**, where holes are the majority carriers.

Again, "p-type" does not mean the entire material is positively charged. It means the dominant mobile carriers are positive holes.

### Majority and minority carriers

This vocabulary is very important in all semiconductor devices.

In n-type material:

- **majority carriers** are electrons,
- **minority carriers** are holes.

In p-type material:

- **majority carriers** are holes,
- **minority carriers** are electrons.

These minority carriers are still important. They become especially important in reverse-biased diodes and transistor operation.

### How to picture the carrier situation

The carrier picture is:

- intrinsic semiconductor: balanced but weak conduction,
- n-type semiconductor: many useful electrons added,
- p-type semiconductor: many useful holes created.

So the engineer is not only increasing conductivity. The engineer is choosing which carrier type will dominate.

**Image prompt for Figure 5.2:** Create a clean textbook-style two-panel illustration comparing n-type and p-type silicon crystals. In the n-type panel, show a silicon lattice with one pentavalent donor atom, four covalent bonds, and one extra free electron. Label donor impurity, free electron, majority carriers, and minority holes. In the p-type panel, show a silicon lattice with one trivalent acceptor atom, one incomplete bond represented as a hole, and label acceptor impurity, hole, majority carriers, and minority electrons.

### Properties of n-type and p-type material

The practical properties may be summarized as follows.

**Table 5.1: Comparison of n-type and p-type semiconductors**

| Property | n-type | p-type |
|---|---|---|
| Dopant type | pentavalent donor | trivalent acceptor |
| Typical dopants | P, As, Sb | B, Al, Ga |
| Majority carriers | electrons | holes |
| Minority carriers | holes | electrons |
| Dominant current mechanism | electron conduction | hole conduction |

This table is compact, but each row should be connected to the physical carrier picture rather than memorized as isolated words.

::: {.worked-example title="Worked Example 5.2"}

A silicon sample is doped with phosphorus. Identify:

1. whether it becomes p-type or n-type,
2. the majority carriers,
3. the minority carriers.

Phosphorus is a pentavalent impurity. Pentavalent impurities act as donors and create n-type material.

So:

- type = **n-type**
- majority carriers = **electrons**
- minority carriers = **holes**

:::

### Practical uses of p-type and n-type material

By themselves, p-type and n-type materials are already useful concepts, but their greatest importance appears when they are combined.

Applications based on p-type and n-type regions include:

- p-n junction diodes,
- bipolar transistors,
- many sensor structures,
- rectifiers,
- switching devices,
- logic and integrated circuits.

P-type and n-type materials are the building blocks from which junction devices are formed.

## 5.3 PN Junction Diode

### From two regions to one junction

Now imagine joining p-type material and n-type material in one crystal. At the instant they are joined, the carrier concentrations are very different on the two sides:

- many holes on the p-side,
- many electrons on the n-side.

Nature does not leave this imbalance unchanged. Carriers begin to diffuse across the boundary. This leads to the most important structure in basic electronics: the **p-n junction**.

### Formation of the p-n junction

When p-type and n-type semiconductors are joined, electrons from the n-side and holes from the p-side diffuse toward the junction. Near the boundary, they recombine. As a result, a region forms where there are no mobile charge carriers. This is the **depletion layer**.

This region is electrically very important because it produces a barrier to further majority-carrier diffusion. The junction therefore does not allow free two-way current like an ordinary metal conductor.

### Barrier potential and depletion region

The depletion region contains fixed charged ions left behind after mobile carriers diffuse away and recombine. This creates an internal electric field and a built-in potential difference often called the **barrier potential** or **built-in potential**.

The built-in field does not need a mathematical treatment here. Its operating effect is:

- the junction creates a natural barrier,
- forward bias reduces its effective opposition,
- reverse bias increases its effective opposition.

This one idea explains the basic operation of the diode.

**Image prompt for Figure 5.3:** Create a clean textbook-style illustration of a silicon p-n junction before and after equilibrium. Show p-type region on the left and n-type region on the right. Label holes, electrons, the depletion region, fixed acceptor ions, fixed donor ions, and the built-in electric field direction. Include a simple energy-barrier indication and keep the diagram clear for diploma beginners.

### What is a diode

A **diode** is a semiconductor device with two terminals, an **anode** and a **cathode**, that allows current mainly in one direction under ordinary operation.

This one-way behavior is called **rectification**.

### Forward bias

If the p-side is connected to the positive terminal of a source and the n-side to the negative terminal, the diode is **forward biased**.

In forward bias:

- the external voltage opposes the barrier,
- the depletion region becomes narrower,
- majority carriers can cross the junction more easily,
- current increases strongly after the forward voltage becomes sufficient.

For a silicon p-n junction diode, conduction begins around a forward voltage of roughly `0.7 V`.

This does not mean the diode has exactly `0.700 V` under all conditions. The actual forward voltage depends on current, temperature, and device type. But `0.7 V` is a useful approximation for an ordinary silicon junction diode.

### Reverse bias

If the p-side is connected to the negative terminal and the n-side to the positive terminal, the diode is **reverse biased**.

In reverse bias:

- the external voltage supports the barrier,
- the depletion region widens,
- majority carriers are pulled away from the junction,
- only a very small reverse leakage current flows under normal conditions.

If the reverse voltage becomes too large, breakdown occurs and large current can flow. In ordinary p-n diodes this is usually an unwanted condition unless the diode is specifically designed for breakdown operation, as in a Zener diode.

### V-I characteristics of a p-n junction diode

The **V-I characteristic** of a diode tells how current changes with applied voltage.

In forward bias:

- current remains very small at first,
- then rises rapidly after the knee region,
- this is why a diode is often approximated as having a forward drop.

In reverse bias:

- current remains very small over a wide voltage range,
- then rises sharply at breakdown.

For a silicon p-n diode, the forward voltage is often approximated as about `700 mV`, while reverse breakdown occurs at a product-dependent voltage that may be tens to hundreds of volts.

### Static approximation for basic circuits

For hand calculations, we often use a simplified model:

- diode off in reverse bias,
- diode on in forward bias with about `0.7 V` drop for silicon.

This approximation is not the whole truth, but it is very useful for basic circuit analysis.

::: {.worked-example title="Worked Example 5.3"}

A silicon diode is forward biased in a simple circuit. Using the basic constant-drop approximation, what forward voltage may be assumed across the diode?

For an ordinary silicon p-n junction diode, we use:

$$
V_D \approx 0.7\ \text{V}
$$

So the assumed forward voltage is **about `0.7 V`**.

:::

::: {.worked-example title="Worked Example 5.4"}

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

:::

### Common diode applications

Several applications are worth knowing.

**Rectification:** A diode passes one half of an AC waveform more easily than the other. This is the basis of rectifier circuits.

**Clipping and limiting:** Diodes can limit signal amplitude and protect circuit inputs from excessive voltage.

**Reverse battery protection:** A series diode can protect a circuit if battery polarity is connected incorrectly.

**Signal switching:** Fast diodes such as the 1N4148 are used in small-signal switching and logic-related circuits.

### Real diode ratings

A real diode datasheet may include:

- maximum reverse voltage,
- continuous forward current,
- forward voltage,
- reverse leakage current,
- package type,
- switching speed or recovery characteristics,
- power dissipation.

These ratings matter because a diode is not "just one-way." It must also survive the applied voltage, carry the required current, and operate fast enough for the intended circuit.

## 5.4 Transistor

### Why the transistor matters

The diode allows or blocks current mainly in one direction. The **transistor** goes further. It allows a small input current or voltage condition to control a larger current. This made modern electronics possible.

This section focuses on the **bipolar junction transistor** or **BJT**, including the NPN and PNP concept and **common-emitter (CE)** operation.

### NPN and PNP concept

A BJT is formed from two p-n junctions and has three regions:

- **emitter**
- **base**
- **collector**

There are two types:

- **NPN transistor**
- **PNP transistor**

A bipolar transistor consists of collector, base, and emitter regions, with a very thin base region between emitter and collector.

**Image prompt for Figure 5.4:** Create a clean textbook-style comparison of NPN and PNP transistor symbols and simplified layer structures. Show the three terminals emitter, base, and collector for each. Label the emitter arrow direction clearly, and place a simple note that arrow out indicates NPN and arrow in indicates PNP. Include the layer order for each device.

### Identification of emitter, base, and collector

Each transistor terminal has a different role.

**Emitter:** emits the main charge carriers into the base region.

**Base:** very thin central region that controls the transistor action.

**Collector:** collects most of the carriers that pass through the base region.

Do not assume collector and emitter are interchangeable. A transistor does not function properly if collector and emitter are reversed, because the internal dopant concentrations are intentionally different.

Pin identification matters.

### How a transistor works physically

Consider an NPN transistor. If the base-emitter junction is forward biased and the base-collector junction is reverse biased, carriers injected from the emitter cross the thin base region and are collected by the collector. Because the base is very thin and lightly doped compared with the emitter, most injected carriers reach the collector rather than recombining in the base.

This leads to the central transistor idea:

- a small base current controls a much larger collector current.

In the basic BJT model, a small base current controls a larger collector current of approximately $I_B \times h_{FE}$.

### Current relations in a BJT

The basic current relation is:

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

This is a simplified relation suitable for basic CE calculations. In real devices, $\beta$ changes with operating conditions and is never a perfectly fixed constant.

### Common-emitter configuration

In the **common-emitter (CE)** configuration, the emitter is the terminal common to the input and output circuits. The input is applied between base and emitter. The output is taken between collector and emitter.

This configuration is widely used because:

- it can provide current gain,
- it can provide voltage gain in amplifier circuits,
- and it is very common in switching applications.

CE mode is best understood in three operating regions.

### Cut-off region

In **cut-off**, the base-emitter junction is not sufficiently forward biased. Base current is very small or zero, and collector current is nearly zero. The transistor behaves like an open switch.

### Active region

In the **active region**, the base-emitter junction is forward biased and the base-collector junction is reverse biased. Here the transistor acts as an amplifier. Collector current is controlled by base current.

### Saturation region

In **saturation**, the transistor is driven hard on. Collector-emitter voltage becomes low, and the transistor behaves like a closed switch.

For switching applications, the practical goal is usually to move the transistor clearly between cut-off and saturation.

### CE operation of an NPN transistor

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

::: {.worked-example title="Worked Example 5.5"}

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

:::

::: {.worked-example title="Worked Example 5.6"}

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

:::

### CE transistor as a switch

In a simple switching circuit:

- if base current is absent, transistor is off and collector current is nearly zero,
- if enough base current is provided, transistor saturates and current flows through the collector load.

This makes the transistor an electronically controlled switch.

Practical examples include:

- switching an LED,
- operating a relay from a small control signal,
- driving a buzzer,
- controlling a sensor output stage.

### CE transistor as a simple amplifier

In the active region, a small change in base current causes a larger change in collector current. With a collector resistor, this change in current produces a change in output voltage.

This is the basis of amplification:

- small signal at the base,
- larger controlled variation at the collector,
- CE mode can therefore provide useful amplification.

Detailed small-signal transistor amplifier design belongs to a later electronics course.

### Real transistor ratings

A transistor datasheet may include:

- collector-emitter voltage rating,
- collector current rating,
- power dissipation,
- package type,
- DC current gain range,
- saturation voltages,
- pin order.

These ratings tell whether the transistor is suitable for switching or amplification in a given circuit.

## Worked Interpretation Exercise

### Reading a Transistor Datasheet

Consider the onsemi P2N2222A transistor datasheet.

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

Fourth, the current-gain value `hFE` is not one fixed universal number. It is specified under particular test conditions. This reminds us that transistor gain varies with current and operating point. Rough calculations may use a nominal value, but practical design always respects datasheet ranges.

Fifth, saturation values such as `VCE(sat)` directly support the switching idea from this chapter: when driven hard on, the transistor does not become a perfect short circuit, but the collector-emitter voltage becomes low.

This one artifact ties several chapter ideas together:

- identification of collector, base, and emitter,
- current gain,
- switching use,
- voltage and current limits,
- and the difference between a conceptual transistor model and a real component.

## Further Reading

1. Robert L. Boylestad and Louis Nashelsky, *Electronic Devices and Circuit Theory* — popular text for diode and transistor fundamentals with practical circuit examples.

2. Adel S. Sedra and Kenneth C. Smith, *Microelectronic Circuits* — standard electronics text covering semiconductor devices, diode circuits, and BJT operation.

3. Ben G. Streetman and Sanjay Kumar Banerjee, *Solid State Electronic Devices* — widely used semiconductor-device text for energy bands, doping, p-n junctions, and device physics.

4. S. M. Sze and Kwok K. Ng, *Physics of Semiconductor Devices* — classic reference for deeper semiconductor-device physics and p-n junction behavior.
