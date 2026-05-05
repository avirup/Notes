#!/usr/bin/env python3

from __future__ import annotations

import argparse
import importlib.util
import os
import re
import shutil
import subprocess
import tempfile
from pathlib import Path
from types import ModuleType

os.environ.setdefault("MPLCONFIGDIR", str(Path(tempfile.gettempdir()) / "matplotlib"))

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import numpy as np

plt.rcParams.update(
    {
        "figure.facecolor": "white",
        "axes.facecolor": "white",
        "savefig.facecolor": "white",
        "font.family": "DejaVu Serif",
        "axes.titlesize": 13,
        "axes.labelsize": 11,
        "xtick.labelsize": 10,
        "ytick.labelsize": 10,
    }
)


ROOT = Path(__file__).resolve().parent.parent
FEEE_SCRIPT = (
    ROOT
    / "Fundamentals of Electrical and Electronics Engineering"
    / "ImagenScript"
    / "generate_feee_figures.py"
)
POWER_IMAGE_DIR = ROOT / "Power Electronics" / "images" / "module-4" / "chapter-1"

PRIMARY = "#1f3a5f"
ACCENT = "#c25b20"
GREEN = "#1e6f5c"
RED = "#b23a48"
PURPLE = "#6d597a"
GRAY = "#5f6b7a"
LIGHT_BLUE = "#d9eaf7"
LIGHT_ORANGE = "#f7ead9"
LIGHT_GREEN = "#dff1ea"
LIGHT_RED = "#f7d8dc"


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
    ax.spines["left"].set_color("#4b5563")
    ax.spines["bottom"].set_color("#4b5563")
    ax.spines["left"].set_linewidth(0.9)
    ax.spines["bottom"].set_linewidth(0.9)
    ax.grid(True, color="#d7dce2", alpha=0.45, linewidth=0.6)
    ax.set_axisbelow(True)


def save_svg(fig: plt.Figure, output_svg: Path) -> None:
    ensure_parent(output_svg)
    fig.savefig(output_svg, format="svg", bbox_inches="tight", facecolor="white")
    plt.close(fig)


def load_feee_generator() -> ModuleType:
    if not FEEE_SCRIPT.exists():
        raise SystemExit(f"Missing FEEE figure generator: {FEEE_SCRIPT}")

    spec = importlib.util.spec_from_file_location("feee_figure_generator", FEEE_SCRIPT)
    if spec is None or spec.loader is None:
        raise SystemExit(f"Unable to load FEEE figure generator: {FEEE_SCRIPT}")

    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def triangle_wave(time: np.ndarray, period: float, amplitude: float = 1.0, offset: float = 0.0) -> np.ndarray:
    phase = (time % period) / period
    tri = 1.0 - np.abs(2.0 * phase - 1.0)
    return offset + amplitude * tri


def smooth_pulse_train(time: np.ndarray, period: float, duty: float, high: float, low: float = 0.0) -> np.ndarray:
    phase = (time % period) / period
    return np.where(phase < duty, high, low)


def plot_conceptual_waveforms(
    output_svg: Path,
    title: str,
    vo: np.ndarray,
    io: np.ndarray,
    t: np.ndarray,
    *,
    vo_label: str = r"$v_o$",
    io_label: str = r"$i_o$",
    notes: str | None = None,
    bands: list[tuple[float, float, str, float]] | None = None,
) -> Path:
    fig, axes = plt.subplots(2, 1, figsize=(11.2, 5.8), sharex=True, constrained_layout=True)
    colors = [PRIMARY, ACCENT]
    labels = [
        (axes[0], vo, colors[0], vo_label),
        (axes[1], io, colors[1], io_label),
    ]

    for ax, values, color, ylabel in labels:
        ax.plot(t, values, color=color, linewidth=2.2)
        ax.axhline(0.0, color="#6b7280", linewidth=0.9)
        style_axis(ax)
        ax.set_ylabel(ylabel)

    if bands:
        for start, end, color, alpha in bands:
            for ax in axes:
                ax.axvspan(start, end, color=color, alpha=alpha)

    axes[0].set_title(title, fontsize=13, loc="left", pad=8)
    axes[1].set_xlabel("Normalized time")

    if notes:
        axes[0].text(
            0.99,
            1.02,
            notes,
            transform=axes[0].transAxes,
            ha="right",
            va="bottom",
            fontsize=10,
            color=GRAY,
        )

    save_svg(fig, output_svg)
    return output_svg


