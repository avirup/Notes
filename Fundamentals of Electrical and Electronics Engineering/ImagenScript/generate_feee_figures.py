#!/usr/bin/env python3

from __future__ import annotations

import argparse
import math
import os
import re
import shutil
import subprocess
import tempfile
from pathlib import Path

os.environ.setdefault("MPLCONFIGDIR", str(Path(tempfile.gettempdir()) / "matplotlib"))

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import numpy as np
from matplotlib import patches


ROOT = Path(__file__).resolve().parents[2]
TEXTBOOK_DIR = ROOT / "Fundamentals of Electrical and Electronics Engineering" / "Textbook"
UNIT1_IMAGE_DIR = TEXTBOOK_DIR / "images" / "unit-1"
UNIT3_IMAGE_DIR = TEXTBOOK_DIR / "images" / "unit-3"

PRIMARY = "#1f3a5f"
ACCENT = "#c25b20"
GREEN = "#1e6f5c"
RED = "#b23a48"
PURPLE = "#6d597a"
GOLD = "#d4a72c"
GRAY = "#5f6b7a"
LIGHT_BLUE = "#d9eaf7"
LIGHT_ORANGE = "#f7ead9"
LIGHT_GREEN = "#dff1ea"


def ensure_parent(path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)


def run_command(args: list[str], cwd: Path | None = None) -> None:
    subprocess.run(args, cwd=cwd, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)


def add_white_background_to_svg(svg_path: Path) -> None:
    svg_text = svg_path.read_text(encoding="utf-8")
    svg_text = re.sub(r'\s*<rect id="svg-background"[^>]*/>\s*', "\n", svg_text, count=1)

    background = '  <rect id="svg-background" x="0" y="0" width="100%" height="100%" fill="#ffffff" />\n'
    svg_start = svg_text.find("<svg")
    if svg_start == -1:
        raise ValueError(f"Unexpected SVG structure in {svg_path}")
    svg_open_end = svg_text.find(">", svg_start)
    if svg_open_end == -1:
        raise ValueError(f"Unexpected SVG structure in {svg_path}")
    svg_text = f"{svg_text[: svg_open_end + 1]}\n{background}{svg_text[svg_open_end + 1 :]}"

    svg_path.write_text(svg_text, encoding="utf-8")


def render_circuitikz_svg(tex_body: str, output_svg: Path) -> None:
    ensure_parent(output_svg)
    with tempfile.TemporaryDirectory(prefix="circuitikz-") as tmp_name:
        tmpdir = Path(tmp_name)
        tex_path = tmpdir / "figure.tex"
        pdf_path = tmpdir / "figure.pdf"

        tex_source = rf"""
\documentclass[tikz,border=4pt]{{standalone}}
\usepackage{{circuitikz}}
\usepackage{{amsmath}}
\usetikzlibrary{{arrows.meta,positioning}}
\begin{{document}}
{tex_body}
\end{{document}}
""".strip()

        tex_path.write_text(tex_source, encoding="utf-8")
        run_command(
            [
                "pdflatex",
                "-interaction=nonstopmode",
                "-halt-on-error",
                "-output-directory",
                str(tmpdir),
                str(tex_path),
            ]
        )
        run_command(
            [
                "inkscape",
                str(pdf_path),
                "--export-area-drawing",
                "--export-type=svg",
                f"--export-filename={output_svg}",
            ]
        )
    add_white_background_to_svg(output_svg)


def style_axis(ax: plt.Axes) -> None:
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.grid(True, alpha=0.2, linewidth=0.6)
    ax.set_axisbelow(True)


def setup_clean_axes(
    ax: plt.Axes,
    xlim: tuple[float, float],
    ylim: tuple[float, float],
    *,
    equal: bool = False,
) -> None:
    ax.set_xlim(*xlim)
    ax.set_ylim(*ylim)
    if equal:
        ax.set_aspect("equal", adjustable="box")
    ax.axis("off")


def draw_phasor_axis(ax: plt.Axes, title: str) -> None:
    ax.axhline(0.0, color="0.75", linewidth=0.8)
    ax.axvline(0.0, color="0.75", linewidth=0.8)
    ax.set_xlim(-0.2, 1.35)
    ax.set_ylim(-0.9, 1.15)
    ax.set_aspect("equal", adjustable="box")
    ax.set_xticks([])
    ax.set_yticks([])
    for spine in ax.spines.values():
        spine.set_visible(False)
    ax.set_title(title, fontsize=12, pad=8)


def add_phasor(ax: plt.Axes, angle_rad: float, label: str, color: str) -> None:
    x = math.cos(angle_rad)
    y = math.sin(angle_rad)
    ax.annotate(
        "",
        xy=(x, y),
        xytext=(0.0, 0.0),
        arrowprops=dict(arrowstyle="->", lw=2.2, color=color),
    )
    ax.text(x + 0.04, y + 0.04, label, color=color, fontsize=11, fontweight="bold")


def save_svg(fig: plt.Figure, output_svg: Path) -> None:
    ensure_parent(output_svg)
    fig.savefig(output_svg, format="svg", bbox_inches="tight")
    plt.close(fig)


def draw_resistor_symbol(
    ax: plt.Axes,
    x0: float,
    x1: float,
    y: float,
    *,
    amplitude: float = 0.06,
    turns: int = 6,
    color: str = PRIMARY,
    linewidth: float = 2.0,
) -> None:
    xs = np.linspace(x0, x1, 2 * turns + 1)
    ys = np.full_like(xs, y)
    for idx in range(1, len(xs) - 1):
        ys[idx] = y + amplitude * (1 if idx % 2 else -1)
    ax.plot(xs, ys, color=color, linewidth=linewidth)


def draw_capacitor_symbol(
    ax: plt.Axes,
    x_center: float,
    y: float,
    *,
    height: float = 0.18,
    gap: float = 0.04,
    color: str = PRIMARY,
) -> None:
    ax.plot(
        [x_center - gap / 2.0, x_center - gap / 2.0],
        [y - height / 2.0, y + height / 2.0],
        color=color,
        linewidth=2.0,
    )
    ax.plot(
        [x_center + gap / 2.0, x_center + gap / 2.0],
        [y - height / 2.0, y + height / 2.0],
        color=color,
        linewidth=2.0,
    )


