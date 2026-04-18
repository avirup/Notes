# Chapter 4.3: Isolated DC-DC Converters (Overview)

## Chapter opening

In Chapter 4.2, we studied non-isolated DC-DC converters such as the buck, boost, buck-boost, Cuk, and SEPIC converters. Those circuits are extremely important, but they all share one basic feature: the input side and output side are electrically connected through a continuous conducting path. In many applications, that is perfectly acceptable. In other applications, it is not enough.

Now imagine a few practical situations. A solar inverter may have a high-voltage DC link, but its control board and sensing circuits need a much lower, safer supply. A battery charger may need to keep the user-accessible output electrically separated from the input side. An EV traction inverter may need a small isolated supply to power gate drivers and measurement circuits while the main battery bus sits at a much higher potential. In these cases, we do not want only voltage conversion. We also want **galvanic isolation**.

This chapter introduces the beginner-level picture of **isolated DC-DC converters**. We will first understand why isolation is needed and what it really means physically. Then we will study the two most important introductory isolated topologies in the syllabus: the **flyback converter** and the **forward converter**. After that, we will compare the more powerful double-ended families: **push-pull**, **half-bridge**, and **full-bridge** converters. The syllabus asks for an overview, so our goal here is not detailed magnetics design or advanced control. Our goal is a clear and confident topology-level understanding.

This chapter also forms a bridge to later renewable-energy study. Once we understand why an isolation barrier matters, why a transformer must be excited by a switching waveform rather than steady DC, and why some isolated topologies suit low-power auxiliary supplies while others suit higher-power conversion, we are much better prepared to read charger topologies, inverter auxiliary supplies, EV DC-DC stages, and grid-interface support electronics [Erickson and Maksimovic, *Fundamentals of Power Electronics*, 2e], [Mohan, Undeland, Robbins, *Power Electronics: Converters, Applications, and Design*, 3e].

## Prerequisites check

- You should remember duty cycle, switching period, and the ON-state/OFF-state picture from Chapter 4.1.
- You should remember the non-isolated buck and buck-boost ideas from Chapter 4.2, because flyback and forward converters are easiest to understand as isolated relatives of those circuits.
- You should be comfortable with the idea that an inductor opposes sudden change of current and a capacitor opposes sudden change of voltage.
- You should know the basic ideal-transformer turns-ratio idea, even if only at a simple level.
- You should remember that a transformer cannot transfer steady DC directly; it needs a changing magnetic flux.

If the transformer idea feels weak, do not worry. We will refresh exactly what we need in the first section before moving into the converter topologies.

## Core content

### 4.3.1 Need for galvanic isolation in renewable-energy and battery-charging systems

#### A first physical picture

Suppose a battery energy storage system has a DC bus around $400 \text{ V}$, but the control board needs an isolated $15 \text{ V}$ auxiliary supply for gate drivers, signal conditioning, or protection circuits. At first glance, this sounds like an ordinary step-down problem. Why not simply use a non-isolated buck converter?

The answer is that the voltage value is only part of the problem. The control electronics may need to be electrically separated from the high-voltage battery bus for safety, noise management, ground-reference reasons, or system architecture. In such a case, we do not just want "400 V to 15 V." We want "400 V to 15 V with an isolation barrier in between."

**Galvanic isolation** means there is no direct conducting path for DC current between two circuits. Analog Devices defines it as a design technique that separates electrical circuits so that stray currents are blocked, even though signals or power may still pass across the barrier by some non-conductive coupling method [Analog Devices, "Galvanic Isolation" glossary]. In power electronics, that coupling method is very often magnetic coupling through a transformer.

#### What isolation does and does not do

It helps to be very explicit here, because beginners often hear the word isolation and imagine a perfect wall.

Isolation does these useful things:

- it removes a direct conductive path between input and output
- it improves safety when one side may be at hazardous potential
- it helps break ground loops and reduce unwanted coupling through common ground paths
- it allows the output to "float" with respect to the input side if the application requires that
- it lets us use a transformer turns ratio for convenient step-up or step-down action
- it can support multiple isolated outputs from one switching stage

But isolation does **not** mean:

- zero parasitic capacitance between primary and secondary
- zero noise coupling under all conditions
- zero design effort for creepage, clearance, shielding, and insulation
- automatic compliance with safety standards simply because a transformer is present

That distinction matters. Isolation is a powerful design tool, but it still has to be implemented correctly in real hardware.

