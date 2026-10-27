---
tags: [systems, rendering, webgpu]
---
# Rendering with WebGPU (optional)

Engine choice stored in `bitwistor-engine` (`ENGK`); `GPU.eng === 'gl'` forces WebGL. If `navigator.gpu` or an adapter is missing, `gpuStart` fails and the app stays on [[Rendering with WebGL]]; the engine badge (`.engtag`, `gpuChip`) says why.

## Parts of the `GPU` object
- Start and build: `gpuStart` (high-performance adapter), `gpuBuild`, `gpu2Build`; draw: `gpuRender`.
- Particles `gpuPart*`, lines `gpuLines*`, isosurface `gpuIso*`, slices `gpuSlice*`, volume `gpuVol*`.
- Post-processing `gpuPost` (HDR bloom with mip chain `gpuPostMips`); only runs when wanted (`gpuPostWant`: bloom > 0, or volume on).
- Lattice compute `latGpu*` ([[Lab Lattice]]); Universe gets up to 16384 particles.
- Shaders are the `WGSL_*` strings; uniforms are packed by the `GU` index table.

Maths matches the CPU path; WebGPU only moves drawing and some compute.
