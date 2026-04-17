# Chapter 2.3: Overvoltage and Overcurrent Protection

## Chapter opening

Previous chapters examined gate driving and transient control during switching. Those topics address normal converter operation. Protection addresses abnormal operation: line surges, regulator failure, wiring faults, stalled loads, short circuits, and device faults can impose excessive voltage, excessive current, or both.

Protection is therefore part of converter design rather than an afterthought. This chapter examines overvoltage protection using the MOV, the TVS diode, and the crowbar circuit, and overcurrent protection using fast-acting (HRC) fuses, electronic current limiting, and desaturation detection at concept level. The central design question is not which protector is "best," but which abnormal event must be survived and how the protective response should occur.

## Prerequisites check

This chapter assumes familiarity with basic gate-driver function, switching transients and snubbers, RMS and peak values of sinusoidal voltage, inductor energy $\tfrac{1}{2}LI^2$, and ON-state voltage terms such as $V_{CE(\text{sat})}$ and $V_{DS}$. The discussion builds on those ideas by moving from transient control to explicit fault protection.

## Core content

### 2.3.1 Overvoltage protection: MOV, TVS diodes, crowbar circuits

#### Why overvoltage protection is needed

A rooftop PV inverter may encounter several distinct overvoltage conditions. A surge can enter from the AC line during a nearby lightning event, parasitic inductance can produce a switching spike inside the converter, and a regulator failure can drive a low-voltage rail far above its intended value. All three are overvoltage events, but they differ in source, duration, and energy.

Protection method must therefore match fault type. A surge absorber, a fast local clamp, and a crowbar circuit do not serve the same purpose. For AC systems, one basic relation is immediately relevant:

$$\boxed{V_{pk} = \sqrt{2}\,V_{rms}} \quad \text{(8.1)}$$

where $V_{pk}$ is the sinusoidal peak voltage and $V_{rms}$ is the RMS value.

For a 230 V, 50 Hz mains supply,

$$V_{pk} = \sqrt{2}\times 230 \approx 325 \text{ V}.$$

Any protector connected across the line must first tolerate the normal operating voltage. If the normal peak value is misunderstood, a device may begin to conduct during ordinary operation rather than only during an abnormal event. Overvoltage protection also does not imply perfect regulation; many protectors allow voltage to rise to a defined clamping level above nominal, and no single protective element is suitable for every location [Bourns, *Tips on Selecting the Right MOV Surge Suppressor*], [Littelfuse 5KP Series], [onsemi AN004E/D].

#### The MOV

A **metal-oxide varistor**, or **MOV**, is a common surge-protection device at the input of power equipment.

Below its threshold region, the MOV presents very high impedance. During a surge, its resistance falls sharply and it diverts current away from the protected circuit. It is therefore best understood as a strongly nonlinear resistor rather than an ideal fixed-voltage ceiling. As surge current increases, the clamping voltage also increases [Bourns, *Tips on Selecting the Right MOV Surge Suppressor*].

The key terms used with an MOV are:

- **maximum continuous operating voltage (MCOV)**: the highest continuous AC or DC voltage the MOV should withstand in normal operation
- **varistor voltage**: a test-condition voltage, often specified at a current such as 1 mA DC
- **clamping voltage**: the voltage developed across the MOV at a specified surge current
- **surge current rating**: the magnitude of surge current the MOV can survive for a specified waveform

Bourns notes that MOV surge ratings are commonly specified on an **8/20 us** current waveform, meaning a standardized current pulse that rises and decays very quickly [Bourns, *Tips on Selecting the Right MOV Surge Suppressor*]. That rating immediately shows the intended service: short surge events rather than indefinite abnormal mains voltage.

##### Choosing the MOV from the normal voltage first

To protect the AC input of a 230 V, 50 Hz UPS or PV inverter, the first selection criterion is the continuous voltage rating. It must safely exceed the actual steady operating condition, including line tolerance. Only after that should the clamping level and surge capability be checked [Bourns, *Tips on Selecting the Right MOV Surge Suppressor*].

