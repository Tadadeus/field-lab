---
tags: [reference, parameters]
---
# Parameter reference

Every slider has a help entry in the `HELP` table (id → `text|unit`). Hovering or tapping a slider label shows it (`tipShow`). This table is generated from that data, so ids are the real DOM ids and `HELP` keys. Count: **359** entries.

## Motion and time

| id | meaning | unit |
|---|---|---|
| `par` | The parameter of the transformation picked in the tabs above: time t of the full motion, a rotation angle, a boost rapidity, a dilation log-scale, a conformal or mixing angle, or the evolution time. Dragging it pauses playback. | depends on the transformation |
| `spd` | Speed of simulated time against real time. 1× means one simulation second per real second; every engine (particles, lattices, the universe) runs on this clock. | × real time |
| `amp` | Swing: the amplitude of the oscillating transformation (boost rapidity, dilation or conformal size) when that transformation is selected. | rapidity or log-scale |
| `beta` | Mix phase β: the relative complex phase used when the two objects are combined. Turning it slides the interference pattern between the two fields. | degrees |
| `lr` | Left ↔ right balance: a 4D rotation splits into a left and a right isoclinic part (SO(4) ≅ SU(2)×SU(2)/ℤ₂). 0 runs both equally, an ordinary rotation of ℝ³. Sliding right weakens the left part, sliding left weakens the right part; at ±2 that side is off, a pure Hopf rotation. | balance of the two parts |
| `axT` | Polar angle of the rotation axis n̂, measured from +z. | degrees |
| `axP` | Azimuth of the rotation axis n̂ around z, measured from +x. | degrees |
| `axV` | One component of a custom rotation axis. The vector is normalised before use, so only the direction matters. | unit-vector component |
| `arot` | Rotation rate in the combined motion. | degrees per second |
| `abA` | Peak boost rapidity η. A Lorentz boost with rapidity η moves at v = c·tanh η, so η = 1 is 76 % of light speed. | rapidity |
| `abF` | How often the boost swings back and forth. | Hz |
| `adA` | Peak dilation λ: all lengths scale by e^λ (λ = 0.7 roughly doubles them). | log-scale |
| `adF` | How often the dilation swings. | Hz |
| `acA` | Peak special-conformal parameter: an inversion, a translation and another inversion. It bends straight lines into circles while keeping angles. | 1 / lab units |
| `acF` | How often the conformal transformation swings. | Hz |
| `amA` | Peak mixing angle between the two halves of the pair. For Courant pairs it rotates vectors X into forms ξ; at a full swap it is T-duality. | degrees |
| `amF` | How often the mixing swings. | Hz |
| `atS` | Speed of free time evolution t; negative values run it backwards. | t per second |

## Field display

| id | meaning | unit |
|---|---|---|
| `fpart` | How many tracer particles ride the field flow. More particles resolve finer structure but cost GPU time; the quality level can cap this number. | particles |
| `fsize` | Drawn size of each tracer particle. | lab units |
| `fsl` | Length of the streak behind each particle. Longer streaks show the local flow direction more clearly. | seconds of flow |
| `fml` | Field-energy density at which the glowing membrane (an isosurface) is drawn. Lower levels wrap a larger region around the sources. | energy density, lab units |
| `fmo` | How opaque the membrane isosurface is. | 0 – 1 |
| `fbr` | Overall brightness of particles and field lines. | × |
| `fspd` | How fast tracers drift along the field relative to the clock. | lab units per second |
| `fnl` | Field lines traced from each source. A field line follows the field direction at every point. | lines |
| `fgr` | Number of lines in the reference grid that the field deforms. | lines per side |
| `fga` | Brightness of the reference grid. | 0 – 1 |
| `fdga` | Brightness of the dual grid that draws the form half T* of the Courant bundle T ⊕ T*. | 0 – 1 |

## Objects

| id | meaning | unit |
|---|---|---|
| `osz` | Scale of the selected object. | × |
| `osp` | How fast the object spins about its own axis; negative spins the other way. | turns per second |
| `o4` | Turns the object through the 4th direction (an xw rotation). In the 3D slice it seems to shrink, grow or turn inside out. | turns per second |
| `oop` | How opaque the object is drawn. | 0 – 1 |
| `orr` | Radius of the circular route the object follows. | lab units |
| `ors` | Speed along the route; negative runs it the other way. | laps per second |
| `okp` | Torus knot (p, q): the curve winds p times around the tube. Coprime p and q make one knot; a common factor makes a link of several loops. | whole number |
| `okq` | Torus knot (p, q): the curve winds q times through the hole of the torus. (2, 3) is the trefoil. | whole number |

## 4D view

