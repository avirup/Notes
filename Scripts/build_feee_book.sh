#!/usr/bin/env bash

set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
BOOK_DIR="$ROOT_DIR/Fundamentals of Electrical and Electronics Engineering/Textbook"
OUTPUT_DIR="$ROOT_DIR/pdf"
SCRIPT_DIR="$ROOT_DIR/Scripts"
HEADER_FILE="$SCRIPT_DIR/pandoc-book-header.tex"
FEEE_HEADER_FILE="$SCRIPT_DIR/feee-book-header.tex"
TEXTBOOK_FILTER="$SCRIPT_DIR/feee-textbook-filter.lua"
OUTPUT_FILE="$OUTPUT_DIR/Fundamentals_of_Electrical_and_Electronics_Engineering.pdf"
TITLE="Fundamentals of Electrical and Electronics Engineering"
SUBTITLE="Compiled from the textbook chapter markdown sources in this repository"
AUTHOR_NAME="${BOOK_AUTHOR:-Avirup}"
ISBN_VALUE="${BOOK_ISBN:-979-8-00000-000-0 (placeholder; replace with assigned ISBN)}"
COPYRIGHT_YEAR="${BOOK_COPYRIGHT_YEAR:-$(date +%Y)}"
COPYRIGHT_HOLDER="${BOOK_COPYRIGHT_HOLDER:-$AUTHOR_NAME}"

declare -A UNIT_TITLES=(
  [1]="Basic Electrical Quantities, Components, and Sources"
  [2]="Magnetic Circuits and Electromagnetic Induction"
  [3]="A.C. Circuits"
  [4]="Transformer and Machines"
  [5]="Overview of Basic Semiconductor Devices"
  [6]="Overview of Analog Circuits"
  [7]="Overview of Digital Electronics"
)

declare -A UNIT_DESCRIPTIONS=(
  [1]="This unit builds the basic language of electrical engineering, introducing the core quantities, passive components, waveform families, source models, and practical measurement ideas used throughout the book."
  [2]="This unit develops magnetic-circuit ideas and electromagnetic induction, connecting field concepts to induced EMF, energy transfer, and the operating principles behind transformers and machines."
  [3]="This unit introduces alternating-current circuit analysis, including sinusoidal quantities, phase relationships, reactance, impedance, power in AC systems, and simple RLC behavior."
  [4]="This unit presents the basic construction, principles, and operating ideas of transformers and electrical machines, with emphasis on conceptual understanding before detailed machine theory."
  [5]="This unit introduces semiconductor materials and the fundamental devices built from them, preparing the reader for later study of rectifiers, transistors, switching, and electronic systems."
  [6]="This unit surveys foundational analog-circuit ideas such as amplification, biasing, signal handling, and the role of analog building blocks in instrumentation and control."
  [7]="This unit introduces digital-electronics fundamentals, including logic levels, gates, Boolean reasoning, combinational building blocks, and the basic interpretation of digital systems."
)

require_tool() {
  if ! command -v "$1" >/dev/null 2>&1; then
    echo "Missing required tool: $1" >&2
    exit 1
  fi
}

require_tool pandoc
require_tool xelatex
require_tool inkscape
require_tool perl

mkdir -p "$OUTPUT_DIR" "$SCRIPT_DIR"

tmp_dir="$(mktemp -d)"
trap 'rm -rf "$tmp_dir"' EXIT

processed_dir="$tmp_dir/processed"
mkdir -p "$processed_dir/images"

mapfile -t chapter_files < <(
  find "$BOOK_DIR" -maxdepth 1 -type f -name 'unit-*-chapter-*.md' ! -name '* copy.md' | sort -V
)

if [[ "${#chapter_files[@]}" -eq 0 ]]; then
  echo "No chapter markdown files found under: $BOOK_DIR" >&2
  exit 1
fi