#### Why a transformer appears in isolated DC-DC conversion

In ordinary power systems, a transformer works by magnetic coupling between windings. For an ideal transformer,

$$\boxed{\frac{V_s}{V_p} = \frac{N_s}{N_p}} \quad \text{(15.1)}$$

where $V_p$ and $V_s$ are the primary-side and secondary-side voltages, and $N_p$ and $N_s$ are the numbers of primary and secondary turns.

This equation is familiar, but there is an important catch. A transformer needs a changing magnetic flux. A steady DC voltage applied directly to a transformer primary would produce a dangerous magnetizing-current problem rather than normal transformer action. So an isolated DC-DC converter cannot simply connect a DC source to a transformer and expect it to work like a mains-frequency transformer.

Instead, the converter first turns DC into a high-frequency pulsating waveform by switching. That waveform excites the transformer. The transformer then transfers energy across the isolation barrier. On the secondary side, rectifiers and filters convert the transferred high-frequency energy back into a useful DC output [MIT OCW, 6.334 *Power Electronics*, ch7 notes], [Erickson and Maksimovic, *Fundamentals of Power Electronics*, 2e].

The key conceptual picture is that an isolated DC-DC converter performs these steps in sequence:

1. convert DC into a high-frequency switched waveform
2. transfer energy through a transformer across an isolation barrier
3. rectify and smooth the secondary-side waveform back into DC

If we keep that three-step picture in mind, the topologies that follow become much easier to understand.

**Image prompt for Figure 15.1:** Create a clean textbook-style block-level technical illustration of an isolated DC-DC converter. Show a DC input source on the left, a switching stage that converts DC into a high-frequency pulsating waveform, a transformer in the center with a clearly marked isolation barrier between primary and secondary, and a rectifier plus output filter on the right producing DC output. Add arrows showing energy flow left to right. Label the primary side, secondary side, isolation barrier, turns ratio $N_p:N_s$, and indicate that the output may float with respect to the input ground. Use monochrome textbook engineering style with clear labels.

#### Why renewable-energy and battery systems need isolation

The need becomes clearer when we connect the idea to real systems.

In a **battery charger**, isolation can separate the user-side battery terminals or low-voltage battery pack from a higher-voltage input side. In a **solar inverter**, isolation may be needed in auxiliary supplies for control and gate-drive circuits, or in some converter architectures for system safety and grounding strategy. In an **EV**, high-voltage domains and low-voltage control domains often coexist, which makes isolated auxiliary supplies and isolated measurement channels very important [TI, TIDA-01513 reference design], [TI, PMP22288 reference design].

There is also a noise and measurement reason. Renewable-energy systems often contain fast-switching inverters, long cabling, large common-mode voltage swings, and sensitive sensing electronics. Functional isolation can help keep a noisy ground domain from directly disturbing another domain [Analog Devices, "Easy Galvanic Isolation"], [Analog Devices, "Galvanic Isolation" glossary].

Finally, transformers bring a practical benefit that non-isolated converters do not: one switching stage can often create more than one output by adding secondary windings. That is useful in auxiliary supply design, where a solar inverter or EV subsystem may need several isolated low-power rails.

#### A small numerical reminder about turns ratio

Suppose a transformer in an isolated converter has $N_p = 40$ turns and $N_s = 10$ turns. Then

$$\frac{N_s}{N_p} = \frac{10}{40} = 0.25.$$

If the primary-side applied waveform has an ideal amplitude of $80 \text{ V}$ during an interval, the corresponding ideal secondary-side amplitude during that interval is

$$V_s = 0.25 \times 80 = 20 \text{ V}.$$

This does **not** yet tell us the final DC output, because the rectifier arrangement, duty cycle, filter, and topology also matter. But it does show why isolated converters are attractive for large conversion ratios. Turns ratio and duty cycle can work together instead of asking duty cycle alone to do the entire job [Analog Devices, "Isolated Switch-Mode Power Supplies: How to Choose a Forward vs. a Flyback Converter", 2024].

#### Common misconceptions

A common mistake is to treat isolation as only a shock-safety issue. In practice it also matters for noise, floating outputs, level shifting, and multiple-output architectures. Another mistake is to imagine that isolated conversion is just a non-isolated converter with a transformer inserted in the middle. The switching sequence, rectifier arrangement, and magnetic behavior are different, and turns ratio does not replace duty-cycle control. Renewable-energy relevance: galvanic isolation appears naturally in charger auxiliaries, inverter bias supplies, battery-management interfaces, gate-driver supplies, and measurement systems that sit beside high-voltage power stages [TI, PMP22288 reference design], [TI, TIDA-01513 reference design].

