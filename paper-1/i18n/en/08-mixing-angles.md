# 8. Mixing Angles — CKM and PMNS

§7 derived the fermion mass ratios. This chapter derives the inter-generation mixing — the quark CKM matrix and the neutrino PMNS matrix — and, with it, the Dirac nature of the neutrinos.

## 8.1. CKM Mixing

§7.1–7.2 established the mass ratios. With masses determined, we now derive the inter-generation mixing [24]. Why is V_ub small, and why does the Cabibbo angle [19] take its particular value? The Standard Model does not explain these. In V = −H, the potential symmetry corresponds to the former and the marginality of the third generation to the latter.

The potential V = −H is symmetric: V(φ) = V(−φ). This fixes the parity of each eigenfunction: ψ_0 even, ψ_1 odd, ψ_2 even. The direct overlap between distinct modes vanishes by Sturm-Liouville orthogonality: ⟨ψ_0|ψ_2⟩ = 0. Since ψ_0 and ψ_2 are both even, ⟨ψ_0|M|ψ_2⟩ = 0 for a V-parity-odd mixing operator M — the leading 0↔2 transition is forbidden:

$$V_{ub}\big|_\mathrm{tree} = 0$$

The measured value |V_{ub}| ≈ 0.004 arises at higher orders of the Wolfenstein hierarchy [25]; the first non-zero term is given by the closed form below.

The Cabibbo angle follows from spectral marginality. The third bound state ψ₂ is marginally bound — its binding energy |E₂| = 0.010 is only 1.5% of the well depth. The parameter measuring this marginality is the gap between the exact bound-state count and the semiclassical action count:

$$\varepsilon = N - n_\mathrm{WKB} = 3 - 2.781 = 0.219$$

Mixing angles reflect the mismatch between mass and weak eigenstates; the marginality of the third bound state (ε > 0) is the source of mixing, and in the formal limit ε → 0 each transition formula tends to zero, leaving the three generations intact (that this formal limit does not define a family of unitary CKM matrices is noted in §8.2). The expression giving the angle as a series in ε (which operator carries the transition, and what fixes its order and denominator) is proven unique per observable^II^ (see the list in §5.2). To second order:

$$\sin\theta_C = \varepsilon(1 + \varepsilon/N^2) = 0.2245 \quad (\text{expt: } 0.2243,\; 0.10\%)$$

This value is the unscreened internal value. The value composed with colour screening is sinθ_C·(1−x) = 0.22435 (x = N²α/(2π|PG|) = 9α/(26π) is the colour-screening expansion parameter; derived in Paper II).

The Wolfenstein hierarchy follows from the Cabibbo angle: |V_{us}| ∼ ε, |V_{cb}| ∼ ε², and |V_{ub}| is suppressed to at least O(ε³) with first non-zero term 2ε⁴ (experiment: 0.225, 0.041, 0.004). NLO corrections take the form 1 ± ℓε/k. The assignment of the denominator k and of the sign and coefficient ℓ is as listed in §5.2 (1+ε/9 for sinθ_C, 1−2ε/3 for sin²θ₁₃). The full closed forms, proved as a theorem^II^, are

$$|V_{cb}| = \varepsilon^2\left(1-\frac{2\varepsilon}{3}\right) = 0.0410,\qquad |V_{ub}| = 2\varepsilon^4\left(1-\frac{2\varepsilon}{3}\right)\left(1-\frac{3\varepsilon}{26}\right) = 0.00384$$

The origin of these exponents and of the coefficient 2 is discrete. Generation transitions are carried only by parity-odd permutations of the three generations (a consequence of V-parity). The adjacent transitions 1↔2 and 2↔3 are realised by the transpositions t₁₂ and t₂₃. With respect to the flag V₁ ⊂ V₂ fixed by the generation order (the line spanned by the first generation and the plane spanned by the first two), count the cost of a wall as the shallowest flag level it moves: t₁₂ moves V₁, cost 1; t₂₃ fixes V₁ and moves only V₂, cost 2 — these are the exponents of |V_us| ∼ ε and |V_cb| ∼ ε².

Parity makes the direct one-step 1↔3 element vanish, but it does not by itself forbid the two-step composite 1→2→3: two odd insertions compose to an even one, and the product of the two matrix elements is nonzero. What separates them is the generative type—the composite carries a different composition tree, so it is a different observable rather than a neglected term of the same one^II^.

