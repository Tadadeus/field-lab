---
tags: [lab, la, lattice, field-theory]
lab-id: la
---
# Lab Lattice (`la`): field theory on a grid

**Idea.** Fields live on a 3D grid (sites, links, plaquettes) and are stepped in time with a kick–drift (leapfrog) scheme. Each model in `LATM` declares its field counts (`na` site fields, `nl` link fields, `ne` electric fields), time step `dt`, sliders `ps`, start states `ini` and colour modes `cm`.

## Models (`LATM`, 16), with their start states
| id | label | start states |
|---|---|---|
| phi4 | Real scalar φ⁴ · domain walls | random quench, collapsing bubble, colliding walls, false vacuum decays, bubble too small to grow, many bubbles nucleate |
| cplx | Complex Higgs · global strings | random quench, vortex ring, vortex and antivortex |
| ah | Abelian Higgs · flux tubes | random quench, vortex and antivortex, vortex ring |
| em | Maxwell U(1) · photons | oscillating dipole, two light pulses |
| su2 | SU(2) Yang–Mills · W field | random color field, colliding color waves |
| su3 | SU(3) Yang–Mills · gluons | random gluon field, colliding gluon waves |
| ew | SU(2) Higgs doublet · electroweak | Higgs quench, Higgs bubble |
| dirac | Dirac field · electron | moving packet, Klein paradox, Zitterbewegung, magnetic field, Coulomb atom, left-handed packet (Weyl) |
| grav | Linearized gravity · waves | orbiting binary, inspiral chirp |
| schr | Schrödinger particle · quantum waves | double slit, tunneling, squeezed state in a trap, orbiting in a trap, quantum Hall edge state, edge state meets an impurity, Landau level orbit |
| gpe | Bose–Einstein condensate · Gross–Pitaevskii | rotating trap, dark soliton, two condensates, vortex ring |
| tdgl | Superconductor · Ginzburg–Landau | field switched on, cooled in a field, with pinning centers |
| llg | Chiral magnet · skyrmions | skyrmion lattice, helical stripes, one skyrmion, magnetic domains |
| chain | Quantum spin chain · entanglement | all up then sudden field, one flipped spin, Néel ↑↓↑↓, domain wall ↑↑↑↓↓↓, all along x |
| lqcd | Lattice QCD 2D · confinement | hot start (random links), cold start (links = 1) |
| metal | Superconducting metal · Meissner, vortices, current | cooled in a field, field switched on, cooled then field removed, slowly warmed |

## Code
- CPU reference step `latStepCPU(dt)`: source terms (`latSrc`), then a `kick` per model, damping `1 − gam·|dt|`. Dirac has its own `latDiracCPU`; topological defects are found by `latDefectsCPU`.
- GPU path: `latGpuBuild / latGpuStep / latGpuKick / latGpuDraw / latGpuSlice`, plus volume rendering `latVolOn / latVolStep` ([[Rendering with WebGPU]]).
- Absorbing edges: `latSponge`. Grid size: `latN` (follows [[Quality tiers]]).
- Registered as `ENG.la` (`render3, hide, bg, plane, chart, slice, svcap, chip`), see [[Architecture]].
- 64 Lattice scenes in [[Scene catalog]].

Related: [[Lab Universe]], [[Lab su3]], [[Lab Qubits]].
