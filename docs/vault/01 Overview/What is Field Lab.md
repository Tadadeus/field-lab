---
tags: [overview]
---
# What is Field Lab

A browser lab where you **see** mathematics and physics move: twistors, generalized geometry, non-associative algebras, lattice field theories, a particle zoo, fluids, your own equations, and calculus. Everything runs locally in one HTML file; nothing is sent anywhere.

## The 12 labs (called "sets" in the UI)
Switch with the lab tabs at the top (`#segTh`) or keys **1…9, 0**.

| group | labs | what they have in common |
|---|---|---|
| Algebra and geometry pairs | [[Lab Twistor]], [[Lab Courant]], [[Lab Octonion]], [[Lab su3]], [[Lab Clifford]], [[Lab Qubits]], [[Lab Sedenion]] | Two objects ("a bi-object") make one 3D/4D field. All seven use [[Shared 4D field engine]]. |
| Simulation labs | [[Lab Lattice]], [[Lab Universe]], [[Lab Fluid]] | Real time-stepping solvers with their own engine object registered in `ENG`. |
| Build-your-own labs | [[Lab Law]], [[Lab Calc]] | You type formulas; they are compiled in the browser. |

In total there are **506 ready-made scenes** ([[Scene catalog]]) and **359 documented sliders** ([[Parameter reference]]).

## What you can do in any lab
- Pick a scene, press play, drag the 3D view to turn it, pinch/scroll to zoom, tap to drop a probe ([[Sandbox objects and probes]]).
- Change settings in tabs (Field, Objects, Motion, 4D view, Visual, Camera, State, Geometry, Quantum, Physics, Memory) ([[Controls framework]]).
- Read live numbers: telemetry tiles, matrices, charts, 12 s traces ([[Telemetry pins and CSV]]).
- Scrub back through the recorded run ([[History timeline]]), undo settings ([[Undo and redo]]), compare two states ([[Compare A-B]]), share a code ([[Share codes]]).
- Choose quality from Potato to Maximum ([[Quality tiers]]) and colour maps ([[Colormaps and colorbars]]).

## Who it is for
The owner (Tade) uses it mostly on a phone at about 390 px width with a 2K display. The UI is designed mobile-first ([[Design tokens]], [[Component conventions]]) and meets WCAG 2.2 AA ([[Accessibility layer]]).

## Technology
- One file, ~1.66 MB: a CSS block, the HTML body, one `<script src=three.js r128>` and one big `<script>` IIFE of ~6300 lines.
- Fonts from Google Fonts (IBM Plex Sans / Condensed, JetBrains Mono, STIX Two Text); no other dependencies.
- 2D canvases for charts, three.js (WebGL) for 3D, **WebGPU** for the heavy path when available ([[Rendering with WebGPU]]).

See [[Architecture]] next.
