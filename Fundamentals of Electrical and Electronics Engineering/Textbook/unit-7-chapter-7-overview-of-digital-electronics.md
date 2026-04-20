# Unit 7: Overview of Digital Electronics

## Chapter Opening

The earlier chapters dealt mainly with quantities that can vary continuously. Voltage may rise smoothly, current may fall gradually, and an op-amp may amplify a small analog signal into a larger analog signal. Digital electronics works differently. Instead of treating every intermediate value as meaningful, it groups signals into a small number of logical states, usually two: `0` and `1`.

This simple idea makes it possible to build reliable systems that can count, compare, decide, store, and control. A temperature controller, a washing-machine sequence circuit, a battery charger indicator, a traffic-light controller, and the logic section of a microcontroller-based system all depend on digital decisions. At the beginner level, the foundation of digital electronics is built from **logic gates**, **Boolean algebra**, and standard expression forms such as **SOP** and **POS**.

This chapter explains those foundations carefully. We begin with the physical idea of digital signals and logic levels. We then study the common gates and their truth tables, learn how Boolean algebra simplifies logic expressions, apply **De Morgan's theorem**, and build expressions in **sum-of-products** and **product-of-sums** form. The chapter stays at diploma-entry depth, but it is written in enough detail that later topics such as combinational circuits, sequential circuits, counters, and programmable logic will feel much more natural.

## Prerequisites Check

- Basic idea of voltage, current, and circuit connections from Chapter 1.
- Familiarity with semiconductor devices and integrated circuits from Chapters 5 and 6.
- Confidence with simple algebraic symbols such as `+`, `×`, brackets, and variable names.
- Awareness that a practical circuit must be powered and that device ratings matter.

If active-low versus active-high notation, IC supply pins, or the idea of an integrated circuit package feel unfamiliar, review the end of Chapter 5 and the beginning of Chapter 6 before continuing.

## Core Content

### 7.1 Logic Gates

#### From physical voltage to digital state

Suppose a switch-controlled lamp circuit is designed so that the lamp is treated as **OFF** when the control voltage is near `0 V` and **ON** when the control voltage is near `5 V`. In a real circuit, the voltage may not be exactly `0 V` or exactly `5 V` at every instant. There can be noise, wiring drop, or switching delay. Even so, digital design works well because the circuit does not need infinitely precise values. It only needs the voltage to fall within a range recognized as logic LOW or logic HIGH.

This is the key abstraction of digital electronics. A varying electrical signal is interpreted as one of a few logical states.

A **digital signal** is a signal that represents information using discrete levels. In basic digital electronics, we usually use two levels:

- logic `0`, also called **LOW**
- logic `1`, also called **HIGH**

