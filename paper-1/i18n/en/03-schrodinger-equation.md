# 3. Derivation of the Schrödinger Equation and N = d = 3

V = −H is a potential; by itself it does not yet say how many discrete states exist. This chapter first derives the eigenvalue equation — the Schrödinger equation — from the same exponential-family structure as the potential (§3.1). The spectral question — how many bound states the well holds — then becomes well-posed, and its answer is N = 3 (§3.2–3.3). At the end of §3.3 the three bound states are identified with the three generations of fermions — the one physical identification this chapter makes. Only under that identification does the second question arise: the particles the bound states represent exist in real space, so what determines the dimension of that space? Realisation consistency answers it, and d = 3 follows (§3.4). The derivation of d = 3 makes no use of the value N = 3 — the two derivations share the operator and nothing else. The coincidence N = d = 3 becomes the input of §4.
## 3.1. Derivation of the Schrödinger Equation

To write the eigenvalue equation, a kinetic term is needed in addition to the potential of §2.3, and it follows from the same structure as the potential. Dynamics enters by reading the canonical ensemble of §2 as sequential transfer: a family of transfer operators that, at each step, exponentiate the quadratic variation of the displacement (the kinetic term) together with V = −H (the action weight); its continuum limit yields the eigenvalue equation at the end of this section^II^. Two data remain: the coordinate carrying the motion, and one dimensionless normalisation. Both are fixed uniquely; the uniqueness is proved^II^.

First, the coordinate. The exponential family of a binary variable has two natural coordinates:

$$u = 2\arcsin\sqrt{\sigma}\quad(\text{Fisher metric flat}),\qquad \phi = \mathrm{logit}(\sigma)\quad(\text{canonical parameter in the exponent})$$

A3 decides between them. The coordinate u places the forbidden point σ = 0 at the finite endpoint u = 0, so dynamics on u would need boundary data exactly at the point of non-existence — non-existence would become a repository of model-defining data. The coordinate φ sends σ = 0 to φ → −∞: no boundary data attaches to non-existence, and under A3 none is admissible. Among the admissible coordinates, φ is the one on which the tilting action of A1 (the tilting weight e^{nφ}, §2.2) is linear — unique up to affine maps — and the binary indicator n ∈ {0,1} fixes its scale. Free motion on φ therefore has a constant-coefficient quadratic Lagrangian; position-dependent coefficients are excluded by displacement homogeneity^II^.

Second, the normalisation. Writing the kinetic coefficient as a²/2 and the action weight as b, the apparent two-parameter family reduces to a single dimensionless ratio:

$$\frac{a^2}{2}\Bigl(\frac{d}{d\phi}\Bigr)^{\!2},\quad b\,V \qquad\longrightarrow\qquad g = \frac{b}{a^2}$$

The reason is that the binary indicator n ∈ {0,1} of A1 fixes the unit of φ, the Legendre identity fixes the unit of V = −H, and rescaling the transfer step moves a² and b in the same proportion. Measuring the quadratic variation per step and the action weight as quantities of one and the same transfer process sets g = 1; the Landauer bit-normalisation (which takes as its unit the minimal work of erasing one bit) gives the same value independently. The uniqueness of both fixings is proved^II^.

The bound-state count established below (§3.3) does not depend on this last choice: it is the same across the whole family −½ d²/dφ² − g H(σ(φ)) for g ∈ [0.80, 1.50]. The number of negative eigenvalues is non-decreasing in g (since H(σ) ≥ 0, raising g lowers the quadratic form uniformly), and the count of three at both endpoints g = 4/5 and g = 3/2 is certified by an accompanying interval-arithmetic certificate — so N = 3 holds throughout the interval. An accompanying script further checks numerically that the count is stable across box sizes L = 60/100/160.

The ε-dependent corrections of §5–§8, by contrast, do rely on g = 1, since ε = N − √g·n_WKB(1) changes sign inside the same window (+0.51 at g = 0.80, −0.41 at g = 1.50); at the lower edge the action count 2.49 dips below the Maslov threshold 2.5 while the exact count is unchanged — the threshold rule of §3.2 is a heuristic only.

Combining V = −H as the potential with the kinetic term of the canonical normalisation (g = 1):

$$\left[-\frac{1}{2}\frac{d^2}{d\phi^2} - H(\sigma(\phi))\right]\Psi = E\,\Psi$$

This is nothing other than a Schrödinger equation: with only the three axioms of existence and the canonical normalisation g = 1 above as input, the eigenvalue equation of quantum mechanics emerges as the continuum limit of the transfer matrix of the canonical action.

The question posed at the head of this chapter — how many discrete states the well holds — is now well-posed, and §3.2–3.3 answer it. Whatever that count turns out to be, it is a consequence of this construction — the coordinate φ fixed uniquely above together with a flat kinetic term. Writing the flat kinetic term in a different coordinate yields a different operator and a different spectrum, so the uniqueness of φ is essential.

The derivation chain so far is summarised as:

$$A1\text{--}A3 \;\Rightarrow\; n^2 = n,\; 0<\sigma<1 \;\Rightarrow\; Z = 1+e^{\varphi} \;\xrightarrow{\text{Legendre}}\; V = -H \;\xrightarrow{\text{transfer matrix}}\; \left[-\tfrac{1}{2}\partial_\phi^2 + V\right]\Psi = E\Psi$$

## 3.2. Three Bound States

Why do fermions come in exactly three generations — why τ, μ, e, and why not a fourth? This and the following subsection prove rigorously that the potential V = −H has exactly three bound states and no fourth (hereafter N = 3), and identify them with the three generations of fermions. The identification is corroborated by the agreement of the mass ratios and mixing angles in §7.

The potential V = −H is a well. It is deepest at the centre (φ = 0) where V = −ln 2, returning to zero at both ends φ → ±∞. In quantum mechanics, such a well confines discrete energy levels — by the same principle that the hydrogen atom confines electrons to discrete orbitals. In general, how many levels a well holds is set by two free parameters, its depth and its width — a deep, wide well holds many levels, a shallow, narrow well holds few.

The well of V = −H, however, has no such free parameters. Its depth is fixed as the number ln 2 ≈ 0.693 directly by the functional form of the Shannon entropy itself (§2.3), and the coefficient of the kinetic term that plays the role of width is likewise fixed to the unique value g = 1 (the uniqueness theorem of §3.1). In an ordinary well problem, depth and width are free to choose; here neither is — both are completely fixed by the form of the equations alone.

How many levels, then, does this uniquely fixed well hold? That can only be found by actually solving it and counting.

![The potential V = −H(σ(φ)) and the probability densities |ψ_n|² of its three bound states (left)](img/fig_potential.png)

*Figure 1. The potential V = −H(σ(φ)) and the probability densities |ψ_n|² of its three bound states (left). More localised states correspond to heavier particles (right). No fourth negative eigenvalue: the prediction that no fourth sequential chiral generation exists.*

We denote the number of levels confined in this well by N. A semiclassical (WKB) approximation estimates how many half-wavelengths fit inside the well. Each integer half-wavelength corresponds to one bound state:

$$n_\mathrm{WKB} = \frac{1}{\pi}\int_{-\infty}^{\infty}\sqrt{2H(\sigma(\phi))}\,d\phi = 2.781$$

In the standard convention including the Maslov correction, the threshold for the k-th state is n_WKB > k − 1/2. The value n_WKB = 2.781 exceeds the third-state threshold 2.5 by 0.281, while falling short of the fourth-state threshold 3.5 by 0.719. The WKB estimate therefore suggests N = 3. We define ε ≡ N − n_WKB = 3 − 2.781 = 0.219: the gap between the exact count and the semiclassical action count.[^epsenc] That ε > 0 says the third state is barely bound.[^epsconv] This ε is the source of every correction exponent in this paper: it controls the NLO corrections to the couplings and mixing angles of §5 and §8.
[^epsenc]: The rigorous interval enclosure 0.219188 is certified by the accompanying certificate script (rigorous Arb-ball integration with an analytic tail bound); the certified interval lies inside the certified interval of Paper II.

[^epsconv]: Measured against the Maslov-corrected threshold, the same marginality reads 2.781 − 2.5 = 0.281. We use ε because it compares two unambiguously defined quantities — the exact count and the action integral — whereas the threshold rule is an asymptotic heuristic; the g = 0.80 example of §3.1 shows it can fail at finite depth.