| id | meaning | unit |
|---|---|---|
| `v4rho` | Radius ρ of the 3-sphere used by the stereographic and sphere embeddings of 4D space. The far pole (w = ρ) is sent to infinity. | lab units |
| `v4d` | Distance of the 4D camera along w for perspective projection. Closer exaggerates depth in w. | lab units |
| `v4t` | How strongly time is stretched when it is drawn as the 4th axis. | × |
| `v4c` | Depth cue: fades or tints points by their w coordinate, so you can tell what lies ahead or behind in the 4th direction. | strength |
| `v4xw` | Rotation angle in the x–w plane. Rotations that mix a 3D axis with w bring hidden 4D structure into view. | degrees |
| `v4yw` | Rotation angle in the y–w plane. | degrees |
| `v4zw` | Rotation angle in the z–w plane. | degrees |
| `v4hl` | Left isoclinic (Hopf) rotation: turns ℝ⁴ by the same angle in two orthogonal planes at once, sliding every point along its Hopf circle. | degrees |
| `v4hr` | Right isoclinic (Hopf) rotation: like the left one with opposite handedness. Left and right rotations commute. | degrees |
| `v4sxw` | Continuous spin of the x–w angle. | degrees per second |
| `v4syw` | Continuous spin of the y–w angle. | degrees per second |
| `v4szw` | Continuous spin of the z–w angle. | degrees per second |
| `v4shl` | Continuous left Hopf spin. | degrees per second |
| `v4shr` | Continuous right Hopf spin. | degrees per second |
| `v4sl` | Thickness of the 3D slice through 4D space: points within half this distance of the slice are shown. | lab units |

## Rendering (Visual tab)

| id | meaning | unit |
|---|---|---|
| `vgl` | Strength of the additive glow on particles and points. | × |
| `vla` | Brightness of field lines. | × |
| `vsa` | Brightness of particle streaks. | × |
| `vex` | Exposure of the final image, as on a camera. | × |
| `vGmul` | Particle multiplier while the GPU particle engine runs. | × |
| `vLw` | Width of drawn lines. | pixels |
| `vBl` | Bloom: how much bright areas bleed light into their surroundings. | strength |
| `vBt` | Brightness above which bloom starts. | brightness |
| `vVs` | Strength of the volumetric rendering of field density. | × |
| `vGl` | Field-line multiplier on the GPU. | × |
| `vGd` | Resolution multiplier of the GPU membrane mesh. | × |

## Camera

| id | meaning | unit |
|---|---|---|
| `vos` | Automatic camera orbit around the vertical axis. | degrees per second |
| `vd` | Distance of the camera from its target. | lab units |
| `vfov` | Vertical field of view. Wide angles exaggerate perspective. | degrees |
| `vfg` | Depth fog: distant points fade out. | density per lab unit |

## Twistor state

| id | meaning | unit |
|---|---|---|
| `hs` | Helicity s of the massless field: ±½ is neutrino-like, ±1 photon-like. The sign picks the handedness of the twist. | units of ħ |
| `hE` | Energy of the twistor’s null momentum. Higher energy makes the pattern tighter, because its size scales as 1/E. | lab units |
| `ht` | Polar angle of the momentum direction. | degrees |
| `hf` | Azimuth of the momentum direction. | degrees |
| `hc` | Phase χ: rotates the complex phase of the field pattern without moving it. | degrees |
| `hx` | x position of the centre, where the twistor’s light rays focus. | lab units |
| `hy` | y position of the centre. | lab units |
| `hz` | z position of the centre. | lab units |

## Geometry tab

| id | meaning | unit |
|---|---|---|
| `gK` | How strong the curved background is: 0 is flat space, 1 the full chosen geometry. | 0 – 1 |
| `gL` | Radius L of anti-de Sitter space; its curvature is −1/L², so a smaller L bends space more. | lab units |
| `gS` | Radius R of the 3-sphere background; its curvature is +1/R². | lab units |
| `gT` | Period of the 4-torus: space wraps around every T units in each direction. | lab units |
| `gN` | Degree n of the Fermat curve z₁ⁿ + z₂ⁿ = 1, the classic picture of a Calabi–Yau slice (n = 5 belongs to the quintic). | whole number |
| `gCs` | Size of the drawn Calabi–Yau surface. | lab units |
| `gCr` | Turns the projection from ℂ² down to 3D, revealing other sides of the surface. | angle |
| `gCo` | Glow of the Calabi–Yau surface. | 0 – 1 |
| `gFd` | Density of the glyphs that draw the Dirac structure. | glyphs per side |
| `gB` | B-field: a closed 2-form acting as e^B : X + ξ ↦ X + ξ + ι_X B. It shears vectors into forms and is a symmetry of the Courant bracket. | lab units |
| `gNs` | Number 𝒩 of fermionic (Grassmann) coordinates in supertwistor space ℂ^{4/𝒩}. 𝒩 = 4 holds the whole 𝒩 = 4 super-Yang–Mills multiplet. | whole number |
| `gEps` | Size of the supersymmetry parameter ε, which rotates bosonic components into fermionic ones. | 0 – 1 |

