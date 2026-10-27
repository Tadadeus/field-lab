---
tags: [overview, rules]
---
# Project rules

These come from the owner's "hyper prompt" (`field-lab-redesign-prompt.md`) and from standing preferences. Every change must keep them.

## Hard rules
1. **Maths, physics and computation stay byte-for-byte unchanged.** Redesign work changes UI chrome only. Proof: `mdiff.py` compares statements against `base_v17.html` and classifies every hunk.
2. **Every feature, ID, class and data attribute stays.** Tests, wrappers and saved states refer to them.
3. **No new dependencies and no new fonts.** Potato quality must not get heavier ([[Quality tiers]]).
4. **One desaturated accent, tokens only.** Dark `--acc:#7fb6c9`, light `--acc:#1d6a82`. No literal colours in CSS ([[Design tokens]]).
5. **WCAG 2.2 AA** contrast, focus, names ([[Accessibility layer]]); **44 px** touch areas on coarse pointers; motion **120–250 ms** ([[Motion]]).
6. New labs and controls must **match the existing visual style** and put long descriptions behind small **ⓘ** buttons ([[Info icons and sections]]).
7. Never remove an existing feature; only fix or add.

## The phases that were used
| phase | goal | status |
|---|---|---|
| 1 | audit (scored, reached 20/20) | done, `phase1-audit.md` |
| 2 | design system | done, `DESIGN.md` |
| 3 | implementation in 9 batches | done |
| 4 | verification | done ([[Verification tools]]) |

## Owner preferences (how to work)
- Talk little; don't explain code unless asked; just code more.
- Minimal, comment-free code. Always put `{}` on `if`/`for` blocks.
- Prefer single targeted edits over rewrites (token cost).
- Owner usually writes in Czech or English; replies in the language used.
- Uses the app on a phone (~390 px, 2K display): check changes at 390 px first.

## Deliverables of a release
`DESIGN.md`, a diff-based unchanged-maths statement, the republished artifact and `Field_Lab.html`, a report of tools/skills used.

## Open decisions (not yet built)
See [[Open decisions]].
