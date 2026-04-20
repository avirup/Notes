# Chapter 3.3: Applications of Controlled Rectifiers in Renewable Energy Systems

## Chapter opening

Chapters 3.1 and 3.2 treated controlled rectifiers mainly as converter circuits. In renewable-energy systems, the same circuits appear as system interfaces between a variable AC source and a controlled DC or AC destination. Their importance therefore lies not only in waveform conversion, but also in the way they establish usable electrical conditions for later stages.

This chapter examines that role in two settings: wind-energy conversion systems and HVDC transmission. Wind-energy systems show how a rectifier stage can form or support a DC link between a generator and downstream power-conditioning equipment. HVDC shows the same AC-DC conversion principle at a much larger scale, where converter stations control the transfer of bulk power over long distances [Mohan, Undeland, Robbins, *Power Electronics: Converters, Applications and Design*, 3e], [Abu-Rub, Malinowski, Al-Haddad, *Power Electronics for Renewable Energy Systems, Transportation and Industrial Applications*].

Classical line-commutated thyristor rectifiers remain central to understanding high-power conversion and traditional HVDC. At the same time, many modern wind turbines and newer transmission schemes use self-commutated converters instead of SCR bridges. Controlled-rectifier theory therefore serves both as a description of practical hardware and as a foundation for understanding why later converter technologies developed [NPTEL, *Line Commutated and PWM Rectifiers*], [Hitachi Energy, *HVDC Classic (LCC)*], [Hitachi Energy, *HVDC Light (VSC)*].

## Prerequisites check

- You should be comfortable with SCR triggering, natural commutation, and firing angle from Chapters 1.2, 3.1, and 3.2.
- You should remember the average-voltage result for the three-phase full-controlled bridge under continuous-current conditions.
- You should know the basic idea of a DC link: AC is first converted to DC, then processed further by another converter stage.
- You should be comfortable with the basic power relation $P = VI$ and with the difference between AC side quantities and DC side quantities.
- You should have a basic physical picture of a wind turbine, a generator, and an electrical grid.

If the average-voltage expression of the three-phase bridge is not fresh in your mind, review Chapter 3.2 before continuing.

## Core content

### 3.3.1 Controlled rectifiers as front-end stages in wind-energy conversion systems

#### Generator-side conversion and the DC link

Wind turbines do not operate from a constant mechanical input. As wind speed changes, rotor speed and generator electrical output also tend to change unless the turbine is intentionally constrained to a narrow operating range. The generator side therefore does not naturally produce the stable voltage, frequency, or phase required by the grid, nor does it directly provide the regulated DC required by storage systems or DC loads.

For that reason, the generator output is commonly passed first through a **front-end stage**. If the generator produces AC, that stage often performs a rectifier function by converting AC into DC. Downstream converters can then smooth, regulate, boost, invert, synchronize, or protect the power before it is delivered to the grid, a battery charger, or a shared DC bus [Abu-Rub, Malinowski, Al-Haddad, *Power Electronics for Renewable Energy Systems, Transportation and Industrial Applications*], [NREL Technical Report NREL/TP-5D00-59195].

For an ideal three-phase fully controlled bridge with continuous current, the average DC output is

$$\boxed{V_{DC,avg} \approx 1.35\,V_{LL,rms}\cos\alpha} \quad \text{(12.1)}$$

where $V_{DC,avg}$ is the average DC output voltage, $V_{LL,rms}$ is the line-to-line RMS voltage at the rectifier input, and $\alpha$ is the firing angle. Equation (12.1) shows the essential point: the rectifier can control the average DC voltage by changing $\alpha$, provided the source and operating conditions are suitable for line commutation [Rashid, *Power Electronics: Circuits, Devices and Applications*, 4e, Ch. 6], [Mohan, Undeland, Robbins, *Power Electronics: Converters, Applications and Design*, 3e, Ch. 6].

A **DC link** separates the system into two converter tasks. The generator-side stage extracts electrical power from the wind turbine generator, while the load-side or grid-side stage delivers power in the form required by the next part of the system. In practice, the DC link is often a capacitor-supported DC bus that electrically decouples these two functions.

