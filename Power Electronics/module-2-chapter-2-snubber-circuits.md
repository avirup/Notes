# Chapter 2.2: Snubber Circuits

## Chapter opening

In the previous chapter, we studied how to command a power device. We learned that a good gate or base driver must deliver the correct voltage or current, switch quickly, and hold the device firmly in the intended state. But even a very good drive circuit cannot remove one basic fact of power electronics: real power circuits contain inductance, capacitance, stored energy, and sudden changes of current. Those realities create voltage spikes, current surges, ringing, false triggering, and extra switching loss.

That is why this chapter matters. A **snubber circuit** is one of the simplest and most practical ways of helping a power switch survive real switching conditions. It is not the main power-conversion circuit, and it is not the control circuit. It is supporting circuitry placed around the switch, transformer, diode, or load so that dangerous transients are limited and energy is redirected in a safer way [Rashid, *Power Electronics: Circuits, Devices and Applications, 4e*], [onsemi AN1048/D].

This chapter is especially important for self-study because beginners often meet snubbers only as small extra parts added near a switch: a resistor and capacitor here, a diode-capacitor-resistor there, an extra diode across an inductive load somewhere else. Without the physical story, those parts look arbitrary. They are not arbitrary. Each one exists because a circuit current cannot change instantaneously in an inductor, because a device voltage cannot rise without charging capacitance, and because stored magnetic energy must go somewhere.

We will begin by asking why snubbers are needed at all, and we will connect that need to stray inductance, leakage inductance, $dv/dt$, $di/dt$, and switching stress. Then we will distinguish **turn-ON snubbers** from **turn-OFF snubbers** at concept level. After that, we will study the two most common named families in the syllabus: **RC snubbers** and **RCD snubbers**. We will also study the **freewheeling diode**, which is not identical to every other snubber, but which performs a closely related protective role whenever an inductive current needs a safe path after the main switch changes state. These ideas will appear again in later chapters on rectifiers, choppers, inverters, and renewable-energy converters, especially in PV stages, battery chargers, UPS systems, and auxiliary power supplies.

## Prerequisites check

- You should remember from Chapter 1.2 that an SCR can false-trigger if the voltage across it changes too quickly.
- You should remember from Chapters 1.4 and 1.5 that MOSFETs and IGBTs do not switch instantaneously and that parasitic capacitances influence their switching behavior.
- You should be comfortable with the basic inductor relation that current through an inductor cannot jump suddenly.
- You should know that the energy stored in an inductor is $\tfrac{1}{2}LI^2$, even if you are not yet fully confident using it.
- You should remember from Chapter 2.1 that driver strength affects $dv/dt$ and $di/dt$, but layout and external protection components matter too.

If the ideas of leakage inductance, Miller effect, or reverse recovery feel weak, a short review of Chapters 1.2, 1.4, 1.5, and 2.1 will make this chapter easier to absorb.

## Core content

### 2.2.1 Need for snubbers; turn-ON and turn-OFF snubbers

#### Why switching stress appears even in a "simple" circuit

Let us begin with a practical picture.

Suppose a MOSFET is switching current through an inductive load in a 48 V battery charger, or an IGBT is switching a few amperes in an inverter leg fed from a rectified 230 V, 50 Hz supply. On paper, the switch turns OFF, current stops, and the voltage rises to the expected blocking level. In a real circuit, that does not happen so neatly. The wiring, package leads, PCB traces, transformer leakage path, and load all contribute some inductance. The switch node and device terminals also have capacitance. So when the current path is interrupted, the stored magnetic energy in that inductance does not disappear. It tries to keep current flowing. The result is usually a voltage overshoot, ringing, or both.

The first equation to keep in mind is the stored magnetic energy:

$$\boxed{E_L = \frac{1}{2}L_{\sigma} I^2} \quad \text{(7.1)}$$

where $E_L$ is the energy stored in the stray or leakage inductance, $L_{\sigma}$ is that inductance, and $I$ is the current flowing just before the switching event.

This equation is small, but it carries a big message. Even a very small inductance can store meaningful energy if the current is large enough.

Consider a numerical example from a medium-power converter. Suppose the effective stray or leakage inductance is only $2\,\mu\text{H}$ and the current just before turn-OFF is $12 \text{ A}$. Then

