---
tags: [reference, glossary]
---
# Glossary

The in-app glossary (`GLOS`, 202 terms in 11 groups; open it with **G**). Which groups each lab shows first is set by `GLSET`: tw → st/ge, ca → ge/st, oc → al, su → al/pa, cl → al/st, qb → al/qm, se → al, la → la/qm, un → pa/co, eq → dy/la/ge, fl → fl/dy/la, cx → cx/ge.

## Spacetime and twistors (`st`)

- **Twistor**: A point of twistor space ℂ⁴, written Z = (ω, π). Each twistor stands for a twisting family of light rays in spacetime; Penrose built it so that light rays become the basic objects instead of points.
- **Bi-twistor**: A pair of twistors (Z₁, Z₂), a point of ℂ⁸. Two twistors together can describe a massive particle, because two light-like momenta add up to a time-like one.
- **Penrose transform**: The rule that turns a function on twistor space into a massless field on spacetime, φ = ∮ f(Z) dπ. It is how the lab gets the light field it draws from each twistor.
- **Robinson congruence**: The family of twisting light rays belonging to one twistor. Seen at an instant, the rays wind around nested tori: the picture behind the twisting streaks.
- **Helicity**: The spin of a massless particle along its direction of motion: ±½ for neutrinos, ±1 for photons, ±2 for gravitons. In twistor theory it is half of Σ(Z, Z).
- **Null vector**: A spacetime vector of zero length, p·p = 0: the momentum of anything that moves at the speed of light.
- **Lorentz boost**: A change to a moving frame of reference. Its size is the rapidity η, and the speed is v = c·tanh η.
- **Rapidity**: The additive measure of a boost: two boosts along one line add their rapidities, while their speeds do not simply add.
- **Dilation**: Scaling all lengths by the same factor e^λ. Massless fields keep their shape under it, which makes them conformally invariant.
- **Special conformal transformation**: An inversion, a translation and another inversion. It bends straight lines into circles but keeps every angle.
- **Conformal group**: All transformations of spacetime that keep angles: rotations, boosts, translations, dilations and special conformal maps. In twistor space they act as the linear group SU(2, 2).
- **Klein quadric**: The space of lines in twistor projective space. Each point of complexified spacetime is such a line; the Plücker relation says which pairs of twistors span one.
- **Plücker relation**: The single quadratic equation P⁰¹P²³ − P⁰²P¹³ + P⁰³P¹² = 0 that the coordinates of a line must obey.

## Geometry (`ge`)

- **Hopf fibration**: A way to fill the 3-sphere S³ with circles, any two of them linked once. Its stereographic picture is the nested tori seen in the light-knot scenes.
- **Hopfion**: A knotted field configuration whose field lines follow Hopf circles. The light knot in the first scene is a hopfion of the electromagnetic field.
- **Stereographic projection**: Projecting a sphere onto flat space from one pole. It keeps angles and circles, which is why the 4D views use it for S³.
- **Isoclinic rotation**: A 4D rotation that turns two orthogonal planes by the same angle. Every rotation of ℝ⁴ is a left one followed by a right one.
- **Torus knot**: A closed curve on the surface of a torus winding p times one way and q times the other. (2, 3) is the trefoil.
- **Courant algebroid**: The bundle T ⊕ T* of vectors plus 1-forms, with a pairing and the Courant bracket. It is the stage of generalised geometry and of T-duality in string theory.
- **Generalised geometry**: Geometry built on T ⊕ T* instead of only T, so that metrics, B-fields and symplectic forms become parts of one object.
- **B-field**: A 2-form B that acts on T ⊕ T* by X + ξ ↦ X + ξ + ι_X B. In string theory it is the Kalb–Ramond field that strings couple to.
- **T-duality**: The string-theory symmetry that swaps a circle of radius R with one of radius 1/R, exchanging momentum and winding. In the Courant picture it swaps vectors with forms.
- **Dirac structure**: A maximal isotropic subbundle of T ⊕ T* closed under the Courant bracket. Graphs of closed 2-forms and of Poisson structures are examples.
- **Anti-de Sitter space**: A spacetime with constant negative curvature, radius L. It is the bulk of the AdS/CFT correspondence.
- **Calabi–Yau manifold**: A Ricci-flat complex manifold used to curl up the 6 extra dimensions of superstring theory. The lab draws the classic 2D slice of the Fermat quintic.
- **Supertwistor**: A twistor with 𝒩 extra fermionic (Grassmann) coordinates, ℂ^{4|𝒩}. Expanding a function in them gives a whole supersymmetric multiplet at once.

