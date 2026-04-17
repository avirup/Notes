#!/usr/bin/env bash

set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
BOOK_DIR="$ROOT_DIR/Power Electronics"
OUTPUT_DIR="$ROOT_DIR/pdf"
SCRIPT_DIR="$ROOT_DIR/Scripts"
HEADER_FILE="$SCRIPT_DIR/pandoc-book-header.tex"
OUTPUT_FILE="$OUTPUT_DIR/Power_Electronics_Fundamentals_for_Renewable_Energy_Systems.pdf"
TITLE="Power Electronics Fundamentals for Renewable Energy Systems"
SUBTITLE="Compiled from the chapter markdown sources in this repository"
AUTHOR_NAME="${BOOK_AUTHOR:-Avirup}"
ISBN_VALUE="${BOOK_ISBN:-979-8-00000-000-0 (placeholder; replace with assigned ISBN)}"
COPYRIGHT_YEAR="${BOOK_COPYRIGHT_YEAR:-$(date +%Y)}"
COPYRIGHT_HOLDER="${BOOK_COPYRIGHT_HOLDER:-$AUTHOR_NAME}"

declare -A MODULE_TITLES=(
  [1]="Power Semiconductor Devices"
  [2]="Device Protection, Gate Drive and Thermal Management"
  [3]="AC to DC Converters (Controlled Rectifiers)"
  [4]="DC to DC Converters"
  [5]="DC to AC Converters (Inverters)"
  [6]="AC to AC Converters and Power Quality in Renewable Energy Systems"
)

declare -A MODULE_DESCRIPTIONS=(
  [1]="This module introduces the principal power semiconductor devices used in renewable-energy converters, emphasizing structure, operation, characteristics, switching behavior, and device-selection context."
  [2]="This module develops the practical support circuits that make power switches reliable in real hardware, covering drive requirements, snubbers, electrical protection, and thermal design."
  [3]="This module explains controlled rectifier circuits that convert AC to adjustable DC, with attention to firing angle control, waveforms, average output relations, and renewable-energy applications."
  [4]="This module presents DC-DC conversion principles and the converter families used in renewable-energy and storage systems, from basic choppers to isolated and bidirectional topologies."
  [5]="This module covers inverter fundamentals, switching strategies, PWM methods, and converter structures used to synthesize AC from DC sources in renewable-energy systems."
  [6]="This module studies AC voltage and frequency conversion together with power-quality considerations, connecting converter operation to filtering and grid-interface performance."
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

mkdir -p "$OUTPUT_DIR" "$SCRIPT_DIR"

tmp_dir="$(mktemp -d)"
trap 'rm -rf "$tmp_dir"' EXIT

processed_dir="$tmp_dir/processed"
mkdir -p "$processed_dir/images"

mapfile -t chapter_files < <(printf '%s\n' "$BOOK_DIR"/module-*-chapter-*.md | sort -V)

if [[ "${#chapter_files[@]}" -eq 0 ]]; then
  echo "No chapter markdown files found under: $BOOK_DIR" >&2
  exit 1
fi

while IFS= read -r -d '' svg_file; do
  rel_path="${svg_file#"$BOOK_DIR"/}"
  target_pdf="$processed_dir/${rel_path%.svg}.pdf"
  mkdir -p "$(dirname "$target_pdf")"
  inkscape "$svg_file" --export-filename="$target_pdf" >/dev/null 2>&1
done < <(find "$BOOK_DIR/images" -type f -name '*.svg' -print0)

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
  - a4paper
  - inner=28mm
  - outer=22mm
  - top=24mm
  - bottom=28mm
  - headsep=10mm
linestretch: 1.15
toc: false
colorlinks: false
linkcolor: black
urlcolor: black
lof: false
lot: false
---

\\frontmatter
\\pagenumbering{gobble}

# Copyright and License

**Title:** $TITLE

**Author:** $AUTHOR_NAME

**ISBN:** $ISBN_VALUE

**Copyright:** Copyright (c) $COPYRIGHT_YEAR $COPYRIGHT_HOLDER

**License file:** \`LICENSE.md\`

**License:** $license_title

**Repository note:** This PDF is generated from the chapter markdown files stored under \`Power Electronics/\`.

\\clearpage

EOF
  cat <<'EOF'

\tableofcontents
\clearpage
\mainmatter
EOF
} > "$frontmatter_file"

assembled_parts=("$frontmatter_file")
processed_chapters=()
last_module=""

for chapter in "${chapter_files[@]}"; do
  rel_name="${chapter#"$BOOK_DIR"/}"
  target_md="$processed_dir/$rel_name"
  mkdir -p "$(dirname "$target_md")"
  sed 's/\.svg)/.pdf)/g; s/\.svg[[:space:]]*$/\.pdf/g' "$chapter" > "$target_md"
  processed_chapters+=("$target_md")

  module_number="$(basename "$chapter" | sed -E 's/^module-([0-9]+)-chapter-.*/\1/')"
  if [[ "$module_number" != "$last_module" ]]; then
    module_intro="$tmp_dir/module-${module_number}-intro.md"
    module_title="${MODULE_TITLES[$module_number]:-Module $module_number}"
    module_description="${MODULE_DESCRIPTIONS[$module_number]:-This module groups the chapters associated with Module $module_number in the source collection.}"
    {
      printf '\\clearpage\n'
      printf '\\thispagestyle{empty}\n'
      printf '\\vspace*{0.14\\textheight}\n'
      printf '\\begin{center}\n'
      printf '{\\Large\\scshape Module %s\\par}\n' "$module_number"
      printf '\\vspace{0.7cm}\n'
      printf '\\rule{0.72\\textwidth}{0.6pt}\\par\n'
      printf '\\vspace{0.8cm}\n'
      printf '{\\Huge\\bfseries %s\\par}\n' "$module_title"
      printf '\\vspace{0.8cm}\n'
      printf '\\rule{0.72\\textwidth}{0.6pt}\\par\n'
      printf '\\end{center}\n\n'
      printf '\\vspace{1.0cm}\n'
      printf '\\noindent\\textbf{Overview}\\par\n'
      printf '\\vspace{0.35cm}\n'
      printf '%s\n\n' "$module_description"
      printf '\\vspace{0.5cm}\n'
      printf '\\noindent\\textbf{Contents}\\par\n'
      printf '\\vspace{0.3cm}\n\n'
      for grouped_chapter in "${chapter_files[@]}"; do
        grouped_module="$(basename "$grouped_chapter" | sed -E 's/^module-([0-9]+)-chapter-.*/\1/')"
        if [[ "$grouped_module" == "$module_number" ]]; then
          grouped_heading="$(sed -n '1s/^# //p' "$grouped_chapter" | tr -d '\r')"
          [[ -n "$grouped_heading" ]] || grouped_heading="$(basename "$grouped_chapter" .md)"
          printf -- '- %s\n' "$grouped_heading"
        fi
      done
      if [[ "$module_number" == "1" ]]; then
        printf '\n\\setcounter{page}{0}\n'
      fi
      printf '\n\\clearpage\n'
    } > "$module_intro"
    assembled_parts+=("$module_intro")
    last_module="$module_number"
  fi

  assembled_parts+=("$target_md")
done

pandoc \
  "${assembled_parts[@]}" \
  --from markdown+tex_math_dollars+raw_tex \
  --resource-path="$processed_dir:$BOOK_DIR:$ROOT_DIR" \
  --top-level-division=chapter \
  --pdf-engine=xelatex \
  --include-in-header="$HEADER_FILE" \
  --output="$OUTPUT_FILE"

echo "Created: $OUTPUT_FILE"
