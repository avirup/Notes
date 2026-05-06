# Unit Overview Page Examples

## Before and After Comparison

### BEFORE (Old Format)

```
UNIT 1
═════════════════════════════════════════════════════════════

  Basic Electrical Quantities, Components, and Sources

═════════════════════════════════════════════════════════════



Overview
This unit builds the basic language of electrical engineering, 
introducing the core quantities, passive components, waveform 
families, source models, and practical measurement ideas used 
throughout the book.


Contents

- Unit 1: Basic Electrical Quantities, Components, and Sources


                                [Page break]
```

**Issues:**
- Contents only shows chapter title
- No prerequisites information
- Wasted vertical space
- Doesn't show structure of chapter

---

### AFTER (New Format)

```
UNIT 1
═════════════════════════════════════════════════════════════

  Basic Electrical Quantities, Components, and Sources

═════════════════════════════════════════════════════════════

Overview
This unit builds the basic language of electrical engineering, 
introducing the core quantities, passive components, waveform 
families, source models, and practical measurement ideas used 
throughout the book.

Prerequisites
Chapter 1:
  • Meaning of current, voltage, polarity, and resistance from Chapter 1.
  • Basic idea of electric field and current direction.
  • Familiarity with simple circuit symbols and the idea of source, 
    load, and current path.
  • Elementary algebra, especially rearranging formulas and working 
    with units.

Contents
Unit 1: Basic Electrical Quantities, Components, and Sources
  • 1.1 Basic Electrical Quantities
  • 1.2 Passive Components
  • 1.3 Signal Waveforms
  • 1.4 Sources


                                [Page break]
```

**Improvements:**
✅ Shows chapter structure with subsections
✅ Lists prerequisite knowledge upfront
✅ Efficient use of space
✅ Guides reader on what to expect

---

## Detailed Example: Unit 3 (AC Circuits)

### New Unit 3 Overview Page

```
╔═══════════════════════════════════════════════════════════════╗
║                        UNIT 3                                ║
║                 ─────────────────────────                    ║
║                  A.C. Circuits                                ║
║                 ─────────────────────────                    ║
║                                                              ║
║ Overview                                                      ║
║ This unit introduces alternating-current circuit analysis,  ║
║ including sinusoidal quantities, phase relationships,        ║
║ reactance, impedance, power in AC systems, and simple RLC   ║
║ behavior.                                                    ║
║                                                              ║
║ Prerequisites                                                ║
║ Chapter 3:                                                   ║
║   • Meaning of voltage, current, and resistance from Ch. 1. ║
║   • Basic passive components (R, L, C) from Chapter 1.      ║
║   • Self-inductance concept from Chapter 2.                 ║
║   • Basic phasor and complex number ideas from Ch. 3.       ║
║                                                              ║
║ Contents                                                     ║
║ Unit 3: A.C. Circuits                                        ║
║   • 3.1 Basic AC Terms                                       ║
║   • 3.2 Pure R, L, and C under Sinusoidal Excitation        ║
║   • 3.3 Simple AC Circuits                                   ║
║   • 3.4 AC Power                                             ║
║   • 3.5 Three-Phase Connection Basics                        ║
║   • 3.6 Practice Set                                         ║
║                                                              ║
╚═══════════════════════════════════════════════════════════════╝
```

---

## Space Breakdown (New Format)

For a typical unit overview page (assuming 7in × 10in paper):

| Section | Height | % of Page |
|---------|--------|-----------|
| Top margin | 0.5" | 5% |
| Title "Unit X" | 0.3" | 3% |
| Unit title and rules | 1.2" | 12% |
| Overview section | 1.5" | 15% |
| Prerequisites section | 2.0" | 20% |
| Contents section | 2.5" | 25% |
| Bottom margin | 1.0" | 10% |
| **Total** | **9.0"** | **90%** |

This fits comfortably on the 10" page height with minimal wasted space.

---

## Key Features of the New Implementation

### 1. **Automatic Prerequisites Detection**
- Scans each chapter for `## Prerequisites Check` heading
- Extracts everything after that heading until the next `## ` section
- Groups by chapter and displays with chapter name as header
- Only shows this section if prerequisites exist

### 2. **Subsection Listing**
- Extracts all `## X.X ...` headings from each chapter
- Displays as bullet points under the chapter name
- Uses the exact text from markdown headings
- Provides reader with clear content structure

### 3. **Space Optimization**
- Top margin: 0.5" (down from 0.9")
- Line spacing: 0.8-0.85 (tighter than document default of 1.22)
- Font size: `\small` for prerequisites and contents
- All content designed to fit on single page