### 4.3.2 Flyback converter - topology and applications

#### Why the flyback converter is often the first isolated topology we meet

The **flyback converter** is the simplest isolated converter that many students encounter, and there is a good reason for that. It gives us isolation, step-up or step-down capability, and relatively low part count in one conceptually compact circuit. At a beginner level, the cleanest way to think about it is this:

The flyback converter is the isolated relative of the buck-boost converter.

That sentence is not the full story, but it is a very helpful starting point. Like the buck-boost converter, the flyback stores energy during one part of the switching cycle and delivers it during another part. The difference is that the energy-storage and transfer mechanism now uses a transformer structure with isolated windings rather than a single ordinary inductor [Erickson and Maksimovic, *Fundamentals of Power Electronics*, 2e], [MIT OCW, 6.334 *Power Electronics*, ch7 notes].

Analog Devices describes the flyback as an isolated SMPS topology in which energy is stored during the ON interval and transferred to the output during the OFF interval [Analog Devices, "Isolated Switch-Mode Power Supplies: How to Choose a Forward vs. a Flyback Converter", 2024]. That one sentence captures the heart of flyback operation.

#### The ON interval

During the switch ON interval, the primary winding is connected to the input source. Because of the winding polarity and rectifier arrangement, the secondary diode is reverse biased during this time. So the secondary does not deliver power directly to the load in the simplest flyback picture.

Instead, the input source builds current in the transformer's **magnetizing inductance**. In beginner language, it is fair to say that energy is being stored in the magnetic field.

Meanwhile, the output capacitor supports the load for that short interval.

#### The OFF interval

When the switch turns OFF, the primary current can no longer continue through the switch path. The magnetic field therefore begins to collapse, and the transformer winding voltages reverse in the way needed to keep current flowing. The secondary diode now becomes forward biased, and the stored energy is delivered to the output capacitor and load.

So the flyback converter works in two clear steps:

- ON interval: store energy
- OFF interval: release energy to the output

That is why the flyback feels different from the forward converter, which we will study next. In a forward converter, energy goes to the output during the ON interval itself. In a flyback converter, the main transfer to the output happens during the OFF interval.

**Image prompt for Figure 15.2:** Create a clean textbook-style technical illustration of an isolated flyback converter. Show an input DC source, a primary-side controlled switch, a flyback transformer with dotted polarity marks, a secondary-side diode, output capacitor, and load. Beside the circuit, show two operating states labeled ON interval and OFF interval. In the ON interval, indicate increasing primary magnetizing current and reverse-biased secondary diode. In the OFF interval, indicate reversed winding polarity, forward-biased secondary diode, and current flowing to the output capacitor and load. Add aligned waveforms for gate signal, primary current, and secondary diode current. Use monochrome engineering style with clear labels.

#### A simple ideal gain relation

Let us write the ideal CCM gain relation in a form that is useful at this level. If the converter operates in continuous-conduction mode and we neglect losses, the flyback relation can be written as

$$\boxed{\frac{V_o}{V_{in}} = \frac{N_s}{N_p}\frac{D}{1-D}} \quad \text{(15.2)}$$

Here:

- $V_{in}$ is the input voltage
- $V_o$ is the average output voltage
- $N_p$ and $N_s$ are primary and secondary turns
- $D$ is the duty cycle

Let us motivate this relation rather than simply stating it.

During the ON interval, the magnetizing inductance sees approximately

$$v_{Lm,\text{ON}} = V_{in}. \quad \text{(15.3)}$$

During the OFF interval, the output voltage is reflected to the primary side through the turns ratio, so the primary-side magnetizing voltage is approximately

$$v_{Lm,\text{OFF}} = -\frac{N_p}{N_s}V_o. \quad \text{(15.4)}$$

In steady periodic operation, the average voltage across the magnetizing inductance over one switching period must be zero. Therefore,

$$D(V_{in}) + (1-D)\left(-\frac{N_p}{N_s}V_o\right) = 0. \quad \text{(15.5)}$$

Rearranging gives

$$DV_{in} = (1-D)\frac{N_p}{N_s}V_o$$

and therefore