## Quantum tab

| id | meaning | unit |
|---|---|---|
| `qTh` | Non-commutativity θ: coordinates obey [x, y] = iθ, so a position cannot be sharper than about √θ. | lab units² |
| `qCc` | Strength of the Moyal star-product drift, the first quantum correction to the motion (proportional to θ). | × |
| `qBl` | Visual smearing of each point by its quantum uncertainty. | × |
| `qQ` | Deformation q of the quantum group SU_q(2). At q = 1 it is the ordinary group. | dimensionless |
| `qJ` | Spin j of the fuzzy sphere: positions take only 2j + 1 allowed values. | units of ħ |
| `qSn` | How strongly points snap to the fuzzy-sphere grid: 0 is classical, 1 fully quantised. | 0 – 1 |
| `qF` | Spatial frequency of the interference fringes. | fringes across the view |

## Physics tab

| id | meaning | unit |
|---|---|---|
| `pHb` | Planck constant ħ. It sets how far quantum paths spread: larger is more quantum, smaller is closer to the classical path. | lab units |
| `pAp` | String scale α′ (string length squared): each point is smeared over a string of size √α′. | lab units² |
| `pNp` | Number of sampled paths in the path-integral sum. | paths |
| `pT` | Travel time T of each path. | seconds |
| `pVp` | Strength c of the potential V = −c log ρ that pulls paths toward high field density. | × |
| `pD` | How far the sampled paths may stray from the classical path. | lab units |
| `pNs` | Number of open strings stretched between the two objects. | strings |
| `pSm` | How many vibration modes each string has excited. | modes |
| `pSn` | Winding number n, the topological charge: how many times the field wraps around the vacuum circle. | whole number |
| `pSv` | Vacuum value v of the scalar field; it sets the soliton’s mass and size. | field units |
| `pSl` | Self-coupling λ of the potential λ(φ² − v²)². Larger λ makes thinner, heavier solitons. | dimensionless |
| `pSr` | Size ρ of the instanton. Yang–Mills instantons can have any size, so it is a free parameter. | lab units |
| `pScn` | Number of particles in the scattering state. | particles |

## Object position and charge

| id | meaning | unit |
|---|---|---|
| `cx` | x position of the object’s centre. | lab units |
| `cy` | y position of the object’s centre. | lab units |
| `cz` | z position of the object’s centre. | lab units |
| `cw` | Position in the 4th direction w. Only a slice of 4D space is drawn, so moving w slides the object through it. | lab units |
| `cm` | Charge m of the source: the strength of its field, which falls off like m/r² far away. | charge units |
| `ca` | Core radius a: smooths the field inside the source and removes the 1/r² spike. | lab units |
| `ct` | Polar angle of the object’s axis. | degrees |
| `cp` | Azimuth of the object’s axis. | degrees |
| `cc` | Phase χ of the object. | degrees |

## Algebra pair controls

| id | meaning | unit |
|---|---|---|
| `apB` | How far the pair tilts out of the quaternions ℍ. At 0 everything associates; as β grows the associator (ab)c − a(bc) appears. | degrees |
| `apK` | Strength of the colour flux tube between quark and antiquark. | × |
| `apE` | Balance η between the electric and magnetic parts of F = E + IB. At 45° with E ⟂ B the field is null, like light. | degrees |
| `apZ` | Angle between E and B. A null field needs 90° and /E/ = /B/. | degrees |
| `apZ@se` | Moves the pair toward a zero divisor: two nonzero sedenions whose product is zero, which octonions never allow. | 0 – 1 |
| `apN` | Tilts the vector v toward the time direction, a boost-like mix of space and time. | degrees |
| `apM` | Mixes the vector part into the trivector (pseudovector) part of the multivector. | degrees |
| `apR` | Weight of the real part: at 0 the sedenion pair is purely imaginary. | degrees |
| `apG` | Mixes the two octonion halves of the sedenion (Cayley–Dickson doubling). | degrees |

## Lattice lab