def simulate_step_down_chopper(
    vs: float = 48.0,
    resistance: float = 2.5,
    inductance: float = 8e-3,
    duty: float = 0.6,
    switching_frequency: float = 1_000.0,
    periods: int = 6,
    steps_per_period: int = 1200,
) -> tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    period = 1.0 / switching_frequency
    dt = period / steps_per_period
    total_steps = periods * steps_per_period

    time = np.linspace(0.0, periods * period, total_steps, endpoint=False)
    gate = np.zeros_like(time)
    output_voltage = np.zeros_like(time)
    current = np.zeros_like(time)

    i = 0.0
    for idx, t in enumerate(time):
        position = t % period
        is_on = position < duty * period
        gate[idx] = 1.0 if is_on else 0.0
        output_voltage[idx] = vs if is_on else 0.0
        di_dt = (vs - resistance * i) / inductance if is_on else (-resistance * i) / inductance
        i = max(0.0, i + di_dt * dt)
        current[idx] = i

    return time, gate, output_voltage, current


def generate_power_circuit() -> Path:
    output = POWER_IMAGE_DIR / "figure-13-1a-step-down-chopper-rl-circuit.svg"
    tex_body = r"""
\begin{circuitikz}[american]
\draw
  (0,0) to[battery1, l=$V_s$] (0,4)
  to[short] (1.6,4)
  node[draw, minimum width=0.95cm, minimum height=0.55cm]{S}
  (2.6,4) to[L, l=$L$] (5.2,4)
  to[R, l=$R$] (5.2,0)
  -- (0,0);
\draw
  (2.6,4) -- (2.6,5)
  node[above]{Switch node $v_o$};
\draw
  (5.2,4) -- (6.7,4)
  to[D*, l_=$D_F$] (6.7,0)
  -- (5.2,0);
\draw[->] (3.4,3.25) -- (4.8,3.25);
\draw (4.1,3.45) node[above]{Load current $i_o$};
\draw[->] (6.2,1.1) arc[start angle=-25,end angle=-305,radius=0.9];
\draw (7.6,2.1) node[right]{Freewheel path};
\end{circuitikz}
"""
    render_circuitikz_svg(tex_body, output)
    return output


def generate_power_waveforms() -> Path:
    output = POWER_IMAGE_DIR / "figure-13-1b-step-down-chopper-rl-waveforms.svg"
    time, gate, output_voltage, current = simulate_step_down_chopper(periods=24)

    period = 1.0 / 1000.0
    ton = 0.6 * period
    window_periods = 4
    start_time = time[-1] - window_periods * period
    mask = time >= start_time

    time = time[mask] - start_time
    gate = gate[mask]
    output_voltage = output_voltage[mask]
    current = current[mask]

    t_ms = time * 1000.0
    gate_y = 1.15 * gate

    fig, axes = plt.subplots(3, 1, figsize=(11.5, 7.5), sharex=True, constrained_layout=True)
    labels = [
        ("Gate command", gate_y, PRIMARY, "Gate"),
        (r"Output voltage $v_o$", output_voltage, GREEN, r"$v_o$ (V)"),
        (r"Load current $i_o$", current, ACCENT, r"$i_o$ (A)"),
    ]

    for ax, (title, values, color, ylabel) in zip(axes, labels):
        ax.plot(t_ms, values, color=color, linewidth=2.1)
        style_axis(ax)
        ax.set_title(title, fontsize=12, loc="left", pad=6)
        ax.set_ylabel(ylabel)

    axes[-1].set_xlabel("Time (ms)")
    axes[0].set_ylim(-0.1, 1.35)
    axes[1].set_ylim(-2.0, 52.0)

    first_period_end = period * 1000.0
    ton_ms = ton * 1000.0
    toff_ms = (period - ton) * 1000.0

    for ax in axes:
        ax.axvspan(0.0, ton_ms, color=LIGHT_BLUE, alpha=0.35)
        ax.axvspan(ton_ms, first_period_end, color=LIGHT_ORANGE, alpha=0.35)
        ax.axvline(first_period_end, color="#6b7280", linewidth=0.9, linestyle="--")

    axes[0].annotate(r"$T_{ON}$", xy=(ton_ms / 2.0, 1.22), ha="center", va="bottom", fontsize=10)
    axes[0].annotate(
        r"$T_{OFF}$",
        xy=(ton_ms + toff_ms / 2.0, 1.22),
        ha="center",
        va="bottom",
        fontsize=10,
    )
    axes[0].annotate(
        r"$T = 1.0\ \mathrm{ms},\ f_s = 1\ \mathrm{kHz},\ D = 0.6$",
        xy=(3.15, 1.22),
        ha="left",
        va="bottom",
        fontsize=10,
    )

    save_svg(fig, output)
    return output