def draw_polarized_capacitor_symbol(ax: plt.Axes, x_center: float, y: float) -> None:
    ax.plot([x_center - 0.02, x_center - 0.02], [y - 0.09, y + 0.09], color=PRIMARY, linewidth=2.0)
    theta = np.linspace(-np.pi / 2.0, np.pi / 2.0, 100)
    ax.plot(x_center + 0.03 + 0.035 * np.cos(theta), y + 0.09 * np.sin(theta), color=PRIMARY, linewidth=2.0)
    ax.text(x_center - 0.075, y + 0.11, "+", color=RED, fontsize=12, fontweight="bold")


def draw_inductor_symbol(
    ax: plt.Axes,
    x0: float,
    x1: float,
    y: float,
    *,
    loops: int = 4,
    radius: float = 0.04,
    color: str = PRIMARY,
    linewidth: float = 2.0,
) -> None:
    spacing = (x1 - x0) / loops
    for idx in range(loops):
        center = x0 + spacing * idx + spacing / 2.0
        theta = np.linspace(np.pi, 0.0, 100)
        ax.plot(center + radius * np.cos(theta), y + radius * np.sin(theta), color=color, linewidth=linewidth)


def draw_axial_resistor(ax: plt.Axes, center_x: float, center_y: float, width: float = 0.4) -> None:
    body_w = width * 0.46
    body_h = 0.12
    left = center_x - body_w / 2.0
    right = center_x + body_w / 2.0
    ax.plot([center_x - width / 2.0, left], [center_y, center_y], color=GRAY, linewidth=2.0)
    ax.plot([right, center_x + width / 2.0], [center_y, center_y], color=GRAY, linewidth=2.0)
    ax.add_patch(
        patches.FancyBboxPatch(
            (left, center_y - body_h / 2.0),
            body_w,
            body_h,
            boxstyle="round,pad=0.02,rounding_size=0.04",
            facecolor="#e6c48c",
            edgecolor="#8a6338",
            linewidth=1.5,
        )
    )
    band_positions = np.linspace(left + 0.04, right - 0.04, 4)
    band_colors = ["#7a4e21", "#111111", "#c43d2b", "#d7b45e"]
    for x, color in zip(band_positions, band_colors):
        ax.add_patch(patches.Rectangle((x, center_y - body_h / 2.0), 0.02, body_h, facecolor=color, edgecolor="none"))


def draw_rotary_pot(ax: plt.Axes, center_x: float, center_y: float) -> None:
    ax.add_patch(patches.Circle((center_x, center_y), 0.1, facecolor="#5a6472", edgecolor="#2d3642", linewidth=1.5))
    ax.add_patch(patches.Circle((center_x, center_y), 0.03, facecolor="#d9dde3", edgecolor="none"))
    ax.plot([center_x, center_x + 0.08], [center_y, center_y + 0.08], color="#f4f6f8", linewidth=2.2)
    for dx in (-0.12, 0.0, 0.12):
        ax.plot([center_x + dx, center_x + dx], [center_y - 0.1, center_y - 0.18], color=GRAY, linewidth=2.0)


def draw_disc_capacitor(ax: plt.Axes, center_x: float, center_y: float) -> None:
    ax.add_patch(patches.Circle((center_x, center_y), 0.11, facecolor="#d9822b", edgecolor="#934d0f", linewidth=1.5))
    ax.plot([center_x - 0.04, center_x - 0.04], [center_y - 0.11, center_y - 0.22], color=GRAY, linewidth=2.0)
    ax.plot([center_x + 0.04, center_x + 0.04], [center_y - 0.11, center_y - 0.22], color=GRAY, linewidth=2.0)


def draw_electrolytic_can(ax: plt.Axes, center_x: float, center_y: float) -> None:
    ax.add_patch(
        patches.FancyBboxPatch(
            (center_x - 0.1, center_y - 0.14),
            0.2,
            0.28,
            boxstyle="round,pad=0.01,rounding_size=0.03",
            facecolor="#3c4a59",
            edgecolor="#1d2733",
            linewidth=1.5,
        )
    )
    ax.add_patch(patches.Rectangle((center_x + 0.05, center_y - 0.14), 0.03, 0.28, facecolor="#cfd6df", edgecolor="none"))
    ax.text(center_x + 0.065, center_y + 0.08, "-", color="#1d2733", fontsize=10, ha="center", va="center")
    ax.plot([center_x - 0.035, center_x - 0.035], [center_y - 0.14, center_y - 0.28], color=GRAY, linewidth=2.0)
    ax.plot([center_x + 0.035, center_x + 0.035], [center_y - 0.14, center_y - 0.24], color=GRAY, linewidth=2.0)
    ax.text(center_x - 0.06, center_y + 0.11, "+", color=RED, fontsize=11, fontweight="bold")


def draw_coil_component(ax: plt.Axes, center_x: float, center_y: float) -> None:
    ax.plot([center_x - 0.22, center_x - 0.14], [center_y, center_y], color=GRAY, linewidth=2.0)
    ax.plot([center_x + 0.14, center_x + 0.22], [center_y, center_y], color=GRAY, linewidth=2.0)
    radius = 0.035
    centers = np.linspace(center_x - 0.105, center_x + 0.105, 4)
    for xc in centers:
        theta = np.linspace(np.pi, 0.0, 80)
        ax.plot(xc + radius * np.cos(theta), center_y + radius * np.sin(theta), color=GREEN, linewidth=2.0)
    ax.add_patch(
        patches.FancyBboxPatch(
            (center_x - 0.14, center_y - 0.055),
            0.28,
            0.11,
            boxstyle="round,pad=0.01,rounding_size=0.03",
            facecolor="none",
            edgecolor="#9fb8aa",
            linewidth=1.0,
            linestyle="--",
        )
    )


def generate_unit1_emf_vs_potential_difference() -> Path:
    output = UNIT1_IMAGE_DIR / "figure-1-1-emf-vs-potential-difference.svg"
    tex_body = r"""
\begin{circuitikz}[american, scale=1.0]
\draw
  (0,0) to[battery1,l_=$\mathcal{E}$] (0,4)
  -- (5.0,4)
  to[lamp,l=$\text{Lamp}$] (5.0,0)
  -- (0,0);
\node at (0.42,3.65) {$+$};
\node at (0.42,0.35) {$-$};
\draw[-{Latex[length=3mm]}, very thick, blue] (0.8,4.45) -- (4.2,4.45)
  node[midway, above, black] {Conventional current $I$};
\draw[-{Latex[length=3mm]}, very thick, orange] (4.2,-0.45) -- (0.8,-0.45)
  node[midway, below, black] {Electron flow};
\draw[-{Latex[length=3mm]}, thick, teal!70!black] (-0.75,0.45) -- (-0.75,3.55)
  node[midway, left, align=center, black] {EMF at source\\raises charge energy};
\draw[-{Latex[length=3mm]}, thick, red!70!black] (6.05,3.45) -- (6.05,0.55)
  node[midway, right, align=center, black] {Potential difference\\across lamp};
\end{circuitikz}
"""
    render_circuitikz_svg(tex_body, output)
    return output