$$\boxed{V_o = V_{in}\frac{N_s}{N_p}\frac{D}{1-D}} \quad \text{(15.6)}$$

This equation is extremely useful because it shows two control handles at once:

- the **turns ratio** $\dfrac{N_s}{N_p}$
- the **duty cycle** $\dfrac{D}{1-D}$

That is the real strength of isolated conversion. We do not have to rely on duty cycle alone.

#### A numerical example

Suppose an auxiliary isolated supply must produce $15 \text{ V}$ from a $48 \text{ V}$ DC source. Let the flyback transformer turns ratio be

$$\frac{N_s}{N_p} = \frac{1}{3}.$$

Using Equation (15.6),

$$15 = 48 \times \frac{1}{3} \times \frac{D}{1-D}.$$

Now $48 \times \dfrac{1}{3} = 16$, so

$$15 = 16\frac{D}{1-D}.$$

Thus,

$$\frac{D}{1-D} = \frac{15}{16} = 0.9375.$$

Now solve for $D$:

$$D = 0.9375(1-D)$$

$$D = 0.9375 - 0.9375D$$

$$1.9375D = 0.9375$$

$$D \approx 0.484.$$

So the ideal duty cycle is about $48.4\%$.

Notice how reasonable this is. We did not need an extreme duty cycle because the turns ratio already helped shape the voltage conversion.

#### Why flyback converters are popular

At introductory level, the flyback converter is popular because it offers several attractive features:

- relatively low component count
- easy creation of isolated outputs
- ability to step up or step down
- good suitability for low-power and auxiliary supplies
- fairly natural multi-output extension by adding secondary windings

Analog Devices notes that flyback implementations are often favored when smaller size and lower component count matter, while also pointing out that their energy-storage method limits how much power is conveniently transferred compared with forward converters [Analog Devices, "Isolated Switch-Mode Power Supplies: How to Choose a Forward vs. a Flyback Converter", 2024].

#### Where flyback converters appear in practice

A very relevant modern example comes from TI's **PMP22288** reference design, which is a 15 W isolated flyback supply for automotive inverter power. TI lists a wide $40 \text{ V}$ to $550 \text{ V}_{DC}$ input range, an isolated $15 \text{ V}$ output up to $1 \text{ A}$, and identifies the topology as flyback operating in DCM [TI, PMP22288 reference design].

That is a useful real-world reminder. In an EV or traction-inverter environment, the flyback converter is often not the main propulsion power stage. Instead, it is an isolated **auxiliary** supply that powers the electronics around the main power stage.

#### Common misconceptions

A common mistake is to imagine that the flyback transformer transfers energy continuously like an ordinary power transformer. It is better to think of the flyback element as a coupled magnetic component that stores energy during one interval and releases it during another. The output also does not become automatically low-ripple just because isolation is present; the output capacitor still has major work to do. Renewable-energy relevance: flyback converters are common in the isolated support supplies that sit beside the main converter, including gate-driver bias supplies, traction-inverter auxiliaries, battery-management support power, communication power rails, and small charger subcircuits [TI, PMP22288 reference design], [Analog Devices, "Easy Galvanic Isolation"].

### 4.3.3 Forward converter - topology and applications

#### The key change from flyback to forward

The **forward converter** also uses a transformer for isolation, but its energy-transfer idea is different from the flyback converter. Analog Devices describes the difference clearly: the forward converter does not rely on the transformer as the main energy-storage element. Instead, energy is transferred directly to the secondary during the ON interval [Analog Devices, "Isolated Switch-Mode Power Supplies: How to Choose a Forward vs. a Flyback Converter", 2024].

That single sentence is the right starting point.

If the flyback converter is best understood as an isolated buck-boost, then the forward converter is best understood as an isolated buck converter. The transformer provides isolation and turns-ratio scaling, but the output side usually includes an inductor and capacitor that smooth the energy delivered during the ON interval [MIT OCW, 6.334 *Power Electronics*, ch7 notes], [Mohan, Undeland, Robbins, *Power Electronics: Converters, Applications, and Design*, 3e].

#### ON interval

When the primary switch turns ON, the transformer primary is excited. Because of the dot convention and rectifier arrangement, the secondary rectifier that feeds the output becomes forward biased. Energy is transferred immediately through the transformer to the output side. The output inductor stores some of that energy and helps smooth the load current.

So in a forward converter, the load is being supplied during the ON interval itself.