def generate_duty_cycle_figure() -> Path:
    output = POWER_IMAGE_DIR / "figure-13-1c-duty-cycle-and-average-voltage.svg"
    fig, axes = plt.subplots(3, 1, figsize=(10.4, 6.2), sharex=True, constrained_layout=True)

    duties = [0.25, 0.5, 0.8]
    titles = [r"$D = 0.25$", r"$D = 0.50$", r"$D = 0.80$"]
    t = np.linspace(0.0, 4.0, 1600, endpoint=False)

    for ax, duty, title in zip(axes, duties, titles):
        vo = smooth_pulse_train(t, 1.0, duty=duty, high=1.0)
        ax.plot(t, vo, color=PRIMARY, linewidth=2.2)
        ax.axhline(duty, color=RED, linewidth=1.4, linestyle="--")
        style_axis(ax)
        ax.set_ylim(-0.08, 1.15)
        ax.set_ylabel(r"$v_o/V_s$")
        ax.set_title(title + rf", average = {duty:.2f}$V_s$", loc="left", fontsize=12, pad=6)
        ax.text(3.98, duty + 0.04, r"$V_{o,\mathrm{avg}}$", color=RED, ha="right", va="bottom", fontsize=10)

    axes[-1].set_xlabel("Normalized time")
    save_svg(fig, output)
    return output


def generate_load_comparison() -> Path:
    output = POWER_IMAGE_DIR / "figure-13-1d-resistive-vs-rl-load-waveforms.svg"
    time, _, vo_rl, io_rl = simulate_step_down_chopper(periods=24)
    period = 1.0 / 1000.0
    start_time = time[-1] - 4.0 * period
    mask = time >= start_time
    t_ms = (time[mask] - start_time) * 1000.0
    vo_rl = vo_rl[mask]
    io_rl = io_rl[mask]
    io_r = vo_rl / 4.0

    fig, axes = plt.subplots(2, 1, figsize=(11.0, 6.2), sharex=True, constrained_layout=True)

    axes[0].plot(t_ms, io_r, color=RED, linewidth=2.0, label="Resistive load current")
    axes[0].plot(t_ms, io_rl, color=PRIMARY, linewidth=2.0, label="R-L load current")
    style_axis(axes[0])
    axes[0].set_title("Load-current comparison for the same chopped output voltage", loc="left", fontsize=12, pad=6)
    axes[0].set_ylabel(r"$i_o$ (A)")
    axes[0].legend(frameon=False, loc="upper right")

    axes[1].plot(t_ms, vo_rl, color=PRIMARY, linewidth=2.0)
    style_axis(axes[1])
    axes[1].set_ylabel(r"$v_o$ (V)")
    axes[1].set_xlabel("Time (ms)")
    axes[1].set_title("Applied switch-node voltage", loc="left", fontsize=12, pad=6)

    save_svg(fig, output)
    return output


