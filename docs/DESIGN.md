# Field Lab — DESIGN.md

The design system for Field Lab, a single-file maths and physics lab (vanilla JS, three.js r128, optional WebGPU). Its main audience uses it on a phone (~390 px wide), so it is designed mobile-first and then widened.

**Scope.** These rules cover the UI chrome only: panels, controls, type, colour, motion and states.

What stays exactly as it is:
- **Simulations.** Their maths, physics, computation, animation paths, speeds and timing are content and stay byte-for-byte identical.
- **Hooks.** Every ID, class and data attribute keeps its name.
- **Features.** Every feature, control, chart, view, shortcut, setting, tour step, glossary entry, sound and quality level stays.

Two constraints apply to everything below:
- **No new weight.** No new dependencies and no new font families. Potato must never get heavier.
- **Where the tokens live.** All tokens sit in one `:root` block (dark), with one `:root[data-theme=light]` override. Nothing else may define a colour, size, space, radius, duration or z-index. In code these values arrive through `ds.TOKENS`, `sys.css` and `CK` (canvas chrome).

---

## 1. Colour

### 1.1 Surfaces (elevation ramp)
| Token | Dark | Light | Use |
|---|---|---|---|
| `--well` | `#0d1013` | `#ffffff` | inset wells, code, fields |
| `--bg` | `#121519` | `#e8ebee` | page |
| `--panel` | `#171b20` | `#f6f7f9` | panels, sections |
| `--panel2` | `#1c2127` | `#eef1f4` | nested groups, segmented tracks |
| `--ctl` (`--bg2`) | `#21272e` | `#ffffff` | controls at rest |
| `--elev` | `#262d35` | `#ffffff` | popovers, menus, toasts |
| `--line` | `#2a2f35` | `#d7dce1` | dividers |
| `--line2` | `#3a414a` | `#b4bcc5` | control borders |

**How depth is shown.** Depth comes from lightness steps of about 2–3 % L, never from shadows on large surfaces. Only floating layers get shadows: `--sh-1` for menus and `--sh-2` for dialogs. The app has no backdrop-filter anywhere.

### 1.2 Text and accent: contrast on every surface (WCAG 2.2)
Each ratio is measured against `bg / panel / panel2 / ctl / elev`. Text needs 4.5:1 and non-text UI needs 3:1.

| Token | Dark | Dark ratios | Light | Light ratios |
|---|---|---|---|---|
| `--fg` | `#dfe3e8` | 14.2 · 13.4 · 12.6 · 11.7 · 10.8 | `#161b21` | 14.5 · 16.2 · 15.3 · 17.3 · 17.3 |
| `--dim` | `#a8b1bb` | 8.4 · 8.0 · 7.5 · 6.9 · 6.4 | `#46505b` | 6.9 · 7.7 · 7.2 · 8.2 · 8.2 |
| `--faint` | `#8d97a2` | 6.2 · 5.8 · 5.5 · 5.1 · 4.7 | `#5b6570` | 5.0 · 5.5 · 5.2 · 5.9 · 5.9 |
| `--acc` | `#7fb6c9` | 8.2 · 7.8 · 7.3 · 6.8 · 6.3 | `#1d6a82` | 5.1 · 5.7 · 5.4 · 6.1 · 6.1 |
| `--track` (non-text) | `#707984` | 4.2 · 3.9 · 3.7 · 3.4 · 3.2 | `#78818b` | 3.3 · 3.7 · 3.5 · 4.0 · 4.0 |

The three text levels each have one job:
- `--fg` is for values and primary labels.
- `--dim` is for secondary labels.
- `--faint` is for units, captions and hints.

Nothing is lighter than `--faint`.

**One chrome accent.** `--acc` is a desaturated steel-cyan. It marks only selection, focus, the active tab and the primary action. Selection fill is `--sel` (accent 14 %) and the selected border is `--selb`. Labs no longer recolour the chrome; each lab's identity lives in its data colours (§1.4).

### 1.3 Semantic
| Token | Dark | Light | Lowest light ratio |
|---|---|---|---|
| `--ok` | `#5fc98a` | `#16733d` | 4.9 |
| `--bad` | `#ef7a6a` | `#b2342a` | 5.1 |
| `--warn` | `#e3b45a` | `#8a5f00` | 4.7 |
| `--rec` | `#ef6a6a` | `#b2342a` | 5.1 |
| `--star` | `#e9c46a` | `#8a6200` | 4.6 |