The power transferred through that link is

$$\boxed{P_{DC} = V_{DC}I_{DC}} \quad \text{(12.2)}$$

where $V_{DC}$ is the DC-link voltage and $I_{DC}$ is the DC-link current. A controlled generator-side rectifier therefore influences the electrical condition seen by every downstream stage. Even when the final useful output is AC, the DC link is often the point at which variable generation is separated from controlled delivery.

**Image prompt for Figure 12.1:** Create a clean textbook-style technical illustration of a wind-energy power-conversion chain. Show, from left to right, wind turbine rotor, gearbox or direct-drive option, AC generator, generator-side rectifier block, DC-link capacitor and DC bus, grid-side inverter block, transformer, and utility grid. Add an alternate branch from the DC bus to a battery charger or DC load. Label the generator-side block as "front-end rectifier function" and the DC bus as "electrical decoupling stage." Use monochrome engineering style with clear arrows showing power flow.

#### A simple numerical example of front-end control

Suppose a wind-turbine generator, after suitable matching through a transformer, presents a three-phase supply of $V_{LL,rms} = 380 \text{ V}$ to a six-pulse controlled rectifier. Assume continuous current and ideal operation so that Equation (12.1) applies.

If the firing angle is $\alpha = 20^\circ$, then

$$V_{DC,avg} \approx 1.35 \times 380 \times \cos 20^\circ.$$

Since $\cos 20^\circ \approx 0.94$,

$$V_{DC,avg} \approx 1.35 \times 380 \times 0.94 \approx 482 \text{ V}.$$

Now suppose the wind changes and the effective rectifier-input voltage drops to $320 \text{ V}$ while the controller seeks to hold the DC link near $400 \text{ V}$. Using Equation (12.1),

$$400 = 1.35 \times 320 \times \cos\alpha.$$

So

$$\cos\alpha = \frac{400}{432} \approx 0.926.$$

Therefore,

$$\alpha \approx \cos^{-1}(0.926) \approx 22^\circ.$$

The example is idealized, but the control implication is clear: a controllable rectifier can help regulate the DC link against changes on the AC side. In an actual wind-energy system, the generator, turbine, and downstream converter are dynamically coupled, so the complete control problem is more involved.

#### Rectifier role in common wind-turbine topologies

Wind turbines do not all place the rectifier function in the same part of the electrical path. The location of the AC-DC stage determines how much of the turbine power passes through converters and how strongly the machine is coupled to the grid.

In older fixed-speed or nearly fixed-speed wind turbines, the generator may connect to the grid with relatively little power-electronic processing in the main power path. In such systems, a controlled rectifier is limited or absent as the principal front-end stage.

In a **doubly-fed induction generator (DFIG)** or Type 3 wind turbine, the stator is connected directly to the grid while the rotor is connected through a partial-size back-to-back AC-DC-AC converter [NREL Technical Report NREL/TP-5D00-59195]. The rectifier function is therefore present in the rotor-side converter, not in the full stator power path. This arrangement is closely related to slip power. With

$$\boxed{s = \frac{n_s - n_r}{n_s}} \quad \text{(12.3)}$$

where $n_s$ is synchronous speed and $n_r$ is rotor speed, a common rule-of-thumb is

$$\boxed{P_{conv} \approx |s|\,P_{ag}} \quad \text{(12.4)}$$

where $P_{conv}$ is converter-processed power and $P_{ag}$ is air-gap power. If the rotor operates only moderately away from synchronous speed, the converter processes only a fraction of total turbine power. NREL notes that Type 3 turbines commonly operate over about $\pm 30\%$ slip and that the converter is typically about $30\%$ of rated output power [NREL Technical Report NREL/TP-5D00-59195]. For a $2 \text{ MW}$ turbine operating at $|s| = 0.25$, the converter-handled power is roughly

$$P_{conv} \approx 0.25 \times 2 \text{ MW} = 0.5 \text{ MW}.$$

