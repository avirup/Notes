**West Bengal State Council of Technical & Vocational Education and Skill Development**

**TEACHING AND EXAMINATION SCHEME FOR DIPLOMA COURSES**

**COURSE NAME: RENEWABLE ENERGY ENGINEERING \| COURSE CODE: REE \| DURATION: 6 SEMESTERS**

**PROGRAM ELECTIVE — DETAILED SYLLABUS**

|                          |                           |
|--------------------------|---------------------------|
| **Semester**             | V / VI (Program Elective) |
| **Course Code**          | REEPE                     |
| **Course Title**         | Power Electronics         |
| **Number of Credits**    | 3 (L-3; T-0; P-0)         |
| **Total Teaching Hours** | 45 Hours (Theory)         |
| **Course Category**      | Program Elective (PE)     |

**Prerequisite**

The student is expected to have the following background knowledge before undertaking this course. This course builds on these topics and does not revisit signal-level transistor theory in depth.

| **Sl. No.** | **Prerequisite Subject / Area**        | **Specific Topics Expected to be Known**                                                                                                         |
|-------------|----------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------|
| 1           | Basic Electronics / Electronic Devices | PN junction diode, Zener diode, BJT and FET construction & basic operation, transistor as a switch, operation in cut-off and saturation regions. |
| 2           | Basic Electrical Engineering           | DC and AC circuit fundamentals, RMS and average values, series & parallel R-L-C circuits, single-phase and three-phase systems, power factor.    |
| 3           | Network Analysis / Circuit Theory      | Kirchhoff's laws, Thevenin & Norton equivalents, response of R-L and R-C circuits to step inputs, transient behaviour.                           |
| 4           | Fundamentals of Renewable Energy       | Basic concept of solar PV, wind energy, and battery energy storage systems — required to contextualise converter applications.                   |

**Course Objectives**

1\. To provide knowledge of the construction, operating principles, characteristics and ratings of modern power semiconductor devices used in renewable-energy converters.

2\. To develop the ability to select appropriate gate-drive, snubber, protection and thermal-management circuits for power electronic switches.

3\. To impart understanding of AC-DC, DC-DC, DC-AC and AC-AC converter topologies relevant to solar photovoltaic, wind, battery-storage and electric-vehicle systems.

4\. To introduce modern converter topologies such as isolated and bidirectional DC-DC converters, PWM inverters, multilevel inverters and grid-interactive inverters.

5\. To develop an appreciation of power-quality issues and filter design in the grid integration of renewable energy sources.

**Module-wise Distribution of Teaching Hours**

| **Module** | **Title**                                                       | **Teaching Hours** |
|------------|-----------------------------------------------------------------|--------------------|
| 1          | Power Semiconductor Devices                                     | 10                 |
| 2          | Device Protection, Gate Drive & Thermal Management              | 05                 |
| 3          | AC to DC Converters (Controlled Rectifiers)                     | 07                 |
| 4          | DC to DC Converters                                             | 10                 |
| 5          | DC to AC Converters (Inverters)                                 | 08                 |
| 6          | AC to AC Converters & Power Quality in Renewable Energy Systems | 05                 |
|            | **Total**                                                       | **45**             |

**Course Contents (Theory)**

**Module 1 — Power Semiconductor Devices**

*(10 Teaching Hours)*

**1.1 Power BJT**

> 1.1.1 History of Power BJT.
>
> 1.1.2 Structure, quasi-saturation, safe operating area (SOA).
>
> 1.1.3 Switching characteristics and specifications.

**1.2 Thyristor (SCR)**

> 1.2.1 History of Thyristor (SCR).
>
> 1.2.2 Construction, two-transistor analogy, operating principle.
>
> 1.2.3 Static V-I characteristics: latching current, holding current, break-over voltage, forward and reverse blocking.
>
> 1.2.4 Turn-ON methods (gate triggering, dv/dt, thermal, light, forward-voltage).
>
> 1.2.5 Turn-OFF and commutation methods: natural (line) commutation and forced commutation (Class A to E — concept level).
>
> 1.2.6 Gate-triggering circuits: R, R-C and UJT-based triggering (overview).
>
> 1.2.7 SCR ratings and specifications; di/dt and dv/dt protection.

**1.3 DIAC and TRIAC**

