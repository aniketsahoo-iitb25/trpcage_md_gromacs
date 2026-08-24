# trpcage_md_gromacs
All-atom molecular dynamics simulation of the Trp-cage mini-protein using GROMACS, including system preparation, energy minimization, NVT/NPT equilibration, production MD, and trajectory analysis.


# Trp-Cage Molecular Dynamics Simulation and Analysis

## Overview

Molecular dynamics simulation of the 20-residue Trp-Cage mini-protein
(TC5B; PDB ID: 1L2Y) using GROMACS.

The project demonstrates an end-to-end molecular dynamics workflow including
protein preparation, topology generation, solvation, ion addition, energy
minimization, NVT/NPT equilibration, production MD, and trajectory analysis.

## Objectives

- Set up a solvated protein molecular dynamics system
- Perform energy minimization
- Equilibrate the system under NVT and NPT ensembles
- Perform production molecular dynamics
- Characterize structural stability using RMSD and radius of gyration
- Quantify residue-level flexibility using RMSF
- Monitor temperature, pressure, density, and potential energy
- Automate statistical analysis using Python

## System

| Parameter | Value |
|---|---|
| Protein | Trp-Cage / TC5B |
| PDB | 1L2Y |
| Residues | 20 |
| Force field | AMBER99SB-ILDN |
| Water model | TIP3P |
| Simulation engine | GROMACS 2026.3 |
| Production length | 1 ns |
| Analysis window | 200–1000 ps |
| Hardware | CPU |
| GPU acceleration | Disabled |

## Workflow

```text
PDB structure
     ↓
pdb2gmx
     ↓
Topology generation
     ↓
Dodecahedral box
     ↓
TIP3P solvation
     ↓
Ion addition
     ↓
Energy minimization
     ↓
NVT equilibration
     ↓
NPT equilibration
     ↓
1 ns production MD
     ↓
Trajectory analysis
     ↓
RMSD / RMSF / Rg / T / P / Density / Energy

```
## Key Results

Analysis of the final 800 ps of the production trajectory produced:

| Metric             |             Mean |
| ------------------ | ---------------: |
| Backbone RMSD      |         0.088 nm |
| Radius of gyration |         0.722 nm |
| Temperature        |         299.99 K |
| Density            |     990.67 kg/m³ |
| Potential energy   | −76865.52 kJ/mol |
| Mean RMSF          |         0.061 nm |
| Maximum RMSF       |         0.144 nm |


The backbone RMSD remained in the range of approximately 0.064–0.123 nm
during the analyzed period, while the radius of gyration remained around
0.72 nm.

Residue 20 showed the highest RMSF at approximately 0.144 nm.

These results indicate no obvious large-scale structural destabilization
during this short production trajectory. However, the 1 ns simulation is
insufficient to make claims about long-timescale conformational stability.

## Analysis

Analysis data are provided as GROMACS .xvg files in analysis/.

The Python script: python scripts/analyze_md.py

generates summary statistics in: analysis/md_statistics.csv

## Visualizations

Backbone RMSD

Radius of gyration

RMSF

Temperature

Density

Pressure

Potential energy

## Repository Structure
```text
├── input/          # Initial PDB structure
├── mdp/            # GROMACS simulation parameters
├── topology/       # Molecular topology files
├── structures/     # Intermediate/final coordinate files
├── trajectories/   # Information about excluded large trajectories
├── analysis/       # XVG data and statistical summaries
├── figures/        # Analysis plots
├── scripts/        # Python analysis scripts
└── docs/           # Workflow and detailed results
```
## Reproducibility

The repository contains the input structure, topology, GROMACS parameter
files, analysis data, and analysis scripts required to reproduce the workflow.

Large binary trajectory and checkpoint files are intentionally excluded from
the repository.

## Limitations
Production MD duration was limited to 1 ns.
The simulation was performed using CPU-only GROMACS.
RMSD, RMSF and other observables are trajectory-dependent and should not be
interpreted as definitive evidence of long-timescale protein stability.
Longer simulations and replicate trajectories would be required for a more
rigorous assessment of conformational behavior.

## Tools
GROMACS,
Python,
NumPy,
Pandas,
Matplotlib,
Linux,
Bash,
Git/GitHub

## Author

Aniket Sahoo

Bioinformatics / Computational Biology Portfolio Project
