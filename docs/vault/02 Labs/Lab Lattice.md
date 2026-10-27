---
tags: [lab, la, lattice, field-theory]
lab-id: la
---
# Lab Lattice (`la`): field theory on a grid

**Idea.** A field lives on an `N×N×N` grid and is stepped in time by **leapfrog** (symplectic, second order). Each model in `LATM` defines its fields, a Hamiltonian/force, initial conditions and readouts. The lab renders the field as isosurface/volume/slice and charts conserved quantities.

## Models (`LATM`)
| id | model |
|---|---|
| phi4 | real scalar φ⁴ (kinks, domain walls, symmetry breaking) |
| cplx | complex scalar, U(1) global (Goldstone mode, vortices; NG modes are in the dynamics) |
| ah | Abelian Higgs (U(1) gauge + Higgs, superconductor, Meissner effect, flux tubes) |
| em | free Maxwell field (E, B waves) |
| su2 | SU(2) gauge |
| su3 | SU(3) gauge (gluons) |
| ew | electroweak SU(2)×U(1) with Higgs |
| dirac | Dirac fermion field |
| grav | linearised gravity / waves |
| schr | Schrödinger equation (wave packets, tunnelling) |
| gpe | Gross–Pitaevskii (Bose–Einstein condensate, vortices) |
| tdgl | time-dependent Ginzburg–Landau |
| llg | Landau–Lifshitz–Gilbert (magnetisation, skyrmions) |
| chain | quantum spin chain (small exact state vector) |
| lqcd | lattice QCD style link variables |
| metal | tight-binding metal / band structure |

## Code
- CPU step: `latStepCPU`; GPU path via WebGPU compute (see [[Rendering with WebGPU]]) when available, same equations, CPU is the reference.
- Boundary conditions, damping, quench and "kick" tools are controls in the `qm`, `ph` and `field` tabs of [[Settings and app popover]].
- Isosurface via marching tetrahedra (`mtRun`), volume ray-march on GPU, slices through the engine registry `ENG.la` (`render3, hide, bg, plane, chart, slice, svcap, chip`). See [[Architecture]].
- Charts: energy, norm, topological charge, order parameter; data exportable via [[Telemetry pins and CSV]].
- Per-model scenes in [[Scene catalog]] (category Lattice); help entries in [[Help tooltips glossary tour]].

## Notes
- Time stepping is velocity-Verlet/leapfrog, so energy oscillates but does not drift.
- Quality tier sets `N` and substeps per frame, see [[Quality tiers]].
- Universe-scale physics built on similar fields: [[Lab Universe]].
