# Chapter 4.4: Bidirectional DC-DC Converters

## Chapter opening

Previous chapters introduced DC-DC converters that regulate one voltage level from another and usually transfer power in one preferred direction. Many practical systems, however, contain storage elements or coupled DC buses that must exchange energy in both directions. A battery is charged in one interval and discharged in another. A storage unit beside a renewable source absorbs surplus energy and later returns it to the bus. In an electric vehicle, energy flows from the battery during acceleration and back toward the battery during regenerative braking [DOE FEMP, *Electric Vehicle Technology Overview*].

A **bidirectional DC-DC converter** is designed for this reversible average power flow. The same hardware may act as a charger in one operating condition and as a source interface in another. This chapter introduces the need for bidirectional power flow and then develops the conceptual operation of the **bidirectional buck-boost converter**, a widely used non-isolated topology for battery and storage interfaces [Mohan, Undeland, Robbins, *Power Electronics: Converters, Applications, and Design*, 3e], [NPTEL, *Multi Quadrant DC-DC Converters I*].

## Prerequisites check

- Recall the duty-cycle concept from Chapter 4.1 and the basic buck and boost relations from Chapter 4.2.
- Recall the quadrant classification of choppers, especially the relation between voltage sign, current sign, and power flow.
- Recall that an inductor stores energy temporarily and resists sudden change of current.
- Treat ideal converter equations as first models. Real circuits include losses, current limits, and control constraints.

## Core content

### 4.4.1 Concept and need for bidirectional power flow - battery charging/discharging, EV regenerative braking

#### Why one-way conversion is sometimes not enough

Consider a $48 \text{ V}$ DC bus connected to a $24 \text{ V}$ battery bank. When excess solar power is available, the bus may charge the battery. Later, when solar power falls or the load rises, the battery may support the same bus.

A strictly unidirectional converter can perform only one of these functions:

- bus-to-battery charging, or
- battery-to-bus discharging.

Supporting both functions therefore requires either two separate converters or one converter whose average power flow can reverse. The second approach is often more economical in components and more coherent in control, especially when the two operating modes occur regularly [Rashid, *Power Electronics: Circuits, Devices and Applications*, 4e], [Mohan, Undeland, Robbins, *Power Electronics: Converters, Applications, and Design*, 3e].

#### What "bidirectional" really means

For a converter port, instantaneous power is

$$\boxed{p(t) = v(t)i(t)} \quad \text{(16.1)}$$

where $v(t)$ is the instantaneous voltage and $i(t)$ is the instantaneous current at that port.

For DC ports, the average power over a switching interval or over a longer interval is often approximated by

$$\boxed{P \approx VI} \quad \text{(16.2)}$$

where $V$ and $I$ are average port voltage and average port current.

A bidirectional DC-DC converter is therefore a converter whose **average power** can flow from Port A to Port B or from Port B to Port A, according to switching commands and system conditions.

In many practical battery interfaces, both port voltages remain positive with respect to a common reference. Power reverses because current reverses through the controlled switch-inductor network. Bidirectional operation should therefore not be identified with reversal of voltage polarity. In many systems it simply means that the same two positive-voltage DC ports can exchange energy in either direction [NPTEL, *Multi Quadrant DC-DC Converters I*].

#### A first numerical picture

Let a $48 \text{ V}$ bus exchange power with a $24 \text{ V}$ battery. Assume, for a first estimate, that the converter is lossless.

If the battery is charging at

$$24 \text{ V} \times 10 \text{ A} = 240 \text{ W},$$

then the $48 \text{ V}$ bus must supply approximately

$$I_H = \frac{240}{48} = 5 \text{ A}.$$

In charging mode:

- battery side: $24 \text{ V}, 10 \text{ A}$ into the battery
- bus side: $48 \text{ V}, 5 \text{ A}$ from the bus

Now reverse the power flow while keeping the same ideal power level of $240 \text{ W}$. The bus still receives

$$I_H = \frac{240}{48} = 5 \text{ A},$$

while the battery side provides