> 1.3.1 History of DIAC and TRIAC.
>
> 1.3.2 Construction, operating principle, V-I characteristics.
>
> 1.3.3 Modes of operation of TRIAC; DIAC-TRIAC based phase control (concept).
>
> 1.3.4 Applications: light dimmers, fan regulators, small AC loads.

**1.4 Power MOSFET**

> 1.4.1 History of Power MOSFET.
>
> 1.4.2 Vertical (V-DMOS) structure, operation, output and transfer characteristics.
>
> 1.4.3 Switching behaviour, body diode, specifications.

**1.5 IGBT**

> 1.5.1 History of IGBT.
>
> 1.5.2 Structure, operating principle, output and transfer characteristics.
>
> 1.5.3 Switching characteristics, latch-up, SOA.
>
> 1.5.4 Comparison of Power BJT, Power MOSFET and IGBT — selection for solar, wind and EV converters.

**Module 2 — Device Protection, Gate Drive & Thermal Management**

*(5 Teaching Hours)*

**2.1 Gate / Base Drive Circuits**

> 2.1.1 Requirements of a good drive circuit.
>
> 2.1.2 MOSFET and IGBT gate driver basics — totem-pole driver, dedicated driver ICs (block-level understanding).
>
> 2.1.3 Isolated gate drive: opto-coupler and pulse-transformer based isolation; high-side and low-side driver concept.

**2.2 Snubber Circuits**

> 2.2.1 Need for snubbers; turn-ON and turn-OFF snubbers.
>
> 2.2.2 RC and RCD snubber circuits; freewheeling diode.

**2.3 Overvoltage and Overcurrent Protection**

> 2.3.1 Overvoltage protection: MOV, TVS diodes, crowbar circuits.
>
> 2.3.2 Overcurrent protection: fast-acting (HRC) fuses, electronic current limiting, desaturation detection (concept).

**2.4 Thermal Management**

> 2.4.1 Power losses in semiconductor devices: conduction and switching losses (qualitative).
>
> 2.4.2 Thermal resistance, heat-sink selection — simple design approach.
>
> 2.4.3 Forced cooling — overview.

**Module 3 — AC to DC Converters (Controlled Rectifiers)**

*(7 Teaching Hours)*

**3.1 Single-phase Controlled Rectifiers**

> 3.1.1 Single-phase half-wave controlled rectifier with R and R-L loads; effect of freewheeling diode.
>
> 3.1.2 Single-phase full-wave fully controlled bridge rectifier with R and R-L loads.
>
> 3.1.3 Single-phase semi-controlled (half-controlled) bridge rectifier — concept.
>
> 3.1.4 Expressions for average and RMS output voltage; effect of firing angle.

**3.2 Three-phase Controlled Rectifiers**

> 3.2.1 Three-phase half-wave controlled rectifier (overview).
>
> 3.2.2 Three-phase fully controlled bridge rectifier with R-L load; continuous conduction.
>
> 3.2.3 Average output voltage expression; effect of firing angle on DC output.

**3.3 Applications in Renewable Energy Systems**

> 3.3.1 Controlled rectifiers as front-end stages in wind-energy conversion systems.
>
> 3.3.2 HVDC transmission — introductory role of controlled rectifiers.

**Module 4 — DC to DC Converters**

*(10 Teaching Hours)*

**4.1 Fundamentals of DC Choppers**

> 4.1.1 Principle of chopper operation; duty cycle.
>
> 4.1.2 Control strategies: Time-Ratio Control (constant-frequency and variable-frequency), Current-Limit Control.
>
> 4.1.3 Classification of choppers: Type-A, B, C, D and E — operating principle, output waveforms, applications.

**4.2 Non-isolated DC-DC Converters**

> 4.2.1 Buck (step-down) converter — circuit, operation in CCM, voltage gain.
>
> 4.2.2 Boost (step-up) converter — circuit, operation in CCM, voltage gain.
>
> 4.2.3 Buck-Boost converter — circuit, operation, voltage gain, polarity inversion.
>
> 4.2.4 Cuk converter — circuit, operation, voltage gain, advantages (continuous input and output current).
>
> 4.2.5 SEPIC converter — circuit, operation, applications in PV systems.

**4.3 Isolated DC-DC Converters (Overview)**

