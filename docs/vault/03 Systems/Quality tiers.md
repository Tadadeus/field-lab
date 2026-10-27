---
tags: [systems, performance]
---
# Quality tiers

Seven options in `QOPT` / `PERFV`: **auto, potato, low, med, high, ultra, max** (6 fixed tiers plus auto).

- **auto** (`autoQ`): watches frame time (`rdt` clamped to 0.05 s) and moves the tier down or up.
- **potato**: lowest cost; **must never get heavier** after any change (project rule, see [[Project rules]]; measured by `potperf.py`, see [[Verification tools]]).
- Each tier sets: grid/particle counts, substeps, pixel ratio, post effects, GPU features ([[Rendering with WebGPU]]).
- The switch lives in the app popover ([[Settings and app popover]]) and in the quality control built in `q.js`.
- Saved in state ([[State and persistence]]).

Descriptions shown to the user come from `QOPT` and are listed in [[Parameter reference]].
