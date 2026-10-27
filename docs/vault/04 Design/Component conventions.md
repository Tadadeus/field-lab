---
tags: [design, components]
---
# Component conventions

**Base rules.** States: rest, hover (only in `@media (hover:hover) and (pointer:fine)`), pressed, selected. Focus: 2 px `--acc` ring, 2 px offset. Disabled: opacity .45. Visual min 24 px; on `pointer:coarse` the hit area grows to 44 px via `::after`.

| # | component | key rules |
|---|---|---|
| 3.1 | Panel `.panel` | `--panel`, 1 px `--line`, `--r-2`, 28 px header; no nested panels |
| 3.2 | Section header `h3.sph`, `details>summary` | caret, title 13/600, whole row toggles |
| 3.3 | Button `.act` | sentence-case verb + object; at most one primary per group |
| 3.4 | Icon button `.icon`, `.ib` | 28×26 visual, `aria-label` required, grouped `.btns`, `.qfg` |
| 3.5 | Chip `.chip` | 24 px, `aria-pressed`, selected = `--sel` + `--selb` |
| 3.6 | Segmented `.seg`, `.apseg`, `.modes` | radiogroup/tablist, sliding `.sind` (scaleX) |
| 3.7 | Slider `label.sl` | label, 4 px track, editable number + unit; arrows, Shift ×10, PgUp/PgDn, Home/End. Drawer not built ([[Open decisions]]) |
| 3.8 | Select | native, 16 px text on touch |
| 3.9 | Popover `.apop`, `.qpop`, `.secm`, `.bmpop` | grows from trigger 160 ms; focus in on open; Esc returns focus |
| 3.10 | Telemetry tile `.tile`, `.rv` | label above value, tabular, fixed ch width |
| 3.11 | Legend `#legend`, `.rh` | swatch, name, symbol with `.dtx` |
| 3.12 | Matrix grid `.mx8`, `.kv` | `.dtx` headers, mono values |
| 3.13 | Colorbar | see [[Colormaps and colorbars]] |
| 3.14 | Caption `figcaption`, `.cap`, `.seccap` | 11 px faint, one line, also canvas `aria-label` |
| 3.15 | Toast `.toast` | `role=status`, "[What happened]. [Next step].", 4 s |
| 3.16 | Engine badge `.engtag` | 11 px mono, states fact and reason |

Tokens: [[Design tokens]]. Motion: [[Motion]]. Accessibility: [[Accessibility layer]].