def generate_freewheel_paths() -> Path:
    output = POWER_IMAGE_DIR / "figure-13-1e-on-and-freewheel-current-paths.svg"
    tex_body = r"""
\begin{circuitikz}[american]
\begin{scope}
\draw
  (0,0) to[battery1, l=$V_s$] (0,4)
  to[short] (1.5,4)
  node[draw, fill=black!5, minimum width=0.95cm, minimum height=0.55cm]{S ON}
  (2.5,4) to[L, l=$L$] (4.9,4)
  to[R, l=$R$] (4.9,0)
  -- (0,0);
\draw
  (4.9,4) -- (6.4,4)
  to[D*, l_=$D_F$] (6.4,0)
  -- (4.9,0);
\draw[->, thick] (1.2,3.2) -- (4.2,3.2);
\draw (2.8,4.85) node[above]{Switch ON: source powers the load};
\end{scope}

\begin{scope}[xshift=8.6cm]
\draw
  (0,0) to[battery1, l=$V_s$] (0,4)
  to[short] (1.5,4)
  node[draw, fill=black!5, minimum width=1.05cm, minimum height=0.55cm]{S OFF}
  (2.6,4) to[L, l=$L$] (5.0,4)
  to[R, l=$R$] (5.0,0)
  -- (0,0);
\draw
  (5.0,4) -- (6.5,4)
  to[D*, l_=$D_F$] (6.5,0)
  -- (5.0,0);
\draw[->, thick] (5.9,1.2) arc[start angle=-20,end angle=-300,radius=0.95];
\draw (3.0,4.85) node[above]{Switch OFF: inductor current freewheels};
\end{scope}
\end{circuitikz}
"""
    render_circuitikz_svg(tex_body, output)
    return output


def generate_control_strategy_comparison() -> Path:
    output = POWER_IMAGE_DIR / "figure-13-2-control-strategy-comparison.svg"
    fig, axes = plt.subplots(3, 1, figsize=(11.6, 8.2), sharex=False, constrained_layout=True)

    t_cf = np.array([0.0, 0.55, 2.0, 2.95, 4.0, 5.45, 6.0])
    y_cf = np.array([1, 0, 1, 0, 1, 0, 0])
    axes[0].step(t_cf, y_cf, where="post", color=PRIMARY, linewidth=2.1)
    style_axis(axes[0])
    axes[0].set_ylim(-0.1, 1.2)
    axes[0].set_ylabel("Gate / $v_o$")
    axes[0].set_title("Constant-frequency TRC: equal period, changing pulse width", loc="left", fontsize=12, pad=6)
    for x in [0.0, 2.0, 4.0, 6.0]:
        axes[0].axvline(x, color="#6b7280", linewidth=0.8, linestyle="--")
    axes[0].annotate(r"$T$", xy=(1.0, 1.06), ha="center", fontsize=10)
    axes[0].annotate(r"$T$", xy=(3.0, 1.06), ha="center", fontsize=10)
    axes[0].annotate(r"$T_{ON}$ increases", xy=(3.3, 0.82), ha="left", fontsize=10, color=GRAY)

    t_var = np.array([0.0, 0.8, 1.8, 2.6, 4.2, 5.0, 6.0])
    y_var = np.array([1, 0, 1, 0, 1, 0, 1])
    axes[1].step(t_var, y_var, where="post", color=GREEN, linewidth=2.1)
    style_axis(axes[1])
    axes[1].set_ylim(-0.1, 1.2)
    axes[1].set_ylabel("Gate / $v_o$")
    axes[1].set_title("Variable-frequency TRC: pulse timing changes with operating point", loc="left", fontsize=12, pad=6)
    axes[1].annotate(r"$f_s$ changes", xy=(4.25, 0.84), ha="left", fontsize=10, color=GRAY)

    t3 = np.linspace(0.0, 6.0, 1200, endpoint=False)
    i_band = 20.0 + 2.0 * triangle_wave(t3, period=1.5, amplitude=1.0, offset=0.0)
    i_band[300:520] = 18.0 + 4.0 * triangle_wave(t3[300:520], period=1.1, amplitude=1.0, offset=0.0)
    i_band[520:850] = 18.0 + 4.0 * triangle_wave(t3[520:850], period=1.7, amplitude=1.0, offset=0.0)
    axes[2].plot(t3, i_band, color=ACCENT, linewidth=2.1)
    axes[2].axhline(22.0, color=RED, linewidth=1.3, linestyle="--")
    axes[2].axhline(18.0, color=PURPLE, linewidth=1.3, linestyle="--")
    style_axis(axes[2])
    axes[2].set_ylabel(r"$i_o$ (A)")
    axes[2].set_xlabel("Normalized time")
    axes[2].set_title("Current-limit control: current oscillates between $I_L$ and $I_U$", loc="left", fontsize=12, pad=6)
    axes[2].text(5.95, 22.25, r"$I_U$", ha="right", va="bottom", fontsize=10, color=RED)
    axes[2].text(5.95, 17.75, r"$I_L$", ha="right", va="top", fontsize=10, color=PURPLE)

    save_svg(fig, output)
    return output


