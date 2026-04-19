# Reviewers' Guide — APF Paper 0: What Physics Permits: An Ontology for Admissibility Physics

This guide is the physics-first walkthrough for peer reviewers of What Physics Permits: An Ontology for Admissibility Physics. It addresses the structural assumptions, anticipated objections, and falsification surfaces of the paper's argument. The intended audience is a peer reviewer with a background in physics or mathematics.

The guide complements three other verification routes:
- The [executable codebase](apf/) (run `python run_checks.py` for the full 20-theorem verification);
- The [Colab notebook](APF_Reviewer_Walkthrough.ipynb) (zero-install, theorem-by-theorem cells with prose + code);
- The [interactive derivation DAG](https://ethan-brooke.github.io/What-Physics-Permits/) (hover-for-details, click-for-dependencies, animated verification).

---

## The derivation in 20 steps

The full chain from the foundational commitments to this paper's results:

**Step 1 — L_epsilon_star** (`check_L_epsilon_star`)

  L_epsilon*: Minimum Enforceable Distinction.


**Step 2 — L_loc** (`check_L_loc`)

  L_loc: Locality from Admissibility Physics.


**Step 3 — L_nc** (`check_L_nc`)

  L_nc: Non-Closure from Admissibility Physics + Locality.


**Step 4 — T_canonical** (`check_T_canonical`)

  T_canonical: The Canonical Object (Theorem 9.16, Paper 13 Section 9).


**Step 5 — T_alg** (`check_T_alg`)

  T_alg: Enforcement algebra A = Alg{E_d} cannot be faithfully represented


**Step 6 — T_Born** (`check_T_Born`)

  T_Born: Born Rule from Admissibility Invariance.


**Step 7 — T_Tsirelson** (`check_T_Tsirelson`)

  T_Tsirelson: CHSH bound <= 2*sqrt(2) from enforcement noncommutativity.


**Step 8 — L_gauge_template_uniqueness** (`check_L_gauge_template_uniqueness`)

  L_gauge_template_uniqueness: SU(N_c)×SU(2)×U(1) is the Unique Gauge Template.


**Step 9 — T_gauge** (`check_T_gauge`)

  T_gauge: SU(3)*SU(2)*U(1) from Capacity Budget.


**Step 10 — T_field** (`check_T_field`)

  T_field: SM Fermion Content -- Exhaustive Derivation.


**Step 11 — L_Gram_generation** (`check_L_Gram_generation`)

  L_Gram_generation: Gram Bilinear for Generation Routing [P].


**Step 12 — T_second_law** (`check_T_second_law`)

  T_second_law: Second Law of Thermodynamics [P].


**Step 13 — T_horizon_reciprocity** (`check_T_horizon_reciprocity`)

  T_horizon_reciprocity: Bulk vs Horizon Entropy from Second-Epsilon Structure [P].


**Step 14 — T7** (`check_T7`)

  T7: Generation Bound N_gen = 3 [P].


**Step 15 — T_CKM** (`check_T_CKM`)

  T_CKM: Zero-Parameter CKM Matrix Prediction [P].


**Step 16 — T_CPTP** (`check_T_CPTP`)

  T_CPTP: CPTP Maps from Admissibility-Preserving Evolution.


**Step 17 — A9_closure** (`check_A9_closure`)

  A9_closure: Unified Lovelock-Prerequisite Closure (A9.1..A9.5) [P].


**Step 18 — L_spectral_action_internal** (`check_L_spectral_action_internal`)

  L_spectral_action_internal: Spectral Action = APF Partition Function [P].


**Step 19 — T6B_beta_one_loop** (`check_T6B_beta_one_loop`)

  T6B_beta_one_loop: 1-Loop SM Beta Functions from APF Content [P].


**Step 20 — L_seesaw_type_I** (`check_L_seesaw_type_I`)

  L_seesaw_type_I: Type-I Seesaw from APF Dirac Operator [P].



Each step is a single theorem. The dependencies form a directed acyclic graph (DAG) with no cycles; the [interactive DAG](https://ethan-brooke.github.io/What-Physics-Permits/) shows multiple derivation paths to the same result, which is structural redundancy: many results are over-determined and would survive even if individual derivation steps were weakened.

---

## Pre-empting the operational-witness objection

A common objection to executable mathematical appendices is that the test-case witnesses (specific small examples used to verify the theorem) "smuggle in" the very structure being derived. Each test-case witness in this paper is the smallest concrete instance of a structure already proved in the abstract argument. Witnesses are constructed *after* the abstract claim is established, never before. The reviewer can re-derive each witness from the abstract derivation chain, not the other way around. If a witness appears to smuggle structure in, the corresponding `check_*` function will fail when the witness is replaced with an explicit countermodel.

---

## The structural assumptions

Beyond Axiom A1, this paper relies on the four PLEC components and a small set of structural regularity conditions:

- **A1 (Finite Enforcement Capacity)** — at any interface, the total enforcement cost across maintained distinctions is bounded.
- **MD (Minimum Distinction)** — every physical distinction has strictly positive enforcement cost (positive floor μ\* > 0).
- **A2 (Argmin selection)** — the realized configuration is the argmin of cost over the admissible set.
- **BW (Boundary Weight / Non-degeneracy)** — the cost spectrum is rich enough that the argmin is generically informative.

The four are pairwise logically independent (proved in Paper 1's Technical Supplement §1 with explicit countermodels). Together they define the variational structure named the **Principle of Least Enforcement Cost (PLEC)**: *reality is the minimum-cost expression of distinction compatible with finite capacity.*

_No paper-specific assumptions beyond the PLEC framework._

---

## The identifications

Several mappings between enforcement concepts and standard mathematical structures are used in the paper. They are **motivated, not deduced**, and reviewers should pay particular attention to their justification:

1. **Distinction ↔ binary partition of admissible configurations.** Spencer-Brown's distinction primitive (drawing the line between *this* and *not-this*) is identified with a binary measurement / partition at an enforcement interface. Motivated, not deduced.

2. **Cost ↔ resource expenditure.** The framework's $\varepsilon(d)$ functional is identified with the operational resource (energy / mass / barrier height) that maintains a distinction in any specific laboratory instance. This is a multi-resource correspondence; specific identifications appear in domain-specific papers (Paper 7 for action / Lagrangian, Paper 6 for spacetime metric, etc.).

3. **Capacity bound ↔ physical scarcity.** $C(\Gamma) < \infty$ at every interface is identified with the universally observed pattern that any specific physical system supports finitely many distinguishable states (Bekenstein--Hawking, Landauer, Ashby). Motivated by these traditions; not derived from them.

4. **Argmin ↔ realization.** The realized configuration at an interface is identified with the $\arg\min$ of total enforcement cost over the admissible set. This is a *locator*, not a process: nothing is doing the optimization; the argmin is what realization *means* under the framework.

These identifications are conventional rather than discovered: they are the choice that makes the framework's vocabulary and standard mathematics align. None is internally derivable.

---

## What is *not* proved in this paper

To prevent scope inflation, the following are flagged explicitly as *outside* the scope of What Physics Permits:

- **Specific gauge-group derivations** belong to Paper 2; this paper assumes them as imports if cited.
- **Specific particle content / generation count** belongs to Papers 2 and 4; not derived here.
- **Quantitative cosmological observables** beyond what is explicitly cited belong to Papers 3 (entropy / horizon) and 6 (geometry / DESI).
- **Quantum-gravity backreaction** is out of scope for any single paper in the v6.8 series; it is a future direction.
- **Numerical mass values** (absolute scales for $m_t$, $m_b$, $m_\nu$) are open problems noted in Paper 4 and the Engine paper; not within this paper's scope.
- **Spacetime dimension** (D = 4) is structurally derived in Paper 6 from Lovelock uniqueness; this paper assumes it where used.

If a reviewer concludes that the paper claims any of the above without supplying a proof for it, the reviewer is correct that the paper does not deliver that claim — those claims belong to other papers in the series and are explicitly flagged as such.

---

## How to falsify: attack surfaces

Each falsifier below targets a specific theorem or structural assumption. The corresponding code change in `apf/core.py` is also identified; reviewers can modify the codebase and re-run `python run_checks.py` to test each surface directly.

| # | Surface | Code-level test |
|---|---------|------------------|
| 1 | **Numerical disagreement.** A predicted observable disagrees with experiment beyond the framework's stated tolerance. | Modify the corresponding `check_*` to use the published experimental value; observe failure. |
| 2 | **Structural redundancy collapse.** Removing one PLEC component (A1, MD, A2, BW) leaves the derivation chain intact. | Comment out the test for the removed component in `apf/core.py`; observe other downstream checks failing. |
| 3 | **Reconstruction-program parity.** A standard quantum reconstruction (Hardy / CDP / Masanes--Müller) reaches the same conclusion with a strictly weaker assumption set. | Extract the GPT axioms used by the comparator; supply them as inputs to the relevant `apf/core.py` functions. |
| 4 | **Composition / locality break.** A multi-interface test with one interface deliberately violating $L_{\rm loc}$ does not produce the expected falsification mode. | Modify `check_L_loc` countermodel; rerun and observe expected vs. actual behavior. |
| 5 | **Cost-functional uniqueness fails.** An alternative cost functional satisfies all framework axioms equally well. | Replace the cost functional in `apf_utils.py`; observe whether downstream checks still pass. |
| 6 | **Scope-creep test.** A claim attributed to this paper is shown to actually require an unstated assumption. | Trace the claim's `\coderef`s through the bank dependency chain; identify any check that exits the paper's named scope. |

This is a structured threat model. If any of the surfaces fails empirically, the paper falsifies on that specific point.

---

## Reading the code

The codebase has three files in `apf/`:

- **`apf/core.py`** — the 20 theorem check functions for this paper. Each function constructs a mathematical witness, verifies the theorem's claim, and returns a structured result with name, dependencies, status, and key result.
- **`apf/apf_utils.py`** — exact arithmetic utilities (mostly `Fraction`-based; numpy/scipy where required by specific numerical lemmas).
- **`apf/bank.py`** — registry of all check functions in this repo, plus the `run_all()` runner.

Execution model: `run_checks.py` calls `bank.run_all()`, which iterates over every registered check and aggregates pass/fail/error counts. Individual checks can be invoked via `apf.bank.get_check('T_Born')()`.

---

## Scalar-to-matrix boundary

A characteristic feature of the APF program is that the early derivations use only finite sets and exact rational arithmetic (no matrices, no complex numbers, no linear algebra). Matrices first appear at the GNS construction (T2 in Paper 1), as the *minimal representation* of structure that the earlier scalar-only theorems prove must exist. This paper inherits the scalar-to-matrix transition from Paper 1's $T_2$. No new derivations of matrix structure occur in this paper; matrices appear where Paper 1 already established them.

This stratification is a deliberate methodological commitment: matrices are derived as representations of an already-proved abstract structure, not assumed as the substrate of the framework.

---

## The complex-field justification

The complex numbers as the unique admissible amplitude field is not a postulate but a derived selection (Paper 1 T2c, with proved exclusions $P_{\rm tom}$ and $P_{\rm cls}$ ruling out $\mathbb{R}$ and $\mathbb{H}$ respectively). This paper does not re-derive the complex-field selection; it inherits from Paper 1 ($T_{2c}$, with proved exclusions $P_{\rm tom}$ and $P_{\rm cls}$). For the original derivation, see Paper 1's [REVIEWERS_GUIDE.md](https://github.com/Ethan-Brooke/The-Enforceability-of-Distinction/blob/main/REVIEWERS_GUIDE.md).

---

## Citation and Zenodo

This repository is the executable mathematical appendix to APF Paper 0. The canonical archival deposit is at [https://doi.org/10.5281/zenodo.18605692](https://doi.org/10.5281/zenodo.18605692) (DOI: 10.5281/zenodo.18605692).

---

*Generated by the APF `create-repo` skill. Codebase snapshot: v6.8 (frozen 2026-04-18; 348 verify_all checks, 335 bank-registered theorems, 48 quantitative predictions).*