Colour never carries meaning on its own. Every semantic colour comes with a glyph (✓, ✕, ●) or a word.

### 1.4 Data colours
- **Twistor pair.** `--Z1` / `--Z2` are dark `#2fd8f2` / `#ff6b2c` and light `#08718a` / `#b8410f`. Each lab overrides them with its own pair, `--lab-<id>-1/2` (for example `--lab-qb-1` is `#5ab8ff` dark and `#1f78c2` light).
- **Axes** (`AXC`): x `#ff6b6b`, y `#7dff8a`, z `#6bb8ff`, w `#c9a6ff`. These are the same in every lab, in canvas and in the DOM.
- **Data colour used as text.** Add the class `.dtx` and set `--c:<colour>`. The theme then clamps its lightness so it passes AA on every surface while keeping the hue:
  - dark: `oklch(from var(--c) max(l,.72) c h)`;
  - light: `oklch(from var(--c) min(l,.44) c h)`, with a `color-mix(… 45%, #000)` fallback.
- **Where `.dtx` is used:** axis chips and labels, plane chips, matrix headers (`.h8`), particle symbols (`.ups`), coloured section headings (`h3.sph`) and legend `em`.
- **Plots.** Plot areas are always dark in both themes. They use `--dk-*` (`--dk-bg #0d1013`, `--dk-fg #dfe3e8`, `--dk-dim`, `--dk-faint`). Canvas chrome reads these once per theme change through `CK` (`CK.fg`, `CK.dim`, `CK.faint`, `CK.bg`, `CK.i(alpha)`), so the drawing code holds no hex literals.