#### OFF interval

When the switch turns OFF, the direct primary-to-secondary transfer stops. But the output inductor current cannot collapse instantly. It therefore continues through a freewheeling path on the secondary side, supporting the load during the OFF interval in a way that closely resembles the OFF interval of a buck converter.

There is also an important magnetic detail: the transformer core must be **reset** or **demagnetized** properly before the next cycle. If that does not happen, flux can build up from cycle to cycle and eventually drive the core toward saturation. In introductory study, it is enough to know that practical forward converters require a reset mechanism, such as a reset winding or another reset arrangement. The exact reset design is a later topic.

#### Ideal gain relation

For the ideal forward converter operating in CCM, the familiar beginner-level relation is

$$\boxed{\frac{V_o}{V_{in}} = D\frac{N_s}{N_p}} \quad \text{(15.7)}$$

This looks very much like the buck relation, except that the transformer turns ratio multiplies the result.

We can motivate it by writing the output-inductor voltage in the two intervals.

During the ON interval, the secondary-side applied voltage is approximately

$$V_{sec} = \frac{N_s}{N_p}V_{in}. \quad \text{(15.8)}$$

So the output inductor sees

$$v_{L,\text{ON}} = \frac{N_s}{N_p}V_{in} - V_o. \quad \text{(15.9)}$$

During the OFF interval, the freewheeling path holds the inductor current and the inductor voltage becomes approximately

$$v_{L,\text{OFF}} = -V_o. \quad \text{(15.10)}$$

Applying volt-second balance to the output inductor,

$$D\left(\frac{N_s}{N_p}V_{in} - V_o\right) + (1-D)(-V_o) = 0. \quad \text{(15.11)}$$

Expand the expression:

$$D\frac{N_s}{N_p}V_{in} - DV_o - V_o + DV_o = 0.$$

So

$$D\frac{N_s}{N_p}V_{in} - V_o = 0,$$

and therefore

$$\boxed{V_o = D\frac{N_s}{N_p}V_{in}} \quad \text{(15.12)}$$

This is the ideal forward-converter gain relation at the level we need in this chapter.

#### A numerical example

Suppose an isolated forward converter must produce $12 \text{ V}$ from a $48 \text{ V}$ input, and let the transformer turns ratio be

$$\frac{N_s}{N_p} = \frac{1}{2}.$$

Using Equation (15.12),

$$12 = D \times \frac{1}{2} \times 48.$$

Since $\dfrac{1}{2} \times 48 = 24$, we get

$$12 = 24D,$$

so

$$D = \frac{12}{24} = 0.5.$$

This is a neat example because it also reminds us that the turns ratio and duty cycle share the conversion job together.

#### Why choose a forward converter instead of flyback

Now we can ask the practical question. If the flyback converter is simpler, why use a forward converter?

The answer is that the forward converter is often more attractive when load current and power level increase. Because energy is transferred to the output during the ON interval rather than being stored and released in the same magnetic element in flyback style, the forward topology often handles higher output power and higher output current more gracefully. Analog Devices notes that forward converters tend to be better suited to higher current and higher power levels, while flybacks tend to win on simplicity and lower component count [Analog Devices, "Isolated Switch-Mode Power Supplies: How to Choose a Forward vs. a Flyback Converter", 2024].

The tradeoff is also visible in hardware count. The forward converter usually needs more parts, including an output inductor and a transformer reset arrangement. So we gain capability, but we also accept more complexity.

#### Where forward converters appear

Forward converters are common in isolated power supplies where we want better current capability than a simple flyback but do not yet need the highest-power bridge topologies. They are often seen in industrial power modules, telecom-style supplies, charger subassemblies, and auxiliary converter stages where isolation and tighter output behavior are desirable [Analog Devices, "Isolated Switch-Mode Power Supplies: How to Choose a Forward vs. a Flyback Converter", 2024], [TI, UCC28250 product page].

#### Common misconceptions

A common mistake is to treat the forward converter as just a flyback with an extra output inductor. Its energy-transfer timing is different, the output inductor is central rather than optional, and the transformer still needs proper reset treatment. Renewable-energy relevance: forward converters are attractive for isolated support supplies that need more output-current capability than a simple flyback can comfortably provide, including charger auxiliaries, industrial battery interfaces, and support rails in larger power-conversion cabinets [TI, UCC28250 product page], [Mohan, Undeland, Robbins, *Power Electronics: Converters, Applications, and Design*, 3e].