$$I_L = \frac{240}{24} = 10 \text{ A}.$$

The voltage levels are unchanged, but the direction of power has reversed. This is the essential operating idea of a bidirectional converter.

#### Batteries and reversible operation

A battery naturally operates in two energy directions. During **charging**, electrical energy is absorbed and stored chemically. During **discharging**, stored chemical energy returns as electrical output [Abu-Rub, Malinowski, Al-Haddad, *Power Electronics for Renewable Energy Systems, Transportation and Industrial Applications*].

The converter connected to a battery must therefore do more than regulate a voltage ratio. It must also manage current direction, current magnitude, and mode transition. In charging mode, the converter may have to enforce current limits and voltage limits required by the battery. In discharge mode, it may instead regulate a DC bus, support a load, or share power with other sources [TI, BQ25756 product page].

This pattern appears across many systems:

- a PV-plus-battery installation charges the battery in daytime and discharges it after sunset
- a UPS battery charges during normal supply and discharges during outage
- a DC microgrid battery alternately absorbs and supplies power to stabilize a common bus
- a portable power station charges from an adaptor or solar source and later powers external loads

#### Connection to earlier quadrant classification

The quadrant classification introduced in Chapter 4.1 is useful here. In many battery interfaces, the two port voltages remain positive, but current and power may reverse. The chapter can therefore be read as an application of the same sign conventions already used for multi-quadrant chopper operation [Singh and Khanchandani, *Power Electronics*], [NPTEL, *Multi Quadrant DC-DC Converters I*].

Table 16.1 summarizes the distinction between one-way and two-way conversion.

Table 16.1: Unidirectional and bidirectional DC-DC conversion at a glance

| Feature | Unidirectional converter | Bidirectional converter |
| --- | --- | --- |
| Average power flow | One preferred direction only | Either direction as commanded |
| Typical role | Simple supply regulator, fixed charger, fixed load interface | Battery charging/discharging, supercapacitor backup, regenerative systems |
| Need for active switches in both directions | Usually not | Usually yes |
| Control task | Regulate voltage or current in one main direction | Regulate voltage or current while also managing flow direction |
| Typical example | Ordinary buck regulator from 48 V to 12 V | 48 V to 12 V dual-battery interface, battery-to-bus storage stage |

#### EV regenerative braking

Electric vehicles provide a clear example of reversible power flow. During acceleration, the battery supplies electrical energy to the traction system. During **regenerative braking**, the machine is driven mechanically by the moving vehicle and acts as a generator. Part of the vehicle's kinetic energy is then returned electrically toward the battery [DOE FEMP, *Electric Vehicle Technology Overview*].

The full traction system includes an inverter and machine, and some architectures also include a separate DC-DC stage for storage or bus coupling. The underlying principle remains the same: power electronics must permit controlled reversal of power flow. Regenerative braking does not recover all of the vehicle's kinetic energy; machine losses, converter losses, battery acceptance limits, and braking conditions all reduce the recovered fraction [DOE FEMP, *Electric Vehicle Technology Overview*].

#### Another useful application: supercapacitor backup

The same principle appears in supercapacitor backup systems. Analog Devices describes the LTC3110 as a bidirectional buck-boost regulator that charges a supercapacitor when the bus is present and discharges the supercapacitor into the load when the bus fails [Analog Devices, *Bidirectional DC/DC Regulator and Supercapacitor Charger*].

The storage element is different, but the operating logic is the same:

- normal condition: energy moves from the bus to the storage element
- backup condition: energy moves from the storage element to the bus

#### Common misconceptions

One misconception is that a bidirectional converter must reverse output-voltage polarity. In many practical systems, both DC-port voltages remain positive while current and average power reverse.

Another misconception is that bidirectional conversion means simultaneous power transfer in both directions. In normal operation, the converter is commanded to transfer net average power in one direction at a time, although direction may change when system conditions change.

A third misconception is that battery charging and battery discharging are the same control problem with arrows reversed. The same hardware may be used in both modes, but the control objective often changes with direction.

