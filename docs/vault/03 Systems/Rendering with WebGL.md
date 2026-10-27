---
tags: [systems, rendering, webgl]
---
# Rendering with WebGL (three.js r128)

The default and fallback renderer.

- `render3(...)` begins `EN=ENG[st.alg]; engHide(st.alg); if(EN){EN.render3(...);return}`: algebra labs fall through to the shared 4D path, engine labs ([[Lab Lattice]], [[Lab Universe]], [[Lab Fluid]], [[Lab Law]], [[Lab Calc]]) draw themselves.
- **Isosurface**: marching tetrahedra `mtRun` over a sampled grid; normals from the field gradient.
- **Lines and membranes** are rebuilt in a 3-phase rotation (a third of the geometry per frame) so frame time stays flat.
- **4D → 3D** projection: `V4S` stereographic, `V4e` perspective; rotation by left and right isoclinic quaternions (`rotLR`). See [[Shared 4D field engine]].
- Particles are `THREE.Points`; instance counts follow [[Quality tiers]].
- Colours come from the canvas colour kit `CK` ([[Light theme and data colour]]).

Faster path when available: [[Rendering with WebGPU]]. Frame order: [[Frame loop]].