| id | meaning | unit |
|---|---|---|
| `laDt` | Time step of the leapfrog integrator. Too large and the run blows up: in 3D stability needs dt below 1/√3 ≈ 0.58. | lattice time units |
| `laRate` | Lattice steps per unit of simulation time, multiplied by the speed slider. | steps per second |
| `laLam` | Higgs self-coupling λ in V = λ/4 · (/φ/² − v²)². A larger λ stiffens the vacuum: thinner walls and strings, a heavier Higgs. | dimensionless |
| `laV` | Vacuum value v: away from defects the field settles at /φ/ = v. | field units |
| `laGam` | Damping γ in φ̈ + γφ̇ = …. It drains energy so the field cools into its vacuum and defects freeze out. | 1 / time |
| `laEx` | Brightness of the lattice rendering. | × |
| `laIso` | Level at which the isosurface is drawn, as a fraction of the vacuum value. | fraction |
| `laEps` | Bias ε between the two vacua: φ = +v sits higher by ε, so bubbles of the true vacuum grow and walls are pushed. | energy density |
| `laG` | Gauge coupling g. A larger g makes thinner flux tubes, because the penetration depth goes like 1/(g v). | dimensionless |
| `laAmp` | Amplitude of the oscillating source. | field units |
| `laOm` | Frequency ω of the driven source; the radiated wavelength is 2πc/ω. | radians per time |
| `laM` | Mass m of the Dirac electron. At m = 0 it moves at light speed; heavier packets move slower. | lattice units |
| `laV0` | Height V₀ of the potential wall. Above 2m it shows Klein tunnelling: the wall turns transparent. | energy, lattice units |
| `laB` | Uniform magnetic field: charged packets circle in Landau orbits. | lattice units |
| `laZ` | Charge Z of the nucleus in the Coulomb potential −Z/r. | elementary charges |
| `lqWr` | Wilson term r: removes fermion doublers (copies of the particle at the edge of the lattice zone) at the price of breaking chiral symmetry. | dimensionless |
| `lqM` | Mass of the quantum particle. Heavier packets spread more slowly (spread ∝ ħt/m). | lattice units |
| `lqK` | Central momentum k of the wave packet; its wavelength is 2π/k. | 1 / lattice spacing |
| `lqV` | Height V₀ of the wall or barrier. Packets with less kinetic energy than V₀ can only tunnel through. | energy, lattice units |
| `lqOm` | Trap frequency ω of the harmonic potential V = ½mω²r². | radians per time |
| `lqG` | Contact interaction g of the Gross–Pitaevskii equation (term g/ψ/²ψ). Repulsive g > 0 spreads the condensate. | lattice units |
| `lqOm2` | Frequency ω of the harmonic trap that holds the condensate. | radians per time |
| `lqRot` | Rotation Ω of the trap as a fraction of ω. Above a critical speed quantised vortices enter the condensate. | fraction of ω |
| `lqGam` | Imaginary-time cooling γ: drains energy so the condensate relaxes toward its ground state. | 1 / time |
| `lqLam` | Condensation strength λ of the Ginzburg–Landau potential. It sets the coherence length ξ ∝ 1/(√λ v). | dimensionless |
| `lqV2` | Order parameter v = /ψ/ deep inside the superconductor; the Cooper-pair density goes like v². | field units |
| `lqQ` | Charge g of the Cooper-pair field. The penetration depth is about 1/(g v): a larger g expels fields over a shorter distance. | dimensionless |
| `lqB` | Applied magnetic field. In a type-II superconductor it enters above H_c1 as vortices, each carrying one flux quantum. | lattice units |
| `lqJ` | Applied transport current. It pushes vortices sideways with the force J × B, which causes resistance. | lattice units |
| `lqD` | Dzyaloshinskii–Moriya twist D: favours a twist between neighbouring spins and stabilises skyrmions of size about J/D. | energy |
| `lqB2` | Magnetic field B along z (Zeeman term). A larger B shrinks skyrmions until they collapse. | energy |
| `lqKa` | Anisotropy K: positive favours spins along ±z (easy axis), negative an easy plane. | energy |
| `lqAl` | Gilbert damping α in the Landau–Lifshitz–Gilbert equation: how quickly precessing spins relax. | dimensionless |

## Universe lab

