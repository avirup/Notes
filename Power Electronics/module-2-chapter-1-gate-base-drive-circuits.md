# Chapter 2.1: Gate / Base Drive Circuits

## Chapter opening

The performance of a power semiconductor depends not only on the device itself but also on the circuit that drives it. Between a low-power controller and a power switch sits the drive circuit, which must apply the correct control voltage or current, deliver adequate source and sink capability, establish the correct electrical reference, and often provide isolation or level shifting. A device with excellent ratings can still switch poorly or fail if its drive circuit is weak, noisy, or incorrectly referenced.

This chapter examines that interface. For a power BJT it is a **base-drive circuit**; for a MOSFET or IGBT it is a **gate-drive circuit**. The chapter develops the requirements of a good driver, the role of gate charge and peak current, the totem-pole output stage, dedicated driver ICs, high-side and low-side driving, and isolated-drive methods. These ideas are central to practical converters in PV systems, battery chargers, UPS hardware, motor drives, and EV auxiliary supplies, where switching quality depends as much on the driver as on the power device itself.

## Prerequisites check

- forced beta and base-current requirement from Chapter 1.1
- capacitive gate behavior of the power MOSFET from Chapter 1.4
- stored-charge effects in the IGBT from Chapter 1.5
- basic relations such as $Q = CV$, $P = VI$, and the link between current, charge, and time
- the fact that converter switches may sit at potentials far above controller ground

The chapter assumes familiarity with basic switching waveforms, device terminals, and DC-bus voltage levels.

### 2.1.1 Requirements of a good drive circuit

A drive circuit is the interface between the low-power control stage and the power device. Its function is to force the device into the intended ON or OFF state at the intended time and with the intended electrical reference. The name changes with the device terminal: base drive for a BJT, gate drive for a MOSFET or IGBT. The system purpose is the same.

The first distinction is between current-driven and charge-driven control:

- A **power BJT** requires control current while it is ON.
- A **power MOSFET** or **IGBT** requires gate charge to be moved during switching; under steady DC gate bias, the ideal input current is very small [Infineon AN_2203 Gate Drive].

For a power BJT, the base-drive burden can be estimated from the forced-beta relation

$$\boxed{I_B \ge \frac{I_C}{\beta_{\text{forced}}}} \quad \text{(2.1)}$$

where $I_B$ is base current, $I_C$ is collector current, and $\beta_{\text{forced}}$ is the deliberately chosen switching gain.

If a power BJT must carry $10 \text{ A}$ and the design uses $\beta_{\text{forced}} = 5$, then

$$I_B \ge \frac{10}{5} = 2 \text{ A}.$$

This base-current requirement explains why a practical power-BJT drive stage is a substantial circuit rather than a direct logic interface.

For MOSFETs and IGBTs, the problem is different. The insulated gate does not require large steady current, but it must be charged and discharged quickly. Slow charging keeps the device in its transition region longer, increases switching loss, and can create cross-conduction in bridge circuits.

Table 2.1 summarizes the main requirements of a good drive circuit.

Table 2.1: Main requirements of a good drive circuit

| Requirement | What it means in practice | Why it matters |
|---|---|---|
| Correct drive amplitude | Apply the correct base-emitter or gate-source / gate-emitter voltage | Too little drive raises loss; too much drive can damage the device |
| Adequate source and sink capability | Charge and discharge the control terminal quickly | Faster, cleaner switching and lower switching loss |
| Correct reference point | Drive voltage must be measured with respect to the correct source or emitter terminal | A 12 V gate signal is meaningful only if it is 12 V above the local source/emitter |
| Noise immunity | Resist false turn-ON from $dv/dt$, ringing, and parasitic inductance | Prevents shoot-through and erratic switching |
| Timing accuracy | Turn devices ON and OFF at the intended instants, often with dead time | Essential in half-bridges, full-bridges, and inverters |
| Protection support | Include or cooperate with UVLO, current sense, shutdown, and fault reporting | Prevents operation in unsafe conditions |
| Isolation or level shifting when needed | Transfer control safely across a large potential difference | Necessary in many high-side and mains-referenced power stages |
| Low output impedance | Hold the device firmly in OFF state and drive it strongly in transition | Reduces sensitivity to noise and Miller-coupled disturbances |