def generate_quadrant_plot() -> Path:
    output = POWER_IMAGE_DIR / "figure-13-3-quadrant-classification-of-choppers.svg"
    fig, ax = plt.subplots(figsize=(8.0, 7.2), constrained_layout=True)
    ax.set_facecolor("white")
    ax.axhline(0.0, color="#111827", linewidth=1.0)
    ax.axvline(0.0, color="#111827", linewidth=1.0)
    ax.set_xlim(-1.2, 1.2)
    ax.set_ylim(-1.2, 1.2)
    ax.set_xlabel(r"Output voltage $V_o$")
    ax.set_ylabel(r"Output current $I_o$")
    ax.set_title("Quadrant classification of classical DC choppers", loc="left", fontsize=13, pad=8)
    ax.grid(True, color="#d7dce2", alpha=0.45, linewidth=0.6)

    ax.text(0.55, 0.55, "Quadrant I", fontsize=11, color=GREEN, fontweight="bold")
    ax.text(-0.95, 0.55, "Quadrant II", fontsize=11, color=RED, fontweight="bold")
    ax.text(-0.95, -0.82, "Quadrant III", fontsize=11, color=PURPLE, fontweight="bold")
    ax.text(0.52, -0.82, "Quadrant IV", fontsize=11, color=ACCENT, fontweight="bold")

    ax.text(0.62, 0.22, "Type A", fontsize=12, color=GREEN)
    ax.text(-0.86, 0.22, "Type B", fontsize=12, color=RED)
    ax.text(-0.1, 0.95, "Type C", fontsize=12, color=PRIMARY)
    ax.text(0.82, -0.18, "Type D", fontsize=12, color=ACCENT)
    ax.text(-0.06, -1.06, "Type E", fontsize=12, color=PURPLE)

    ax.add_patch(plt.Circle((0.55, 0.45), 0.22, fill=True, linewidth=1.7, color=GREEN, alpha=0.10))
    ax.add_patch(plt.Circle((-0.55, 0.45), 0.22, fill=True, linewidth=1.7, color=RED, alpha=0.10))
    ax.add_patch(plt.Rectangle((0.02, 0.05), 0.95, 0.95, fill=False, linewidth=1.8, color=PRIMARY))
    ax.add_patch(plt.Rectangle((0.05, -0.95), 0.95, 0.95, fill=False, linewidth=1.8, color=ACCENT))
    ax.add_patch(plt.Rectangle((-1.0, -1.0), 2.0, 2.0, fill=False, linewidth=1.8, color=PURPLE, linestyle="--"))

    ax.annotate("Motoring", xy=(0.7, 0.7), xytext=(0.82, 1.02), arrowprops=dict(arrowstyle="->", color=GRAY))
    ax.annotate("Regeneration", xy=(-0.72, 0.68), xytext=(-1.14, 1.02), arrowprops=dict(arrowstyle="->", color=GRAY))
    ax.annotate("Voltage reversal", xy=(0.82, -0.62), xytext=(0.35, -1.08), arrowprops=dict(arrowstyle="->", color=GRAY))
    ax.annotate("Four-quadrant operation", xy=(-0.7, -0.7), xytext=(-1.12, -1.12), arrowprops=dict(arrowstyle="->", color=GRAY))

    save_svg(fig, output)
    return output


