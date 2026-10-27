---
tags: [lab, su, algebra]
lab-id: su
---
# Lab su3 (`su`): the strong force's Lie algebra

**Object.** The colour charges `Q₁, Q₂` of two quarks live in **su(3)**, the 8-dimensional Lie algebra with Gell-Mann generators λ₁…λ₈. Together `Z = Q₁ + iQ₂ ∈ sl(3,ℂ) = ℂ⁸`.

**Picture.** Charges in the Cartan plane (λ₃, λ₈) commute. Any off-diagonal part makes the commutator `[Q₁,Q₂] = i f_abc Q₁ᵃ Q₂ᵇ λ_c` non-zero and **twists the flux tube** between them. Colour and anticolour attract and pull a tube; equal colours don't.

## Code (`ALG.su.post`)
- Basis: Gell-Mann with `[λa/2, λb/2] = i f_abc λc/2`, `f₁₂₃ = 1`, `f₄₅₈ = f₆₇₈ = √3/2`. `FABC` is the 8×8×8 structure-constant table, `comm8(X,Y)` the commutator.
- `qv8(θ, φ)` maps two angles to a unit charge vector in ℝ⁸ (θ mixes the Cartan plane with the off-diagonal generators, φ is the colour angle). `Q = [qv8(P0.th, P0.ph + C.b·120), qv8(P1.th + C.phi, P1.ph)]`.
- Quantities: `K = comm8(Q0,Q1)`, `kap = |K|` (non-abelian-ness), `dt = Q0·Q1`, attraction `att = (1 − dt)/2`, tube strength `T = ap.kap·0.32·(m0+m1)·att`.
- The tube is installed by `setTube(T, a)` (`RT.tb`); `fCa` adds `tubeF` (field around the segment between the two sources, flux-tube profile).
- `RT.am[k] = (1−w)·LRm(axis, k, …) + w·LRm(tube direction)` with `w = min(1, kap·1.4)`: the streams bend toward the tube as the commutator grows.
- Readouts in `D.al`: `dot, kap, att, T, cas` (Casimir |Q₀+Q₁|²), angles `a1, a2`, Cartan magnitudes `dg`. `m8` = adjoint representation matrix `ad(Q₀)`.

## Controls
`apK`: strength of the colour flux tube. Presets: quark and antiquark (meson), off-diagonal charges, two equal colours, long string.

## Scenes
17, e.g. meson flux tube, charge rotation, Casimir. See [[Scene catalog]]. Compare with real QCD in [[Lab Lattice]] (SU(3) gluons, lattice QCD, confinement) and [[Lab Universe]] (string breaking, jets).

Engine: [[Shared 4D field engine]].