def generate_unit1_current_cross_section() -> Path:
    output = UNIT1_IMAGE_DIR / "figure-1-2-current-charge-flow.svg"
    fig, ax = plt.subplots(figsize=(11.5, 3.8))
    setup_clean_axes(ax, (0.0, 12.0), (0.0, 4.0))

    conductor = patches.FancyBboxPatch(
        (0.8, 1.35),
        8.8,
        1.3,
        boxstyle="round,pad=0.02,rounding_size=0.2",
        facecolor="#eff3f7",
        edgecolor="#8c99a5",
        linewidth=1.6,
    )
    ax.add_patch(conductor)
    ax.text(1.0, 2.85, "Conductor", fontsize=12, color=GRAY)

    cross_section_x = 5.2
    ax.plot([cross_section_x, cross_section_x], [1.0, 3.0], linestyle="--", color=RED, linewidth=1.8)
    ax.text(cross_section_x + 0.12, 2.92, "Reference cross-section", fontsize=11, color=RED, va="top")

    charge_positions = [(2.0, 2.2), (2.7, 1.75), (3.3, 2.3), (4.1, 1.95), (4.6, 2.35)]
    for x, y in charge_positions:
        ax.add_patch(patches.Circle((x, y), 0.11, facecolor=LIGHT_BLUE, edgecolor=PRIMARY, linewidth=1.3))
        ax.text(x, y, "-", fontsize=10, ha="center", va="center", color=PRIMARY, fontweight="bold")

    ax.annotate(
        "",
        xy=(4.85, 0.95),
        xytext=(1.65, 0.95),
        arrowprops=dict(arrowstyle="<->", linewidth=1.8, color=ACCENT),
    )
    ax.text(3.25, 0.55, r"Charge $Q$ passes in time $t$", fontsize=12, ha="center", color=ACCENT)

    ax.annotate(
        "",
        xy=(4.9, 2.65),
        xytext=(1.5, 2.65),
        arrowprops=dict(arrowstyle="->", linewidth=2.2, color=PRIMARY),
    )
    ax.text(3.2, 2.95, "Net charge transfer", fontsize=11, ha="center", color=PRIMARY)

    formula_box = patches.FancyBboxPatch(
        (9.0, 1.35),
        2.3,
        1.25,
        boxstyle="round,pad=0.04,rounding_size=0.12",
        facecolor="#fffaf0",
        edgecolor=GOLD,
        linewidth=1.6,
    )
    ax.add_patch(formula_box)
    ax.text(10.15, 2.0, r"$I = \dfrac{Q}{t}$", fontsize=20, ha="center", va="center")
    ax.text(10.15, 1.52, "Current = charge flow rate", fontsize=11, ha="center", color=GRAY)

    save_svg(fig, output)
    return output


def generate_unit1_meter_connections() -> Path:
    output = UNIT1_IMAGE_DIR / "figure-1-3-meter-connections.svg"
    tex_body = r"""
\begin{circuitikz}[american]
\begin{scope}
\draw
  (0,0) to[battery1,l_=$V_s$] (0,4)
  to[ammeter,l=$A$] (3,4)
  -- (5,4)
  to[R,l=$R$] (5,0)
  -- (0,0);
\draw
  (5,4) -- (7,4)
  to[voltmeter,l=$V$] (7,0)
  -- (5,0);
\node[font=\bfseries, text=teal!70!black] at (3.5,5.0) {Correct};
\node[align=center] at (3.5,-1.0) {Ammeter in series\\Voltmeter in parallel};
\end{scope}

\begin{scope}[xshift=10.5cm]
\draw
  (0,0) to[battery1,l_=$V_s$] (0,4)
  to[voltmeter,l=$V$] (3,4)
  -- (5,4)
  to[R,l=$R$] (5,0)
  -- (0,0);
\draw
  (5,4) -- (7,4)
  to[ammeter,l=$A$] (7,0)
  -- (5,0);
\node[font=\bfseries, text=red!75!black] at (3.5,5.0) {Wrong};
\draw[red, line width=1.8pt] (-0.5,-0.6) -- (7.5,4.8);
\draw[red, line width=1.8pt] (-0.5,4.8) -- (7.5,-0.6);
\node[align=center] at (3.5,-1.0) {Voltmeter in series\\Ammeter across the load};
\end{scope}
\end{circuitikz}
"""
    render_circuitikz_svg(tex_body, output)
    return output


