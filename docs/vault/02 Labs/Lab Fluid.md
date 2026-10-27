---
tags: [lab, fl, fluid]
lab-id: fl
---
# Lab Fluid (`fl`): lattice Boltzmann and smoke

Two solvers in one lab.

## D2Q9 lattice Boltzmann (`flLbmStep`)
- 9 discrete velocities on a 2D grid; collide (BGK relaxation to equilibrium, relaxation time sets viscosity) then stream.
- Obstacles use bounce-back; inflow/outflow set the boundary velocity.
- Outputs: velocity, vorticity, pressure (density), shown as colour field and streaklines. Re = U·L/ν is displayed.
- Classic scenes: flow past a cylinder (von Kármán street), channel, lid-driven cavity.

## Stable-fluids smoke and heat (`flSmokeStep`)
- Semi-Lagrangian advection, pressure projection (Jacobi/Gauss–Seidel), buoyancy from temperature/density, dissipation.
- Interactive: tap/drag injects smoke and velocity.

## Code
- Registered as `ENG.fl` (`render3, hide, bg, plane, chart, slice, svcap, chip`), see [[Architecture]].
- Wrapper hot-swap on `ENG.fl.plane` is used by the design layer; keep it intact.
- Quality tier sets grid size and substeps ([[Quality tiers]]).
- Colourmaps and bars: [[Colormaps and colorbars]].

Related: [[Lab Law]] (PDE mode can solve fluid-like equations), [[Lab Calc]] (vector fields).