## Algebras (`al`)

- **Quaternions**: The 4D number system ℍ with i² = j² = k² = ijk = −1. Multiplication is associative but not commutative; unit quaternions are the 3-sphere.
- **Octonions**: The 8D number system 𝕆 built by doubling the quaternions. Multiplication is neither commutative nor associative, though every two elements still generate an associative subalgebra.
- **Associator**: (ab)c − a(bc). Zero for real, complex and quaternion numbers, nonzero for octonions; the octonion scenes measure it.
- **Sedenions**: The 16D algebra from doubling the octonions once more. They have zero divisors: two nonzero sedenions can multiply to zero.
- **Zero divisor**: A nonzero element a with ab = 0 for some nonzero b. Sedenions have them, so they are no longer a division algebra.
- **Cayley–Dickson construction**: Doubling an algebra by pairs (a, b) with a twisted product: ℝ → ℂ → ℍ → 𝕆 → sedenions, losing a property at every step.
- **Clifford algebra**: An algebra generated by vectors with v² = |v|². The spacetime algebra Cl(1,3) writes the electromagnetic field as one object F = E + IB.
- **Null field**: An electromagnetic field with E ⟂ B and |E| = |B|, so both invariants vanish. Light far from its source is null.
- **su(3)**: The Lie algebra of SU(3), the colour symmetry of the strong force. Its 8 generators are the Gell-Mann matrices, matching the 8 gluons.
- **Gell-Mann matrices**: Eight 3 × 3 matrices that span su(3), the way the Pauli matrices span su(2).

## Quantum (`qm`)

- **Qubit**: A two-level quantum system, state α|0⟩ + β|1⟩. Three qubits have 8 complex amplitudes, the same count as a bi-twistor.
- **Entanglement**: Correlation between quantum systems that no description of the parts alone can give. GHZ and W states are the two inequivalent kinds for three qubits.
- **GHZ state**: (|000⟩ + |111⟩)/√2: three qubits that are all equal, with no pairwise entanglement left after one is traced out.
- **W state**: (|001⟩ + |010⟩ + |100⟩)/√3: one excitation shared by three qubits; it keeps pairwise entanglement if one is lost.
- **Non-commutative geometry**: Geometry in which coordinates do not commute, [x, y] = iθ, so a point cannot be located more sharply than about √θ.
- **Moyal product**: The star product f ⋆ g that replaces ordinary multiplication on a non-commutative plane, to first order f g + (iθ/2){f, g}.
- **Fuzzy sphere**: A sphere whose coordinates are spin-j matrices, so it has only 2j + 1 cells: the simplest non-commutative space.
- **Quantum group**: A deformation of a symmetry group by a parameter q, such as SU_q(2). At q = 1 the ordinary group comes back.
- **Path integral**: Feynman’s formulation: a particle takes every path, each weighted by e^{iS/ħ}, and the paths near the classical one add up most.
- **Planck constant ħ**: The quantum of action. It sets how far quantum behaviour spreads around classical motion.
- **Soliton**: A lump of field energy that keeps its shape while it moves, held together by non-linearity or by topology.
- **Kink**: A 1D soliton that steps between two vacua, the simplest topological defect.
- **Instanton**: A solution of the equations in imaginary time that tunnels between vacua. Yang–Mills instantons have a free size ρ.
- **Winding number**: An integer that counts how many times a field wraps around its vacuum manifold. Smooth changes cannot alter it.
- **Supersymmetry**: A symmetry that turns bosons into fermions. Its parameter ε is a Grassmann number.
- **Grassmann number**: A number that anticommutes, θη = −ηθ, so θ² = 0. They are the coordinates of fermions.

