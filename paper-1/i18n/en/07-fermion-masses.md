# 7. Fermion Masses

§4–6 established the structures corresponding to gauge structure, coupling constants, and the Higgs mass. Based on the provisional identification of the generations made in §3, this chapter derives formulas for the mass ratios from the localisation of the bound states; the inter-generation mixing is derived in the next chapter. The derived mass ratios agree to high precision with experiment for charged leptons, quarks, and neutrinos — this agreement corroborates the provisional identification of §3.

## 7.1. Mass Formula

The three bound states of V = −H differ in localisation. The deepest ψ₀ is localised at the well bottom and couples most strongly to the gauge field, corresponding to the heaviest τ:

| Bound state | Energy | Localisation | Particle | Mass (MeV) |
|---|---|---|---|---|
| ψ₀ | E₀ = −0.485 | High (well bottom) | τ | 1777 |
| ψ₁ | E₁ = −0.159 | Medium | μ | 106 |
| ψ₂ | E₂ = −0.010 | Low (well edge) | e | 0.511 |

The mass ratios are determined by the localisation of the wave functions, not as independent parameters. The hierarchy that the Standard Model inputs by hand as three Yukawa couplings is given here by the difference in localisation of the three modes of one well. The key quantity is R = ln(m_τ/m_e)/ln(m_μ/m_e), which compresses the three-body mass hierarchy into a single number.

$$V = -H \xrightarrow{\text{§3}} \psi_n \xrightarrow{\text{IPR}} \mathrm{localisation} \xrightarrow{b} m_n \xrightarrow{} R = 1.5293$$

Each eigenstate has a binding energy |E_n| and a localisation, measured by the inverse participation ratio IPR_n = ∫|ψ_n|⁴dφ. Since the coupling to the gauge field is proportional to the wave-function amplitude at the interaction point, a more localised state acquires a larger mass: m_n ∝ IPR_n^b.

The exponent b is not a free parameter. In 0D there are no loop integrals, hence no running that would generate an anomalous dimension dynamically. By the Peter-Weyl theorem for finite groups, the heat kernel on the group is the finite sum K(t) = Σ_ρ dim(ρ) χ_ρ(g) e^{−λ_ρ t}, admitting only exponential decay with no power-law terms — the exponent is a structurally fixed quantity. The exponent b is the contact index derived from the normalisation of the finite incidence geometry PG(2, F₃): with the normalised single-leg index w_leg = (N+1)/N, b = 2w_leg = 8/3[^casimir]. The uniqueness of this mapping rule is a theorem^II^[^massuniq].

To this, a small correction from the anharmonicity of V = −H is added. The virial ratio |⟨V⟩_n|/T_n (potential to kinetic energy) measures how differently each mode samples the well, and its exponent is read as the per-mode marginality ε/N = 0.219/3 = 0.073 (ε from §3.2). The reading takes the total deficit to be carried by the three generation terminals (Tr D = ε) and reads the generation-terminal weight as the normalised evaluation on the three-terminal support, (1/3)Tr D = ε/3, independently of how the insertion is distributed. The value itself agrees with the Koide inversion below to 0.07%.

The complete mass formula is:

$$m_n \propto |E_n| \times \mathrm{IPR}_n^{\,b} \times (|\langle V \rangle_n| / T_n)^{\varepsilon/N}$$

The three factors have different origins:

| Factor | Physical meaning | Determined by |
|---|---|---|
| \|E_n\| | Energy scale | Binding energy |
| IPR^{b} | Localisation → coupling strength | Finite incidence geometry (contact index) |
| (|⟨V⟩|/T)^{ε/N} | Anharmonic correction | Spectral marginality |

All exponents are determined by V = −H. The result:

$$R = \frac{\ln(m_\tau/m_e)}{\ln(m_\mu/m_e)} = 1.5293 \quad (\text{expt: } 1.5294,\; 0.006\%)$$

(All spectral quantities computed with |φ|_max = 100, Δφ = 1.25×10⁻⁴ (N_grid = 1600001), verified stable under grid-resolution doubling and box enlargement.)

Koide's relation Q ≈ 3/2 [23] (this paper's convention Q = (Σ√m)²/Σm is the reciprocal of the standard 2/3) is not an input that determines b, but a cross-check — a verification on the output side. Parametrising the mass formula in Koide form yields the pair (b, c), where c is the exponent of the virial correction. Back-solving, for each b, the c required to force Q = 3/2, only b = 2w_leg = 8/3 returns a value, 0.0730, matching the spectral value ε/N = 0.073 (to 0.07%):

