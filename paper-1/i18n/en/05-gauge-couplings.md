# 5. Gauge Coupling Constants

§4.2 derived the structure corresponding to the gauge group (which forces exist). This chapter derives their strengths (coupling constants).

## 5.1. Weinberg Angle

The partition 9+3+1 of §4.2 gives values corresponding to the coupling constants. The weight of each point is fixed by the symmetry prior to choosing a flag: PGL(3, F₃) acts transitively on PG(2,3), so the 13 directions carry equal weight (invariant measure). Fixing the flag does not alter these weights; it only classifies the 13 points into 9+3+1. On this basis, the Weinberg angle [21] (weak mixing angle) sin²θ_W is read and identified as the fraction that the 3 weak directions occupy among all 13 — taking all internal directions as the denominator^II^:

$$\sin²θ_W = 3/13 = 0.23077 \quad (\text{expt: } 0.23122\;\overline{\mathrm{MS}}\text{ at }M_Z,\; 0.2\%)$$

Alternatives such as taking only the four electroweak directions in the denominator correspond to a different observable type; that the type-preserving correspondence is unique to this fraction is proved^II^.

This angle also fixes the tree-level W/Z mass ratio (§5.4).

**Radiative corrections.** The predictions above are algebraic values, and their comparison with M_Z-scale experiments requires the 4D RG evolution and radiative corrections of the running quantities (§9.3). The next correction to the weak angle — the radiative correction, with expansion parameter α, that carries the tree value 3/13 to the MS-bar value at M_Z — is fixed in closed form by the framework itself:

$$\Delta_\mathrm{rad} = \alpha\cdot\frac{5N^3}{|\mathrm{PG}|^3} = \alpha\cdot\frac{135}{2197} = 0.00045$$

(N and |PG| are quantities of this paper; the uniqueness of this product form, including the coefficient 5, is proved as a theorem^II^.) This gives sin²θ_W = 3/13 + Δ_rad = 0.23077 + 0.00045 = 0.23122, in agreement with the MS-bar experimental value 0.23122 ± 0.00003 [22] within errors.

## 5.2. Strong Coupling Constant

The strong coupling constant follows by distributing the weak-sector fraction over the rank of the colour sector. Of the 9 colour-sector directions, the independent directions number rank(SU(3)) = 2 (Cartan generators); equidistributing sin²θ_W over these 2 directions: α_s^(0) = sin²θ_W / (N−1) = 3/26 = 0.1154 (the uniqueness of this distribution rule is proven^II^). The spectral marginality ε = 0.219 from §3 provides the NLO correction. The correction is distributed over N²+1 = 10 non-weak PG directions (colour 9 + hypercharge 1):

$$α_s = (3/26)(1 + ε/(N²+1)) = 0.1179 \quad (\text{expt: } 0.1180\;\overline{\mathrm{MS}}\text{ at }M_Z,\; 0.07\%)$$

The value k = N²+1 = 10 follows from the number of non-weak directions in PG(2, F₃). Throughout this paper the NLO corrections take the form 1 ± ℓε/k, where the denominator k is the size of the finite support over which the correction is distributed — k = N²+1 = 10 for the non-weak sector (α_s; affine + hypercharge), k = N² = 9 for generation mixing (sinθ_C; affine plane), k = |PG| = 13 for the full set of PG modes (m_H/v, sin²θ₂₃; full projective space), and k = N = 3 for the three weak directions (sin²θ₁₃). The assignments of (ℓ, k) to each observable, including the sign and coefficient ℓ, are each proven unique^II^.

## 5.3. Fine-Structure Constant

The Weinberg angle and strong coupling constant were determined by simple point ratios on PG(2,3). The fine-structure constant requires more — the full spectral structure of the internal space.

The inverse electromagnetic coupling 1/α measures the weakness of the electromagnetic interaction. The observed charge is the charge screened by the matter fields — the stronger the screening, the weaker the coupling and the larger 1/α. In this framework 1/α is given (up to the self-consistent correction −α) by the sum of the bare photon propagation cost λ₁ and the matter screening quantity Z, and the Thomson-point value is dominated by the screening term.

In 4D QED this structure is formalised as the Dyson equation. In 0D the same structure holds but becomes algebraically exact. The propagator is a constant, so the vertex correction and self-energy are determined by the same resolvent, and the 4D perturbative cancellation Z₁ = Z₂ holds as an exact algebraic identity^II^. The self-consistency equation is:

$$\frac{1}{\alpha} + \alpha = \lambda_1 + Z$$

The right-hand side has two terms: λ₁ is the bare photon inverse propagator (propagation cost) and Z corresponds to the scalar-channel spectral quantity (screening). This correspondence is a spectral one — Z is the resolvent trace whose energy-denominator structure matches the matter vacuum polarisation.

The form of the equation (the left-hand side 1/α + α with unit coefficient) is derived^II^ — what remains external is the comparison convention identifying the incidence current with the Thomson-point electromagnetic current. The full justification of this correspondence as a self-consistent prediction, and the proof that the physical root is unique under this identification, are both given in Paper II. The dominant contribution to Z is 1/|E₂| = 95.94; since E₂ is rigorously certified by the interval arithmetic of §3.3, the certified enclosure of E₂ does not change the displayed digits of this spectral contribution.

The minimum cost λ₁ for gauge-field propagation through internal space is the smallest non-zero eigenvalue of the Laplacian on internal space. Since gauge interactions involve both positions (points) and directions (lines), the natural object for diffusion is a flag (point-line incidence pair). The spectrum of the graph Laplacian ℒ on the flag graph of PG(2, F₃), a 52×52 matrix, is:

| Eigenvalue | Value at N = 3 | Multiplicity |
|---|---|---|
| 0 | 0 | 1 |
| (N+1) − √N | 2.268 | 12 |
| (N+1) + √N | 5.732 | 12 |
| 2(N+1) | 8 | 27 |

This spectrum follows elementarily from the incidence counts of the projective plane alone. Each point lies on 4 lines and each line carries 4 points, so flag adjacency (sharing the point or sharing the line) forms a 6-regular graph, and the Laplacian can be written

$$\mathcal{L} = 8\,\mathbf{1} - P - \Lambda$$

where P (Λ) is the operator summing over the 4 flags with the same point (the same line). On constant functions P = Λ = 4, so ℒ = 0 (multiplicity 1). On the space of functions whose sum vanishes within every point group and within every line group — of dimension 52 − 13 − 13 + 1 = 27 — one has P = Λ = 0, so ℒ = 8 (multiplicity 27).

The remaining 24 dimensions are spanned by pairs of a zero-sum point function u and a zero-sum line function v, on which ℒ acts as

$$(u, v) \mapsto (4u - Mv,\ 4v - M^{\mathsf T}u)$$

with M the 13×13 point-line incidence matrix. Since exactly one line passes through two distinct points, M Mᵀ = 3I + J (J the all-ones matrix), which on zero-sum functions reduces to M Mᵀ = 3I. Hence

$$(4-\lambda)^2 = 3,\qquad \lambda = 4 \mp \sqrt{3}\quad(\text{multiplicity 12 each})$$ The √3 comes from the uniqueness of the line joining two points; the 4 = N + 1 from the number of lines through a point.

The smallest non-zero eigenvalue λ₁ = 4 − √3 = 2.268 is the quantity that corresponds to the bare photon inverse propagator in the self-consistent equation 1/α + α = λ₁ + Z above.

The screening term Z corresponds to the scalar-channel spectral quantity from three generations of matter fields, determined by the resolvent of the internal kinetic operator. The internal kinetic operator is a tensor sum of the generation sector (K_gen, whose eigenvalues are the binding energies |E_n|) and the gauge sector (ℒ, eigenvalues λ_k):

$$K_\mathrm{int} = K_\mathrm{gen} \otimes \mathbf{1} + \mathbf{1} \otimes \mathcal{L}$$

This form — the tensor sum, with both factors measured in the same unit at relative scale 1 — is established as a uniqueness theorem^II^ under the single-clock unit clause (product couplings, twisted products, and rescalings of the relative unit are excluded). Decomposing the trace of the resolvent by multiplicity:

$$Z = \mathrm{Tr}[1/K_\mathrm{int}] = \zeta_V(1) + 12\,S_1 + 12\,S_2 + 27\,S_3 = 134.77613$$

where ζ_V(1) = Σ_n |E_n|⁻¹ and S_i = Σ_n (|E_n| + λ_i)⁻¹. The intermediate values are

$$\zeta_V(1) = 104.28714,\qquad 12S_1 = 14.57025,\qquad 12S_2 = 6.05684,\qquad 27S_3 = 9.86190$$

with ζ_V(1) dominated by the E₂⁻¹ contribution 95.94. The 27-dimensional sector (multiplicity 27 = 3³) contributes 9.86 ≈ N², providing the spectral structure corresponding to the QCD vacuum-polarisation correction (all intermediate values are reproducible with the accompanying verification code).

Substituting λ₁ = 4 − √3 = 2.26795 and Z = 134.77613 into the self-consistency equation:

$$\frac{1}{\alpha} = \frac{(Z + \lambda_1) + \sqrt{(Z + \lambda_1)^2 - 4}}{2} = 137.0368 \quad (\text{expt: } 137.036,\; 0.0006\%)$$

Adding the correction terms^II^:

$$\frac{1}{\alpha} + \alpha = \Lambda_0 - x\Bigl(1+\frac{\alpha}{2}\Bigr) + \frac{3}{4}\varepsilon^2 x + \frac{1589}{5408}\,x^2 - \frac{2}{13}\,\frac{x^3}{1+x},\qquad x = \frac{9\alpha}{26\pi}$$

where Λ₀ = λ₁ + Z is the right-hand side of the leading term and x is the same expansion parameter as the colour screening of §8.1. The origin of each term — the self-consistent screening correction, the generation branching for ε²x, the second-order screening count for x², and the first return of the 52-flag orbit for x³ — and the proof that the series closes in this form are given in Paper II. The physical root of this equation is

$$\frac{1}{\alpha}\Big|_{\text{all orders}} = 137.035999084$$

Here "all orders" refers to all orders of the typed finite Dyson closure defined in Paper II. The value is certified to 13 digits by the interval [137.0359990843979, 137.0359990844119]^II^. We note that the experimental recommendations split by measurement system: CODATA 2018, whose principal input is the Cs photon-recoil measurement, gives 137.035999084(21) — agreement to all displayed digits — while CODATA 2022, based on the Rb recoil, gives 137.035999177(21), 4.4σ away. The Cs and Rb measurements themselves disagree by more than 5σ; on this open experimental dispute the framework gives the prediction that the fine-structure constant lies on the Cs side (Table 4).

## 5.4. The W/Z Mass Ratio

From the weak angle the W/Z mass ratio follows: m_W/m_Z = cosθ_W = √(10/13) = 0.8771 — 0.5% below experiment; this residual has approximately the size and sign of the standard SM top-quark Δρ correction. That the custodial response is carried by exactly one neutral component of the one Higgs doublet is a theorem; what remains as identification is the naming of the experimental definition points (the on-shell convention) and the readout word. Under that identification, m_W/m_Z = 0.88137 follows uniquely and agrees with experiment at +1.0σ^II^.
