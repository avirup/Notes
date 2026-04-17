# Chapter 2.3: Overvoltage and Overcurrent Protection

## Chapter opening

In the previous two chapters, we learned how to command a power semiconductor and how to soften the transients that appear during switching. Those were essential steps, but they still do not answer a harder question: what happens when something goes wrong?

Power-electronic systems do not live in ideal conditions. A mains line can see a surge. A battery cable can be connected poorly and then reconnected abruptly. A transformer leakage path can create an unexpected spike. A motor can stall. A diode can recover badly. Two switches in one leg can momentarily conduct together. A controller can fail. A regulator can drift high. In each of these cases, the converter may see either too much voltage, too much current, or both.

That is why this chapter matters. **Protection** in power electronics is not an optional extra added after the converter is designed. It is part of the converter design. We need circuits and devices that act when normal control is no longer enough. Some protective elements absorb a surge. Some clamp it. Some deliberately short the supply so that a fuse opens. Some measure current and reduce duty ratio electronically. Some sit inside a gate driver and watch for the collector-emitter voltage of an IGBT to rise abnormally during a fault. All of these belong to the same engineering goal: keep the power stage, the load, and the user safe [Rashid, *Power Electronics: Circuits, Devices and Applications, 4e*], [Mohan, Undeland, Robbins, *Power Electronics*].

In this chapter we will study two broad protection families from the syllabus. First, we will study **overvoltage protection** using the **MOV**, the **TVS diode**, and the **crowbar circuit**. Then we will study **overcurrent protection** using **fast-acting (HRC) fuses**, **electronic current limiting**, and **desaturation detection** at concept level. Along the way, we will keep asking the same practical question: what exactly is the abnormal event, and what kind of protective response matches it?

These ideas connect strongly to renewable-energy hardware. MOVs appear at AC inputs and surge-exposed terminals. TVS diodes protect low-voltage buses and control electronics. Crowbar circuits protect sensitive DC supplies. Semiconductor fuses protect converter branches. Electronic current limiting shapes charger and converter behavior under overload. DESAT protection is common in modern IGBT and SiC gate-driver systems. This chapter therefore sits at an important point in the book: it moves us from "how converters switch" toward "how converters survive."

## Prerequisites check

- You should remember from Chapter 2.1 that a gate driver does more than reproduce logic; it also supports safe switching and fault response.
- You should remember from Chapter 2.2 that snubbers control switching transients, but they are not the same thing as complete fault protection.
- You should be comfortable with RMS and peak value relation for a sine wave, even if you still need a short refresher.
- You should remember that inductors resist sudden current change and that stored magnetic energy is $\tfrac{1}{2}LI^2$.
- You should know the basic meaning of semiconductor ON-state voltage, such as $V_{CE(\text{sat})}$ for an IGBT and $V_{DS}$ for a MOSFET.

If the distinction between normal switching transient and true fault condition feels unclear, a short review of Chapter 2.2 will help before you go deeper into this chapter.

## Core content

### 2.3.1 Overvoltage protection: MOV, TVS diodes, crowbar circuits

#### Why overvoltage protection is needed

Let us begin with a simple example.

Suppose a rooftop PV inverter is powered from a 230 V, 50 Hz single-phase utility line on one side and contains low-voltage control electronics on another board. The power stage may tolerate several hundred volts on its DC bus, but the control board may only tolerate 5 V, 12 V, or 15 V rails. Now imagine one of three disturbances:

- a surge arrives from the AC line during a nearby lightning event,
- a switching node rings above its expected value because of parasitic inductance,
- a DC regulator fails and its output rises far above the safe voltage for the controller board.

All three are "too much voltage," but they are not the same problem.

That is the first protection lesson of this chapter. **Overvoltage** is not one single event. It may be:

- a very short high-energy surge from outside the converter,
- a repetitive internal spike caused by switching,
- a sustained DC overvoltage caused by control or regulator failure.

Different protective devices respond well to different kinds of abnormal voltage. A beginner often asks, "Which is better: MOV, TVS, or crowbar?" That is not yet the right question. The right question is: "What kind of abnormal voltage do we need to survive?"

Before comparing protective devices, let us refresh one very basic relation for AC systems:

$$\boxed{V_{pk} = \sqrt{2}\,V_{rms}} \quad \text{(8.1)}$$

where $V_{pk}$ is the sinusoidal peak voltage and $V_{rms}$ is the RMS value.

For a 230 V, 50 Hz mains supply,

$$V_{pk} = \sqrt{2}\times 230 \approx 325 \text{ V}.$$

This number matters because any protector connected across the line must tolerate the normal mains voltage first and only act when an abnormal condition appears. If we misunderstand the normal peak value, we may accidentally choose a protector that conducts during ordinary operation instead of only during a surge.

Two common misconceptions should be corrected early.

The first misconception is that overvoltage protection always means "keeping the voltage exactly constant." In reality, many protectors only act during abnormal events and still allow the voltage to rise to some clamped value above nominal.

The second misconception is that one protective device can solve all overvoltage problems in all locations. In practice, surge absorbers, fast clamps, and crowbars are complementary tools, not universal substitutes [Bourns, *Tips on Selecting the Right MOV Surge Suppressor*], [Littelfuse 5KP Series], [onsemi AN004E/D].

*Renewable-energy relevance.* In solar and wind hardware, overvoltage events come from both outside and inside the converter. Grid-side equipment sees line surges. DC-DC stages create switching spikes. Battery systems can generate inductive transients during connection and disconnection. Protection therefore has to be layered.

