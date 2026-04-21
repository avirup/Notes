# Unit 4: Transformer and Machines

## Chapter Opening

Electrical energy becomes useful when it can be changed from one voltage level to another and when it can be converted into motion. A **transformer** changes AC voltage and current levels without altering frequency. An **electric motor** converts electrical energy into mechanical rotation. This chapter treats the single-phase transformer and the most common AC and DC motors at first-year diploma depth, drawing on the ideas of electromagnetic induction from Chapter 2 and AC quantities from Chapter 3. Later chapters on rectifiers, instrumentation, and industrial control assume the material presented here.

## Core Content

### 4.1 Single-Phase Transformer

#### Construction

A single-phase transformer has no moving parts. It transfers energy between two electrically isolated circuits through a shared alternating magnetic field. The essential parts are:

- **Magnetic core:** built from thin laminated silicon-steel sheets to reduce eddy-current loss and provide a low-reluctance magnetic path.
- **Primary winding:** connected to the supply.
- **Secondary winding:** connected to the load.
- **Insulation:** separates turns of the same winding and separates primary from secondary.
- **Tank or enclosure and terminals:** for protection, cooling, and external connection.

In small transformers the two windings are placed concentrically on the same limb. Two common constructions are distinguished in the literature: in a **core-type transformer** the windings surround the core, while in a **shell-type transformer** the core surrounds the windings. Both arrangements provide a low-reluctance magnetic path and adequate insulation space; the choice is a matter of mechanical and thermal design [V. K. Mehta and Rohit Mehta, *Principles of Electrical Engineering and Electronics*] [B. L. Theraja and A. K. Theraja, *A Textbook of Electrical Technology, Vol. II*].

#### Working principle

When AC voltage is applied to the primary, the resulting alternating current produces an alternating flux in the core. This flux links the secondary winding and induces an emf in it by Faraday's law. If a load is connected across the secondary, secondary current flows and power is delivered to the load [OpenStax, *College Physics 2e, 23.7 Transformers*](https://openstax.org/books/college-physics-2e/pages/23-7-transformers).

A steady DC supply produces a steady core flux after the switching transient, and by Faraday's law a steady flux induces no secondary emf. Moreover, since the primary winding resistance is small, direct connection to DC allows a damaging current to develop without the limiting action of the magnetising reactance. Ordinary power transformers are therefore designed for AC at their rated frequency.

#### The emf equation

Let the core flux vary sinusoidally as

$$
\Phi = \Phi_m \sin \omega t,
$$

with $\omega = 2\pi f$. For a winding of $N$ turns, Faraday's law gives

$$
e = -N\frac{d\Phi}{dt} = -N\omega\Phi_m\cos\omega t.
$$

The peak induced emf is $E_m = 2\pi f N \Phi_m$, and dividing by $\sqrt{2}$ gives the RMS value

$$
\boxed{E = 4.44 f N \Phi_m}. \tag{4.1}
$$

Applying Equation (4.1) separately to the two windings,

$$
E_1 = 4.44 f N_1 \Phi_m, \qquad E_2 = 4.44 f N_2 \Phi_m, \tag{4.2, 4.3}
$$

so that

$$
\boxed{\frac{E_2}{E_1} = \frac{N_2}{N_1}}. \tag{4.4}
$$

For an ideal or nearly ideal transformer the terminal voltages follow the same ratio, giving the **transformation ratio**

$$
\boxed{k = \frac{V_2}{V_1} \approx \frac{N_2}{N_1}}. \tag{4.5}
$$

If $N_2 > N_1$ the transformer is a **step-up** type; if $N_2 < N_1$ it is a **step-down** type; if $N_2 = N_1$ it acts as an **isolation transformer**. In every case the frequency is unchanged.

#### Current and power relations

In an ideal transformer, input power equals output power:

$$
V_1 I_1 = V_2 I_2, \tag{4.6}
$$

which gives

$$
\boxed{\frac{I_2}{I_1} = \frac{V_1}{V_2} = \frac{N_1}{N_2}}. \tag{4.7}
$$

A step-down transformer therefore raises current capability in the same ratio as it lowers voltage. This is why low-voltage secondaries are normally wound with thicker wire for the same VA rating.

#### No-load and loaded operation

On no load, the primary draws a small magnetising current that establishes the core flux and supplies the core losses. When a load is connected, the secondary current produces its own magnetic effect, and the primary current rises so that the core flux remains approximately constant and the required power is transferred to the load [V. K. Mehta and Rohit Mehta, *Principles of Electrical Engineering and Electronics*].

