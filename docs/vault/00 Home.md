---
tags: [home, index]
aliases: [Index, MOC, Start here]
---
# Field Lab: vault home

Field Lab is a **single-file maths and physics lab** (one HTML file, vanilla JavaScript in one IIFE, three.js r128, optional WebGPU). It is used mostly on a phone (about 390 px wide). This vault explains every part of it. Open notes in the order below the first time; afterwards use search, backlinks and the graph view.

> Notes marked *(generated)* were produced from the running app (scene tables, parameter help, glossary, function names), so they match the code exactly. The rest are written by hand from the source of build **v21**.

## Start here
1. [[What is Field Lab]]: what it does, the 12 labs, who it is for.
2. [[Architecture]]: how the one file is organised.
3. [[Build pipeline]]: how `Field_Lab.html` is assembled from parts (this matters for working in a repo).
4. [[Project rules]]: the constraints that every change must keep.

## Overview
- [[What is Field Lab]] · [[Architecture]] · [[Build pipeline]] · [[State and persistence]] · [[Frame loop]] · [[Naming conventions]] · [[Project rules]]

## The 12 labs
| id | lab | note |
|---|---|---|
| `tw` | Twistor | [[Lab Twistor]] |
| `ca` | Courant (generalized geometry) | [[Lab Courant]] |
| `oc` | Octonion | [[Lab Octonion]] |
| `su` | su(3) | [[Lab su3]] |
| `cl` | Clifford | [[Lab Clifford]] |
| `qb` | 3 qubits | [[Lab Qubits]] |
| `se` | Sedenion ℂ¹⁶ | [[Lab Sedenion]] |
| `la` | Lattice field theory | [[Lab Lattice]] |
| `un` | Universe (particle zoo) | [[Lab Universe]] |
| `fl` | Fluid Lab | [[Lab Fluid]] |
| `eq` | Law Lab (write your own laws) | [[Lab Law]] |
| `cx` | Calc Lab | [[Lab Calc]] |

The first seven share one engine: [[Shared 4D field engine]].

## Systems (shared by all labs)
- Rendering: [[Rendering with WebGL]] · [[Rendering with WebGPU]] · [[Quality tiers]] · [[Colormaps and colorbars]]
- Content: [[Scenes system]] · [[Sandbox objects and probes]] · [[Quantum Geometry Physics tabs]]
- Controls: [[Controls framework]] · [[Settings and app popover]] · [[Info icons and sections]]
- Data and state: [[Telemetry pins and CSV]] · [[History timeline]] · [[Undo and redo]] · [[Share codes]] · [[Compare A-B]] · [[Camera bookmarks]] · [[Storage keys]]
- Help and polish: [[Help tooltips glossary tour]] · [[Sound]] · [[Accessibility layer]]

## Design system
[[Design tokens]] · [[Component conventions]] · [[Motion]] · [[Light theme and data colour]]

## Reference *(generated)*
[[Scene catalog]] (506 scenes) · [[Parameter reference]] (359 sliders) · [[Glossary]] (202 terms) · [[Function index]] (1865 names) · [[Keyboard shortcuts]] · [[Guided tour]] · [[Verification tools]]

## Roadmap and ideas
[[Particle Fields lab plan]] (waves of all 17 Standard Model particles) · [[s+tD sandbox idea]] · [[Open decisions]]
