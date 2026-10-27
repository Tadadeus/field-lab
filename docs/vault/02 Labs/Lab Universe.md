---
tags: [lab, un, universe, particles]
lab-id: un
---
# Lab Universe (`un`): build and run a universe

**Idea.** Pick a universe (`UNIV`), tune constants, and watch particles, stars, black holes and the early universe respond. Everything is driven by a real particle table.

## Particle table `UPT`
181 particles (non-anti): leptons 6, quarks 6, gauge bosons 4, Higgs 1, mesons 44, baryons 57, nucleons 15, hyperons 28, exotics 20. Each entry carries real mass, charge, spin, lifetime and decay channels.

### The 17 Standard Model particles
They are already point particles here (6 quarks, 3 charged leptons, 3 neutrinos, photon, gluon, W, Z, Higgs). What is **not** yet shown is their *field* (wave) picture, see [[Particle Fields lab plan]].

## Universes (`UNIV`, 12)
our, noweak, freeq, strongG, flat, space4, cube, slowc, mirror, exotic, rhand, lrsym. Each changes a set of constants/rules (e.g. no weak force, free quarks, strong gravity, flat spacetime, 4 space dimensions, cubic lattice space, slow light, mirror matter, exotic matter, right-handed only, left-right symmetric).

## Subsystems
- **Stars** (`sr*`): mass → luminosity, lifetime, fusion chain, end state.
- **Big Bang** (`bb*`): temperature history, freeze-outs, nucleosynthesis.
- **Black holes and gravitational waves** (`unBH`, `unBN`): Schwarzschild/Kerr scales, mergers, chirp.
- **Neutrino oscillation** (`nu*`): PMNS mixing between flavours.
- **Vacuum** and **Hawking** radiation.
- **Chirality** (names with suffix `H`): handedness of particles.
- **Inventor**: compose your own particle and see whether it is stable.

## Code
Registered in `ENG.un` with the same interface as the other engines (see [[Architecture]]). Scenes live in [[Scene catalog]]; sliders in [[Parameter reference]].

Related: [[Lab Lattice]] (fields), [[Particle Fields lab plan]], [[s+tD sandbox idea]].