def generate_unit1_component_panel() -> Path:
    output = UNIT1_IMAGE_DIR / "figure-1-4-symbols-and-components.svg"
    fig, axes = plt.subplots(1, 5, figsize=(15.5, 4.2), constrained_layout=True)
    labels = ["Resistor", "Potentiometer", "Capacitor", "Electrolytic\ncapacitor", "Inductor"]

    for ax, label in zip(axes, labels):
        setup_clean_axes(ax, (0.0, 1.0), (0.0, 1.0))
        ax.text(0.5, 0.94, label, ha="center", va="top", fontsize=11.5, fontweight="bold", color=GRAY)
        ax.plot([0.12, 0.88], [0.5, 0.5], color="#d7dde5", linewidth=0.8, linestyle="--")

    draw_resistor_symbol(axes[0], 0.18, 0.82, 0.72, amplitude=0.06, turns=6)
    axes[0].plot([0.08, 0.18], [0.72, 0.72], color=PRIMARY, linewidth=2.0)
    axes[0].plot([0.82, 0.92], [0.72, 0.72], color=PRIMARY, linewidth=2.0)
    draw_axial_resistor(axes[0], 0.5, 0.26)

    draw_resistor_symbol(axes[1], 0.2, 0.78, 0.72, amplitude=0.05, turns=5)
    axes[1].plot([0.08, 0.2], [0.72, 0.72], color=PRIMARY, linewidth=2.0)
    axes[1].plot([0.78, 0.9], [0.72, 0.72], color=PRIMARY, linewidth=2.0)
    axes[1].annotate(
        "",
        xy=(0.6, 0.8),
        xytext=(0.42, 0.58),
        arrowprops=dict(arrowstyle="->", linewidth=1.8, color=ACCENT),
    )
    draw_rotary_pot(axes[1], 0.5, 0.28)

    axes[2].plot([0.08, 0.42], [0.72, 0.72], color=PRIMARY, linewidth=2.0)
    draw_capacitor_symbol(axes[2], 0.5, 0.72)
    axes[2].plot([0.58, 0.92], [0.72, 0.72], color=PRIMARY, linewidth=2.0)
    draw_disc_capacitor(axes[2], 0.5, 0.3)

    axes[3].plot([0.08, 0.42], [0.72, 0.72], color=PRIMARY, linewidth=2.0)
    draw_polarized_capacitor_symbol(axes[3], 0.5, 0.72)
    axes[3].plot([0.58, 0.92], [0.72, 0.72], color=PRIMARY, linewidth=2.0)
    draw_electrolytic_can(axes[3], 0.5, 0.3)

    axes[4].plot([0.08, 0.2], [0.72, 0.72], color=PRIMARY, linewidth=2.0)
    draw_inductor_symbol(axes[4], 0.2, 0.8, 0.72, loops=4, radius=0.05)
    axes[4].plot([0.8, 0.92], [0.72, 0.72], color=PRIMARY, linewidth=2.0)
    draw_coil_component(axes[4], 0.5, 0.28)

    save_svg(fig, output)
    return output


def generate_unit1_voltage_divider() -> Path:
    output = UNIT1_IMAGE_DIR / "figure-1-5-voltage-divider.svg"
    tex_body = r"""
\begin{circuitikz}[american]
\draw
  (0,0) node[ground] {}
  to[battery1,l_=$V_s$] (0,5)
  -- (3.5,5)
  to[R,l=$R_1$] (3.5,2.5)
  to[R,l=$R_2$] (3.5,0)
  node[ground] {};
\draw[fill] (3.5,2.5) circle (2.2pt);
\node[right] at (3.7,2.5) {$V_{out}$};
\draw[-{Latex[length=3mm]}, thick, teal!70!black] (1.2,4.7) -- (3.1,4.7)
  node[midway, above, black] {$I$};
\node[align=center] at (5.7,1.25) {Output taken\\with respect to ground};
\end{circuitikz}
"""
    render_circuitikz_svg(tex_body, output)
    return output


def generate_unit1_capacitor_field() -> Path:
    output = UNIT1_IMAGE_DIR / "figure-1-6-capacitor-field-and-polarity.svg"
    fig, axes = plt.subplots(1, 2, figsize=(12.5, 4.8), constrained_layout=True)

    ax = axes[0]
    setup_clean_axes(ax, (0.0, 10.0), (0.0, 5.0))
    ax.set_title("Parallel-plate capacitor", fontsize=12, pad=10)
    ax.add_patch(patches.Rectangle((2.0, 0.7), 0.28, 3.6, facecolor=PRIMARY, edgecolor=PRIMARY))
    ax.add_patch(patches.Rectangle((7.72, 0.7), 0.28, 3.6, facecolor=PRIMARY, edgecolor=PRIMARY))
    ax.add_patch(
        patches.FancyBboxPatch(
            (2.28, 0.7),
            5.44,
            3.6,
            boxstyle="round,pad=0.02,rounding_size=0.06",
            facecolor="#f8f1d6",
            edgecolor=GOLD,
            linewidth=1.5,
            alpha=0.85,
        )
    )
    ax.text(5.0, 4.55, "Dielectric", fontsize=12, ha="center", color="#8a6d1d")
    ax.text(1.45, 2.5, "+", fontsize=18, fontweight="bold", color=RED, ha="center", va="center")
    ax.text(8.55, 2.5, "-", fontsize=18, fontweight="bold", color=PRIMARY, ha="center", va="center")
    for y in np.linspace(1.15, 3.85, 6):
        ax.annotate(
            "",
            xy=(7.25, y),
            xytext=(2.75, y),
            arrowprops=dict(arrowstyle="->", linewidth=1.5, color=GREEN),
        )
    ax.text(5.0, 0.28, "Electric field lines point from + plate to - plate", ha="center", fontsize=11, color=GREEN)

    ax = axes[1]
    setup_clean_axes(ax, (0.0, 10.0), (0.0, 5.0))
    ax.set_title("Electrolytic capacitor polarity", fontsize=12, pad=10)
    ax.add_patch(
        patches.FancyBboxPatch(
            (4.0, 1.1),
            2.2,
            2.6,
            boxstyle="round,pad=0.02,rounding_size=0.18",
            facecolor="#3f4b59",
            edgecolor="#222b34",
            linewidth=1.6,
        )
    )
    ax.add_patch(patches.Rectangle((5.72, 1.1), 0.28, 2.6, facecolor="#d6dde7", edgecolor="none"))
    ax.text(5.86, 3.25, "-", fontsize=12, ha="center", va="center", color="#222b34", fontweight="bold")
    ax.text(4.35, 3.25, "+", fontsize=14, ha="center", va="center", color=RED, fontweight="bold")
    ax.plot([4.62, 4.62], [1.1, 0.22], color=GRAY, linewidth=2.3)
    ax.plot([5.38, 5.38], [1.1, 0.46], color=GRAY, linewidth=2.3)
    ax.text(4.62, 0.08, "+ terminal", ha="center", fontsize=11, color=RED)
    ax.text(5.95, 0.08, "- terminal", ha="center", fontsize=11, color=PRIMARY)
    ax.annotate(
        "Observe the polarity marks\nbefore connecting",
        xy=(6.0, 2.8),
        xytext=(8.2, 4.0),
        fontsize=11,
        ha="center",
        arrowprops=dict(arrowstyle="->", linewidth=1.4, color=ACCENT),
    )
    ax.text(5.1, 0.62, "Reverse connection can damage an electrolytic capacitor", ha="center", fontsize=10.5, color=GRAY)

    save_svg(fig, output)
    return output


