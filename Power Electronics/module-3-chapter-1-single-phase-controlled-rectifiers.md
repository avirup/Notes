# Chapter 3.1: Single-phase Controlled Rectifiers

## Chapter opening

Previous chapters treated the SCR primarily as a device: its latching behavior, triggering, protection, and thermal limits. This chapter turns that device into a converter. A controlled rectifier uses SCRs to convert AC to DC while controlling the instant at which conduction begins in each cycle [Rashid, *Power Electronics: Circuits, Devices and Applications*, 4e, Ch. 6], [Mohan, Undeland, Robbins, *Power Electronics: Converters, Applications and Design*, 3e, Ch. 6].

Control of the conduction interval is useful whenever the DC side must be adjustable rather than fixed. Battery chargers, DC drives, soft-start circuits, and line-frequency front ends all use delayed firing to vary average output. This chapter develops that idea through the single-phase half-wave controlled rectifier, the fully controlled bridge, and the semi-controlled bridge, and then collects the average- and RMS-voltage expressions used later in the module [Littelfuse AN1003].

## Prerequisites check

- You should remember from Chapter 1.2 that an SCR can be triggered by a gate pulse but does not turn OFF by gate control in ordinary operation.
- You should be comfortable with sinusoidal AC voltage, including the relation between RMS value and peak value.
- You should know that a resistor makes current follow voltage, while an inductor resists sudden change of current.
- You should remember from Chapter 2.1 that firing pulses must be synchronized correctly with the AC waveform.
- You should remember from Chapter 2.2 that an inductive load often needs a freewheeling path when the main source is removed.

If SCR latching and natural turn-off are unclear, review Chapter 1.2. If average value and RMS value are not yet comfortable, review those now before continuing.

### 3.1.1 Single-phase half-wave controlled rectifier with R and R-L loads; effect of freewheeling diode

#### Phase control in the half-wave rectifier

In the single-phase half-wave controlled rectifier, an SCR is connected in series with the load and the AC source. During each positive half-cycle the SCR is forward biased, but forward bias alone does not produce conduction. The device conducts only after a gate pulse is applied. Delaying the gate pulse by an angle $\alpha$ delays conduction and therefore controls the average output voltage [Littelfuse AN1003], [Rashid, *Power Electronics: Circuits, Devices and Applications*, 4e, Ch. 6].

The supply is written as

$$\boxed{V_m = \sqrt{2}\,V_{s,rms}} \quad \text{(10.1)}$$

where $V_{s,rms}$ is the RMS value of the sinusoidal source and $V_m$ is its peak value.

For a 230 V, 50 Hz single-phase supply,

$$V_m = \sqrt{2}\times 230 \approx 325 \text{ V}.$$

The 230 V RMS mains value therefore corresponds to a peak of about 325 V.

The firing instant is described by the **firing angle** $\alpha$, measured from the zero crossing of the positive half-cycle. If the SCR is triggered at $\omega t = \alpha$, conduction begins at that angle provided the load current exceeds the holding current [Mohan, Undeland, Robbins, *Power Electronics: Converters, Applications and Design*, 3e, Ch. 6], [ST AN4607].

**Image prompt for Figure 10.1:** Create a clean textbook-style technical illustration of a single-phase half-wave controlled rectifier using one SCR and a load. Include three vertically aligned waveform plots versus electrical angle $\omega t$: source voltage $v_s$, gate pulse train showing a pulse at firing angle $\alpha$ in each positive half-cycle, and output voltage $v_o$ for a resistive load that is zero from $0$ to $\alpha$ and follows the positive sine wave from $\alpha$ to $\pi$. Clearly mark $0$, $\alpha$, $\pi$, and $2\pi$. Use monochrome engineering style with axes and units.

#### Half-wave controlled rectifier with R load

With a purely resistive load, current and voltage are in phase. After the SCR is fired at angle $\alpha$, the output voltage follows the source until the current falls to zero at $\omega t = \pi$. The SCR then turns OFF by line commutation, because the AC supply itself drives the current to zero [Rashid, *Power Electronics: Circuits, Devices and Applications*, 4e, Ch. 6].