## Lattice and materials (`la`)

- **Lattice field theory**: A field theory on a grid of points in space (and sometimes time). It is how quantum fields are simulated on computers.
- **Higgs field**: A field whose potential λ(|φ|² − v²)² has its minimum away from zero. Its settling to |φ| = v gives particles mass.
- **Spontaneous symmetry breaking**: When the laws are symmetric but the state is not, like a pencil falling one way. Separate regions can choose differently and leave defects between them.
- **Cosmic string**: A line defect around which the phase of a complex field winds by 2π. In the complex Higgs model it forms after a quench.
- **Domain wall**: A sheet separating regions in different vacua of a real field.
- **Kibble–Zurek mechanism**: A fast quench leaves defects, because distant regions cannot agree in time; slower cooling leaves fewer.
- **Gauge field**: A field that keeps a local symmetry intact, such as the electromagnetic potential or the gluon field. On a lattice it lives on links between sites.
- **Plaquette**: The smallest square of a lattice. The product of the link variables around it measures the field strength there.
- **Wilson loop**: The product of gauge links around a closed loop. Its decay with loop area signals confinement and gives the quark potential V(R).
- **Confinement**: Quarks cannot be pulled apart: the energy between them grows linearly with distance, like a stretching string.
- **String tension**: The energy per length of the colour flux tube between quarks, about 1 GeV per femtometre in nature.
- **Heat-bath algorithm**: A Monte Carlo update that redraws each link from its exact local probability distribution.
- **Dirac equation**: The relativistic equation for spin-½ particles such as electrons. On a lattice it brings fermion doublers unless a Wilson term is added.
- **Klein paradox**: A Dirac particle hitting a wall higher than 2mc² passes through, because the wall turns into antiparticle states.
- **Bose–Einstein condensate**: A gas cooled until most atoms share one quantum state. It flows without friction and forms quantised vortices when stirred.
- **Gross–Pitaevskii equation**: The non-linear Schrödinger equation iħψ̇ = (−∇²/2m + V + g|ψ|²)ψ for a condensate.
- **Superconductor**: A metal with zero electrical resistance below a critical temperature T_c, because electrons pair into Cooper pairs.
- **Meissner effect**: A superconductor pushes magnetic fields out of its interior; the field only enters a thin layer of depth λ.
- **Ginzburg–Landau theory**: The field theory of superconductivity with an order parameter ψ and a vector potential A. Its ratio κ = λ/ξ separates type I from type II.
- **Abrikosov vortex**: A tube of magnetic flux through a type-II superconductor, carrying one flux quantum h/2e. Many of them form a triangular lattice.
- **Coherence length ξ**: The distance over which the superconducting order parameter can change.
- **Penetration depth λ**: How far a magnetic field reaches into a superconductor before it is screened.
- **Skyrmion**: A small whirl of spins that cannot be smoothly unwound. Its topological charge counts how often the spins cover the sphere.
- **Spin chain**: Quantum spins in a row coupled to their neighbours. Small chains can be solved exactly, with 2^N amplitudes.
- **Transverse-field Ising model**: Spins with Ising coupling J and a sideways field h. At h = J it has a quantum phase transition.
- **Many-body localisation**: Strong disorder can stop an interacting quantum system from ever thermalising, so it remembers its starting state.

## Particles (`pa`)

