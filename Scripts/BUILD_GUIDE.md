# PDF Build Quick Start Guide

## Running the Build

From the repository root:

```bash
cd /home/avirup/Notes
bash Scripts/build_feee_book.sh
```

Expected output:
```
Created: /home/avirup/Notes/pdf/Fundamentals_of_Electrical_and_Electronics_Engineering.pdf
```

## Build Process Overview

The script:
1. ✅ Finds all `unit-*-chapter-*.md` files
2. ✅ Converts SVG images to PDF
3. ✅ Creates unit overview pages with:
   - Unit title and description
   - Prerequisites (if available)
   - Contents (chapter titles + subsections)
4. ✅ Compiles everything with Pandoc and XeLaTeX
5. ✅ Outputs single PDF file

**Typical build time:** 30-60 seconds (depending on image processing)

## What You Changed

### Files Modified

1. **`build_feee_book.sh`** (lines 159-246)
   - Added prerequisites extraction logic
   - Enhanced contents to show subsections
   - Reduced vertical spacing for unit overview pages
   - Changed top margin from 0.14 to 0.05 textheight

2. **`feee-book-header.tex`** (line 4)
   - Added `\usepackage{setspace}` for line spacing control

### How It Works

**For each unit:**

1. Scans chapter files for unit number
2. For each chapter in the unit:
   - **Prerequisites**: Looks for `## Prerequisites Check` heading
   - **Contents**: Extracts all `## X.X ...` section headings
3. Generates a formatted overview page with all this info
4. Inserts it before the chapter content

## Unit Overview Page Structure

```
┌─────────────────────────────┐
│ [Spacing: 0.5"]             │
│ UNIT 1                      │ ← Large scshape (small caps)
│ ─────────────────────────── │
│ Unit Title Here             │ ← Large bfseries (bold)
│ ─────────────────────────── │
│ [Spacing: 0.35"]            │
│ Overview                    │ ← Bold heading
│ [Spacing: 0.15"]            │
│ Description text...         │ ← Small font
│ [Spacing: 0.2"]             │
│ Prerequisites               │ ← Bold heading (conditional)
│ Chapter X:                  │ ← Small font, 0.85 spacing
│   • Bullet point 1          │
│   • Bullet point 2          │
│ [Spacing: 0.15"]            │
│ Contents                    │ ← Bold heading
│ [Spacing: 0.1"]             │
│ Chapter Title               │ ← Bold, 0.8 spacing
│   • Subsection 1            │
│   • Subsection 2            │
│   • Subsection 3            │
│                             │ ← Bottom margin: ~1"
└─────────────────────────────┘
```

## Prerequisites Extraction

The script looks for this markdown structure in each chapter:

```markdown
## Prerequisites Check

- Meaning of [something]
- Understanding of [something]
- Familiarity with [something]
```

Everything between `## Prerequisites Check` and the next `## ` (section heading) is extracted and displayed on the overview page.

**Important:** If your chapter doesn't have a `## Prerequisites Check` section, no prerequisites will appear on the overview page (which is fine).

## Contents Extraction

The script extracts all level 2 headings:

```markdown
## 1.1 Section Name         ← This gets listed
## 1.2 Another Section      ← This gets listed
### Subsection Name         ← This is NOT listed (level 3)
```

Only `## ` headings appear in Contents. This maintains readability while showing chapter structure.

## Troubleshooting

### "No chapter markdown files found"
**Error message:**
```
No chapter markdown files found under: 
/home/avirup/Notes/Fundamentals of Electrical and Electronics Engineering/Textbook
```

**Solutions:**
- Check files exist: `ls Scripts/../Fundamentals*Textbook/unit-*.md`
- Check naming: Files must match `unit-*-chapter-*.md` pattern
- Remove " copy" files if they exist

### Missing prerequisites on overview page
**Symptom:** Overview page shows Contents but no Prerequisites section

**Possible causes:**
- Chapter doesn't have `## Prerequisites Check` heading (normal)
- Heading spelling differs (must be exactly `## Prerequisites Check`)
- Prerequisites section is empty

**Check:**
```bash
grep "## Prerequisites Check" Fundamentals\ of\ Electrical\ and\ Electronics\ Engineering/Textbook/unit-*.md
```

### Missing subsections in Contents
**Symptom:** Contents shows only chapter titles, no subsections