#### Losses

Two loss mechanisms are important:

- **Core loss:** hysteresis and eddy-current losses in the core (Chapter 2). Roughly independent of load, so it dominates at light load.
- **Copper loss:** $I^2R$ dissipation in the windings. Increases with the square of load current.

Because the core is continuously magnetised at supply frequency, a transformer warms up even at no load.

#### Ratings and center-tapped windings

A transformer nameplate typically shows primary voltage, secondary voltage (or voltages), frequency, VA or kVA rating, current rating, and tap information. The rating is given in VA rather than watts because heating depends on voltage and current regardless of load power factor. A `230 V / 12 V, 24 VA` transformer can supply a rated secondary current of $24/12 = 2\ \text{A}$. Before connecting any transformer to a supply, the input voltage and frequency ratings must be verified; an output voltage that "looks useful" is not a valid selection criterion.

A **center-tapped** secondary is a single winding with a connection brought out from its midpoint. A `12.6 V C.T.` winding gives $12.6\ \text{V}$ end-to-end and $6.3\ \text{V}$ from the center tap to either end. This arrangement is used in full-wave rectifiers, dual-polarity supplies, and heater circuits. A center-tapped winding is not equivalent to two independent secondaries.

#### Worked Example 4.1

A single-phase transformer has 500 primary turns and 100 secondary turns. The primary is connected to $230\ \text{V}$, $50\ \text{Hz}$. Find the secondary voltage.

From Equation (4.5),

$$
V_2 = V_1 \frac{N_2}{N_1} = 230 \times \frac{100}{500} = 46\ \text{V}.
$$

The transformer is a step-down type with $V_2 = 46\ \text{V}$.

#### Worked Example 4.2

A transformer operates at $50\ \text{Hz}$, with 400 primary turns and a maximum core flux of $2.5 \times 10^{-3}\ \text{Wb}$. Find the primary induced emf.

From Equation (4.2),

$$
E_1 = 4.44 \times 50 \times 400 \times 2.5 \times 10^{-3} = 222\ \text{V}.
$$

#### Worked Example 4.3

An ideal transformer steps $230\ \text{V}$ down to $23\ \text{V}$. If the secondary current is $4\ \text{A}$, find the primary current.

From Equation (4.6),

$$
I_1 = \frac{V_2 I_2}{V_1} = \frac{23 \times 4}{230} = 0.4\ \text{A},
$$

a factor of ten smaller than $I_2$, as the turns ratio requires.

### 4.2 AC and DC Motors

#### Common construction

Rotating machines share a standard set of mechanical parts: a stationary **stator** carrying windings or magnetic poles; a **rotor** mounted on a **shaft**; **bearings** supporting the shaft; a **frame or yoke** providing mechanical support; and, in most practical machines, an internal fan and terminal box. Electrical details distinguish one motor type from another, but this vocabulary is common to both AC and DC machines.

#### Force and torque

The motor principle follows from Fleming's Left-Hand Rule (Chapter 2): a current-carrying conductor in a magnetic field experiences a force. When conductors are arranged on a rotor, these forces combine to produce **torque** and hence rotation [NPTEL, *Elements of CNC Machine Tools: Electric Motors*](https://archive.nptel.ac.in/content/storage2/courses/112103174/module4/lec1/3.html). Motor families differ in how the field is produced, how current is delivered to the rotor, and how unidirectional torque is maintained over each revolution.

#### DC motors

