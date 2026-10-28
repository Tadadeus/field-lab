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

## Added in `src/qg.js` (v22)
- **dirac · `super`** "supercritical nucleus (Z > 173)": starts as the Coulomb atom, then the charge ramps from Z = 1 to the slider value over t = 70 (`qgZ`, smoothstep). The softened potential −Z/√(r²+1) acts as a finite nucleus. Measured on the lattice (m = 0.3): the 1s level crosses −m at Z_cr ≈ 2.33, shown as 173 (`qgZr`). Above it the 1s state dives into the Dirac sea, so the particle part drops and an antiparticle halo leaks out (positron emission in the hole picture). Scene `la_super`.
- **grav · `foam`** "quantum foam · micro black holes" (illustration): random Planck-scale kicks to the six metric components (`qgFoamStep`). A site whose energy exceeds 7× the sampled mean collapses into a micro black hole (≤ 5 at once), which absorbs ripples and evaporates as dM/dt = −0.03/M². It ends in a burst that sends out a quadrupole ripple. The black hole state lives in `LT.qf`; meshes are in `QGV`. Scene `la_foam`.
- Both run on the CPU path only: a `latGpuReady` wrapper returns false for them, so GPU shaders and other models are untouched.

## Code
- CPU reference step `latStepCPU(dt)`: source terms (`latSrc`), then a `kick` per model, damping `1 − gam·|dt|`. Dirac has its own `latDiracCPU`; topological defects are found by `latDefectsCPU`.
- GPU path: `latGpuBuild / latGpuStep / latGpuKick / latGpuDraw / latGpuSlice`, plus volume rendering `latVolOn / latVolStep` ([[Rendering with WebGPU]]).
- Absorbing edges: `latSponge`. Grid size: `latN` (follows [[Quality tiers]]).
- Registered as `ENG.la` (`render3, hide, bg, plane, chart, slice, svcap, chip`), see [[Architecture]].
- 66 Lattice scenes in [[Scene catalog]].

Related: [[Lab Universe]], [[Lab su3]], [[Lab Qubits]].
