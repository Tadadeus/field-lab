---
tags: [systems, performance]
---
# Quality tiers (`QOPT`)

| id | name | description (from the app) |
|---|---|---|
| auto | Auto | Adapts to this device and lowers detail by itself when frames get slow. |
| potato | Potato | Fastest: coarse grids and meshes, ¾× pixels in 3D, fewest particles. |
| low | Low | Phones and older laptops: 1× pixels, light grids. |
| med | Medium | Balanced: 1.5× pixels, medium grids and particle counts. |
| high | High | Sharp: 2× pixels, full grids, meshes and particle counts. |
| ultra | Ultra | Smoothest: up to 3× supersampled pixels, 1.5× finer grids, meshes and images. |
| max | Maximum | Best possible: up to 4× supersampled pixels, 2× finer grids, meshes and images, most particles. For 2K/4K screens on fast devices. |

- Stored as `APP.perf`. `QS(a,b)` and `QLV` scale sizes per tier (e.g. Fluid grid 128…576, Universe particles).
- **Auto** watches frame time and lowers `RT.qlev` when slow.
- Rule: Potato must never get heavier ([[Project rules]], checked by `potperf.py` in [[Verification tools]]).
- Switch in the app popover and the quality control (`q.js`).