### 4. **Smart Conditional Rendering**
- Prerequisites section only appears if needed
- Handles units with varying content lengths
- Falls gracefully onto second page if content exceeds page height

---

## What Gets Extracted

### Prerequisites Example (from Chapter 5)

**Markdown source:**
```markdown
## Prerequisites Check

- Meaning of current, voltage, polarity, and resistance from Chapter 1.
- Basic idea of electric field and current direction.
- Familiarity with simple circuit symbols and the idea of source, 
  load, and current path.
- Elementary algebra, especially rearranging formulas and working 
  with units such as mA, µA, and V.

If current direction, voltage polarity, or unit conversion feels weak, 
review Chapter 1 before studying diode and transistor bias conditions.
```

**Extracted and displayed as:**
```
Prerequisites
Chapter 5: Overview of Basic Semiconductor Devices
  • Meaning of current, voltage, polarity, and resistance from Chapter 1.
  • Basic idea of electric field and current direction.
  • Familiarity with simple circuit symbols and the idea of source, 
    load, and current path.
  • Elementary algebra, especially rearranging formulas and working 
    with units such as mA, µA, and V.
  • If current direction, voltage polarity, or unit conversion feels weak, 
    review Chapter 1 before studying diode and transistor bias conditions.
```

### Contents Example (from Chapter 1)

**Markdown source:**
```markdown
# Unit 1: Basic Electrical Quantities, Components, and Sources

## 1.1 Basic Electrical Quantities
### EMF and potential difference
### Electric current
### Power and energy

## 1.2 Passive Components
### Resistor
### Capacitor
### Inductor

## 1.3 Signal Waveforms
...

## 1.4 Sources
...
```

**Extracted and displayed as:**
```
Contents
Unit 1: Basic Electrical Quantities, Components, and Sources
  • 1.1 Basic Electrical Quantities
  • 1.2 Passive Components
  • 1.3 Signal Waveforms
  • 1.4 Sources
```

Note: Only level 2 headings (`## X.X`) are listed as subsections. 
Level 3 headings (`### ...`) are not included to maintain readability.

---

## PDF Build Process

When you run:
```bash
bash Scripts/build_feee_book.sh
```

The script performs these steps for each unit:

1. **Detects new unit** — Reads unit number from chapter filename
2. **Creates unit intro** — Generates unit overview page with:
   - Unit number and title (from UNIT_TITLES array)
   - Description (from UNIT_DESCRIPTIONS array)
   - Prerequisites section (extracted from chapters)
   - Contents section (extracted from chapter headings)
3. **Inserts before chapters** — Places overview page before first chapter of unit
4. **Processes chapters** — Converts markdown to PDF
5. **Combines** — Merges front matter, unit overviews, and chapters into final PDF

---

## Customization Options

To adjust spacing, edit `build_feee_book.sh`:

### Reduce top margin further:
```bash
printf '\\vspace*{0.05\\textheight}\n'  # Change 0.05 to 0.03 for even less
```

### Adjust line spacing in Contents:
```bash
printf '\\begin{spacing}{0.8}\n'  # Change 0.8 to 0.75 for tighter
```

### Change font size:
```bash
printf '\\noindent\\small\n'  # Change 'small' to 'footnotesize' for smaller
```

### Add more/less space between sections:
```bash
printf '\\vspace{0.2cm}\n'  # Adjust 0.2cm as needed
```

---

## Known Limitations

1. **Very long prerequisites** — If a chapter has extensive prerequisites (>15 bullet points), the page may overflow. Solution: Keep prerequisites concise in markdown or use abbreviations.

2. **Many subsections** — Chapters with 10+ subsections will push contents lower. Solution: This is intentional to maintain readability; content slightly exceeding one page is acceptable.

3. **Special characters** — LaTeX special characters in prerequisites/contents are not escaped. Solution: Keep chapter headings and prerequisites in simple ASCII where possible.

---

## Testing the Build

After making changes to the script, test with:

```bash
# Full build
bash Scripts/build_feee_book.sh

# Check output
ls -lh pdf/Fundamentals_of_Electrical_and_Electronics_Engineering.pdf

# View page 5 onwards (where Unit 1 overview starts)
# with your PDF reader
```

Look for:
- ✅ Unit overviews before each chapter
- ✅ Prerequisites listed (if chapter has them)
- ✅ All subsections visible in Contents
- ✅ Single-page unit overview (no overflow to next page)
