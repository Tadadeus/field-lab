---
tags: [overview, naming]
---
# Naming conventions

The code is terse by design (single file, no minifier needed). Names are mostly **prefix + meaning**.

## Prefixes
| prefix | meaning | examples |
|---|---|---|
| `tw*`, `ca*` | twistor / Courant engines | `twFrame`, `caFrame`, `caCompose`, `fCa` |
| `lat*`, `lq*`, `LAT*`, `LA*` | Lattice lab ([[Lab Lattice]]) | `latInit`, `latStepCPU`, `LATM`, `lqInit` |
| `ch*`, `sg*`, `q*` (lattice QCD) | spin chain, superconducting metal, 2D lattice QCD | `chStep`, `sgStep`, `qSweep` |
| `un*`, `UN`, `UP*`, `UF*` | Universe lab ([[Lab Universe]]) | `unStep`, `UPT`, `UNIV`, `upParse` |
| `sr*`, `bb*`, `tv*` | stars, Big Bang, Universe telemetry views | `srBuild`, `bbDraw`, `tvNu` |
| `eq*`, `EQ*` | Law Lab ([[Lab Law]]) | `eqParse`, `eqCompileODE`, `EQS` |
| `fl*`, `FL*` | Fluid Lab ([[Lab Fluid]]) | `flLbmStep`, `FLS`, `flSmokeStep` |
| `cx*`, `CX*` | Calc Lab ([[Lab Calc]]) | `cxSurf3`, `CXF`, `CXS` |
| `gpu*`, `g*`, `WGSL_*`, `GPU`, `GU` | WebGPU ([[Rendering with WebGPU]]) | `gpuRender`, `WGSL_FL` |
| `cb*`, `CB` | colorbars ([[Colormaps and colorbars]]) | `cbDraw`, `cbDesc` |
| `q*` (UI) | quality ([[Quality tiers]]) | `qUI`, `qOpen`, `QOPT` |
| `sv*`, `m*` | slice viewer and mini views | `svDraw`, `mDials` |
| `hs*`, `HS` | history ([[History timeline]]) | `hsPut`, `hsTick` |
| `ent*`, `ETYPES` | sandbox entities ([[Sandbox objects and probes]]) | `entNew` |
| `spec*` | control **spec** functions: return an array of control descriptors | `specLat`, `specUni`, `specField` |
| `CK` | canvas colour kit, reads CSS variables once ([[Design tokens]]) | `CK.fg`, `CK.i(.5)` |

## Suffix letters on lab functions
Features were added as layers on top of earlier ones. The suffix says which:
| suffix | layer | example |
|---|---|---|
| `0` | the original version, later wrapped | `specLat0`, `latStepCPU0` |
| `H` | handedness / chirality (Universe) | `specUniH`, `unSpawnH` |
| `R` | real-physics options (Universe) | `specUniR`, `unRealStepV` |
| `L` | "long"/extras (Universe) | `specUniL` |
| `B`, `N`, `Nu`, `V`, `BB`, `SR` | black hole, binary/GW, neutrino, vacuum, Big Bang, star life | `specUniB`, `specUniNu` |
| `C` | chain (Lattice) | `latFrameC`, `specLatC` |
| `Q` | lattice QCD | `latFrameQ` |
| `S` | superconducting metal | `latFrameS` |
| `V` (Lattice) | vacuum decay | `specLatV` |

A function with a suffix usually **wraps** the one without it: it calls the earlier function and adds behaviour, or replaces it for one sub-model.

## Core data shapes
- Complex number = `[re, im]`. Helpers: `cm` multiply, `ca` add, `csub`, `cj` conjugate, `cs` scale, `ci` times i, `cinv`, `ab2` |z|².
- Twistor `Z` = 4 complex numbers `(ω0, ω1, π0, π1)`.
- 4×4 real matrix = flat array of 16 (`m4mul`, `m4v`, `m4inv`).
- Bi-object source `S[k]` = `{c, m, a, a2, th, ph, chi, n, e2, e3, …}`: centre, charge, core radius, axis angles, orthonormal frame.
- Colour = `[r,g,b]` 0–255 from `pcol(hue, light)`; palettes are `PALETTES` / `PALRGB`.
- Scene = `{k, th, n, f(C)}`.
- Control spec = `{t:'r'|'s'|'a'|'c'|'h'|'n', id, lb, …}` ([[Controls framework]]).
- Constants: `DEG=π/180`, `PR=1.7`, `HB=2.2` (half-size of the 3D box, ±2.2 units).