#### The MOV

A **metal-oxide varistor**, or **MOV**, is one of the most common surge-protection devices at the input of power equipment.

The easiest way to understand an MOV is to think of it as a normally quiet device that becomes much more conductive when the voltage rises high enough. At normal voltage, the MOV draws only a very small current. During a surge, its resistance drops sharply and it diverts current away from the protected equipment. Bourns describes this behavior clearly: the MOV has very high impedance below its threshold region, then conducts increasingly as the voltage rises, but the clamp is not perfectly constant; the clamping voltage also rises with current [Bourns, *Tips on Selecting the Right MOV Surge Suppressor*].

This last sentence is important. A beginner may imagine an MOV as an ideal ceiling that says, "No voltage may go above this value." A real MOV does not behave that way. It is a strongly nonlinear resistor. The more surge current it carries, the more its clamping voltage rises.

The key terms used with an MOV are:

- **maximum continuous operating voltage (MCOV)**: the highest continuous AC or DC voltage the MOV should withstand in normal operation,
- **varistor voltage**: a test-condition voltage, often specified at a current such as 1 mA DC,
- **clamping voltage**: the voltage developed across the MOV at a specified surge current,
- **surge current rating**: the magnitude of surge current the MOV can survive for a specified waveform.

Bourns notes that MOV surge ratings are commonly specified on an **8/20 µs** current waveform, meaning a standardized current pulse that rises and decays very quickly [Bourns, *Tips on Selecting the Right MOV Surge Suppressor*]. That tells us immediately that the MOV is intended for surge events, not for indefinitely carrying abnormal mains voltage.

##### Choosing the MOV from the normal voltage first

Suppose we want to protect the AC input of a 230 V, 50 Hz UPS or PV inverter. The line has a normal RMS value of 230 V and a normal peak of about 325 V from Equation (8.1). The MOV must remain essentially inactive during ordinary operation, including normal tolerance on the line. So the first selection step is not surge energy. The first selection step is choosing a continuous voltage rating that safely exceeds the actual steady operating condition [Bourns, *Tips on Selecting the Right MOV Surge Suppressor*].

This is a useful beginner habit:

1. Start with the normal operating voltage.
2. Add realistic tolerance and operating margin.
3. Only then check clamp level and surge capability.

If we skip step 1, the MOV may run hot even when the system is healthy.

##### What the MOV does well and what it does not

The MOV is attractive because it is simple, inexpensive, bidirectional in common AC use, and able to absorb substantial surge current. That is why MOVs are so common at mains inputs.

But the MOV has two major limitations.

First, it degrades with repeated surge stress. Protection is not free. Each severe hit ages the device to some extent [Bourns, *Tips on Selecting the Right MOV Surge Suppressor*].

Second, the MOV is not meant to endure a long-lasting overvoltage. Bourns explicitly warns that if the abnormal overvoltage lasts too long, the MOV heats up and may enter thermal runaway, which is why a fuse, thermal disconnect, or similar series protection is recommended [Bourns, *Tips on Selecting the Right MOV Surge Suppressor*].

This is a crucial conceptual distinction:

- An MOV is very good for short surges.
- An MOV is not a good answer to a sustained regulator failure or a prolonged overvoltage on its own.

**Image prompt for Figure 8.1:** Create a clean textbook-style illustration of an MOV connected across a 230 V AC equipment input. Show normal sinusoidal mains where MOV current is nearly zero, and a second waveform panel showing a short surge on the mains with the MOV conducting large current and clamping the voltage. Label line, neutral, MOV, normal leakage region, surge current path, clamping voltage, and note that the clamp voltage rises with current. Use monochrome engineering style with clear axes and units.

##### A practical AC-input example

Imagine a small inverter-powered water pump controller used with rooftop solar backup. The controller operates from the utility when available and contains an AC-DC front end. A surge enters from the mains during a storm. The front-end bridge rectifier and bulk capacitor do not want to see the full surge amplitude. An MOV placed across the line can divert much of the surge current and reduce the stress on downstream components. But if the mains remains abnormally high for a long time because of a wiring fault or regulator failure elsewhere, the MOV alone is not enough. It must work together with upstream disconnection.

That simple example captures the proper mindset: the MOV is a surge absorber, not a universal overvoltage cure.

*Renewable-energy relevance.* MOVs are common at the AC input of PV inverters, battery chargers, and UPS equipment because utility-connected hardware is exposed to line disturbances and surge energy that low-voltage electronics cannot tolerate directly.

#### The TVS diode

A **transient voltage suppressor diode**, or **TVS diode**, is another overvoltage-protection device, but its personality is different from that of an MOV.

The TVS diode is usually used where we want a faster, more sharply defined clamp on a lower-voltage line or sensitive node. Littelfuse describes TVS diodes as devices intended to protect sensitive electronics against transient voltage events and highlights fast response and strong clamping capability [Littelfuse 5KP Series], [Littelfuse 3.0SMC Series].

At beginner level, the cleanest intuition is this:

- the MOV is often chosen for higher-energy surge handling, especially at AC or DC inputs,
- the TVS diode is often chosen for faster, more defined clamping of shorter transients on lower-voltage buses or interfaces.

That is a useful first picture, although real designs can be more nuanced.

The key TVS terms are:

- **reverse standoff voltage**, often written $V_R$ or $V_{RWM}$: the maximum normal working voltage that should not trigger significant conduction,
- **breakdown voltage**, $V_{BR}$: the region where avalanche conduction begins under the specified test current,
- **clamping voltage**, $V_C$: the voltage across the TVS at a specified pulse current,
- **peak pulse current**, $I_{PP}$: the surge current used in the clamping specification,
- **peak pulse power**: the rated pulse power under a specified surge waveform.

For a pulse event, a useful first estimate is

$$\boxed{P_{\text{pulse,approx}} \approx V_C I_{PP}} \quad \text{(8.2)}$$

where $P_{\text{pulse,approx}}$ is the approximate pulse power during the clamped event, $V_C$ is the clamping voltage, and $I_{PP}$ is the peak pulse current. This is an approximation, not a full energy calculation, because real surge waveforms vary with time. But it explains why both voltage and current matter in a TVS event.

##### Reading the TVS ratings correctly

Suppose a low-voltage controller board in a battery-energy-storage system uses a 48 V nominal DC bus for relays, fans, and auxiliary electronics. The protective designer wants a TVS diode across that bus.

The first temptation is to choose a TVS whose breakdown voltage is "about 48 V." That is often too simplistic. The important first question is the highest voltage the bus sees during normal operation, including charging, regulation tolerance, and possible ripple. The TVS reverse standoff voltage must be above that normal condition. Only then do we check the breakdown and clamping values [Littelfuse 5KP Series].

Here is the basic logic:

1. The normal bus voltage must stay below the reverse standoff rating.
2. The abnormal transient must rise into the avalanche region.
3. The resulting clamp voltage must stay below what the protected electronics can survive.

This is why TVS selection is often more exact than beginners expect. If the standoff voltage is too low, the diode leaks excessively or conducts during normal operation. If the clamping voltage is too high, the protected circuit still sees too much stress.

##### Why TVS diodes are so useful

TVS diodes are especially useful because they respond very quickly and are widely available for many voltage classes. Littelfuse highlights their use for protection against transient events such as lightning-induced disturbances, ESD, EFT, and inductive switching transients [Littelfuse 3.0SMC Series], [Littelfuse SLD6S Series].

They are common on:

- low-voltage DC buses,
- gate-driver supply rails,
- communication and sensing lines,
- control inputs and outputs,
- automotive and battery-connected electronics,
- local protection points near sensitive ICs.

That last point matters in power electronics. The TVS diode is often not the only protective element. It is often the local fast clamp placed close to the vulnerable node.

##### What the TVS diode cannot replace

The TVS diode is not a magic high-energy absorber for every power fault. Compared with an MOV used at a mains input, the TVS diode is often protecting a more local node and usually handles less total surge energy. Littelfuse also notes a typical failure mode of short circuit when a TVS is overstressed beyond its specified limits [Littelfuse 3.0SMC Series].

That fact is not a weakness; it is a design reality. If the expected surge energy is too large or the event is too long, a larger protector or a different protection architecture is needed.

**Image prompt for Figure 8.2:** Create a textbook-style voltage-current concept figure for a unidirectional TVS diode. Show a horizontal axis for voltage and vertical axis for current. Mark reverse standoff region with very small current, breakdown region, and clamping region at specified pulse current. Add labels for $V_{RWM}$, $V_{BR}$, $V_C$, and $I_{PP}$. Include a side inset showing a TVS connected across a 48 V DC auxiliary bus feeding a controller. Use monochrome engineering style with clear labels.

##### MOV versus TVS in plain language

At this point, it helps to pause and compare them directly.

Table 8.1: MOV, TVS diode, and crowbar compared at beginner level

| Protection method | Main physical action | Strongest use case | Main limitation |
|---|---|---|---|
| MOV | Nonlinear resistance diverts surge current | Input surge suppression, especially at AC or higher-energy entry points | Degrades with repeated surges; not suited to sustained overvoltage by itself |
| TVS diode | Avalanche clamp limits transient voltage quickly | Fast local protection of sensitive low-voltage buses and nodes | Usually lower energy capability than a mains MOV; overstress may short the device |
| Crowbar circuit | Deliberately forces a low-impedance fault path when threshold is exceeded | Sustained overvoltage protection of sensitive DC supplies | Requires current limiting or fuse action elsewhere; trips hard rather than gently |

The important beginner insight is not that one row is "best." The important insight is that the three rows represent three different protective strategies.

*Renewable-energy relevance.* TVS diodes are very common in solar, wind, and battery systems on sensor inputs, CAN or communication interfaces, isolated-driver supplies, 12 V or 24 V auxiliary rails, and contactor or relay-associated control nodes.

#### Crowbar circuits

The **crowbar circuit** is conceptually different from both the MOV and the TVS diode.

An MOV or TVS tries to keep the overvoltage under some clamped level while still remaining a protection element in parallel with the circuit. A crowbar circuit acts more dramatically. When the voltage exceeds a defined threshold, the crowbar turns on a device such as an SCR and effectively places a short circuit across the supply or output. This forces the upstream source into current limit or causes a fuse or breaker to open [onsemi AN004E/D], [onsemi MC3423 Datasheet].

The name is vivid and helpful. It is as if a metal crowbar were thrown across the supply rails. That is not elegant regulation. It is emergency action.

##### Why a hard short can be the safest choice

At first, beginners sometimes dislike the crowbar idea because it sounds violent. But consider a 5 V processor board or gate-driver supply. If a regulator fails and the rail rises to 12 V or 15 V, the downstream electronics may be destroyed very quickly. In that case, a hard trip that sacrifices a fuse may be far better than allowing the overvoltage to continue.