| b | c (Q=3/2) | Deviation |
|---|---|---|
| 2.0 | 0.437 | 500% |
| 2.5 | 0.163 | 120% |
| **8/3 = 2w_leg** | **0.0730** | **0.07%** |
| 2.78 | 0.012 | 84% |
| 3.0 | -0.107 | 246% |

| | Prediction | Experiment | Accuracy |
|---|---|---|---|
| m_τ/m_e | 3481 | 3477 | 0.1% |
| m_μ/m_e | 207.0 | 206.8 | 0.1% |
| R | 1.5293 | 1.5294 | 0.006% |
| Q (Koide) | 1.499985 | 1.500005(11) | 2σ (from PDG masses) |

The 0.006% agreement of R = 1.5293 quantitatively supports the identification of the bound states with the lepton generations. Because this quantity is measured to 6 × 10⁻⁶, the 0.006% difference amounts to about 10σ of the experimental uncertainty; it is a consequence of the truncation order used here, and the evaluation including the next order gives R = 1.529365 (0.0008%, −1.3σ), and the evaluation including the feedback term gives R = 1.529371 (−0.7σ)^II^. The stability of the Koide relation under radiative corrections is discussed by Sumino [43].

[^massuniq]: The functional form of the mass response and the contact exponent b = 2w_leg = 8/3 are given as uniqueness theorems in Paper II; the latter is a theorem once the correspondence carrying the finite-side eigenvalue into a power of the contact coordinate is fixed.

[^casimir]: This is not the physical colour charge of leptons. The exponent b is the contact index of the incidence geometry; its numerical agreement with the SU(3) fundamental Casimir, 2C_F = 8/3, holds only at N = 3 — (N²−1)/2N = (N+1)/N only for N = 3 — and is a consistency check at N = 3. See Paper II [20].

## 7.2. Quark Masses

The mass formula of §7.1 reproduced R = 1.5293 for leptons. Can the same formula be applied to quarks? The formula itself does not change — only the well depth changes.

Leptons are colour singlets and feel V = −H as a single copy. Quarks carry three colours. The colour-triplet well composes the three colour contributions — isomorphic copies of the same Bernoulli degree of freedom — as independent factors pulled back to the common existence coordinate φ: Z₃ = Z₁³, additivity of the logarithm gives log Z₃ = 3 log Z₁, and additivity of the Legendre dual gives V = −3H^II^; weak isospin does not deepen the well, because the doublet is an orientation structure within a single copy — it fixes which component is called I₃ = +1/2 (the g_c correction below) — and adds no second copy. The deeper well supports 5 bound states (n_WKB = 4.82). In the tables below, κ denotes the well-depth multiplier (the κ in V = −κH):

| Sector | Operator | κ | Bound states | Modes used |
|---|---|---|---|---|
| Lepton | −H | 1 | 3 | (0,1,2) = τ,μ,e |
| Up-type | −3H | 3 | 5 | (1,2,3) = t,c,u |
| Down-type | −3H (correction in kinetic term) | 3 | 4 | (0,1,2) = b,s,d |

**Up-type.** Mode 0 is deeply confined and belongs to the I_3 = −1/2 sector. Up-type quarks (I_3 = +1/2) use modes (1,2,3), giving R_up = 1.777 (expt: 1.7697(25), +0.41% = +2.9σ). The evaluation including the colour feedback term gives R_up = 1.767 (−0.17%, −1.2σ), and the same evaluation gives the light-quark mass ratio m_u/m_d = 0.477 (expt: 0.460(16))^II^.

**Down-type.** Up-type and down-type belong to the same SU(2) doublet and feel the same V = −3H, but differ in the sign of weak isospin (I_3 = +1/2 vs −1/2). This sign supplies a correction to the mass formula.