Nothing in this count is adjustable. The three ingredients of the construction are each unique: the coordinate and the normalisation are the unique ones of §3.1, and Shannon entropy is the unique entropy satisfying the Khinchin axioms, which include strong additivity (Khinchin's theorem [16, 17]). Under this construction, N = 3 is rigorously proved by interval arithmetic (§3.3).

## 3.3. Rigorous Proof

**Theorem (N = 3).** The Schrödinger equation of §3.1 has exactly three bound states, and their eigenvalues are rigorously enclosed by interval arithmetic:

$$\begin{aligned}
E_0 &= -0.4850022531029642374452777658 \pm 10^{-24},\\
E_1 &= -0.1590522216188561779934190 \pm 10^{-24},\\
E_2 &= -0.010423393062109459327616 \pm 10^{-22}
\end{aligned}$$

No fourth negative eigenvalue exists; the essential spectrum begins at 0 (the small positive values seen on finite grids are discretisation artifacts of the box).

*Proof (computer-assisted, interval arithmetic).* The proof has three independent layers.

*Counting.* By parity the problem splits into a Neumann problem (even) and a Dirichlet problem (odd) on the half-line [0,∞). Propagating the Prüfer angle by interval enclosures (using the monotonicity of the potential), combined with analytic tail estimates, gives rigorous two-sided bounds on the angle at the trial energies. By Sturm oscillation theory the rotation of the angle counts the negative eigenvalues exactly: two in the even sector, one in the odd — N = 3.

*Enclosures.* The eigenvalue intervals above are certified by two-sided shooting with a verified high-order Taylor integrator over interval coefficients.

*Independent checks.* A separate implementation in Arb ball arithmetic re-certifies N = 3, and variational upper bounds from Rayleigh quotients of three sech-type (Pöschl–Teller-type [18]) trial functions confirm the existence of three negative eigenvalues. Three certificate scripts are included in the ancillary files. □

**Identification with generations.** Here we hypothesise that these three bound states ψ₀, ψ₁, ψ₂ are the mathematical structure of the three generations of fermions. The ordering then fixes which state is which generation: binding energy orders localisation (|E₀| > |E₁| > |E₂|, from most to least localised), and the generations carry the mass hierarchy — the most localised ψ₀ is the heaviest generation. For charged leptons, ψ₀, ψ₁, ψ₂ ↔ τ, μ, e.

At this stage the identification is provisional. In §7–§8 the mass ratios and mixing angles are derived from it and agree with experiment; that agreement is what makes it credible. If the identification is correct, the absence of a fourth negative eigenvalue is the prediction that no fourth sequential chiral generation exists.

## 3.4. Three Spatial Dimensions

The preceding subsections proved N = 3. That proof lives in the internal space (the φ coordinate), and φ is not a spatial coordinate — as §9.2 shows, the internal and spacetime factors are independent. Under the provisional identification of §3.3, however, the fermions represented by the three bound states are particles that exist in real space. What, then, determines the dimension of that space? The answer is the consistency of realisation: the internal well must be realised, unbroken, on a particle in space. This subsection shows that the two conditions of this consistency — preservation of the well (the operator must not be deformed under the radial transfer, the A3-based criterion: d = 1, 3 only) and propagating gravity (d ≥ 3) — have d = 3 as their unique common solution.

Consider the same well shape V = −H realised as a radial profile in d-dimensional space. Here σ(r) is the same well shape as σ(φ) on φ ∈ ℝ, transferred to the radial variable r ≥ 0; the difference in domain is addressed below in the comparison with full-line quantisation. Reducing the d-dimensional Schrödinger equation to a one-dimensional radial equation by standard partial-wave decomposition, an additional effective force (d−1)(d−3)/(8r²) appears in the zero-angular-momentum (spherically symmetric) radial channel:

$$V_\mathrm{eff}(r) = -H(\sigma(r)) + \frac{(d-1)(d-3)}{8r^2}.$$

The numerator (d−1)(d−3) vanishes for d = 1 and d = 3, leaving V = −H unchanged. In other dimensions, this geometric term deforms the operator:

| d | (d-1)(d-3)/8 | Effect on the operator |
|---|---|---|
| 1 | 0 | No deformation |
| 2 | -1/8 | An attractive term is added (tending to create extra states) |
| 3 | **0** | **No deformation: the well shape is preserved** |
| 4 | +3/8 | A repulsive term is added (tending to remove the marginal third state) |
| ≥5 | ≥1 | Strong repulsion |

Full-line quantisation (φ ∈ ℝ) is essentially self-adjoint at the endpoints and requires no boundary condition. Under A3 (non-existence is not a state — no additional data is admissible at the boundary; the same conclusion as the exclusion of u-type coordinates in §3.1)^II^, this canonical full-line quantisation is the reference, and a spatial realisation is required not to add an extra inverse-square term to the canonical operator. This requirement is met only when the coefficient (d−1)(d−3)/8 vanishes, i.e. only for d = 1, 3. Note that a vanishing inverse-square term does not make the full-line and radial problems identical — a half-line radial model adds endpoint structure at the origin (a choice of self-adjoint extension) and is a different model, outside the comparison fixed by this correspondence^II^.

A realisation-consistency condition excludes d = 1. The realisation of a spin-2 field (gravity) — taken as a premise, as in §9.1, with its derivation left to a subsequent paper — propagating dynamically requires d ≥ 3 (for d ≤ 2 the Weyl tensor vanishes identically, leaving no local degrees of freedom). The fermionic structure (CAR) derived from A1–A3^II^ has, in its spatial realisation, finite-dimensional spinor representations for d ≥ 3 (π₁(SO(d)) = Z₂, the double cover Spin(d)) and is consistent with this choice; but since fermionic statistics can be realised in lower dimensions as well, this is not a condition that excludes d = 1 on its own, and it is not used for the selection.

We summarise this as a theorem.

**Theorem (d = 3).** Under the above choice of full-line quantisation, d = 3 is the unique spatial dimension simultaneously satisfying: *(i)* the well operator is preserved with no extra geometric term: d = 1, 3; *(ii)* gravity propagates (Weyl tensor non-trivial): d ≥ 3. Intersection: {3}.

*Proof.* (i) The centrifugal term (d−1)(d−3)/(8r²) = 0 if and only if d = 1 or 3; (ii) the Weyl tensor vanishes identically in spacetime dimension ≤ 3, i.e. spatial d ≤ 2; propagating gravity requires d ≥ 3. □

The three spatial dimensions are also obtained independently from the fact that the traceless part of the self-adjoint sector of the complex carrier M₂(ℂ) is three-dimensional^II^; the well-preservation argument of this section is also a consistency check of that result.