In a **full-converter** or Type 4 wind turbine, the entire generator output passes through an AC-DC-AC converter chain. The generator-side converter therefore performs the rectifier role for all generated power, not just a fraction. This arrangement is common in variable-speed designs using permanent-magnet synchronous generators and other machines that benefit from wide speed range and strong electrical controllability [Abu-Rub, Malinowski, Al-Haddad, *Power Electronics for Renewable Energy Systems, Transportation and Industrial Applications*], [NREL Technical Report NREL/TP-5D00-59195].

Table 12.1 summarizes the distinction.

Table 12.1: Rectifier role in common wind-turbine electrical topologies

| Topology | Main power path to grid | Where the rectifier function appears | Approximate converter share of total power |
| --- | --- | --- | --- |
| Fixed-speed turbine | Mostly direct AC connection | Limited or absent in main path | Low or none in main path |
| Type 3 DFIG | Stator direct to grid, rotor through converter | In the rotor-side back-to-back converter | Partial-scale, often around 30% [NREL Technical Report NREL/TP-5D00-59195] |
| Type 4 full-converter turbine | Entire output through converter | In the full generator-side converter | Full-scale |

The phrase "rectifier front end in wind energy" does not necessarily mean an SCR bridge tied directly to the turbine terminals. In many modern wind systems, the generator-side AC-DC stage is implemented with self-commutated PWM converters rather than line-commutated thyristor bridges. The system function, however, remains the same: generator-side AC is converted into a controlled DC link.

#### Why classical controlled rectifiers still matter

Controlled-rectifier theory remains relevant in wind-energy study for three reasons. First, it establishes the basic electrical role of the generator-side AC-DC interface. Second, line-commutated rectifiers are still useful wherever AC must be converted to DC at moderate or high power with simple and rugged control. Third, the limitations of SCR rectifiers help explain why later wind-converter topologies adopted self-commutated converters. A line-commutated SCR rectifier depends on the AC source for commutation, draws reactive power, and offers less independent control over current waveform and power factor than a modern PWM converter [Mohan, Undeland, Robbins, *Power Electronics: Converters, Applications and Design*, 3e], [NPTEL, *Line Commutated and PWM Rectifiers*].

### 3.3.2 HVDC transmission - introductory role of controlled rectifiers

#### HVDC link structure and renewable-energy relevance

Renewable-energy resources are often remote from major load centers. Offshore wind farms, distant hydro resources, and large wind or solar plants in sparsely populated regions may require long transmission corridors or submarine cables. In such cases, AC transmission is not always the best choice, and **HVDC** becomes important.

Classical HVDC systems consist of a sending-end converter station, a DC transmission path, and a receiving-end converter station. At the sending end, AC is converted to DC. At the receiving end, DC is converted back to AC. In line-commutated HVDC, the sending-end station performs the controlled-rectifier function by means of high-power thyristor valve groups, converter transformers, filters, smoothing reactors, and control equipment [Hitachi Energy, *HVDC converter stations*], [NPTEL, *HVDC converters*].

**Image prompt for Figure 12.2:** Create a clean textbook-style technical illustration of a classical HVDC transmission link. Show, from left to right, sending-end AC grid, converter transformer, thyristor-based controlled rectifier station, smoothing reactor, DC transmission line or submarine cable, thyristor-based receiving-end converter station operating as inverter, converter transformer, and receiving-end AC grid. Label AC filters, reactive power support, and control system blocks. Mark power flow from sending end to receiving end. Use monochrome engineering style with clear block labels.

HVDC is closely connected with renewable-energy systems because long-distance controllable transmission is often required to move power from the generation site to the main grid. Hitachi Energy describes HVDC Classic as a line-commutated technology used for remote generation, grid interconnection, and long-distance high-power transmission, while HVDC Light uses voltage-source converters in applications including wind-farm connections and compact converter stations [Hitachi Energy, *HVDC Classic (LCC)*], [Hitachi Energy, *HVDC Light (VSC)*].

#### Control of DC voltage and transmitted power