The odd permutation carrying 1↔3 directly is the longest permutation w₀, which reverses the three generations. Its gallery crosses all three walls t₁₂, t₂₃, t₁₃, with total cost 1 + 2 + 1 = 4 — the reason the first non-zero term is of order ε⁴. The coefficient 2 arises because w₀ has exactly two shortest decompositions (galleries), exchanged by point-line duality. The assignment of ε per wall and this count are proved as theorems under the specified mapping rule^II^.

The parity symmetry V(φ) = V(−φ) suppresses the direct 0↔2 flavour transition, but it does not by itself fix the QCD vacuum angle: parity alone leaves θ ∈ {0, π}.

The observable strong-CP angle is

$$\bar\theta = \theta_\mathrm{QCD} + \arg\det M_q$$

That both terms vanish is shown by the strong-CP matching theorem of Paper II: applying A1–A3 so as to preserve the action, the fermion determinant and the realisation of large gauge transformations gives arg det(M_u M_d) = 0 and a vanishing bare θ_QCD, hence θ̄(μ₀) = 0 at the matching point. What removes the bare θ_QCD is that the only unitary scalar preserving the positive measure ray is 1 (the measure-line triviality^II^) — not V-parity on its own.

However, this is a statement at the matching point and not an exact zero at all scales. For the infrared θ̄_IR, which includes weak CKM loops and thresholds, Paper II gives the conditional bound |θ̄_IR| < 6.0×10⁻¹⁷ at the declared orders — weak O(G_F²), chiral O(p²), in the large-N_c chiral-perturbation framework; the all-orders evaluation is a continuing computation. Consequently, beyond a PQ-type axion — excluded by the absence of a PQ-type global U(1) — no claim is made about the non-existence of axion-like particles in general.

Yet CP violation is observed in the CKM sector (J = 3.16 × 10⁻⁵ [22]). This is consistent with the bare θ_QCD = 0: the CKM phase arises at higher order in ε:

$$J = \frac{\pi\varepsilon^5}{N_\mathrm{flags}} = \frac{\pi\varepsilon^5}{52} = 3.06\times10^{-5}$$

(N_flags = 52 is the total number of flags, §4.1; a theorem under the specified mapping rule^II^.) The matching-point condition remains exactly zero.

The strong-CP attributions are summarised:

| Quantity | Prediction | Experiment |
|---|---|---|
| Bare θ_QCD | **Not a consequence of V-parity** (matching-point value θ̄(μ₀)=0 from the strong-CP matching theorem^II^) | — (the bound \|θ̄_IR\| ≲ 10⁻¹⁰ applies to the infrared quantity; not directly comparable) |
| CKM CP violation | J = πε⁵/N_flags (theorem under the mapping rule^II^) | 3.06 × 10⁻⁵ (expt 3.16 × 10⁻⁵) |

## 8.2. PMNS Mixing

In §8.1, CKM mixing angles were obtained from ε = 0.219 — small values (sinθ_C ≈ 0.22). Yet PMNS mixing angles are large (sin²θ₁₂ ≈ 1/3). Why does the same V = −H produce both small and large mixing?

The answer lies in colour charge. Quarks carry colour and reside in the deep well V = −3H, which places their mixing in the perturbative regime of small mode overlap — a localisation picture consistent with the smallness of quark mixing, whose expansion parameter is the generation-sector marginality ε (§3.2); the formulae themselves rest on the generating flag orders and screening words of Paper II.

Neutrinos are colour-neutral; instead, the geometric allocation of gauge directions on PG(2,3) directly gives values corresponding to the mixing angles. The solar angle is the fraction of one complete electroweak line (N+1 = 4 points) in the 13 directions of PG:

$$\sin²θ_{12} = 4/13 = 0.3077 \quad (\text{expt: } 0.3088,\; 0.4\%)$$

At LO the atmospheric angle is the fraction that the disjoint union of the N pure-weak directions and another line through the reference point (N+1 points) occupies among the 13 directions of PG, namely 7/13. With the PG-scale NLO correction (k = |PG| = 13):

$$\sin²θ_{23} = (7/13)(1 + ε/13) = 0.5475 \quad (\text{second octant})$$

