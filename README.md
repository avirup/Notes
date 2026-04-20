AI Generated Texbooks for my class

Generated engineering figures now live alongside the chapter sources.

- Run `python3 Scripts/generate_engineering_figures.py --target all` to regenerate the current circuit schematics and waveform plots.
- The script uses `circuitikz` plus `pdflatex` and `inkscape` for SVG schematics, and `numpy` plus `matplotlib` for simulation-backed waveform plots.