onsemi describes crowbar overvoltage protection in exactly this spirit: the sensing circuit detects the overvoltage and quickly crowbars the supply, forcing current limiting or opening a fuse or breaker [onsemi AN004E/D], [onsemi MC3423 Datasheet].

So a crowbar is best understood as a **latching protection response** to a sustained or dangerous overvoltage.

##### Threshold setting in a simple sensing scheme

A very common way to define the trip point is to compare a divided-down supply voltage with a reference. In a simple divider-based sense circuit, the trip voltage can be expressed as

$$\boxed{V_{\text{trip}} = V_{\text{ref}}\left(1+\frac{R_1}{R_2}\right)} \quad \text{(8.3)}$$

where $V_{\text{trip}}$ is the supply voltage at which the crowbar should trigger, $V_{\text{ref}}$ is the sensing reference, and $R_1$ and $R_2$ are the divider resistors.

Suppose we want a 5 V auxiliary rail to crowbar at about $6.25 \text{ V}$, and suppose the reference is $2.5 \text{ V}$. Then

$$6.25 = 2.5\left(1+\frac{R_1}{R_2}\right).$$

So

$$\frac{R_1}{R_2} = \frac{6.25}{2.5}-1 = 1.5.$$

If we choose $R_2 = 10 \text{ k}\Omega$, then a nearby practical choice is $R_1 = 15 \text{ k}\Omega$.

This is a simple example, but it teaches an important point: the crowbar threshold is a deliberate design choice. It is not guessed.

##### Practical concerns in crowbar protection

Crowbar circuits raise three practical questions.

First, how do we avoid nuisance tripping on very short harmless spikes? onsemi notes that crowbar sensing can be designed with a minimum overvoltage duration before tripping, which improves noise immunity [onsemi MC3423 Datasheet].

Second, what device carries the crowbar current? Often this is an SCR. Its current, surge, and $di/dt$ capability must match the source and fuse behavior.

Third, what actually clears the fault? The crowbar itself does not make energy disappear. It relies on the upstream system to do one of the following:

- enter current limit,
- blow a fuse,
- trip a breaker,
- shut down by control action.

That is why a crowbar must be designed as part of a protection chain, not as an isolated symbol on a schematic.

**Image prompt for Figure 8.3:** Create a clean textbook-style schematic illustration of a DC supply protected by an SCR crowbar circuit. Show the regulated supply output feeding a sensitive load, a sense network and reference that trigger an SCR when output voltage exceeds threshold, and an upstream fuse or current-limited source. Add a waveform panel showing output voltage rising abnormally, crowbar firing, voltage collapsing, and source current increasing until protection clears. Label $V_{\text{trip}}$, fuse, SCR, sense divider, and load. Use monochrome engineering style.

##### A realistic low-voltage example

Imagine a 15 V isolated gate-driver supply inside a motor-drive inverter. If the isolated DC-DC converter fails and the output rises to 24 V, the gate-driver IC and the power-device gate oxide may both be in danger. An MOV is not the natural first answer here, because the abnormal event may be a sustained regulator failure rather than a short surge. A TVS could help with brief spikes, but if the source can continue delivering current, the TVS may overheat. A crowbar circuit is much more suitable because it detects the abnormal DC overvoltage and forces the upstream source into a protective response.

This example shows why the crowbar belongs in the same chapter as MOVs and TVS diodes while still being conceptually different from them.

##### Common misconceptions in overvoltage protection

Three misconceptions are especially common at this stage.

The first is that a higher clamping voltage rating is always safer because it avoids nuisance action. That is not true if the protected circuitry cannot survive the higher clamp.

The second is that an MOV or TVS always protects indefinitely once installed. Real protectors have energy limits, thermal limits, and aging behavior [Bourns, *Tips on Selecting the Right MOV Surge Suppressor*], [Littelfuse 3.0SMC Series].

The third is that a crowbar "regulates" the output. It does not. It is a fault response, not a normal control mechanism.

*Renewable-energy relevance.* Crowbar protection appears in low-voltage converter auxiliaries, battery-management support rails, gate-driver supplies, and instrumentation supplies where a sustained overvoltage could destroy expensive digital electronics long before a human operator notices the problem.

### 2.3.2 Overcurrent protection: fast-acting (HRC) fuses, electronic current limiting, desaturation detection (concept)

#### Why overcurrent protection is needed

If overvoltage threatens insulation and semiconductor blocking capability, **overcurrent** threatens something just as serious: heat and destruction due to excessive conduction.

Again, let us begin with a physical picture.

Suppose an IGBT leg in a three-phase inverter is operating normally from a rectified 415 V three-phase supply. Suddenly a motor cable fault occurs, or two switches in one leg overlap because of a control failure. The current does not politely rise to a slightly larger steady value. It may jump toward a very large fault current limited only by the source, the DC-link impedance, and the device itself.

What makes overcurrent dangerous is not only the magnitude of current, but also the time for which that current persists. The useful energy-related measure is the **Joule integral**:

$$\boxed{I^2 t = \int i^2(t)\,dt} \quad \text{(8.4)}$$

where $I^2 t$ is the current-squared time integral and $i(t)$ is the fault current waveform.

This relation is important because heating effect scales with current squared. A moderate overload for a long time and a severe short circuit for a very short time can both be destructive, but they stress the system differently. Fuses, semiconductor short-circuit ratings, and coordination discussions often use $I^2 t$ because it directly reflects let-through thermal stress [Mersen HSJ Family].