The LO fraction 7/13 exceeds 1/2, predicting the second octant. In NuFIT 6.1 [28] the global best fit has moved to the first octant (sin²θ₂₃ = 0.470), but the octant is unresolved and the prediction 0.5475 lies within the 3σ range (0.432–0.587). The second-octant local minimum of the NuFIT 6.1 χ² profile lies at 0.550, and the prediction deviates from it by 0.45%.[^nufitgrid]

[^nufitgrid]: The local minimum is obtained from the released grid by projecting over Δm²₃₁ and δ_CP; it lies at Δχ² ≈ 1.03 above the global minimum, with a grid step of 0.005 in sin²θ₂₃. Unless stated otherwise, all NuFIT 6.1 values quoted in this paper are the without-SK-atm, normal-ordering set, consistent with the Δm² inputs used above.

The reactor angle is sin²θ_{13} = 1/(N·|PG|) = 1/39 with NLO correction (k = N = 3):

$$\sin²θ_{13} = (1/39)(1 - 2ε/3) = 0.0219 \quad (\text{expt: } 0.02249,\; 2.6\%)$$

Sum rule: 7/13 = 3/13 + 4/13 (at LO, sin²θ₂₃ = sin²θ_W + sin²θ₁₂) is a finite-counting identity with denominator 13. This is a formal sum, not a partition of point sets: the 3 pure-weak points are contained in the 4 points of the complete electroweak line (the two sets overlap; their union is 4 points). The geometric origin of the atmospheric 7 directions is the disjoint union above. NLO corrections break this sum rule; Paper II gives its form.

**The PMNS and CKM phases.** The atmospheric holonomy ratio q₂₃ = (7/13)(1+ε/13) = sin²θ₂₃ also fixes the PMNS phase directly, proved as a theorem^II^:

$$\delta_{\rm PMNS} = 2\pi q_{23} = 197.1^\circ$$

The CKM phase does not reduce to a single closed-form expression of ε alone: it is fixed by embedding the three mixing quantities of §8.1 — the screened sinθ_C, |V_cb|, and |V_ub| — together with the CP-odd invariant J = πε⁵/N_flags in one unitary CKM matrix and solving sinδ = J/(c₁₂s₁₂c₂₃s₂₃c₁₃²s₁₃) together with cos δ > 0 (the sign fixed by the initial path lifting of A1). This is proved as a theorem^II^ and gives

$$\delta_{\rm CKM} = 62.595^\circ,\qquad \beta = 23.972^\circ,\qquad \gamma = 62.560^\circ$$

with the experimental values δ_CKM = 66.1° and γ = 66.4° [22]. Because β and γ follow rigidly from the same unitary matrix, their deviations from experiment are one and the same phase difference and are not counted as two independent tests^II^. The three angles and J are derived independently, so |sinδ| ≤ 1 is a non-trivial constraint; it holds for ε ≳ 0.204, and the derived value 0.2192 lies inside. Each transition formula formally tends to zero as ε → 0, but the four fit into a single unitary CKM matrix only in that range; they do not define a common ε → 0 CKM family.

## 8.3. Neutrino Properties

Whether neutrinos are Dirac or Majorana is an unresolved experimental question. This framework gives a clear prediction. Combining the phase covariance of the number-operator algebra (a → e^{iθ}a) with the derived particle census, the single Higgs, the four non-vanishing Dirac edges, the anomaly-free integral character lattice, and the naturality of the generation structure fixes the residual global phase direction uniquely as B−L^II^. The Majorana bilinear aa + a†a† (Δ(B−L) = 2) carries non-zero weight under this B−L and therefore has no invariant component. V-parity then pairs the distinct states ν and ν^c (lepton number L = ±1) into a Dirac fermion (operator-level proof: the Dirac-selection theorem of Paper II [20]). Therefore neutrinoless double beta decay is exactly zero:

$$0\nu\beta\beta = 0$$

With this, fermion mass ratios (§7), mixing angles, and neutrino properties have been obtained from the structure of V = −H and PG(2, F₃) (the absolute masses with normal ordering assumed and m_e as the single absolute scale). Where the Standard Model treats these as independent free parameters, this framework treats them all as different aspects of the algebraic expansion of a single equation V = -H.