A brushed DC motor consists of a **yoke** carrying **field poles** with either a field winding or permanent magnets, an **armature** on the rotor, and a **commutator** and **brushes** that feed current to the armature [NPTEL, *Elements of CNC Machine Tools: Electric Motors*](https://archive.nptel.ac.in/content/storage2/courses/112103174/module4/lec1/3.html) [Edward Hughes, *Hughes Electrical and Electronic Technology*]. The field system establishes the magnetic flux; current flowing through the armature conductors produces a force in that field, and the forces on individual conductors combine into shaft torque.

If the armature current were not reversed as the rotor turned, the torque on any given conductor would reverse every half revolution. The commutator acts as a mechanical rectifier, reversing the connections to the armature coils at the correct instants so that the torque on each conductor always has the same rotational sense. The brushes provide the sliding electrical contact between the external supply and the rotating commutator segments.

As the armature rotates through the field, an emf is also induced in its conductors. This **back emf** opposes the supply voltage, and the armature circuit satisfies

$$
\boxed{V = E_b + I_a R_a}, \tag{4.8}
$$

where $R_a$ is the armature resistance. Back emf rises with speed and falls with load: if the motor is loaded and slows, $E_b$ drops, $I_a$ rises, and the motor develops more torque to meet the load — the feedback mechanism that makes a DC motor self-regulating.

#### AC induction motors

The most widely used AC motor is the **induction motor**, found in ceiling fans, pumps, compressors, and the great majority of industrial drives. Its main parts are a **stator** carrying the supply winding, a **rotor** (most commonly a **squirrel-cage** construction with conducting bars shorted by end rings), a shaft in bearings, a frame, a cooling fan, and a terminal box [NPTEL, *Elements of CNC Machine Tools: Electric Motors*](https://archive.nptel.ac.in/content/storage2/courses/112103174/module4/lec1/4.html).

When the stator is energised, its current sets up a magnetic field that, in a three-phase machine, rotates naturally at a speed fixed by the supply frequency. This field induces currents in the rotor bars, and the interaction of those induced currents with the stator field produces torque. The rotor current is not supplied from outside — hence the name *induction* motor.

A **single-phase induction motor** cannot produce a rotating field from a single winding alone. It uses a **main winding**, an **auxiliary (starting) winding** often fed through a **capacitor**, and a squirrel-cage rotor. The auxiliary circuit creates the phase displacement needed to start the rotor; depending on the design, it may be switched out once the motor reaches running speed or left permanently in circuit [WEG, *W21 - Single Phase TEFC*](https://www.weg.net/catalog/weg/RU/en/Electric-Motors/Special-Application-Motors/Single-Phase-Motors/Cast-Iron-Single-Phase/W21---Single-Phase-TEFC/p/MKT_WMO_RU_SINGLE_PHASE_TEFC).

#### Synchronous speed and slip

The stator field in an AC machine rotates at the **synchronous speed**

$$
\boxed{N_s = \frac{120f}{P}}, \tag{4.9}
$$

where $f$ is the supply frequency and $P$ is the number of poles. On a $50\ \text{Hz}$ supply, a 2-pole machine has $N_s = 3000\ \text{rpm}$, a 4-pole machine $1500\ \text{rpm}$, and a 6-pole machine $1000\ \text{rpm}$.

An induction motor cannot run at exactly $N_s$: if it did, there would be no relative motion between the stator field and the rotor, no induced rotor current, and no torque. The rotor therefore runs slightly below synchronous speed, and the fractional difference is the **slip**

$$
\boxed{s = \frac{N_s - N_r}{N_s}}, \qquad s\% = \frac{N_s - N_r}{N_s}\times 100. \tag{4.10, 4.11}
$$

#### Worked Example 4.4

A 4-pole induction motor runs on a $50\ \text{Hz}$ supply. Its synchronous speed is

$$
N_s = \frac{120 \times 50}{4} = 1500\ \text{rpm}.
$$

#### Worked Example 4.5

The same motor runs at $1440\ \text{rpm}$ under load. The slip is

$$
s\% = \frac{1500 - 1440}{1500}\times 100 = 4\%.
$$

#### Worked Example 4.6

A DC motor is supplied at $220\ \text{V}$ with a back emf of $210\ \text{V}$ and an armature resistance of $1\ \Omega$. From Equation (4.8),

$$
I_a = \frac{V - E_b}{R_a} = \frac{220 - 210}{1} = 10\ \text{A}.
$$

#### Comparison of AC and DC motors

#### Table 4.1 Introductory comparison of AC and DC motors

| Feature | AC motor | DC motor |
|---|---|---|
| Supply type | AC | DC |
| Typical applications | Fans, pumps, compressors, industrial drives | Small drives, battery-operated equipment, variable-speed drives |
| Distinctive part | Stator winding with induced-current rotor | Commutator and brushes (brushed type) |
| Torque mechanism | Interaction of stator field with induced rotor currents | Force on armature current in the field |
| Speed determined by | Supply frequency and pole number | Armature voltage and back emf |
| Maintenance | Low for cage induction motors | Higher for brushed types |

The appropriate choice in any application depends on the available supply, control requirements, cost, maintenance access, and load characteristics.

#### Nameplate information

Motor and transformer nameplates are the practical interface between textbook theory and real equipment selection. A motor nameplate typically shows rated voltage, frequency, current, output power in W or kW, speed in rpm, number of phases, duty, insulation class, and — for single-phase motors — capacitor data. A transformer nameplate shows primary and secondary voltages, frequency, VA or kVA rating, current rating, tap information, and enclosure or temperature class.

#### Applications

Transformers appear in power transmission and distribution, battery chargers, welding equipment, inverter front ends, control-panel supplies, and isolating adapters. AC induction motors drive domestic fans, pumps, coolers, refrigeration compressors, conveyors, blowers, and most machine tools. DC motors are used in battery-operated equipment, small actuators, automotive auxiliaries such as wipers and blowers, portable tools, and laboratory drives [Britannica, *transformer*](https://www.britannica.com/technology/transformer-electronics) [WEG, *W21 - Single Phase TEFC*](https://www.weg.net/catalog/weg/RU/en/Electric-Motors/Special-Application-Motors/Single-Phase-Motors/Cast-Iron-Single-Phase/W21---Single-Phase-TEFC/p/MKT_WMO_RU_SINGLE_PHASE_TEFC) [NPTEL, *Elements of CNC Machine Tools: Electric Motors*](https://archive.nptel.ac.in/content/storage2/courses/112103174/module4/lec1/3.html).

## Worked Interpretation Exercise

The [Hammond Manufacturing 166N12 power transformer](https://www.hammfg.com/part/166N12) is listed with a primary of `115 V, 60 Hz`, a secondary of `12.6 V C.T.`, a secondary current of `4 A`, and a rating of `50.4 VA`.

The primary marking fixes the supply for which the unit is designed: $115\ \text{V}$ at $60\ \text{Hz}$. It is therefore not suitable for direct connection to a $230\ \text{V}, 50\ \text{Hz}$ Indian single-phase mains. The secondary marking `12.6 V C.T.` indicates a center-tapped winding, giving $12.6\ \text{V}$ end-to-end and approximately $6.3\ \text{V}$ from the center tap to either end. The rated secondary current is $4\ \text{A}$, and the VA rating is consistent with the voltage–current product:

$$
VA = 12.6 \times 4 = 50.4\ \text{VA}.
$$

Reading a catalogue entry in this way demonstrates that transformer selection begins with input voltage and frequency, that the VA rating is the product of rated secondary voltage and current, and that a center tap must be interpreted as a midpoint on a single winding rather than as two separate secondaries.

## Chapter Summary

- For sinusoidal core flux, the transformer emf equation is $E = 4.44 f N \Phi_m$.
- Voltage, turns, and current are related by $\dfrac{V_2}{V_1} \approx \dfrac{N_2}{N_1} = \dfrac{I_1}{I_2}$; frequency is unchanged.
- Transformers are classified as step-up, step-down, or isolation according to the turns ratio.
- Practical transformers suffer **core losses** (hysteresis and eddy current, roughly load-independent) and **copper losses** ($I^2R$, rising with load).
- In a brushed DC motor the commutator reverses armature current each half revolution to maintain unidirectional torque, and the armature circuit satisfies $V = E_b + I_a R_a$.
- In an AC induction motor the stator field induces rotor current; torque requires slip between the rotor and the synchronous speed $N_s = 120f/P$, with $s = (N_s - N_r)/N_s$.
- Transformer ratings are given in VA; motor ratings include output power, rated speed, and, for single-phase motors, capacitor data.

## Further Reading

1. [V. K. Mehta and Rohit Mehta, *Principles of Electrical Engineering and Electronics*](https://www.schandpublishing.com/books/technical/general-engineering/principles-electrical-engineering-electronics/9789352534798/) — a widely used diploma-level text for transformer basics, machine principles, and numerical problems.
2. [NPTEL, *Elements of CNC Machine Tools: Electric Motors*](https://archive.nptel.ac.in/content/storage2/courses/112103174/module4/lec1/3.html) — introductory treatment of DC motor construction, commutator action, and torque production.
3. [OpenStax, *College Physics 2e, 23.7 Transformers*](https://openstax.org/books/college-physics-2e/pages/23-7-transformers) — open-textbook treatment of transformer action, voltage and current ratios, and the AC-only nature of ordinary transformers.
4. [Britannica, *transformer*](https://www.britannica.com/technology/transformer-electronics) — concise definitions, applications, and the reason for core lamination.
5. [WEG, *W21 - Single Phase TEFC*](https://www.weg.net/catalog/weg/RU/en/Electric-Motors/Special-Application-Motors/Single-Phase-Motors/Cast-Iron-Single-Phase/W21---Single-Phase-TEFC/p/MKT_WMO_RU_SINGLE_PHASE_TEFC) — a manufacturer's description of a practical single-phase induction motor.