| id | meaning | unit |
|---|---|---|
| `unSE` | Kinetic energy of each spawned particle, on a log scale. | eV to TeV |
| `unSN` | How many particles each spawn creates. | particles |
| `unB` | Uniform magnetic field along z. Charged tracks curve with radius r = p/(/q/B), and the direction of the curl shows the sign of the charge. | field units |
| `unMed` | Density of the bubble-chamber liquid. Particles lose energy by ionisation (dE/dx) and spiral inward; 0 is vacuum. | × |
| `unKE` | Electromagnetic coupling: the fine-structure constant α, about 1/137 ≈ 0.0073 in our universe. | dimensionless |
| `unKS` | Tension of the QCD string between quarks (about 1 GeV per fm in nature). Pulling quarks apart stores energy until the string snaps into new hadrons. | string tension |
| `unKN` | Strength of the residual nuclear force that binds protons and neutrons. | × |
| `unG` | Newton’s gravitational constant on a log scale; “off” disables gravity. | simulation units |
| `unC` | Speed of light: nothing moves faster. A slower c makes relativistic effects, such as the time dilation of decays, easy to see. | units per second |
| `unLife` | Multiplies every particle lifetime, so unstable particles fly further before they decay. | × |
| `unW4` | Turns the view through the 4th space dimension (x–w plane). | radians |
| `unLam` | Cosmological constant Λ: a push that grows with distance and accelerates expansion, like dark energy. | 1 / s² |
| `unHub` | Hubble rate H: space stretches, so distant particles recede at v = H·d and light is redshifted. | 1 / s |
| `unTemp` | Temperature of a heat bath that creates particles thermally: pairs of mass m appear once kT is comparable to m. | MeV |
| `unVac` | Rate of virtual particle–antiparticle pairs flickering out of the vacuum. | pairs per second |
| `unBH` | Schwarzschild radius r_s = 2GM/c² of a central black hole; anything that crosses it is captured. | units |
| `unHawk` | Strength of Hawking radiation: black holes glow at a temperature ∝ 1/r_s and slowly evaporate. | × |
| `unRs1` | Schwarzschild radius of the first black hole of the binary. | units |
| `unRs2` | Schwarzschild radius of the second black hole of the binary. | units |
| `unA0` | Starting distance between the two black holes. | units |
| `unGwk` | Multiplier on the energy carried off by gravitational waves. The orbit shrinks faster and the chirp rises sooner. | × |
| `unNuKm` | How many kilometres one unit of the view stands for. The oscillation length grows like E/Δm². | km per unit |
| `unNuDet` | Detector efficiency: the fraction of passing neutrinos that it registers. | fraction |
| `unNuE` | Neutrino beam energy. Higher energy stretches the oscillation length (L_osc ∝ E/Δm²). | MeV |
| `srM` | Starting mass of the star on a log scale. Mass decides the whole life: below 0.5 M☉ a red dwarf, near 1 M☉ a white dwarf at the end, above 8 M☉ a supernova, above about 20 M☉ a black hole. | solar masses |
| `srSp` | Playback speed of the star’s life. | × |
| `srPos` | Stage of the star’s life; drag to jump. | life stage |
| `bbSp` | Playback speed of cosmic history. | × |
| `bbPos` | Cosmic time since the Big Bang on a log scale; drag to jump. | seconds to billions of years |
| `unIvM` | Mass of your invented particle on a log scale. | MeV |
| `unIvQ` | Electric charge in units of e; quarks carry thirds. | e |
| `unIvT` | Mean lifetime τ on a log scale. After a time τ about 37 % (1/e) of the particles are left. | seconds |
| `unIvH` | Colour of its tracks. | hue |
| `unFade` | How long tracks stay visible. | seconds |
| `unSz` | Drawn size of the particles. | × |
| `unRate` | Clock rate of the particle simulation, multiplied by the speed slider. | × |

## Spin chain

| id | meaning | unit |
|---|---|---|
| `chN` | Number of spins N. The exact quantum state has 2^N amplitudes, so N = 12 means 4096. | spins |
| `chJ` | Exchange coupling J between neighbours. Its sign decides ferromagnetic (aligned) or antiferromagnetic (alternating) order. | energy |
| `chHx` | Transverse field h along x. In the transverse-field Ising chain the quantum phase transition sits at h = /J/. | energy |
| `chD` | Anisotropy Δ of the XXZ chain: Δ = 1 is the isotropic Heisenberg chain, Δ = 0 the XY chain (free fermions), /Δ/ > 1 Ising-like. | ratio |
| `chW` | Random field on each site, drawn from [−W, W]. Strong disorder can stop the chain from thermalising (many-body localisation). | energy |

## Lattice QCD

| id | meaning | unit |
|---|---|---|
| `qBs` | Lattice coupling β = 2N/g². A larger β means a weaker bare coupling and a finer lattice, closer to the continuum; a small β confines strongly. | dimensionless |
| `qLs` | Sites per side of the 2D lattice (L × L). | sites |
| `qSws` | Monte Carlo heat-bath sweeps per second; one sweep updates every link once. | sweeps per second |
| `qRs` | Spatial size R of the Wilson loop: the distance between the static quark and antiquark. | lattice spacings |
| `qTs` | Time extent T of the Wilson loop. The potential is V(R) = −ln[W(R, T+1) / W(R, T)]. | lattice spacings |

## Superconducting metal

