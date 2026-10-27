---
tags: [systems, ui, help]
---
# Info icons and sections

- Info buttons `.ib` (`iiBtn`, placed by `iiScan`/`iiAttach`) sit next to headings. The section's own explanatory notes are hidden in place (`.ii-src`) and shown in an info card (`iiOpen`: `.icard` with role dialog over an overlay `.icov`). The card grows from the button (`--ax` origin) and closes on Esc, a tap outside, a short tap on the card, or the same button again (`iiClose`). Slider and term help comes from HELP ([[Help tooltips glossary tour]]).
- Collapsible settings sections are `h3.sph` headers (▾ / ▸) wrapping `.spsec` groups; reset buttons (`.sprs`, ↺) restore a section's defaults.
- Slider labels show a tooltip (`.tip`) with a short explanation.
- Convention: [[Component conventions]]; accessibility: [[Accessibility layer]].