def generate_unit1_rc_curves() -> Path:
    output = UNIT1_IMAGE_DIR / "figure-1-7-rc-charging-and-discharging.svg"
    t = np.linspace(0.0, 5.5, 600)
    vc_charge = 1.0 - np.exp(-t)
    ic_charge = np.exp(-t)
    vc_discharge = np.exp(-t)
    ic_discharge = -np.exp(-t)

    fig, axes = plt.subplots(1, 2, figsize=(13.0, 4.8), constrained_layout=True)
    configs = [
        ("Charging", vc_charge, ic_charge),
        ("Discharging", vc_discharge, ic_discharge),
    ]

    for ax, (title, vc, ic) in zip(axes, configs):
        ax.plot(t, vc, color=PRIMARY, linewidth=2.4, label=r"$V_C$")
        ax.plot(t, ic, color=ACCENT, linewidth=2.2, label=r"$I_C$")
        style_axis(ax)
        ax.set_xlim(0.0, 5.5)
        ax.set_ylim(-1.15, 1.15)
        ax.set_title(title, fontsize=12, pad=8)
        ax.set_xlabel(r"Time in multiples of $\tau = RC$")
        ax.set_ylabel("Normalized value")
        ax.axvline(1.0, color=PURPLE, linestyle="--", linewidth=1.4)
        ax.axvline(5.0, color=PURPLE, linestyle="--", linewidth=1.4)
        ax.text(1.0, 1.06, r"$\tau$", ha="center", va="bottom", fontsize=10, color=PURPLE)
        ax.text(5.0, 1.06, r"$5\tau$", ha="center", va="bottom", fontsize=10, color=PURPLE)
        ax.axhline(0.0, color="0.6", linewidth=0.9)
        ax.legend(loc="upper right", frameon=False)

    axes[0].scatter([1.0], [1.0 - math.e ** -1], color=PRIMARY, s=28, zorder=3)
    axes[0].annotate(
        "At 1τ, capacitor reaches\n63.2% of final voltage",
        xy=(1.0, 1.0 - math.e ** -1),
        xytext=(1.8, 0.55),
        fontsize=10,
        arrowprops=dict(arrowstyle="->", linewidth=1.2, color=PRIMARY),
    )
    axes[1].annotate(
        "By about 5τ,\nthe transient is practically complete",
        xy=(5.0, math.e ** -5),
        xytext=(2.65, 0.42),
        fontsize=10,
        arrowprops=dict(arrowstyle="->", linewidth=1.2, color=PRIMARY),
    )

    save_svg(fig, output)
    return output


def generate_unit1_inductor_field() -> Path:
    output = UNIT1_IMAGE_DIR / "figure-1-8-inductor-field-and-back-emf.svg"
    fig = plt.figure(figsize=(12.8, 4.8), constrained_layout=True)
    gs = fig.add_gridspec(2, 2, width_ratios=[1.15, 1.0], height_ratios=[1.0, 1.0])
    left = fig.add_subplot(gs[:, 0])
    top = fig.add_subplot(gs[0, 1])
    bottom = fig.add_subplot(gs[1, 1])

    setup_clean_axes(left, (0.0, 10.0), (0.0, 5.2), equal=False)
    left.set_title("Coil current creates a magnetic field", fontsize=12, pad=10)
    left.plot([0.8, 2.0], [2.6, 2.6], color=GRAY, linewidth=2.2)
    left.plot([8.0, 9.2], [2.6, 2.6], color=GRAY, linewidth=2.2)
    loop_centers = np.linspace(2.45, 7.55, 6)
    for xc in loop_centers:
        theta = np.linspace(np.pi, 0.0, 120)
        left.plot(xc + 0.42 * np.cos(theta), 2.6 + 0.42 * np.sin(theta), color=GREEN, linewidth=2.2)
    left.annotate(
        "",
        xy=(2.0, 3.45),
        xytext=(0.95, 3.45),
        arrowprops=dict(arrowstyle="->", linewidth=2.0, color=PRIMARY),
    )
    left.text(1.45, 3.75, "Current $i$", ha="center", fontsize=11, color=PRIMARY)
    for y, rad in zip((1.2, 2.0, 3.2, 4.0), (2.2, 2.55, 2.55, 2.2)):
        left.add_patch(
            patches.Arc((5.0, y), width=rad * 2.0, height=0.85 + 0.2 * abs(2.6 - y), theta1=15, theta2=165, color=PRIMARY, linewidth=1.2)
        )
        left.add_patch(
            patches.Arc((5.0, y), width=rad * 2.0, height=0.85 + 0.2 * abs(2.6 - y), theta1=195, theta2=345, color=PRIMARY, linewidth=1.2)
        )
    left.annotate(
        "",
        xy=(6.9, 2.9),
        xytext=(3.1, 2.9),
        arrowprops=dict(arrowstyle="->", linewidth=1.8, color=ACCENT),
    )
    left.text(5.0, 3.15, "Magnetic field $B$", ha="center", fontsize=11, color=ACCENT)
    left.text(5.0, 0.38, "The magnetic field stores energy while current is present", ha="center", fontsize=10.5, color=GRAY)

    time = np.array([0.0, 1.0, 3.8, 5.0])
    current = np.array([0.0, 0.0, 1.0, 1.0])
    voltage = np.array([0.0, 0.75, 0.75, 0.0])

    top.plot(time, current, color=PRIMARY, linewidth=2.3)
    style_axis(top)
    top.set_xlim(0.0, 5.0)
    top.set_ylim(-0.1, 1.15)
    top.set_title("Current command", fontsize=12, pad=6)
    top.set_ylabel(r"$i$")
    top.set_xticks([])
    top.annotate("Current tries to rise", xy=(2.45, 0.62), xytext=(0.8, 0.95), fontsize=10, arrowprops=dict(arrowstyle="->", linewidth=1.2, color=PRIMARY))

    bottom.plot(time, voltage, color=RED, linewidth=2.3)
    style_axis(bottom)
    bottom.set_xlim(0.0, 5.0)
    bottom.set_ylim(-0.1, 0.95)
    bottom.set_title(r"Inductor voltage $v_L = L \, di/dt$", fontsize=12, pad=6)
    bottom.set_xlabel("Time")
    bottom.set_ylabel(r"$v_L$")
    bottom.annotate(
        "Back EMF appears only while\ncurrent is changing",
        xy=(2.6, 0.75),
        xytext=(3.5, 0.35),
        fontsize=10,
        ha="center",
        arrowprops=dict(arrowstyle="->", linewidth=1.2, color=RED),
    )

    save_svg(fig, output)
    return output