For an R load:

- from $0$ to $\alpha$, the SCR blocks and $v_o = 0$,
- from $\alpha$ to $\pi$, the SCR conducts and $v_o = V_m\sin\omega t$,
- from $\pi$ to $2\pi$, the source is negative, the SCR is reverse biased, and $v_o = 0$.

The average output voltage over one full cycle is therefore

$$\boxed{V_{o,avg} = \frac{V_m}{2\pi}(1+\cos\alpha)} \quad \text{(10.2)}$$

[Rashid, *Power Electronics: Circuits, Devices and Applications*, 4e, Ch. 6], [Mohan, Undeland, Robbins, *Power Electronics: Converters, Applications and Design*, 3e, Ch. 6].

For a 230 V RMS source, $V_m \approx 325 \text{ V}$. If the firing angle is $\alpha = 60^\circ$, then $\cos 60^\circ = 0.5$, so

$$V_{o,avg} = \frac{325}{2\pi}(1+0.5) \approx 77.6 \text{ V}.$$

Phase control does not reduce the peak of the source. It changes the portion of the positive half-cycle that is applied to the load.

#### Half-wave controlled rectifier with R-L load

With a series R-L load, the current cannot change instantaneously. When the source voltage passes through zero, energy stored in the inductor can keep the current flowing, so conduction may continue into the negative half-cycle.

During SCR conduction, the load current satisfies

$$\boxed{L\frac{di_o}{dt} + Ri_o = V_m\sin\omega t} \quad \text{(10.3)}$$

where $L$ is the inductance, $R$ is the resistance, and $i_o$ is the load current.

Instead of ending at $\pi$, conduction may continue to an **extinction angle** $\beta$, where $\beta > \pi$ [Rashid, *Power Electronics: Circuits, Devices and Applications*, 4e, Ch. 6]. Two consequences follow:

- the output voltage becomes negative between $\pi$ and $\beta$ while the SCR continues conducting,
- the average output voltage becomes smaller than in the resistive-load case for the same firing angle.

If device drops are neglected, the average output voltage over one cycle is

$$\boxed{V_{o,avg} = \frac{V_m}{2\pi}(\cos\alpha - \cos\beta)} \quad \text{(10.4)}$$

where $\beta$ depends on $R$, $L$, the source frequency, and the firing angle [Mohan, Undeland, Robbins, *Power Electronics: Converters, Applications and Design*, 3e, Ch. 6].

The reduction in average output is the direct result of the negative-voltage interval introduced by continued inductive current.

#### Effect of a freewheeling diode

A freewheeling diode connected across the load provides an alternate current path when the source voltage becomes negative. The inductive current then circulates through the load and diode instead of through the source and SCR [Rashid, *Power Electronics: Circuits, Devices and Applications*, 4e, Ch. 6], [Mohan, Undeland, Robbins, *Power Electronics: Converters, Applications and Design*, 3e, Ch. 6].

The output-voltage waveform changes as follows:

- from $0$ to $\alpha$, $v_o = 0$,
- from $\alpha$ to $\pi$, the SCR conducts and $v_o = V_m\sin\omega t$,
- from $\pi$ onward, the freewheeling diode conducts, current continues through the load, and the load voltage is approximately zero.

The average output voltage becomes

$$\boxed{V_{o,avg} = \frac{V_m}{2\pi}(1+\cos\alpha)} \quad \text{(10.5)}$$

The expression matches the half-wave resistive case because the diode removes the negative load-voltage interval, even though the current waveform remains inductive.

**Image prompt for Figure 10.2:** Create a clean textbook-style technical illustration comparing a single-phase half-wave controlled rectifier with an R-L load, first without and then with a freewheeling diode across the load. Show two output-voltage waveforms versus $\omega t$: in the first, the output follows the source from $\alpha$ to $\beta$ and becomes negative between $\pi$ and $\beta$; in the second, the output follows the source from $\alpha$ to $\pi$ and becomes approximately zero during the freewheeling interval. Also show corresponding load-current waveforms that continue after $\pi$. Label $\alpha$, $\pi$, $\beta$, and the freewheeling interval clearly. Use monochrome engineering style.

