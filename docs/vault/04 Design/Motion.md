---
tags: [design, motion]
---
# Motion

UI chrome only. Simulations' own speeds and timing are content and never change.

| token | ms | use |
|---|---|---|
| `--d-1` | 120 | press, hover, tab fade |
| `--d-2` | 160 | popover in, colour change |
| `--d-3` | 200 | indicator slide, panel open |
| `--d-4` | 250 | ceiling |

- Animate only `transform` and `opacity`; never `transition: all`; `will-change` only while moving.
- Press: `:active { transform: scale(.97) }`. Popovers grow from the trigger corner and exit in 120 ms.
- Tooltip pop 120 ms; shortcuts dialog does not animate; boot and lab-switch fade 150 ms.
- Exception: section locate-flash `.secfl` (`mFl`) 1.4 s, removed under reduced motion.
- Reduced motion removes chrome animation; sim controls stay.

File: `motion.js` in [[Build pipeline]]. Tokens: [[Design tokens]].
