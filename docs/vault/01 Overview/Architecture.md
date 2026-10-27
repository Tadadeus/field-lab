---
tags: [overview, architecture]
---
# Architecture

## The file
`Field_Lab.html` is one document:
1. `<head>` with viewport meta and Google Fonts link, then **one large `<style>`** (about 100 KB after the design pass).
2. `<body>` markup of the shell: `section.panel.cmd` (controls), `section.stage` (the 3D view `#gl` with `canvas#c3`, WebGPU canvas `#c3g` added later), `section#views2` (slice viewer), `section.setp` (settings tabs), `section#cxMini` (Calc Lab mini views), `section#sandbox`, telemetry `section.sec`, `#reads`, `#info`, `.mats`, compare panel `#cmpP`.
3. `<script src="three.min.js r128">`.
4. **One `<script>` containing an IIFE `(()=>{ … })()`**. Nothing is global; all state is closed over. A second tiny script block after the IIFE adds the sliding selection indicator (`.sind`).

## Layers inside the IIFE (top to bottom)
| layer | what lives there | where to read |
|---|---|---|
| Core maths | complex/vector helpers, twistor maths, quaternion/4×4 matrices, marching tetrahedra | [[Shared 4D field engine]] |
| Model and state | `TWS/CAS/ALS` presets, `defCtx`, `st`, `G`, persistence | [[State and persistence]] |
| Scenes | the `SC` array and each lab's `SC.push(...)` | [[Scenes system]] |
| Algebra labs | the `ALG` table (`oc, su, cl, qb, se`) | [[Lab Octonion]] … [[Lab Sedenion]] |
| WebGL | `initGL`, particles, field lines, membranes, objects, trails, probes, `render3` | [[Rendering with WebGL]] |
| UI text & telemetry | `TH` (per-lab headings/footnotes), `infoHTML`, tiles, matrices | [[Controls framework]] |
| Tabs | Quantum / Geometry / Physics add-ons, sandbox entities, slice viewer | [[Quantum Geometry Physics tabs]], [[Sandbox objects and probes]] |
| WebGPU | WGSL shaders, GPU particles/lines/isosurface/volume/post-processing | [[Rendering with WebGPU]] |
| Engines | Lattice, Universe, Law, Fluid, Calc (each registers in `ENG`) | the five lab notes |
| UI systems | history, undo, share, compare, pins, settings, sound, tour, help | [[Systems overview]] |
| Patches | colorbars (`cb.js`), quality (`q.js`), accessibility (`ux.js`) | [[Colormaps and colorbars]], [[Quality tiers]], [[Accessibility layer]] |
| Shell | controls framework (`CTL`, `mkCtl`, `spec*`), `onCtx`, `frame()` | [[Frame loop]] |

## The engine contract (`ENG`)
The first seven labs are drawn by the *main* 3D pipeline. The other five (`la, un, eq, fl, cx`) each register an object in `ENG[labId]` with these hooks (some optional):

| hook | job |
|---|---|
| `render3(rdt, sdt)` | advance the solver and update the 3D objects |
| `hide()` | hide that engine's 3D objects when another lab is active (`engHide`) |
| `bg(sdt)` | keep running when the 3D view is off-screen |
| `plane()`, `chart()`, `slice()` | draw the 2D plane view, the chart, the slice view |
| `svcap()`, `chip()` | caption of the slice view, text of the engine badge |

`render3` in the main pipeline starts with `const EN=ENG[st.alg]; engHide(st.alg); if(EN){EN.render3(rdt,sdt);return}`. This is how one canvas serves 12 labs. Details: [[Frame loop]].

## Contexts and the active lab
Each lab and dimension (3D or 4D) has its own saved settings object, a *context*, keyed `tw3, tw4, ca3, ca4, oc3, …`. The active one is `st`. `st.th` is `'tw'` or `'ca'` (which base engine), and `st.alg` is the lab id for the algebra/engine labs (`''` for tw/ca). `TK()` returns the current lab key. See [[State and persistence]].

## Patching style
The project grew by layers. Later code often *wraps* earlier functions:
```js
const th0 = thApply; thApply = function(){ th0.apply(this, arguments); tcSet(); … };
```
Wrappers and suffix names (`specLat0`, `specUniH`, `latFrameC`) mark features added on top of earlier ones. Read them in file order. See [[Naming conventions]].