Consider a simple example. If a fault current of $100 \text{ A}$ flows approximately constantly for $1 \text{ ms}$, then

$$I^2 t \approx 100^2 \times 0.001 = 10 \text{ A}^2\text{s}.$$

If the current were instead $300 \text{ A}$ for the same $1 \text{ ms}$, then

$$I^2 t \approx 300^2 \times 0.001 = 90 \text{ A}^2\text{s}.$$

So trip time matters enormously. Three times the current creates nine times the $I^2 t$ for the same duration.

This is why overcurrent protection in power electronics is usually layered:

- one layer for catastrophic short circuit,
- one layer for controlled overload limiting,
- one layer for local device protection,
- sometimes another layer for wiring or branch-circuit protection.

At beginner level, this chapter focuses on three foundational examples of those layers.

*Renewable-energy relevance.* Overcurrent protection is central in PV inverters, wind converters, EV auxiliary converters, UPS systems, and battery chargers because these systems are expected to survive abnormal loads without turning a device fault into a system fire or bus explosion.

#### Fast-acting (HRC) fuses

A **fuse** is the oldest and still one of the most important protective devices in power electronics.

The basic principle is familiar: if excessive current flows long enough, a calibrated element melts and opens the circuit. But not all fuses are the same. The syllabus specifically mentions **fast-acting (HRC) fuses**. The phrase **HRC** means **high rupturing capacity**, which tells us the fuse is designed to interrupt very large fault current safely without exploding externally. In power-electronic service, we are often especially interested in semiconductor-protecting fuses with low let-through energy.

Mersen describes its HSJ high-speed series as combining branch-circuit protection with very low $I^2 t$ for protection of power semiconductors such as diodes, SCRs, GTOs, and solid-state relays [Mersen HSJ Family]. That statement contains the key idea we need: a semiconductor-protecting fuse is valued not only because it opens eventually, but because it limits the energy allowed through during the fault.

##### Why "fast" matters for semiconductors

Power semiconductors can be damaged long before a slow general-purpose fuse reacts. This is especially true in short-circuit conditions. A fast semiconductor fuse is therefore chosen so that its let-through energy is compatible with the survival limit of the protected semiconductor branch.

This does not mean the fuse can always save the device in every fault. Very fast solid-state faults may still need gate-driver shutdown or electronic protection first. But the fast fuse is still essential because it provides a final interruption layer when current becomes catastrophic.

##### A careful beginner distinction

Here is an important distinction that students often miss:

- a general wiring fuse protects cables and installation,
- a semiconductor fuse is selected with device-stress coordination in mind.

Sometimes one product family can address both roles, as Mersen notes for the HSJ line [Mersen HSJ Family]. But we must not assume every HRC fuse is automatically suited to semiconductor protection. The time-current behavior and let-through energy matter.

##### A realistic converter example

Imagine the DC link of a medium-power battery charger or inverter. If one bridge device fails short, the DC-link capacitor can dump very large current into the fault path. A fast semiconductor fuse in the right location can interrupt that current and help prevent the fault from propagating into copper bars, cables, or additional devices.

Now compare that with a slow overload in a battery charger caused by an over-demanding load. In that case, opening a fuse immediately may not be the preferred control behavior. Electronic current limiting may be better. This comparison helps us see why fuses and current limiting are not rivals. They serve different time scales and fault severities.

##### What the fuse does not know

A fuse does not know why the overcurrent happened. It does not distinguish:

- overload from short circuit,
- temporary inrush from sustained fault,
- control error from wiring short.

It responds only to current and time. That simplicity is a strength, but it is also why electronic protection is often added.

#### Electronic current limiting

**Electronic current limiting** means that the converter measures current and actively changes its own behavior to keep that current below a chosen level.

This is a very different protection philosophy from the fuse. The fuse sacrifices itself to open the circuit. Electronic current limiting tries to keep the system operating, or at least shut it down gracefully, before destructive current flows too long.

The most basic sensing idea is to place a small resistor in the current path and measure the voltage across it. From Ohm's law,

$$V_{\text{sense}} = I R_s.$$

If a control circuit compares that sense voltage with a reference $V_{\text{ref}}$, the current-limit threshold is approximately

$$\boxed{I_{\text{lim}} \approx \frac{V_{\text{ref}}}{R_s}} \quad \text{(8.5)}$$

where $I_{\text{lim}}$ is the current-limit value and $R_s$ is the sense resistance.

Suppose a battery charger uses a sense resistor of $0.05\,\Omega$ and the current-limit comparator threshold is $0.25 \text{ V}$. Then

$$I_{\text{lim}} \approx \frac{0.25}{0.05} = 5 \text{ A}.$$

That arithmetic is simple, but it captures the core idea of a huge amount of practical power electronics.

##### Different behaviors under current limit

Once the current reaches the threshold, the controller may respond in different ways:

- **constant-current limiting**: hold the current near a set value,
- **cycle-by-cycle limiting**: in a switching converter, terminate or reduce each switching pulse when the current reaches the threshold,
- **foldback limiting**: reduce the allowed current further when the output voltage collapses,
- **shutdown and retry**: stop switching, wait, and then attempt restart.

The syllabus asks only for concept level, so we do not need every detail. But we do need the main lesson: electronic current limiting is an active control response, not a passive sacrificial event.