The total gauge charge of the SU(2) doublet (u, d), 2C_F + 1/N_c = N_c, is an exact algebraic identity. The physical mechanism originates from PG(2, F₃) geometry: among the N+1 = 4 points on line L, the reference point P₀ is the reference that orients the doublet (which component is called I_3 = +1/2), and the remaining 3 points generate SU(2). Reversing this orientation flips the sign of I_3 and reverses the SU(2) action, coupling the total charge N_c to g_F(φ) = σ(1−σ) (the Bernoulli Fisher metric g_F = Var(n) of §2.2; its uniqueness is Čencov's theorem [13]) with a negative sign. The effective mass is:

$$m_\mathrm{eff}(φ) = 1 − N_c σ(1−σ)$$

This is the static Fisher-limit form of the down-sector mass formula. The operator actually solved is the symmetric position-dependent-mass form −½ ∂_φ (1/m_eff) ∂_φ − 3H (identical to the discretisation in the accompanying verification code).

The correction coefficient g_c = −N_c = −3 (distinct from the normalisation g of §3.1) is fixed by the algebraic structure of the SU(2) doublet. The corrected operator has 4 negative eigenvalues (−1.5709, −0.5455, −0.1952, −0.00733; stable for box size L_box = 40/80/120), of which 3 modes (0,1,2) correspond to the physical window b, s, d — the physical window is uniquely determined by type exclusivity and order preservation^II^ (the window differs sector by sector: all 3 modes for leptons, (1,2,3) for up-type, (0,1,2) for down-type). With modes (0,1,2): R_down = 2.273 (expt: 2.276, 0.1%).

The mass ratios of all three charged-fermion sectors are reproduced:

| Sector | κ | g_c | R (pred.) | R (expt.) | Accuracy |
|---|---|---|---|---|---|
| Lepton | 1 | 0 | 1.529 | 1.529 | 0.006% |
| Up | N_c = 3 | 0 | 1.777 | 1.770 | 0.4% |
| Down | N_c = 3 | −N_c | 2.273 | 2.276 | 0.1% |

Here R captures the shape of the log-hierarchy---it is invariant under a uniform stretching of the mass ratios (raising every m_i/m_j to a common power)---not the individual masses. The accuracy column gives the deviation of the prediction from the experimental central value. The experimental R inherits the light-quark mass uncertainties (PDG 2026: m_u = 2.16 ± 0.07 MeV, etc.), which propagate to a width of about ±0.15–0.25%, and the comparison further depends on the scheme and scale conventions for each mass (light quarks MS-bar at 2 GeV, c and b at m(m), t from direct measurement).[^absquark]

[^absquark]: The individual quark magnitudes are not derived in this paper. Paper II derives the within-sector ratios and then gives a closed form for the six absolute masses written in derived quantities alone — the fixings of meaning are explicit physical identifications, with the conversion between schemes and definition points remaining as continuing computation. Agreement with the six measured masses used in assessing those identifications is not counted as independent validation.

## 7.3. Neutrino Masses and the Absolute Scale

§7.1–7.2 derived the charged-fermion (lepton and quark) mass ratios. What remains are the neutrinos.

**Mass predictions.** Neutrinos are colour singlets with κ = 1, coupling to V = −H — the same potential as charged leptons. The mass ratio R depends only on the well shape (IPR and virial ratios), not on particle species. The same well gives the same R:

$$R_\nu = R_\mathrm{lepton} = 1.529$$

This is the input-free prediction of this section. Together with the spectral ratio (m₃/m₂)² = 169/5 established below, it fixes the *dimensionless* mass ray completely, with no oscillation input at all.

Absolute masses in meV require one quantity that carries the dimensionless internal quantities into human units. This paper takes it to be the electron mass m_e = 0.51099895069(16) MeV (CODATA 2022 [34]) — the most precisely measured particle mass (relative 3 × 10⁻¹⁰), and a member of the linked mass system of charged leptons and neutrinos. This one point fixes the internal mass unit, and the electroweak scale v becomes a quantity predicted in that unit: v = 246.2360 GeV (+6.7 × 10⁻⁵ against the 246.2196 GeV fixed by the Fermi constant G_F = 1.1663788(6) × 10⁻⁵ GeV⁻²)^II^. No second scale is needed for the neutrino sector, and m_e itself is not counted as an independent prediction. The mass ratio between the lightest neutrino and the electron is derived from the specified operator word and read as a physical mass ratio in the same unit^II^:

$$\frac{m_1}{m_e} = x^3\,\frac{7}{6}\Bigl(1 + \frac{\varepsilon^2}{9}\Bigr) = 6.097 \times 10^{-10},\qquad x = \frac{9\alpha}{26\pi}$$

Here x is the expansion quantity of §5.3, which reappears in §8.1 as the colour screening of the Cabibbo angle; the ten orders of magnitude by which the neutrino masses fall below the charged-lepton masses follow from that quantity entering at the third power. The unit that displays the charged leptons therefore carries over to the neutrinos. No oscillation data enter the choice of any formula, coefficient or branch. Conditional on the normal-ordering branch, this gives[^numass]:

| Quantity | Prediction | Status |
|---|---|---|
| m_1 | 0.3116 meV | Unmeasured |
| m_2 | 8.667 meV | Consistent |
| m_3 | 50.39 meV | Consistent |
| Σm_i | 59.37 meV | Below Planck (<120) |

[^numass]: The displayed digits depend on where the higher-order charged-lepton evaluation used for the absolute normalisation is truncated; an identification concerning corrections beyond the displayed order is not yet fixed, and the displayed digits carry that condition^II^. Since the mass ray is fixed internally, all three masses scale with the common unit. The theory has no free parameters. Normal ordering is an input condition in this section; its independent derivation is given as a theorem^II^ (a consequence of R_ν > 1 and (m₃/m₂)² = 169/5 > 1). These values are consequences of setting the absolute scale m_e, and are not counted as independent predictions.

In that same unit, both oscillation splittings become quantities to be compared only after the computation is complete: Δm²₂₁ = 7.5016 × 10⁻⁵ eV² (against the measured 7.537 × 10⁻⁵ eV², −0.47%) and Δm²₃₁ = 2.5387 × 10⁻³ eV² (against the measured 2.521 × 10⁻³ eV², +0.70%). One degree of freedom tests this common unit, however, so the two must not be counted as two independent tests; their ratio tests the mass ray discussed next.

What the flag-Laplacian spectrum fixes exactly is

$$\Bigl(\frac{m_3}{m_2}\Bigr)^{\!2} = \frac{169}{5},\qquad \frac{m_3}{m_2} = \frac{|\mathrm{PG}|}{\sqrt{N+2}} = \frac{13}{\sqrt{5}} = 5.814$$

The numerator 169 is fixed by two elementary facts that follow from the spectrum of §5.3 alone. First, the non-zero eigenvalues 4∓√3 form a conjugate pair whose product reproduces the size of the projective plane exactly,

$$(4-\sqrt3)(4+\sqrt3) = 16 - 3 = 13 = |\mathrm{PG}(2,\mathbb F_3)|$$

so no separate normalisation enters. Second, write ς for the involution exchanging the eigenvectors v₁, v₂ of that pair and consider the doublet ψ = cos θ_H·v₁ + sin θ_H·v₂ (the coefficient angle θ_H is distinct from the atmospheric angle θ₂₃). Exchange invariance ςψ = ±ψ forces equal weights |cos θ_H| = |sin θ_H|, so the coherent amplitude has magnitude |13 sin 2θ_H| = 13 regardless of the choice of sign. The squaring of this amplitude to the intensity 13² = 169 is not a second identification; it is a theorem under the identification^II^.

The denominator 5 = N+2 = 3+2 is the rank of the solar-channel inventory, and its derivation — including the exhaustiveness of that inventory — is given as an operator-trace theorem^II^. The mass-squared-difference ratio, obtained by eliminating t = m₁/m₂ using R_ν = R_lepton, is given by the full relation^II^

$$\frac{\Delta m^2_{31}}{\Delta m^2_{21}} = \frac{169/5 - t^2}{1 - t^2} = 33.842\ldots\quad(\text{displayed as } 33.84)$$

With non-zero m₁, 169/5 is not the exact value of the mass-squared-difference ratio; the full relation above gives 33.84, with no oscillation input. The measured ratio is 2.521/0.07537 = 33.45, so the theoretical and measured values differ by 1.2%. Because no oscillation data were used to set the absolute scale, this difference is not absorbed anywhere: it stands as the quantity under test, and the unrounded masses behind the table above satisfy the internal ratio m₃/m₂ = 13/√5 = 5.814 exactly (recomputing from the displayed digits leaves rounding residue).

**Scope of the mass formula.** The mass formula of §7.1 determines mass ratios within a sector, and its overall proportionality constant is sector-dependent. Only the ratio joining the lightest neutrino to the electron is derived from the specified operator word, and with it the lepton mass system closes on the single absolute scale m_e^II^ — the dimensionless inter-sector ratio m(ν₃)/m(τ) ~ 3×10⁻¹¹ is fixed along with it. The absolute quark masses are given by the closed form of Paper II (footnote of §7.2), with the conversion between schemes and definition points remaining as continuing computation.