$$E_L = \frac{1}{2}\times 2\times 10^{-6}\times 12^2 = 144\times 10^{-6}\text{ J} = 144\,\mu\text{J}.$$

At first glance, $144\,\mu\text{J}$ may not sound large. But now imagine that, for a brief moment, this energy can charge only about $200 \text{ pF}$ of effective node capacitance. Using the capacitor-energy relation $E=\tfrac{1}{2}CV^2$, the equivalent voltage associated with that energy is

$$V \approx \sqrt{\frac{2E}{C}} = \sqrt{\frac{2\times 144\times 10^{-6}}{200\times 10^{-12}}} \approx 1200 \text{ V}.$$

This does not mean the real circuit will always reach exactly $1200 \text{ V}$. Real circuits distribute energy through several paths. But it does show why a converter running from a few hundred volts can still produce a much larger transient spike if we do nothing to control it.

A **snubber circuit** is added precisely to shape this transient. It gives the unwanted energy a less dangerous path. Depending on topology, a snubber can:

- limit the rate of rise of voltage across a device,
- limit peak overvoltage,
- limit turn-ON current surge,
- reduce ringing,
- reduce false triggering of thyristors,
- reduce stress caused by diode reverse recovery,
- trade a small controlled power loss for a large improvement in device safety [Rashid, *Power Electronics: Circuits, Devices and Applications, 4e*], [onsemi AN1048/D].

Table 7.1 collects the main reasons snubbers appear.

Table 7.1: Why snubber circuits are used

| Problem in the power stage | What the snubber tries to do | Typical consequence if no snubber is used |
|---|---|---|
| Stray or leakage inductance stores energy | Provide a controlled path for that energy | Overvoltage spike at turn-OFF |
| Device or load capacitances resonate with inductance | Add damping or clamp voltage | Ringing, EMI, repeated stress |
| SCR or TRIAC sees rapid voltage rise | Reduce effective $dv/dt$ across device | False turn-ON |
| Inductive load current has nowhere to go when switch opens | Provide recirculation path | Very large voltage spike or device avalanche |
| Diode reverse recovery interacts with switch turn-ON | Soften or absorb part of the transient | High turn-ON current stress and noise |

#### What a snubber really is

A useful beginner definition is this:

A **snubber circuit** is a small auxiliary network placed around a switching element or energy-storage element to control transient voltage, transient current, or oscillation during switching.

This definition is deliberately broad, because power electronics uses the word "snubber" in more than one way. Some snubbers are mainly **dissipative**, meaning they absorb transient energy and convert it into heat in a resistor. Others are mainly **clamping** networks, steering the energy into a capacitor first and then removing it later. Some are associated mainly with the switch; others are associated mainly with the diode or the inductive load. A freewheeling diode is often discussed in the same chapter as snubbers because it performs the same family of job: it gives inductive current a safe path when the main switch state changes.

The most important mindset is not to memorize the names first. The first question should always be:

Where will the stored energy go at the instant of switching?

If the answer is "through a controlled auxiliary path," the stress will usually be manageable. If the answer is "wherever parasitics force it to go," then voltage spikes and ringing will often decide the behavior.

#### Turn-OFF stress and turn-OFF snubbers

A **turn-OFF snubber** mainly helps during the interval when the power device is being turned OFF and the current through a stray inductive path wants to continue flowing.

This is the most familiar snubber situation. A switch current is falling quickly, so the stray inductance produces a voltage according to the inductor relation

$$v_L = L\frac{di}{dt}.$$

If $\tfrac{di}{dt}$ is large and there is no alternative path, the voltage across the switch rises sharply. A turn-OFF snubber softens that event by giving the current a temporary destination. In practice:

- an RC snubber lets a capacitor take some of the sudden voltage rise while the resistor damps the oscillation,
- an RCD snubber lets a diode conduct only when the voltage exceeds a chosen level and then stores the energy in a capacitor before dissipating it in a resistor,
- a clamp or freewheel path can keep the switch from seeing the full stress directly [onsemi AN1048/D], [onsemi AN4137].

One simple way to see the effect of a snubber capacitor is to recall the capacitor current law:

$$\boxed{i_C = C\frac{dv}{dt}} \quad \text{(7.2)}$$

or rearranged,