def generate_unit1_waveform_families() -> Path:
    output = UNIT1_IMAGE_DIR / "figure-1-9-common-waveform-families.svg"
    t = np.linspace(0.0, 2.0, 800)
    sine = np.sin(2.0 * np.pi * t)
    square = np.where(np.sin(2.0 * np.pi * t) >= 0.0, 1.0, -1.0)
    triangular = 2.0 * np.abs(2.0 * (t - np.floor(t + 0.5))) - 1.0
    saw = 2.0 * (t - np.floor(t)) - 1.0
    pulse = np.where((t % 1.0) < 0.35, 1.0, 0.0)
    pulsating = np.abs(np.sin(2.0 * np.pi * t)) + 0.05

    fig, axes = plt.subplots(3, 2, figsize=(13.5, 9.5), sharex=False, constrained_layout=True)
    axes = axes.ravel()
    configs = [
        ("Sine wave", sine, PRIMARY),
        ("Square wave", square, ACCENT),
        ("Triangular wave", triangular, GREEN),
        ("Sawtooth wave", saw, PURPLE),
        ("Pulse waveform", pulse, RED),
        ("Pulsating DC", pulsating, GOLD),
    ]

    for ax, (title, values, color) in zip(axes, configs):
        ax.plot(t, values, color=color, linewidth=2.2)
        style_axis(ax)
        ax.set_xlim(0.0, 2.0)
        ax.set_ylim(-1.35, 1.35)
        ax.set_title(title, fontsize=11.5, pad=8)
        ax.set_xlabel("Time")
        ax.set_ylabel("Amplitude")
        ax.set_xticks([0.0, 0.5, 1.0, 1.5, 2.0])

    sine_ax = axes[0]
    sine_ax.annotate("", xy=(0.25, 1.0), xytext=(0.25, 0.0), arrowprops=dict(arrowstyle="<->", linewidth=1.4, color=GRAY))
    sine_ax.text(0.29, 0.54, "Amplitude", fontsize=9.8, color=GRAY)
    sine_ax.annotate("", xy=(1.55, 1.0), xytext=(1.55, -1.0), arrowprops=dict(arrowstyle="<->", linewidth=1.4, color=GRAY))
    sine_ax.text(1.61, 0.03, "Peak-to-peak", fontsize=9.8, color=GRAY)
    sine_ax.annotate("", xy=(1.0, 1.2), xytext=(0.0, 1.2), arrowprops=dict(arrowstyle="<->", linewidth=1.4, color=PURPLE))
    sine_ax.text(0.5, 1.24, r"Period $T$", fontsize=10, ha="center", color=PURPLE)
    sine_ax.text(0.98, -1.17, r"$f = 1/T$", fontsize=10, ha="right", color=PURPLE)

    pulse_ax = axes[4]
    pulse_ax.annotate("", xy=(0.35, 1.12), xytext=(0.0, 1.12), arrowprops=dict(arrowstyle="<->", linewidth=1.4, color=RED))
    pulse_ax.annotate("", xy=(1.0, 1.24), xytext=(0.0, 1.24), arrowprops=dict(arrowstyle="<->", linewidth=1.4, color=PURPLE))
    pulse_ax.text(0.175, 1.16, r"$t_{on}$", fontsize=9.7, ha="center", color=RED)
    pulse_ax.text(0.5, 1.28, r"$T$", fontsize=9.7, ha="center", color=PURPLE)
    pulse_ax.text(1.36, 0.84, "Duty cycle\n= $t_{on}/T$", fontsize=10, ha="left", color=RED)

    pulsating_ax = axes[5]
    offset = np.mean(pulsating)
    pulsating_ax.axhline(offset, color=GRAY, linestyle="--", linewidth=1.3)
    pulsating_ax.text(1.1, offset + 0.08, "DC offset / average value", fontsize=9.8, color=GRAY)
    pulsating_ax.set_ylim(-0.15, 1.35)

    save_svg(fig, output)
    return output


def generate_unit1_source_models() -> Path:
    output = UNIT1_IMAGE_DIR / "figure-1-10-ideal-and-practical-source-models.svg"
    tex_body = r"""
\begin{circuitikz}[american]
\begin{scope}[xshift=0.8cm]
\node[font=\bfseries\small] at (1.5,5.2) {Ideal V source};
\draw
  (1.5,0.4) node[ocirc] {}
  to[sV,l_=$V_s$] (1.5,4.2)
  node[ocirc] {};
\node at (1.5,-0.25) {Internal $R = 0$};
\end{scope}

\begin{scope}[xshift=6.6cm]
\node[font=\bfseries\small] at (1.5,5.2) {Practical V source};
\draw
  (1.5,0.4) node[ocirc] {}
  to[sV,l_=$\mathcal{E}$] (1.5,2.35)
  to[R,l=$r_s$] (1.5,4.2)
  node[ocirc] {};
\node at (1.5,-0.25) {Ideal EMF + series $r_s$};
\end{scope}

\begin{scope}[xshift=0.8cm,yshift=-6.0cm]
\node[font=\bfseries\small] at (1.5,5.2) {Ideal I source};
\draw
  (1.5,4.2) node[ocirc] {}
  to[I,l=$I_s$] (1.5,0.4)
  node[ocirc] {};
\node at (1.5,-0.25) {Internal $R \to \infty$};
\end{scope}

\begin{scope}[xshift=6.6cm,yshift=-6.0cm]
\node[font=\bfseries\small] at (1.8,5.2) {Practical I source};
\draw
  (0.8,4.2) node[ocirc] {}
  to[I,l=$I_s$] (0.8,0.4)
  node[ocirc] {};
\draw
  (0.8,4.2) -- (2.8,4.2)
  to[R,l=$R_p$] (2.8,0.4)
  -- (0.8,0.4);
\node at (1.8,-0.25) {Ideal source + parallel $R_p$};
\end{scope}
\end{circuitikz}
"""
    render_circuitikz_svg(tex_body, output)
    return output