Low output impedance matters because the control terminal must be held firmly at the intended voltage. A weak driver allows external disturbances to move the gate or base voltage. A strong driver resists that movement and provides active control during both turn-ON and turn-OFF.

Correct referencing is equally important. A MOSFET responds to $V_{GS}$, not to gate voltage measured relative to earth or controller ground. An IGBT responds to $V_{GE}$. If the source or emitter is moving, the driver must move with it or must be isolated from it. This is the basis of the high-side driving problem.

**Image prompt for Figure 2.1:** Create a clean textbook-style technical illustration showing the role of a power-device drive circuit between a low-voltage controller and a power semiconductor switch. Show, from left to right, a controller block generating a 3.3 V PWM signal, a gate/base driver block, and a power switch connected in a converter leg tied to a high-voltage DC bus. Include labels for "logic-level command," "level shifting," "source/sink current," "isolation if required," "local gate/emitter reference," and "power switch." Add a separate small comparison inset showing a BJT requiring base current continuously while a MOSFET/IGBT requires gate charge mainly during switching. Use monochrome textbook style with clear arrows and no decorative background.

The driver is therefore more than a pulse amplifier. It sets switching speed, OFF-state firmness, noise margin, and often part of the protection behavior. Insulated-gate devices do not require large steady input current, but they can still demand substantial peak drive current, and poor gate drive can create more loss in the switch than in the driver itself [Infineon AN_2203 Gate Drive].

### 2.1.2 MOSFET and IGBT gate driver basics: totem-pole driver and dedicated driver ICs

#### Gate charge and switching current

A MOSFET or IGBT gate is often described as voltage-controlled, but switching design is governed just as much by charge as by voltage. In steady state, the insulated gate draws very little DC current [Infineon AN_2203 Gate Drive]. During switching, however, the gate behaves as a capacitive load, and the driver must supply or remove charge quickly enough to produce acceptable transition times.

The fundamental relation is

$$\boxed{Q_G = \int i_G(t)\,dt} \quad \text{(2.2)}$$

where $Q_G$ is total gate charge and $i_G(t)$ is gate current during the switching event.

Gate charge is often more useful than a single capacitance value for design estimates because the effective capacitances vary with operating condition [Infineon AN_2203 Gate Drive]. For a first estimate, if the driver current is treated as approximately constant over the critical part of the transition, then

$$\boxed{t_{\text{sw,est}} \approx \frac{Q_G}{I_G}} \quad \text{(2.3)}$$

where $t_{\text{sw,est}}$ is estimated switching time, $Q_G$ is required gate charge, and $I_G$ is available gate-drive current.

The same logic gives a useful estimate of average gate-drive power:

$$\boxed{P_{\text{DRV,avg}} \approx Q_G V_{\text{DRV}} f_s} \quad \text{(2.4)}$$

where $P_{\text{DRV,avg}}$ is average drive power, $V_{\text{DRV}}$ is drive-voltage swing, and $f_s$ is switching frequency [Infineon AN_2203 Gate Drive].

Equation (2.4) shows that average drive power can remain small even when peak gate current is large. That distinction is central in practice. A design may dissipate little average power in the driver while still requiring several hundred milliamperes or several amperes of peak current for fast switching.

#### A short numerical example

Suppose a MOSFET used in a 48 V to 12 V EV auxiliary converter has total gate charge $Q_G = 60 \text{ nC}$ at the chosen drive condition, and the important part of the switching interval is limited to about $120 \text{ ns}$.

Using Equation (2.3),

$$I_G \approx \frac{Q_G}{t_{\text{sw,est}}} = \frac{60 \times 10^{-9}}{120 \times 10^{-9}} = 0.5 \text{ A}.$$

The driver should therefore be able to source and sink on the order of $0.5 \text{ A}$, and usually more once parasitics and design margin are included.

If the driver voltage swing is $V_{\text{DRV}} = 12 \text{ V}$ and the switching frequency is $f_s = 50 \text{ kHz}$, Equation (2.4) gives

$$P_{\text{DRV,avg}} \approx 60 \times 10^{-9} \times 12 \times 50 \times 10^3 = 36 \text{ mW}.$$

The average gate-drive power is only about $36 \text{ mW}$, yet the peak current requirement is around $0.5 \text{ A}$. This is why a microcontroller pin is usually inadequate as a direct power-switch driver.

#### The Miller plateau