The same controlled-rectifier principle studied earlier appears in classical HVDC at much higher voltage and power levels. A concept-level expression for the ideal average DC voltage of a line-commutated converter is

$$\boxed{V_{DC} = V_{d0}\cos\alpha} \quad \text{(12.5)}$$

where $V_{DC}$ is the average DC output of the converter station, $V_{d0}$ is the ideal maximum average DC voltage at zero delay for that converter arrangement, and $\alpha$ is the firing delay angle. Once DC current is established, the transmitted power is approximately

$$\boxed{P_{DC} = V_{DC}I_{DC}} \quad \text{(12.6)}$$

where $I_{DC}$ is the DC-line current. Equations (12.5) and (12.6) show why the controlled rectifier is central to classical HVDC: by setting DC voltage and current, the converter station controls transmitted power [Hitachi Energy, *HVDC converter stations*].

Consider a simple numerical illustration in which a converter station operates around an ideal no-delay value of $V_{d0} = 500 \text{ kV}$.

If the firing angle is $\alpha = 15^\circ$, then

$$V_{DC} = 500\cos 15^\circ \approx 500 \times 0.966 \approx 483 \text{ kV}.$$

If the DC current is $I_{DC} = 2 \text{ kA}$, then

$$P_{DC} \approx 483 \text{ kV} \times 2 \text{ kA} = 966 \text{ MW}.$$

Now suppose the control system increases the firing angle to $\alpha = 30^\circ$. Then

$$V_{DC} = 500\cos 30^\circ \approx 500 \times 0.866 \approx 433 \text{ kV}.$$

At the same current,

$$P_{DC} \approx 433 \text{ kV} \times 2 \text{ kA} = 866 \text{ MW}.$$

The power falls by about $100 \text{ MW}$. Although the example is idealized, it captures the governing idea: in an HVDC rectifier station, firing-angle control changes the DC voltage that helps determine bulk power transfer.

#### Classical HVDC, inversion, and converter choice

Thyristors became dominant in classical HVDC because they can handle very large voltages and currents, are naturally suited to line-frequency commutation, and can be assembled into large valve structures by series and parallel combinations [Rashid, *Power Electronics: Circuits, Devices and Applications*, 4e], [Hitachi Energy, *HVDC converter stations*]. Practical stations also use more elaborate converter arrangements than a single textbook six-pulse bridge; twelve-pulse operation is common because transformer phase shifting reduces certain harmonics and improves overall performance [Mohan, Undeland, Robbins, *Power Electronics: Converters, Applications and Design*, 3e], [NPTEL, *HVDC converters*].

At the receiving end of a classical HVDC link, the converter station returns DC power to AC. The hardware remains based on controlled thyristor bridges, but the station operates in inversion mode rather than rectification mode. The same converter family can therefore serve as either a rectifier or an inverter, depending on operating conditions and control angles. For the present chapter, the essential point is that the sending station establishes DC voltage and power flow into the line, while the receiving station returns that power to the AC system.

The importance of this distinction for renewable-energy systems is clear. Classical HVDC demonstrates the large-scale application of controlled-rectifier theory, while many newer offshore-wind and compact-station projects use VSC technology instead of line-commutated SCR converters. Both technologies rely on controllable AC-DC conversion, but they differ in semiconductor type, commutation method, and control flexibility.

Table 12.2 provides a first comparison.

Table 12.2: Introductory comparison of HVDC technologies in renewable-energy context

| Feature | HVDC Classic (LCC) | HVDC Light (VSC) |
| --- | --- | --- |
| Main semiconductor tradition | Thyristor line-commutated valves | Self-commutated voltage-source converters |
| Controlled rectifier role | Central to classical operation | Replaced by controlled VSC switching |
| Typical use picture | Very high power, long distance, bulk transmission | Offshore wind, underground or underwater links, compact stations |
| Control character | Strong bulk-power control but depends on line commutation | Broader waveform and reactive-power control |
| Chapter relevance | Direct continuation of controlled-rectifier theory | Useful contrast showing why newer converters gained importance |

## Worked interpretation exercise

