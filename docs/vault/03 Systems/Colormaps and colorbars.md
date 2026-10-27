---
tags: [systems, color]
---
# Colormaps and colorbars

- Field values map through colormaps to RGB; the canvas colour kit `CK` ([[Light theme and data colour]]) supplies theme-aware colours for canvases.
- `cb.js` draws the **colorbar**: gradient, min/max labels and units, redrawn when the map or range changes.
- Data text uses the `.dtx` class so numbers stay readable in both themes.
- Colour is never the only carrier of meaning: values are also shown as numbers in readouts ([[Accessibility layer]]).
- Used by [[Rendering with WebGL]], [[Rendering with WebGPU]], [[Lab Lattice]], [[Lab Fluid]], [[Lab Calc]].
