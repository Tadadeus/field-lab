---
tags: [lab, qb, quantum]
lab-id: qb
---
# Lab Qubits (`qb`): three qubits

**Object.** A three-qubit state `|ψ⟩ ∈ (ℂ²)^{⊗3}` has 2·2·2 = 8 complex amplitudes `ψ_abc` (16 real numbers): ℂ⁸ again, but as a **tensor product** (a tri-object instead of a bi-object). Pauli operators don't commute, and three qubits can be entangled in two inequivalent ways: **GHZ** and **W**.

**Picture.** Qubits A and B sit at their **Bloch vectors**. As they entangle, their Bloch vectors **shrink** and their throats **fuse** into one membrane. The shrinking vector length `l` scales the source charge (`m = mb·(0.35 + 0.65·l)`).

## Code (`ALG.qb.pre` and `.post`)
Because the state changes, this lab has a `pre(o)` hook that runs *before* the frame is built:
- `psi0(key)`: start states `ghz, w, plus (|+++⟩), bell, one, p00, …` as a 16-float vector (8 complex).
- Gates on the amplitude vector `p`: `qg1(p,q,U)` single-qubit unitary, `xyg(p,q1,q2,φ)` XY (iSWAP-like) exchange between two qubits, `czg(p,φ)` controlled phase, `cnotg(p,t)` fractional CNOT.
- `ru(n, θ)` = SU(2) rotation about axis n (used for the rotation mode).
- Modes map to circuits: `evo` = XY chain evolution of the whole register, `rot` = rotate all qubits about the axis, `boost`/`dil`/`conf`/`mix` = other gate combinations, `all` = the whole circuit.
- `bloch(p,q)` returns the reduced Bloch vector of qubit q; `RT.qr` holds all three.
- `tangle3(p)` = Coffman–Kundu–Wootters 3-tangle `τ = 4|d₁ − 2d₂ + 4d₃|` (genuine three-way entanglement).
- `post` sets `D.Z` from the amplitudes, `D.al` = `{l, tau, share, zz, fg, fw, E, m8, rC}` where `share = 1 − l₀² − τ` and `fg, fw` are overlaps with GHZ and W. `m8` = real part of the density matrix `ψψ†` (8×8).

## Controls
State chooser `ap.psi`; presets: A and B on a line, close, separated along w. Entanglement tube strength `apK`.

## Scenes
21: GHZ, W, product |000⟩, CNOT Bell pair, |+++⟩ under controlled phase, XY spin chain, iSWAP, Hadamard, whole circuit, plus Quantum / Geometry / Soliton / Lattice demos. See [[Scene catalog]].

Engine: [[Shared 4D field engine]]. Many-body version with exact diagonalisation: spin chain in [[Lab Lattice]].
