# Results

## Production MD

The system was subjected to a 1 ns production molecular dynamics simulation
following energy minimization and NVT/NPT equilibration.

The final 800 ps of the trajectory (200–1000 ps) were used for the primary
time-series analysis.

| Property | Mean | SD | Minimum | Maximum |
|---|---:|---:|---:|---:|
| Backbone RMSD (nm) | 0.0881 | 0.0123 | 0.0641 | 0.1226 |
| Radius of gyration (nm) | 0.7221 | 0.0092 | 0.6985 | 0.7511 |
| Temperature (K) | 299.99 | 4.37 | 287.96 | 317.85 |
| Pressure (bar) | 1.91 | 343.08 | -994.91 | 933.14 |
| Density (kg/m³) | 990.67 | 6.76 | 970.63 | 1010.31 |
| Potential energy (kJ/mol) | -76865.52 | 318.43 | -77806.67 | -75652.19 |

## Structural dynamics

The backbone RMSD during the analyzed period averaged approximately
0.088 nm (0.88 Å), with values ranging from 0.064 to 0.123 nm.

The radius of gyration averaged approximately 0.722 nm, indicating that the
protein maintained a relatively compact overall size during the analyzed
trajectory.

Residue-wise RMSF showed a mean fluctuation of 0.061 nm. The largest RMSF
was observed at residue 20 (0.144 nm), while the lowest RMSF was approximately
0.034 nm.

## Thermodynamic behavior

The production temperature averaged approximately 300 K, consistent with the
target simulation temperature.

The density averaged approximately 991 kg/m³. Instantaneous pressure exhibited
large fluctuations around the target pressure, which is expected for a small
periodic molecular dynamics system.

## Interpretation

Within the limitations of the 1 ns production trajectory, the analyzed
structural and thermodynamic observables show no obvious large-scale
destabilization of the Trp-Cage system. The backbone RMSD and radius of
gyration remained within relatively narrow ranges during the analyzed
production period.

Because the production trajectory is only 1 ns long, these observations should
be considered a short-timescale characterization rather than definitive
evidence of long-timescale conformational stability.