def generate_type_a_circuit() -> Path:
    output = POWER_IMAGE_DIR / "figure-13-4-type-a-chopper-circuit.svg"
    tex_body = r"""
\begin{circuitikz}[american]
\draw
  (0,0) to[battery1, l=$V_s$] (0,4)
  to[short] (1.6,4)
  node[draw, minimum width=0.95cm, minimum height=0.55cm]{S}
  (2.6,4) to[L, l=$L$] (5.2,4)
  to[R, l=$R$] (5.2,0)
  -- (0,0);
\draw
  (5.2,4) -- (6.7,4)
  to[D*, l_=$D_F$] (6.7,0)
  -- (5.2,0);
\draw[->] (3.4,3.2) -- (4.8,3.2);
\draw (4.1,3.45) node[above]{$i_o > 0$};
\draw (2.9,4.75) node[above]{Type A: Quadrant-I step-down chopper};
\end{circuitikz}
"""
    render_circuitikz_svg(tex_body, output)
    return output


def generate_type_b_circuit() -> Path:
    output = POWER_IMAGE_DIR / "figure-13-6-type-b-chopper-circuit.svg"
    tex_body = r"""
\begin{circuitikz}[american]
\draw
  (0,0) to[battery1, l=$V_s$] (0,4)
  -- (2.0,4)
  to[D*, l=$D$] (4.2,4)
  -- (6.0,4)
  to[L, l=$L$] (6.0,2.3)
  to[battery1, l_=$E$] (6.0,0)
  -- (0,0);
\draw
  (4.2,4) -- (4.2,0)
  node[midway, draw, minimum width=0.95cm, minimum height=0.55cm]{S};
\draw[->] (5.5,1.0) -- (5.5,2.5);
\draw (5.8,1.75) node[right]{$i_o < 0$ by sign convention};
\draw (3.0,4.75) node[above]{Type B: regenerative chopper};
\end{circuitikz}
"""
    render_circuitikz_svg(tex_body, output)
    return output


def generate_type_c_circuit() -> Path:
    output = POWER_IMAGE_DIR / "figure-13-8-type-c-chopper-circuit.svg"
    tex_body = r"""
\begin{circuitikz}[american]
\draw
  (0,0) to[battery1, l=$V_s$] (0,5)
  -- (2.0,5)
  -- (7.0,5);
\draw
  (0,0) -- (7.0,0);
\draw
  (4.8,5) to[L, l=$L$] (4.8,3.0)
  to[battery1, l_=$E$] (4.8,0);
\draw
  (2.0,5) node[draw, minimum width=0.95cm, minimum height=0.55cm]{S$_1$}
  (2.95,5) -- (4.8,5);
\draw
  (3.4,5) to[D*, l=$D_2$] (3.4,3.0);
\draw
  (2.0,0) node[draw, minimum width=0.95cm, minimum height=0.55cm]{S$_2$}
  (2.95,0) -- (4.8,0);
\draw
  (3.4,2.0) to[D*, l_=$D_1$] (3.4,0);
\draw (3.35,5.75) node[above]{Type C: Type-A and Type-B functions combined};
\end{circuitikz}
"""
    render_circuitikz_svg(tex_body, output)
    return output


def generate_type_d_circuit() -> Path:
    output = POWER_IMAGE_DIR / "figure-13-10-type-d-chopper-circuit.svg"
    tex_body = r"""
\begin{circuitikz}[american]
\draw
  (0,0) to[battery1, l=$V_s$] (0,5)
  -- (8,5);
\draw
  (0,0) -- (8,0);
\draw
  (2.0,5) -- (2.0,3.8) node[draw, minimum width=0.95cm, minimum height=0.55cm]{S$_1$} (2.0,3.2) -- (2.0,0);
\draw
  (6.0,5) -- (6.0,3.8) node[draw, minimum width=0.95cm, minimum height=0.55cm]{S$_2$} (6.0,3.2) -- (6.0,0);
\draw
  (2.0,3.25) to[D*, l_=$D_1$] (2.0,1.1);
\draw
  (6.0,1.1) to[D*, l=$D_2$] (6.0,3.25);
\draw
  (2.0,2.2) to[L, l=$L$] (6.0,2.2)
  node[midway, above=7pt]{Load, $i_o > 0$};
\draw (4.0,5.75) node[above]{Type D: reversible output voltage with positive current};
\end{circuitikz}
"""
    render_circuitikz_svg(tex_body, output)
    return output