| id | meaning | unit |
|---|---|---|
| `sgTs` | Temperature in units of the critical temperature T_c. Below 1 the metal superconducts. | T / T_c |
| `sgTrs` | How fast the temperature changes during a cooling or heating sweep. | T_c per time |
| `sgHs` | Applied magnetic field in units of the upper critical field H_c2. Above 1 superconductivity is destroyed. | H / H_c2 |
| `sgHrs` | How fast the applied field is ramped. | H_c2 per time |
| `sgIs` | Transport current through the wire. Above the critical current vortices move and resistance appears. | current units |
| `sgKs` | Ginzburg–Landau parameter κ = λ/ξ (penetration depth over coherence length). Below 1/√2 ≈ 0.71 type I expels the field completely; above it type II lets it in as a vortex lattice. | dimensionless |
| `sgSs` | Conductivity σ of the normal electrons. It sets how fast flux diffuses and how much heat moving vortices make. | × |
| `sgSps` | Solver steps per frame, multiplied by the speed slider. | steps |
| `sgNs` | Grid resolution N × N. Finer grids show smaller vortices but run slower. | cells per side |

## Selected object and sandbox

| id | meaning | unit |
|---|---|---|
| `oS` | Helicity s of the selected twistor: ±½ neutrino-like, ±1 photon-like; the sign sets the handedness of its twist. | units of ħ |
| `oE` | Energy of the selected twistor; its field pattern shrinks as 1/E. | lab units |
| `oT` | Polar angle of the selected object’s axis or momentum, measured from +z. | degrees |
| `oF` | Azimuth of the selected object’s axis or momentum around z. | degrees |
| `oX` | Phase χ of the selected object: turns its complex phase without moving it. | degrees |
| `oM` | Charge m of the selected object: the strength of its field. | charge units |
| `oA` | Core radius a of the selected object: smooths the field inside it. | lab units |
| `eSp` | Speed of the sandbox object along its path, or its spin rate for a spinor. | rate |
| `eSz` | Radius or length of the sandbox object. | lab units |
| `eTw` | Twist (helicity) of the sandbox object: how far its light rays wind around the axis. | degrees |

## Law Lab

| id | meaning | unit |
|---|---|---|
| `eqDt` | Time step of the Runge–Kutta integrator. Smaller is more accurate but slower; RK4's error shrinks like dt⁴. | time units |
| `eqRate` | How much model time passes per real second (multiplied by the speed slider). If the step budget runs out the run slows down instead of losing accuracy. | time units per second |
| `eqCopies` | How many copies of your system run side by side. They start almost together so you can watch whether they separate (chaos) or stay together. | copies |
| `eqEps` | How far apart the copies start: the size of the random nudge added to each starting value. Large values scatter them across phase space. | units of your variables |
| `eqTrail` | How much history each copy keeps on screen. | × |
| `eqPa` | Variable on the horizontal axis of the phase portrait and the Poincaré section. | variable |
| `eqPb` | Variable on the vertical axis of the phase portrait and the Poincaré section. | variable |
| `eqPs` | The Poincaré section records a dot each time this variable rises through the level below. | variable |
| `eqPc` | Level at which the section variable is crossed. | units of the section variable |
| `eqN` | Number of particles. Each step computes every pair, so the cost grows like N². | particles |
| `eqR0` | Size of the starting cloud, disk or lattice. | view units |
| `eqV0` | Typical starting speed. | view units per time |
| `eqMs` | Spread of masses: 0 gives equal masses, larger values give a log-normal mix of light and heavy particles. | log spread |
| `eqNdt` | Time step of velocity Verlet. Close encounters need a small step; watch the energy drift. | time units |
| `eqSoft` | Softening length ε: the distance used is √(r² + ε²), which tames the infinite forces of exact collisions. | view units |
| `eqGL` | Half the width of the square domain, so each grid cell is 2L/N wide. | length units |
| `eqGdt` | Time step. Diffusion needs dt below about h²/(4D) and waves need c·dt below about h/√2; if it blows up, the step is halved automatically. | time units |
| `eqHs` | How tall the field's surface is drawn. | × |
| `eqDw` | Width of the drop added when you click the field panel. | length units |
| `eqDa` | Strength of each drop; negative values make dips. | field units |
| `eqMR` | Half the width of the visible region of the x, y (or complex) plane. The mouse wheel over the map changes it too. | plane units |
| `eqMx` | x (real part) at the centre of the view; drag the map to move it. | plane units |
| `eqMy` | y (imaginary part) at the centre of the view. | plane units |
| `eqRes` | Number of grid points per side of the 3D mesh. | points |
| `eqMh` | How tall the surface is drawn; 1 is true scale for surfaces. | × |
| `eqMcs` | How fast the point with its moving frame travels along the curve. | curve lengths per time |
| `svEqPs` | The Poincaré section marks a dot each time this variable rises through the level. | variable |
| `svEqPc` | Level at which the crossing variable is counted. | units of the variable |
| `svEqHr` | Largest pair distance in the histogram. | × the box size |
| `svEqGs` | Show the other field, or a cut through the field drawn in 3D. | view |
| `svEqCut` | Height of the horizontal cut through the field. | as x and y |
| `svEqWz` | How much wider than the main view the wide view is. | × |
| `svEqMs` | Show arrows pointing uphill, or a cut through the surface. | view |
| `svEqCut2` | Height of the cut through the surface. | as x and y |