### 4.4.2 Bidirectional buck-boost converter - topology and operation (conceptual)

#### The basic physical idea

Among non-isolated bidirectional converters, one widely used arrangement is the **bidirectional buck-boost converter**. In modern implementations, this often appears as a **four-switch synchronous buck-boost converter** with one inductor between two actively switched half-bridges [TI, BQ25756 product page], [Analog Devices, LTC3871 product brief].

Its conceptual structure is simple:

- one port is the higher-voltage side, $V_H$
- the other port is the lower-voltage side, $V_L$
- an inductor lies between the switching networks connected to the two ports
- active switching determines the direction and magnitude of inductor current

Unlike a diode-based unidirectional buck or boost converter, current paths are not fixed by passive diode direction alone. Because both sides use controllable switches, the same hardware can support power flow from high to low or from low to high.

**Image prompt for Figure 16.1:** Create a clean textbook-style technical illustration of a non-isolated four-switch bidirectional buck-boost converter. Show a high-voltage port labeled $V_H$, a low-voltage battery port labeled $V_L$, two half-bridges made of switches $S_1$-$S_4$, and a single inductor $L$ between the two bridge midpoints. Add an arrow for positive inductor current from the high-voltage side toward the low-voltage side, and a second arrow showing reversible current direction. Mark charging mode as $V_H \rightarrow V_L$ and discharging mode as $V_L \rightarrow V_H$. Use monochrome engineering style with clear component labels.

#### Why active switches make reversal possible

In a basic unidirectional buck converter, a diode provides a freewheeling path. In a basic unidirectional boost converter, a diode prevents reverse discharge of the output capacitor into the source. Those features are useful when one-way power transfer is desired.

For bidirectional transfer, however, the same diode behavior becomes restrictive. A diode that blocks reverse current in one operating direction also blocks the reverse energy transfer required in the other direction. Bidirectional converters therefore replace passive one-way rectifier paths with **synchronous switches**, usually MOSFETs. By selecting which devices conduct and when, the controller can create a buck-like transfer from the high side to the low side or a boost-like transfer from the low side to the high side.

#### Mode 1: charging the lower-voltage battery from a higher-voltage bus

When a higher-voltage DC bus charges a lower-voltage battery, the converter operates in the **buck direction**.

Consider a $48 \text{ V}$ bus charging a $24 \text{ V}$ battery. In broad terms, operation may be described in two intervals.

During the first interval:

- the switching network connects the high-voltage side to the inductor
- the inductor sees a positive voltage
- inductor current rises
- energy is taken from the high-voltage bus

During the second interval:

- the switching state changes to a synchronous freewheeling path
- inductor current continues toward the low-voltage side
- the inductor current falls more gradually
- energy continues into the battery

The inductor smooths current, and the switching pattern determines the average power delivered to the battery.

#### Ideal buck-direction voltage relation

In the same ideal form used for the ordinary buck converter, the charging direction follows approximately

$$\boxed{V_L = D\,V_H} \quad \text{(16.3)}$$

where:

- $V_H$ is the higher-voltage port
- $V_L$ is the lower-voltage port
- $D$ is the duty cycle referred to the buck-direction switching interval

This is a first-order conceptual relation. Practical implementations include multiple switching states, nonideal drops, current limits, and control constraints.

#### A numerical example in charging mode

Suppose a storage converter must charge a $24 \text{ V}$ battery from a $48 \text{ V}$ DC bus. Under the ideal buck relation of Equation (16.3),

$$D = \frac{V_L}{V_H} = \frac{24}{48} = 0.5.$$

If the battery is charged at $8 \text{ A}$, then the battery-side power is approximately

$$P_L = 24 \times 8 = 192 \text{ W}.$$

Ignoring losses, the high-side current is then

$$I_H = \frac{192}{48} = 4 \text{ A}.$$

The lower-voltage side therefore carries the larger current for the same power level.

#### Mode 2: supporting the higher-voltage bus from the lower-voltage battery