> 4.3.1 Need for galvanic isolation in renewable-energy and battery-charging systems.
>
> 4.3.2 Flyback converter — topology and applications.
>
> 4.3.3 Forward converter — topology and applications.
>
> 4.3.4 Push-Pull, Half-Bridge and Full-Bridge isolated converters — topology-level comparison (no detailed analysis).

**4.4 Bidirectional DC-DC Converters**

> 4.4.1 Concept and need for bidirectional power flow — battery charging/discharging, EV regenerative braking.
>
> 4.4.2 Bidirectional buck-boost converter — topology and operation (conceptual).

**4.5 Applications in Renewable Energy**

> 4.5.1 Maximum Power Point Tracking (MPPT): concept, P-V curve of solar panels, need for MPPT.
>
> 4.5.2 Overview of MPPT techniques: Perturb & Observe (P&O) and Incremental Conductance (algorithm-level understanding).
>
> 4.5.3 Selection of DC-DC converter topology for solar PV, battery charging and EV drivetrain applications.

**Module 5 — DC to AC Converters (Inverters)**

*(8 Teaching Hours)*

**5.1 Classification and Basic Topologies**

> 5.1.1 Classification of inverters: voltage-source vs current-source; line-commutated vs self-commutated; single-phase vs three-phase.
>
> 5.1.2 Single-phase half-bridge voltage-source inverter with R and R-L loads.
>
> 5.1.3 Single-phase full-bridge voltage-source inverter with R and R-L loads.

**5.2 Three-phase Inverters**

> 5.2.1 Three-phase bridge inverter — 180° conduction mode; phase and line voltage waveforms.
>
> 5.2.2 Three-phase bridge inverter — 120° conduction mode; comparison with 180° mode.

**5.3 Pulse-Width Modulation (PWM) Techniques**

> 5.3.1 Single-pulse-width modulation.
>
> 5.3.2 Multiple-pulse-width modulation.
>
> 5.3.3 Sinusoidal PWM (SPWM) — principle, modulation index, harmonic content.
>
> 5.3.4 Introduction to Space-Vector PWM (concept only).

**5.4 Multilevel Inverters (Introduction)**

> 5.4.1 Need for multilevel inverters in medium- and high-voltage renewable-energy applications.
>
> 5.4.2 Diode-clamped (neutral-point-clamped) multilevel inverter — three-level topology.
>
> 5.4.3 Cascaded H-bridge multilevel inverter — basic topology and advantages in solar PV.

**5.5 Grid-Interactive Inverters**

> 5.5.1 Block diagram of a grid-tie inverter; stand-alone vs grid-connected operation.
>
> 5.5.2 Grid synchronization — basic requirements (voltage, frequency, phase).
>
> 5.5.3 Anti-islanding protection — concept and importance.
>
> 5.5.4 Solar PV inverter topologies (overview): central, string and micro-inverters.
>
> 5.5.5 Role of inverters in wind-energy conversion systems — DFIG and PMSG-based systems (block-level overview).

**Module 6 — AC to AC Converters & Power Quality in Renewable Energy Systems**

*(5 Teaching Hours)*

**6.1 AC Voltage Controllers**

> 6.1.1 Principle of phase-angle control and integral-cycle (ON-OFF) control.
>
> 6.1.2 Single-phase AC voltage controller with R and R-L loads — waveforms.
>
> 6.1.3 Applications: soft-starters, induction-heating control, lighting control.

**6.2 Cycloconverters**

> 6.2.1 Principle of operation of a cycloconverter.
>
> 6.2.2 Single-phase to single-phase cycloconverter — circuit, waveforms.
>
> 6.2.3 Three-phase cycloconverter — block-level overview.
>
> 6.2.4 Applications: low-speed large drives, wind-turbine drives.

**6.3 Power Quality in Power-Electronic Systems**

> 6.3.1 Power quality issues: harmonics, voltage sag/swell, flicker — causes and effects.
>
> 6.3.2 Total Harmonic Distortion (THD) — definition, importance for grid connection.
>
> 6.3.3 IEEE 519 / relevant Indian standards — awareness level.

**6.4 Filters for Grid Integration of Renewable Energy Sources**

> 6.4.1 Need for filtering at inverter output.
>
> 6.4.2 L, LC and LCL filters — circuit topology, qualitative behaviour, comparison.
>
> 6.4.3 Selection of filter for grid-tie inverter applications.

