---
tags: [design, color, theme]
---
# Light theme and data colour

- Plot areas are **always dark** in both themes: `--dk-bg` #0d1013, `--dk-fg` #dfe3e8, `--dk-dim`, `--dk-faint`.
- `CK` (canvas kit) reads these once per theme change: `CK.fg/dim/faint/bg`, `CK.i(alpha)`, `CK.ax`, `CK.pos`, `CK.neg`. Drawing code holds no hex literals.
- **Axes** `AXC`: x #ff6b6b, y #7dff8a, z #6bb8ff, w #c9a6ff, same everywhere.
- **Lab pairs**: `--Z1/--Z2` default dark #2fd8f2 / #ff6b2c, light #08718a / #b8410f; each lab overrides via `--lab-<id>-1/2` (e.g. `--lab-qb-1` #5ab8ff / #1f78c2). Labs never recolour the chrome.
- **`.dtx`**: data colour as text. Set `--c`; the theme clamps lightness: dark `oklch(from var(--c) max(l,.72) c h)`, light `min(l,.44)`, fallback `color-mix(… 45%, #000)`.
- Used for axis chips, plane chips, `.h8` matrix headers, `.ups` particle symbols, `h3.sph`, legend `em`.
- **Colormaps**: sequential viridis (cividis, classic selectable); cyclic OKLCH ring; diverging `eqCm('div')` blue-dark-red, pivot 0. Setting `APP.cmap`. See [[Colormaps and colorbars]].
- Open: should "positive" turn orange? ([[Open decisions]])
