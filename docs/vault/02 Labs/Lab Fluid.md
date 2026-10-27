---
tags: [lab, fl, fluid]
lab-id: fl
---
# Lab Fluid (`fl`): wind tunnel and smoke

Two solvers (`FLM`): **`lbm`** "Wind tunnel (lattice Boltzmann)" and **`smoke`** "Smoke and heat (stable fluids)".

## Wind tunnel: D2Q9 lattice Boltzmann (`flLbmStep`)
- Distributions on 9 velocities, BGK collision with relaxation time from Re (`flTau`), streaming, bounce-back walls (`flBound`).
- Settings (`flDef`): inflow `u0`, Reynolds `re`, obstacle `obs` (cylinder by default), size/angle/position, Smagorinsky `smag`, boundary `bc` (tunnel), lid speed, shear.
- Readouts: vorticity `flVort`, Strouhal number `flStrouhal`, flow rate, mass `flMass`.

## Smoke and heat: stable fluids (`flSmokeStep`)
Semi-Lagrangian advection (`flAdvect`), pressure projection (`flProject`), buoyancy, heat, dye, vorticity confinement `vc`, dissipation, sources (plume…).

## Tools
Draw on the view with `flTool`: wall, erase, stir and more; brush size `brush`. Tracers (`flTrSpawn / flTrStep`), arrows, stripes.

## Scenes (28)
Kármán street, slow/fast flow, square cylinder, flat plate, wing at 6° and 22° (stall), two cylinders, backward step, Poiseuille channel, lid-driven cavity, Kelvin–Helmholtz, Taylor–Green, porous rock, city blocks, Venturi, baffles, empty tunnel, smoke plume, candle, Rayleigh–Bénard, Rayleigh–Taylor, vortex pair, smoke jet, stir the tea, Tesla valve both ways. See [[Scene catalog]].

Grid width follows quality: 128 / 160 / 224 / 320 / 448 / 576 (`flCap`, [[Quality tiers]]). Engine `ENG.fl` ([[Architecture]]); colorbar on the top view ([[Colormaps and colorbars]]).