When the battery supports the higher-voltage bus, power flows from the low-voltage port toward the high-voltage port. The converter now behaves conceptually as a **boost converter**.

Again the operation may be viewed in two intervals.

During the first interval:

- the low-voltage side charges the inductor
- inductor current rises
- energy is stored in the magnetic field

During the second interval:

- the switching state changes
- the inductor forces its current to continue
- the inductor voltage adds appropriately to the battery-side voltage
- energy is delivered to the higher-voltage bus

The operating idea is the same as in an ordinary boost converter, but the hardware is arranged so that the direction can later reverse again when required.

#### Ideal boost-direction voltage relation

In the ideal conceptual model for the reverse direction,

$$\boxed{V_H = \frac{V_L}{1-D}} \quad \text{(16.4)}$$

where $D$ is interpreted with respect to the boost-direction switching interval.

Equation (16.4) shows why the same converter can raise the bus voltage above the battery voltage when the battery is the source side.

#### A numerical example in discharging mode

Suppose a $24 \text{ V}$ battery must support a $48 \text{ V}$ bus during a backup interval. Using Equation (16.4),

$$48 = \frac{24}{1-D}.$$

So

$$1-D = \frac{24}{48} = 0.5,$$

and therefore

$$D = 0.5.$$

If the bus requires $240 \text{ W}$ ideally, then

$$I_H = \frac{240}{48} = 5 \text{ A}$$

at the high-voltage side, while the battery must supply approximately

$$I_L = \frac{240}{24} = 10 \text{ A}.$$

Once again, the lower-voltage side carries the larger current. This is a major design consideration for conductors, inductor current rating, switch current rating, sensing, and thermal performance.

#### Ideal power balance

For a lossless converter, input power equals output power. As a first approximation,

$$\boxed{V_H I_H \approx V_L I_L} \quad \text{(16.5)}$$

This relation explains why the lower-voltage side often experiences the highest current stress in both charging and discharging operation.

#### A practical comparison of the two directions

Table 16.2 summarizes the same hardware in its two main conceptual roles.

Table 16.2: Bidirectional buck-boost converter viewed in each power-flow direction

| Operating direction | Energy flow | Converter behaves like | Useful first equation | Typical example |
| --- | --- | --- | --- | --- |
| High side to low side | $V_H \rightarrow V_L$ | Buck converter | $V_L = D V_H$ | Charging a lower-voltage battery from a DC bus |
| Low side to high side | $V_L \rightarrow V_H$ | Boost converter | $V_H = \dfrac{V_L}{1-D}$ | Battery supporting a higher-voltage DC bus |

#### Why this converter is attractive in real systems

The bidirectional buck-boost converter is widely used because one stage can perform several important functions:

- charge a storage element from a bus
- allow the same storage element to support that bus later
- connect ports with unequal voltage levels
- regulate current as well as voltage
- use one inductor rather than separate buck and boost magnetics in many implementations

Such converters appear in battery chargers, portable power systems, 48 V/12 V automotive systems, supercapacitor backup supplies, and renewable-energy storage interfaces. Analog Devices describes the LTC3871 as a bidirectional buck or boost controller for 48 V/12 V dual-battery systems [Analog Devices, LTC3871 product brief]. TI describes the BQ25756 as a wide-input bidirectional buck-boost battery charge controller with reverse mode and solar MPPT support [TI, BQ25756 product page].

#### Control considerations at concept level

Although this chapter does not develop full controller design, several practical ideas are essential.

First, **current control** is usually an important inner function, because current direction and current magnitude must be limited in both modes.

Second, the controller must prevent **shoot-through**. If both switches in the same half-bridge turn ON simultaneously, a destructive short circuit can occur. Dead time and proper gate-drive sequencing are therefore required.

Third, the control objective changes with operating mode:

- in charging mode, the converter may follow constant-current and then constant-voltage charging behavior
- in discharge mode, it may regulate the DC-bus voltage or a commanded output current

Fourth, direction reversal must be managed deliberately. The controller has to sense voltages and currents, decide when the operating condition has changed, and transition without large current spikes.