## Fluid Lab

| id | meaning | unit |
|---|---|---|
| `flBc` | Where the fluid comes from and where it goes. | boundary type |
| `flRe` | Reynolds number Re = U·D/ν. Sets the viscosity for the chosen speed and obstacle size. Low: smooth and steady; high: vortices and turbulence. | dimensionless |
| `flU0` | Flow speed in lattice units (cells per step). Keep it below about 0.15: the method is only accurate well below the speed of sound (about 0.58). | cells per step |
| `flSmag` | Smagorinsky constant: adds viscosity where the flow is strongly sheared, standing in for eddies smaller than the grid. Needed for high Re. | dimensionless |
| `flGf` | How hard the pressure difference pushes fluid along the channel. 1 keeps the centre speed at the flow speed above; the parabola grows with it. | × the balanced push |
| `flSrc` | What drives the smoke flow: a heater, hot and cold walls, a heavy layer on top, a vortex pair, a jet or your stirring. | source |
| `flBc2` | Walls around the box, an outflow at the right, or periodic sides. | boundary type |
| `flBuoy` | How strongly warm fluid is pushed up (and heavy fluid down). | relative |
| `flHeat` | How much heat the heater adds each step, or the temperature of the hot floor. | relative |
| `flDyeR` | How much smoke the source adds each step. | relative |
| `flVc` | Vorticity confinement: puts back small swirls that the coarse grid smears out. Too much makes the flow noisy. | relative |
| `flDiss` | How fast smoke and heat fade away. | per step |
| `flKap` | How fast heat spreads by conduction. Larger values calm the convection. | cells² per step |
| `flU0b` | Speed of the jet entering from the left wall. | cells per step |
| `flObs` | The obstacle placed in the flow. Changing it restarts the flow. | shape |
| `flOsz` | Obstacle size as a fraction of the domain height. Sets the length D in the Reynolds and Strouhal numbers. | fraction of the height |
| `flOang` | Rotation of the obstacle: the angle of attack of a wing. | degrees |
| `flOx` | Where the obstacle sits along the flow. | fraction of the length |
| `flOy` | Shift of the obstacle across the flow. A small offset helps the vortex street start. | fraction of the height |
| `flTool` | What dragging on the top view does: draw walls, erase them, stir the fluid or add dye. | tool |
| `flBrush` | Radius of the drawing brush. | cells |
| `flCol` | The quantity shown by colour and height: spin (vorticity), speed, pressure, dye or temperature. | quantity |
| `flCm` | Colour map for the chosen quantity. | colours |
| `flHs` | How far the surface is lifted by the chosen quantity. 0 is flat. | × |
| `flTrc` | Number of massless tracer particles carried by the flow. | particles |
| `flTrl` | Length of the tracer trails. | × |
| `flPx` | Horizontal position of the probe (yellow ring) whose vertical velocity is plotted. | fraction of the length |
| `flPy` | Vertical position of the probe. | fraction of the height |
| `flProf` | Where the speed profile in the slice panel is cut. | fraction of the length |
| `flNx` | Number of cells along the flow. More cells resolve smaller eddies but cost more. | cells |
| `flAsp` | Length of the domain compared with its height. | ratio |
| `flRate` | Simulation steps per real second, relative to normal. | × |
| `svFlDir` | Cut the profile across the flow (a vertical line) or along it (a horizontal line). | direction |
| `svFlPos` | Where the dashed cut line sits. | fraction of the length or height |

## Calc Lab