1. Determine the highest normal operating voltage.
2. Add realistic margin for supply tolerance.
3. Then check clamping and surge ratings.

If this order is ignored, the MOV may run hot even when the system is healthy.

##### What the MOV does well and what it does not

The MOV is simple, inexpensive, bidirectional in typical AC use, and capable of absorbing substantial surge current. It is therefore widely used at mains inputs.

Its limitations are equally important. Repeated surges age the device [Bourns, *Tips on Selecting the Right MOV Surge Suppressor*]. Sustained overvoltage can overheat the MOV and may drive it into thermal runaway, which is why fuse protection, thermal disconnects, or another upstream disconnection method is commonly required [Bourns, *Tips on Selecting the Right MOV Surge Suppressor*]. An MOV is suited to short surges; it is not by itself a remedy for long-duration overvoltage.

**Image prompt for Figure 8.1:** Create a clean textbook-style illustration of an MOV connected across a 230 V AC equipment input. Show normal sinusoidal mains where MOV current is nearly zero, and a second waveform panel showing a short surge on the mains with the MOV conducting large current and clamping the voltage. Label line, neutral, MOV, normal leakage region, surge current path, clamping voltage, and note that the clamp voltage rises with current. Use monochrome engineering style with clear axes and units.

##### A practical AC-input example

In a small inverter-powered water-pump controller, an MOV across the AC input can divert surge current during a storm and reduce stress on the bridge rectifier and bulk capacitor. If the mains remains abnormally high for a prolonged period, however, the MOV cannot serve as the only protection. It must work with an upstream fuse or disconnect.

#### The TVS diode

A **transient voltage suppressor diode**, or **TVS diode**, serves a different role. It is used where a fast, sharply defined clamp is needed on a lower-voltage line or sensitive node. Littelfuse describes TVS diodes as devices intended to protect sensitive electronics against transient voltage events and emphasizes fast response and strong clamping capability [Littelfuse 5KP Series], [Littelfuse 3.0SMC Series].

In first approximation, the distinction from an MOV is straightforward: the MOV is often chosen for higher-energy surge handling at equipment entry points, whereas the TVS diode is often chosen for fast local protection of lower-voltage buses and interfaces.

The key TVS terms are:

- **reverse standoff voltage**, often written $V_R$ or $V_{RWM}$: the maximum normal working voltage that should not trigger significant conduction
- **breakdown voltage**, $V_{BR}$: the region where avalanche conduction begins under the specified test current
- **clamping voltage**, $V_C$: the voltage across the TVS at a specified pulse current
- **peak pulse current**, $I_{PP}$: the surge current used in the clamping specification
- **peak pulse power**: the rated pulse power under a specified surge waveform

For a pulse event, a useful first estimate is

$$\boxed{P_{\text{pulse,approx}} \approx V_C I_{PP}} \quad \text{(8.2)}$$

where $P_{\text{pulse,approx}}$ is the approximate pulse power during the clamped event, $V_C$ is the clamping voltage, and $I_{PP}$ is the peak pulse current. This is an approximation rather than a full energy calculation, because real surge waveforms vary with time.

##### Reading the TVS ratings correctly

Consider a low-voltage controller board in a battery-energy-storage system using a 48 V nominal auxiliary bus. The first selection question is the highest bus voltage present during normal operation, including charging, regulation tolerance, and ripple. The reverse standoff voltage must exceed that normal condition. Only then should the breakdown and clamping values be checked [Littelfuse 5KP Series].

The basic selection logic is:

1. The normal bus voltage must stay below the reverse standoff rating.
2. The abnormal transient must rise into the avalanche region.
3. The resulting clamping voltage must stay below what the protected electronics can survive.

If the standoff voltage is too low, the diode leaks excessively or conducts during normal operation. If the clamping voltage is too high, the protected circuit still sees excessive stress.

##### Where TVS diodes are useful and where they are not

TVS diodes are widely used on:

- low-voltage DC buses
- gate-driver supply rails
- communication and sensing lines
- control inputs and outputs
- automotive and battery-connected electronics
- local protection points near sensitive ICs

Their value lies in fast local clamping close to the vulnerable node [Littelfuse 3.0SMC Series], [Littelfuse SLD6S Series].

They are not universal high-energy absorbers. Compared with an MOV at a mains input, a TVS diode usually protects a more local node and usually handles less total surge energy. Littelfuse also notes a typical failure mode of short circuit when a TVS is overstressed beyond its specified limits [Littelfuse 3.0SMC Series]. When surge energy or fault duration is too large, a different protector or a layered protection architecture is required.

**Image prompt for Figure 8.2:** Create a textbook-style voltage-current concept figure for a unidirectional TVS diode. Show a horizontal axis for voltage and vertical axis for current. Mark reverse standoff region with very small current, breakdown region, and clamping region at specified pulse current. Add labels for $V_{RWM}$, $V_{BR}$, $V_C$, and $I_{PP}$. Include a side inset showing a TVS connected across a 48 V DC auxiliary bus feeding a controller. Use monochrome engineering style with clear labels.

##### MOV versus TVS in plain language

Table 8.1 compares the three main overvoltage methods introduced in this section.

Table 8.1: MOV, TVS diode, and crowbar compared at beginner level

| Protection method | Main physical action | Strongest use case | Main limitation |
|---|---|---|---|
| MOV | Nonlinear resistance diverts surge current | Input surge suppression, especially at AC or higher-energy entry points | Degrades with repeated surges; not suited to sustained overvoltage by itself |
| TVS diode | Avalanche clamp limits transient voltage quickly | Fast local protection of sensitive low-voltage buses and nodes | Usually lower energy capability than a mains MOV; overstress may short the device |
| Crowbar circuit | Deliberately forces a low-impedance fault path when threshold is exceeded | Sustained overvoltage protection of sensitive DC supplies | Requires current limiting or fuse action elsewhere; trips hard rather than gently |

The distinction is strategic: these devices absorb, clamp, and force shutdown in different ways.

#### Crowbar circuits

The **crowbar circuit** differs from both MOV and TVS protection. Instead of clamping the voltage while remaining a passive shunt element, it deliberately creates a low-impedance fault path when the voltage exceeds a defined threshold. In a common implementation, an SCR is triggered across the supply or output, forcing the source into current limit or causing a fuse or breaker to open [onsemi AN004E/D], [onsemi MC3423 Datasheet].

A crowbar is therefore a latching response to dangerous sustained overvoltage. For a 5 V processor board or gate-driver supply, sacrificing a fuse may be preferable to allowing the rail to rise to 12 V or 15 V for even a short time.

##### Threshold setting in a simple sensing scheme

A common way to define the trip point is to compare a divided-down supply voltage with a reference. In a simple divider-based sense circuit, the trip voltage can be expressed as

$$\boxed{V_{\text{trip}} = V_{\text{ref}}\left(1+\frac{R_1}{R_2}\right)} \quad \text{(8.3)}$$

where $V_{\text{trip}}$ is the supply voltage at which the crowbar should trigger, $V_{\text{ref}}$ is the sensing reference, and $R_1$ and $R_2$ are the divider resistors.

Suppose a 5 V auxiliary rail should crowbar at about $6.25 \text{ V}$ and the reference is $2.5 \text{ V}$. Then

$$6.25 = 2.5\left(1+\frac{R_1}{R_2}\right).$$

So

$$\frac{R_1}{R_2} = \frac{6.25}{2.5}-1 = 1.5.$$

If $R_2 = 10 \text{ k}\Omega$, a nearby practical choice is $R_1 = 15 \text{ k}\Omega$.

The trip point is a design parameter that must be set deliberately.

##### Practical concerns in crowbar protection