During turn-ON, gate voltage does not always rise at a uniform rate. There is often an interval in which the gate-voltage rise slows or nearly flattens while the drain-source or collector-emitter voltage is changing. This is the **Miller plateau**. During that interval, much of the gate current is diverted into the effective gate-drain or gate-collector feedback capacitance rather than into further gate-voltage rise [Infineon AN_2203 Gate Drive].

Its practical meaning is straightforward: the driver is doing critical work even while the gate voltage appears nearly stationary. That interval corresponds to the collapse of device voltage and a large share of switching loss.

**Image prompt for Figure 2.2:** Create a textbook-style waveform figure for MOSFET/IGBT gate driving. Show three aligned plots versus time: gate current $i_G$, gate-source or gate-emitter voltage, and drain-source or collector-emitter voltage. Mark initial charging, threshold crossing, Miller plateau, and final fully enhanced region. Label the plateau as the interval where device voltage is changing while gate current continues to flow. Use monochrome engineering style with axes, units, and clean annotations.

#### The totem-pole driver

One of the most important output structures in gate driving is the **totem-pole driver**, also called a **push-pull output stage**. One device in the driver sources current into the gate during turn-ON, and another device sinks current during turn-OFF. The result is a low-impedance path in both directions.

This is a major improvement over passive charging or discharging through large resistances. A resistor can eventually move the required charge, but a totem-pole stage does so actively and much more strongly. Discrete driver examples built from small-signal BJTs or MOSFETs are often used to raise a logic signal to the required gate-drive level and to provide the necessary source and sink current [Infineon AN_2203 Gate Drive].

In many practical designs the turn-OFF path is intentionally stronger than the turn-ON path. A strong pull-down helps prevent false turn-ON caused by $C\,dv/dt$ coupling in half-bridge and full-bridge circuits [Infineon AN_2203 Gate Drive].

#### A simple low-side example

If a low-side MOSFET source is tied near ground, a 3.3 V controller pulse may still be insufficient for efficient switching. The gate may require 10 V to 12 V drive, and the transition may require substantial current. A small level-shift stage followed by a totem-pole output stage can translate the logic pulse to the required amplitude and deliver strong gate current. Infineon gives a discrete BJT-based example that raises the logic pulse to a 12 V swing and provides approximately $\pm 0.5 \text{ A}$ source and sink capability [Infineon AN_2203 Gate Drive]. The exact values are example-specific; the design lesson is general.

**Image prompt for Figure 2.3:** Create a clean textbook-style schematic-level illustration of a low-side totem-pole gate driver for a power MOSFET or IGBT. Show a 3.3 V logic input feeding a level-shift stage, then a push-pull output stage with an upper sourcing transistor and lower sinking transistor, then a gate resistor leading to the power device gate. Label source current path during turn-ON and sink current path during turn-OFF. Include the local source/emitter reference node and supply such as 12 V or 15 V. Use monochrome engineering style with clear labels and no decorative effects.

#### Dedicated gate-driver ICs

Discrete totem-pole stages are useful for explanation and still appear in practice, but modern converters commonly use **dedicated gate-driver ICs**. Such ICs provide a push-pull output stage together with features such as predictable peak source and sink current, UVLO, logic-level compatibility, matched timing, enable or shutdown functions, and in some families Miller clamp, fault reporting, dead-time control, or desaturation protection. Infineon notes the wide availability of low-side and dual-low-side driver ICs with different output-current classes and protection features [Infineon AN_2203 Gate Drive]. TI likewise describes modern isolated drivers with strong peak output current, UVLO, and timing features [TI UCC21520 Product Page].

**Undervoltage lockout**, or **UVLO**, is especially important. If the driver supply falls below a safe level, the driver inhibits normal operation rather than attempting to switch the device with inadequate drive voltage. Partial enhancement is dangerous because the current may be high while the ON-state voltage remains too large.

Drive voltage must also be taken from the specific device datasheet rather than from a generic rule. Infineon notes that standard-level power MOSFETs are commonly driven with about 10 V to 15 V gate pulses, while logic-level MOSFETs operate from lower gate voltage but may involve tradeoffs such as higher gate charge or greater susceptibility to induced turn-ON in half-bridge service [Infineon AN_2203 Gate Drive]. Threshold voltage is not the correct design target; it merely marks the onset of conduction under light test conditions. The same principle applies to IGBTs, whose recommended gate-emitter drive conditions depend on the device family and application.

