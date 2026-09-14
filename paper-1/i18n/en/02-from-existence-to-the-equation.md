# 2. From Existence to the Equation

This chapter formalises three axioms about existence mathematically and shows that the fundamental equation V = −H is derived as an algebraic identity. From this equation, the geometric representation corresponding to the internal-symmetry structure of the Standard Model is uniquely determined^II^.

## 2.1. The Axioms

Paring the question of the introduction — might the existence of the universe itself, like quantum existence, be undetermined? — down to a form that can become an equation leaves three short sentences. What the three sentences speak of is a single proposition, prior to any property: that something exists. Which particles, what space, what laws — nothing of that is said yet. These three sentences are the entire input of the theory; no physical constant, no spacetime, and no postulate of quantum mechanics enters here.

**A1 (Existence):** Something exists. "Exists" is a proposition; it is either true or false — by the law of excluded middle, there is no third value. Writing the state of existence as n, the state space is n ∈ {0,1}. A1 defines the state space but does not determine the **value** of n.

What is bivalent is the *proposition* of existence, not a claim that the world is deterministic. To ask about the existence of something is, before asking about any of its properties, the single question: is it, or is it not? A1 fixes only the minimal structure this question carries — a one-bit state space. Everything that follows is built on this one bit.

**A2 (Uncertainty):** Existence is uncertain. Whatever exists does not exist with certainty: the occupation probability σ = ⟨n⟩ satisfies σ ≠ 1. A2 excludes the upper endpoint (certain existence) but says nothing about the lower endpoint.

If existence were certain (σ = 1), it would be an immovable background: nothing left to ask, nothing left to happen. As quantum theory teaches, microscopic existence is given only as a probability — A2 lifts this fact to the existence of the universe itself. Existence is not a given but something that *occurs*, carrying uncertainty. This one sentence is what later generates the statistical ensemble and the dynamics.

**A3 (Prohibition of non-existence):** Non-existence is not a state (σ ≠ 0). A way of being that consists in not-being is a contradiction.

"Nothing" is not a way for something to be. If σ = 0 were a realisation state, non-existence would be *there*, carrying data — the absence of being would be. A3 is the hardest-working of the three axioms: here it only removes the lower endpoint, but later it selects the coordinate by forbidding model data at the point of non-existence (§3.1) and selects the spatial dimension as the prohibition of boundary conditions (§3.4).

The three axioms are mutually independent — A1 removes the third truth value, A2 the upper endpoint, A3 the lower, each removing what the other two do not. And the three are exhaustive: together they leave only the open interval 0 < σ < 1 (§2.2), and no further axiom enters anywhere in this paper. The axioms are these three sentences; how they are realised mathematically is constructed in minimal form in the following sections, and the proof that no freedom of choice remains in that realisation is given^II^.

## 2.2. Bivalence and the Partition Function

Starting from the state space n ∈ {0,1} established by A1, we construct the partition function.

Since n takes only the values 0 and 1,

$$n^2 = n$$

follows — because the solutions of n(n − 1) = 0 are exactly {0,1}. However, A1 alone still admits the endpoint pure states n = 0 and n = 1, and no dynamics arises. A2 (σ ≠ 1) excludes certain existence; A3 (σ ≠ 0) excludes non-existence. Together they determine σ ∈ (0,1): the system is described as a canonical ensemble of a binary variable — an exponential family with mean parameter σ — neither certainly present nor certainly absent. The tilt weight e^{nφ} has its tilt coefficient fixed to 1 (the scale of φ; §3.1)^II^. n² = n truncates the sum to two terms, and the partition function is

$$Z = \sum_{n=0}^{1} e^{n\varphi} = 1 + e^{\varphi}$$

where φ = ln[σ/(1−σ)] (the logit transform) is the canonical coordinate of the exponential family.

Were n able to take values 0, 1, 2, … (Bose statistics), the sum would be an infinite series. As a consequence of the law of excluded middle, n² = n forbids this and restricts the occupation number of each binary mode to {0,1} — the exclusion of occupations 2, 3, … of that same mode, the Fermi–Dirac occupation statistics. This one-mode relation alone does not determine the exchange law between distinct modes — exchange antisymmetry (spin statistics) is fixed uniquely by the many-body realisation (§4.3)^II^.

The expectation σ = ⟨n⟩ = ∂lnZ/∂φ coincides with the Fermi–Dirac distribution, and its variance is the source of all subsequent structure:

$$\sigma = \frac{1}{1+e^{-\varphi}}, \qquad g_F = \sigma(1-\sigma) = \mathrm{Var}(n) > 0$$

These are not assumed but derived, from the combination of A1 (existence: n² = n), A2 (uncertainty: σ ≠ 1), and A3 (non-existence forbidden: σ ≠ 0). g_F is the gap between the binary observable (n² = n) and its uncertain expectation (σ² ≠ σ), and vanishes only at the pure values σ ∈ {0,1}.

## 2.3. The Effective Potential V = −H

§2.2 established the partition function Z = 1+e^φ. The next step is to construct an effective potential from it. The naive choice −ln Z diverges as φ → ∞, so a Legendre transform to the canonical free energy is required.

The logarithm W = ln Z of the partition function generates the classical field σ = dW/dφ, yielding the effective potential:

$$V(\varphi) = \varphi\sigma - W(\varphi) = \sigma\ln\sigma + (1-\sigma)\ln(1-\sigma) = -H(\sigma)$$

where H(p) = −p ln p − (1−p) ln(1−p) is the binary Shannon entropy [12].

That is, written out with its arguments, V(φ) = −H(σ(φ)): at each point of the canonical coordinate φ, the value of the potential equals minus the binary entropy of the occupation probability σ(φ). This is an algebraic identity — the canonical free energy of a single binary degree of freedom n ∈ {0,1} equals the negative of the Shannon entropy — and there is no freedom of choice. The bare form V = −H, used throughout, abbreviates this identity of functions.

The potential

$$V = -H$$

is thereby uniquely determined by axioms A1–A3 together with the exponential-family realisation above.

From this single equation, a mathematical structure corresponding to the structure of the Standard Model emerges, and values agreeing with physical constants to high precision are derived (§3–§10).

The derivation chain of this chapter is summarised as:

$$A1\text{–}A3 \;\Rightarrow\; n^2 = n,\; 0<\sigma<1 \;\Rightarrow\; Z = 1+e^{\varphi} \;\xrightarrow{\text{Legendre}}\; V = -H$$