- **Quark**: A matter particle with colour charge. Six flavours: up, down, strange, charm, bottom, top. Never seen alone because of confinement.
- **Gluon**: The carrier of the strong force. It has colour charge itself, which is why the force confines.
- **Hadron**: A bound state of quarks: baryons (three quarks, like the proton) and mesons (quark plus antiquark, like the pion).
- **Lepton**: A matter particle without colour: electron, muon, tau and their neutrinos.
- **Neutrino oscillation**: Neutrinos change flavour as they travel, because flavour and mass states differ. The oscillation length grows like E/Δm².
- **W and Z bosons**: The heavy carriers of the weak force, about 80 and 91 GeV. W’s change one flavour into another, which drives beta decay.
- **Higgs boson**: The particle of the Higgs field, about 125 GeV, found at the LHC in 2012.
- **Antiparticle**: A partner with the same mass and opposite charges. A particle and its antiparticle can annihilate into energy.
- **Decay**: An unstable particle turning into lighter ones. Its lifetime τ is the time after which 1/e of a sample survives; moving particles live longer by time dilation.
- **Bubble chamber**: A detector of superheated liquid in which charged particles leave trails of bubbles; a magnetic field curls the tracks.

## Cosmos and stars (`co`)

- **Hawking radiation**: Black holes glow thermally at a temperature inversely proportional to their mass, so small ones evaporate.
- **Schwarzschild radius**: r_s = 2GM/c², the size of a black hole’s event horizon.
- **Gravitational waves**: Ripples in spacetime from accelerating masses. A black-hole binary radiates them, spirals in and ends with a chirp.
- **Hubble expansion**: Space stretches, so distant objects recede at v = H·d and their light is redshifted.
- **Cosmological constant**: Λ, the energy of empty space. It drives the accelerating expansion we call dark energy.
- **Big Bang nucleosynthesis**: The first minutes, when protons and neutrons fused into helium, deuterium and lithium.
- **Recombination**: About 380 000 years after the Big Bang, electrons joined nuclei, the universe became transparent and the cosmic microwave background was released.
- **Main sequence**: The long stable phase of a star burning hydrogen in its core. Heavier stars burn hotter and live much shorter lives.
- **White dwarf**: The hot, Earth-sized core left by a star like the Sun, held up by electron degeneracy pressure up to the Chandrasekhar mass, 1.4 M☉.
- **Supernova**: The explosion of a massive star when its core collapses, leaving a neutron star or a black hole.
- **Neutron star**: A collapsed core about 20 km across, as dense as an atomic nucleus.

## Using the lab (`ap`)

- **Probe**: A marker you drop by clicking the 3D view. It reports the field at that point in the telemetry section.
- **Telemetry**: Live readings of the running simulation with a 12-second trace. Pin up to 4 so they stay on screen.
- **Timeline**: The recording under the 3D view: drag back through the run and continue from any moment.
- **Compare**: Freeze a moment as A and set it beside B, live or captured, with the readings and the settings that differ.
- **Scene**: A ready-made starting point with chosen settings. ↺ on a settings section returns it to the scene’s values.
- **Law Lab**: The set where you write your own equations; each named number becomes a slider and the result runs with all the lab's tools.

## Dynamics (`dy`)