### 2.1.3 High-side driving and isolated gate drive

#### Low-side and high-side driver concept

A **low-side switch** sits between the load and the negative rail. Its source or emitter is usually close to local ground, so the driver can often share the same reference. A **high-side switch** sits between the positive rail and the load. Its source or emitter moves with the switching node, so the driver output must be referenced to that moving node. A statement such as "apply 12 V to the gate" is incomplete unless it also states the reference: 12 V relative to the local source or emitter.

This is why high-side driving is more difficult. In a half-bridge, when the low-side switch turns ON, the midpoint falls near the negative rail; when the high-side switch turns ON, the midpoint rises near the positive rail. The high-side driver must therefore operate on a floating reference.

#### Bootstrap high-side driving

One common high-side solution is the **bootstrap circuit**. A capacitor is charged while the switching node is low. That stored charge is then used as a floating supply for the high-side driver when the switching node rises.

This approach appears in many high-side/low-side driver IC families. The Infineon IRS2101 datasheet, for example, describes a floating high-side channel intended for bootstrap operation, with up to $600 \text{ V}$ offset capability and UVLO [Infineon IRS2101 Datasheet].

The first sizing relation is

$$\boxed{\Delta V_{\text{BOOT}} \approx \frac{Q_{\text{TOT}}}{C_{\text{BOOT}}}} \quad \text{(2.5)}$$

where $\Delta V_{\text{BOOT}}$ is allowed bootstrap-voltage droop during the ON interval, $Q_{\text{TOT}}$ is the total charge drawn from the capacitor during that interval, and $C_{\text{BOOT}}$ is bootstrap capacitance.

This is a first estimate rather than a complete design equation. In practice, $Q_{\text{TOT}}$ includes not only power-device gate charge but also driver quiescent current, leakage, and design margin.

If $Q_{\text{TOT}} = 120 \text{ nC}$ and the allowed droop is $\Delta V_{\text{BOOT}} = 0.2 \text{ V}$, then

$$C_{\text{BOOT}} \approx \frac{120 \text{ nC}}{0.2 \text{ V}} = 600 \text{ nF}.$$

A practical design would choose a larger standard value to allow for tolerance and operating variation.

Bootstrap driving is compact and economical, but it is not universal. The capacitor must be refreshed, which means the switching pattern must periodically return the node to a condition that allows recharging. For that reason, bootstrap high-side drive is well suited to many PWM bridge circuits but not to every duty cycle or operating mode.

**Image prompt for Figure 2.4:** Create a textbook-style half-bridge driver illustration. Show a DC bus with upper high-side switch and lower low-side switch, a load connected to the midpoint, a low-side driver referenced to ground, and a floating high-side driver referenced to the switching node. Include a bootstrap diode and bootstrap capacitor between the driver supply and the high-side floating supply. Label the switching node, local emitter/source reference for each driver, charging path for the bootstrap capacitor, and high-side ON condition. Use monochrome engineering style with clear polarity and node labels.

#### When isolation is needed

**Galvanic isolation** means that no direct conductive path for steady current exists between the two sides of the interface. In gate driving, isolation may be required for safety, for noise immunity, for level shifting across large potential differences, or for some combination of these reasons. The controller may sit on a safe low-voltage domain while the power switch moves through hundreds of volts and high common-mode transient stress.

The main families are opto-coupler-based isolated drive, pulse-transformer-based isolated drive, and integrated isolated gate-driver ICs.

#### Opto-coupler-based isolated gate drive

An **opto-coupler** transfers the command across the isolation barrier by light. The input side drives an LED, and the output side detects that light and reconstructs the signal. In gate-drive applications, the isolated output side must still provide or control a stage capable of charging and discharging the MOSFET or IGBT gate.

The attraction of the opto-coupler method is clear galvanic isolation and good separation between the low-voltage controller domain and the noisy power domain. The main practical caution is equally clear: the isolated output side usually still needs its own local supply. The signal crosses the barrier optically, but the energy required to charge the gate on the isolated side must still be provided locally unless a specialized architecture is used.

#### Pulse-transformer-based isolated gate drive

A **pulse transformer** transfers the drive command magnetically. This approach has a long history in power electronics and is attractive where strong isolation and good common-mode immunity are required. ST's application note AN461 describes a pulse-transformer-based scheme for floating switches in motor drives, UPS systems, and AC switches, and shows how transformer coupling can transfer both signal information and drive energy without a floating auxiliary supply in that specific architecture [ST AN461].