### 4.3.4 Push-Pull, Half-Bridge and Full-Bridge isolated converters - topology-level comparison

#### Why these topologies are grouped together

So far, we have studied two **single-ended** isolated converters: flyback and forward. In both cases, one primary-side switch action mainly excites the transformer in one direction during the active interval, and the converter relies on the rest of the cycle for reset or discharge behavior.

The next family is different. **Push-pull**, **half-bridge**, and **full-bridge** converters are often introduced together because they are all **double-ended** topologies. That means the transformer primary is driven in alternating polarities over the switching cycle, which tends to use the magnetic core more effectively and makes these topologies suitable for higher power than the simplest isolated single-ended circuits [MIT OCW, 6.334 *Power Electronics*, ch7 notes], [TI, UCC28250 product page].

We will stay at topology-comparison level here, just as the syllabus requests.

#### Push-pull converter

In the **push-pull converter**, two switches alternately drive a center-tapped primary or an equivalent arrangement. During one interval, one half of the primary is energized. During the next interval, the other half is energized with opposite polarity.

The big intuitive advantage is that the transformer can be driven in both directions, which improves core utilization. Another practical attraction is that the primary sees the full input voltage on the active half-winding, which can be useful at comparatively lower DC input voltages.

But there is a caution. Push-pull converters can be sensitive to timing imbalance and transformer asymmetry. If one half-cycle is not well balanced with the other, flux can drift toward saturation. Also, switch voltage stress can be significant in practical designs, especially when leakage spikes are added.

So the push-pull converter is appealing, but it demands respect in implementation.

#### Half-bridge converter

In the **half-bridge converter**, two switches drive the transformer primary from a split bus or midpoint arrangement. The transformer primary typically sees approximately $+\dfrac{V_{in}}{2}$ and $-\dfrac{V_{in}}{2}$ in alternating intervals.

A helpful beginner picture is this: the half-bridge gives us double-ended transformer excitation, but with fewer primary switches than a full bridge. It often provides a good compromise among component count, device stress, transformer utilization, and power capability. TI's LM5036 product page identifies half-bridge, full-bridge, and push-pull as supported topologies for a controller aimed at high-density DC-DC power converters [TI, LM5036 product page].

Because only half the bus is applied to the transformer primary during each active interval, the transformer turns ratio and current levels must be chosen accordingly. That is neither good nor bad by itself. It is simply part of the topology tradeoff.

#### Full-bridge converter

In the **full-bridge converter**, four switches drive the transformer primary so that the full input voltage can be applied across the primary in both polarities: $+V_{in}$ in one interval and $-V_{in}$ in another.

This gives very strong transformer utilization and makes the full-bridge topology a common choice for higher-power isolated conversion. The price is obvious: more switches, more gate-drive complexity, more careful control of dead time and switching transitions, and generally more design effort than in flyback or forward converters.

TI's **PMP8877** reference design is a good example of where a full bridge begins to make sense. TI describes it as an isolated DC/DC power module using a hard-switching full-bridge topology to deliver about $180 \text{ W}$ nominally, with table values showing $12 \text{ V}$ output, up to $18 \text{ A}$, and about $216 \text{ W}$ maximum output from a $36 \text{ V}$ to $75 \text{ V}$ input range [TI, PMP8877 reference design]. Even without studying the detailed waveforms, we can see the message: once isolated power levels rise substantially, designers often move beyond flyback and toward bridge topologies.

#### A comparison table

Table 15.1 helps organize the overview.

Table 15.1: Topology-level comparison of isolated converter families in this chapter

| Topology | Beginner mental model | Main energy-transfer idea | Relative complexity | Typical role in a system |
| --- | --- | --- | --- | --- |
| Flyback | Isolated buck-boost | Store during ON, deliver during OFF | Low | Low-power or auxiliary isolated supplies |
| Forward | Isolated buck | Transfer during ON, freewheel during OFF | Moderate | Isolated supplies with better current capability |
| Push-pull | Double-ended transformer drive with two switches | Alternate primary excitation using two halves | Moderate to high | Medium-power isolated conversion, often lower-voltage input contexts |
| Half-bridge | Double-ended bridge using two switches and split bus | Alternate $\pm V_{in}/2$ across primary | Moderate to high | Medium to higher-power isolated supplies |
| Full-bridge | Double-ended bridge using four switches | Alternate $\pm V_{in}$ across primary | High | Higher-power isolated conversion |

