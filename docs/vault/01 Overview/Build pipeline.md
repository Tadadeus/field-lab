---
tags: [overview, build]
---
# Build pipeline

`Field_Lab.html` is **not edited by hand**. It is assembled by `build.py` from a base file plus part files, then post-processed by `ds.py`. This is how the redesign was made while keeping the simulation code byte-for-byte unchanged ([[Project rules]]).

## Inputs
| file | role |
|---|---|
| `orig.html` | the base single file the work started from (about 1.3 MB) |
| `base_v17.html` | the v17 build that is the **reference for maths diffs**: `mdiff.py` compares the final file to it statement by statement |
| `layer.css` | the first CSS layer, inserted just before `</style>` (see [[Component conventions]]) |
| `motion.js` | small UI motion script appended after the main script (the sliding `.sind` indicator, [[Motion]]) |
| `cx0.js … cx9.js`, `cxs.js`, `cxg.js` | the **Calc Lab**, split into ten parts plus scenes (`cxs`) and the 4D/GPU glue (`cxg`) ([[Lab Calc]]) |
| `cb.js` | colorbars ([[Colormaps and colorbars]]) |
| `q.js` | the quality popover and level table ([[Quality tiers]]) |
| `ux.js` | accessibility and editing helpers ([[Accessibility layer]]) |
| `ds.py` | the design-system pass: defines `TOKENS` and `run(css, sys_css)` which rewrites all CSS onto tokens ([[Design tokens]]) |
| `sys.css` | CSS appended *after* the token pass: focus rings, 24 px minimum targets, coarse-pointer hit areas, `.dtx` data colours, reduced motion |
| `DESIGN.md` | the written design system (also stored in the Claude project "Field Lab") |

## What `build.py` does, in order
1. Read `orig.html`; swap the Google Fonts link (adds IBM Plex Sans Condensed and IBM Plex Sans; keeps JetBrains Mono and STIX Two Text).
2. Insert `layer.css` before `</style>`.
3. Append `motion.js` after the main script.
4. Apply many **exact-string patches**: each is `(old, new)` and `build.py` asserts the old string occurs exactly once (`assert s.count(a)==1`). A patch that no longer matches stops the build, so changes can never silently miss.
   - Examples: add the "Calc Lab" tab button; add the `#cxMini` section; change the MONO font stack; make the lattice arrows shorter; rename the CSV button to "Download CSV".
5. Insert the part files `cx0…cx9, cxs, cxg, cb, q, ux` (in that order, if they exist) right **before `const IIC={el:null`** in the main script, so they can use everything defined above.
6. Regex rewrite of canvas colours in JS: hard-coded `rgba(220,226,236,.x)`, `'#e8ecf2'`, axis colours and pos/neg colours become `CK.i(.x)`, `CK.fg`, `AXC[i]`, `CK.pos/neg`; small font sizes (9–10.5 px) become 11 px.
7. Take the biggest `<style>` block and run `ds.run(css, sys.css)`: tokens plus transform plus `sys.css`.
8. Write `Field_Lab.html`.

## Output copies
- `Field_Lab.html`: the deliverable.
- `field-lab.html` (artifact copy): the same file starting at `<title>Field Lab</title>` with the trailing `</body></html>` removed, because the Artifact tool wraps the page in its own skeleton. Published at the artifact URL; republish with the same path to update it in place.

## Backups
`build.bak*`, `build.pre_ds.py`, `build.pre_p3.py`, `build.pre_fix19.py`, `build.pre_s4.py`, `build.pre_v21.py`, `ds.pre_p3.py`, `sys.pre_p3.css`, `cb.pre_fix19.js` are snapshots before risky steps. In a git repo these become history and can be dropped.

## Working in a repo (suggested layout)
```
src/    orig.html  layer.css  motion.js  cx0.js … cx9.js  cxs.js  cxg.js  cb.js  q.js  ux.js  sys.css
tools/  build.py  ds.py  (verification scripts: see [[Verification tools]])
docs/   DESIGN.md  this vault
dist/   Field_Lab.html
```
Rebuild with `python3 build.py`; run [[Verification tools]]; publish.

## Adding a new lab, in this pipeline
1. Write `newlab.js` as a part file (engine object in `ENG.<id>`, `ALG.<id>`, `TH.<id>`, `SC.push(...)`, `specX` controls).
2. Add the tab button and any HTML with an exact-string patch in `build.py`.
3. Add the file name to the `parts` list.
4. Add tokens (`--lab-<id>-1/2`) in `ds.py` if it has data colours ([[Light theme and data colour]]).
5. Run the maths diff to prove old labs are untouched, then the sweeps in [[Verification tools]].
