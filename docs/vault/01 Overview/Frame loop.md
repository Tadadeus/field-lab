---
tags: [overview, runtime]
---
# Frame loop

`requestAnimationFrame(frame)` runs everything. Order inside `frame(now)`:

1. **Delta time** `rdt = min(.05, (now-last)/1000)`. Smoothed FPS: `RT.fps = RT.fps*.92 + (1/rdt)*.08`.
2. **Auto quality** `autoQ(rdt)` ([[Quality tiers]]).
3. **Simulation delta** `sdt = rdt * st.spd * (st.rev ? -1 : 1)` while playing; when paused and the user presses → / ←, `RT.stepOnce` gives one step of `spd/30`.
4. If `sdt != 0`: `advance(sdt)` (advances the motion mode, see [[Shared 4D field engine]]) and `syncSlider()`.
5. **Frame data** `FD = st.th==='ca' ? caFrame() : twFrame()`.
6. **Render** if the 3D view is on screen (`RT.visible`, set by an IntersectionObserver): `render3(rdt, sdt)`. Otherwise run only the cheap updates (`qmFrame, geoFrame, phFrame`, plus the engine's `bg(sdt)` so Universe/Lattice keep their physics going).
7. Object speed estimates `RT.ov` (for telemetry).
8. Complex-plane trails if the plane view is open (`WP>0`, then `drawPlane()`).
9. **Throttled UI**: `updateDom()` every 66 ms, `telemetry()` every 125 ms, `drawSphere()` every 40 ms, `views()` (slice viewer + mini views) every frame but each view skips itself when off-screen.

## `render3` (WebGL path)
```
EN = ENG[st.alg]; engHide(st.alg)
if EN: EN.render3(rdt, sdt); return          // Lattice, Universe, Law, Fluid, Calc
qmFrame(); geoFrame(); phFrame(sdt); v4Setup(rdt); updCam(rdt); applyVis()
particles (psStep) · field lines · membranes · grid · rings · objects · pair · trails · probes · box · labels · gizmo · sandbox entities
if GPU.on → gpuRender(sdt)  else  GL.ren.render(scene, camera)
snapshot if requested
```
Lines and membranes are rebuilt in a rotation (`GL.fc++ % 3`): lines on phase 0, membrane mesh on phase 1, to spread cost across frames. Details in [[Rendering with WebGL]].

## Input
Pointer events on `#gl`: one pointer drags the camera (yaw/pitch); with Shift or the "drag w" option in 4D it rotates the xw/yw planes; two pointers pinch the distance (3–18 units); wheel zooms; a single tap probes or picks; a double tap recentres (`viewReset`). Keyboard: [[Keyboard shortcuts]].

## Start-up order (end of the script)
`loadAll(); st = getCtx(G.theory, G.dim); GL = initGL(); gpuStart(); onCtx(); fitP(); requestAnimationFrame(frame)`, then listeners for reset, theme tabs, and **scene application** for labs with engines (`applyScene(st.scene)` once, guarded so saved settings are not overwritten).

## Why dt is clamped
`rdt` is capped at 50 ms so a tab returning from the background or a slow device never makes a physics step explode (the lattice stability limit in 3D is dt < 1/√3).
