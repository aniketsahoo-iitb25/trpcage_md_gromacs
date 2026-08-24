# Trp-Cage MD Workflow

## System

- Protein: Trp-Cage (TC5B)
- PDB: 1L2Y
- Number of residues: 20
- Force field: AMBER99SB-ILDN
- Water model: TIP3P
- Simulation engine: GROMACS 2026.3
- Hardware: CPU-only
- GPU acceleration: disabled

## Workflow

1. Protein structure preparation
2. Topology generation using `pdb2gmx`
3. Dodecahedral simulation box generation
4. TIP3P solvation
5. System ionization and neutralization
6. Energy minimization
7. NVT equilibration
8. NPT equilibration
9. 1 ns production molecular dynamics
10. Trajectory analysis

## Key GROMACS commands

### Structure preparation

```bash
gmx pdb2gmx \
    -f 1L2Y.pdb \
    -o processed.gro \
    -p topol.top \
    -i posre.itp \
    -ignh

Box Generation----------------------------------------------------------------
gmx editconf \
    -f processed.gro \
    -o boxed.gro \
    -c \
    -d 1.0 \
    -bt dodecahedron

Solvation---------------------------------------------------------------------
gmx solvate \
    -cp boxed.gro \
    -cs spc216.gro \
    -o solvated.gro \
    -p topol.top

Ion Addition-----------------------------------------------------------------
gmx grompp \
    -f ions.mdp \
    -c solvated.gro \
    -p topol.top \
    -o ions.tpr

gmx genion \
    -s ions.tpr \
    -o solvated_ions.gro \
    -p topol.top \
    -pname NA \
    -nname CL \
    -neutral

Energy Minimization----------------------------------------------------------
gmx grompp \
    -f em.mdp \
    -c solvated_ions.gro \
    -p topol.top \
    -o em.tpr

gmx mdrun \
    -deffnm em

NVT Equilibration------------------------------------------------------------
gmx grompp \
    -f nvt.mdp \
    -c em.gro \
    -r em.gro \
    -p topol.top \
    -o nvt.tpr

gmx mdrun \
    -deffnm nvt

NPT Equilibration------------------------------------------------------------
gmx grompp \
    -f npt.mdp \
    -c nvt.gro \
    -r nvt.gro \
    -t nvt.cpt \
    -p topol.top \
    -o npt.tpr

gmx mdrun \
    -deffnm npt

Production MD----------------------------------------------------------------
gmx grompp \
    -f md.mdp \
    -c npt.gro \
    -t npt.cpt \
    -p topol.top \
    -o md.tpr

gmx mdrun \
    -deffnm md


----------------------------------------------------------------------------
Analysis

The production trajectory was analyzed using GROMACS tools for:

Backbone RMSD
Residue-wise RMSF
Radius of gyration
Temperature
Pressure
Density
Potential energy

Additional statistical summaries were generated using:

python scripts/analyze_md.py


---


# 14. Create the Results document


This is where your actual numbers are useful.


```bash
nano docs/results.md