The freewheeling diode provides three practical benefits:

- it improves the average output voltage for the same firing angle,
- it eliminates the negative load-voltage interval,
- it smooths the load current and reduces the reactive burden on the source.

### 3.1.2 Single-phase full-wave fully controlled bridge rectifier with R and R-L loads

A half-wave circuit uses only one half-cycle of the supply. In practice, full-wave conversion is preferred because it uses the source more effectively, raises the ripple frequency at the output, and offers broader control flexibility. The **single-phase fully controlled bridge rectifier**, often called the **single-phase full converter**, achieves this using four SCRs [Rashid, *Power Electronics: Circuits, Devices and Applications*, 4e, Ch. 6].

#### Fully controlled bridge with R load

Let the SCR pairs be $(T_1,T_2)$ and $(T_3,T_4)$. With a resistive load, each pair conducts from the firing instant to the natural current zero of that half-cycle:

- $T_1$ and $T_2$ conduct from $\alpha$ to $\pi$,
- $T_3$ and $T_4$ conduct from $\pi+\alpha$ to $2\pi$.

The output therefore contains two positive pulses per source cycle. The average output voltage is

$$\boxed{V_{o,avg} = \frac{V_m}{\pi}(1+\cos\alpha)} \quad \text{(10.6)}$$

which is twice the half-wave resistive-load result [Mohan, Undeland, Robbins, *Power Electronics: Converters, Applications and Design*, 3e, Ch. 6].

For the same 230 V supply and $\alpha = 60^\circ$,

$$V_{o,avg} = \frac{325}{\pi}(1+0.5) \approx 155.2 \text{ V}.$$

This value is twice the half-wave result because both half-cycles are used.

#### Fully controlled bridge with R-L load and continuous current

With an R-L load and sufficiently large inductance, load current may remain continuous throughout the cycle. Each SCR pair then conducts for $180^\circ$ electrical, and commutation occurs when the next pair is fired [Rashid, *Power Electronics: Circuits, Devices and Applications*, 4e, Ch. 6].

The average output voltage becomes

$$\boxed{V_{o,avg} = \frac{2V_m}{\pi}\cos\alpha} \quad \text{(10.7)}$$

Three standard cases follow directly:

- if $\alpha = 0^\circ$, then $V_{o,avg} = \dfrac{2V_m}{\pi}$,
- if $\alpha = 90^\circ$, then $V_{o,avg} = 0$,
- if $\alpha > 90^\circ$, then $V_{o,avg}$ becomes negative.

A negative average output becomes possible because a continuous-current DC side can drive power back toward the AC source under line commutation. That operating region is the basis of **line-commutated inverter** behavior [Mohan, Undeland, Robbins, *Power Electronics: Converters, Applications and Design*, 3e, Ch. 6].

For a 230 V source:

- at $\alpha = 30^\circ$, $V_{o,avg} \approx \dfrac{2\times 325}{\pi}\times 0.866 \approx 179.3 \text{ V}$,
- at $\alpha = 75^\circ$, $V_{o,avg} \approx \dfrac{2\times 325}{\pi}\times 0.259 \approx 53.5 \text{ V}$,
- at $\alpha = 105^\circ$, $V_{o,avg} \approx \dfrac{2\times 325}{\pi}\times (-0.259) \approx -53.5 \text{ V}$.

By crossing $\alpha = 90^\circ$, the converter crosses from positive to negative average output.

