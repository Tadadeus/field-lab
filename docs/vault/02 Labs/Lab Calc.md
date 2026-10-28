---
tags: [lab, cx, calculus]
lab-id: cx
---
# Lab Calc (`cx`): multivariable calculus you can see

## Modes (`CXM`, 10)
| id | label |
|---|---|
| surf | Derivatives and gradients |
| dint | Double integrals |
| vec2 | Vector fields in the plane |
| vec3 | Vector fields in space |
| para | Surfaces and shape tools |
| map | Maps and Jacobians |
| air | Airflow and lift |
| vol | Triple integrals and solids |
| hyp | Hypersurfaces in 4D |
| v4 | Vector fields in 4D |

## State (`cxDef`)
Function `fs` (default `peaks`), domain `R`, resolution `res`, probe point `px, py`; toggles for tangent plane, gradient, contours, critical points; Lagrange constraint (`lag`, `con`); integration region `reg`, coordinates `coord`, Riemann rule `rule`, `n`; vector field `v2`/`v3` presets or custom `P, Q`, streamlines, curl/divergence colouring, circulation curve, paddle wheel.

## Data and files
- Function families `CXF`, scenes `CXS` (102, part of the 506 in [[Scene catalog]]).
- Source parts `cx0.js … cx9.js`, `cxs.js`, `cxg.js`, inserted before `const IIC={el:null` ([[Build pipeline]]). Mini views panel `#cxMini`.
- Uses the Law Lab expression compiler ([[Lab Law]], `CXH = EQHD`).

Related: [[Lab Fluid]], [[Shared 4D field engine]].
