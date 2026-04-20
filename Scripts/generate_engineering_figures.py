#!/usr/bin/env python3

from __future__ import annotations

import argparse
import math
import os
import shutil
import subprocess
import tempfile
from pathlib import Path

os.environ.setdefault("MPLCONFIGDIR", str(Path(tempfile.gettempdir()) / "matplotlib"))

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import numpy as np


ROOT = Path(__file__).resolve().parent.parent
FEEE_IMAGE_DIR = (
    ROOT
    / "Fundamentals of Electrical and Electronics Engineering"
    / "Textbook"
    / "images"
    / "unit-3"
)
POWER_IMAGE_DIR = ROOT / "Power Electronics" / "images" / "module-4" / "chapter-1"


def ensure_parent(path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)


def run_command(args: list[str], cwd: Path | None = None) -> None:
    subprocess.run(args, cwd=cwd, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)


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


def style_axis(ax: plt.Axes) -> None:
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.grid(True, alpha=0.2, linewidth=0.6)
    ax.set_axisbelow(True)


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


def generate_feee_circuits() -> Path:
    output = FEEE_IMAGE_DIR / "figure-3-4a-pure-rlc-reference-circuits.svg"
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


def generate_feee_waveforms() -> Path:
    output = FEEE_IMAGE_DIR / "figure-3-4b-pure-rlc-waveforms-and-phasors.svg"
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
        ax.plot(theta, voltage, label="v(t)", linewidth=2.2, color="#1f3a5f")
        ax.plot(theta, current, label="i(t)", linewidth=2.2, color="#c25b20")
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
            add_phasor(ax, 0.0, "V, I", "#1f3a5f")
            ax.text(0.52, 0.14, r"$I$ in phase with $V$", fontsize=10, color="0.25")
        else:
            add_phasor(ax, 0.0, "V", "#1f3a5f")
            add_phasor(ax, phase, "I", "#c25b20")
        if phase > 0:
            ax.text(0.5, 0.7, r"$I$ leads $V$", fontsize=10, color="0.25")
        elif phase < 0:
            ax.text(0.45, -0.7, r"$I$ lags $V$", fontsize=10, color="0.25")

    save_svg(fig, output)
    return output


def generate_power_circuit() -> Path:
    output = POWER_IMAGE_DIR / "figure-13-1a-step-down-chopper-rl-circuit.svg"
    tex_body = r"""
\begin{circuitikz}[american]
\draw
  (0,0) to[battery1, l=$V_s$] (0,4)
  to[spst, l=$S$] (3,4)
  to[L, l=$L$] (6,4)
  to[R, l=$R$] (6,0)
  -- (0,0);
\draw
  (3,4) -- (3,5)
  node[above]{Switch node $v_o$};
\draw
  (6,4) to[short] (8,4)
  to[D*, l_=$D_F$] (8,0)
  -- (6,0);
\draw
  (6,2) node[right]{Load current $i_o$};
\draw[->] (4.1,3.2) -- (5.5,3.2);
\draw (4.8,3.45) node[above]{ON current path};
\draw[->] (7.6,1.0) arc[start angle=-20,end angle=-300,radius=0.95];
\draw (8.9,2.1) node[right]{Freewheel path};
\end{circuitikz}
"""
    render_circuitikz_svg(tex_body, output)
    return output


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
        ("Gate command", gate_y, "#2c5d8a", "Gate"),
        (r"Output voltage $v_o$", output_voltage, "#1e6f5c", r"$v_o$ (V)"),
        (r"Load current $i_o$", current, "#c25b20", r"$i_o$ (A)"),
    ]

    for ax, (title, values, color, ylabel) in zip(axes, labels):
        ax.plot(t_ms, values, color=color, linewidth=2.0)
        style_axis(ax)
        ax.set_title(title, fontsize=12, loc="left", pad=6)
        ax.set_ylabel(ylabel)

    axes[-1].set_xlabel("Time (ms)")
    axes[0].set_ylim(-0.1, 1.35)
    axes[1].set_ylim(-2.0, 52.0)

    first_period_start = 0.0
    first_period_end = period * 1000.0
    ton_ms = ton * 1000.0
    toff_ms = (period - ton) * 1000.0

    for ax in axes:
        ax.axvspan(first_period_start, ton_ms, color="#d7eaf4", alpha=0.35)
        ax.axvspan(ton_ms, first_period_end, color="#f7ead9", alpha=0.35)
        ax.axvline(first_period_end, color="0.45", linewidth=0.9, linestyle="--")

    axes[0].annotate(
        r"$T_{ON}$",
        xy=(ton_ms / 2.0, 1.22),
        ha="center",
        va="bottom",
        fontsize=10,
    )
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


def generate_all() -> list[Path]:
    outputs = [
        generate_feee_circuits(),
        generate_feee_waveforms(),
        generate_power_circuit(),
        generate_power_waveforms(),
    ]
    return outputs


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
        outputs = [generate_feee_circuits(), generate_feee_waveforms()]
    else:
        outputs = [generate_power_circuit(), generate_power_waveforms()]

    for output in outputs:
        print(output.relative_to(ROOT))


if __name__ == "__main__":
    main()
