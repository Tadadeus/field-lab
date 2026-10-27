---
tags: [lab, oc, algebra]
lab-id: oc
---
# Lab Octonion (`oc`): non-associative algebra

**Object.** A *bioctonion* `Z = X + iY` with `X, Y ∈ 𝕆` (the 8-dimensional octonions): 8 complex components, 16 real numbers, in one object. Octonion multiplication is neither commutative nor associative: `(ab)c ≠ a(bc)`.

**Picture.** Split by Cayley–Dickson into halves `A + Bℓ` (ℍ ⊕ ℍℓ). Stream 1 follows `U₁(U₂∇f)`; stream 2 follows `(U₁U₂)∇f`: the *same product bracketed two ways*. Where the two streams part, the **associator** is at work. `U_k = cos β·u_k + sin β·w_k·ℓ`; at `β = 0` the units stay inside the quaternions ℍ and everything associates.

## Code (`ALG.oc.post`)
- Cayley–Dickson product `omul(x,y)` = `(a,b)(c,d) = (ac − d̄b, da + bc̄)` on pairs of quaternions (`qmu`, `qcj`).
- `U[k] = [0, cosβ·n, sinβ·(cosχ, sinχ·e2)]` built per source from its axis `n`, frame `e2` and phase χ. `β = clamp(ap.beta + C.b·45, 0, 90)°`.
- `RT.am[0] = hMat(g ↦ U₁(U₂ g))`, `RT.am[1] = hMat(g ↦ (U₁U₂) g)`: 4×4 matrices acting on the gradient (`hMat` evaluates a map on the 4 basis vectors `HB4`).
- Diagnostics in `D.al`: `be` (β), `dot` (⟨U₁,U₂⟩), `com` (commutator size), `as` (associator size, √(Σ(am₀−am₁)²/4)), `zz` (|Z·Z|), `nx, ny` (norms of X and Y).
- 8×8 matrix panel `m8` = left-multiplication matrix `L₁L₂` over the octonion basis `OB`.

## Controls
`apB` tilt out of ℍ (0–90°): "At 0 everything associates; as β grows the associator (ab)c − a(bc) appears." Preset states (`ALS.oc`): halves A and Bℓ apart, halves overlapping, diagonal in 4D, parallel units.

## Scenes
20: inside the quaternions (associative), leaving ℍ, fully octonionic units, non-associativity sweep, triality phase, parallel units split by ℓ, Spin(7), plus Quantum / Geometry / Physics tab demos on the bioctonions. See [[Scene catalog]].

Engine: [[Shared 4D field engine]]. Next step up: [[Lab Sedenion]] (one more doubling).