**Image prompt for Figure 10.3:** Create a clean textbook-style technical illustration of a single-phase fully controlled bridge rectifier using four SCRs. Include two waveform sets. In the first set, show the R-load case with gate pulses for the two SCR pairs and output voltage pulses from $\alpha$ to $\pi$ and from $\pi+\alpha$ to $2\pi$. In the second set, show the R-L continuous-current case with nearly constant positive load current and output voltage that alternates between positive and negative segments according to the firing angle. Clearly label SCR pairs, $\alpha$, $\pi$, and the conduction intervals. Use monochrome textbook engineering style.

The fully controlled bridge therefore has a wider operating range than the half-wave circuit or the semi-converter.

### 3.1.3 Single-phase semi-controlled (half-controlled) bridge rectifier - concept

A **semi-controlled bridge rectifier**, also called a **half-controlled bridge** or **semi-converter**, uses two SCRs and two diodes. It sits between the diode bridge and the full SCR bridge: the output is adjustable, but only two devices require gate control [Rashid, *Power Electronics: Circuits, Devices and Applications*, 4e, Ch. 6], [Mohan, Undeland, Robbins, *Power Electronics: Converters, Applications and Design*, 3e, Ch. 6]. In each half-cycle one SCR and one diode conduct. With an inductive load, the diode arrangement also provides a natural freewheeling path.

#### Average output voltage of the semi-converter

For the standard inductive-load case with continuous current and ideal devices, the average output voltage is

$$\boxed{V_{o,avg} = \frac{V_m}{\pi}(1+\cos\alpha)} \quad \text{(10.8)}$$

For $0^\circ \le \alpha \le 180^\circ$, the term $(1+\cos\alpha)$ is never negative. The semi-converter therefore cannot produce negative average output voltage in normal operation and is a **one-quadrant converter** in the usual introductory sense.

#### Example: charger-type supply

Suppose an isolated secondary provides 18 V RMS to a single-phase semi-converter used in a small battery charger. Then

$$V_m = \sqrt{2}\times 18 \approx 25.5 \text{ V}.$$

If the firing angle is $\alpha = 60^\circ$,

$$V_{o,avg} = \frac{25.5}{\pi}(1+0.5) \approx 12.2 \text{ V}.$$

Changing $\alpha$ therefore changes the average DC output without requiring four controlled devices.

#### Operating features of the semi-converter

Because freewheeling occurs naturally, the load voltage does not go negative in the way it can for the full-controlled bridge under continuous-current conditions. The current is correspondingly smoother for many one-directional loads. The tradeoff is reduced control authority: negative average output voltage is not available.

Table 10.1 compares the three main single-phase topologies discussed in this chapter.

Table 10.1: Comparing single-phase controlled-rectifier topologies

| Topology | Controlled devices used | Uses both half-cycles? | Natural freewheeling path with inductive load? | Can average output become negative? | Typical application picture |
|---|---|---|---|---|---|
| Half-wave controlled rectifier | 1 SCR | No | No, unless a freewheeling diode is added | No practical inversion mode | Foundational teaching circuit, low-cost power control |
| Fully controlled bridge | 4 SCRs | Yes | No inherent freewheeling path | Yes, when current is continuous and $\alpha > 90^\circ$ | Controlled DC supplies, classical drives, line-commutated converters |
| Semi-controlled bridge | 2 SCRs + 2 diodes | Yes | Yes | No | Battery chargers, one-way variable DC front ends |

**Image prompt for Figure 10.4:** Create a clean textbook-style technical illustration of a single-phase semi-controlled bridge rectifier with two SCRs and two diodes feeding an R-L load. Show gate pulses only for the SCRs. Include output-voltage and load-current waveforms for continuous-current operation. Mark source-connected intervals where output follows the rectified sine wave, and freewheeling intervals where load voltage is approximately zero while current continues. Use monochrome engineering style with clear device labels and conduction intervals.

### 3.1.4 Expressions for average and RMS output voltage; effect of firing angle

Average output voltage measures the DC component delivered by the rectifier. RMS output voltage determines heating and effective power in resistive elements. Two rectifier waveforms can have the same average value and different RMS values, so both quantities are required in analysis [Littelfuse AN1003], [Mohan, Undeland, Robbins, *Power Electronics: Converters, Applications and Design*, 3e, Ch. 6].