**Text / Reference Books**

| **Sl. No.** | **Title of Book**                                                                          | **Author(s)**                            | **Publisher**                          |
|-------------|--------------------------------------------------------------------------------------------|------------------------------------------|----------------------------------------|
| 1           | Power Electronics                                                                          | M. D. Singh, K. B. Khanchandani          | Tata McGraw-Hill                       |
| 2           | Power Electronics: Circuits, Devices and Applications                                      | M. H. Rashid                             | Pearson / PHI                          |
| 3           | Power Electronics: Converters, Applications and Design                                     | Ned Mohan, T. M. Undeland, W. P. Robbins | Wiley India                            |
| 4           | Power Electronics                                                                          | P. S. Bimbhra                            | Khanna Publishers                      |
| 5           | Power Electronics                                                                          | S. N. Singh                              | Dhanpat Rai Publications               |
| 6           | Power Electronics                                                                          | S. K. Mondal                             | Tata McGraw-Hill                       |
| 7           | Power Electronics for Renewable Energy Systems, Transportation and Industrial Applications | H. Abu-Rub, M. Malinowski, K. Al-Haddad  | Wiley-IEEE Press                       |
| 8           | Power Electronics for Renewable Energy Systems                                             | R. Seyezhai, R. Ramaprabha               | SciTech Publications (India) Pvt. Ltd. |
| 9           | First Course on Power Electronics and Drives                                               | Ned Mohan                                | Wiley India                            |

**Online Learning Resources**

| **Sl. No.** | **Course / Resource**                                      | **Platform / Source** |
|-------------|------------------------------------------------------------|-----------------------|
| 1           | Power Electronics — Prof. G. Bhuvaneswari, IIT Delhi       | NPTEL / SWAYAM        |
| 2           | Power Electronics — Prof. L. Umanand, IISc Bangalore       | NPTEL / SWAYAM        |
| 3           | Fundamentals of Power Electronics — Prof. V. Ramanarayanan | NPTEL                 |
| 4           | Power Electronics in Renewable Energy Systems              | NPTEL / SWAYAM        |

**Course Outcomes (COs)**

| **CO No.** | **After completing the course, the student will be able to:**                                                                                                                                                  | **Bloom's Level** |
|------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------|
| **CO1**    | Describe the construction, operating principle and V-I characteristics of power semiconductor devices (SCR, TRIAC, Power BJT, Power MOSFET, IGBT) and compare their ratings for renewable-energy applications. | L2 — Understand   |
| **CO2**    | Select appropriate gate-drive, snubber, protection and thermal-management schemes for power electronic switches used in solar and wind converters.                                                             | L3 — Apply        |
| **CO3**    | Analyze the operation and output waveforms of single-phase and three-phase controlled rectifiers with R and R-L loads, with and without freewheeling diode.                                                    | L4 — Analyze      |
| **CO4**    | Apply non-isolated (Buck, Boost, Buck-Boost, Cuk, SEPIC), isolated (Flyback, Forward, Push-Pull, Bridge) and bidirectional DC-DC converter topologies to solar PV MPPT, battery charging and EV applications.  | L3 — Apply        |
| **CO5**    | Analyze the operation of single-phase, three-phase, PWM and multilevel inverters and explain the role of grid-interactive inverters in solar PV and wind energy conversion systems.                            | L4 — Analyze      |
| **CO6**    | Interpret power-quality issues (harmonics, THD) arising in power-electronic systems and evaluate suitable passive filters (L, LC, LCL) for grid integration of renewable energy sources.                       | L5 — Evaluate     |

**Notes for the Teacher**

*1. All device-level discussions (Module 1 & 2) should emphasise the switching behaviour and application fitness for renewable-energy converters, rather than small-signal amplifier behaviour.*

*2. Mathematical treatment of converters should be limited to waveform derivation and average / RMS expressions; detailed design-oriented derivations are outside the diploma scope.*

*3. Application examples should, wherever possible, be drawn from solar PV, wind, battery-storage and EV systems to align with the REE program learning outcomes.*

*4. Module 4 is the most content-heavy; the teacher is advised to use block diagrams and waveform sketches rather than extensive algebraic derivations.*

*5. Laboratory experiments covering the above topics are addressed in the corresponding Power Electronics Laboratory syllabus (separate document).*