if [[ -d "$BOOK_DIR/images" ]]; then
  while IFS= read -r -d '' svg_file; do
    rel_path="${svg_file#"$BOOK_DIR"/}"
    target_pdf="$processed_dir/${rel_path%.svg}.pdf"
    mkdir -p "$(dirname "$target_pdf")"
    inkscape "$svg_file" --export-filename="$target_pdf" >/dev/null 2>&1
  done < <(find "$BOOK_DIR/images" -type f -name '*.svg' -print0)
fi

license_title="$(sed -n '1p' "$ROOT_DIR/LICENSE.md" | tr -d '\r')"
if [[ -z "$license_title" ]]; then
  license_title="See LICENSE.md"
fi

frontmatter_file="$tmp_dir/frontmatter.md"
{
  cat <<EOF
---
lang: en-US
documentclass: book
classoption:
  - 11pt
  - openany
  - twoside
fontsize: 11pt
geometry:
  - paperwidth=7in
  - paperheight=10in
  - inner=0.90in
  - outer=0.72in
  - top=0.64in
  - bottom=0.82in
  - headsep=0.18in
linestretch: 1.22
toc: false
colorlinks: false
linkcolor: black
urlcolor: black
lof: false
lot: false
---

\frontmatter
\pagenumbering{gobble}

# Copyright and License

**Title:** $TITLE

**Author:** $AUTHOR_NAME

**ISBN:** $ISBN_VALUE

**Copyright:** Copyright (c) $COPYRIGHT_YEAR $COPYRIGHT_HOLDER

**License file:** \`LICENSE.md\`

**License:** $license_title

**Repository note:** This PDF is generated from the chapter markdown files stored under \`Fundamentals of Electrical and Electronics Engineering/Textbook/\`.

\clearpage

EOF
  cat <<'EOF'

\tableofcontents
\clearpage
\mainmatter
EOF
} > "$frontmatter_file"

assembled_parts=("$frontmatter_file")
last_unit=""

for chapter in "${chapter_files[@]}"; do
  rel_name="${chapter#"$BOOK_DIR"/}"
  target_md="$processed_dir/$rel_name"
  mkdir -p "$(dirname "$target_md")"
  perl -0pe '
    s{<figure[^>]*>\s*<img\s+src="([^"]+)"\s+alt="([^"]*)"[^>]*/>\s*<figcaption[^>]*>(.*?)</figcaption>\s*</figure>}{
      my ($src, $alt, $caption) = ($1, $2, $3);
      $caption =~ s/<[^>]+>//g;
      $caption =~ s/\s+/ /g;
      $caption =~ s/^\s+|\s+$//g;
      $caption = $alt if $caption eq "";
      "\n![$caption]($src)\n";
    }gex
  ' "$chapter" | sed 's/\.svg)/.pdf)/g; s/\.svg[[:space:]]*$/\.pdf/g' > "$target_md"

  unit_number="$(basename "$chapter" | sed -E 's/^unit-([0-9]+)-chapter-.*/\1/')"
  if [[ "$unit_number" != "$last_unit" ]]; then
    unit_intro="$tmp_dir/unit-${unit_number}-intro.md"
    unit_title="${UNIT_TITLES[$unit_number]:-Unit $unit_number}"
    unit_description="${UNIT_DESCRIPTIONS[$unit_number]:-This unit groups the chapters associated with Unit $unit_number in the source collection.}"

    {
      printf '\\clearpage\n'
      printf '\\thispagestyle{empty}\n'
      printf '\\vspace*{0.04\\textheight}\n'
      printf '\\begin{center}\n'
      printf '{\\large\\scshape Unit %s\\par}\n' "$unit_number"
      printf '\\vspace{0.35cm}\n'
      printf '\\rule{0.72\\textwidth}{0.7pt}\\par\n'
      printf '\\vspace{0.35cm}\n'
      printf '{\\Huge\\bfseries %s\\par}\n' "$unit_title"
      printf '\\vspace{0.35cm}\n'
      printf '\\rule{0.72\\textwidth}{0.7pt}\\par\n'
      printf '\\end{center}\n\n'
      printf '\\vspace{0.4cm}\n'
      printf '{\\Large\\textbf{Overview}\\par}\n'
      printf '\\vspace{0.2cm}\n'
      printf '\\noindent %s\n\n' "$unit_description"

      # Check if there are any prerequisites
      has_prerequisites=false
      for grouped_chapter in "${chapter_files[@]}"; do
        grouped_unit="$(basename "$grouped_chapter" | sed -E 's/^unit-([0-9]+)-chapter-.*/\1/')"
        if [[ "$grouped_unit" == "$unit_number" ]] && grep -q "^## Prerequisites Check" "$grouped_chapter"; then
          has_prerequisites=true
          break
        fi
      done

      if [[ "$has_prerequisites" == "true" ]]; then
        printf '\\vspace{0.3cm}\n'
        printf '{\\Large\\textbf{Prerequisites}\\par}\n'
        printf '\\vspace{0.2cm}\n'
        printf '\\begin{spacing}{0.9}\n'
        for grouped_chapter in "${chapter_files[@]}"; do
          grouped_unit="$(basename "$grouped_chapter" | sed -E 's/^unit-([0-9]+)-chapter-.*/\1/')"
          if [[ "$grouped_unit" == "$unit_number" ]]; then
            grouped_heading="$(sed -n '1s/^# //p' "$grouped_chapter" | tr -d '\r')"
            [[ -n "$grouped_heading" ]] || grouped_heading="$(basename "$grouped_chapter" .md)"
            if grep -q "^## Prerequisites Check" "$grouped_chapter"; then
              # Extract prerequisites (between "## Prerequisites Check" and next ## or EOF)
              prereq_text=$(sed -n '/^## Prerequisites Check/,/^## [^#]/p' "$grouped_chapter" | sed '/^## Prerequisites Check/d; /^## [^#]/d; /^$/d' | tr '\n' ' ')
              if [[ -n "$prereq_text" ]]; then
                printf '\\noindent\\textit{%s:} %s\n\n' "$grouped_heading" "$prereq_text"
              fi
            fi
          fi
        done
        printf '\\end{spacing}\n'
        printf '\\vspace{0.2cm}\n'
      fi

      printf '\\vspace{0.3cm}\n'
      printf '{\\Large\\textbf{Contents}\\par}\n'
      printf '\\vspace{0.2cm}\n'
      printf '\\begin{spacing}{1.0}\n'

      for grouped_chapter in "${chapter_files[@]}"; do
        grouped_unit="$(basename "$grouped_chapter" | sed -E 's/^unit-([0-9]+)-chapter-.*/\1/')"
        if [[ "$grouped_unit" == "$unit_number" ]]; then
          grouped_heading="$(sed -n '1s/^# //p' "$grouped_chapter" | tr -d '\r')"
          [[ -n "$grouped_heading" ]] || grouped_heading="$(basename "$grouped_chapter" .md)"
          printf '\\noindent\\textbf{%s}\n' "$grouped_heading"

          # Extract ONLY numbered subsections (## X.X format) - exclude unrelated sections
          grep "^## [0-9]\+\.[0-9]\+ " "$grouped_chapter" | sed 's/^## //' | while IFS= read -r subsection; do
            printf '\\quad %s\n' "$subsection"
          done
          printf '\\vspace{0.1cm}\n'
        fi
      done
      printf '\\end{spacing}\n'

      if [[ "$unit_number" == "1" ]]; then
        printf '\n\\setcounter{page}{0}\n'
      fi
      printf '\n\\clearpage\n'
    } > "$unit_intro"
    assembled_parts+=("$unit_intro")
    last_unit="$unit_number"
  fi

  assembled_parts+=("$target_md")
done

pandoc \
  "${assembled_parts[@]}" \
  --from markdown+tex_math_dollars+raw_tex+fenced_divs \
  --resource-path="$processed_dir:$BOOK_DIR:$ROOT_DIR" \
  --top-level-division=chapter \
  --pdf-engine=xelatex \
  --include-in-header="$HEADER_FILE" \
  --include-in-header="$FEEE_HEADER_FILE" \
  --lua-filter="$TEXTBOOK_FILTER" \
  --output="$OUTPUT_FILE"

echo "Created: $OUTPUT_FILE"
