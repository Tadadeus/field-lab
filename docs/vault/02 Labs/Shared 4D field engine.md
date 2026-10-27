---
tags: [lab, engine]
---
# Shared 4D field engine

Seven labs (`tw, ca, oc, su, cl, qb, se`) draw "the field of a pair of objects". Only **two base engines** exist; the algebra labs reuse the Courant one and plug in their own algebra.

```
tw  → twFrame()  Penrose-transform light field of two twistors       (st.th = 'tw')
ca  → caFrame()  doubled-geometry field of two NS5-brane throats     (st.th = 'ca')
oc su cl qb se → caFrame() + ALG[id].post(D, C)   (st.th = 'ca', st.alg = id)
```

## Common pieces
| piece | meaning |
|---|---|
| `st.fl.src` | which source(s) to show: `both`, `0` or `1` (`srcList()`) |
| `fld(k,x,y,z,w)` | field of source k at a point; returns `{rho, th, d, …}` = density, phase, direction. Routes to `fTw` or `fCa` |
| `ldir(k,…)` | direction used to trace field lines (also E/B variants for twistors) |
| particles | tracer points spawned where `rho` is large and advected along `d` (`spawn`, `psStep`) |
| lines | field lines integrated from anchor points (`linesUpd`) |
| membrane | isosurface `rho = level` built with marching tetrahedra `mtRun` ([[Rendering with WebGL]]) |
| objects | the two shaped objects (Hopf link, knots, tori, …) that ride the transformation (`objUpd`) |
| probes | field measured at a dropped point ([[Sandbox objects and probes]]) |
| slice | 2D cut through the pair in the `xy / xz / yz / xw / yw / zw` plane (`svDraw`, `PLN`) |

## Motion modes (`st.mode`)
`composeS`: `twCompose()` for twistors, `caCompose()` for Courant. Modes:

| mode | what happens | parameter |
|---|---|---|
| `rot` | rotation (spinor-rotation `U2`, with the 720° spinor feature) along path styles `st.path` | angle `v.rot` (0–720) |
| `boost` | Lorentz boost (`Tbo` / `stretch4`) | rapidity `v.boost` |
| `dil` | dilation (`Tdi` / `scaleM4`), lengths ×e^λ | `v.dil` |
| `conf` | special conformal map (`Tco`), inversion-translation-inversion | `v.conf` |
| `mix` | helicity/Courant mixing (`Gmix`, with phase β) | `v.mix` |
| `evo` | free time evolution (`Tev`, phases `phG`) | `v.evo` ∈ [−2, 2] |
| `all` | everything together ("Motion" tab): each term oscillates with its own waveform and frequency (`wave()`, `st.fr`) | `fv` + `fr` |

`advance(dt)` moves these over time. In `rot` the angle runs at 40°/s, in `mix` at 28°/s, in `evo` the time sweeps −2…2 and wraps (clearing trails). Oscillating modes use `amp[mode]·sin(phase)`.

The twistor transformation matrix is 4×4 complex (`T4`, `mm4`); the Courant one is a real 4×4 `A = R·SD` (rotation × stretch) with `Ai`, `AiT` its inverse and transpose.

## Left/right isoclinic rotation (4D)
A 4D rotation is a pair of unit quaternions (α, β): `rotLR(al, be)`. The *left ↔ right balance* slider `lr` scales α and β (`lbW`) so you can move continuously from an ordinary 3D rotation (balance 0) to a pure left or right Hopf rotation (±2).

## 4D viewing (`V4S`, `V4`)
In 4D mode the points are 4-vectors. `v4Setup` builds the 4D rotation `V4S.R` from the plane angles (xw, yw, zw) and Hopf angles (left, right) and continuous spins. `V4e` projects with **stereographic** (from the 3-sphere pole at w=ρ) or **perspective** (camera at distance along w) projection and returns depth `W` used for the depth cue (`cueF`). Embeddings: `sphere` (stereographic ℝ³→S³), `native` (Courant: ℝ⁴ directly), `time` (w as scaled time).

## Algebra hook (`ALG[id]`)
```js
ALG.oc = {
  post(D, C){ … sets RT.am (2 matrices), RT.ab, RT.tb, D.Z (8 complex comps per object), D.axes, D.al, … },
  m8: D => D.al.m8,    // the 8×8 matrix shown in the matrix panel
  rl, rs, sl, hd, nt, ctl, rows, msg, info …   // labels, controls, readouts, text
}
```
`RT.am[k]` is a 4×4 matrix that turns the gradient `(g0..g3)` of the scalar `f = 1 + Σ m/(r²+a²)` into the direction of stream k, so each algebra changes **how the stream bends**, not the density `f`. `RT.tb` adds a flux tube between the two sources (`setTube`, `tubeF`); `RT.ab` adds a bias term.

The algebra helpers: octonions `omul`, sedenions `smul`, su(3) `comm8` with structure constants `FABC`, qubits `psi0/qg1/xyg/czg/cnotg/bloch/tangle3`.

## Source setup
`cpar(c, m, a, th, ph, chi)` makes a source: centre `c` (4D), charge `m`, core `a`, axis polar/azimuth `th, ph` and phase `chi`. Preset tables `TWS` (twistors), `CAS` (branes) and `ALS[id]` (per algebra lab) map a name to a function returning two such sources. `buildTw` / `buildCa` convert them to runtime objects `RT.Z0` / `RT.C0`.

## Where each lab differs
[[Lab Twistor]] · [[Lab Courant]] · [[Lab Octonion]] · [[Lab su3]] · [[Lab Clifford]] · [[Lab Qubits]] · [[Lab Sedenion]]. The Sandbox, Quantum, Geometry and Physics tabs work on top of any of them ([[Sandbox objects and probes]], [[Quantum Geometry Physics tabs]]).
