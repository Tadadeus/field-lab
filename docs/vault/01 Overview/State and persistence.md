---
tags: [overview, state]
---
# State and persistence

## The three state objects
| name | what | defined by |
|---|---|---|
| `G` | global: `{theory, dim, ctx, tab}`. `theory` = active lab id, `dim` = 3 or 4, `ctx` = map of contexts, `tab` = open settings tab | `const G=…` |
| `st` | the **active context** (alias of `G.ctx[theory+dim]`) | `getCtx(th, dim)` |
| `RT` | **runtime only**, never saved: clocks, FPS, `Z0`/`C0` (built twistors/branes), quality level, `visible`, `am/ab/tb` (algebra matrices) | `const RT=…` |
| `FD` | the current **frame data** returned by `twFrame()` or `caFrame()` (fields, anchors, matrices) | recomputed every frame |

## A context (`defCtx(th, dim)`)
One object per lab per dimension, keys such as `tw3, tw4, ca3, ca4, oc3, oc4, su3…`. Fields of `st` (from the live app):

`th, alg, ap, dim, mode, v, mph, amp, axKey, axT, axP, axV, path, beta, lr, lb, spd, rev, play, state, Pm, scene, fv, fr, fl, ob, vw, v4, vis, yaw, pitch, lat, probes, ents, sel, qm, geo, ph` plus lab-specific ones added by `*Ok()` functions: `uni` (Universe), `eq`, `flu` (Fluid), `cx`.

| key | meaning |
|---|---|
| `th` | base engine: `'tw'` or `'ca'` |
| `alg` | lab id for algebra/engine labs; `''` for tw and ca |
| `ap` | algebra-pair parameters (`beta, kap, eta, zeta, nu, mu, psi, gam, zd, rho`) |
| `mode` | motion mode: rot / boost / dil / conf / mix / evo / all |
| `v`, `mph`, `amp` | current value, phase and amplitude of each transformation |
| `axKey, axT, axP, axV` | rotation axis choice and angles/vector |
| `path` | rotation path style (wobble, tumble, liss, gyro, eight, precess, random, …) |
| `beta, lr, lb` | mix phase, left↔right balance, balance slider |
| `spd, rev, play` | simulation speed, reverse, playing |
| `state`, `Pm`, `scene` | preset key within the lab, edited parameters per preset, scene key |
| `fv`, `fr` | values and rhythm (waveform, rates) of the "all at once" motion |
| `fl` | field display: sources, lines, colours, particle counts, membrane level… |
| `ob` | the two objects' shape, size, spin, material, route |
| `vw` | view: slice settings, camera distance/FOV, box, labels, trails, probes, fog |
| `v4` | 4D view: embedding, projection, angles and spins, gizmo, slab |
| `vis` | visual: palette, background, glow, bloom, exposure, quality override, GPU multipliers |
| `yaw, pitch` | camera angles |
| `probes` | up to 4 dropped probe points |
| `ents`, `sel` | sandbox entities and the selected id ([[Sandbox objects and probes]]) |
| `qm, geo, ph` | Quantum / Geometry / Physics tab settings ([[Quantum Geometry Physics tabs]]) |

## Saving
- Key `bitwistor-lab-v5` (`SKEY`): JSON `{v:5, theory, dim, tab, ctx}`.
- `mark()` sets `dirty=true`; a `setInterval` every 1.5 s calls `saveAll()` if dirty; `pagehide` saves too.
- `loadAll()` validates everything: unknown labs are ignored, contexts are **deep-merged** into fresh defaults (`deepMerge`), so adding new settings never breaks old saves, and presets `Pm` must pass `validP`.
- Switching 3D↔4D copies the other dimension's context if the target has none (`getCtx`).

Other persisted values (settings, favourites, pins, cameras, tour flag) are listed in [[Storage keys]].

## Rules for new state
1. Add the default in `defCtx` (or the lab's `*Def()` with an `*Ok()` repair function).
2. Anything that must survive reload goes inside `st`; anything per-frame goes in `RT`.
3. Call `mark()` after changing saved state.
4. Don't store functions or DOM objects in `st`: it is `JSON.stringify`-ed for saving, undo ([[Undo and redo]]), sharing ([[Share codes]]) and compare ([[Compare A-B]]).