$$\frac{dv}{dt} = \frac{i_C}{C}.$$

This tells us something very practical. If a transient current must charge a capacitor, then a larger capacitor causes the voltage to rise more slowly. That is exactly why a capacitor across a switch can reduce $dv/dt$.

But we must not jump to the beginner mistake of thinking that "bigger capacitor is always better." A larger capacitor:

- reduces $dv/dt$,
- but stores more energy,
- may create more loss,
- and can increase turn-ON current when the switch closes again.

So snubber design is always a compromise. onsemi states this clearly in its thyristor snubber note: snubber design involves compromises among cost, voltage rate, peak voltage, and turn-ON stress [onsemi AN1048/D].

#### Turn-ON stress and turn-ON snubbers

A **turn-ON snubber** mainly helps during the interval when the device is being turned ON.

At first, this may feel surprising. Why would turn-ON be stressful? The answer is that a device being turned ON may suddenly encounter:

- discharge current from a previously charged snubber capacitor,
- reverse-recovery current from a diode that had been conducting,
- current surge into a capacitive node,
- large $di/dt$ determined not by the load alone, but by parasitics and recovery behavior.

ST's application note on gate and base drive makes an important point here: in many inductive-load applications, turn-ON occurs while the freewheeling diode is conducting, and the reverse recovery of that diode influences the device current rise and switching loss [ST AN509/1293]. In other words, turn-ON stress is often not only about the transistor; it is also about what the diode was doing just before the transistor turned ON.

A classical turn-ON snubber may place inductance, capacitance, or diode steering so that the switch does not see a brutal current rise at the instant of turn-ON. In modern textbooks and application notes, the term is used somewhat differently across topologies, so at beginner level it is safest to understand the purpose rather than memorize every variant:

- a turn-OFF snubber mainly restrains voltage rise and turn-OFF spike,
- a turn-ON snubber mainly restrains current surge and turn-ON stress.

**Image prompt for Figure 7.1:** Create a clean textbook-style technical illustration comparing unsnubbed and snubbed switch turn-OFF in an inductive circuit. Show a power switch carrying inductive current, a small stray inductance in the loop, and two aligned voltage waveforms across the switch: one with a sharp overshoot and ringing, one with a slower controlled rise and lower peak due to a snubber. Label stored energy in stray inductance, voltage overshoot, ringing, and controlled transient. Use monochrome engineering style with axes, units, and clear labels.

#### A practical way to classify snubbers

At beginner level, we can classify snubbers in a useful practical way:

1. **Across-the-switch snubbers**: usually intended to reduce switch voltage stress.
2. **Clamp snubbers**: usually intended to prevent a node from exceeding a chosen voltage too much.
3. **Load-current recirculation paths**: usually intended to give inductive current a safe path after switching.
4. **Diode snubbers**: usually intended to reduce ringing or recovery stress associated with rectifier diodes.

This chapter focuses on the syllabus items that matter most in foundational power electronics: RC, RCD, and the freewheeling diode.

#### Common misconceptions at this stage

Three misconceptions are worth correcting early.

The first misconception is that a snubber is optional decoration added only after a circuit "mostly works." In reality, many power circuits work safely only because the snubber is present.

The second misconception is that a freewheeling diode and an RC snubber are interchangeable. They are not. A freewheeling diode gives the inductive load current a path. An RC snubber mainly controls voltage rise or ringing. In some circuits both are needed.

The third misconception is that if a device has avalanche capability or a high voltage rating, no snubber is needed. Voltage rating is necessary, but repeated transient stress still affects reliability, EMI, and switching loss. A rugged device is not a substitute for good transient control.

*Renewable-energy relevance.* Snubbers matter in PV converters because high-frequency switching and wiring inductance easily create overshoot. They matter in battery chargers because inductors and transformers store energy every cycle. They matter in small wind or UPS converters because bridge legs and rectifier paths contain both switch and diode transients. In renewable-energy hardware, efficiency and reliability are both important, and snubbers sit exactly at that intersection.

### 2.2.2 RC and RCD snubber circuits; freewheeling diode

#### RC snubber circuits

The simplest named snubber is the **RC snubber**, a resistor and capacitor connected in series and placed across a device or across a problematic node.

Its logic is easy to understand if we assign one job to each component:

- the **capacitor** slows the voltage change because current must charge it first,
- the **resistor** damps the oscillation and limits the current that would otherwise flow too sharply into or out of the capacitor.

If we used only a capacitor, the circuit might reduce the initial $dv/dt$ but could create heavy current pulses and strong resonant ringing with the stray inductance. If we used only a resistor, the voltage spike would usually still be too sharp. The series RC combination is used because it controls both the first transient and the ringing behavior.

In time-domain language, the RC pair introduces a time constant

$$\boxed{\tau = RC} \quad \text{(7.3)}$$

where $\tau$ is the RC time constant, $R$ is the snubber resistance, and $C$ is the snubber capacitance.

This equation by itself does not fully design the snubber, but it does help us reason:

- larger $C$ means slower voltage rise,
- larger $R$ means gentler current pulse and stronger damping effect,
- too much of either can increase loss or slow the transition more than desired.

##### RC snubbers across thyristors

One classical use of the RC snubber is across an SCR or TRIAC. onsemi's application note AN1048/D describes the simple snubber as a series resistor and capacitor placed around the thyristor, and explains that RC networks are used to control voltage transients that could falsely turn on a thyristor [onsemi AN1048/D].

This is a very important historical use because the SCR is sensitive to rapid $dv/dt$. If the anode-cathode voltage rises too quickly, the internal junction capacitances can drive enough current into the regenerative structure to trigger the device even without an intentional gate command. So the RC snubber across an SCR is not mainly there to improve efficiency. It is there to prevent unwanted turn-ON and to control transient behavior.

**Image prompt for Figure 7.2:** Create a textbook-style figure showing an SCR with a series RC snubber connected across anode and cathode. Include a corresponding waveform panel that compares voltage across the SCR with and without the snubber during a transient. Label anode, cathode, gate, snubber resistor, snubber capacitor, false-triggering risk, and reduced $dv/dt$. Use monochrome engineering style with clear engineering labels.

##### RC snubbers across transistor switches

RC snubbers are also used with MOSFETs, IGBTs, and diodes to reduce ringing on a switch node or across a device. The goal here is often less about false triggering and more about:

- limiting overshoot,
- damping resonance caused by stray inductance and node capacitance,
- reducing EMI,
- lowering repetitive stress on the semiconductor.

The price is power loss. Every cycle, the snubber capacitor is charged and discharged. A useful first estimate for the average power associated with that repetitive charging is

$$\boxed{P_{RC,\text{approx}} \approx \frac{1}{2}CV^2 f_s} \quad \text{(7.4)}$$

where $P_{RC,\text{approx}}$ is the approximate average snubber-related power, $C$ is the snubber capacitance, $V$ is the voltage swing across it, and $f_s$ is switching frequency.

This is a simplified first estimate, not a complete exact model, because the real loss distribution depends on topology, waveform, and how fully the capacitor charges and discharges. But it is a very useful warning sign.

Consider a converter switching at $20 \text{ kHz}$ with an RC snubber capacitor of $1 \text{ nF}$ that experiences about $325 \text{ V}$ each cycle in an off-line stage. Then

$$P_{RC,\text{approx}} \approx \frac{1}{2}\times 1\times 10^{-9}\times 325^2\times 20\times 10^3 \approx 1.06 \text{ W}.$$

That is not negligible. So an RC snubber may be electrically simple, but thermally it is real. The resistor must be chosen and mounted so that this heat can be dissipated safely.

##### What an RC snubber cannot do alone

An RC snubber is very good at damping and slowing a transient. But it does not magically remove all stored energy without consequence. If the transient energy is large and repetitive, the resistor must absorb it. That is why RC snubbers are common where the stress is moderate and the goal is mainly waveform shaping rather than heavy energy clamping.

#### RCD snubber circuits

An **RCD snubber** adds a diode to the resistor-capacitor network. This gives the circuit a directional behavior. Instead of the capacitor always being directly involved in both polarities of voltage change, the diode allows the snubber to conduct mainly when the node tries to exceed a certain level in the dangerous direction.

This makes the RCD snubber especially useful in circuits such as the flyback converter primary switch, where transformer leakage inductance produces a turn-OFF spike at the switch drain or collector. onsemi's AN4137 places an RCD snubber directly in the basic off-line flyback reference schematic and treats its design as a dedicated step in the converter design process [onsemi AN4137].