**Image prompt for Figure 16.2:** Create a clean textbook-style technical illustration showing the two conceptual operating modes of a four-switch bidirectional buck-boost converter. In the left panel, label "Charging / Buck Mode" and show energy flowing from a higher-voltage DC bus $V_H$ through the inductor into a lower-voltage battery $V_L$, with a note $V_L = D V_H$. In the right panel, label "Discharging / Boost Mode" and show energy flowing from the lower-voltage battery through the inductor into the higher-voltage DC bus, with a note $V_H = V_L/(1-D)$. Add simplified inductor-current waveforms in both panels, clear current-direction arrows, and monochrome engineering styling.

#### What this topology does not automatically solve

A bidirectional buck-boost converter does not automatically provide galvanic isolation. If safety requirements or grounding constraints require isolation, an isolated bidirectional topology is needed instead.

It also does not make battery charging safe by itself. Proper charge limits, thermal limits, and battery-management logic remain necessary.

Finally, it does not eliminate ripple, EMI, switching loss, or thermal stress. These remain important in both directions of operation, especially on the lower-voltage side where current is often highest.

#### Common misconceptions

One misconception is that the bidirectional buck-boost converter is merely a buck converter and a boost converter placed in series, with no added control difficulty. Buck and boost action are indeed its conceptual foundation, but coordinated switching, reverse-current control, protection, and mode transition make the practical implementation more demanding.

Another misconception is that one duty-ratio equation can be used carelessly without specifying the operating direction. The appropriate relation depends on which side is acting as the source and which side is acting as the receiving port.

A third misconception is that a bidirectional converter requires both connected systems to behave bidirectionally. In practice, one side may be a bus that usually acts as a source, while the other is a storage element that alternates between absorbing and delivering power.

## Worked interpretation exercise

### Reading a real bidirectional buck-boost product page