##### Why electronic current limiting is so useful

Electronic current limiting is especially attractive in:

- battery chargers, where current often needs to be controlled intentionally,
- DC-DC converters, where overload response should be graceful,
- auxiliary converters, where restart behavior matters,
- renewable-energy interfaces, where temporary overload should not always mean replacing a fuse.

This is one of the biggest practical differences between a laboratory supply and a crude raw source. A good power-electronic system often limits current intelligently before it reaches a destructive region.

##### Limits of electronic current limiting

Electronic current limiting is powerful, but it has limitations.

First, it depends on sensing and response speed. If the fault rises much faster than the controller can react, the device may still see dangerous stress.

Second, the sense resistor and circuitry introduce cost, power loss, and noise sensitivity.

Third, very severe hard shorts may still require a fuse or device-level shutdown path as a backup.

So the right conclusion is not "electronic limiting replaces the fuse." The right conclusion is "electronic limiting reduces the number and severity of events that the fuse must finally clear."

**Image prompt for Figure 8.4:** Create a textbook-style figure showing electronic current limiting in a DC-DC converter. Show a power switch, load, sense resistor in the current path, a comparator or controller that monitors the sense voltage, and a control action block that reduces PWM or turns the switch off when current exceeds threshold. Add aligned waveforms for inductor current, sense voltage, and PWM command, marking the current-limit threshold. Use monochrome engineering style.

*Renewable-energy relevance.* Electronic current limiting is central in solar battery chargers, MPPT converters, EV auxiliary converters, and bidirectional storage interfaces because these systems often need to operate safely under overload without immediate hard disconnection.

#### Desaturation detection (concept)

The third overcurrent-protection method in the syllabus is **desaturation detection**, usually shortened to **DESAT**.

This is one of the most important modern fault-protection concepts for IGBT gate drivers, and it is worth learning slowly.

##### The physical idea behind DESAT

In normal ON-state operation, an IGBT has a relatively low collector-emitter voltage. If a severe short circuit occurs while the IGBT is commanded ON, the current rises dramatically and the device is driven out of its normal low-voltage saturation region. The collector-emitter voltage then rises abnormally. Infineon describes this directly: under short-circuit conditions the power switch goes into desaturation mode and its $V_{CE(\text{sat})}$ rises; the driver detects that increase while the switch is ON [Infineon DESAT Article].

So DESAT does not measure current directly with a large shunt in the main current path. Instead, it infers dangerous overcurrent from abnormal device voltage during the ON state.

That is a very elegant idea because the gate driver is already electrically close to the power device.

##### The basic threshold relation

In a common DESAT arrangement, the detection path includes a diode from the collector side to the DESAT node. A useful simplified relation is

$$\boxed{V_{CE,\text{trip}} \approx V_{\text{DESAT,th}} - V_D} \quad \text{(8.6)}$$

where $V_{CE,\text{trip}}$ is the approximate collector-emitter voltage at which the driver interprets a fault, $V_{\text{DESAT,th}}$ is the internal DESAT threshold, and $V_D$ is the detection-diode drop.

Infineon's DESAT guidance gives a concrete illustration of the idea: the sense path includes the device voltage and diode behavior, and the protection threshold is determined from that sensed value [Infineon DESAT Article]. The exact equation varies with the particular driver architecture, but the core principle is the same.

Suppose a driver uses a DESAT threshold near $9 \text{ V}$ and the sensing diode contributes about $1 \text{ V}$. Then the circuit may begin to interpret an IGBT collector-emitter voltage of roughly $8 \text{ V}$ as a severe fault indicator. That is much higher than a normal saturated IGBT ON-state drop, which is exactly the point.

##### Why blanking time is needed

A beginner might now ask a smart question: if the collector-emitter voltage is high during the switching transition, would DESAT falsely trip every turn-ON?

That is exactly why DESAT protection includes a short **blanking time**. During normal turn-ON, the IGBT needs a brief interval to enter its normal saturated state. The driver ignores the DESAT signal during that interval. Infineon explicitly notes that blanking time is used to allow normal turn-on before fault judgment is made [Infineon DESAT Article], [TI UCC21750 Datasheet].

This is a beautiful example of good protection design. The protection must be fast, but it must also understand what normal behavior looks like.

##### What happens after a DESAT event

A modern driver typically does more than simply turn the device off instantly.

TI describes the UCC21750 as providing fast DESAT protection, fault reporting, and **soft turn-off** when a fault happens [TI UCC21750 Datasheet]. Soft turn-off is important because a very abrupt turn-off during a short circuit could create even worse overvoltage due to stray inductance. So the driver deliberately removes gate charge in a controlled way.

At concept level, a DESAT protection sequence is often:

1. Device is commanded ON.
2. Blanking time allows normal turn-on transition.
3. Driver monitors the DESAT sense node.
4. If the inferred device voltage exceeds the fault threshold, the driver declares overcurrent or short circuit.
5. The driver initiates controlled turn-off and often asserts a fault flag.

Infineon describes essentially this sequence in its DESAT guidance [Infineon DESAT Article].

##### What DESAT is good at and what it is not

DESAT is especially good for protecting IGBTs and similar devices against severe short-circuit events close to the device. It is fast and integrated naturally with the driver.

But DESAT is not the whole protection system.

- It does not replace branch-circuit fusing.
- It does not replace careful layout and snubbing.
- It does not mean the device can survive every possible fault indefinitely.
- It is mainly aimed at severe overcurrent or short-circuit conditions, not ordinary mild overload.

