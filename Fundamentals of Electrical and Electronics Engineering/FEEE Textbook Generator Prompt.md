# Prompt — FEEE Textbook Generator

Write a **textbook-style self-study book on Fundamental of Electrical and Electronics Engineering (FEEE)** for a beginner reader. I will provide:

1. A full **chapter-and-topic plan or syllabus**
2. The **chapter number to write now**

Your job is to expand the plan into a full textbook, **one chapter at a time**, building carefully from first principles.

## Reader and teaching level

Assume the reader is a **first-year diploma student** with only a **basic** understanding of:

- school-level electricity and magnetism
- elementary algebra and arithmetic used in engineering
- common electrical appliances and simple electronic devices

Assume weak confidence with:

- current, voltage, power, and energy
- magnetic circuits and electromagnetic induction
- AC quantities such as RMS value, phase difference, and power factor
- transformers and motors
- semiconductor devices, op-amps, and digital logic
- laboratory instruments such as multimeter, CRO/DSO, and LCR meter

The reader is studying independently, so the writing must be patient, clear, steady, and beginner-friendly without becoming shallow.

The goal is to help the reader become comfortable enough with FEEE fundamentals to later study electrical machines, circuit theory, power electronics, control, measurements, and applied electronics with confidence.

## Scope and depth

- The book must read like a **real textbook**, not lecture notes, a guide sheet, or a summary.
- Write at **full textbook depth**, but keep the level appropriate for diploma beginners.
- A typical chapter should be about **4,000-8,000 words**, depending on the topic.
- Prioritize **physical meaning first, mathematics second**.
- Start new ideas with a concrete physical situation, measurement setup, or numerical example before generalizing.
- Explain equations in words before and after using them.
- Show arithmetic clearly in worked examples.
- Use realistic examples where relevant, including:
  - `230 V`, `50 Hz` single-phase supply
  - household and workshop loads
  - battery chargers
  - ceiling fans, pumps, and small motors
  - simple transformers
  - diode rectifier situations
  - op-amp signal-conditioning examples
  - basic digital logic applications
- Use Indian / South-Asian context naturally where appropriate.
- Keep broad topics at diploma-entry depth. For machines, transformers, transistor applications, op-amps, and digital electronics, emphasize:
  - basic principle
  - main parts
  - simple operation
  - common applications
- Do not drift into advanced design unless the syllabus explicitly requires it.

## Chapter output contract

- The **unit of generation is one full chapter per response**.
- Return **only** the requested chapter in markdown, ready to save as a chapter file.
- Do not add preambles, meta-commentary, or closing chat.
- If a chapter is too long to finish in one response, continue it only when I explicitly ask you to continue that same chapter.

## Required structure for every chapter

Use this structure in order:

## Chapter opening

A short narrative introduction explaining why the chapter matters, what the reader will learn, and how it connects to earlier and later chapters.

## Prerequisites check

A short box listing what the reader should already know. If a prerequisite may be weak, point back to the earlier chapter or section that supports it.

## Core content

Follow the supplied chapter plan section by section.

For each major section:

- begin with physical intuition before formal explanation
- define key terms clearly on first use
- briefly refresh a previously defined term only when the gap is long or confusion is likely
- explain what each symbol means when mathematics appears
- derive or motivate foundational equations step by step
- walk through arithmetic clearly in numerical examples
- explain instruments, waveforms, characteristics, and ratings in plain language
- flag common misconceptions explicitly
- end the section with a short practical note where appropriate

## Worked interpretation exercise

Include at least one worked reading of a real artifact relevant to the chapter, such as:

- a device datasheet
- a nameplate
- a laboratory instrument panel
- a waveform plot
- a specification table
- a truth table
- a component marking or resistor color code example

If no real artifact is available from reliable sources, omit this section rather than inventing one.

## How this matters in practice

End the chapter with a short section showing where the chapter's ideas appear in:

- household and industrial electrical systems
- transformers and motors
- battery charging
- solar PV and inverter-based systems
- instrumentation and control circuits
- digital systems and automation

Use only the applications that naturally fit the chapter.

## Chapter summary

A bulleted recap of key ideas, equations, and vocabulary.

## Further reading

Three to five real, relevant sources with a one-sentence note on why each is useful.

## Writing rules

- Use a clear, direct, textbook voice with **we** and **you** only where natural.
- Keep the tone professional, calm, and readable.
- Do not sound like a chatbot, marketing copywriter, or motivational speaker.
- Do not use flowery language, dramatic hooks, exaggerated praise, or clickbait-style transitions.
- Do not use filler phrases such as:
  - "Let us dive into"
  - "In today's world"
  - "It is important to note that" unless truly needed
  - "Obviously"
  - "As we all know"
  - "Game changer"
  - "Revolutionary"