The [TI BQ25756 product page](https://www.ti.com/product/BQ25756) is a useful industrial example because it describes the device explicitly as a **70-V bidirectional buck-boost charge controller with MPPT** [TI, BQ25756 product page].

Several product-page statements connect directly to the chapter concepts:

- wide input voltage operating range: $4.2 \text{ V}$ to $70 \text{ V}$
- wide battery voltage operating range: up to $70 \text{ V}$
- synchronous buck-boost charge controller with NFET drivers
- adjustable switching frequency from $200 \text{ kHz}$ to $600 \text{ kHz}$
- automatic maximum power point tracking (MPPT) for solar charging
- bidirectional converter operation in reverse mode
- charge current capability up to $20 \text{ A}$ according to the product summary [TI, BQ25756 product page]

These statements can be interpreted as follows. The phrase **bidirectional buck-boost** confirms that one hardware stage can exchange energy in either direction while accommodating unequal DC voltages. The phrase **charge controller** indicates that the battery side is managed as a battery rather than as a fixed passive load. The term **synchronous** indicates active MOSFET switching instead of passive one-way diode rectification, which is one of the main practical enablers of reverse power flow.

The MPPT feature also shows that the device is intended for renewable-energy operation, not only for a generic two-way battery interface. The reverse-mode description on the product page is essentially the industrial form of the textbook statement that the battery can supply power back to the other port [TI, BQ25756 product page].

Table 16.3 organizes that interpretation.

Table 16.3: Interpreting the BQ25756 product page using chapter concepts

| Product-page statement | Plain-language meaning | Chapter connection |
| --- | --- | --- |
| 70-V bidirectional buck-boost charge controller | One stage can exchange energy in either direction across unequal DC voltages | Bidirectional power flow plus buck/boost action |
| Synchronous buck-boost with NFET drivers | Active switches replace passive one-way paths | Practical enabler of reverse current and reverse power |
| MPPT for solar charging | Device is intended for renewable-energy-style source management | Battery charging from a variable solar source |
| Reverse mode | Battery can supply power back to the other port | Discharge / support mode |
| 200 kHz to 600 kHz switching frequency | High-frequency switching is used to control inductor current and reduce component size | Chopper principle from Chapter 4.1 |
| Up to 20 A charge current | The converter is intended for substantial battery current, not only tiny logic loads | Importance of current control and thermal design |

## How this matters in renewable-energy systems

Bidirectional DC-DC conversion is central to storage-rich power systems. In a solar PV plus battery installation, the converter must absorb energy when PV generation exceeds demand and return energy when the source is weak or absent. In a DC-coupled storage system or hybrid microgrid, the same bidirectional interface helps the battery exchange power with a common DC bus [Abu-Rub, Malinowski, Al-Haddad, *Power Electronics for Renewable Energy Systems, Transportation and Industrial Applications*].

The same principle appears in battery-backed UPS systems, transport applications with regenerative operation, dual-battery automotive systems, and backup supplies using batteries or supercapacitors [DOE FEMP, *Electric Vehicle Technology Overview*], [Analog Devices, LTC3871 product brief]. As soon as a storage element becomes part of the system, power electronics must usually support reversible energy flow in some controlled form.

## Chapter summary

- A **bidirectional DC-DC converter** can transfer average power in either direction between two DC ports.
- Bidirectional operation is required when the same electrical interface must support both charging and discharging.
- Reversal of power flow does not necessarily require reversal of voltage polarity; in many systems both port voltages remain positive while current direction changes.
- Batteries, supercapacitors, storage-backed DC buses, and EV regenerative systems are major applications of bidirectional conversion.
- Instantaneous power is $p(t) = v(t)i(t)$, and a useful DC approximation is $P \approx VI$.
- A non-isolated **bidirectional buck-boost converter** commonly uses four active switches and one inductor between two DC ports.
- In the high-side-to-low-side direction, the converter behaves conceptually like a buck converter, with the first-order relation $V_L = D V_H$.
- In the low-side-to-high-side direction, the converter behaves conceptually like a boost converter, with the first-order relation $V_H = \dfrac{V_L}{1-D}$.
- Under ideal lossless conditions, a useful power-balance estimate is $V_H I_H \approx V_L I_L$.
- The lower-voltage side often carries the larger current for a given power level, so current rating, sensing, and thermal design are especially important there.
- Practical bidirectional converters usually require synchronous switches, current sensing, current limiting, dead-time control, and careful mode transition.
- A bidirectional buck-boost converter does not automatically provide galvanic isolation; isolated bidirectional topologies are separate converter families.
- Commercial devices such as TI's BQ25756 and ADI's LTC3871 illustrate the practical use of bidirectional buck-boost conversion in battery charging, backup power, solar input management, and dual-battery systems.

## Further reading

1. M. H. Rashid, *Power Electronics: Circuits, Devices and Applications*, 4th ed.  
   A reliable textbook source for converter fundamentals, chopper quadrants, and the broader context needed to understand reversible power flow.

2. Ned Mohan, Tore M. Undeland, and William P. Robbins, *Power Electronics: Converters, Applications, and Design*, 3rd ed.  
   Especially useful for connecting first-principles converter operation with real applications in drives, storage, and power processing.

3. NPTEL, *Module 4: DC-DC Converters, Lecture 11: Multi Quadrant DC-DC Converters I* (archive.nptel.ac.in).  
   A helpful educational source for quadrant-based interpretation of bidirectional DC-DC converters and EV-related examples.

4. [Texas Instruments, BQ25756 product page and datasheet](https://www.ti.com/product/BQ25756).  
   A strong practical example of a modern bidirectional buck-boost battery charge controller with reverse mode and solar MPPT support.

5. [U.S. Department of Energy FEMP, *Electric Vehicle Technology Overview*](https://www.energy.gov/cmei/femp/articles/electric-vehicle-technology-overview-federal-fleet-training) and [Analog Devices, LTC3871 product brief](https://www.analog.com/en/resources/media-center/videos/5579264353001.html).  
   These sources are useful for seeing why bidirectional energy flow matters in EV regenerative operation and in 48 V/12 V dual-battery systems.