The physical story is:

1. The switch turns OFF.
2. Leakage inductance tries to keep current flowing.
3. The switch voltage rises.
4. When that voltage rises above the clamp path condition, the snubber diode conducts.
5. Energy is diverted into the snubber capacitor.
6. The resistor then dissipates that stored energy between switching events.

So the RCD snubber is a **clamp-plus-dissipation** network. It does not usually eliminate loss. Instead, it moves that loss away from the fragile switching transient and into a more controlled passive path.

##### First energy estimate for an RCD snubber

If we make the beginner-level assumption that most of the transformer leakage energy each cycle ends up being dissipated through the RCD network, then a useful first estimate is

$$\boxed{P_{RCD,\text{approx}} \approx \frac{1}{2}L_{lk} I_{pk}^2 f_s} \quad \text{(7.5)}$$

where $L_{lk}$ is the leakage inductance, $I_{pk}$ is the peak current present when the switch turns OFF, and $f_s$ is switching frequency.

This estimate is simple, but very powerful. It tells us that the average burden of the snubber scales directly with:

- leakage inductance,
- square of current,
- switching frequency.

Consider a small isolated auxiliary supply in a wind-converter control cabinet or a PV inverter control board. Suppose

- $L_{lk} = 3\,\mu\text{H}$,
- $I_{pk} = 2.5 \text{ A}$,
- $f_s = 65 \text{ kHz}$.

Then

$$P_{RCD,\text{approx}} \approx \frac{1}{2}\times 3\times 10^{-6}\times 2.5^2\times 65\times 10^3 \approx 0.61 \text{ W}.$$

Again, that is not huge, but it is very real. It also tells us something deeper: reducing transformer leakage inductance reduces the snubber burden directly.

##### Why the diode matters

Without the diode, an RC network across a switch may participate in both the voltage-rise and voltage-fall events. With the diode added, the snubber can be made more selective. That means:

- lower unnecessary current in the benign part of the cycle,
- more focused clamping of the dangerous transient,
- often better control of peak voltage in flyback and related circuits.

Fairchild's AN-6014 distinguishes diode RC snubber design from MOSFET RCD snubber design, which is a useful reminder that different transient problems need different auxiliary networks [Fairchild AN-6014].

##### RC versus RCD in plain language

An RC snubber says, "I will be present whenever this node moves, and I will damp the motion."

An RCD snubber says, "I will step in mainly when this node tries to overshoot in the dangerous direction, and I will clamp that event more selectively."

That is why RCD networks are especially common around flyback primary switches, while simple RC networks are often used for damping ringing or controlling $dv/dt$ across SCRs, TRIACs, MOSFETs, or diodes.

**Image prompt for Figure 7.3:** Create a textbook-style schematic of a flyback converter primary showing a MOSFET switch, transformer primary, leakage inductance indicated, and an RCD snubber made of diode $D_{sn}$, capacitor $C_{sn}$, and resistor $R_{sn}$ connected as a clamp from the switch node to the DC input rail. Add a waveform panel showing drain voltage rising to reflected output voltage plus input voltage, then a leakage-induced spike, with the RCD clamp limiting the peak. Label all parts, polarities, and current path during turn-OFF. Use monochrome engineering style.

#### The freewheeling diode

The **freewheeling diode**, also called a **flyback diode** or **freewheel diode** in many contexts, is one of the most important protective elements in power electronics.

Its job is different from that of a simple RC snubber, even though both address switching transients.

When a switch controlling an inductive current turns OFF, the inductor current cannot instantly become zero. If a diode is connected so that it becomes forward-biased at that moment, the current can continue circulating through the load and diode instead of forcing the switch voltage to rise destructively.

In plain words, the freewheeling diode gives the inductor current somewhere safe to go.

This matters in:

- DC choppers,
- buck converters,
- motor drives,
- relay and solenoid circuits,
- inverter legs during dead time,
- many rectifier and current-commutation situations [Mohan, Undeland, Robbins, *Power Electronics*], [ST STTH60AC06C Product Page].

