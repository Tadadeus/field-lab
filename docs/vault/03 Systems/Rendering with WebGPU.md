---
tags: [systems, rendering, webgpu]
---
# Rendering with WebGPU (optional)

Stored engine choice: `ENGK` = `bitwistor-engine` (see [[Storage keys]]). If the device has no WebGPU or init fails, the app stays on [[Rendering with WebGL]].

## The `GPU` object
- `gpuStart` requests adapter/device, `gpuBuild` creates pipelines and buffers, `gpuRender` draws a frame.
- WGSL shaders are the `WGSL_*` strings in the script.
- **HDR bloom** post-processing, **volume ray-march**, **GPU particles**, **GPU lines**, **GPU isosurface**, and the lattice compute step ([[Lab Lattice]]).
- Same data as the WebGL path (`FD`), so maths is not duplicated; only drawing and some compute move.

## Rules
- Maths and results must match the CPU/WebGL path.
- Potato tier never starts WebGPU post effects ([[Quality tiers]]).
- Phone note: bloom and volume are the costly parts; they drop first when `autoQ` lowers quality.