def generate_unit1_terminal_characteristic() -> Path:
    output = UNIT1_IMAGE_DIR / "figure-1-11-terminal-characteristic.svg"
    emf = 12.0
    rs = 0.5
    isc = emf / rs
    current = np.linspace(0.0, isc, 300)
    terminal_voltage = emf - rs * current

    fig, ax = plt.subplots(figsize=(8.0, 5.0))
    ax.plot(current, terminal_voltage, color=PRIMARY, linewidth=2.4)
    style_axis(ax)
    ax.set_xlim(0.0, isc * 1.05)
    ax.set_ylim(0.0, emf * 1.1)
    ax.set_xlabel("Load current I (A)")
    ax.set_ylabel("Terminal voltage V (V)")
    ax.set_title(r"Practical voltage-source characteristic: $V = \mathcal{E} - I r_s$", fontsize=12, pad=10)

    ax.scatter([0.0, isc], [emf, 0.0], color=[GREEN, RED], s=35, zorder=3)
    ax.annotate(
        r"Open-circuit voltage $\mathcal{E}$",
        xy=(0.0, emf),
        xytext=(isc * 0.16, emf * 0.92),
        fontsize=10,
        arrowprops=dict(arrowstyle="->", linewidth=1.2, color=GREEN),
    )
    ax.annotate(
        r"Short-circuit current $I_{sc}$",
        xy=(isc, 0.0),
        xytext=(isc * 0.55, emf * 0.12),
        fontsize=10,
        arrowprops=dict(arrowstyle="->", linewidth=1.2, color=RED),
    )
    ax.annotate(
        r"Slope $= -r_s$",
        xy=(isc * 0.55, emf - rs * isc * 0.55),
        xytext=(isc * 0.28, emf * 0.46),
        fontsize=10,
        arrowprops=dict(arrowstyle="->", linewidth=1.2, color=ACCENT),
    )

    save_svg(fig, output)
    return output


def generate_unit1_load_regulation() -> Path:
    output = UNIT1_IMAGE_DIR / "figure-1-12-load-regulation-droop.svg"
    load_fraction = np.array([0.0, 0.25, 0.5, 0.75, 1.0])
    voltage = np.array([12.0, 11.9, 11.75, 11.55, 11.35])

    fig, ax = plt.subplots(figsize=(7.8, 4.6))
    ax.plot(load_fraction, voltage, color=ACCENT, linewidth=2.4, marker="o")
    style_axis(ax)
    ax.set_xlim(-0.02, 1.02)
    ax.set_ylim(11.1, 12.15)
    ax.set_xlabel("Load current from no-load to full-load")
    ax.set_ylabel("Terminal voltage (V)")
    ax.set_xticks([0.0, 1.0])
    ax.set_xticklabels(["No-load", "Full-load"])
    ax.set_title("Load regulation and voltage droop", fontsize=12, pad=10)
    ax.annotate(
        "",
        xy=(1.0, 11.35),
        xytext=(1.0, 12.0),
        arrowprops=dict(arrowstyle="<->", linewidth=1.4, color=PURPLE),
    )
    ax.text(0.73, 11.73, "Voltage droop", color=PURPLE, fontsize=10)

    save_svg(fig, output)
    return output


def generate_unit1_source_transformation() -> Path:
    output = UNIT1_IMAGE_DIR / "figure-1-13-source-transformation.svg"
    tex_body = r"""
\begin{circuitikz}[american]
\begin{scope}
\node[font=\bfseries] at (2.6,4.9) {Voltage-source form};
\draw
  (0,0) to[sV,l_=$\mathcal{E}$] (0,3.6)
  to[R,l=$R$] (3.0,3.6)
  -- (5.0,3.6)
  to[R,l=$R_L$] (5.0,0)
  -- (0,0);
\node at (2.5,-0.6) {$R$ stays the same};
\end{scope}

\begin{scope}[xshift=8.2cm]
\node[font=\bfseries] at (2.6,4.9) {Current-source form};
\draw
  (0,3.6) to[I,l=$I_s$] (0,0);
\draw
  (0,3.6) -- (2.2,3.6)
  to[R,l=$R$] (2.2,0)
  -- (0,0);
\draw
  (2.2,3.6) -- (5.0,3.6)
  to[R,l=$R_L$] (5.0,0)
  -- (2.2,0);
\node at (2.5,-0.6) {$I_s = \mathcal{E} / R$};
\node at (2.5,-1.2) {Same load current and voltage};
\end{scope}

\draw[-{Latex[length=3mm]}, thick] (6.1,1.8) -- (7.3,1.8);
\draw[-{Latex[length=3mm]}, thick] (7.3,1.45) -- (6.1,1.45);
\node[align=center] at (6.7,2.45) {Equivalent\\at the terminals};
\end{circuitikz}
"""
    render_circuitikz_svg(tex_body, output)
    return output


def generate_unit1_resistor_colour_code() -> Path:
    output = UNIT1_IMAGE_DIR / "figure-1-14-resistor-colour-code.svg"
    fig, ax = plt.subplots(figsize=(11.5, 3.8))
    setup_clean_axes(ax, (0.0, 12.0), (0.0, 4.2))

    ax.plot([0.8, 3.1], [2.1, 2.1], color=GRAY, linewidth=2.3)
    ax.plot([8.9, 11.2], [2.1, 2.1], color=GRAY, linewidth=2.3)
    body = patches.FancyBboxPatch(
        (3.1, 1.45),
        5.8,
        1.3,
        boxstyle="round,pad=0.02,rounding_size=0.35",
        facecolor="#e8c88f",
        edgecolor="#8a6338",
        linewidth=1.8,
    )
    ax.add_patch(body)

    band_x = [4.2, 5.15, 6.35, 7.75]
    band_specs = [
        ("Brown", "#7a4e21", "1st digit = 1"),
        ("Black", "#111111", "2nd digit = 0"),
        ("Red", "#c43d2b", r"Multiplier = $\times 10^2$"),
        ("Gold", "#d7b45e", r"Tolerance = $\pm 5\%$"),
    ]
    for x, (_, color, _) in zip(band_x, band_specs):
        ax.add_patch(patches.Rectangle((x, 1.45), 0.24, 1.3, facecolor=color, edgecolor="none"))

    label_y = 3.62
    for x, (name, color, label) in zip(band_x, band_specs):
        ax.annotate(
            "",
            xy=(x + 0.12, 2.78),
            xytext=(x + 0.12, label_y - 0.12),
            arrowprops=dict(arrowstyle="->", linewidth=1.3, color=color if name != "Gold" else "#8a6d1d"),
        )
        ax.text(
            x + 0.12,
            label_y,
            f"{name}\n{label}",
            ha="center",
            va="bottom",
            fontsize=10.5,
            color=color if name != "Gold" else "#8a6d1d",
            fontweight="bold" if name != "Black" else None,
        )

    ax.text(6.0, 0.62, "Example: Brown - Black - Red - Gold = 1 kΩ ±5%", ha="center", fontsize=11.5, color=GRAY)

    save_svg(fig, output)
    return output


