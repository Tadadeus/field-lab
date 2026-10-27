# Field Lab

An interactive maths and physics lab in a single HTML file: 4D twistor and algebra fields, lattice field theory, a particle universe, fluids, an equation runner and multivariable calculus. Vanilla JS, three.js r128, optional WebGPU. Built phone-first.

**Live:** https://claude.ai/artifact/KXkKrJx1MFN1ZxFWwWMJHW

## Layout
| folder | contents |
|---|---|
| `src/` | `orig.html` (base app) plus patch and part files; `build.py` assembles them |
| `dist/` | `index.html`, the built app (open it directly in a browser) |
| `tools/` | Playwright checks: contrast, targets, keyboard, error sweeps, maths diff, Potato perf |
| `docs/` | `DESIGN.md` (design system) and `vault/` (Obsidian notes, start at `00 Home.md`) |

## Build
```
cd src && python3 build.py
```
Writes `src/Field_Lab.html` (ignored) and `dist/index.html`.

## Rules
See `CLAUDE.md`.