#### RMS output voltage for half-wave controlled rectifier with R load

For the half-wave controlled rectifier with a resistive load,

$$V_{o,rms} = \sqrt{\frac{1}{2\pi}\int_{\alpha}^{\pi} V_m^2\sin^2\theta\,d\theta}.$$

Carrying out the integration gives

$$\boxed{V_{o,rms} = \frac{V_m}{2}\sqrt{1-\frac{\alpha}{\pi}+\frac{\sin 2\alpha}{2\pi}}} \quad \text{(10.9)}$$

The limiting cases are consistent. At $\alpha = 0^\circ$, $V_{o,rms} = V_m/2$, which is the known RMS value of an uncontrolled half-wave rectified sine wave. As $\alpha$ approaches $180^\circ$, the term inside the square root approaches zero, so the RMS output also approaches zero.

For the earlier 230 V example with $\alpha = 60^\circ$,

$$V_{o,rms} = \frac{325}{2}\sqrt{1-\frac{60^\circ}{180^\circ}+\frac{\sin 120^\circ}{2\pi}} \approx 145.8 \text{ V}.$$

In that case the average output is about 77.6 V, while the RMS output is about 145.8 V. The two quantities must not be confused.

#### RMS output voltage for full-wave R-load and semi-converter waveforms

For the single-phase fully controlled bridge with an R load, or for the semi-converter output-voltage waveform during source-connected intervals with ideal freewheeling, the RMS output becomes

$$\boxed{V_{o,rms} = \frac{V_m}{\sqrt{2}}\sqrt{1-\frac{\alpha}{\pi}+\frac{\sin 2\alpha}{2\pi}}} \quad \text{(10.10)}$$

This expression is larger than the half-wave RMS value because both half-cycles contribute. The limiting cases are again consistent:

- at $\alpha = 0^\circ$, $V_{o,rms} = V_m/\sqrt{2} = V_{s,rms}$,
- at $\alpha \to 180^\circ$, $V_{o,rms}\to 0$.

#### RMS output voltage for full-controlled bridge with continuous current

For the ideal single-phase fully controlled bridge with continuous current and negligible overlap, the output voltage at every instant is either $+v_s$ or $-v_s$. When it is squared for RMS calculation, the sign disappears. The RMS output voltage therefore equals the source RMS voltage:

$$\boxed{V_{o,rms} = V_{s,rms}} \quad \text{(10.11)}$$

The RMS value remains fixed because the waveform changes sign and timing, not its squared magnitude over the cycle.

#### Effect of firing angle

The firing angle affects more than the average output voltage. It changes:

- the average DC output,
- the RMS output in pulsed-output cases,
- the timing and distortion of the source current, and therefore the power factor,
- the boundary between discontinuous and continuous current in inductive loads [Rashid, *Power Electronics: Circuits, Devices and Applications*, 4e, Ch. 6], [Mohan, Undeland, Robbins, *Power Electronics: Converters, Applications and Design*, 3e, Ch. 6].

Table 10.2 collects the principal expressions from this chapter.

Table 10.2: Summary of important average and RMS expressions

| Circuit and load condition | Average output voltage | RMS output voltage | Main note |
|---|---|---|---|
| Half-wave controlled rectifier, R load | $\dfrac{V_m}{2\pi}(1+\cos\alpha)$ | $\dfrac{V_m}{2}\sqrt{1-\dfrac{\alpha}{\pi}+\dfrac{\sin 2\alpha}{2\pi}}$ | Conduction from $\alpha$ to $\pi$ |
| Half-wave controlled rectifier, R-L load without freewheeling diode | $\dfrac{V_m}{2\pi}(\cos\alpha-\cos\beta)$ | Depends on $\beta$ and exact current continuity | Negative output interval can appear |
| Half-wave controlled rectifier, R-L load with freewheeling diode | $\dfrac{V_m}{2\pi}(1+\cos\alpha)$ | Depends on current waveform | Freewheeling prevents negative output voltage |
| Fully controlled bridge, R load | $\dfrac{V_m}{\pi}(1+\cos\alpha)$ | $\dfrac{V_m}{\sqrt{2}}\sqrt{1-\dfrac{\alpha}{\pi}+\dfrac{\sin 2\alpha}{2\pi}}$ | Two positive pulses per cycle |
| Fully controlled bridge, R-L load, continuous current | $\dfrac{2V_m}{\pi}\cos\alpha$ | $V_{s,rms}$ | Average becomes negative for $\alpha>90^\circ$ |
| Semi-controlled bridge, continuous current | $\dfrac{V_m}{\pi}(1+\cos\alpha)$ | Same waveform trend as full-wave pulsed case when freewheeling intervals are ideal | One-quadrant operation |