The actual voltage corresponding to LOW and HIGH depends on the logic family and supply voltage. For example, the TI SN74HC00 NAND gate operates from `2 V` to `6 V`, and its recommended input thresholds depend on the supply voltage. At `V_{CC} = 4.5 V`, the datasheet gives `V_{IL(max)} = 1.35 V` and `V_{IH(min)} = 3.15 V` [Texas Instruments, *SN74HC00 Quadruple 2-Input NAND Gates Datasheet*](https://www.ti.com/lit/gpn/sn74hc00). That means an input not above `1.35 V` is safely LOW, and an input not below `3.15 V` is safely HIGH.

So digital electronics is not the claim that only two voltages exist. It is the design method of assigning ranges of voltage to two logical meanings.

#### Positive logic

In **positive logic**, the higher voltage level represents logic `1` and the lower voltage level represents logic `0`. Most beginner-level digital analysis in this chapter uses positive logic. TI logic-gate datasheets commonly state the Boolean function "in positive logic" when describing a device [Texas Instruments, *SN74HC00 product page*](https://www.ti.com/product/SN74HC00).

For example, if a gate output is near the positive supply, we interpret that as logic `1`. If the output is near ground, we interpret that as logic `0`.

#### Why digital circuits are robust

The advantage of this method is practical robustness. If a signal that should be HIGH is `4.7 V` one moment and `4.9 V` the next, the logic meaning remains the same. Small unwanted variations are ignored as long as the signal stays within the valid region.

This is one reason digital systems became so important in control and computation. The circuit makes decisions based on state, not on tiny analog differences.

#### Truth tables

A **truth table** lists all possible input combinations of a logic function and shows the corresponding output. It is one of the most useful tools in digital electronics because it gives the complete behavior of a gate or logic expression in an organized way.

For a single-input gate, there are `2` possible input states: `0` and `1`.

For a two-input gate, there are `2^2 = 4` input combinations:

- `00`
- `01`
- `10`
- `11`

For a three-input gate, there are `2^3 = 8` combinations.

If a logic function has `n` binary inputs, the truth table contains `2^n` rows.

#### A switching picture of logic

Before naming the common gates, it helps to connect them to ordinary switching ideas.

- An **AND** action is like two series switches. The load receives power only if both switches are closed.
- An **OR** action is like two parallel switches. The load receives power if either switch is closed.
- A **NOT** action is an inversion. If the input command is `1`, the output becomes `0`; if the input command is `0`, the output becomes `1`.

This does not mean that a digital IC literally contains mechanical switches. It means the logical behavior can first be understood with a familiar physical analogy.

**Image prompt for Figure 7.1:** Create a clean textbook-style illustration with three panels. Panel 1 shows an AND action using two series switches controlling a lamp. Panel 2 shows an OR action using two parallel switches controlling a lamp. Panel 3 shows a NOT action using a control block labeled inverter that produces the opposite output state. Label input switches `A` and `B`, lamp state, and logic outputs clearly.

#### AND gate

An **AND gate** gives a HIGH output only when all its inputs are HIGH.

For a two-input AND gate:

$$
Y = A \cdot B \tag{7.1}
$$

Here `A` and `B` are the input variables and `Y` is the output. The dot means logical multiplication, also called the AND operation.

#### Table 7.1 Truth table of a two-input AND gate

| A | B | Y = A·B |
|---|---|---|
| 0 | 0 | 0 |
| 0 | 1 | 0 |
| 1 | 0 | 0 |
| 1 | 1 | 1 |

An everyday interpretation is a motor starter interlock. Suppose a small control system should energize a relay only when the `START` signal is HIGH and the `SAFETY_OK` signal is HIGH. That is an AND condition.

#### OR gate

An **OR gate** gives a HIGH output when at least one input is HIGH.

For a two-input OR gate:

$$
Y = A + B \tag{7.2}
$$

The plus sign here does not mean ordinary arithmetic addition. It means logical OR.

#### Table 7.2 Truth table of a two-input OR gate

| A | B | Y = A+B |
|---|---|---|
| 0 | 0 | 0 |
| 0 | 1 | 1 |
| 1 | 0 | 1 |
| 1 | 1 | 1 |

If either of two sensors is allowed to trigger an alarm, the output logic can be OR.

#### NOT gate

A **NOT gate** has one input and one output. It produces the complement of the input.

$$
Y = \bar{A} \tag{7.3}
$$

The bar over a variable means **complement** or **logical inverse**.

#### Table 7.3 Truth table of a NOT gate

| A | Y = Ā |
|---|---|
| 0 | 1 |
| 1 | 0 |

If a signal named `DOOR_OPEN` is `1` when the door is open, then `\bar{A}` represents the logic meaning "door not open," which in a simple two-state system means "door closed."

#### NAND gate

A **NAND gate** is a NOT-AND combination. It gives the complement of the AND output.

$$
Y = \overline{A \cdot B} \tag{7.4}
$$

So a NAND gate is LOW only when both inputs are HIGH. In every other case, it is HIGH.

#### Table 7.4 Truth table of a two-input NAND gate

| A | B | Y = (A·B)̄ |
|---|---|---|
| 0 | 0 | 1 |
| 0 | 1 | 1 |
| 1 | 0 | 1 |
| 1 | 1 | 0 |

Because it combines logic action with inversion, NAND becomes extremely useful in practical digital systems.

#### NOR gate

A **NOR gate** is a NOT-OR combination. It gives the complement of the OR output.

$$
Y = \overline{A + B} \tag{7.5}
$$

So a NOR gate is HIGH only when all inputs are LOW.

#### Table 7.5 Truth table of a two-input NOR gate

| A | B | Y = (A+B)̄ |
|---|---|---|
| 0 | 0 | 1 |
| 0 | 1 | 0 |
| 1 | 0 | 0 |
| 1 | 1 | 0 |

#### EX-OR gate

The **exclusive-OR** gate, written **EX-OR** or **XOR**, gives a HIGH output when the inputs are different.

$$
Y = A \oplus B = \bar{A}B + A\bar{B} \tag{7.6}
$$

This equation says that the output is HIGH in either of two cases:

- `A = 0`, `B = 1`
- `A = 1`, `B = 0`

#### Table 7.6 Truth table of a two-input EX-OR gate

| A | B | Y = A ⊕ B |
|---|---|---|
| 0 | 0 | 0 |
| 0 | 1 | 1 |
| 1 | 0 | 1 |
| 1 | 1 | 0 |

An XOR gate is often described as an **inequality detector** for two inputs. If the two inputs differ, the output is `1`.

#### EX-NOR gate

The **exclusive-NOR** gate, written **EX-NOR** or **XNOR**, gives a HIGH output when the inputs are equal.

$$
Y = \overline{A \oplus B} = AB + \bar{A}\bar{B} \tag{7.7}
$$

#### Table 7.7 Truth table of a two-input EX-NOR gate

| A | B | Y = (A ⊕ B)̄ |
|---|---|---|
| 0 | 0 | 1 |
| 0 | 1 | 0 |
| 1 | 0 | 0 |
| 1 | 1 | 1 |

So XNOR is an **equality detector**. When two digital signals should match, XNOR is a natural comparison function.

#### A combined comparison table

#### Table 7.8 Summary of common two-input gates

| Gate | Boolean expression | Output is HIGH when... | Simple meaning |
|---|---|---|---|
| AND | `A·B` | both inputs are HIGH | all conditions satisfied |
| OR | `A+B` | at least one input is HIGH | any condition satisfied |
| NAND | `(A·B)̄` | all cases except both HIGH | NOT-AND |
| NOR | `(A+B)̄` | both inputs are LOW | NOT-OR |
| XOR | `A ⊕ B` | inputs are different | inequality detector |
| XNOR | `(A ⊕ B)̄` | inputs are same | equality detector |

#### Worked Example 7.1

A safety interlock produces output `Y = A·B`, where:

- `A = 1` means the protective door is closed,
- `B = 1` means the emergency stop is released.

Find the output for the following conditions.

1. `A = 1`, `B = 1`
2. `A = 1`, `B = 0`
3. `A = 0`, `B = 1`

Using the AND rule:

$$
Y = A \cdot B
$$

Case 1:

$$
Y = 1 \cdot 1 = 1
$$

Case 2:

$$
Y = 1 \cdot 0 = 0
$$

Case 3:

$$
Y = 0 \cdot 1 = 0
$$

So the machine is enabled only in Case 1, when both conditions are satisfied.

#### Worked Example 7.2

A comparison circuit uses `Y = A \oplus B`. Find the output for all four input combinations and explain the meaning.

From the XOR truth table:

- `0 ⊕ 0 = 0`
- `0 ⊕ 1 = 1`
- `1 ⊕ 0 = 1`
- `1 ⊕ 1 = 0`

So the output is HIGH only when the inputs are unequal.

#### Universal logic gates

The **NAND** and **NOR** gates are called **universal gates** because any basic logic function can be built using only NAND gates or only NOR gates.

This is not just a mathematical curiosity. It has practical importance. If a designer has a stock of one gate type, many logic functions can still be realized.

##### Realizing NOT with NAND

If both inputs of a NAND gate are tied together and fed with the same variable `A`, then

$$
Y = \overline{A \cdot A} = \bar{A} \tag{7.8}
$$

So a NAND gate can work as an inverter.

##### Realizing AND with NAND

First generate `\overline{A \cdot B}` using one NAND gate, then invert it with a second NAND gate used as a NOT gate:

$$
Y = \overline{\overline{A \cdot B}} = A \cdot B \tag{7.9}
$$

##### Realizing OR with NAND

Using De Morgan's theorem,

$$
A + B = \overline{\bar{A} \cdot \bar{B}} \tag{7.10}
$$

This means:

1. invert `A` using a NAND-as-NOT,
2. invert `B` using another NAND-as-NOT,
3. NAND the two inverted signals.

Then the final output becomes `A + B`.

##### Realizing NOT with NOR

If both inputs of a NOR gate are tied together,

$$
Y = \overline{A + A} = \bar{A} \tag{7.11}
$$

##### Realizing OR with NOR

First form `\overline{A+B}` using one NOR gate. Then invert it using a second NOR-as-NOT stage:

$$
Y = \overline{\overline{A + B}} = A + B \tag{7.12}
$$

##### Realizing AND with NOR

Using De Morgan's theorem,

$$
A \cdot B = \overline{\bar{A} + \bar{B}} \tag{7.13}
$$

So by first inverting `A` and `B` with NOR gates and then NORing those inverted outputs, we obtain an AND function.

**Image prompt for Figure 7.2:** Create a clean textbook-style logic illustration showing universal-gate realization. In one column, show NOT, AND, and OR implemented using only NAND gates. In a second column, show NOT, OR, and AND implemented using only NOR gates. Label each intermediate node and final Boolean function clearly.

#### Practical note on real logic ICs

Textbook truth tables show the logical function. Real ICs also have supply-voltage limits, input thresholds, output current limits, propagation delay, and package details. For example, TI's SN74HC00 contains four independent 2-input NAND gates in one package, operates from `2 V` to `6 V`, and supports fanout up to 10 LSTTL loads [Texas Instruments, *SN74HC00 product page*](https://www.ti.com/product/SN74HC00).

This is a good habit to develop early: a gate is not only a symbol on paper. It is also a real component with ratings.

#### Floating inputs must be avoided

A beginner sometimes leaves an unused CMOS input open, assuming it will simply remain `0`. That is unsafe. TI notes that slow or floating CMOS inputs can cause extra current and unpredictable behavior [Texas Instruments, *Implications of Slow or Floating CMOS Inputs*](https://e2e.ti.com/cfs-file/__key/communityserver-discussions-components-files/151/4760.scba004c_5F00_slownfloatingCMOS.pdf). In practical circuits, unused logic inputs are tied to a defined HIGH or LOW level according to the application.

This point matters in laboratory work. If a breadboarded logic circuit behaves erratically, one of the first things to check is whether every input has a valid logic level.

### 7.2 Boolean Algebra

#### Why Boolean algebra is needed

Truth tables show complete behavior, but they become longer as the number of inputs increases. A circuit with four inputs already requires `2^4 = 16` rows. For larger systems, we need a symbolic way to express logic and simplify it. That symbolic language is **Boolean algebra**.

Boolean algebra deals with variables that take only two values:

- `0`
- `1`

Unlike ordinary algebra, Boolean algebra uses logical operations such as AND, OR, and NOT.

#### Boolean variables and literals

A **Boolean variable** is a variable that can have only the values `0` or `1`.

Examples:

- `A`
- `B`
- `X`
- `Y`

A variable itself, such as `A`, is called a **literal**. Its complement, such as `\bar{A}`, is also a literal.

#### Basic postulates and laws

At introductory level, the most useful Boolean laws are listed in one place below.

#### Table 7.9 Basic Boolean laws

| Law name | Boolean form | Meaning |
|---|---|---|
| Identity for OR | `A + 0 = A` | OR with 0 changes nothing |
| Identity for AND | `A·1 = A` | AND with 1 changes nothing |
| Null law for OR | `A + 1 = 1` | OR with 1 always gives 1 |
| Null law for AND | `A·0 = 0` | AND with 0 always gives 0 |
| Idempotent OR | `A + A = A` | repeating the same term does not change result |
| Idempotent AND | `A·A = A` | same |
| Complement OR | `A + \bar{A} = 1` | one of them must be true |
| Complement AND | `A \cdot \bar{A} = 0` | both cannot be true together |
| Involution | `\bar{\bar{A}} = A` | double inversion returns original value |
| Commutative OR | `A + B = B + A` | order does not matter |
| Commutative AND | `A·B = B·A` | order does not matter |
| Associative OR | `(A+B)+C = A+(B+C)` | grouping does not matter |
| Associative AND | `(A·B)·C = A·(B·C)` | grouping does not matter |
| Distributive | `A(B+C)=AB+AC` | AND distributes over OR |
| Distributive | `A+BC=(A+B)(A+C)` | OR distributes over AND |

These laws are the tools used in simplification.

#### Physical meaning of some basic laws

The law `A + 1 = 1` says that if one OR input is already HIGH, the output is certainly HIGH, whatever the other input may be.

The law `A \cdot 0 = 0` says that if one AND input is LOW, the output is certainly LOW, whatever the other input may be.

The law `A + \bar{A} = 1` says that either a statement or its complement must be true in a two-state system.

These are simple, but they save a lot of work in actual logic reduction.

#### Simple algebraic simplification

Consider the expression

$$
Y = A + A \cdot B
$$

We can simplify it using a standard absorption result:

$$
A + A \cdot B = A \tag{7.14}
$$

Why is this correct? If `A = 1`, then the output is certainly `1`. If `A = 0`, then `A·B = 0`, so the whole expression is still `0`. Therefore `B` does not affect the result.

Another important simplification is

$$
A(A + B) = A \tag{7.15}
$$

Again, once `A` is known, the extra term does not change the final result.

#### Worked Example 7.3

Simplify

$$
Y = A + A\bar{B}
$$

Using the absorption law:

$$
A + A\bar{B} = A
$$

So the simplified expression is

$$
Y = A
$$

#### Worked Example 7.4

Simplify

$$
Y = A \cdot 1 + B \cdot 0
$$

Using the identity and null laws:

$$
A \cdot 1 = A
$$

and

$$
B \cdot 0 = 0
$$

Therefore

$$
Y = A + 0 = A
$$

#### Worked Example 7.5

Simplify

$$
Y = A\bar{A} + B
$$

Since

$$
A\bar{A} = 0
$$

we get

$$
Y = 0 + B = B
$$

#### Truth-table verification of an algebraic result

In Boolean algebra, a simplification can always be checked by a truth table. This is a good habit for beginners because it prevents symbol mistakes.

For example, verify

$$
A + A\bar{B} = A
$$

#### Table 7.10 Verification of `A + A B̄ = A`

| A | B | B̄ | A·B̄ | A + A·B̄ | A |
|---|---|---|---|---|---|
| 0 | 0 | 1 | 0 | 0 | 0 |
| 0 | 1 | 0 | 0 | 0 | 0 |
| 1 | 0 | 1 | 1 | 1 | 1 |
| 1 | 1 | 0 | 0 | 1 | 1 |

The two final columns are identical. So the simplification is correct.

#### Practical note

Boolean simplification reduces the number of required gates, interconnections, and package count. In a real circuit this can reduce cost, power consumption, delay, and fault probability. Even in a small student breadboard circuit, a simpler expression is usually easier to wire and easier to debug.

### 7.3 Standard Theorems and Forms

#### De Morgan's theorem

One of the most useful theorems in digital electronics is **De Morgan's theorem**. It provides a systematic way to handle complements of expressions.

For two variables, the theorem has two forms:

$$
\overline{A \cdot B} = \bar{A} + \bar{B} \tag{7.16}
$$

and

$$
\overline{A + B} = \bar{A} \cdot \bar{B} \tag{7.17}
$$

The rule in words is simple:

- the complement of a product becomes the sum of the complements,
- the complement of a sum becomes the product of the complements.

De Morgan's theorem is essential when converting between NAND/NOR implementations and standard Boolean expressions.

#### Why De Morgan's theorem matters physically

Suppose an output should go LOW only when both conditions are true. That is a NAND function. Instead of thinking only in terms of "NOT after AND," De Morgan's theorem lets us rewrite the same function as "the first condition is false OR the second condition is false." Both descriptions are logically equivalent.

This theorem often allows a circuit to be built more economically from available gate types.

#### Worked Example 7.6

Apply De Morgan's theorem to simplify

$$
Y = \overline{A + B}
$$

Using Equation (7.17),

$$
Y = \bar{A}\bar{B}
$$

So a complemented OR expression is equal to the AND of the complemented variables.

#### Worked Example 7.7

Rewrite

$$
Y = \overline{AB}
$$

using De Morgan's theorem.

From Equation (7.16),

$$
Y = \bar{A} + \bar{B}
$$

#### Truth-table verification of De Morgan's theorem

#### Table 7.11 Verification of `\overline{A+B} = ĀB̄`

| A | B | A+B | (A+B)̄ | Ā | B̄ | Ā·B̄ |
|---|---|---|---|---|---|---|
| 0 | 0 | 0 | 1 | 1 | 1 | 1 |
| 0 | 1 | 1 | 0 | 1 | 0 | 0 |
| 1 | 0 | 1 | 0 | 0 | 1 | 0 |
| 1 | 1 | 1 | 0 | 0 | 0 | 0 |

The columns for `(A+B)̄` and `Ā·B̄` are identical, so the theorem is verified.

#### Minterms

A **minterm** is a standard product term in which every variable appears once, either in direct form or complemented form.

For two variables `A` and `B`, the four minterms are:

- `\bar{A}\bar{B}`
- `\bar{A}B`
- `A\bar{B}`
- `AB`

Each minterm is equal to `1` for exactly one row of the truth table.

#### Table 7.12 Two-variable minterms

| A | B | Minterm that is 1 |
|---|---|---|
| 0 | 0 | `ĀB̄` |
| 0 | 1 | `ĀB` |
| 1 | 0 | `AB̄` |
| 1 | 1 | `AB` |

This is why minterms are useful. They allow us to build a Boolean expression directly from the rows where the output is `1`.

#### SOP representation

**SOP** means **sum of products**. Each product term is usually a minterm or a simplified product term, and the final expression is formed by ORing those product terms.

To write the canonical SOP of a logic function:

1. write the rows of the truth table for which the output is `1`,
2. write the corresponding minterm for each such row,
3. OR the minterms together.

#### Worked Example 7.8

A function `Y` of variables `A` and `B` has output `1` for the rows:

- `A = 0`, `B = 1`
- `A = 1`, `B = 0`

Write the SOP expression.

For `01`, the minterm is

$$
\bar{A}B
$$

For `10`, the minterm is

$$
A\bar{B}
$$

So the SOP expression is

$$
Y = \bar{A}B + A\bar{B} \tag{7.18}
$$

This is exactly the XOR function.

#### Worked Example 7.9

The truth table of a function `Y(A,B,C)` gives output `1` for the rows:

- `001`
- `011`
- `110`

Write the canonical SOP.

For `001`, the minterm is

$$
\bar{A}\bar{B}C
$$

For `011`, the minterm is

$$
\bar{A}BC
$$

For `110`, the minterm is

$$
AB\bar{C}
$$

Therefore

$$
Y = \bar{A}\bar{B}C + \bar{A}BC + AB\bar{C} \tag{7.19}
$$

This is the canonical SOP form.

#### Maxterms

A **maxterm** is a standard sum term in which every variable appears once, either in direct or complemented form.

Each maxterm is equal to `0` for exactly one row of the truth table.

For two variables `A` and `B`, the four maxterms are:

- `A + B`
- `A + \bar{B}`
- `\bar{A} + B`
- `\bar{A} + \bar{B}`

The pattern is the opposite of minterms. In a maxterm, a variable appears uncomplemented when its row value is `0`, and complemented when its row value is `1`, so that the whole sum becomes `0` only for that row.

#### Table 7.13 Two-variable maxterms

| A | B | Maxterm that is 0 |
|---|---|---|
| 0 | 0 | `A + B` |
| 0 | 1 | `A + B̄` |
| 1 | 0 | `Ā + B` |
| 1 | 1 | `Ā + B̄` |

#### POS representation

**POS** means **product of sums**. The canonical POS is formed from the rows for which the output is `0`.

To write the canonical POS:

1. identify the rows where the output is `0`,
2. write the corresponding maxterm for each such row,
3. AND those sum terms together.

#### Worked Example 7.10

Suppose a two-variable function `Y` is `0` for the rows:

- `00`
- `11`

Write the canonical POS.

For `00`, the maxterm is

$$
A + B
$$

For `11`, the maxterm is

$$
\bar{A} + \bar{B}
$$

Therefore

$$
Y = (A + B)(\bar{A} + \bar{B}) \tag{7.20}
$$

#### Worked Example 7.11

A function `Y(A,B,C)` is `0` for the rows:

- `000`
- `010`
- `111`

Write the canonical POS.

For `000`, the maxterm is

$$
A + B + C
$$

For `010`, the maxterm is

$$
A + \bar{B} + C
$$

For `111`, the maxterm is

$$
\bar{A} + \bar{B} + \bar{C}
$$

So the canonical POS is

$$
Y = (A + B + C)(A + \bar{B} + C)(\bar{A} + \bar{B} + \bar{C}) \tag{7.21}
$$

#### Relation between SOP and POS

SOP is built from the rows where the output is `1`.

POS is built from the rows where the output is `0`.

Both describe the same logic function, but from opposite viewpoints. In practice:

- SOP often matches an OR of AND-gate outputs,
- POS often matches an AND of OR-gate outputs.

This makes the forms especially useful when connecting algebra to gate-level realization.

#### Simple conversion and verification example

Consider the function with truth table:

#### Table 7.14 Example truth table for conversion

| A | B | Y |
|---|---|---|
| 0 | 0 | 0 |
| 0 | 1 | 1 |
| 1 | 0 | 1 |
| 1 | 1 | 0 |

From the rows where `Y = 1`, the SOP is

$$
Y = \bar{A}B + A\bar{B}
$$

From the rows where `Y = 0`, the POS is

$$
Y = (A + B)(\bar{A} + \bar{B})
$$

These look different, but they describe the same function. A truth table or algebraic expansion can verify the equivalence.

#### Worked Example 7.12

Verify that

$$
\bar{A}B + A\bar{B}
$$

and

$$
(A + B)(\bar{A} + \bar{B})
$$

represent the same logic function.

Expand the POS form:

$$
(A + B)(\bar{A} + \bar{B}) = A\bar{A} + A\bar{B} + B\bar{A} + B\bar{B}
$$

Now use

$$
A\bar{A} = 0, \qquad B\bar{B} = 0
$$

So

$$
(A + B)(\bar{A} + \bar{B}) = A\bar{B} + \bar{A}B
$$

which is exactly the XOR SOP expression.

Therefore the two forms are equivalent.

#### Common beginner mistakes

- Treating Boolean `+` as ordinary arithmetic addition.
- Forgetting that `1 + 1 = 1` in Boolean algebra.
- Forgetting that `A + \bar{A} = 1` and `A\bar{A} = 0`.
- Writing minterms from the `0` rows instead of the `1` rows.
- Writing maxterms from the `1` rows instead of the `0` rows.
- Leaving CMOS inputs floating on breadboards.
- Mixing the ordinary meaning of "exclusive OR" with the ordinary OR gate.

#### Practical note

At this stage, the most important skill is not memorizing every pattern mechanically. It is learning to move comfortably among four representations of the same logic:

- verbal statement,
- truth table,
- Boolean expression,
- gate realization.

That skill is the bridge to all later digital-circuit study.

## Worked Interpretation Exercise

### Reading a Real Logic-IC Datasheet: TI SN74HC00

The TI `SN74HC00` is a useful real artifact for this chapter because it is a standard logic-gate IC containing four independent 2-input NAND gates [Texas Instruments, *SN74HC00 product page*](https://www.ti.com/product/SN74HC00) [Texas Instruments, *SN74HC00 Quadruple 2-Input NAND Gates Datasheet*](https://www.ti.com/lit/gpn/sn74hc00).

Here is how to read the most important information from the datasheet at beginner level.

#### 1. Part description

The datasheet states that the device contains **four independent 2-input NAND gates** and performs the Boolean function in positive logic. That means one IC package gives four identical NAND-gate sections.

So if a circuit needs up to four NAND gates, one `SN74HC00` may be enough.

#### 2. Supply-voltage range

The recommended operating supply range is `2 V` to `6 V` [Texas Instruments, *SN74HC00 Datasheet*]. This tells us immediately that the device is from the HC CMOS logic family, not a `230 V` mains device and not a raw transistor that can simply be connected without a supply plan.

In a beginner laboratory, a regulated `5 V` supply is a common operating choice.

#### 3. Package and pin count

The PDIP version has `14` pins. The datasheet shows the functional pinout. Important pins include:

- `1A`, `1B` as the inputs of gate 1
- `1Y` as the output of gate 1
- `2A`, `2B`, `2Y` for gate 2
- `3A`, `3B`, `3Y` for gate 3
- `4A`, `4B`, `4Y` for gate 4
- `GND` on pin `7`
- `VCC` on pin `14`

This tells us how to wire the IC on a breadboard. Without checking `VCC` and `GND`, the logic function on paper cannot become a working circuit.

#### 4. Input thresholds

At `V_{CC} = 4.5 V`, the datasheet gives:

- `V_{IL(max)} = 1.35 V`
- `V_{IH(min)} = 3.15 V`

So an input up to `1.35 V` is safely read as LOW, and an input from `3.15 V` upward is safely read as HIGH. Voltages in between are not reliable logic levels.

This is a very practical point. A student may think that `2.0 V` should "probably be HIGH enough" in a `5 V` logic system, but the datasheet shows why that assumption is unsafe.

#### 5. Fanout and family behavior

TI notes that the device supports fanout up to `10` LSTTL loads [Texas Instruments, *SN74HC00 product page*]. At beginner level, the important meaning is that one gate output can drive several compatible logic inputs, but output loading is still a real design consideration.

#### 6. Floating-input caution

The datasheet family documentation and TI's application note on slow or floating CMOS inputs warn that CMOS inputs should not be left floating [Texas Instruments, *Implications of Slow or Floating CMOS Inputs*]. In a lab circuit, an unused input should be tied to a valid logic HIGH or LOW.

This single detail explains many "mysterious" breadboard faults in beginner experiments.

## How This Matters in Practice

The ideas in this chapter appear almost everywhere that electrical systems make decisions.

In household and industrial equipment, digital logic decides whether a load should turn on, whether a door interlock is satisfied, whether a timer has completed its cycle, and whether a fault signal should trigger an alarm. Even when a system is controlled by a microcontroller, the underlying decision structure is still built from Boolean conditions.

In transformers and motors, the power stage is usually electrical or electromechanical, but digital logic often supervises start permissives, overload indication, sequencing, and protective shutdown. A pump controller may use an AND condition for `WATER_AVAILABLE` and `MOTOR_HEALTHY`, and an OR condition for manual or automatic start.

In battery charging and solar PV systems, logic is used for charge-state indication, source selection, undervoltage lockout, comparator outputs, and relay control. The signal coming from a sensor may first be analog, but after threshold detection it is frequently processed as a digital HIGH or LOW.

In instrumentation and control circuits, truth tables and Boolean expressions describe alarm conditions, window comparators, enable logic, fault latching, and basic automation actions. A plant signal may be represented by a bit such as `PRESSURE_OK`, then combined with other bits using AND, OR, and NOT operations.

In digital systems and automation, this chapter is the direct foundation for combinational logic design, encoders, decoders, multiplexers, flip-flops, counters, registers, programmable controllers, and embedded digital interfaces. Without comfort in truth tables, Boolean algebra, and standard forms, later digital topics feel disconnected. With that foundation, they become systematic.

## Chapter Summary

- **Digital electronics** represents information using discrete logic states, usually `0` and `1`.
- In **positive logic**, the higher voltage range represents logic `1` and the lower range represents logic `0`.
- A **truth table** lists all possible input combinations and the corresponding output of a logic function.
- The basic gates are **AND**, **OR**, and **NOT**.
- The common derived gates are **NAND**, **NOR**, **EX-OR**, and **EX-NOR**.
- For two inputs, the main gate equations are:
  AND: `$Y = A \cdot B$`
  OR: `$Y = A + B$`
  NOT: `$Y = \bar{A}$`
  NAND: `$Y = \overline{A \cdot B}$`
  NOR: `$Y = \overline{A + B}$`
  XOR: `$Y = \bar{A}B + A\bar{B}$`
  XNOR: `$Y = AB + \bar{A}\bar{B}$`
- **NAND** and **NOR** are **universal gates** because other logic functions can be built using only one of those gate types.
- **Boolean algebra** provides symbolic rules for expressing and simplifying logic functions.
- Important Boolean laws include:
  `$A + 0 = A$`, `$A \cdot 1 = A$`, `$A + 1 = 1$`, `$A \cdot 0 = 0$`, `$A + \bar{A} = 1$`, `$A \cdot \bar{A} = 0$`, and `$\bar{\bar{A}} = A$`.
- **De Morgan's theorem** states:
  `$\overline{A \cdot B} = \bar{A} + \bar{B}$` and `$\overline{A + B} = \bar{A}\bar{B}$`.
- A **minterm** is a standard product term that is `1` for exactly one truth-table row.
- **SOP** means **sum of products** and is formed from the rows where the output is `1`.
- A **maxterm** is a standard sum term that is `0` for exactly one truth-table row.
- **POS** means **product of sums** and is formed from the rows where the output is `0`.
- Real logic ICs must be read from datasheets for supply range, pinout, input thresholds, and other practical details.
- CMOS logic inputs should not be left floating.

## Further Reading

1. Texas Instruments, [*SN74HC00 Quadruple 2-Input NAND Gates Datasheet*](https://www.ti.com/lit/gpn/sn74hc00). Useful for learning how a textbook NAND gate appears in a real IC with supply range, pinout, and threshold ratings.
2. Texas Instruments, [*SN74HC86 Quadruple 2-Input XOR Gates Datasheet*](https://www.ti.com/lit/gpn/sn74hc86). Useful for seeing how XOR behavior is specified in an actual logic device and for connecting truth-table theory to a real package.
3. Texas Instruments, [*Implications of Slow or Floating CMOS Inputs*](https://e2e.ti.com/cfs-file/__key/communityserver-discussions-components-files/151/4760.scba004c_5F00_slownfloatingCMOS.pdf). Helpful practical reading on why logic inputs must be held at valid levels.
4. M. Morris Mano and Michael D. Ciletti, *Digital Design*. A standard text for Boolean algebra, truth tables, logic simplification, and later combinational and sequential design.
5. Thomas L. Floyd, *Digital Fundamentals*. A beginner-friendly reference for logic gates, Boolean laws, standard forms, and laboratory-oriented digital-electronics study.