Infineon's DESAT guidance makes this point clearly by distinguishing DESAT as short-circuit protection rather than general overload control [Infineon DESAT Article].

##### Putting the three overcurrent methods together

At this point, it helps to compare the three methods side by side.

Table 8.2: Overcurrent protection methods compared

| Method | Main response style | Best at | Main tradeoff |
|---|---|---|---|
| Fast-acting / HRC fuse | Opens the circuit after overcurrent energy exceeds its design limit | High-fault-current interruption and backup protection | Sacrificial, passive, and not selective about fault cause |
| Electronic current limiting | Actively controls or shuts down the converter as current approaches threshold | Graceful overload handling and controlled converter behavior | Depends on sensing speed, control action, and added circuitry |
| DESAT detection | Uses abnormal ON-state device voltage to detect severe short circuit locally | Fast protection of IGBTs or similar devices during hard faults | Usually complements, not replaces, fuses and wider system protection |

##### Common misconceptions in overcurrent protection

Three misconceptions are especially worth flagging.

The first is that a fuse alone is enough for every semiconductor fault. It is often essential, but it may be too slow to prevent all device damage in very fast faults.

The second is that current limiting alone makes the system indestructible. A hard short or control failure may still exceed what the limiting loop can safely handle.

The third is that DESAT is just another current sensor. It is not. It is a device-voltage-based fault-detection method optimized for severe short-circuit protection in the driver environment [Infineon DESAT Article], [TI UCC21750 Datasheet].

*Renewable-energy relevance.* Inverter legs for PV, wind, and UPS systems often combine these layers: electronic current control during normal overload, DESAT or local short-circuit shutdown at the gate-driver level, and fusing at the branch or DC-link level.

## Worked interpretation exercise

We will read a real artifact that matches this chapter well:

