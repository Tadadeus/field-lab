---
tags: [lab, tw]
lab-id: tw
---
# Lab Twistor (`tw`)

**Idea.** In twistor theory (Penrose) the basic objects are *light rays*, not points. A **twistor** `Z = (ω, π)` is a point of ℂ⁴ and stands for a twisting family of light rays. A **bi-twistor** `(Z₁, Z₂) ∈ ℂ⁸` (two twistors together) makes one real light field on spacetime: the Penrose transform of `1/((Z̄₁·Z)(Z̄₂·Z)^{n+1})`. The field's energy streams along the twisting rays of each twistor; its centre is the **Klein point** where the pair meets. Two light-like momenta add up to a time-like one, which is how a pair describes a massive particle.

## Maths in the code
- Spacetime point as a 2×2 matrix `X = t·1 − x·σ`; incidence `ω = iXπ`. `xsig(x,p)` computes `Xπ`, `tw(x0,θ,φ,E,s,χ)` builds a twistor from centre `x0`, momentum direction (θ, φ), energy `E`, helicity `s` and phase χ.
- `qOf(Z,X,Y,W,o)` computes the incidence residual `ω − iXπ` at a point; `fieldAt(Zf,k,x,n)` returns
  - density `rho = (|a|²+|b|²)^n / |D|^{2(n+1)}` with `D` the pairing of the two residuals (`dQ`),
  - phase `th = −(n+1)·arg D`,
  - direction `d` from the spinor bilinear `(2 Re(a b̄)…)/L`,
  - `xi` the two complex components.
  `n` = `st.fl.n` is the field's *spin parameter* (2 → electromagnetic-like, other values → gravity-wave, neutrino, scalar scenes).
- `maxF` builds a Maxwell field `F` (E and B vectors) from the spinors; `eDir(f)` returns E.
- `frameOf(Z)` extracts the geometric frame of one twistor (energy, helicity `s`, centre `c`, pole direction) via the Hopf map.
- `anal(Z)` returns the invariants of the pair: energies `E`, momentum `Pv`, mass² `M2`, twistor norms `N`, cross-term `S12`, Gram determinant, Plücker coordinates `pl` and `plk`, and the **Klein point** `K` with its velocity.
- The transformation group acts on `Z` by 4×4 complex matrices (`Tbo` boost, `Tdi` dilation, `Tco` special conformal, `Tev` time evolution) and the SU(2) rotation `U2`. `mapper(T)` / `tmap` map spacetime points through a transformation (used to warp the objects: `mkWarp4`, `preImg`, `stretchAt`).
- `st.fl.n` and the presets define the **helicity** of the field: ±½ neutrino, ±1 photon, ±2 graviton, 0 scalar.

## UI
- Heading: "Bi-twistor (Z₁, Z₂)", legend: twistor Z₁, twistor Z₂, link to the pair, pair centre, Im x.
- Plane view: the 4 complex components of each twistor as trails in the complex plane (`drawPlane`, `TP` trails).
- Sphere view: momentum directions on the celestial sphere (`drawSphere`).
- State tab (`specState`): edit `Z` directly: helicity `hs`, energy `hE`, polar `ht`, azimuth `hf`, phase `hc`, centre `hx hy hz` (see [[Parameter reference]], "Twistor state").

## Scenes
50 scenes (`tw_*`, `tw4_*`): knot pair, head-on beams, crossed beams, fast pair (v ≈ 0.94c), singular rings, opposite helicities, boosts, conformal pinch, dilation, spinor 720° tumble, gyroscope, helicity mixing, gravitational-wave knot (spin 2), neutrino twist (spin ½), scalar breather (spin 0), polarization vortex, binary orbit, chaos drive, 4D scenes (S³ knot, flying through infinity, double rotation, worldlines, light-cone streaks). Full list: [[Scene catalog]].

Engine details shared with the other six labs: [[Shared 4D field engine]].
