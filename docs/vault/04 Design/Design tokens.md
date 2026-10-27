---
tags: [design, tokens]
---
# Design tokens

All tokens live in one dark `:root` block plus one `:root[data-theme=light]` override. Nothing else may define a colour, size, space, radius, duration or z-index. They reach code through `ds.TOKENS`, `sys.css` and `CK` (see [[Light theme and data colour]]).

## Surfaces (dark / light)
| token | dark | light | use |
|---|---|---|---|
| `--well` | #0d1013 | #ffffff | wells, fields |
| `--bg` | #121519 | #e8ebee | page |
| `--panel` | #171b20 | #f6f7f9 | panels |
| `--panel2` | #1c2127 | #eef1f4 | nested groups |
| `--ctl` | #21272e | #ffffff | controls |
| `--elev` | #262d35 | #ffffff | popovers, toasts |
| `--line` / `--line2` | #2a2f35 / #3a414a | #d7dce1 / #b4bcc5 | dividers / control borders |

Depth by lightness steps (2–3 % L); shadows only on floating layers (`--sh-1` menus, `--sh-2` dialogs). No backdrop-filter.

## Text and accent
`--fg` #dfe3e8 / #161b21 · `--dim` #a8b1bb / #46505b · `--faint` #8d97a2 / #5b6570 · `--acc` #7fb6c9 / #1d6a82 (**one** desaturated steel-cyan: selection, focus, active tab, primary action) · `--track` #707984 / #78818b. Text ≥ 4.5:1, non-text ≥ 3:1 on every surface.

## Semantic
`--ok` #5fc98a/#16733d · `--bad` #ef7a6a/#b2342a · `--warn` #e3b45a/#8a5f00 · `--rec` · `--star`. Always paired with a glyph or word.

## Type
Families: `--ui` IBM Plex Sans Condensed, `--prose` IBM Plex Sans, `--mono` JetBrains Mono, `--math` STIX Two. Sizes `--t-1…6` = 11, 12, 13, 16, 19, 24 px (nothing below 11, canvas included). Line heights 1.25 / 1.5.

## Space, radius, motion, z
- Space base 4 px: `--s-h 2 · 1:4 · 2:8 · 3:12 · 4:16 · 6:24 · 8:32 · 12:48`.
- Radius `--r-1` 2, `--r-2` 4, `--r-3` 8.
- Motion `--d-1…4` = 120/160/200/250 ms (250 never exceeded); `--ease-out` cubic-bezier(.23,1,.32,1), `--ease-in-out` cubic-bezier(.77,0,.175,1). See [[Motion]].
- z: `--z-1/2/3`, sticky 10, float 20, modal 30, top 40.

Next: [[Component conventions]].