ST describes the STTH60AC06C as intended for use as a freewheeling diode in power supplies and other power-switching applications [ST STTH60AC06C Product Page]. ST also describes the SiC diode STPSC40065C as usable as a freewheeling or output rectification diode and notes that, due to its Schottky construction, it shows no recovery at turn-OFF in the application current range [ST STPSC40065C Product Page]. These statements are very helpful because they tell us what experienced manufacturers expect such diodes to do in practice.

##### Current decay with a freewheeling diode

When the current freewheels through a diode, the inductor sees only a small reverse voltage, roughly the diode forward drop plus any resistive drops in the loop. A useful first approximation is

$$\boxed{\frac{di}{dt} \approx -\frac{V_F}{L}} \quad \text{(7.6)}$$

where $V_F$ is the effective forward drop of the recirculating path and $L$ is the inductance.

This equation explains a key design tradeoff.

Suppose a $2 \text{ mH}$ inductor is carrying $5 \text{ A}$ when the main switch turns OFF, and the freewheeling path imposes about $1 \text{ V}$ across the inductor. Then

$$\frac{di}{dt} \approx -\frac{1}{2\times 10^{-3}} = -500 \text{ A/s}.$$

The current therefore takes about

$$t \approx \frac{5}{500} = 0.01 \text{ s} = 10 \text{ ms}$$

to fall to zero in this simplified estimate.

This is a very important lesson. A diode freewheel path gives low voltage stress, but it also causes slow current decay because the reverse voltage across the inductor is small.

If, instead, a higher clamp voltage were allowed, the current would fall faster. So the designer always balances:

- lower voltage stress,
- against slower current decay,
- and against the needs of control, efficiency, and EMI.

##### Freewheeling diode versus snubber: not the same thing

The freewheeling diode is often taught alongside snubbers because it protects the circuit during switching, but its primary function is different.

- An RC snubber mainly shapes a transient.
- An RCD snubber mainly clamps a transient more selectively.
- A freewheeling diode mainly provides a recirculating path for inductive load current.

In many circuits, the freewheeling diode handles the main inductive current path, while a separate RC or RCD snubber still handles ringing and stray-inductance stress. So the presence of one does not automatically remove the need for the other.

##### Why diode type matters

Not every diode is equally suitable as a freewheeling diode. The designer must care about:

- repetitive reverse voltage rating,
- average forward current,
- peak forward current,
- reverse recovery behavior,
- thermal capability.

This is why ultrafast and Schottky or silicon-carbide diodes are often preferred in high-frequency converters. ST explicitly notes that the STPSC40065C SiC Schottky has no reverse recovery in the application current range, and that kind of behavior can strongly reduce switching stress and ringing in real converters [ST STPSC40065C Product Page].

ST's older drive note also reminds us that, at turn-ON, the switching transistor often encounters the recovery behavior of the conducting freewheeling diode [ST AN509/1293]. This is one of the clearest reasons why diode selection is not a side issue. It directly affects switch stress.

Table 7.2 summarizes the three main elements of this chapter.

Table 7.2: RC snubber, RCD snubber, and freewheeling diode compared

| Network | Main purpose | Main strength | Main tradeoff | Typical place |
|---|---|---|---|---|
| RC snubber | Reduce $dv/dt$ and damp ringing | Simple and widely applicable | Continuous loss and extra turn-ON burden | Across SCR, TRIAC, switch, or diode |
| RCD snubber | Clamp overvoltage more selectively | Better suited to leakage-spike control | Dissipates leakage energy and needs tuning | Flyback primary switch, clamp node |
| Freewheeling diode | Provide path for inductive current after switch state change | Strong reduction of voltage stress from interrupted load current | Slow current decay if clamp voltage is low | Across inductive load or as recirculation path in converter leg |

##### A practical example from renewable-energy hardware

Imagine a small isolated flyback auxiliary supply inside a grid-tied PV inverter. The main DC bus may be several hundred volts, but the control electronics still need low-voltage rails such as 15 V and 5 V. The flyback transformer will have some leakage inductance. When the MOSFET turns OFF, that leakage inductance will generate a spike at the drain. An RCD snubber is a common way to keep that spike within safe limits [onsemi AN4137].

Now imagine, separately, a buck converter charging a battery from a lower DC source. When the main switch turns OFF, the inductor current must keep flowing. Here the freewheeling diode is not optional. It is a fundamental current path. If the switching frequency is high and efficiency is important, the diode's reverse-recovery behavior becomes very important, and an additional RC snubber may still be added if ringing remains problematic.