| id | meaning | unit |
|---|---|---|
| `cxFs` | Choose a surface z = f(x, y), or type your own below. | preset |
| `cxFe` | Type any formula in x and y, for example  sin(x)*cos(y)  or  exp(-(x^2 + y^2)). Use ^ for powers. | formula |
| `cxFp` | Parameters become sliders. Write them like  a = 1 [0, 2]; k = 3  and use a and k in the formula. | parameters |
| `cxR` | Half the width of the square shown, in the units of x and y. | units |
| `cxZs` | Stretches the surface up and down without changing any numbers. | factor |
| `cxRes` | Number of grid points per side used for drawing and for finding critical points. | points |
| `cxCby` | What the colours on the surface show. | colour |
| `cxPx` | x of the point being studied. You can also drag it on the top view. | units |
| `cxPy` | y of the point being studied. You can also drag it on the top view. | units |
| `cxAng` | The direction u for the directional derivative, measured from the x axis. | degrees |
| `cxCon` | The constraint curve g(x, y) = c for Lagrange multipliers. | curve |
| `cxReg` | The region D of the double integral. | region |
| `cxCo` | Square cells dx dy or polar tiles r dr dθ. | coordinates |
| `cxN` | How many cells (or rings) across the region. More cells, better sum. | cells |
| `cxRule` | Where in each cell f is sampled for the Riemann sum. | rule |
| `cxV2` | Choose a field F = (P, Q), or type your own below. | preset |
| `cxV2P` | The x part of the field, any formula in x, y and t. | formula |
| `cxV2Q` | The y part of the field, any formula in x, y and t. | formula |
| `cxCol` | What the background colour shows. | colour |
| `cxLift` | Turns the colour into height in the 3D view. | amount |
| `cxNp` | How many tracer particles ride the flow. | particles |
| `cxCur` | The closed loop C for line integrals and Green’s theorem. | shape |
| `cxIv` | Arrows along C show either the flow along it (circulation) or across it (flux). | arrows |
| `cxV3` | Choose a field F = (P, Q, R) in space, or type your own below. | preset |
| `cxSf` | The closed surface whose flux is compared with the divergence inside. | shape |
| `cxBul` | How far the cap bulges out of the loop. Stokes says the answer does not change. | bulge |
| `cxSlz` | Position of the coloured slice along the axis it cuts. | units |
| `cxSlp` | Which plane the coloured slice lies in: xy, yz or zx. The slider below moves it along the third axis. | plane |
| `cxVpl` | Which plane the cross-section lies in. The sweep moves it along the third axis. | plane |
| `cxVcut` | Where the cross-section cuts the solid when the sweep is off, from one end (0%) to the other (100%). | fraction |
| `cxCsh` | What the slice through the field shows. | colour |
| `cxPs` | Choose a surface r(u, v), or type your own below. | preset |
| `cxPcol` | What the colours on the surface show. | colour |
| `cxTmorph` | Scales every shape tool at once: 0 is the plain surface, 1 the full effect. | fraction |
| `cxMp` | Choose a map of the plane, or type your own w(z) or (u, v). | preset |
| `cxMt` | Slides from the identity map (0) to the full map (1). | fraction |
| `cxMcol` | What the colours on the mapped plane show. | colour |
| `cxAf` | The body in the wind. | body |
| `cxAl` | Angle between the wind and the wing chord. | degrees |
| `cxG` | Circulation round the body, clockwise counted positive. | circulation |
| `cxSol` | The solid to integrate over. | solid |
| `cxRho` | Density ρ(x, y, z, w) of the solid. | density |
| `cxVco` | Shape of the cells: boxes, cylindrical wedges or spherical wedges. | coordinates |
| `cxVn` | Cells per direction. | cells |
| `cxVw` | Which 3D slice of the 4D solid to show. | units |
| `cxRate` | How fast the animations run. | factor |
| `cxHf` | Choose a hypersurface f(x, y, z, w) = c, or type your own. | shape |
| `cxHe` | Any formula in x, y, z and w. Parameters go in the box below. | formula |
| `cxHc` | The level c of the hypersurface f = c. | value |
| `cxHw` | Which 3D slice of the 4D picture is shown. | units |
| `cxHwm` | How far the sweep travels in w. | units |
| `cxHres` | Grid points per side used to build the slice surface. | points |
| `cxHcol` | What the colours on the slice surface show. | colour |
| `cxPz` | z of the point being studied. | units |
| `cxV4` | Choose a 4D vector field, or type your own. | field |
| `cxV4P` | The x part of the field. | formula |
| `cxV4Q` | The y part of the field. | formula |
| `cxV4R` | The z part of the field. | formula |
| `cxV4S` | The w part of the field. | formula |
| `cxV4b` | The closed hypersurface for the 4D divergence theorem. | shape |
| `cxV4a` | Radius of the 3-sphere, or half-width of the tesseract. | units |
| `cxAn4` | Arrows per side in the slice. | count |
| `cxNp4` | How many particles move through 4D space. | count |
| `cxSvv` | What the slice panel shows: a cut through the picture by a plane, or the chart that belongs to this topic. | view |
| `cxCpos` | Where the cutting plane sits along the axis it cuts. | units |

## Slice viewer and history

| id | meaning | unit |
|---|---|---|
| `hsR` | Scrub back through the recorded run. Moving it pauses the simulation; press live to continue from now. | seconds of real time |
| `svZoom` | How much of space the slice shows around its centre. | × the box size |
| `svOff` | Moves the cut plane along the axis that is not in the slice. | view units |