- **Differential equation**: A law that says how a quantity changes: x' = f(x, t). Solving it means following the change step by step from a starting value.
- **Phase space**: The space of all states of a system, for example position and velocity. A solution is a curve through it; the phase portrait draws those curves.
- **Chaos**: Deterministic motion that is so sensitive to its starting point that tiny differences grow exponentially, making long-term prediction impossible.
- **Lyapunov exponent**: The rate λ at which nearby solutions separate, like e^{λt}. Positive means chaos; the Law Lab measures it with a shadow copy.
- **Strange attractor**: The fractal set that chaotic motion settles onto, like the Lorenz butterfly. Nearby points on it still separate.
- **Limit cycle**: A closed orbit that nearby solutions spiral onto, so the system oscillates with one amplitude whatever its start.
- **Poincaré section**: A slice through phase space: mark a dot each time the orbit crosses it. Curves mean regular motion, scattered dust means chaos.
- **Bifurcation**: A sudden qualitative change as a parameter passes a value, like a fixed point turning into an oscillation or a period doubling.
- **Runge–Kutta method**: A way to integrate x' = f(x) by sampling the slope four times per step. Its error shrinks like dt⁴.
- **Symplectic integrator**: A stepping rule, such as velocity Verlet, that respects the geometry of mechanics, so energy errors stay bounded over very long runs.
- **N-body problem**: Predicting the motion of many bodies that all pull on each other. Beyond two bodies there is no general formula, so it is computed step by step.
- **Virial theorem**: For a settled gravitating system, twice the kinetic energy equals minus the potential energy: 2K = −U.
- **Bertrand's theorem**: Only two central forces make every bound orbit close: gravity (1/r²) and a spring (∝ r).
- **Lennard-Jones potential**: U = 4ε[(σ/r)¹² − (σ/r)⁶]: the standard model of how neutral atoms attract at a distance and repel up close.
- **Langevin thermostat**: Friction plus random kicks of the right size, which keep particles at a chosen temperature.
- **Partial differential equation**: A law for a field that relates its change in time to its shape in space, such as u_t = D·∇²u.
- **Laplacian**: ∇²u, the difference between u and the average of its surroundings. It drives diffusion and appears in waves and quantum mechanics.
- **Diffusion**: Spreading by random motion: u_t = D∇²u. Peaks flatten and the total amount stays the same.
- **Wave equation**: u_tt = c²∇²u: disturbances travel at speed c, reflect and interfere.
- **Reaction–diffusion**: Chemicals that react locally and spread at different rates. Turing showed this can create spots and stripes from nothing.
- **Turing pattern**: A pattern that forms by itself when an activator spreads slower than its inhibitor, as in animal coats.
- **CFL condition**: For explicit time steps, information must not jump more than one grid cell per step; otherwise the simulation blows up.
- **Excitable medium**: A medium that fires a pulse when kicked hard enough, then needs time to recover, such as heart muscle or forest fires.
- **Complex function**: A function f(z) of a complex number z = x + iy. Smooth ones (holomorphic) are rigid: knowing them on a small piece fixes them everywhere.
- **Domain colouring**: Drawing f(z) by colouring each point by the argument of f, with brightness for its size. Zeros show every colour around them.
- **Argument principle**: Going once around a closed curve, the argument of f winds (zeros − poles inside) times.
- **Riemann zeta function**: ζ(s) = Σ 1/nˢ, continued to the whole complex plane. Its zeros encode the distribution of prime numbers.
- **Gamma function**: The smooth extension of the factorial: Γ(n) = (n − 1)!. It has poles at 0, −1, −2, … and no zeros.
- **Curvature and torsion**: How sharply a curve bends (κ) and how fast it twists out of its plane (τ). Together they fix the curve's shape.

## Fluids (`fl`)