Classical pulse-transformer drive, however, is constrained by volt-second balance and saturation. Infineon's isolated-gate-driving comparison note highlights these limitations and notes that simple pulse-transformer solutions are often duty-cycle-limited and suited to a bounded switching-frequency range [Infineon Isolated Gate Driving Solutions]. Specialized circuits can extend that range, but the transformer cannot be treated as an unrestricted DC-coupled interface.

#### Modern isolated gate-driver ICs

Many contemporary converters use **integrated isolated gate drivers** rather than a separate opto-coupler or custom pulse transformer. These devices place the isolation barrier and the output driver in a single package. TI's UCC21520, for example, is described as a dual-channel isolated gate driver with reinforced isolation, strong peak output current, UVLO, and high common-mode transient immunity [TI UCC21520 Product Page].

The integration changes packaging rather than design questions. The designer must still ask about isolation rating, channel arrangement, source and sink current, common-mode transient tolerance, and suitability for low-side, high-side, or half-bridge use.

#### Comparing the main approaches

Table 2.2 summarizes the main approaches at concept level.

Table 2.2: High-side and isolated driver approaches at concept level

| Approach | Main strength | Main limitation or caution | Typical fit |
|---|---|---|---|
| Low-side non-isolated driver | Simple reference, low cost, easy layout | Only works when source/emitter stays near local ground | Buck converters, low-side switches, grounded stages |
| Bootstrap high-side driver | Compact and widely used in bridge circuits | Floating supply must be refreshed; not ideal for every duty condition | Half-bridges, inverters, synchronous legs |
| Opto-coupler isolated drive | Clear galvanic isolation, good noise separation | Often still needs isolated secondary supply | Mains-referenced stages, industrial inverters, battery chargers |
| Pulse-transformer isolated drive | Strong isolation and good $dv/dt$ immunity | Classical circuits are constrained by volt-second balance and saturation | High-frequency isolated drive, some bridge and inverter stages |
| Integrated isolated gate-driver IC | Combines barrier and strong driver in one package | Cost and supply planning still matter | Modern PV, UPS, EV, and motor-drive power stages |

High-side drive and isolated drive are related but not identical. A high-side driver must cope with a floating reference. Isolation is one way to achieve that, but bootstrap high-side drive is another and does not itself provide galvanic isolation.

## Worked interpretation exercise

