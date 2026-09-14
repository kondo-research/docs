# 9. Connection to Spacetime

All calculations in §2–8 were performed in internal space (the φ coordinate). Neither space nor time appeared. How, then, does this zero-dimensional theory connect to four-dimensional spacetime? This chapter answers in three steps: the dimension and signature (3,1) of spacetime (§9.1), the independence of internal space and spacetime (§9.2), and why the zero-dimensional algebraic values correspond to the four-dimensional experimental values (§9.3).

## 9.1. Spacetime Dimension and Gravity

§3.4 derived the spatial dimension d_space = 3. But "why four-dimensional spacetime?" is a separate question — it is not obvious that time is one-dimensional. We show that two independent paths give the same D = 4 — both are consistency checks with stated premises (hereafter we distinguish the spatial dimension d from the spacetime dimension D = d + 1).

The first path comes from gravitational degrees of freedom. A massless spin-2 particle (graviton) in D-dimensional spacetime has D(D−3)/2 physical degrees of freedom (following from Poincaré group representation theory, without assuming any particular D or Einstein's equations). Meanwhile, the N = 3 bound states of V = −H provide N−1 = 2 independent internal degrees of freedom (since three probabilities sum to one). As a consistency check that takes Poincaré symmetry, a spin-2 field, and gauge reduction as premises, matching the spacetime dynamical degrees of freedom (graviton polarisations) one-to-one with the internal degrees of freedom gives:

$$D(D−3)/2 = N − 1 = 2 \quad \Longrightarrow \quad D = 4$$

The second path comes from projective geometry. The projective plane PG(2, ℂ) = ℂP² is a real 4-dimensional manifold, and for N = 3:

$$D = \dim_\mathbb{R}(\mathbb{C}P^{N-1}) = 2(N-1) = 4$$

Both are consistent only for N = 3.

These two paths are independent — one from field-theoretic representation theory (spin-2 polarisations), the other from pure algebraic geometry (complex carrier ℂP²). That both give D = 4 is a non-trivial consistency check of N = 3.

Even with D = 4 fixed, the signature could be (4,0), (3,1), or (2,2). The finite field F₃ (from the primality of N = 3) and the complex carrier ℂ³ (from the unitary realisation) are independent constructions moored to the same N = 3 — since the characteristics differ, no field homomorphism F₃ → ℂ exists, and no lift via F₉ succeeds either. What links the two is the correspondence between the exponent labels of the Heisenberg–Weyl system (F₃ side) and the representation carrier (ℂ³ side); what is preserved is the Weyl commutation relations and the MUB structure. ℂ³ carries a complex structure from the outset. Furthermore, the transfer action S = ∫[½φ̇² + V]dτ of the internal coordinate φ opened by A2 (§2.2) has a single evolution parameter τ, so one of the four real directions is distinguished as the evolution direction.

The complex structure and the single evolution direction alone do not uniquely fix the signature. (3,1) is fixed as the connection to the determinant form on M₂(ℂ)_sa and the structure SL₂(ℂ) → SO⁺(1,3).

Indeed, an element of M₂(ℂ)_sa is parametrised as

$$X = \begin{pmatrix} x^0 + x^3 & x^1 - i x^2 \\ x^1 + i x^2 & x^0 - x^3 \end{pmatrix},\qquad \det X = (x^0)^2 - |\boldsymbol{x}|^2$$

and the determinant is precisely a quadratic form of signature (+,−,−,−). The SL₂(ℂ) action X ↦ AXA† preserves this determinant, giving SO⁺(1,3).

For a four-dimensional metric theory satisfying the locality, naturality, diffeomorphism-covariance, divergence-free and second-order assumptions of Lovelock's theorem [30], the field equation is restricted to the Einstein form with a cosmological term

$$G_{\mu\nu} + \Lambda g_{\mu\nu} = \kappa T_{\mu\nu}.$$

Jacobson [31] showed that, assuming local Rindler horizons, the Unruh temperature, an entropy density proportional to area, and local equilibrium, the same equation follows from δQ = T_H dS on a causal horizon. The gravitational action and its coefficient are derived from the four-dimensional local manifestation in a subsequent paper. Jacobson’s relation is an independent consistency check of that result: when the assumptions above are realised on the same local manifestation, δQ = T_H dS reproduces the same Einstein equation. What stands here is therefore not a second derivation from the identity S = H(σ) alone, but agreement between the derived gravitational structure and its thermodynamic description.

## 9.2. Why Internal Space and Spacetime Are Independent

The coordinate φ = logit(σ) lives in internal space; the coordinate x lives in spacetime. Why are they independent?

The answer lies in the construction of V = −H. The potential V = −H(σ(φ)) is built as the internal zero-mode of the Bernoulli degree of freedom and contains no explicit spacetime coordinate x. However, the coordinate-independence ∂V/∂x = 0 alone does not exclude a mixed kinetic term. What makes the decomposition hold is the construction in which φ (internal) and x (spacetime) are independent degrees of freedom, with generators acting on separate factors and no cross term. Under this, the full Hamiltonian takes the form Ĥ = Ĥ_φ + Ĥ_x, and the Hilbert space decomposes as a tensor product ℋ_int(φ) ⊗ ℋ_space(x).

$$\hat{H} = \hat{H}_\phi \otimes \mathbf{1} + \mathbf{1} \otimes \hat{H}_x,\qquad \mathcal{H} = \mathcal{H}_\mathrm{int}(\phi) \otimes \mathcal{H}_\mathrm{space}(x)$$

Since this composite space is separable with dim ≥ 3 (ℋ_int(φ) is 3-dimensional from the generation factor alone, ℋ_space(x) is infinite-dimensional), Gleason's theorem [32] restricts every non-contextual probability assignment on all projections that is countably additive over orthogonal families to the trace form p(P) = Tr(ρP) — under those assumptions the form of the Born rule is a theorem rather than an axiom. What is unique is the form of the assignment; the single detection probability σ = ⟨n⟩ of §2 does not by itself determine the state ρ.

Two observational facts confirm this. First, all gauge couplings are independent of generation — direct evidence that φ and x are not coupled. Second, the 0D theory computes only dimensionless quantities (mass ratios, mixing angles), while dimensionful quantities (absolute masses) require spacetime — precisely the prediction of the tensor-product structure.

The analogy with spin illuminates this structure. Spin algebra is finite-dimensional and independent of the Lagrangian, yet determines 4D physical quantities (magnetic moment, fine structure). Generations have the same structure — the finite-dimensional structure V = −H corresponds to 4D mass ratios and mixing angles.

Once both factors are in place, the form of the 4D field theory is determined as well. The spacetime factor carries the local Lorentz carrier of §9.1 (spinor fields); the internal factor carries the finite data of §4 — the gauge algebra with its representations, the single Higgs doublet, and the four Yukawa edges. The first-order local operator coupling the two is narrowed to a single form compatible with the tensor-product structure and the internal data:

$$D_{A,\Phi} = i\gamma^\mu(\nabla_\mu + A_\mu) + \gamma_5 \otimes \Phi$$

where A_μ is the gauge connection and Φ contains only the single Higgs and the four Yukawa edges (the classification of §4).

The interactions then decompose uniquely as the curvature components of this single operator — the field strength F_A (gauge self-interaction), the covariant derivative D_AΦ (the gauge–Higgs coupling), and the zero-form component Φ² (whose relativisation to the vacuum point, Φ² − Φ₀², gives the Higgs potential) — whose magnitude gives the bosonic action, while ⟨Ψ, D_{A,Φ}Ψ⟩ gives the fermionic action. Each term of the Standard-Model Lagrangian is thus not a separately postulated assumption but a curvature component of a single first-order coupling.

The rigorous uniqueness of this form (the exclusion of other coupling types) and the values of the dimensionless coefficients are given, under the stated realisation conditions, by the manifestation theorem of Paper II. The electromagnetic-clock correspondence is unique, as a continuous map preserving semigroup composition, up to a single scale-setting quantity^II^. The β functions of individual renormalisation schemes and the numerical conversion between schemes are the continuing computation that displays the same physical quantity in the coordinates of each scheme, and the absolute scale (m_e) is what carries the derived quantities into physical units — the conventional layer (both in Paper II).

## 9.3. Correspondence between 0D Values and 4D Experiment

The tensor-product structure explains why 0D algebraic values coincide with tree-level values of the 4D renormalised theory. The 0D values are algebraic constants. In 4D, tree level is the limit of zero radiative corrections — i.e. the limit in which spacetime dynamics does not affect internal structure — which is precisely the independence guaranteed by the tensor product ℋ_int(φ) ⊗ ℋ_space(x). Radiative corrections arise from loop momenta in the spacetime factor ℋ_space and enter as sub-percent corrections to the internal algebraic values (§5.1: sin²θ_W = 3/13 + Δ_rad = 0.23122). The 0D values are neither RG fixed points nor UV boundary conditions, but the unique algebraically determined point serving as the reference for comparison with 4D theory — running quantities acquire the 4D RG evolution and radiative corrections, while quantities such as discrete state counts do not run.

Concretely, each observable carries a stated definition point for the comparison (α at the Thomson point; sin²θ_W and α_s at M_Z; §5), and the 0D value is compared with the renormalised 4D value at that point. Changing the scale is described on the 4D side as RG evolution; on the internal side it corresponds to reading the same finite resolvent that gave Z in §5.3 at a different evaluation point, and the closed form of this response kernel is derived^II^. The closed form of the β function in any renormalisation scheme is obtained by running between definition points.

For the Thomson-normalised physical electromagnetic effective charge, by contrast, the identification of the electromagnetic response together with the unique clock correspondence yields, as a theorem, uniform boundedness on the whole Euclidean-momentum half-line and the absence of a Landau pole^II^ — α can be followed along it from its Thomson-point value to a finite ultraviolet value. Poles appearing in perturbative displays are coordinate singularities created by a singular reparametrisation of the coupling, not poles of the physical current response.

With this, the relationship between internal structure (φ) and spacetime (x) is established. V = −H gives internal values corresponding to mass ratios, mixing angles, and coupling constants. The spacetime factor supplies, in addition to the overall energy scale, the 4D RG evolution and radiative corrections for running quantities.
