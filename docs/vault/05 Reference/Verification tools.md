---
tags: [reference, testing]
---
# Verification tools (in the build folder)

| script | checks |
|---|---|
| `p1v.py` | contrast, targets < 24 px, coarse hit areas, horizontal scroll: 12 labs × 2 themes × 390/1440 px; must be all 0 |
| `hitall.py` | every control hit area on coarse pointer |
| `kbt.py` | keyboard: focus order, popover focus in/out, Esc/Tab |
| `cxth.py` | Calc Lab theming in both themes |
| `cxe.py` | error sweep of all Calc scenes |
| `ctlwalk.py` | clicks every button, chip, tab, select, slider; compares with v17 |
| `mdiff.py` | statement-level JS diff against v17; every hunk must be presentation only (maths unchanged) |
| `potperf.py` | Potato frame times vs v17 |
| `wdg.py` | WebGPU/WebGL init smoke test |
| `finalsweep.sh` | runs the set before release |
| impeccable detector | design anti-pattern scan (1 accepted finding: corner engine badge) |

Release gate: scene error sweep (all 504 scenes) at Auto, Potato and Ultra with 0 errors. See [[Project rules]], [[Build pipeline]], [[Accessibility layer]].
