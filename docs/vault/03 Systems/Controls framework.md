---
tags: [systems, ui, controls]
---
# Controls framework

- Controls are generated from tables (see [[Parameter reference]]): sliders, toggles, selects, chips, buttons.
- Every control keeps its **ID, class and data attributes** (project rule, [[Project rules]]); the build never renames them.
- Hit areas are ≥ 44 px on coarse pointers; focus, names and roles come from `ux.js` ([[Accessibility layer]]).
- Values change state `st`/`G`, mark it dirty for saving ([[State and persistence]]) and feed `FD` on the next frame ([[Frame loop]]).
- Sliders show value text in `.dtx`; open decision: a min/max/step/play drawer ([[Open decisions]]).
- Component conventions: [[Component conventions]].