The [TI UCC21520 product page](https://www.ti.com/product/UCC21520) is a useful example of how to read a modern gate-driver specification. TI describes the device as a dual-channel isolated gate driver with 4 A source and 6 A sink peak current, reinforced isolation of 5.7 kV RMS for one minute, minimum common-mode transient immunity greater than 125 V/ns, configuration options for two low-side drivers, two high-side drivers, or a half-bridge driver, and UVLO on all supply pins [TI UCC21520 Product Page].

Taken together, those statements identify a real power-driver component rather than a signal isolator. The peak-current ratings indicate a strong push-pull output stage. The isolation and CMTI ratings indicate suitability for fast, noisy switching environments. The channel configuration options show that the same IC can serve in several converter arrangements, and UVLO indicates that the device is designed to prevent unsafe partial-drive operation.

Table 2.3 translates the datasheet language into design language.

Table 2.3: Interpreting the UCC21520 datasheet

| Datasheet statement | Plain-language meaning | Design importance |
|---|---|---|
| Dual-channel isolated gate driver | Two real gate-drive outputs sit behind an isolation barrier | Suitable for one half-bridge leg or two isolated switches |
| 4 A source, 6 A sink peak | Strong push-pull output stage | Can move gate charge quickly and hold OFF state firmly |
| 5.7 kV RMS reinforced isolation | High-grade barrier inside the package | Useful where controller and power stage must be safely separated |
| CMTI greater than 125 V/ns | Fast common-mode node movement will not easily corrupt the signal | Important in hard-switched inverter and converter legs |
| Configurable as two low-side, two high-side, or half-bridge | Flexible channel referencing and use | Fits different topologies without changing IC family |
| UVLO on supply pins | Driver refuses unsafe low-supply operation | Helps prevent partial enhancement and excess device loss |

The same reading method applies to any driver datasheet. The essential questions are whether the part is a true gate driver or only an isolator, how strong the source and sink stages are, whether UVLO is included, what isolation and CMTI ratings are specified, and whether the device is intended for low-side, high-side, bootstrap-based, or fully isolated use.

## How this matters in renewable-energy systems

Drive circuits are easy to overlook in introductory block diagrams, but they are central to the performance of practical converters. In a solar PV inverter or battery-storage converter, the controller may sit on a quiet low-voltage board while the switches operate on a noisy, high-voltage bridge node. The driver must translate those controller commands into correctly referenced, high-current switching action.

The result affects more than turn-ON and turn-OFF. Gate-drive strength, referencing, and isolation influence switching loss, EMI behavior, shoot-through immunity, fault response, and device survival. In that sense, the drive circuit is one of the places where converter theory becomes converter hardware.

## Chapter summary

- A **drive circuit** interfaces the low-power control stage with the power semiconductor switch.
- A **base-drive circuit** for a BJT must supply control current while the device is ON; a first switching estimate is $I_B \ge I_C/\beta_{\text{forced}}$.
- A MOSFET or IGBT gate is insulated, so steady-state input current is small, but switching still requires charge transfer [Infineon AN_2203 Gate Drive].
- The fundamental gate-charge relation is $Q_G = \int i_G(t)\,dt$.
- A useful first switching-time estimate is $t_{\text{sw,est}} \approx Q_G / I_G$.
- A useful first average gate-drive-power estimate is $P_{\text{DRV,avg}} \approx Q_G V_{\text{DRV}} f_s$ [Infineon AN_2203 Gate Drive].
- The **Miller plateau** is the interval during which gate current continues to flow while device voltage is changing.
- A **totem-pole driver** actively sources current for turn-ON and sinks current for turn-OFF, giving low output impedance in both directions.
- **Dedicated gate-driver ICs** commonly add stronger output stages, UVLO, timing control, and sometimes additional protection features.
- A **low-side driver** is referenced to a near-ground source or emitter, while a **high-side driver** must operate on a floating reference.
- A **bootstrap high-side driver** uses stored charge on a capacitor to power a floating high-side channel; a first estimate is $\Delta V_{\text{BOOT}} \approx Q_{\text{TOT}} / C_{\text{BOOT}}$.
- **Opto-coupler-based isolated drive** transfers the command across a light-based galvanic barrier.
- **Pulse-transformer-based isolated drive** transfers gate-drive information magnetically and offers strong isolation, but classical solutions are constrained by volt-second balance and saturation [Infineon Isolated Gate Driving Solutions], [ST AN461].
- Modern **integrated isolated gate-driver ICs** combine the isolation barrier and the output driver in one package [TI UCC21520 Product Page].

## Further reading

- [Infineon, *Gate drive for power MOSFETs in switching applications*](https://www.infineon.com/dgdl/Infineon-Gate_drive_for_power_MOSFETs_in_switchtin_applications-ApplicationNotes-v01_00-EN.pdf?fileId=8ac78c8c80027ecd0180467c871b3622) - A strong beginner-to-intermediate application note on gate charge, discrete drivers, driver ICs, and high-side methods.
- [Infineon, *Isolated gate driving solutions*](https://www.infineon.com/dgdl/Infineon-GateDriverIC_EiceDRIVER_isolated_gate_driving_solutions-ApplicationNotes-v01_00-EN.pdf?fileId=5546d462700c0ae60170a0c4af851028) - A focused comparison of pulse-transformer and isolated-driver approaches, useful for understanding duty-cycle, CMTI, and integration tradeoffs.
- [Infineon, *IRS2101(S)PbF High and Low Side Driver Datasheet*](https://www.infineon.com/assets/row/public/documents/24/49/infineon-irs2101-datasheet-en.pdf) - A concise real datasheet for learning bootstrap high-side/low-side driver terminology and ratings.
- [Texas Instruments, *UCC21520 Product Page and Datasheet*](https://www.ti.com/product/UCC21520) - A useful modern example of an isolated dual-channel gate driver with strong output current, UVLO, CMTI, and flexible channel use.
- [STMicroelectronics, *AN461: An isolated gate drive for Power MOSFETs and IGBTs*](https://www.st.com/resource/en/application_note/an461-an-isolated-gate-drive-for-power-mosfets-and--igbts-stmicroelectronics.pdf) - A compact note that is especially helpful for understanding pulse-transformer-based isolated gate-drive thinking.
