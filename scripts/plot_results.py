#!/usr/bin/env python3

"""
Plot GROMACS XVG analysis files.

Input:
    analysis/*.xvg

Output:
    figures/*.png
"""

from pathlib import Path

import numpy as np
import matplotlib.pyplot as plt


# ---------------------------------------------------------
# Paths
# ---------------------------------------------------------

PROJECT_ROOT = Path(__file__).resolve().parents[1]
ANALYSIS_DIR = PROJECT_ROOT / "analysis"
FIGURES_DIR = PROJECT_ROOT / "figures"

FIGURES_DIR.mkdir(exist_ok=True)


# ---------------------------------------------------------
# XVG reader
# ---------------------------------------------------------

def read_xvg(filename):
    """Read numerical data from a GROMACS XVG file."""
    
    data = []

    with open(filename, "r") as file:
        for line in file:
            line = line.strip()

            # Ignore GROMACS comments and metadata
            if not line or line.startswith("#") or line.startswith("@"):
                continue

            values = line.split()

            try:
                data.append([float(value) for value in values])
            except ValueError:
                continue

    return np.array(data)


# ---------------------------------------------------------
# Plotting function
# ---------------------------------------------------------

def make_plot(filename, output_name, xlabel, ylabel, title):
    """Read an XVG file and generate a PNG figure."""

    filepath = ANALYSIS_DIR / filename
    output = FIGURES_DIR / output_name

    data = read_xvg(filepath)

    if data.size == 0:
        print(f"WARNING: No numerical data found in {filepath}")
        return

    x = data[:, 0]
    y = data[:, 1]

    plt.figure(figsize=(7, 5))

    plt.plot(x, y, linewidth=1.5)

    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)

    plt.tight_layout()
    plt.savefig(output, dpi=300)
    plt.close()

    print(f"Created: {output}")


# ---------------------------------------------------------
# Generate figures
# ---------------------------------------------------------

make_plot(
    "rmsd.xvg",
    "rmsd.png",
    "Time (ns)",
    "Backbone RMSD (nm)",
    "Trp-Cage Backbone RMSD"
)

make_plot(
    "rmsf.xvg",
    "rmsf.png",
    "Residue",
    "RMSF (nm)",
    "Trp-Cage Residue-wise RMSF"
)

make_plot(
    "gyration.xvg",
    "gyration.png",
    "Time (ps)",
    "Radius of gyration (nm)",
    "Trp-Cage Radius of Gyration"
)

make_plot(
    "temperature.xvg",
    "temperature.png",
    "Time (ps)",
    "Temperature (K)",
    "Production MD Temperature"
)

make_plot(
    "pressure.xvg",
    "pressure.png",
    "Time (ps)",
    "Pressure (bar)",
    "Production MD Pressure"
)

make_plot(
    "density.xvg",
    "density.png",
    "Time (ps)",
    "Density (kg m$^{-3}$)",
    "Production MD Density"
)

make_plot(
    "potential.xvg",
    "potential.png",
    "Time (ps)",
    "Potential Energy (kJ mol$^{-1}$)",
    "Potential Energy"
)
