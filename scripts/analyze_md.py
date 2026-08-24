#!/usr/bin/env python3

import numpy as np
import pandas as pd
from pathlib import Path


# ============================================================
# Configuration
# ============================================================

ANALYSIS_DIR = Path("analysis")
ANALYSIS_START_PS = 200.0


# ============================================================
# Read GROMACS XVG
# ============================================================

def read_xvg(filename):
    """
    Read a GROMACS XVG file.

    Lines beginning with # or @ are ignored.
    Returns an Nx2 NumPy array.
    """

    data = []

    with open(filename, "r") as f:
        for line in f:

            line = line.strip()

            if not line:
                continue

            if line.startswith("#") or line.startswith("@"):
                continue

            fields = line.split()

            if len(fields) >= 2:
                data.append([
                    float(fields[0]),
                    float(fields[1])
                ])

    if not data:
        raise ValueError(f"No numerical data found in {filename}")

    return np.array(data)


# ============================================================
# Basic statistics
# ============================================================

def calculate_statistics(values):

    if len(values) == 0:
        raise ValueError("No data points available for statistics.")

    return {
        "N": len(values),
        "Mean": np.mean(values),
        "Std": np.std(values, ddof=1),
        "Min": np.min(values),
        "Max": np.max(values)
    }


# ============================================================
# Time-series analysis
# ============================================================

def analyze_timeseries(filename, time_unit="ps"):

    data = read_xvg(filename)

    time = data[:, 0]
    values = data[:, 1]

    # Convert time to ps internally
    if time_unit == "ns":
        time_ps = time * 1000.0
    elif time_unit == "ps":
        time_ps = time
    else:
        raise ValueError(
            f"Unsupported time unit: {time_unit}"
        )

    # Select analysis window
    mask = time_ps >= ANALYSIS_START_PS

    selected_time = time_ps[mask]
    selected_values = values[mask]

    if len(selected_values) == 0:
        raise ValueError(
            f"No data points remain for {filename} "
            f"after {ANALYSIS_START_PS} ps."
        )

    stats = calculate_statistics(selected_values)

    return {
        "N": stats["N"],
        "Start_ps": selected_time[0],
        "End_ps": selected_time[-1],
        "Mean": stats["Mean"],
        "Std": stats["Std"],
        "Min": stats["Min"],
        "Max": stats["Max"]
    }


# ============================================================
# Production time-series datasets
# ============================================================

datasets = {

    # filename : time unit in original XVG
    "Backbone RMSD": ("rmsd.xvg", "ns"),

    "Radius of gyration": ("gyration.xvg", "ps"),

    "Temperature": ("temperature.xvg", "ps"),

    "Pressure": ("pressure.xvg", "ps"),

    "Density": ("density.xvg", "ps"),

    "Potential energy": ("potential.xvg", "ps"),
}


# ============================================================
# Analyze datasets
# ============================================================

results = []

for name, (filename, time_unit) in datasets.items():

    filepath = ANALYSIS_DIR / filename

    if not filepath.exists():

        print(f"WARNING: {filepath} not found")

        continue

    result = analyze_timeseries(
        filepath,
        time_unit=time_unit
    )

    result["Analysis"] = name

    results.append(result)


# ============================================================
# Create summary table
# ============================================================

df = pd.DataFrame(results)

df = df[
    [
        "Analysis",
        "N",
        "Start_ps",
        "End_ps",
        "Mean",
        "Std",
        "Min",
        "Max"
    ]
]


# ============================================================
# Display results
# ============================================================

print()
print("=" * 100)
print("Trp-Cage Molecular Dynamics — Production Analysis")
print("=" * 100)

print()
print(
    f"Analysis window: "
    f"{ANALYSIS_START_PS:.0f} ps to end of trajectory"
)

print()

print(
    df.to_string(
        index=False,
        float_format=lambda x: f"{x:.5f}"
    )
)

print()


# ============================================================
# Save CSV
# ============================================================

output_file = ANALYSIS_DIR / "md_statistics.csv"

df.to_csv(
    output_file,
    index=False
)

print(f"Results saved to: {output_file}")


# ============================================================
# RMSF analysis
# ============================================================

rmsf_file = ANALYSIS_DIR / "rmsf.xvg"

if rmsf_file.exists():

    rmsf_data = read_xvg(rmsf_file)

    residues = rmsf_data[:, 0].astype(int)
    rmsf_values = rmsf_data[:, 1]

    max_index = np.argmax(rmsf_values)

    print()
    print("=" * 100)
    print("RMSF Analysis")
    print("=" * 100)

    print()
    print(f"Number of residues:       {len(rmsf_values)}")
    print(f"Mean RMSF:                {np.mean(rmsf_values):.4f} nm")
    print(f"Standard deviation:       {np.std(rmsf_values, ddof=1):.4f} nm")
    print(f"Minimum RMSF:             {np.min(rmsf_values):.4f} nm")
    print(f"Maximum RMSF:             {np.max(rmsf_values):.4f} nm")

    print(
        f"Most flexible residue:    "
        f"{residues[max_index]} "
        f"({rmsf_values[max_index]:.4f} nm)"
    )

    print()