Crowbar design raises three practical questions. First, nuisance tripping must be avoided; some sensing schemes impose a minimum overvoltage duration before firing [onsemi MC3423 Datasheet]. Second, the SCR or other crowbar device must withstand the expected current, surge, and $di/dt$. Third, the fault must actually be cleared: the source must current-limit, a fuse must open, a breaker must trip, or control logic must shut the supply down. The crowbar is one element in a protection chain, not a complete standalone solution.

**Image prompt for Figure 8.3:** Create a clean textbook-style schematic illustration of a DC supply protected by an SCR crowbar circuit. Show the regulated supply output feeding a sensitive load, a sense network and reference that trigger an SCR when output voltage exceeds threshold, and an upstream fuse or current-limited source. Add a waveform panel showing output voltage rising abnormally, crowbar firing, voltage collapsing, and source current increasing until protection clears. Label $V_{\text{trip}}$, fuse, SCR, sense divider, and load. Use monochrome engineering style.

##### A realistic low-voltage example

In a 15 V isolated gate-driver supply, if the isolated DC-DC converter fails and the output rises toward 24 V, the gate-driver IC and the power-device gate oxide may both be at risk. A brief spike could be handled by a TVS diode, but a sustained regulator failure demands a different response. A crowbar circuit is more suitable because it detects the abnormal DC voltage and forces the source into protective action.

### 2.3.2 Overcurrent protection: fast-acting (HRC) fuses, electronic current limiting, desaturation detection (concept)

#### Why overcurrent protection is needed

Overcurrent threatens semiconductors, conductors, and insulation through rapid heating and fault energy. In an inverter leg, a control failure or cable fault can drive current toward a value limited only by source impedance, DC-link impedance, and device survival. Magnitude and duration both matter, which is why the Joule integral is a useful measure:

$$\boxed{I^2 t = \int i^2(t)\,dt} \quad \text{(8.4)}$$

where $I^2 t$ is the current-squared time integral and $i(t)$ is the fault current waveform.

This relation matters because heating scales with current squared. A moderate overload for a long time and a severe short circuit for a very short time can both be destructive, but they stress the system differently. Fuses, semiconductor short-circuit ratings, and coordination discussions therefore often use $I^2 t$ as a measure of let-through thermal stress [Mersen HSJ Family].

If a fault current of $100 \text{ A}$ flows approximately constantly for $1 \text{ ms}$, then

$$I^2 t \approx 100^2 \times 0.001 = 10 \text{ A}^2\text{s}.$$

If the current is instead $300 \text{ A}$ for the same $1 \text{ ms}$, then

$$I^2 t \approx 300^2 \times 0.001 = 90 \text{ A}^2\text{s}.$$

Trip time therefore matters enormously. Three times the current produces nine times the $I^2 t$ for the same duration.

Protection is usually layered:

- one layer for catastrophic short-circuit interruption
- one layer for controlled overload limiting
- one layer for local device protection
- and, in many systems, another layer for branch or wiring protection

This chapter focuses on one representative method from each of those layers.

#### Fast-acting (HRC) fuses

A **fuse** remains one of the most important protective devices in power electronics.

Excess current heats a calibrated element until it melts and opens the circuit. The designation **HRC** means **high rupturing capacity**, indicating that the fuse can safely interrupt large fault current. In power-electronic service, the important distinction is often between ordinary installation fuses and semiconductor-protecting fuses selected for low let-through energy.

Mersen describes its HSJ high-speed series as combining branch-circuit protection with very low $I^2 t$ for protection of power semiconductors such as diodes, SCRs, GTOs, and solid-state relays [Mersen HSJ Family]. That description captures the essential point: in semiconductor service, the fuse matters not only because it opens, but because it limits the energy allowed through during the fault.

##### Why "fast" matters for semiconductors

Power semiconductors can be damaged before a general-purpose fuse reacts. A fast semiconductor fuse is selected so that its let-through energy is compatible with the survival limit of the protected branch. It does not guarantee that every device will survive every fault; very fast solid-state faults may still require gate-driver shutdown or other electronic protection. The fuse remains essential as a final interruption layer.