### 1.5 Colormaps
| Role | Default | Selectable |
|---|---|---|
| Sequential (height, magnitude, energy) | **viridis** | cividis (colour-vision-deficiency safe), classic (the original rainbow) |
| Cyclic (phase, angle; the Twistor palette's "cyclic" slot, formerly "rainbow") | OKLCH ring, L .76, C .12, 8 stops (`CMS.cycRGB`) | classic hue wheel |
| Diverging (signed: curl, divergence, flux sign) | *Phase 3:* RdBu-style, pivot at 0, symmetric limits | classic |

The setting lives in **App settings → Colour maps** (`APP.cmap`, stored per device). Every colormap gets a colorbar with a label and units (Phase 3, §3.13).

---

## 2. Type, space, shape, motion, depth

**Families** (unchanged):
- `--ui`: IBM Plex Sans Condensed, for chrome.
- `--prose`: IBM Plex Sans, for notes and the glossary.
- `--mono`: JetBrains Mono, for readouts and code.
- `--math`: STIX Two, for symbols.

**Type scale** (6 sizes; nothing smaller than 11 px, canvas text included):

| Token | px | Role |
|---|---|---|
| `--t-1` | 11 | captions, units, mini-view labels, canvas ticks |
| `--t-2` | 12 | control labels, chips, tabs, readouts |
| `--t-3` | 13 | body, notes (line-height `--lh-prose` 1.5) |
| `--t-4` | 16 | section titles, inputs on touch (no iOS zoom) |
| `--t-5` | 19 | panel and lab titles |
| `--t-6` | 24 | page title |

- **Numbers.** Readouts use `tabular-nums` and `"zero"`.
- **Math scripts.** Sub- and superscripts follow math typesetting at `.75em`, never below 9 px. They are the one exception to the 11 px floor.
- **Line wrapping.** Headings use `text-wrap: balance` and prose uses `pretty`.
- **Line height.** `--lh-tight` (1.25) for headings and `--lh-prose` (1.5) for prose.

**Spacing.** The base is 4 px, with a 2 px half-step reserved for hairline insets. The steps are `--s-h 2 · --s-1 4 · --s-2 8 · --s-3 12 · --s-4 16 · --s-6 24 · --s-8 32 · --s-12 48`. The gaps that recur across components:
- label to control: 8;
- inside a group: 8;
- between groups: 16;
- section padding: 12 on phones, 16 from 700 px up.

**Radii** (3 steps):
- `--r-1` 2 for swatches and inline marks;
- `--r-2` 4 for panels, controls, chips and segmented controls (joined groups round only their outer corners);
- `--r-3` 8 for popovers and dialogs.

**Motion** (UI chrome only):

| Token | Value | Use |
|---|---|---|
| `--d-1` | 120 ms | press, hover, tab content fade |
| `--d-2` | 160 ms | popover in, colour changes |
| `--d-3` | 200 ms | indicator slide, panel open |
| `--d-4` | 250 ms | ceiling, never exceeded |
| `--ease-out` | `cubic-bezier(.23,1,.32,1)` | anything entering or responding |
| `--ease-in-out` | `cubic-bezier(.77,0,.175,1)` | anything moving between two places |

Motion rules:
- **What may animate.** Only `transform` and `opacity`, never `transition: all`. `will-change` is set only while something is moving.
- **Reduced motion.** It removes chrome animation. Simulations keep their own controls.
- **Press feedback.** `:active { transform: scale(.97) }`.
- **Popovers.** They grow from their trigger, using `transform-origin` at the trigger corner.
- **Attention cue (exception).** After you jump to a section, an outline flashes and fades over 1.4 s (`.secfl`, `mFl`). It is a locating cue rather than a state transition, so it lasts long enough to notice. Reduced motion removes it.

**Depth (z):** `--z-1/2/3` (in-flow layers), `--z-sticky` 10, `--z-float` 20 (popovers, menus), `--z-modal` 30, `--z-top` 40 (skip link, tour).

---

## 3. Component conventions

Every interactive component follows the same base rules:
- **States.** Rest, hover, pressed and selected. Hover exists only inside `@media (hover:hover) and (pointer:fine)`.
- **Focus.** `:focus-visible` gives a 2 px `--acc` ring at a 2 px offset (−2 px inside menus).
- **Disabled.** Opacity .45 and `cursor:not-allowed`.
- **Size.** The visual minimum is 24 px. On `pointer:coarse`, the hit area grows to 44 px through a `::after` overlay, so the visual stays the same. Where neighbours touch (mode grid, lab tabs in the 44 px app bar), the control itself is 44 px tall.

| # | Component | Anatomy and rules |
|---|---|---|
| 3.1 | **Panel** (`.panel`, `section`) | `--panel`, 1 px `--line`, `--r-2`. A header row of 28 px (`--hdr`) holds the title (`--t-4`/600), an optional hint (`--t-3`, `--faint`) and actions on the right. No nested cards: a panel holds groups (`--panel2`), never other panels. |
| 3.2 | **Section header** (`h3.sph`, `details>summary`) | Disclosure caret, title `--t-3`/600 `--fg` (or a data colour via `.dtx`), reset and info buttons on the right. The whole row is the toggle, at least 24 px tall. |
| 3.3 | **Button** (`.act`) | Text label in sentence case, written as a verb plus object. `--ctl` fill and `--line2` border. The primary button uses an `--acc` fill with `--on-acc` text, and a group has at most one. |
| 3.4 | **Icon button** (`.icon`, `.ib`) | 28 × 26 px visual with an 18 px icon at a 1.5 stroke, `aria-label` required. Icon buttons that belong together are joined into one group with shared borders (`.btns`, `.qfg`). |
| 3.5 | **Chip** (`.chip`) | `--t-2` text, `--r-2`, 24 px (joined chip rows round only their ends). A toggle chip carries `aria-pressed`; selected means `--sel` fill and `--selb` border. |
| 3.6 | **Segmented control** (`.seg`, `.apseg`, `.modes`) | A 2 px inset track (`--s-h`) holding joined buttons with a 1 px divider, `role=radiogroup`/`radio` or `tablist`/`tab`. The selection is shown by the sliding `.sind` indicator (scaleX only) plus `--sel`. If the options wrap they form a grid, never a ragged flow. |
| 3.7 | **Slider** (`label.sl`) | **Label** (`--t-2`, `--dim`), then **track** (4 px, `--track`, `--acc` fill), then an **editable numeric field** with its unit (`--mono`, tabular, 5–7 ch). On phones the label sits above the track; from 700 px up it sits in a 120 px label column. Keys: arrows step, Shift+arrow steps ×10, PageUp/PageDown step ×10, Home/End jump to min/max. A drawer (long-press or `⋯`) holds min, max, step, play, step ± and speed. *(The numeric field and the drawer are Phase 3, §4 batch 3.)* |
| 3.8 | **Select** | Native `<select>`, `--ctl`, a chevron icon, 26 px tall for a fine pointer. On touch the text is 16 px so iOS doesn't zoom in. |
| 3.9 | **Popover** (`.apop`, `.qpop`, `.secm`, `.bmpop`) | `--elev`, `--r-3`, `--sh-1`. It grows from its trigger in 160 ms. On open, focus moves to the selected option. Escape closes it and returns focus to the trigger. Tab past the last item closes it and continues after the trigger. A pointer press outside closes it. `overscroll-behavior: contain`. |
| 3.10 | **Telemetry tile** (`.tile`, `.rv`) | Label `--t-1` `--faint` above the value `--t-2` `--mono` `--fg`, both tabular, with the unit in `--faint`. A value that changes never shifts the layout because its width is fixed in ch. |
| 3.11 | **Legend** (`#legend`, `.rh`) | A swatch (10 px, `--r-1`) or line sample, then the name (`--t-2`), then the symbol in `--math`, coloured with `.dtx`. It sits beside the plot, never above the controls. |
| 3.12 | **Matrix / readout grid** (`.mx8`, `.kv`) | Header cells use `.dtx` data colours, values are `--mono` tabular, and the half-split uses a 4 px gutter. |
| 3.13 | **Colorbar** *(Phase 3)* | Vertical on the right in landscape and horizontal below the plot in portrait. 8 px bar, 3–5 ticks at `--t-1`, a quantity label and its units, and a pivot tick for diverging maps. It is drawn by the same code path as the plot so it always matches. |
| 3.14 | **Caption** (`figcaption`, `.cap`, `.seccap`) | `--t-1` `--faint`, sentence case, one line, ellipsis with the full text in `title`. A caption also provides the canvas `aria-label` (§5). |
| 3.15 | **Toast** (`.toast`) | `--elev`, `--sh-1`, bottom centre and clear of the safe area, `role=status`. Text is "[What happened]. [Next step]." It disappears after 4 s, or stays while the pointer is over it or it has focus. |
| 3.16 | **Engine badge** (`.engtag`) | `--t-1` `--mono` in the view's corner. The copy states the fact and the reason ("WebGL (no WebGPU in this browser)"). The `title` gives the next step; on touch, tapping the badge shows it as a toast. |

---

## 4. Phase 3 batch plan

Each batch ends with:
- a list of the edited regions;
- the statement-level JS diff against v17, with every hunk classified (presentation only);
- the 12-lab × 2-theme × 2-width checker (contrast, <24 px targets, coarse hit areas, horizontal scroll, page errors);
- the scene error sweep at Auto, Potato and Ultra.

1. **Data-colour unification.** Move `AXC`, `COLS` and the particle palette into tokens `--ax-x/y/z/w` and `--lab-*` that `CK` reads. Canvas legends, axis labels and DOM all draw from that one source, and the positive/negative sign colours become one diverging pair.
2. **Diverging colormap.** Add an RdBu-style map with a pivot at 0 for signed fields (curl, divergence, flux sign, ∂f). Shaders get the same LUT (8-stop `pal` uniform). Classic stays selectable.
3. **Slider anatomy.** An editable numeric field with its unit next to every slider (input stays bound to the same `st.*` setters). Add the keyboard bindings from §3.7 and the min/max/step/play drawer.
4. **Colorbars.** Add colorbars per §3.13 to Calc Lab surfaces, contour maps, slice panels and Fluid Lab.
5. **Describe-graph mode.** A text summary for each chart (range, extrema, current parameter values), exposed as `aria-describedby` and through a "Describe" button.
6. **Typography pass on canvas.** Canvas tick and label fonts follow the `--t-*` scale through `CK`. Check label fit on 360 px phones.
7. **States and copy.** Designed loading, empty and error states (WebGPU unavailable, WebGL context lost, formula error, slice misses the shape), each with the problem and a next step, following §3.15.
8. **Chrome motion polish.** Tighten the boot and lab-switch fades to 150 ms opacity. Popovers exit in 120 ms. Final review with review-animations.
9. **GPU colormaps.** WebGPU and WebGL particle and field shaders sample the selected colormap LUT (viridis, cividis, classic, cyclic) instead of the hard-coded hue wheel.

---

## 4a. Phase 3 status (v19)
| # | Batch | Status | What changed |
|---|---|---|---|
| 1 | Data colours | Done | `--dk-ax-x/y/z/w`, `--dk-pos/--dk-neg` tokens; `CK.ax/pos/neg`; `AXC` reads `CK.ax`; every canvas series named x/y/z/w/P/Q/R/S uses `AXC`. In Calc Lab, x and y direction are now axis red and green (legend, 3D, the slice curve, P/Q series), matching the gizmo. |
| 2 | Diverging map | Done | Signed values in every lab use the one zero-centred map `eqCm('div')` (blue, dark at 0, red). The commutator grid and the max/min and eigenvalue sign dots now use it or `CK.pos/neg`. |
| 3 | Sliders | Done, drawer left out | Tap or click any slider value (or press Enter on a focused slider) to type a number. It accepts −, comma decimals and units, and maps formatted values (degrees, log scales, ×) back to the raw slider value. Shift+arrow steps ×10. The min/max/step/play drawer is not built; your call. |
| 4 | Colorbars | Done | Every Calc plane and slice heatmap, plus the Fluid top view. Vertical on the right where there is room, otherwise a compact bar in the plot corner. Each says sequential/diverging/heat/dye. The surface height map shows its numeric range and label. |
| 5 | Describe | Done (text only) | Each canvas with a colorbar gets an `aria-describedby` sentence: what the colour shows, the map, and the range where known. No visible "Describe" button (it would be a new control). |
| 6 | Chart text | Done | Calc and Law Lab tick labels use the UI font, with decimals chosen from the tick step (−2, −1, 0, 1, 2) and a real minus on degree ticks. |
| 7 | States | Done | WebGL missing now gives a next step. WebGL context lost shows a dark overlay ("3D view paused …") that clears itself on restore. Formula and slice-miss copy already had next steps. |
| 8 | Chrome motion | Done | Tooltip pop shortened to 120 ms; the keyboard-shortcuts dialog no longer animates. The rest passed review-animations. |
| 9 | GPU colour maps | Done | The WebGPU particle shader samples viridis or cividis (`cm9`) for the energy colour mode, matching WebGL; classic keeps the hue ramp. The WGSL compiles clean. The full WebGPU pipeline could not run in the test browser (v17 drops the device there too). |

## 4b. Phase 4 verification (v20)
| Check | Result |
|---|---|
| Your screenshot fixes | Commutator grids and caption centred. 16 × 16 matrix cells centred. Mini-view captions fill their tile (no empty strip). Empty notes hidden. Telemetry buttons 8 px apart. Lattice arrows thinner (1.1 px, 3 px heads). |
| Error sweep | All 12 labs and all 101 Calc scenes, 0 errors at Auto, Potato and Ultra. |
| Control walk | Every button, chip, tab, select and slider in every lab, clicked against v17: same controls, 0 errors, simulations still running. |
| Contrast, targets, scroll, touch | 12 labs × dark/light × 390/1440: 0 failures. |
| Keyboard | Popover focus in/out, Esc and Tab; every collapsible section header reachable by Tab, opened with Enter/Space, with `aria-expanded`. The formula field is tied to its status (`aria-describedby`, `aria-invalid`). |
| Reduced motion, full screen | Same as v17. Chrome animations off under reduced motion; full screen enters and exits. |
| web-design-guidelines | Pass. Placeholders end in "…". Theme-color follows the top bar on purpose. Formula-syntax placeholders keep no ellipsis. |
| Detector | 1 finding: the corner engine badge, kept on purpose. |
| Maths | Statement diff against v17: every changed hunk is presentation, copy or UI helpers. |
| Potato | Frame times equal to v17 within noise. |

## 5. Accessibility contract
- **Document structure.** `lang=en`, a `role=main` landmark, a "Skip to the controls" link, and a `theme-color` meta that follows `--panel`.
- **Canvases.** Every canvas has `role=img` and an `aria-label` taken from its caption or panel title. Phase 3 adds descriptions.
- **Keyboard.** Every control can be reached in DOM order, and popovers manage focus as described in §3.9.
- **Contrast, targets and scroll.** Checked by `p1v.py`, which must report 0 contrast failures, 0 targets under 24 px, 0 coarse hit failures and 0 horizontal scroll across all 12 labs, both themes, and 390 and 1440 px widths.
- **Reduced motion.** It removes chrome motion.
