# Prompt — Power Electronics Textbook Generator

Write a **textbook-style self-study book on power electronics fundamentals** for a beginner reader. I will provide:

1. A full **chapter-and-topic plan or syllabus**
2. The **chapter number to write now**

Your job is to expand the plan into a full textbook, **one chapter at a time**, building carefully from first principles.

## Reader and teaching level

Assume the reader has only a **very basic** understanding of:

- electrical engineering fundamentals
- mathematics used in engineering
- renewable-energy systems

Assume weak confidence with semiconductor devices, waveforms, switching, converters, harmonics, and control. The reader is studying independently, so the writing must be patient, explicit, encouraging, and beginner-friendly without becoming shallow.

The goal is to help the reader become comfortable enough with power-electronics fundamentals to later study converter design, control, simulation, and renewable-energy applications with confidence.

## Scope and depth

- The book must read like a **real textbook**, not lecture notes, a cheat sheet, or a summary.
- Write at **full textbook depth** and explain methods fully when they are introduced.
- A typical chapter should be about **4,000-6,000 words**, depending on the topic.
- Prioritize **intuition first, mathematics second**.
- Start new ideas with a concrete physical or numerical example before generalizing.
- Explain equations rather than dropping them without context.
- Use realistic examples where relevant, including 230 V / 50 Hz single-phase supply, 415 V three-phase supply, battery chargers, rooftop PV inverters, EV auxiliary converters, UPS systems, and small motor-drive contexts.
- Tie major ideas to **renewable-energy applications** wherever natural: solar PV, wind, battery storage, EV power stages, and grid-connected converters.
- Use Indian / South-Asian context naturally where appropriate.

## Chapter output contract

- The **unit of generation is one full chapter per response**.
- Return **only** the requested chapter in markdown, ready to save as `chapter-N.md`.
- Do not add preambles, meta-commentary, or closing chat.
- If a chapter is too long to finish in one response, continue it only when I explicitly ask you to continue that same chapter.

## Required structure for every chapter

Use this structure in order:

## Chapter opening
A narrative introduction explaining why the chapter matters, what the reader will learn, and how it connects to earlier and later chapters.

## Prerequisites check
A short box listing what the reader should already know. If a prerequisite may be weak, point back to the earlier chapter or section that supports it.

## Core content
Follow the supplied chapter plan section by section.

For each major section:

- begin with physical intuition before formalism
- define key terms clearly on first use
- briefly refresh a previously defined term only when the gap is long or confusion is likely
- explain what each symbol means when mathematics appears
- derive or motivate foundational equations step by step
- walk through arithmetic clearly in numerical examples
- explain waveforms, graphs, and device ratings in plain language
- flag common misconceptions explicitly
- close the section with a short renewable-energy relevance note when appropriate

## Worked interpretation exercise
Include at least one worked reading of a real artifact relevant to the chapter, such as a datasheet, waveform plot, converter specification, device rating table, or published figure. If no real artifact is available from the supplied materials or reliable sources, omit this rather than inventing one.

## How this matters in renewable-energy systems
End the chapter with a short section explaining how the chapter's ideas appear in solar PV, battery charging, wind-energy interfaces, EV power stages, or grid-connected converters.

## Chapter summary
A bulleted recap of key ideas, equations, and vocabulary.

## Further reading
Three to five real, relevant sources with a one-sentence note on why each is useful.

## Writing rules

- Use a warm, explanatory voice with **we** and **you**.
- Never be patronizing. Do not say "obviously" or "this is easy."
- Prefer prose over bullets except for prerequisites, summaries, and clearly list-shaped content.
- Use short, clear sentences and explicit signposting when ideas are easy to confuse.
- Reintroduce important ideas briefly when they return after a meaningful gap.
- Do not assume comfort with phasors, RMS, differential equations, or semiconductor terminology unless they have already been taught.
- Keep the book centered on **power electronics**. Do not drift into unrelated deep electronics, communications, or advanced semiconductor physics unless the syllabus clearly requires it.

## Sources and citations

This textbook must be source-grounded.

- Cite authoritative sources for device history, standards, ratings guidance, named methods, equations, application facts, and non-obvious numerical claims.
- Prefer textbooks, standards, manufacturer datasheets, university course notes, and official technical publications.
- Use inline citations in markdown, for example: `[Rashid, Power Electronics, 4e, Ch. 3]`, `[Infineon IGBT Basics App Note]`, `[IEEE 519-2022]`.
- If a claim cannot be verified from the supplied materials or reliable sources, mark it as needing verification rather than presenting it as fact.
- The **Further reading** section must contain real sources actually relevant to that chapter.

## Figures and diagrams

**ASCII art is not allowed anywhere.** Do not draw circuits, waveforms, block diagrams, characteristic curves, rough sketches, Unicode box-drawing diagrams, or any other text-based visual approximation.

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

When using Option B, specify every required component, label, axis, unit, polarity, waveform shape, conduction interval, firing angle, and annotation clearly enough that an illustrator or image model could produce the figure without further clarification.

## Book-level consistency rules

The book must behave like one coherent textbook, not a stack of disconnected drafts.

- Use consistent notation throughout unless a change is explicitly explained.
- Keep core definitions and terminology consistent across chapters.
- Use explicit chapter or section cross-references where useful.
- Number equations chapter-wise and sequentially, for example `(3.1)`, `(3.2)`, `(3.3)`.
- Number figures chapter-wise and sequentially, for example `Figure 4.1`, `Figure 4.2`.
- Number tables chapter-wise and sequentially, for example `Table 5.1`.
- Do not switch carelessly among near-synonyms such as "controlled rectifier", "phase-controlled rectifier", and "SCR rectifier" without clarifying the relationship.
- Preserve the same beginner-friendly depth across chapters.
- Before finishing a chapter, check notation, terminology, numbering, citations, and cross-references for consistency.

## Formatting rules

### Markdown

- Use `#` for the chapter title only.
- Use `##` for major subsections, `###` for minor subsections, and `####` sparingly.
- Bold a key term on first introduction in the current chapter.
- Use markdown tables for comparisons, specifications, and tabular data.
- Do not use fenced code blocks for normal prose or equations.

### Mathematics

- Use inline LaTeX like `$V_m \sin(\omega t)$`.
- Use display LaTeX for important equations.
- Use clear subscripts such as `V_{DC}` and `I_{gate}`.
- Explain symbols in words around the equation.
- Refer to important equations by number in the prose.
- Example final result:

$$\boxed{V_{o,avg} = \frac{V_m}{\pi}(1 + \cos\alpha)} \quad \text{(3.1)}$$

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
- Do not skip the section **How this matters in renewable-energy systems**.
- Do not use emoji.

## What to Provide Back to Me

A single markdown response containing only the requested section, ready to be saved as `module-M-section-S.md`. No preamble, no meta-commentary, no trailing "let me know if you need more" lines.