def generate_type_e_circuit() -> Path:
    output = POWER_IMAGE_DIR / "figure-13-12-type-e-chopper-circuit.svg"
    tex_body = r"""
\begin{circuitikz}[american]
\draw
  (0,0) to[battery1, l=$V_s$] (0,6)
  -- (9,6);
\draw
  (0,0) -- (9,0);
\draw
  (2.0,6) -- (2.0,4.9) node[draw, minimum width=0.95cm, minimum height=0.55cm]{S$_1$} (2.0,4.3) -- (2.0,0);
\draw
  (7.0,6) -- (7.0,4.9) node[draw, minimum width=0.95cm, minimum height=0.55cm]{S$_2$} (7.0,4.3) -- (7.0,0);
\draw
  (2.0,1.7) node[draw, minimum width=0.95cm, minimum height=0.55cm]{S$_3$};
\draw
  (7.0,1.7) node[draw, minimum width=0.95cm, minimum height=0.55cm]{S$_4$};
\draw
  (2.0,4.35) to[D*, l_=$D_1$] (2.0,2.3);
\draw
  (2.0,1.1) to[D*, l_=$D_3$] (2.0,0.2);
\draw
  (7.0,2.3) to[D*, l=$D_2$] (7.0,4.35);
\draw
  (7.0,0.2) to[D*, l=$D_4$] (7.0,1.1);
\draw
  (2.0,3.0) -- (3.5,3.0)
  to[L, l=$L$] (5.5,3.0)
  -- (7.0,3.0);
\draw (4.5,3.4) node[above]{Load};
\draw (4.5,6.75) node[above]{Type E: four-quadrant H-bridge chopper};
\end{circuitikz}
"""
    render_circuitikz_svg(tex_body, output)
    return output


def generate_type_a_waveforms() -> Path:
    output = POWER_IMAGE_DIR / "figure-13-5-type-a-chopper-waveforms.svg"
    t = np.linspace(0.0, 6.0, 1600, endpoint=False)
    vo = smooth_pulse_train(t, period=1.0, duty=0.6, high=1.0)
    io = 0.45 + 0.28 * triangle_wave(t, period=1.0)
    return plot_conceptual_waveforms(
        output,
        "Type A waveforms: positive output voltage and positive output current",
        vo,
        io,
        t,
        notes="Quadrant I operation",
        bands=[(0.0, 0.6, LIGHT_BLUE, 0.25)],
    )


def generate_type_b_waveforms() -> Path:
    output = POWER_IMAGE_DIR / "figure-13-7-type-b-chopper-waveforms.svg"
    t = np.linspace(0.0, 6.0, 1600, endpoint=False)
    vo = 0.25 + 0.75 * smooth_pulse_train(t, period=1.2, duty=0.42, high=1.0)
    io = -(0.35 + 0.3 * triangle_wave(t, period=1.2))
    return plot_conceptual_waveforms(
        output,
        "Type B waveforms: positive output voltage with negative output current",
        vo,
        io,
        t,
        notes="Quadrant II regenerative operation",
    )


def generate_type_c_waveforms() -> Path:
    output = POWER_IMAGE_DIR / "figure-13-9-type-c-chopper-waveforms.svg"
    t = np.linspace(0.0, 6.0, 1800, endpoint=False)
    vo = 0.2 + 0.8 * smooth_pulse_train(t, period=1.0, duty=0.58, high=1.0)
    io = np.where(
        t < 3.0,
        0.3 + 0.28 * triangle_wave(t, period=1.0),
        -(0.25 + 0.26 * triangle_wave(t - 3.0, period=1.0)),
    )
    return plot_conceptual_waveforms(
        output,
        "Type C waveforms: positive voltage with current reversal",
        vo,
        io,
        t,
        notes="Quadrants I and II",
        bands=[(0.0, 3.0, LIGHT_GREEN, 0.18), (3.0, 6.0, LIGHT_RED, 0.18)],
    )