##### A careful beginner distinction

A general wiring fuse is selected primarily to protect cables and installation. A semiconductor fuse is coordinated with device stress, time-current behavior, and let-through energy. Some product families, including the HSJ line, address both roles [Mersen HSJ Family], but that cannot be assumed from the HRC label alone.

##### A realistic converter example

In the DC link of a battery charger or inverter, a failed bridge device can allow the DC-link capacitor to dump very large current into the fault path. A fast semiconductor fuse can interrupt that current and limit propagation into busbars, cables, and adjacent devices. A slower overload condition, by contrast, may be better handled by controlled current limiting rather than immediate fuse operation.

##### What the fuse does not know

A fuse responds only to current and time. It does not distinguish overload from short circuit, temporary inrush from sustained fault, or control error from wiring short. That simplicity is both its strength and its limitation, which is why converters often supplement fusing with electronic protection.

#### Electronic current limiting

**Electronic current limiting** measures current and actively alters converter operation to keep current below a chosen threshold. Unlike a fuse, it aims to preserve controlled operation or achieve a graceful shutdown before destructive heating develops.

The most basic sensing method is to place a small resistor in the current path and measure the voltage across it. From Ohm's law,

$$V_{\text{sense}} = I R_s.$$

If a control circuit compares that sense voltage with a reference $V_{\text{ref}}$, the current-limit threshold is approximately

$$\boxed{I_{\text{lim}} \approx \frac{V_{\text{ref}}}{R_s}} \quad \text{(8.5)}$$

where $I_{\text{lim}}$ is the current-limit value and $R_s$ is the sense resistance.

Suppose a battery charger uses a sense resistor of $0.05\,\Omega$ and the current-limit comparator threshold is $0.25 \text{ V}$. Then

$$I_{\text{lim}} \approx \frac{0.25}{0.05} = 5 \text{ A}.$$

##### Different behaviors under current limit

Once the current reaches the threshold, the controller may respond in several ways:

- **constant-current limiting**: hold the current near a set value
- **cycle-by-cycle limiting**: in a switching converter, terminate or reduce each switching pulse when the current reaches the threshold
- **foldback limiting**: reduce the allowed current further when the output voltage collapses
- **shutdown and retry**: stop switching, wait, and then attempt restart

Electronic current limiting is therefore an active control response rather than a sacrificial event.

##### Where electronic current limiting helps and where it does not

Electronic current limiting is particularly useful in battery chargers, DC-DC converters, and auxiliary supplies where overload response should remain controlled. Its limits are equally important: it depends on sensing accuracy and response speed, it adds cost and power loss, and a severe hard short may still require a fuse or device-level shutdown path as backup. Current limiting reduces the number and severity of events that the interruption layer must clear; it does not eliminate the need for interruption.

**Image prompt for Figure 8.4:** Create a textbook-style figure showing electronic current limiting in a DC-DC converter. Show a power switch, load, sense resistor in the current path, a comparator or controller that monitors the sense voltage, and a control action block that reduces PWM or turns the switch off when current exceeds threshold. Add aligned waveforms for inductor current, sense voltage, and PWM command, marking the current-limit threshold. Use monochrome engineering style.

#### Desaturation detection (concept)

The third overcurrent-protection method in the syllabus is **desaturation detection**, usually shortened to **DESAT**.

DESAT is a gate-driver protection method widely used with IGBTs and similar devices. Instead of measuring load current directly, it infers severe overcurrent from abnormally high ON-state device voltage. Under short-circuit conditions an IGBT leaves its normal low-voltage saturation region and its collector-emitter voltage rises sharply; the driver detects that rise while the device is ON [Infineon DESAT Article].

Because the gate driver is already electrically close to the device, DESAT provides a fast local fault indication without placing a large shunt resistor in the main current path.

##### The basic threshold relation

In a common DESAT arrangement, the detection path includes a diode from the collector side to the DESAT node. A useful simplified relation is

