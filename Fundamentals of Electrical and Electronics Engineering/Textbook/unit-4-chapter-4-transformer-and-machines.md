# Unit 4: Transformer and Machines

## Chapter Opening

Electrical energy becomes truly useful when it can be changed from one voltage level to another and when it can be converted into motion. A **transformer** changes AC voltage and current levels without changing frequency. An **electric motor** converts electrical energy into mechanical rotation. These two ideas appear everywhere: in distribution transformers on electric poles, in mobile-phone chargers, in welding sets, in ceiling fans, in water pumps, in workshop machines, and in industrial drives.

This chapter grows naturally from Chapters 2 and 3. Chapter 2 explained electromagnetic induction and magnetic circuits. Chapter 3 explained AC quantities, reactance, and power. Here those ideas become physical devices. We first study the single-phase transformer: its main parts, working principle, emf equation, transformation ratio, ratings, and simple calculations. Then we study AC and DC motors at diploma-entry depth. The focus remains on parts, principle, simple performance ideas, and practical applications rather than advanced machine design.

Later chapters on power supplies, semiconductor rectifiers, instrumentation, and industrial control will rely on the equipment introduced here. A charger uses a transformer. A pump uses a motor. A control panel may contain both.

## Prerequisites Check

- Meaning of magnetic flux, Faraday's law, and mutual inductance from Chapter 2.
- RMS value, frequency, and AC supply ideas from Chapter 3.
- Basic power relation such as $P = VI$ for DC and apparent power in VA for AC loads.
- Familiarity with passive components such as coil, resistor, and capacitor from Chapter 1.
- Ability to rearrange simple algebraic equations.

If Faraday's law or RMS value feels uncertain, briefly review Chapters 2 and 3 before reading the transformer emf equation section.

## Core Content

### 4.1 Single-Phase Transformer

#### Why transformers matter