The NREL technical report *Simulation for Wind Turbine Generators - With FAST and MATLAB-Simulink Modules* includes a Type 3 wind-turbine connection diagram and a short description of its electrical structure [NREL Technical Report NREL/TP-5D00-59195]. Read as a power-electronics diagram, it shows three points immediately: the stator is connected directly to the grid, the rotor passes through a back-to-back AC/DC/AC converter, and the converter is partial-scale rather than full-scale. Together, those features identify the DFIG as a topology in which the rectifier function is present in the rotor circuit but does not process the entire turbine output.

The same diagram also highlights the practical importance of protection. A crowbar circuit is not an incidental detail; it indicates that converter-connected renewable systems must respond to grid disturbances and abnormal operating conditions as well as normal steady-state power flow.

Table 12.3 converts that diagram into a compact reading guide.

Table 12.3: How to read the NREL Type 3 wind-turbine connection diagram

| Artifact feature | What it tells you | Why it matters |
| --- | --- | --- |
| Stator connected directly to grid | Full turbine power does not all pass through converters | Reduces converter rating requirement |
| Rotor connected through back-to-back AC/DC/AC converter | The rotor circuit is actively controlled through a DC-link-based power-electronic interface | Enables variable-speed operation and control flexibility |
| Converter about 30% of rated output power | Converter is partial-scale rather than full-scale | Major economic and design advantage of DFIG topology |
| Crowbar protection shown or mentioned | Protection is necessary during grid disturbances | Real renewable converters must handle non-ideal conditions |

When reading any wind-energy converter diagram, three structural questions are usually sufficient: which path goes directly to the grid or load, which path passes through the rectifier and DC link, and how much of the total power the converter processes.

## Chapter summary

- Controlled rectifiers appear in renewable-energy systems as generator-side or transmission-side interfaces, not only as stand-alone converter circuits.
- In wind-energy systems, a front-end AC-DC stage commonly forms a DC link that separates variable generator behavior from controlled downstream delivery.
- For the ideal three-phase full-controlled bridge, the average DC output is $V_{DC,avg} \approx 1.35\,V_{LL,rms}\cos\alpha$.
- Wind-turbine topologies differ in where the rectifier function appears: it may be absent from the main path, embedded in a partial-scale DFIG rotor converter, or used in a full-scale generator-side converter.
- Controlled-rectifier theory remains useful even when modern wind turbines use PWM converters, because it clarifies the AC-DC interface role and the limitations of line-commutated operation.
- In classical HVDC, firing-angle control at the sending-end converter station sets the DC voltage that helps determine transmitted power.
- HVDC applies controlled AC-DC conversion to long-distance renewable-power transfer, while modern VSC-based links provide a contrasting converter approach.

## Further reading

- H. Abu-Rub, M. Malinowski, and K. Al-Haddad, *Power Electronics for Renewable Energy Systems, Transportation and Industrial Applications* - A strong bridge between converter theory and renewable-energy applications, especially useful for seeing how wind, storage, and grid interfaces fit together.
- Ned Mohan, Tore M. Undeland, and William P. Robbins, *Power Electronics: Converters, Applications and Design*, 3rd ed. - A reliable text for the controlled-rectifier foundations that later scale into system applications such as HVDC.
- [NREL, *Simulation for Wind Turbine Generators - With FAST and MATLAB-Simulink Modules*](https://docs.nrel.gov/docs/fy14osti/59195.pdf) - Useful for real wind-turbine electrical topologies, especially the Type 3 DFIG and Type 4 full-converter connection diagrams.
- [Hitachi Energy, *HVDC Classic (LCC)*](https://www.hitachienergy.com/us/en/products-and-solutions/hvdc/hvdc-classic) - A concise official overview of classical line-commutated HVDC and its high-power long-distance transmission role.
- [Hitachi Energy, *HVDC Light (VSC)*](https://www.hitachienergy.com/us/en/products-and-solutions/hvdc/hvdc-light) - Useful as a contrast source showing how modern VSC-based HVDC is used in applications such as offshore wind connections.