$$\boxed{V_{CE,\text{trip}} \approx V_{\text{DESAT,th}} - V_D} \quad \text{(8.6)}$$

where $V_{CE,\text{trip}}$ is the approximate collector-emitter voltage at which the driver interprets a fault, $V_{\text{DESAT,th}}$ is the internal DESAT threshold, and $V_D$ is the detection-diode drop.

The exact relation varies with driver architecture, but the principle is the same [Infineon DESAT Article]. If a driver uses a DESAT threshold near $9 \text{ V}$ and the sensing diode contributes about $1 \text{ V}$, the circuit may begin to interpret an IGBT collector-emitter voltage of roughly $8 \text{ V}$ as a severe fault indicator. That is far above a normal saturated IGBT ON-state drop.

##### Why blanking time is needed

During turn-on, the collector-emitter voltage is temporarily high even in normal operation. DESAT protection therefore includes a short **blanking time** so the device can enter its normal saturated state before fault judgment is made [Infineon DESAT Article], [TI UCC21750 Datasheet].

##### What happens after a DESAT event

A modern driver typically does more than turn the device off instantly. TI describes the UCC21750 as providing fast DESAT protection, fault reporting, and **soft turn-off** when a fault occurs [TI UCC21750 Datasheet]. Soft turn-off matters because an abrupt shutdown during a short circuit can create even worse overvoltage through stray inductance.

At concept level, a DESAT response sequence is often:

1. The device is commanded ON.
2. A blanking interval allows normal turn-on.
3. The driver monitors the DESAT sense node.
4. If the inferred device voltage exceeds the threshold, the driver declares a fault.
5. The driver initiates controlled turn-off and often asserts a fault flag.

##### What DESAT is good at and what it is not

DESAT is well suited to severe short-circuit protection close to the device. It does not replace branch-circuit fusing, careful layout, or snubbing, and it is not intended as general mild-overload control [Infineon DESAT Article].

##### Putting the three overcurrent methods together

Table 8.2 compares the overcurrent methods introduced in this section.

Table 8.2: Overcurrent protection methods compared

| Method | Main response style | Best at | Main tradeoff |
|---|---|---|---|
| Fast-acting / HRC fuse | Opens the circuit after overcurrent energy exceeds its design limit | High-fault-current interruption and backup protection | Sacrificial, passive, and not selective about fault cause |
| Electronic current limiting | Actively controls or shuts down the converter as current approaches threshold | Graceful overload handling and controlled converter behavior | Depends on sensing speed, control action, and added circuitry |
| DESAT detection | Uses abnormal ON-state device voltage to detect severe short circuit locally | Fast protection of IGBTs or similar devices during hard faults | Usually complements, not replaces, fuses and wider system protection |

## Worked case study: reading a high-speed fuse page