Suppose a workshop needs a low-voltage AC supply for a control circuit, a soldering tool, or a battery charger front end. The building supply may be $230\ \text{V}$, $50\ \text{Hz}$, but the equipment may need $12\ \text{V}$, $24\ \text{V}$, or some other value. A transformer makes that change possible. In a power system, the same principle is used in the opposite direction: voltage is stepped up for transmission and stepped down for utilization [Britannica, *transformer*](https://www.britannica.com/technology/transformer-electronics) [OpenStax, *College Physics 2e, 23.7 Transformers*](https://openstax.org/books/college-physics-2e/pages/23-7-transformers).

The basic transformer has no rotating parts. That makes it very different from a motor. It transfers energy from one circuit to another through a changing magnetic field. The primary and secondary windings are electrically isolated, but magnetically linked.

**Image prompt for Figure 4.1:** Create a clean textbook-style illustration of a single-phase two-winding transformer on a laminated core. Show the primary winding on one limb connected to an AC source labeled $V_1$, the secondary winding on the other limb connected to a load labeled $V_2$, and alternating core flux $\Phi$ linking both windings. Label laminated core, primary winding, secondary winding, input current $I_1$, output current $I_2$, and load.

#### Main parts of a two-winding transformer

At diploma-entry level, the important physical parts are these:

- **Magnetic core:** usually built from thin laminated silicon-steel sheets for power-frequency transformers, so that magnetic reluctance is low and eddy-current loss is reduced.
- **Primary winding:** the winding connected to the supply.
- **Secondary winding:** the winding connected to the load.
- **Insulation:** separates turns of the same winding and also separates primary from secondary for safety.
- **Tank or enclosure:** present in many practical transformers for protection and cooling.
- **Terminals or leads:** provide electrical connection to the outside circuit.

In small transformers, the windings may be arranged one over the other on the same limb. In larger transformers, the construction becomes more elaborate, but the teaching idea remains the same: one winding creates alternating flux in the core, and that changing flux induces emf in the other winding [V. K. Mehta and Rohit Mehta, *Principles of Electrical Engineering and Electronics*] [B. L. Theraja and A. K. Theraja, *A Textbook of Electrical Technology, Vol. II*].

#### Core-type and shell-type idea

Textbooks often distinguish between **core-type** and **shell-type** transformers. This distinction is useful because students will see both forms in books and laboratories.

In a **core-type transformer**, the windings surround a considerable part of the core. In a **shell-type transformer**, the core surrounds a larger part of the windings. At beginner level, there is no need to compare detailed leakage reactance or mechanical performance. The main point is simply that both constructions provide:

- a magnetic path of low reluctance,
- magnetic linking between primary and secondary,
- space for insulated windings,
- and a practical structure for cooling and mounting.

#### Basic working principle

The transformer works on **mutual induction**. When AC voltage is applied to the primary winding, an alternating current flows in the primary. That alternating current produces an alternating magnetic flux in the core. Because the core flux links the secondary winding also, an emf is induced in the secondary.

This is exactly the Chapter 2 idea of Faraday's law applied to two coils on a common magnetic path. If the flux changes with time, emf is induced. If the flux is steady, no transformer action occurs. That is why a transformer requires a changing magnetic field and therefore normally works with AC rather than steady DC [OpenStax, *College Physics 2e, 23.7 Transformers*](https://openstax.org/books/college-physics-2e/pages/23-7-transformers).

The physical sequence is:

1. AC supply is applied to the primary.
2. Primary current creates alternating core flux.
3. Core flux links both windings.
4. Induced emf appears in both primary and secondary.
5. If a load is connected, secondary current flows and power is delivered to the load.

#### Why DC does not work in an ordinary transformer

Students often ask this question because the primary is just a coil on a core. The answer follows directly from Faraday's law. If the applied voltage is pure DC, the current becomes steady after the switching transient. Then the magnetic flux also becomes nearly steady. A steady flux does not induce continuous emf in the secondary.

There is another practical danger. The winding resistance of a transformer is usually small. If DC is applied directly, the core does not present the usual AC magnetizing behavior, so the current may become excessively large. This can overheat the winding quickly. So a normal power transformer is intended for AC of its rated frequency, not direct connection to DC [OpenStax, *College Physics 2e, 23.7 Transformers*](https://openstax.org/books/college-physics-2e/pages/23-7-transformers).

#### Induced emf and the transformer emf equation

We now derive the most important formula of this chapter. Assume the core flux is sinusoidal:

$$
\Phi = \Phi_m \sin \omega t
$$

where $\Phi_m$ is the maximum flux in weber and $\omega = 2\pi f$ is the angular frequency.

For a winding of $N$ turns, Faraday's law gives the instantaneous induced emf:

$$
e = -N\frac{d\Phi}{dt}
$$

Differentiate the flux:

$$
\frac{d\Phi}{dt} = \omega \Phi_m \cos \omega t
$$

So the maximum value of induced emf is

$$
E_m = \omega N \Phi_m = 2\pi f N \Phi_m
$$

For a sinusoidal wave, RMS value is peak value divided by $\sqrt{2}$. Therefore,

$$
E = \frac{E_m}{\sqrt{2}} = \frac{2\pi f N \Phi_m}{\sqrt{2}}
$$

This becomes

$$
\boxed{E = 4.44 f N \Phi_m} \tag{4.1}
$$

Equation (4.1) is the **transformer emf equation**. It says that induced RMS emf depends on four things:

- frequency $f$,
- number of turns $N$,
- maximum flux $\Phi_m$,
- and the sinusoidal nature of the waveform, which gives the factor 4.44.

Applying Equation (4.1) to the primary and secondary windings separately:

$$
\boxed{E_1 = 4.44 f N_1 \Phi_m} \tag{4.2}
$$

$$
\boxed{E_2 = 4.44 f N_2 \Phi_m} \tag{4.3}
$$

Here:

- $E_1$ is primary induced emf,
- $E_2$ is secondary induced emf,
- $N_1$ is number of primary turns,
- $N_2$ is number of secondary turns.

Dividing Equation (4.3) by Equation (4.2):

$$
\boxed{\frac{E_2}{E_1} = \frac{N_2}{N_1}} \tag{4.4}
$$

This is the voltage-turns relation of the transformer.

#### Transformation ratio

The ratio of secondary quantity to primary quantity is often called the **transformation ratio**. In simple voltage form,

$$
\boxed{k = \frac{V_2}{V_1} \approx \frac{E_2}{E_1} = \frac{N_2}{N_1}} \tag{4.5}
$$

At beginner level, it is common to use induced emf ratio, voltage ratio, and turns ratio almost interchangeably for an ideal or nearly ideal transformer.

Three important cases follow:

- If $N_2 > N_1$, then $V_2 > V_1$: this is a **step-up transformer**.
- If $N_2 < N_1$, then $V_2 < V_1$: this is a **step-down transformer**.
- If $N_2 = N_1$, then $V_2 \approx V_1$: this is an **isolation transformer**.

Transformers change voltage and current level, but not frequency. A $50\ \text{Hz}$ supply remains $50\ \text{Hz}$ at the output.

#### Voltage ratio, current ratio, and power idea

If the transformer is ideal, input power equals output power:

$$
V_1 I_1 = V_2 I_2 \tag{4.6}
$$

From this,

$$
\boxed{\frac{I_2}{I_1} = \frac{V_1}{V_2} = \frac{N_1}{N_2}} \tag{4.7}
$$

This is one of the most important practical ideas. If voltage is stepped down, current capability increases. If voltage is stepped up, current capability decreases.

That is why a small secondary voltage winding may use thicker wire. Lower voltage often means higher current for the same VA rating.

#### No-load idea and load idea

When the secondary is open and no load is connected, the transformer is said to be on **no load**. In that case:

- the primary still draws a small current from the supply,
- that current is needed mainly to establish alternating flux in the core,
- and to supply core losses.

When a load is connected to the secondary, secondary current flows. That current produces its own magnetic effect. The primary then draws additional current from the supply so that the core flux remains approximately at the required value and the transformer can transfer power to the load [V. K. Mehta and Rohit Mehta, *Principles of Electrical Engineering and Electronics*].

At this level, the important point is not the exact equivalent circuit. The important point is that the transformer is not just "sending current across the core." Instead, the supply, core flux, and both windings interact magnetically so that energy is transferred from input to output.

#### Practical transformer losses

No practical transformer is perfect. Two important losses are:

- **Core loss:** mainly hysteresis loss and eddy-current loss in the core. These were introduced in Chapter 2.
- **Copper loss:** $I^2R$ loss in the primary and secondary windings.

At no load, core loss is more prominent than copper loss because current is small. As load increases, copper loss increases because winding current increases.

This is why a transformer may become warm even when it is not heavily loaded. The core is still undergoing repeated magnetization and demagnetization at supply frequency.

#### Ratings found on practical transformers

A practical transformer is usually marked by:

- primary voltage,
- secondary voltage or voltages,
- frequency,
- VA or kVA rating,
- current rating,
- sometimes center tap or multiple taps,
- insulation and temperature information.

The rating is commonly given in **VA** rather than watts because transformer heating depends strongly on voltage and current, while the load power factor may vary.

For example, a `230 V / 12 V, 24 VA` transformer can ideally supply about

$$
I_2 = \frac{24}{12} = 2\ \text{A}
$$

at the rated secondary voltage.

#### Center-tapped secondary

Some transformers have a **center-tapped** secondary. If a secondary is marked `12.6 V C.T.`, it means there are two equal halves with a center connection. The voltage from one end to the other full winding is `12.6 V`. The voltage from the center tap to either end is half of that, ideally `6.3 V`.

This is useful in:

- full-wave rectifier circuits,
- dual-polarity supply arrangements,
- heating and low-voltage legacy circuits,
- some charger and control applications.

Students should not confuse a center-tapped winding with two fully independent secondary windings. The winding is continuous, with a connection brought out from the midpoint.

#### Worked Example 4.1

A single-phase transformer has 500 turns on the primary and 100 turns on the secondary. The primary is connected to $230\ \text{V}$, $50\ \text{Hz}$ AC. Assuming an ideal transformer, find the secondary voltage.

Use Equation (4.5):

$$
\frac{V_2}{V_1} = \frac{N_2}{N_1}
$$

Substitute the values:

$$
\frac{V_2}{230} = \frac{100}{500} = 0.2
$$

So

$$
V_2 = 230 \times 0.2 = 46\ \text{V}
$$

So the transformer is a step-down transformer and the secondary voltage is **46 V**.

#### Worked Example 4.2

A transformer operates at $50\ \text{Hz}$. The primary winding has 400 turns and the maximum core flux is $2.5 \times 10^{-3}\ \text{Wb}$. Find the induced primary emf.

Use Equation (4.2):

$$
E_1 = 4.44 f N_1 \Phi_m
$$

Substitute:

$$
E_1 = 4.44 \times 50 \times 400 \times 2.5 \times 10^{-3}
$$

First multiply step by step:

$$
50 \times 400 = 20000
$$

$$
20000 \times 2.5 \times 10^{-3} = 50
$$

Now:

$$
E_1 = 4.44 \times 50 = 222\ \text{V}
$$

So the induced primary emf is **222 V**.

This value is close to the kind of voltage seen in practical 230 V class transformers, which helps the formula feel physically reasonable.

#### Worked Example 4.3

An ideal transformer steps down $230\ \text{V}$ to $23\ \text{V}$. If the secondary current is $4\ \text{A}$, find the primary current.

Using ideal power balance,

$$
V_1 I_1 = V_2 I_2
$$

So

$$
230 I_1 = 23 \times 4 = 92
$$

Therefore,

$$
I_1 = \frac{92}{230} = 0.4\ \text{A}
$$

So the primary current is **0.4 A**.

This result shows the inverse relation clearly. The voltage is reduced by a factor of 10, so the current is increased by a factor of 10.

#### Common misconceptions

- A transformer does not work on steady DC in the normal sense because continuous induction needs changing flux.
- A step-down transformer reduces voltage but increases current capability for the same apparent power level.
- The primary and secondary are magnetically linked, not directly electrically connected.
- The voltage ratio follows the turns ratio, but frequency does not change.
- A transformer rated in VA is not necessarily delivering the same number of watts unless load power factor is considered.

#### Practical note

Before using any transformer in a circuit, always check three markings first:

- input voltage,
- frequency,
- and VA or current rating.

A transformer with the wrong input voltage rating should never be connected directly to the mains supply just because its output voltage "looks useful."

### 4.2 AC and DC Motors

#### Why motors matter

A motor is an energy-conversion device. It takes electrical energy and produces mechanical rotation. That rotation may drive a ceiling fan, a water pump, a drilling machine, a conveyor, a wiper, or a printing mechanism.

At first-year diploma level, the most important motor ideas are:

- what the main parts are,
- how torque is produced,
- how AC and DC motor arrangements differ,
- and where each type is commonly used.

We do not need advanced equivalent circuits or detailed torque-speed curve derivations here. But we do need a clear physical picture.

**Image prompt for Figure 4.2:** Create a clean textbook-style comparison diagram showing a basic DC motor and a basic AC induction motor side by side in cutaway form. For the DC motor, label yoke, poles, field winding or permanent magnet, armature, commutator, brushes, shaft, and bearings. For the AC induction motor, label stator, stator winding, squirrel-cage rotor, shaft, bearings, cooling fan, frame, and terminal box.

#### Common parts of rotating electrical machines

Many motors, whether AC or DC, share some broad mechanical parts:

- **Stator:** stationary part that carries windings or magnetic poles.
- **Rotor:** rotating part mounted on the shaft.
- **Shaft:** transmits mechanical power to the load.
- **Bearings:** support the shaft and allow smooth rotation.
- **Frame or yoke:** provides mechanical support and protection.
- **Fan or cooling arrangement:** removes heat in many practical machines.
- **Terminal box or leads:** used for electrical connection.

The electrical details differ from one motor type to another, but this common vocabulary helps students identify machines in the lab and field.

#### Basic force and torque idea

The essential motor principle was introduced in Chapter 2 through Fleming's Left-Hand Rule. When a current-carrying conductor is placed in a magnetic field, it experiences a force. If conductors are arranged on a rotating armature or rotor, the forces combine to produce **torque**, which causes rotation [NPTEL, *Elements of CNC Machine Tools: Electric Motors*](https://archive.nptel.ac.in/content/storage2/courses/112103174/module4/lec1/3.html).

So a motor needs two things:

- magnetic field,
- and current in conductors arranged so that force produces turning effect.

The difference between motor types lies in how the field is produced, how current reaches the rotating part, and how continuous unidirectional torque is maintained.

#### DC motor: main parts

A basic **DC motor** contains:

- **yoke or frame,**
- **field poles** and field winding, or permanent magnets,
- **armature** on the rotor,
- **commutator,**
- **brushes,**
- **shaft and bearings** [NPTEL, *Elements of CNC Machine Tools: Electric Motors*](https://archive.nptel.ac.in/content/storage2/courses/112103174/module4/lec1/3.html) [Edward Hughes, *Hughes Electrical and Electronic Technology*].

The field system provides the magnetic field. The armature carries current-carrying conductors. The commutator and brushes are the distinctive parts of a classical brushed DC motor.

#### Working principle of a DC motor

When DC is supplied:

1. the field system produces magnetic flux,
2. current flows in armature conductors,
3. each conductor experiences force in the magnetic field,
4. the forces combine to produce torque,
5. the armature rotates.

If current in the rotating armature were not reversed at the correct instants, the torque would reverse every half turn and continuous rotation would not be maintained. The **commutator** solves this problem by reversing current in the armature connections as the rotor turns. The **brushes** provide sliding electrical contact with the commutator segments [NPTEL, *Elements of CNC Machine Tools: Electric Motors*](https://archive.nptel.ac.in/content/storage2/courses/112103174/module4/lec1/3.html).

This is why the commutator is often called a mechanical rectifying arrangement for the armature current direction.

#### Back emf in a DC motor

As the armature rotates in the magnetic field, it also behaves like a generator. An emf is induced in the armature conductors. This induced emf opposes the supply voltage, so it is called **back emf**.

At concept level, the armature circuit is written as

$$
\boxed{V = E_b + I_a R_a} \tag{4.8}
$$

where:

- $V$ is supply voltage,
- $E_b$ is back emf,
- $I_a$ is armature current,
- $R_a$ is armature resistance.

The physical meaning is important. If the motor speeds up, back emf increases. That tends to reduce armature current. If the motor slows under load, back emf falls, armature current rises, and torque increases. This is one reason DC motors are easy to understand in variable-speed applications.

#### AC motor: main parts

The most common AC motor in practice is the **induction motor**. In homes, this often appears as a single-phase motor in fans, pumps, air coolers, washing machines, and small compressors. In industry, three-phase induction motors are extremely common.

The main parts of a basic induction motor are:

- **stator,**
- **stator winding,**
- **rotor,**
- **shaft and bearings,**
- **frame,**
- **cooling fan,**
- **terminal box** [NPTEL, *Elements of CNC Machine Tools: Electric Motors*](https://archive.nptel.ac.in/content/storage2/courses/112103174/module4/lec1/4.html).

In a **squirrel-cage rotor**, conducting bars are embedded in the rotor and short-circuited by end rings. This construction is rugged and common.

#### Working principle of an induction motor

In an induction motor, the stator is connected to the AC supply. The stator current produces a magnetic field. In a three-phase motor, this field is naturally rotating. In a single-phase motor, the situation is more subtle and starting assistance is needed in practical designs. The changing or rotating stator field induces current in the rotor conductors. Those rotor currents produce their own magnetic effect, and interaction between stator field and rotor currents produces torque [NPTEL, *Elements of CNC Machine Tools: Electric Motors*](https://archive.nptel.ac.in/content/storage2/courses/112103174/module4/lec1/4.html).

This is why the machine is called an **induction motor**: the rotor current is induced, not supplied directly by an external electrical connection in the ordinary cage-rotor case.

#### Single-phase induction motor idea

Because the local supply in homes and many small shops is $230\ \text{V}$, $50\ \text{Hz}$ single-phase AC, students often meet the single-phase induction motor first.

A single-phase induction motor usually has:

- a **main winding,**
- an **auxiliary or starting winding,**
- often a **capacitor** in series with the auxiliary winding,
- and a squirrel-cage rotor.

The auxiliary arrangement is used to create a starting condition that gives a rotating-field effect strong enough to start the rotor. Once the motor comes up to speed, the starting winding may be disconnected in some designs, while in capacitor-run designs a capacitor remains in service [WEG, *W21 - Single Phase TEFC*](https://www.weg.net/catalog/weg/RU/en/Electric-Motors/Special-Application-Motors/Single-Phase-Motors/Cast-Iron-Single-Phase/W21---Single-Phase-TEFC/p/MKT_WMO_RU_SINGLE_PHASE_TEFC).

At this level, the essential point is:

- single-phase motors are common for domestic and light workshop loads,
- they often need a starting arrangement,
- and they are widely used because single-phase supply is widely available.

#### Synchronous speed and slip

For AC motors, one very useful introductory formula is the **synchronous speed** relation:

$$
\boxed{N_s = \frac{120f}{P}} \tag{4.9}
$$

where:

- $N_s$ is synchronous speed in revolutions per minute (rpm),
- $f$ is supply frequency in hertz,
- $P$ is number of poles.

For example, on a $50\ \text{Hz}$ supply:

- a 2-pole machine has $N_s = 3000\ \text{rpm}$,
- a 4-pole machine has $N_s = 1500\ \text{rpm}$,
- a 6-pole machine has $N_s = 1000\ \text{rpm}$.

An induction motor rotor does not normally run exactly at synchronous speed. It runs slightly below it. The difference is described by **slip**:

$$
\boxed{s = \frac{N_s - N_r}{N_s}} \tag{4.10}
$$

If slip is required as a percentage,

$$
\boxed{s\% = \frac{N_s - N_r}{N_s}\times 100} \tag{4.11}
$$

Here $N_r$ is the actual rotor speed.

Slip is necessary in an induction motor because rotor current depends on relative motion between the rotating stator field and the rotor. If there were no relative motion at all, induction would vanish and torque would not be maintained in the same way.

#### Worked Example 4.4

A 4-pole induction motor is connected to a $50\ \text{Hz}$ supply. Find its synchronous speed.

Use Equation (4.9):

$$
N_s = \frac{120f}{P} = \frac{120 \times 50}{4}
$$

$$
N_s = \frac{6000}{4} = 1500\ \text{rpm}
$$

So the synchronous speed is **1500 rpm**.

#### Worked Example 4.5

A 4-pole, $50\ \text{Hz}$ induction motor runs at $1440\ \text{rpm}$. Find the slip percentage.

First find synchronous speed:

$$
N_s = \frac{120 \times 50}{4} = 1500\ \text{rpm}
$$

Now use Equation (4.11):

$$
s\% = \frac{1500 - 1440}{1500}\times 100
$$

$$
s\% = \frac{60}{1500}\times 100 = 4\%
$$

So the slip is **4%**.

#### Worked Example 4.6

A DC motor has supply voltage $220\ \text{V}$, back emf $210\ \text{V}$, and armature resistance $1\ \Omega$. Find the armature current.

Use Equation (4.8):

$$
V = E_b + I_aR_a
$$

So

$$
I_a = \frac{V - E_b}{R_a}
= \frac{220 - 210}{1}
= 10\ \text{A}
$$

So the armature current is **10 A**.

This simple result shows why back emf matters. The armature current is not set by supply voltage alone.

#### AC and DC motors compared

#### Table 4.1 Introductory comparison of AC and DC motors

| Feature | AC motor | DC motor |
|---|---|---|
| Supply type | AC | DC |
| Common field application | Fans, pumps, compressors, industrial drives | Small drives, battery-operated systems, variable-speed drives, traction history |
| Main special part | Stator winding and induced rotor system | Commutator and brushes in brushed DC motor |
| Starting idea | Depends on type; induction motor uses stator field and induced rotor current | Torque produced by armature current in magnetic field |
| Speed concept | Related to frequency and pole number | Related strongly to armature voltage and back emf |
| Maintenance | Often low for induction motors | Higher in brushed motors because of brushes and commutator |

This table is not meant to say one motor is "better" in all cases. The practical choice depends on supply, control need, cost, maintenance, and application.

#### Nameplate terms students should recognize

A motor nameplate or catalog commonly includes:

- rated voltage,
- frequency,
- current,
- output power in W or kW,
- speed in rpm,
- phase,
- duty,
- insulation class,
- sometimes capacitor information for single-phase motors.

A transformer label commonly includes:

- primary voltage,
- secondary voltage,
- frequency,
- VA or kVA rating,
- current rating,
- tap information,
- and sometimes enclosure or temperature information.

Even before advanced machine theory is studied, students should learn to read these basic ratings because real equipment is always selected and used through them.

#### Common applications of transformers

Transformers are used in:

- power transmission and distribution,
- battery chargers,
- doorbell circuits,
- welding equipment,
- inverter systems,
- control panels,
- isolation supplies,
- adapter and low-voltage equipment [Britannica, *transformer*](https://www.britannica.com/technology/transformer-electronics) [Schneider Electric, *What is a Transformer*](https://www.se.com/us/en/work/featured-articles/what-is-a-transformer/).

#### Common applications of AC motors

AC motors are used in:

- ceiling fans,
- water pumps,
- air coolers,
- refrigerators and compressors,
- conveyors,
- blowers,
- machine tools,
- workshop grinders and drills,
- industrial process drives [WEG, *W21 - Single Phase TEFC*](https://www.weg.net/catalog/weg/RU/en/Electric-Motors/Special-Application-Motors/Single-Phase-Motors/Cast-Iron-Single-Phase/W21---Single-Phase-TEFC/p/MKT_WMO_RU_SINGLE_PHASE_TEFC).

#### Common applications of DC motors

DC motors are used in:

- battery-operated equipment,
- toys and small actuators,
- automobile auxiliaries such as wipers and blowers,
- portable tools and small mechanisms,
- some variable-speed drives,
- laboratory demonstration systems [NPTEL, *Elements of CNC Machine Tools: Electric Motors*](https://archive.nptel.ac.in/content/storage2/courses/112103174/module4/lec1/3.html).

#### Common misconceptions

- A transformer is not a generator. It does not create energy; it transfers AC power from one circuit to another.
- A transformer does not normally change frequency.
- A motor does not rotate simply because voltage is present. Torque requires the proper interaction of magnetic field and current.
- In a DC motor, the commutator is not a small unimportant accessory; it is central to continuous torque in the classical brushed design.
- In an induction motor, the rotor is not usually connected directly to the supply in the ordinary squirrel-cage form.
- The speed written on an induction motor is usually slightly below synchronous speed, not exactly equal to it.

#### Practical note

When a student sees a pump motor plate reading something like `230 V`, `50 Hz`, `1440 rpm`, and `single phase`, there is already a lot of useful information there. The supply type, likely motor family, expected speed range, and application all become easier to identify once the ideas of this chapter are understood.

## Worked Interpretation Exercise

Consider the specification table of the [Hammond Manufacturing 166N12 power transformer](https://www.hammfg.com/part/166N12) [Hammond Manufacturing, *Part Number 166N12*].

The page lists these important values:

- primary voltage = `115 V`, `60 Hz`
- secondary voltage = `12.6 V C.T.`
- secondary current = `4 A`
- power rating = `50.4 VA`

Now interpret these one by one.

First, the primary marking `115 V, 60 Hz` tells us this transformer is intended for a supply of 115-volt AC at 60 hertz. That means it is not intended to be connected directly to a `230 V, 50 Hz` Indian single-phase mains supply. Doing so would over-stress the transformer badly.

Second, `12.6 V C.T.` means the secondary is center-tapped. So:

- full secondary voltage from one end to the other is `12.6 V`,
- voltage from center tap to either end is approximately `6.3 V`.

Third, the current rating `4 A` refers to the rated current available from the secondary winding under the specified use conditions.

Fourth, the power rating `50.4 VA` matches the secondary voltage and current:

$$
VA = V \times I = 12.6 \times 4 = 50.4\ \text{VA}
$$

So the listed VA rating is consistent with the voltage and current values on the product page.

This short reading exercise teaches several practical lessons:

- transformer selection begins with input voltage and frequency, not output voltage alone,
- center tap must be interpreted correctly,
- VA rating is checked by voltage-current product,
- and a real catalog entry immediately connects textbook ratios to actual equipment choice.

## How This Matters in Practice

In household and industrial electrical systems, transformers adapt voltage levels for safe and efficient use, while motors turn electrical power into mechanical work. Distribution transformers reduce network voltage for consumers. Small control transformers feed contactor coils or low-voltage control circuits. Motors run fans, compressors, lifts, pumps, mixers, and machine tools.

In transformers and motors themselves, the ideas of Chapters 2 and 3 become visible hardware. The transformer is a direct application of mutual induction. The motor is a direct application of force on a current-carrying conductor and electromagnetic torque production.

In battery charging, a transformer is commonly used ahead of a rectifier in traditional chargers, especially when isolation and step-down voltage are required. In solar PV and inverter-based systems, transformers may be used for isolation, voltage matching, or auxiliary supplies, while motors appear in water pumping and ventilation loads.

In instrumentation and control circuits, small transformers provide isolated AC supplies, and motors appear in actuators, relays with motorized mechanisms, and drive-based control systems. In digital systems and automation, even if logic circuitry runs on low-voltage DC, the front-end power conversion and the final controlled load often involve transformers and motors.

## Chapter Summary

- A **single-phase transformer** transfers AC power from one circuit to another by electromagnetic induction.
- The main parts of a basic two-winding transformer are the **core**, **primary winding**, **secondary winding**, insulation, and terminals.
- A transformer works only with changing flux; this is why ordinary power transformers are for AC, not steady DC.
- For sinusoidal flux, the transformer emf equation is $E = 4.44 f N \Phi_m$.
- For primary and secondary windings: $E_1 = 4.44 f N_1 \Phi_m$ and $E_2 = 4.44 f N_2 \Phi_m$.
- Voltage ratio equals turns ratio: $\dfrac{E_2}{E_1} = \dfrac{N_2}{N_1}$.
- The transformation ratio may be written as $k = \dfrac{V_2}{V_1} \approx \dfrac{N_2}{N_1}$.
- In an ideal transformer, input power equals output power, so current ratio is inverse of voltage ratio.
- A **step-up transformer** increases voltage. A **step-down transformer** decreases voltage. An **isolation transformer** keeps approximately the same voltage but provides isolation.
- Practical transformers have **core loss** and **copper loss**.
- Transformer ratings commonly include input voltage, output voltage, frequency, VA, and current.
- A **center-tapped secondary** gives two equal half voltages from the midpoint to each end.
- A **motor** converts electrical energy into mechanical rotation.
- Common machine parts include stator, rotor, shaft, bearings, and frame.
- A **DC motor** uses current-carrying armature conductors in a magnetic field to produce torque, and a **commutator** helps maintain continuous rotation in a brushed machine.
- Back emf in a DC motor is represented by $V = E_b + I_aR_a$.
- An **AC induction motor** works because stator field action induces rotor current and torque.
- For AC motors, synchronous speed is $N_s = 120f/P$.
- Slip of an induction motor is $s = (N_s - N_r)/N_s$ and percentage slip is $s\% = \dfrac{N_s - N_r}{N_s}\times 100$.
- AC motors are common in fans, pumps, and industrial drives. DC motors are common in small drives and battery-operated systems.

## Further Reading

1. [V. K. Mehta and Rohit Mehta, *Principles of Electrical Engineering and Electronics*](https://www.schandpublishing.com/books/technical/general-engineering/principles-electrical-engineering-electronics/9789352534798/)  
   A widely used diploma-friendly text for transformer basics, machine principles, and simple numerical treatment.

2. [NPTEL, *Elements of CNC Machine Tools: Electric Motors*](https://archive.nptel.ac.in/content/storage2/courses/112103174/module4/lec1/3.html)  
   Useful for introductory DC motor construction, commutator action, and the force principle behind torque production.

3. [OpenStax, *College Physics 2e, 23.7 Transformers*](https://openstax.org/books/college-physics-2e/pages/23-7-transformers)  
   A clear open textbook source for transformer action, voltage ratio, current ratio, and the AC-only nature of ordinary transformers.

4. [Britannica, *transformer*](https://www.britannica.com/technology/transformer-electronics)  
   Useful for concise definitions, applications, and the practical reason for lamination.

5. [WEG, *W21 - Single Phase TEFC*](https://www.weg.net/catalog/weg/RU/en/Electric-Motors/Special-Application-Motors/Single-Phase-Motors/Cast-Iron-Single-Phase/W21---Single-Phase-TEFC/p/MKT_WMO_RU_SINGLE_PHASE_TEFC)  
   Useful for seeing how a practical single-phase motor is described by a manufacturer in terms of construction and application.
