---
tags: [lab, ca]
lab-id: ca
---
# Lab Courant (`ca`): generalized geometry

**Idea.** Instead of vectors alone, generalized geometry uses the **doubled bundle T ⊕ T\*** (vectors plus 1-forms) over ℝ⁴, with the pairing `⟨X+ξ, Y+η⟩ = ½(ξ(Y)+η(X))` of signature (4,4). A **bi-Courant** pair `(C₁, C₂)` consists of two generalized complex structures of a generalized-Kähler pair. The physical picture is a **pair of NS5-brane throats**:

- metric `g = f·δ`, 3-form flux `H = ⋆df`, with `f = 1 + Σ m/(r² + a²)` (`fAt`),
- left and right complex structures `I± = L_u, R_v` (left and right quaternion multiplication, `Lmat`, `Rmat`),
- particles follow the chiral currents `I±∇f`,
- the membrane is a throat `f = const`,
- the dual grid is the T\* half of the doubled space.

## Code
- Sources: `cpar(c, m, a, th, ph, chi)`; `buildCa(P)` makes the runtime source with axis `n`, frame `e2, e3`, and the quaternion that gives the two chiral directions.
- `caCompose()` builds `R` (rotation, left×right via `rotLR` or `rot4` in 4D), `SD` (stretch × scale), `b` (B-field), `phi` (T-duality mixing), `w0`, `te`.
- `caFrame()` computes for each source: the transformed centre `cen`, axis, and the generalized vector `X + ξ` split into `u = (X+ξ)/2` and `w = (X−ξ)/2`; the B-transform `e^B: X+ξ ↦ X+ξ+ι_X B` via `Bmat` and `iB`; the T-duality angle mixes via `Jm`. Output `D.Z` (4 complex components per source), `D.inv` (pairings `p11, p22, p12`, Gram).
- `fCa(k,x,y,z,w)`: density `rho = 2 m r/(r²+a²)²`, phase from the frame, direction `d` = `A·(chiral current)`.
- Dual grid (`fl.dual_on`) draws the T\* half; `st.fl.mSrc==='H'` switches the membrane to the 3-form flux magnitude.

## Controls specific to this lab
B-field `gB`, dual-grid alpha `fdga`, left/right balance `lr`, T-duality (mix angle `amA`), fly-through (slice sweep). See [[Parameter reference]].

## Scenes
43: two NS5 throats, single throat (SU(2) WZW), throats merging, brane fly-through, left and right chiral currents, left-only rotation (isoclinic), B-field shear, T-duality rotation, R↔1/R dilation of the doubled lattice, GL(4) stretch, H-flux lines, instanton-cored/thin/heavy-and-light branes, opposite/orthogonal chiral axes, tilted pair, nebula cinema; 4D: two throats in ℝ⁴, Hopf flows, slice sweep, tesseract spin. See [[Scene catalog]].

Shared machinery: [[Shared 4D field engine]]. Algebra labs reuse this lab as their base: [[Lab Octonion]], [[Lab su3]], [[Lab Clifford]], [[Lab Qubits]], [[Lab Sedenion]].