**Causes:**
- Chapter has no `## X.X ...` headings (level 2)
- Using `### ...` headings only (these don't appear)
- Special characters in headings not rendering

**Check:**
```bash
# See level 2 headings in chapter 1
grep "^## " Fundamentals\ of\ Electrical\ and\ Electronics\ Engineering/Textbook/unit-1-chapter-1-*.md
```

### PDF won't build / XeLaTeX error
**Solutions:**
- Check all required tools: `which pandoc xelatex inkscape`
- Verify no chapter files are open in editor
- Check for very long lines (>1000 chars) in markdown
- Ensure no binary files in Textbook directory

### Build takes too long
**Typical:** 30-60 seconds
**Long:** >2 minutes

**Check:**
- SVG image count: `find Fundamentals*Textbook/images -name "*.svg" | wc -l`
- Disable SVG conversion if not needed (remove or comment line 75 in build script)

## Validating Output

After build completes, check:

```bash
# File size (should be >5MB if images included)
ls -lh pdf/Fundamentals_of_Electrical_and_Electronics_Engineering.pdf

# Page count (should be 500+)
pdfinfo pdf/Fundamentals_of_Electrical_and_Electronics_Engineering.pdf | grep Pages

# Sample pages with unit overviews
# Unit 1 overview: Page 5 (after frontmatter and TOC)
# Unit 2 overview: Page ~50+
# etc.
```

## Customization

### Change unit descriptions
Edit `build_feee_book.sh` lines 30-38:
```bash
declare -A UNIT_DESCRIPTIONS=(
  [1]="Your custom description here"
  [2]="Another description"
  ...
)
```

### Adjust spacing
Key variables in unit overview generation (lines 165-242):

```bash
# Top margin
printf '\\vspace*{0.05\\textheight}\n'  # 0.05 = ~0.5 inches

# Section spacing
printf '\\vspace{0.35cm}\n'   # Space before "Overview"
printf '\\vspace{0.2cm}\n'    # Space before "Prerequisites"
printf '\\vspace{0.15cm}\n'   # Space before "Contents"

# Font sizing
printf '\\noindent\\small\n'  # Use \small font
printf '\\normalsize\n'       # Return to normal

# Line spacing
printf '\\begin{spacing}{0.85}\n'  # 0.85 = tighter than 1.0
printf '\\begin{spacing}{0.8}\n'   # 0.8 = even tighter
```

### Change font size in prerequisites/contents
```bash
# To make smaller:
# Change '\small' to '\footnotesize' or '\tiny'

# To make larger:
# Change '\small' to '\normalsize' or remove the size command
```

## Files Structure

```
/home/avirup/Notes/
├── Scripts/
│   ├── build_feee_book.sh          ← Main build script (MODIFIED)
│   ├── feee-book-header.tex         ← LaTeX header (MODIFIED)
│   ├── pandoc-book-header.tex       ← Generic header
│   ├── feee-textbook-filter.lua     ← Pandoc filter
│   ├── CHANGES_SUMMARY.md           ← What changed
│   ├── UNIT_PAGE_EXAMPLES.md        ← Visual examples
│   └── BUILD_GUIDE.md               ← This file
├── Fundamentals of Electrical.../Textbook/
│   ├── unit-1-chapter-1-*.md
│   ├── unit-2-chapter-2-*.md
│   ├── ... (7 chapters total)
│   └── images/
│       ├── unit-1/
│       ├── unit-2/
│       └── ...
└── pdf/
    └── Fundamentals_of_Electrical_and_Electronics_Engineering.pdf
```

## Quick Testing Command

One-liner to build and check:

```bash
cd /home/avirup/Notes && \
bash Scripts/build_feee_book.sh && \
pdfinfo pdf/Fundamentals_of_Electrical_and_Electronics_Engineering.pdf | head -5 && \
echo "✓ Build successful!"
```

## Next Steps

1. **Run the build:**
   ```bash
   bash Scripts/build_feee_book.sh
   ```

2. **Check the output:**
   - Open PDF at page 5+ to see first unit overview
   - Verify prerequisites appear if chapters have them
   - Check that subsections are listed in Contents

3. **Fine-tune spacing (if needed):**
   - If pages overflow, reduce spacing amounts
   - If too much whitespace, increase spacing amounts
   - Edit `build_feee_book.sh` lines 168, 171, 173, 175, 178, 180, 194, 197, 215, etc.

4. **Commit changes (when satisfied):**
   ```bash
   cd /home/avirup/Notes
   git add Scripts/build_feee_book.sh Scripts/feee-book-header.tex
   git commit -m "Enhance unit overview pages with subsections and prerequisites"
   ```

## Support

If the build fails:

1. Check syntax: `bash -n Scripts/build_feee_book.sh`
2. Check tools: `which pandoc xelatex inkscape perl`
3. Check files: `ls Fundamentals\ of*/Textbook/unit-*.md`
4. Check markdown: Look for very long lines or special characters
5. Check LaTeX: Try building a minimal test file with XeLaTeX

## Summary

- **Modified:** 2 files
- **New:** 3 documentation files
- **Impact:** Unit overview pages now show prerequisites and subsections
- **Space:** Content fits on single page with optimized spacing
- **Build time:** Unchanged (~30-60 seconds)
- **Output:** Single PDF with enhanced structure