#### Another practical comparison

It is also useful to compare what usually drives the topology choice.

Table 15.2: Practical selection intuition for isolated DC-DC topologies

| If your priority is... | A topology often considered first | Why |
| --- | --- | --- |
| Minimum parts and simple isolated auxiliary power | Flyback | Simple structure and good flexibility |
| Better output-current capability with isolation | Forward | More direct energy transfer to the output |
| Better transformer utilization at moderate power | Push-pull or half-bridge | Double-ended operation |
| High isolated power with strong transformer utilization | Full-bridge | Full bus applied across primary in alternating directions |

These are not rigid rules. They are early-selection instincts. Real design choices depend on input voltage, output power, efficiency target, EMI limits, cost, control method, magnetic design, and safety requirements.

**Image prompt for Figure 15.3:** Create a clean textbook-style comparison figure for isolated converter topologies. Show simplified labeled circuit blocks for push-pull, half-bridge, and full-bridge isolated converters side by side. For each topology, include a small accompanying primary-voltage waveform sketch showing the transformer primary excitation polarity over time. Clearly label the number of active switches, whether the transformer sees approximately $\pm V_{in}$ or $\pm V_{in}/2$, and note that these are topology-level conceptual views, not complete detailed schematics. Use monochrome engineering style with consistent layout and annotations.

#### Common misconceptions

Bridge converters are not just "bigger flybacks." Their primary excitation and magnetic use are fundamentally different. More switches also do not automatically guarantee higher efficiency; the outcome depends on the whole design. Renewable-energy relevance: these bridge-based isolated converters matter when renewable-energy systems scale upward in power or voltage, especially in higher-power battery systems, charger hardware, and larger auxiliary stages inside solar and EV equipment [TI, UCC28250 product page], [TI, LM5036 product page], [TI, PMP8877 reference design].

## Worked interpretation exercise

### Reading a real isolated flyback reference design

Let us now read a real artifact and interpret it the way a developing power-electronics engineer would. We will use TI's **PMP22288** reference design page, titled *15-W flyback reference design for automotive inverter power* [TI, PMP22288 reference design].

TI lists the following key items on the page:

- topology: **Flyback - DCM**
- input range: $40 \text{ V}$ to $550 \text{ V}$
- output: isolated $15 \text{ V}$, up to $1 \text{ A}$
- output power: $15 \text{ W}$
- peak efficiency: $86\%$
- application note: automotive inverter power [TI, PMP22288 reference design]

Now let us interpret what those numbers tell us.

First, the **power level** is only $15 \text{ W}$. That immediately suggests we are not looking at the main traction-energy path of an EV or the main power stage of a large renewable inverter. We are looking at an **auxiliary supply**. That is exactly where flyback converters are often strong: modest isolated power with reasonable simplicity.

Second, the **input range** is extremely wide: from $40 \text{ V}$ all the way to $550 \text{ V}$. This tells us the supply is expected to survive and regulate in a harsh high-voltage environment. In an inverter-related system, such a range is consistent with widely varying DC-bus conditions, startup conditions, or operating margins around a high-voltage battery or DC link.

Third, the output is an **isolated $15 \text{ V}$ rail**. That number is very suggestive. A $15 \text{ V}$ isolated rail is a common kind of auxiliary voltage for gate-drive support, control electronics, or bias supplies around high-voltage switching stages. The fact that it is isolated matters just as much as the fact that it is 15 V.

Fourth, the topology is explicitly listed as **flyback - DCM**. That is useful because it tells us this is a real example of the topology we just studied, and it also reminds us that practical flybacks are often operated in discontinuous conduction mode at lower power levels for control and magnetic-design reasons. The syllabus does not require DCM analysis here, so we do not go deeper, but the artifact helps us see that practical designs do make such operating-mode choices.

Fifth, TI lists **86% peak efficiency**. That is a good reminder that auxiliary isolated supplies are judged differently from the main conversion stage. If a 15 W bias supply is compact, isolated, reliable, and efficient enough for its role, it may be an excellent design even though it is not chasing the very highest possible efficiency that a large main power stage might demand.

The broader lesson from this exercise is important. When you read an isolated-converter artifact, ask these questions first:

- Is this a main power stage or an auxiliary supply?
- Why is isolation needed here?
- What does the input range say about the electrical environment?
- What does the power level suggest about topology choice?
- Does the chosen topology match what we learned about that power range and role?