def generate_unit3_circuits() -> Path:
    output = UNIT3_IMAGE_DIR / "figure-3-4a-pure-rlc-reference-circuits.svg"
    tex_body = r"""
\begin{circuitikz}[american]
\draw
  (0,0) node[below]{(a)} to[sV, l=$v_s(t)$] (0,3)
  to[R, l=$R$] (3,3) -- (3,0) -- (0,0);
\draw (1.5,-0.9) node{Pure resistor};

\draw
  (5,0) node[below]{(b)} to[sV, l=$v_s(t)$] (5,3)
  to[L, l=$L$] (8,3) -- (8,0) -- (5,0);
\draw (6.5,-0.9) node{Pure inductor};

\draw
  (10,0) node[below]{(c)} to[sV, l=$v_s(t)$] (10,3)
  to[C, l=$C$] (13,3) -- (13,0) -- (10,0);
\draw (11.5,-0.9) node{Pure capacitor};
\end{circuitikz}
"""
    render_circuitikz_svg(tex_body, output)
    return output


def generate_unit3_waveforms() -> Path:
    output = UNIT3_IMAGE_DIR / "figure-3-4b-pure-rlc-waveforms-and-phasors.svg"
    theta = np.linspace(0.0, 2.0 * np.pi, 1000)
    voltage = np.sin(theta)
    current_r = np.sin(theta)
    current_l = np.sin(theta - np.pi / 2.0)
    current_c = np.sin(theta + np.pi / 2.0)

    fig, axes = plt.subplots(2, 3, figsize=(13.5, 7.5), constrained_layout=True)
    waveform_axes = axes[0]
    phasor_axes = axes[1]

    configs = [
        ("Pure R", current_r, "In phase", 0.0),
        ("Pure L", current_l, "Current lags by 90°", -np.pi / 2.0),
        ("Pure C", current_c, "Current leads by 90°", np.pi / 2.0),
    ]

    for ax, (title, current, phase_text, phase) in zip(waveform_axes, configs):
        ax.plot(theta, voltage, label="v(t)", linewidth=2.2, color=PRIMARY)
        ax.plot(theta, current, label="i(t)", linewidth=2.2, color=ACCENT)
        style_axis(ax)
        ax.set_title(title, fontsize=12, pad=8)
        ax.set_xlim(0.0, 2.0 * np.pi)
        ax.set_ylim(-1.25, 1.25)
        ax.set_xticks([0, np.pi / 2, np.pi, 3 * np.pi / 2, 2 * np.pi])
        ax.set_xticklabels(["0", r"$\pi/2$", r"$\pi$", r"$3\pi/2$", r"$2\pi$"])
        ax.set_xlabel(r"Electrical angle $\omega t$")
        ax.set_ylabel("Normalized amplitude")
        ax.text(0.04, 0.9, phase_text, transform=ax.transAxes, fontsize=10)
        if title == "Pure L":
            ax.annotate(
                "",
                xy=(np.pi / 2, 1.0),
                xytext=(np.pi, 1.0),
                arrowprops=dict(arrowstyle="<->", color="0.35", lw=1.0),
            )
            ax.text(0.44, 0.82, r"$90^\circ$", transform=ax.transAxes, color="0.35")
        if title == "Pure C":
            ax.annotate(
                "",
                xy=(0.0, 1.0),
                xytext=(np.pi / 2, 1.0),
                arrowprops=dict(arrowstyle="<->", color="0.35", lw=1.0),
            )
            ax.text(0.23, 0.82, r"$90^\circ$", transform=ax.transAxes, color="0.35")

    waveform_axes[0].legend(loc="lower left", frameon=False)

    for ax, (title, _, _, phase) in zip(phasor_axes, configs):
        draw_phasor_axis(ax, f"{title} phasors")
        if phase == 0:
            add_phasor(ax, 0.0, "V, I", PRIMARY)
            ax.text(0.52, 0.14, r"$I$ in phase with $V$", fontsize=10, color="0.25")
        else:
            add_phasor(ax, 0.0, "V", PRIMARY)
            add_phasor(ax, phase, "I", ACCENT)
        if phase > 0:
            ax.text(0.5, 0.7, r"$I$ leads $V$", fontsize=10, color="0.25")
        elif phase < 0:
            ax.text(0.45, -0.7, r"$I$ lags $V$", fontsize=10, color="0.25")

    save_svg(fig, output)
    return output


def generate_unit1() -> list[Path]:
    return [
        generate_unit1_emf_vs_potential_difference(),
        generate_unit1_current_cross_section(),
        generate_unit1_meter_connections(),
        generate_unit1_component_panel(),
        generate_unit1_voltage_divider(),
        generate_unit1_capacitor_field(),
        generate_unit1_rc_curves(),
        generate_unit1_inductor_field(),
        generate_unit1_waveform_families(),
        generate_unit1_source_models(),
        generate_unit1_terminal_characteristic(),
        generate_unit1_load_regulation(),
        generate_unit1_source_transformation(),
        generate_unit1_resistor_colour_code(),
    ]


def generate_unit3() -> list[Path]:
    return [generate_unit3_circuits(), generate_unit3_waveforms()]


def generate_circuits() -> Path:
    return generate_unit3_circuits()


def generate_waveforms() -> Path:
    return generate_unit3_waveforms()


def generate_all() -> list[Path]:
    return [*generate_unit1(), *generate_unit3()]


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Generate SVG figures for the Fundamentals of Electrical and Electronics Engineering textbook."
    )
    parser.add_argument(
        "--target",
        choices=["all", "unit1", "unit3", "circuits", "waveforms"],
        default="all",
        help="Which FEEE figure set to generate.",
    )
    args = parser.parse_args()

    if args.target in {"all", "unit1", "unit3", "circuits"}:
        if shutil.which("pdflatex") is None or shutil.which("inkscape") is None:
            raise SystemExit("This script requires both pdflatex and inkscape to render the circuit SVGs.")

    if args.target == "all":
        outputs = generate_all()
    elif args.target == "unit1":
        outputs = generate_unit1()
    elif args.target == "unit3":
        outputs = generate_unit3()
    elif args.target == "circuits":
        outputs = [generate_unit3_circuits()]
    else:
        outputs = [generate_unit3_waveforms()]

    for output in outputs:
        print(output.relative_to(ROOT))


if __name__ == "__main__":
    main()