## How this matters in renewable-energy systems

Single-phase controlled rectifiers are not the dominant form of modern low- and medium-power AC-DC conversion, but they remain foundational. Firing angle, natural commutation, current continuity, and freewheeling reappear throughout the study of controlled chargers, line-frequency converters, and higher-power front ends.

Thyristor-based AC-DC conversion also remains relevant where line-frequency operation and high power matter. Hitachi Energy notes the continued use of high-power thyristors in applications ranging from soft starters to HVDC converter stations [Hitachi Energy Thyristors], [Hitachi Energy HVDC Converter Stations]. At the same time, newer charger and converter designs often move toward PWM rectifiers for improved size and efficiency [NPTEL Line Commutated and PWM Rectifiers]. Controlled rectifiers therefore remain best understood as the classical basis from which modern AC-DC conversion is developed.

## Chapter summary

- A controlled rectifier controls the start of conduction by delaying SCR firing through the angle $\alpha$.
- In the half-wave rectifier, an R load gives Equation (10.2), while an R-L load can extend conduction to an extinction angle $\beta$ and reduce average output through a negative-voltage interval.
- Adding a freewheeling diode to the half-wave R-L circuit removes that negative-voltage interval and gives Equation (10.5).
- The fully controlled bridge uses both half-cycles. With an R load it gives Equation (10.6); with continuous current it gives Equation (10.7) and can produce negative average output when $\alpha > 90^\circ$.
- The semi-converter gives Equation (10.8), includes natural freewheeling, and remains a one-quadrant AC-to-DC converter.
- RMS expressions complement average values: Equations (10.9) to (10.11) show that firing angle changes heating and waveform effectiveness as well as average DC output.

## Further reading

- M. H. Rashid, *Power Electronics: Circuits, Devices and Applications*, 4th ed. - A strong textbook source for first-principles treatment of single-phase controlled rectifiers, waveforms, and average-value derivations.
- Ned Mohan, Tore M. Undeland, and William P. Robbins, *Power Electronics: Converters, Applications and Design*, 3rd ed. - Especially useful for continuous current, semi-converters, and the interpretation of $\alpha$ and $\beta$.
- [Littelfuse, *AN1003: Phase Control Using Thyristors*](https://www.littelfuse.com/~/media/electronics/application_notes/switching_thyristors/littelfuse_thyristor_phase_control_using_thyristors_application_note.pdf.pdf) - A practical note on delay angle, conduction angle, and the change in output voltage with phase control.
- [STMicroelectronics, *AN4607: Basics on the thyristor (SCR) structure and its application*](https://www.st.com/content/ccc/resource/technical/document/application_note/group0/8b/89/db/e6/0d/a1/49/fa/DM00140123/files/DM00140123.pdf/jcr%3Acontent/translations/en.DM00140123.pdf) - A concise refresher on SCR behavior and on applications in UPS, photovoltaic, and related power circuits.
- [Hitachi Energy, *HVDC converter stations*](https://www.hitachienergy.com/us/en/products-and-solutions/hvdc/hvdc-converter-stations) - A high-level link showing how controlled AC-DC conversion scales from textbook rectifiers to grid-scale converter stations.