def generate_type_d_waveforms() -> Path:
    output = POWER_IMAGE_DIR / "figure-13-11-type-d-chopper-waveforms.svg"
    t = np.linspace(0.0, 6.0, 1800, endpoint=False)
    vo = np.where(
        t < 3.0,
        smooth_pulse_train(t, period=1.0, duty=0.55, high=1.0),
        -smooth_pulse_train(t - 3.0, period=1.0, duty=0.55, high=1.0),
    )
    io = 0.35 + 0.24 * triangle_wave(t, period=1.0)
    return plot_conceptual_waveforms(
        output,
        "Type D waveforms: output-voltage reversal while current remains positive",
        vo,
        io,
        t,
        notes="Quadrants I and IV",
        bands=[(0.0, 3.0, LIGHT_GREEN, 0.18), (3.0, 6.0, LIGHT_ORANGE, 0.22)],
    )


def generate_type_e_waveforms() -> Path:
    output = POWER_IMAGE_DIR / "figure-13-13-type-e-chopper-waveforms.svg"
    t = np.linspace(0.0, 8.0, 2400, endpoint=False)
    vo = np.piecewise(
        t,
        [t < 2.0, (t >= 2.0) & (t < 4.0), (t >= 4.0) & (t < 6.0), t >= 6.0],
        [
            lambda x: smooth_pulse_train(x, period=1.0, duty=0.55, high=1.0),
            lambda x: 0.3 + 0.7 * smooth_pulse_train(x - 2.0, period=1.0, duty=0.45, high=1.0),
            lambda x: -smooth_pulse_train(x - 4.0, period=1.0, duty=0.55, high=1.0),
            lambda x: -(0.3 + 0.7 * smooth_pulse_train(x - 6.0, period=1.0, duty=0.45, high=1.0)),
        ],
    )
    io = np.piecewise(
        t,
        [t < 2.0, (t >= 2.0) & (t < 4.0), (t >= 4.0) & (t < 6.0), t >= 6.0],
        [
            lambda x: 0.35 + 0.22 * triangle_wave(x, period=1.0),
            lambda x: -(0.28 + 0.2 * triangle_wave(x - 2.0, period=1.0)),
            lambda x: -(0.32 + 0.2 * triangle_wave(x - 4.0, period=1.0)),
            lambda x: 0.32 + 0.2 * triangle_wave(x - 6.0, period=1.0),
        ],
    )
    return plot_conceptual_waveforms(
        output,
        "Type E waveforms: both output voltage and current reverse",
        vo,
        io,
        t,
        notes="Four-quadrant operation",
        bands=[
            (0.0, 2.0, LIGHT_GREEN, 0.16),
            (2.0, 4.0, LIGHT_BLUE, 0.16),
            (4.0, 6.0, LIGHT_RED, 0.16),
            (6.0, 8.0, LIGHT_ORANGE, 0.18),
        ],
    )


def generate_power_figures() -> list[Path]:
    return [
        generate_power_circuit(),
        generate_power_waveforms(),
        generate_duty_cycle_figure(),
        generate_load_comparison(),
        generate_freewheel_paths(),
        generate_control_strategy_comparison(),
        generate_quadrant_plot(),
        generate_type_a_circuit(),
        generate_type_a_waveforms(),
        generate_type_b_circuit(),
        generate_type_b_waveforms(),
        generate_type_c_circuit(),
        generate_type_c_waveforms(),
        generate_type_d_circuit(),
        generate_type_d_waveforms(),
        generate_type_e_circuit(),
        generate_type_e_waveforms(),
    ]


def generate_all() -> list[Path]:
    feee_module = load_feee_generator()
    return [*feee_module.generate_all(), *generate_power_figures()]


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Generate circuit schematics and simulation-backed SVG figures for the notes."
    )
    parser.add_argument(
        "--target",
        choices=["all", "feee", "power"],
        default="all",
        help="Which book figure set to generate.",
    )
    args = parser.parse_args()

    if shutil.which("pdflatex") is None or shutil.which("inkscape") is None:
        raise SystemExit("This script requires both pdflatex and inkscape to be installed.")

    if args.target == "all":
        outputs = generate_all()
    elif args.target == "feee":
        outputs = load_feee_generator().generate_all()
    else:
        outputs = generate_power_figures()

    for output in outputs:
        print(output.relative_to(ROOT))


if __name__ == "__main__":
    main()