One useful real artifact for this chapter is the [Mersen HSJ series product page](https://www.mersen.com/en/products/hsj-class-j-high-speed), especially the [HSJ200 example page](https://us.mersen.com/en/products/hsj-class-j-high-speed/hsj200). Mersen states that the HSJ line combines branch-circuit protection with very low $I^2 t$ for protection of power semiconductors such as diodes, SCRs, GTOs, and SSRs [Mersen HSJ Family].

The HSJ200 page identifies the device as a **600 VAC, 500 VDC, 200 A** high-speed fuse [Mersen HSJ Family]. These are not all the same kind of rating. The voltage ratings describe where the fuse may be used, and the ampere rating identifies its nominal current class. They do not mean that every 200 A event will be interrupted instantly.

The phrase **very low $I^2 t$** is the most important clue for semiconductor service. It indicates that the fuse is intended not only to open the circuit eventually, but to limit let-through energy to a level more compatible with semiconductor survival. That wording distinguishes a semiconductor-oriented fuse description from a purely installation-oriented one.

When reading a fuse product page for converter use, the useful questions are:

- Is the fuse intended for semiconductor protection or only for wiring protection?
- Does it explicitly mention low $I^2 t$ or high-speed semiconductor service?
- Are the AC and DC voltage ratings compatible with the actual bus?
- Is the current class appropriate for the converter branch?

In a PV inverter, battery converter, or UPS, a fuse of this kind may appear in an AC branch, a DC-link branch, or another high-fault-current path feeding a semiconductor stage. It does not perform the same role as DESAT or active current limiting. Its purpose is physical interruption when fault energy becomes too large for the converter to manage electronically.

## How this matters in renewable-energy systems

Renewable-energy systems connect long cables, switching converters, energy storage, and often the utility grid. They therefore experience both externally imposed disturbances and internally generated faults. Protection cannot be reduced to a single device type, because the events themselves are not all of the same kind.

In practical renewable-energy hardware, protection is layered. MOVs handle surge exposure at entry points. TVS diodes protect low-voltage rails and sensitive interfaces. Crowbar circuits protect supplies that must be shut down hard if regulation fails. Electronic current limiting manages overload in a controlled way. DESAT provides rapid device-level short-circuit detection in gate drivers. Fuses supply the final interruption layer when fault current must be physically cleared.

## Chapter summary

- Overvoltage protection must be matched to the type of abnormal voltage: short surge, switching spike, or sustained DC overvoltage.
- For sinusoidal mains, the peak voltage is $\boxed{V_{pk}=\sqrt{2}\,V_{rms}}$ from Equation (8.1), so a 230 V RMS line has a peak of about 325 V.
- An **MOV** is a nonlinear surge suppressor selected from its continuous operating voltage first; it is effective for short surges but requires upstream disconnection for prolonged overvoltage [Bourns, *Tips on Selecting the Right MOV Surge Suppressor*].
- A **TVS diode** is a fast local clamp for sensitive electronics; reverse standoff, breakdown, and clamping ratings must be read together [Littelfuse 3.0SMC Series], [Littelfuse 5KP Series].
- A **crowbar circuit** detects excessive voltage and deliberately forces a low-impedance fault path, typically to make the source current-limit or a fuse open [onsemi AN004E/D], [onsemi MC3423 Datasheet].
- Overcurrent stress depends on both magnitude and duration, captured by $\boxed{I^2t=\int i^2(t)\,dt}$ from Equation (8.4).
- **Fast-acting / HRC fuses** provide low let-through energy for semiconductor protection, while **electronic current limiting** actively controls overload response before interruption becomes necessary [Mersen HSJ Family].
- **DESAT** detects severe short circuit from abnormal ON-state device voltage in the gate-driver environment and complements, rather than replaces, wider system protection [Infineon DESAT Article], [TI UCC21750 Datasheet].

## Further reading

- [Bourns, *Tips on Selecting the Right MOV Surge Suppressor*](https://www.bourns.com/docs/technical-documents/technical-library/varistors/bourns-tips-on-selecting-the-right-mov-surge-suppressor-white-paper.pdf) - A practical white paper on MOV behavior, MCOV, clamping, surge waveforms, and the thermal limits that matter in real designs.
- [Littelfuse 5KP Series](https://www.littelfuse.com/products/overvoltage-protection/tvs-diodes/high-power/5kp) - A good entry point for reading TVS terminology such as peak pulse power, clamping capability, and intended transient-protection role.
- [onsemi, *AN004E/D: Consideration for DC Power Supply Voltage Protector Circuits*](https://www.onsemi.com/download/application-notes/pdf/an004e-d.pdf) - A strong reference for understanding crowbar overvoltage protection and the practical issues of sensing, nuisance immunity, and SCR action.
- [Mersen HSJ Family](https://www.mersen.com/en/products/hsj-class-j-high-speed) - Useful for learning how fuse manufacturers describe semiconductor protection, low $I^2 t$, and branch-circuit capability in real product language.
- [TI UCC21750 Datasheet](https://www.ti.com/product/UCC21750) - A modern example of a gate driver with DESAT, soft turn-off, UVLO, and fault reporting, very useful for connecting device-level protection concepts to practical converter hardware.