- **Navier–Stokes equations**: The law of motion of a fluid: each bit of fluid is accelerated by pressure differences and slowed by viscosity, while mass is conserved.
- **Reynolds number**: Re = U·D/ν compares inertia with viscosity. Low Re flows are smooth and orderly (honey); high Re flows break into eddies and turbulence (air around a car).
- **Vorticity**: How fast the fluid spins locally: half the curl of the velocity. Vortices are compact blobs of vorticity.
- **Kármán vortex street**: The double row of alternating vortices shed behind a bluff body, seen behind islands in cloud photos and heard as the singing of wires in the wind.
- **Strouhal number**: St = f·D/U, the dimensionless shedding frequency. For a cylinder it stays close to 0.2 over a huge range of Reynolds numbers.
- **Drag coefficient**: Cd = drag force / (½ρU²D): how strongly a shape resists the flow, independent of its size and the flow speed.
- **Lift**: The force across the flow on a body, such as a wing. It comes from lower pressure on one side, which is why the flow there is faster.
- **Stall**: When a wing is tilted too much the flow separates from its upper surface: lift drops and drag rises.
- **Boundary layer**: The thin layer next to a wall where the fluid slows from the free-stream speed to zero. Where it separates, wakes and vortices begin.
- **Lattice Boltzmann method**: A fluid solver that tracks populations of particles moving along a few fixed directions on a grid. They stream to neighbours and collide; the Navier–Stokes equations come out on average.
- **Mach number**: Flow speed divided by the speed of sound. The lattice Boltzmann method is only accurate well below Mach 0.3.
- **Turbulence**: Chaotic flow with eddies of all sizes, from the size of the obstacle down to tiny swirls where viscosity finally turns motion into heat.
- **Eddy viscosity**: A model for turbulence too small for the grid: extra viscosity where the flow is strongly sheared (Smagorinsky).
- **Poiseuille flow**: Steady flow in a channel or pipe pushed by a pressure difference. The speed profile is a parabola, fastest in the middle.
- **Bernoulli principle**: Along a streamline, faster flow has lower pressure. That is why a narrowing tube (venturi) sucks and why wings lift.
- **Kelvin–Helmholtz instability**: When two layers slide past each other, waves on the interface grow and roll up into billows.
- **Rayleigh–Bénard convection**: A fluid heated from below rolls into convection cells once the heating is strong enough compared with viscosity and heat conduction.
- **Rayleigh–Taylor instability**: Heavy fluid on top of light fluid is unstable: any ripple grows into falling fingers and rising mushrooms.
- **Buoyancy**: The upward push on fluid that is lighter (for example hotter) than its surroundings.
- **Incompressible flow**: Flow whose volume never changes, so the divergence of the velocity is zero. The smoke solver enforces it every step with a pressure projection.
- **Vorticity confinement**: A small force that puts back the spin a coarse grid smears out, keeping small swirls alive in smoke simulations.
- **Tracer particle**: A massless marker carried by the flow. Its path shows where the fluid goes; many of them together show streaklines.
- **Tesla valve**: A fixed-geometry check valve: side loops make flow in one direction much harder than in the other, with no moving parts. Its quality is the diodicity, the ratio of the flow rates for the same push.

## Calculus (`cx`)