So the right question is never "Which one is the snubber?" The right question is "What transient problem are we solving in this topology?"

*Renewable-energy relevance.* RC and RCD snubbers appear in flyback bias supplies for PV and wind converters, in isolated charger power supplies, and in control-power stages inside industrial renewable-energy equipment. Freewheeling diodes appear in buck and boost stages, motor drives, relay and contactor interfaces, and inverter commutation paths. These are not rare details. They are part of the normal hardware vocabulary of renewable-energy power conversion.

## Worked interpretation exercise

We will read a real artifact that is closely matched to this chapter:

- the [onsemi AN4137 application note, *Design Guidelines for Off-line Flyback Converters Using Fairchild Power Switch*](https://www.onsemi.com/pub/Collateral/AN-4137.pdf)

This document is useful because its basic converter schematic explicitly includes an RCD snubber labeled with $R_{sn}$, $C_{sn}$, and $D_{sn}$ [onsemi AN4137].

### Step 1: Identify where the snubber is placed

In Figure 1 of the note, the snubber parts are placed around the primary switch node of the flyback converter, not on the low-voltage output side [onsemi AN4137]. That immediately tells us what problem is being addressed. The snubber is meant to control the voltage stress seen by the primary-side switch when it turns OFF.

This is the first good habit in reading any converter schematic: look at where the auxiliary network lives. Placement usually reveals purpose.

### Step 2: Read the diode orientation

The presence and direction of $D_{sn}$ tell us that this is not a simple always-active RC damper. It is a directional clamp. The diode allows the snubber path to conduct mainly when the switch-node voltage rises in the dangerous direction above the clamp level. That is the signature of an RCD snubber rather than a plain RC snubber.

So, from topology alone, we can already infer:

- the designer expects a turn-OFF overvoltage event,
- the event is one-sided in polarity,
- and the chosen solution is selective clamping rather than simple symmetric damping.

That inference is not guesswork. It follows directly from the diode's presence and placement.

### Step 3: Interpret each component by function

The capacitor $C_{sn}$ is the temporary energy receiver. During the spike, it takes charge and therefore limits how rapidly and how far the node voltage rises.

The resistor $R_{sn}$ is the energy-removal path. After the transient, it bleeds away the energy that the capacitor stored, converting it into heat.

The diode $D_{sn}$ makes the path directional so the snubber acts mainly when needed.

This is a good example of how a converter schematic becomes readable once you stop seeing the snubber as "extra parts" and instead see it as an energy-management path.

### Step 4: Connect the artifact to the physical cause

AN4137 also treats RCD snubber design as a distinct design step, which confirms that the leakage-induced spike is not an afterthought but a normal part of flyback design [onsemi AN4137]. In a flyback converter, transformer leakage inductance is unavoidable. The RCD snubber exists because that leakage energy must be handled somewhere every switching cycle.

This is the design sentence we should take away:

The RCD snubber in a flyback converter is a controlled place for leakage-inductance energy to go when the primary switch turns OFF.

### Step 5: Relate it to renewable-energy hardware

Why is this artifact useful beyond a textbook example? Because small isolated flyback supplies are very common inside larger renewable-energy systems. A solar inverter, wind converter controller, EV charger, or UPS often includes one or more off-line or high-voltage auxiliary power supplies for control electronics, sensing, fans, relays, and communication boards. Those small supplies frequently use the same kind of primary-switch RCD snubber shown here.

So when you see $R_{sn}$, $C_{sn}$, and $D_{sn}$ grouped near a flyback switch node in a real schematic, you should now be able to read the intention immediately.

## How this matters in renewable-energy systems

Snubber circuits are deeply connected to renewable-energy reliability because renewable-energy converters switch substantial current repeatedly, often for many hours every day and often in thermally demanding environments.

In **solar PV systems**, snubbers appear in isolated auxiliary supplies, DC-DC stages, and inverter legs to keep switching stress within device limits and to reduce ringing that would otherwise worsen EMI. In **battery chargers** and **battery-energy-storage converters**, freewheeling paths and snubbers determine how safely the inductor current commutates when switches change state. In **wind-energy converters**, transformer leakage inductance and converter-leg stray inductance make overvoltage control essential. In **EV power stages** and **UPS systems**, the same ideas appear again: recirculating current paths, diode recovery, clamp networks, and the tradeoff between stress, efficiency, and switching speed.

There is also a practical system-level lesson here. Renewable-energy systems are judged not only by efficiency, but also by robustness, service life, and electromagnetic behavior. A converter that is a little more efficient on paper but suffers repeated overshoot, diode-recovery stress, or false triggering is not a better converter in practice. Snubbers are one of the places where experienced power-electronics design shows its maturity.

## Chapter summary

- A **snubber circuit** is an auxiliary network used to control transient voltage, transient current, or oscillation during switching [Rashid, *Power Electronics: Circuits, Devices and Applications, 4e*].
- Snubbers are needed because real power circuits contain stray or leakage inductance, capacitance, stored energy, and switching transitions.
- The energy stored in stray or leakage inductance is
  $\boxed{E_L=\tfrac{1}{2}L_{\sigma}I^2}$ from Equation (7.1).
- A capacitor can reduce voltage-rise rate because
  $\boxed{i_C=C\,dv/dt}$ from Equation (7.2).
- A **turn-OFF snubber** mainly reduces voltage overshoot and turn-OFF stress.
- A **turn-ON snubber** mainly reduces current surge and turn-ON stress, often in the presence of diode reverse recovery [ST AN509/1293].
- A series **RC snubber** uses the capacitor to slow the transient and the resistor to damp it.
- The RC time constant is
  $\boxed{\tau=RC}$ from Equation (7.3).
- A useful first estimate of repetitive RC-snubber power is
  $\boxed{P_{RC,\text{approx}}\approx \tfrac{1}{2}CV^2f_s}$ from Equation (7.4).
- onsemi's thyristor note explains that RC snubbers are used to control transients that could falsely turn on a thyristor and that snubber design is always a compromise [onsemi AN1048/D].
- An **RCD snubber** adds a diode so that the clamp acts more selectively, which is especially useful for leakage-induced turn-OFF spikes in flyback converters [onsemi AN4137].
- A useful first estimate of RCD-snubber dissipation when leakage energy is burned each cycle is
  $\boxed{P_{RCD,\text{approx}}\approx \tfrac{1}{2}L_{lk}I_{pk}^2f_s}$ from Equation (7.5).
- A **freewheeling diode** gives inductive current a safe recirculation path when the main switch changes state.
- A first current-decay estimate in a diode freewheel path is
  $\boxed{di/dt\approx -V_F/L}$ from Equation (7.6).
- Freewheeling diodes reduce voltage stress strongly, but because the clamp voltage is low, current decay can be slow.
- Fast, ultrafast, Schottky, and SiC diodes are often preferred in high-frequency converters because reverse-recovery behavior directly affects switching stress [ST STTH60AC06C Product Page], [ST STPSC40065C Product Page].

## Further reading

- [onsemi, *AN1048/D: RC Snubber Networks for Thyristor Power Control and Transient Suppression*](https://www.onsemi.com/download/application-notes/pdf/an1048-d.pdf) - A very useful classic reference for understanding why snubbers are needed, especially for SCR $dv/dt$ control and the tradeoffs involved.
- [onsemi, *AN4137: Design Guidelines for Off-line Flyback Converters Using Fairchild Power Switch*](https://www.onsemi.com/pub/Collateral/AN-4137.pdf) - Helpful for seeing an RCD snubber in a real flyback schematic and understanding its place in practical converter design.
- [Fairchild Semiconductor, *AN-6014: Green Current Mode PWM Controller FAN7602*](https://www.onsemi.com/download/application-notes/pdf/an-6014.pdf) - Useful because it distinguishes diode RC snubber design from MOSFET RCD snubber design in a real SMPS design context.
- [STMicroelectronics, *Influence of gate and base drive on power switch behaviour*](https://www.st.com/resource/en/application_note/cd00003914-influence-of-gate-and-base-drive-on-power-switch-behaviour-stmicroelectronics.pdf) - Especially useful for the link between switch turn-ON stress and the reverse recovery of the conducting freewheeling diode.
- M. H. Rashid, *Power Electronics: Circuits, Devices and Applications*, 4th ed. - A strong textbook reference for the broader role of snubbers, freewheeling diodes, and switching-stress control across converter families.
