---
tags: [lab, cl, algebra]
lab-id: cl
---
# Lab Clifford (`cl`): the spacetime algebra Cl(1,3)

**Object.** A multivector `M ∈ Cl(1,3)` with 1 + 4 + 6 + 4 + 1 = 16 real components. The pseudoscalar `I = γ₀γ₁γ₂γ₃` squares to −1, so the algebra is ℂ⁸: `(s + I·p, E + I·B, v + I·t)` = scalar + I·pseudoscalar, the **bivector F = E + IB** (an electromagnetic field), and vector + I·trivector. Convention `γ₀² = 1, γ_k² = −1`. Lorentz invariants `F² = E² − B² + 2I E·B`.

**Picture.** The even part streams along the Lorentz force `F·∇f`; the odd part along the **reflection of ∇f in v** (a vector acts by reflection). The geometric product does not commute.

## Code (`ALG.cl.post`)
- `E = m₀cos η·n₀`, `B = m₀ sin η (cos ζ·n₀ + sin ζ·e₀)`: η = balance between electric and magnetic part, ζ = angle between E and B. A null field (light) needs η = 45° and ζ = 90°.
- Vector `v` tilts toward time by ν (`apN`); `μ` (`apM`) mixes vector with the trivector part.
- `M₀` = 4×4 matrix of F acting on a vector (antisymmetric: B in the spatial block, E in the time row/column). `M₁` = reflection `R = 1 − 2 v̂v̂ᵀ` blended with F.
- `RT.am = [M0, M1]`. Non-commutativity measure `nc = |M₀M₁ − M₁M₀|`.
- Readouts: `inv1 = E²−B²`, `inv2 = E·B`, `v² = v₃²−|v|²`, `sc`, `ps`, angles. `m8` = 8×8 block matrix `[[M0, M0M1],[M1M0, M1]]`.

## Controls
`apE` (η), `apZ` (ζ), `apN` (ν), `apM` (μ): see [[Parameter reference]] (Algebra pair controls). Presets: even and odd part, parts overlapping, tilted in 4D.

## Scenes
16. See [[Scene catalog]]. Engine: [[Shared 4D field engine]].
