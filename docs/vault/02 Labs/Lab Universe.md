---
tags: [lab, un, universe, particles]
lab-id: un
---
# Lab Universe (`un`): particles in a universe you can change

**Idea.** A particle simulator: particles move, decay, annihilate, react and form hadrons in a chosen universe whose rules you can change. Up to `QS(1200,2400)` particles on CPU, 16384 with WebGPU (`unCap`).

## Particle table `UPT`
181 particles (not counting antiparticles): leptons 6, quarks 6, gauge bosons 4, Higgs 1, mesons 44, baryons 57, nuclei and atoms 15, hypothetical 28, exotic 20. Each entry has real mass, charge, spin, lifetime and decay channels. The 17 Standard Model particles are here as point particles; their *field* picture is the [[Particle Fields lab plan]].

## Universes (`UNIV`, 12)
| id | name | what changes |
|---|---|---|
| our | Our universe | the Standard Model as measured |
| noweak | No weak force | nothing that decays weakly can decay |
| freeq | No confinement | free quarks with ⅓, ⅔ charges, thin tracks instead of jets |
| strongG | Strong gravity | a cooling cloud collapses into a star |
| flat | Flatland (2D) | forces fall as 1/r |
| space4 | Four space dimensions | forces fall as 1/r³, no stable orbits |
| cube | Inverse-cube forces | 1/r³ in 3D, orbits spiral (Bertrand) |
| slowc | Slow light | visible time dilation of muons |
| mirror | Mirror world | mirror atoms that only share gravity |
| exotic | Exotic matter | negative mass, tachyons, monopoles, anyons, paraparticles |
| rhand | Right-handed weak force | weak force acts on right-handed particles |
| lrsym | Left–right symmetric | parity conserved |

## Settings sections
Real physics · Big Bang (`bb*`, epochs and nucleosynthesis) · Life of a star (`sr*`, track by mass 10^`srM`, colour from temperature) · Black hole (`unBH*`, Schwarzschild radius, Hawking strength `unHawk`) · Binary black holes (`unBN*`) · Neutrino oscillations (`nu*`: `nuMix`, `nuProb`) · Invent a particle (`unInv*`: name, symbol, mass, charge, spin, decays; `unInvAdd` registers it). Chirality is `st.uni.chi` (`unChi`, neutrino helicity).

Event toggles in `unDef`: decays, annihilation, hadronisation, reactions, medium; plus trails, bounds, particle spawner (`spk`, energy `sE`, direction `sDir`).

## Scenes
69, e.g. bubble chamber, pair production, Z/W/Higgs decays, LEP, LHC, air shower, first three minutes, one per universe, parity violation (Wu experiment), "Invent a particle: the glimmeron". See [[Scene catalog]].

Code: `ENG.un`, see [[Architecture]]. Related: [[Lab Lattice]], [[s+tD sandbox idea]].