- **Partial derivative**: How fast f changes when only one variable moves: ∂f/∂x holds y fixed. It is the slope of the slice of the surface along x.
- **Tangent plane**: The plane that touches a smooth surface at a point: z − z₀ = f_x (x − x₀) + f_y (y − y₀). Close to the point, the surface and the plane are nearly the same.
- **Directional derivative**: The slope of f in a chosen direction u: D_u f = ∇f · u. It is largest along the gradient and zero along a contour.
- **Gradient**: The vector ∇f = (∂f/∂x, ∂f/∂y) pointing straight uphill. Its length is the steepest slope, and it crosses every contour at right angles.
- **Contour line**: A curve where f has the same value, like height lines on a map.
- **Critical point**: A point where ∇f = 0: a peak, a pit, a saddle or something flatter.
- **Hessian**: The matrix of second derivatives [[f_xx, f_xy], [f_xy, f_yy]]. Its determinant sorts critical points: positive means peak or pit, negative means saddle.
- **Lagrange multiplier**: To find the extremes of f on a curve g = c, look for points where ∇f = λ ∇g: the contour of f just touches the curve.
- **Double integral**: ∬_D f dA adds f times tiny areas over a region D: the signed volume under the surface. Riemann sums of columns approach it as the cells shrink.
- **Polar coordinates**: Describe a point by its distance r and angle θ. A small polar tile has area r dr dθ, so the outer tiles are bigger.
- **Jacobian**: The matrix of partial derivatives of a map. Its determinant is the factor by which the map scales small areas (or volumes); a negative determinant means the map flips orientation.
- **Fubini’s theorem**: A double integral can be done one variable at a time: slice, integrate each slice, then add the slices.
- **Vector field**: An arrow attached to every point, such as wind velocity or a force.
- **Curl**: How much a vector field spins at a point. A tiny paddle wheel turns at half the curl.
- **Divergence**: How much a vector field spreads out from a point: the flux out of a tiny region per unit volume.
- **Line integral**: ∫ F · dr adds the part of F along a path. Round a closed loop it is the circulation.
- **Circulation**: The line integral of a field round a closed loop. For air round a wing it decides the lift.
- **Flux**: How much of a field flows through a curve or surface: ∫ F · n ds in the plane, ∬ F · dS in space.
- **Green’s theorem**: In the plane, the circulation round a loop equals the integral of the curl inside it: ∮ F · dr = ∬ (Q_x − P_y) dA. The flux form does the same for divergence.
- **Stokes’ theorem**: The circulation round a loop equals the flux of the curl through any surface with that loop as its edge.
- **Divergence theorem**: The flux out of a closed surface equals the integral of the divergence over the volume inside.
- **Conservative field**: A field that is the gradient of a potential, F = ∇φ. It has no curl and every loop integral is zero.
- **Gaussian curvature**: K = k₁k₂, the product of the two principal curvatures. Positive on a cap, negative on a saddle, zero on a cylinder.
- **Mean curvature**: H = (k₁ + k₂)/2. Soap films have H = 0 and are called minimal surfaces.
- **Gauss–Bonnet theorem**: For a closed surface the total curvature ∬ K dA equals 2π times the Euler characteristic: 4π for a sphere, 0 for a torus, whatever the bending.
- **First fundamental form**: The numbers E, F, G that say how lengths and angles in the (u, v) parameters turn into lengths and angles on the surface.
- **Conformal map**: A map that keeps angles. Analytic complex functions are conformal wherever their derivative is not zero; the Cauchy–Riemann equations test this.
- **Joukowski map**: w = z + 1/z. It turns circles through z = 1 into wing shapes, so the easy flow round a circle becomes the flow round a wing.
- **Kutta condition**: The rule that air leaves a sharp trailing edge smoothly. It fixes the circulation round the wing, and with it the lift.
- **Kutta–Joukowski theorem**: In ideal flow the lift per unit span equals ρ V Γ: density times speed times circulation.
- **Potential flow**: Flow with no curl and no divergence: v = ∇φ with ∇²φ = 0. A good model of air away from walls.
- **Pressure coefficient**: Cp = 1 − (v/V)². Negative where the air speeds up (suction), positive where it slows down.
- **Triple integral**: ∭ f dV adds f times tiny volumes. In cylindrical coordinates dV = r dr dθ dz, in spherical dV = ρ² sin φ dρ dθ dφ.
- **Centre of mass**: The density-weighted average position, ∭ r ρ dV / ∭ ρ dV.
- **Hypervolume**: The 4D version of volume. A 4D ball of radius a has hypervolume π² a⁴ / 2.
- **Cylindrical coordinates**: (r, θ, z): distance from the z axis, angle round it, and height. The volume element is r dr dθ dz.
- **Spherical coordinates**: (ρ, θ, φ): distance from the origin, angle round the z axis, and angle down from it. The volume element is ρ² sin φ dρ dθ dφ.
- **Polar basis**: The unit vectors e_r (outwards) and e_θ (round) change direction from point to point. Components in this basis, such as F_r and F_θ, follow the geometry of circles.
- **Hypersurface**: A 3D shape living in four dimensions, given by one equation f(x, y, z, w) = c. We see it through its 3D slices w = constant.
- **3-sphere**: All points of 4D space at distance a from a centre. Its slices are spheres; its 3-volume is 2π² a³.
- **Clifford torus**: A flat torus sitting inside the 3-sphere, made of the points where x² + y² = z² + w² = ½.
- **Divergence theorem in 4D**: The flux of F out of a closed hypersurface equals the integral of its divergence P_x + Q_y + R_z + S_w over the 4D region inside.
- **Rotation plane**: In 4D a rotation happens in a plane, not about an axis. The curl of a 4D field has six parts, one for each plane xy, xz, xw, yz, yw, zw.
- **Double rotation**: A 4D motion that turns two perpendicular planes at once, such as xy and zw. When both turn at the same rate it is isoclinic and every orbit is a circle.
- **Gauss law in 4D**: In n dimensions a point charge falls off as 1/r^(n−1). In 4D that is 1/r³, and the flux out of every 3-sphere round the charge is 2π².
