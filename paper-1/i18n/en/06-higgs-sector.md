# 6. The Higgs Sector

§5 derived the gauge coupling constants. The Standard Model has one more free parameter in the scalar sector — the Higgs self-coupling λ. This chapter derives the mathematical structure corresponding to it and shows the pinning of the internal vacuum and the boundedness of the internal potential (no instability channel).

## 6.1. Symmetry Breaking and Higgs Mass

Electroweak symmetry breaking is the statement that, while the dynamical laws remain symmetric, the vacuum (ground state) departs from the symmetric point. Since the W and Z are massive while the photon is massless, the vacuum cannot sit at the field-vanishing point (the symmetric point) — breaking is required by experiment. The Standard Model realises this through the assumption μ² > 0 in the Higgs potential V = −μ²|Φ|² + λ|Φ|⁴: it destabilises the origin, rolling the field to a finite value. But "why μ² > 0" is not explained within the Standard Model.

The V = −H(σ(φ)) of this paper answers this question through structure. The binary Shannon entropy H vanishes at both endpoints σ ∈ {0,1} (the trivial configurations corresponding to the field-vanishing point) and is maximal at the interior point σ = 1/2, so V = −H is a stable well that is 0 at the endpoints and reaches its minimum −ln 2 at the interior point (V''(0) = 1/4 > 0). Moreover A2 (σ ≠ 1) and A3 (σ ≠ 0) forbid the endpoints themselves. The unique minimum of the classical internal potential therefore necessarily lies at the interior point σ = 1/2 — the condition that the vacuum cannot sit at the symmetric point, i.e. the condition for breaking, follows from the shape of the entropy and the axioms rather than from destabilising the origin. What the Standard Model assumes as μ² > 0 becomes here a consequence of the shape of V.

Under the identification of §4.2, the line structure of PG(2, F₃) corresponds to the Higgs SU(2) doublet. The curvature at the centre — the Fisher metric at σ = 1/2 — gives the Higgs mass:

$$V''(0) = g_F(0) = \sigma(1-\sigma)\big|_{\sigma=1/2} = \tfrac{1}{4}$$

$$m_H/v = \sqrt{V''(0)} = 1/2 \quad (LO)$$

The NLO correction enters from all |PG| = 13 modes of the Laplacian matrix ℒ:

$$m_H/v = \frac{1}{2}\sqrt{1 + 2\varepsilon/|PG|} = 0.5084 \quad (\text{expt: } 0.5082,\; 0.03\%)$$

This corresponds to

$$\lambda = \tfrac{1}{2}(m_H/v)^2 = 0.1292\quad(\text{expt: } 0.1291,\ 0.06\%)$$

## 6.2. Vacuum Stability and the Hierarchy Problem

The Standard Model Higgs potential V_SM = −μ²h² + λh⁴ diverges as h → ∞, and the UV correction δμ² ∝ Λ² requires ~10³⁴ fine-tuning between the electroweak and Planck scales (hierarchy problem). Furthermore, the Higgs quartic coupling λ(μ) runs negative at μ ~ 10¹⁰ GeV, making the electroweak vacuum cosmologically metastable.

In the internal sector of V = −H, the instabilities corresponding to these problems do not arise. V = −H is bounded (V ∈ [−ln 2, 0]), with no high-energy divergence. The well depth |V_min| = ln 2 and curvature V''(0) = 1/4 are both O(1) algebraic constants; their ratio |V_min|/V''(0) = 4 ln 2 ≈ 2.77 is a ratio of internal quantities, an order-unity number requiring no fine-tuning:

$$V \in [-\ln 2,\ 0],\qquad |V_{\min}|/V''(0) = 4\ln 2 \approx 2.77$$

Relating this O(1) ratio to the 4D v²/Λ², and interpreting the boundedness as the reason the running coupling λ(μ) in 4D does not turn negative, both require the reconstruction matching (likewise the full 4D vacuum-stability interpretation and the correspondence to thermal properties such as symmetry restoration at high temperature)^II^. The shape of V is fixed by the axioms, and scale dependence does not alter the algebraic structure of V.

Furthermore, V = −H is uniquely determined as the canonical free energy of n ∈ {0,1} (§2). What the uniqueness of V fixes is the shape of the internal potential. Within the minimal operator algebra of the theory, no second fundamental scalar potential is generated, and that the weak-doublet scalar has multiplicity 1 — that the minimal reconstruction predicts a single Higgs doublet — is proved as a classification of one-forms on the finite internal carrier^II^.

**Summary of §5–§6.** sin²θ_W(M_Z) = 0.23122 (<0.01%), α_s(M_Z) = 0.1179 (0.07%), 1/α_em = 137.0368 (0.0006%; 137.035999084 at all orders^II^), m_H/v = 0.5084 (0.03%). All four coupling constants are derived from V = −H and PG(2,3) and agree with experiment. The vacuum is pinned at an interior point, the internal potential is bounded (no instability channel), and there is only one Higgs.