For PMP22288, the answers line up cleanly. It is a wide-input, isolated, moderate-power auxiliary supply in a harsh automotive inverter environment, and a flyback topology is a very sensible choice for that job [TI, PMP22288 reference design].

## How this matters in renewable-energy systems

Isolated DC-DC converters appear all through renewable-energy and electrified systems, even when they are not always the most visible block in the product brochure.

In **solar PV inverters**, isolated auxiliary supplies power control boards, sensing circuits, communication hardware, and gate drivers. In **battery chargers**, isolation supports safety, grounding strategy, and separation between higher-voltage input and battery-side electronics. In **battery energy storage systems**, isolated low-power rails support monitoring, balancing, and supervisory electronics. In **EV power stages**, isolated converters are crucial for traction-inverter gate-drive supplies, current and voltage measurement domains, and high-voltage to low-voltage control support [TI, PMP22288 reference design], [TI, TIDA-01513 reference design].

The topology choice depends strongly on role and power level. A **flyback** converter may be ideal for a 10 W to 20 W isolated bias supply. A **forward** converter may be more attractive when output-current demand rises and better output behavior is needed. A **half-bridge** or **full-bridge** converter becomes increasingly attractive when isolated power climbs much higher and magnetic utilization becomes more important. TI's PMP8877 full-bridge module is a useful example of that progression toward higher power [TI, PMP8877 reference design].

The key system-level lesson is this: renewable-energy hardware is not only about converting kilowatts in the main path. It is also about safely powering all the smaller circuits that let the main path operate, communicate, sense, and protect itself. Isolated DC-DC converters are one of the quiet technologies that make those larger systems practical.

## Chapter summary

- **Galvanic isolation** means there is no direct conductive DC path between input and output; power still crosses the barrier through coupling, often with a transformer.
- An isolated DC-DC converter works by switching DC into a high-frequency waveform, transferring energy through a transformer, and then rectifying and filtering it back into DC.
- The ideal transformer turns-ratio relation is $\dfrac{V_s}{V_p} = \dfrac{N_s}{N_p}$.
- A transformer cannot pass steady DC directly; isolated DC-DC conversion therefore requires switching action.
- A **flyback converter** stores energy during the ON interval and delivers it to the output during the OFF interval.
- For an ideal CCM flyback converter, $\dfrac{V_o}{V_{in}} = \dfrac{N_s}{N_p}\dfrac{D}{1-D}$.
- A **forward converter** transfers energy to the output during the ON interval and uses an output inductor freewheeling path during the OFF interval.
- For an ideal CCM forward converter, $\dfrac{V_o}{V_{in}} = D\dfrac{N_s}{N_p}$.
- Flyback converters are attractive for isolated auxiliary supplies because of simplicity and low part count.
- Forward converters are often chosen when more output-current capability is needed than a simple flyback comfortably offers.
- **Push-pull**, **half-bridge**, and **full-bridge** converters are double-ended isolated topologies that use transformer excitation in alternating polarities.
- Half-bridge and full-bridge topologies are especially important as isolated power level increases.
- In renewable-energy and EV systems, isolated converters often power gate drivers, measurement domains, communication hardware, control boards, and charger auxiliaries.

## Further reading

1. Robert W. Erickson and Dragan Maksimovic, *Fundamentals of Power Electronics*, 2nd ed.  
   A strong foundational text for understanding flyback, forward, and bridge converters from first principles.

2. Ned Mohan, Tore M. Undeland, and William P. Robbins, *Power Electronics: Converters, Applications, and Design*, 3rd ed.  
   A classic text that connects topology operation to practical application choices very well.

3. MIT OpenCourseWare, 6.334 *Power Electronics*, ch7 lecture notes.  
   Useful notes specifically covering isolated DC/DC converters, flyback converters, single-ended forward converters, and double-ended converters.

4. Analog Devices, "Isolated Switch-Mode Power Supplies: How to Choose a Forward vs. a Flyback Converter" (2024), and "Galvanic Isolation" glossary entry.  
   Good modern, readable references for the practical differences between isolation, flyback, and forward approaches.

5. Texas Instruments, PMP22288 reference design, PMP8877 reference design, and UCC28250 / LM5036 product pages.  
   These are excellent real-world examples showing how isolated flyback, half-bridge, and full-bridge ideas appear in commercial and reference hardware.