- the [Mersen HSJ series product page](https://www.mersen.com/en/products/hsj-class-j-high-speed), especially the [HSJ200 example page](https://us.mersen.com/en/products/hsj-class-j-high-speed/hsj200)

This is a useful learning artifact because Mersen explicitly states that the HSJ line combines branch-circuit protection with very low $I^2 t$ for protection of power semiconductors such as diodes, SCRs, GTOs, and SSRs [Mersen HSJ Family].

### Step 1: Read the basic ratings without over-interpreting them

The HSJ200 page identifies the device as a **600 VAC, 500 VDC, 200 A** high-speed fuse [Mersen HSJ Family]. Those numbers are not all the same kind of information.

- `600 VAC` and `500 VDC` are voltage ratings.
- `200 A` is the fuse ampere rating.

This does **not** mean the fuse will interrupt every possible 200 A event instantly. It means that 200 A is the nominal current class of the fuse, while its actual behavior under overload or fault must still be understood from the family characteristics and curves.

That is the first important reading habit: do not confuse nominal ampere rating with fault-clearing behavior.

### Step 2: Focus on the phrase "very low $I^2 t$"

The product page states that the HSJ family provides **very low $I^2 t$** for protection of power semiconductors [Mersen HSJ Family]. This phrase tells us why the fuse belongs in a power-electronics chapter rather than only in a wiring chapter.

Low $I^2 t$ means the fuse is intended to limit the energy let through during a fault. Since semiconductors are sensitive to current-squared heating, this phrase is exactly what we want to see when reading about fuse suitability for semiconductor branches.

So from one short statement we can already infer the design intention:

- not just installation protection,
- but also device-stress limitation.

### Step 3: Notice that Mersen also mentions branch-circuit protection

Mersen says the HSJ combines semiconductor-fuse behavior with branch-circuit performance [Mersen HSJ Family]. That is an important system-level clue.

It tells us the fuse family is trying to serve in the real power path, not only as a tiny internal local protector. In practical equipment, that can reduce the gap between installation protection and semiconductor protection, although final coordination still depends on the exact system design.

This is also a reminder that protection is hierarchical. A device that helps protect the semiconductor may also have to satisfy broader system-protection expectations.

### Step 4: Connect the artifact to the chapter concepts

Now let us connect what we read to the theory from this chapter.

The HSJ page does not use the words "current limiting controller" or "DESAT." That is not a weakness. It tells us this artifact belongs to one particular protection layer: the fuse layer. Its language is about voltage class, ampere rating, standards, and low $I^2 t$.

So when we read a fuse page like this, we should ask:

- Is it intended for semiconductor protection or only wiring protection?
- Does it explicitly mention low $I^2 t$ or high-speed semiconductor service?
- Are the AC and DC voltage ratings compatible with our actual bus?
- Is its current class in the right range for the converter branch?

Those are much better questions than simply asking whether the fuse is "big enough."

### Step 5: Relate it to renewable-energy hardware

In a PV inverter, battery converter, or UPS, a fuse like this could appear on an AC branch, DC link branch, or semiconductor-feeding path where high prospective fault current exists. The fuse is not there to do the same job as a DESAT-capable gate driver. It is there to provide a robust interruption layer when fault current becomes large enough that the system must be physically opened.

That is the key lesson from the artifact:

The wording of a real fuse datasheet or product page tells us whether the device is intended merely to survive current, or to protect semiconductors by limiting let-through energy.

## How this matters in renewable-energy systems

Renewable-energy systems are full of abnormal electrical events because they connect together long cables, switching converters, energy storage, and often the utility grid. Protection therefore cannot be an afterthought.

In **solar PV inverters**, MOVs are commonly used at the AC input or other surge-exposed interfaces, while TVS diodes protect control rails, sensing inputs, and communication ports. In **battery chargers** and **battery-energy-storage systems**, electronic current limiting is often part of normal operation because charge current must be managed deliberately, while TVS diodes and local surge clamps protect low-voltage electronics from connection transients. In **wind-energy converters** and **industrial UPS systems**, branch fuses and device-level short-circuit protection become especially important because the stored energy and prospective fault current can be large. In **EV power stages** and isolated auxiliary converters, DESAT-capable gate drivers are widely valued because they can react quickly to severe short-circuit conditions and perform controlled fault turn-off [TI UCC21750 Datasheet], [Infineon DESAT Article].

There is also a broader engineering lesson. Renewable-energy systems are expected to operate for long periods with high reliability. That means protection must be layered. One device absorbs the surge, another clamps a local node, another limits overload current, another detects device-level short circuit, and another physically interrupts the fault path if necessary. Reliability comes not from one perfect protector, but from several well-coordinated ones.

## Chapter summary

- **Overvoltage protection** must be matched to the type of abnormal voltage: short surge, switching spike, or sustained DC overvoltage.
- For sinusoidal mains, the peak voltage is
  $\boxed{V_{pk}=\sqrt{2}\,V_{rms}}$ from Equation (8.1), so a 230 V RMS line has a peak of about 325 V.
- An **MOV** is a nonlinear voltage-dependent resistor used mainly for surge suppression; it remains high impedance at normal voltage and becomes more conductive during a surge [Bourns, *Tips on Selecting the Right MOV Surge Suppressor*].
- MOV ratings must be read using terms such as MCOV, varistor voltage, clamping voltage, and surge current waveform.
- MOVs are good for short surges, but repeated surges age them and sustained overvoltage can overheat them, which is why upstream fuse or disconnect protection is often recommended [Bourns, *Tips on Selecting the Right MOV Surge Suppressor*].
- A **TVS diode** is a fast avalanche clamp used to protect sensitive electronics against transient voltage events [Littelfuse 3.0SMC Series], [Littelfuse 5KP Series].
- Important TVS terms are reverse standoff voltage, breakdown voltage, clamping voltage, peak pulse current, and peak pulse power.
- A useful first pulse estimate is
  $\boxed{P_{\text{pulse,approx}}\approx V_C I_{PP}}$ from Equation (8.2).
- A **crowbar circuit** senses excessive voltage and then deliberately creates a low-impedance fault path, typically using an SCR, to force current limiting or fuse opening [onsemi AN004E/D], [onsemi MC3423 Datasheet].
- A simple divider-based crowbar threshold can be expressed as
  $\boxed{V_{\text{trip}}=V_{\text{ref}}\left(1+\frac{R_1}{R_2}\right)}$ from Equation (8.3).
- **Overcurrent protection** depends on both current magnitude and duration, captured by
  $\boxed{I^2t=\int i^2(t)\,dt}$ from Equation (8.4).
- **Fast-acting / HRC fuses** are used because power semiconductors may need low let-through energy during faults; Mersen explicitly describes the HSJ family as providing very low $I^2 t$ for protecting semiconductors [Mersen HSJ Family].
- **Electronic current limiting** measures current and changes converter behavior actively; with a sense resistor, a first threshold estimate is
  $\boxed{I_{\text{lim}}\approx V_{\text{ref}}/R_s}$ from Equation (8.5).
- **Desaturation detection** is a gate-driver protection method that infers severe overcurrent from abnormally high ON-state device voltage, especially in IGBTs [Infineon DESAT Article].
- A useful simplified DESAT relation is
  $\boxed{V_{CE,\text{trip}}\approx V_{\text{DESAT,th}}-V_D}$ from Equation (8.6).
- DESAT protection usually includes blanking time, fault signaling, and controlled or soft turn-off [TI UCC21750 Datasheet], [Infineon DESAT Article].
- In real converters, MOVs, TVS diodes, crowbars, fuses, electronic current limiting, and DESAT are often used together as coordinated protection layers.

## Further reading

- [Bourns, *Tips on Selecting the Right MOV Surge Suppressor*](https://www.bourns.com/docs/technical-documents/technical-library/varistors/bourns-tips-on-selecting-the-right-mov-surge-suppressor-white-paper.pdf) - A practical white paper on MOV behavior, MCOV, clamping, surge waveforms, and the thermal limits that matter in real designs.
- [Littelfuse 5KP Series](https://www.littelfuse.com/products/overvoltage-protection/tvs-diodes/high-power/5kp) - A good entry point for reading TVS terminology such as peak pulse power, clamping capability, and intended transient-protection role.
- [onsemi, *AN004E/D: Consideration for DC Power Supply Voltage Protector Circuits*](https://www.onsemi.com/download/application-notes/pdf/an004e-d.pdf) - A strong reference for understanding crowbar overvoltage protection and the practical issues of sensing, nuisance immunity, and SCR action.
- [Mersen HSJ Family](https://www.mersen.com/en/products/hsj-class-j-high-speed) - Useful for learning how fuse manufacturers describe semiconductor protection, low $I^2 t$, and branch-circuit capability in real product language.
- [TI UCC21750 Datasheet](https://www.ti.com/product/UCC21750) - A modern example of a gate driver with DESAT, soft turn-off, UVLO, and fault reporting, very useful for connecting device-level protection concepts to practical converter hardware.

