---
tags: [lab, eq, equations]
lab-id: eq
---
# Lab Law (`eq`): type equations, watch them run

## Pipeline
1. `eqTok` / `eqParse`: text to expression trees. `eqNorm` normalises symbols; `#` or `//` starts a comment.
2. `eqClassify(src)`: each line must look like `name = expression`, `x' = …` / `x'' = …`, or `u_t = …`; it matches the patterns `EQRX` (derivatives, initial values, ranges, definitions). Otherwise it throws "write it as name = expression, x' = … or u_t = …".
3. `eqCompile` picks a mode:
   - **ode** (`eqCompileODE`, `eqOdeAdvance`): ordinary equations, Runge–Kutta (`eqRk`), step `odt`.
   - **nb** (`eqCompileNB`, `eqNbAdvance`): N bodies with pair forces, velocity Verlet (half kick, drift, bounds, forces, half kick), step `ndt`.
   - **pde** (`eqCompilePDE`, `eqPdeStep`): fields on a grid, finite differences, first- or second-order in time, Euler or RK2 (`gmeth`).
   - **math** (`eqCompileMath`): functions, surfaces and complex maps, no time stepping.
4. All modes cap work per frame and set `EQ.slow` when they can't keep up.

## Scenes (48)
Lorenz, Rössler, Thomas, Aizawa, Chua, Van der Pol, Lotka–Volterra, Duffing, double pendulum, Kepler, Hénon–Heiles, SIR, Brusselator; N-body: collapsing cloud, disk galaxy, figure-eight three bodies, toy solar system, 1/r³ gravity, Lennard-Jones, melting crystal, plasma, Yukawa, springs, Brownian motion; PDE: heat, pond waves, double slit, Gray–Scott, spiral waves, quantum double slit, sine-Gordon, Cahn–Hilliard, Swift–Hohenberg, drum; math: monkey saddle, contours, sombrero, roots of unity, zeros and poles, exp(1/z), Möbius map, Riemann zeta. See [[Scene catalog]].

Engine `ENG.eq` ([[Architecture]]). Related: [[Lab Calc]], [[Lab Fluid]].
