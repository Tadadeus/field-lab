---
tags: [lab, cx, calculus]
lab-id: cx
---
# Lab Calc (`cx`): multivariable calculus you can see

## Modes (`CXM`)
| mode | what it shows |
|---|---|
| surf | surface z = f(x,y), gradient, tangent plane, level curves |
| dint | double integral: volume under a surface, Riemann boxes |
| vec2 | 2D vector field, flow lines, divergence, curl |
| vec3 | 3D vector field, flux, circulation |
| para | parametric curves and surfaces |
| map | maps ℝ²→ℝ², Jacobian, area scaling |
| air | airfoil / complex-map flow |
| vol | volume integrals, triple integral regions |
| hyp | hyperbolic geometry |
| v4 | 4D objects and projections |

## Data
- Function families `CXF`; **102 calculus scenes** `CXS` (part of the 504 in [[Scene catalog]]).
- Expressions are compiled from text like [[Lab Law]] `math` mode.

## Code
Built from `cx0.js … cx9.js` part files inserted before `const IIC={el:null` (see [[Build pipeline]]); registered as `ENG.cx`.

Related: [[Lab Fluid]], [[Shared 4D field engine]] (for the v4 projections).
