---
tags: [lab, eq, equations]
lab-id: eq
---
# Lab Law (`eq`): type an equation, watch it run

**Idea.** Write a law of physics or maths as text. The lab tokenises, parses and classifies it, then compiles it into a simulation.

## Pipeline
1. **Tokenizer and parser**: handles symbols, derivatives (`x'`, `x''`, `∂`), vectors, common functions and constants.
2. **`eqClassify`** decides the type from the form of the equation.
3. **Compile modes**
   - `ode`: one or a few ordinary differential equations, integrated with **RK4**.
   - `nb`: N-body systems (pairwise forces), integrated with **velocity Verlet**.
   - `pde`: partial differential equations on a grid, finite differences.
   - `math`: pure functions/curves/surfaces, evaluated and plotted.
4. Result is shown through the usual plane/chart/slice interface (`ENG.eq`), see [[Architecture]].

## Notes
- Numerical schemes are fixed per mode, so results are reproducible; step size follows the quality tier ([[Quality tiers]]).
- Presets include pendulum, Kepler, Lorenz, wave, heat, Schrödinger.
- Errors are shown as plain messages in the lab's status chip.

Related: [[Lab Calc]], [[Lab Fluid]], [[Scene catalog]].
