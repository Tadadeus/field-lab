---
tags: [lab, se, algebra]
lab-id: se
---
# Lab Sedenion (`se`): ℂ ⊗ 𝕊 = ℂ¹⁶

**Object.** Two bioctonions joined by one more Cayley–Dickson doubling make a **complex sedenion** `Z = (Z₁, Z₂) ∈ ℂ ⊗ 𝕊 = ℂ¹⁶`: 16 complex components, 32 real numbers. Sedenions are not even alternative, their norm is not multiplicative, and they have **zero divisors**: two non-zero sedenions whose product is exactly 0. Convention `(a,b)(c,d) = (ac − d̄b, da + bc̄)`; with it `(e₁ + e₁₀)(e₅ + e₁₄) = 0` (`ZD` holds this pair).

**Picture.** Object 1 streams along `s₁(s₂∇f)`, object 2 along `(s₁s₂)∇f`. At a zero divisor the second product vanishes and **object 2 freezes**.

## Code (`ALG.se.post`)
- `smul(x,y)` sedenion product on 16-vectors, using `omul` on halves.
- Each unit sedenion `sv[k]` is built from the octonion-like `U[k]`, with parameters: β (`apB`, tilt out of ℍ), γ (`apG`, mixes the two octonion halves = the doubling), ρ (`apR`, weight of the real part), and `λ = apZ@se` (0–1) which blends toward the exact zero-divisor pair `ZD`.
- `RT.am = [sMat(g ↦ s₁(s₂g)), sMat(g ↦ (s₁s₂)g)]` (`sMat` uses `SB`, four basis sedenions).
- Diagnostics `D.al`: `nz` (number of non-zero real components of Z, up to 32), `rh, la, ga, be`, `pn` = |s₁s₂|, `as` associator, `com` commutator, `dot`. `m8` = 16×16 left-multiplication matrix of `s₁`.
- `D.Z` has 8 complex components per object (the 16 complex in total).

## Controls
`apB`, `apG`, `apR`, `apZ` (moves toward a zero divisor). Presets: dense pair (all parts alive), mirror pair, heavy and light, rainbow sedenion.

## Scenes
26: zero divisors, approaching a zero divisor, mixing octonion halves, all 32 numbers alive, breathing real part, rainbow sedenion, plus Sandbox/Quantum/Geometry/Ambitwistor demos (n = 6 scattering equations). See [[Scene catalog]].

Previous step: [[Lab Octonion]]. Engine: [[Shared 4D field engine]].