- Prefer plain explanation over performance.
- Prefer prose over bullets except for prerequisites, summaries, clearly list-shaped items, and short comparisons.
- Use short, clear sentences and explicit signposting when ideas are easy to confuse.
- Reintroduce important ideas briefly when they return after a meaningful gap.
- Do not assume comfort with phasors, RMS values, magnetic quantities, semiconductor terminology, or Boolean algebra unless they have already been taught.
- Keep the book centered on **fundamental electrical and electronics engineering**.
- Do not drift into deep modern electronics, communication systems, VLSI, control theory, or advanced power-electronics design unless the syllabus clearly requires it.

## Style guardrails to avoid AI-sounding prose

- Vary sentence length naturally, but keep most sentences straightforward.
- Do not repeat the same transition pattern from section to section.
- Do not use artificial enthusiasm.
- Do not overuse rhetorical questions.
- Do not restate the same point in slightly different words.
- Do not end every section with a polished slogan-like sentence.
- When explaining, prefer concrete nouns and verbs over vague abstract phrasing.
- If a statement is simple, write it simply.

## Sources and citations

This textbook must be source-grounded.

- Cite authoritative sources for standards, device characteristics, named laws, equations, instrument guidance, ratings guidance, application facts, and non-obvious numerical claims.
- Prefer textbooks, standards, manufacturer datasheets, university course notes, and official technical publications.
- Use inline citations in markdown, for example:
  - `[V.K. Mehta, Principles of Electrical Engineering]`
  - `[S.K. Bhattacharya, Basic Electricals and Electronics]`
  - `[Horowitz and Hill, The Art of Electronics, 3e]`
  - `[Texas Instruments 741 Op Amp Datasheet]`
  - `[ON Semiconductor PN Junction Diode Basics]`
  - `[IEEE Std 1459-2010]`
- If a claim cannot be verified from reliable sources, mark it as needing verification rather than presenting it as fact.
- The **Further reading** section must contain real sources actually relevant to that chapter.

## Figures and diagrams

**ASCII art is not allowed anywhere.** Do not draw circuits, waveforms, block diagrams, characteristic curves, phasor sketches, truth-table layouts, or any other text-based visual approximation.

For every required figure, use exactly one of these:

### Option A — External web image

Use this when a stable, relevant, citable image is available.

```md
![Figure X.Y: Short caption](https://example.com/image.png)
*Source: Publisher / manufacturer / Wikimedia Commons / official educational source. Include license or usage note when known.*
```

### Option B — Image generation prompt

Use this when a suitable stable web image is not available.

```md
**Image prompt for Figure X.Y:** Create a clean textbook-style technical illustration of ...
```

When using Option B, specify every required component, label, axis, unit, polarity, waveform shape, terminal name, logic state, and annotation clearly enough that an illustrator or image model could produce the figure without further clarification.

## Book-level consistency rules

The book must behave like one coherent textbook, not a set of disconnected drafts.

- Use consistent notation throughout unless a change is explicitly explained.
- Keep core definitions and terminology consistent across chapters.
- Use explicit chapter or section cross-references where useful.
- Number equations chapter-wise and sequentially, for example `(3.1)`, `(3.2)`, `(3.3)`.
- Number figures chapter-wise and sequentially, for example `Figure 4.1`, `Figure 4.2`.
- Number tables chapter-wise and sequentially, for example `Table 5.1`.
- Do not switch carelessly among near-synonyms such as "EMF", "voltage source", and "source voltage" without clarifying the relationship when needed.
- Preserve the same beginner-friendly depth across chapters.
- Before finishing a chapter, check notation, terminology, numbering, and citations for consistency.

## Formatting rules

### Markdown

- Use `#` for the chapter title only.
- Use `##` for major subsections, `###` for minor subsections, and `####` sparingly.
- Bold a key term on first introduction in the current chapter.
- Use markdown tables for comparisons, specifications, and tabular data.
- Do not use fenced code blocks for normal prose or equations.

### Mathematics

- Use inline LaTeX like `$V = IR$`.
- Use display LaTeX for important equations.
- Use clear subscripts such as `V_{rms}`, `I_{avg}`, `N_1`, `N_2`, `P_{in}`, and `P_{out}`.
- Explain symbols in words around the equation.
- Refer to important equations by number in the prose.
- Example final result:

$$\boxed{P = VI \cos\phi} \quad \text{(3.1)}$$

### Units

- Use SI units throughout.
- Always include units in numerical values.
- Use correct multipliers such as µ, m, k, and M.

## Do not do these things

- Do not produce ASCII or text-based diagrams of any kind.
- Do not summarize to save space.
- Do not invent citations, sources, standards, artifacts, or figures.
- Do not assume the reader remembers earlier material without a short reminder when needed.
- Do not include a preface, table of contents, or closing remark.
- Do not skip the section **How this matters in practice**.
- Do not use emoji.
- Do not pad the chapter with generic study advice or motivational filler.

## File naming rule

When I ask for a chapter, write it so it can be saved using a descriptive file name in this pattern:

`unit-1-chapter-1-basic-electrical-quantities-components-and-sources.md`

Use lowercase letters and hyphens. The filename should reflect the actual unit and chapter topic supplied for that request.

## Task

Write the requested FEEE chapter using the syllabus and chapter number I provide next.
