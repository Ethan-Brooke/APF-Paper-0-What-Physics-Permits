# What Physics Permits: An Ontology for Admissibility Physics

### Interactive Mathematical Appendix to Paper 0 of the Admissibility Physics Framework

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.18605692.svg)](https://doi.org/10.5281/zenodo.18605692) [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Ethan-Brooke/APF-Paper-0-What-Physics-Permits/blob/main/APF_Reviewer_Walkthrough.ipynb)

[Interactive Derivation DAG](https://ethan-brooke.github.io/APF-Paper-0-What-Physics-Permits/) · [Theorem Map](#theorem-mapping-table) · [Reviewers' Guide](REVIEWERS_GUIDE.md) · [The full APF corpus](#the-full-apf-corpus) · [Citation](#citation)

> **AI agents:** start with [`START_HERE.md`](START_HERE.md) — operational checklist that loads the framework context in 5–10 minutes. The corpus inventory and full file map are in [`ai_context/repo_map.json`](ai_context/repo_map.json).

---

## Why this codebase exists

The ontology paper of the APF series. Three-book structure: Book I (the keystone, A1, admissibility structure, PLEC, descriptive reading); Book II (one chapter per technical paper, fixed six-section template); Book III (regime scoping, status, reading guide). Canonical sentence at three load-bearing placements.

This repository is the executable proof.

The codebase is a faithful subset of the canonical APF codebase v6.9 (frozen 2026-04-18; 355 verify_all checks, 342 bank-registered theorems across 19 modules + `apf/standalone/`). Each theorem in the manuscript traces to a named `check_*` function in `apf/core.py`, which can be called independently and returns a structured result.

The codebase requires Python 3.8+ and NumPy / SciPy (some numerical lemmas use them; see `pyproject.toml`).

## How to verify

Three paths, in order of increasing friction:

**1. Colab notebook — zero install.** [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Ethan-Brooke/APF-Paper-0-What-Physics-Permits/blob/main/APF_Reviewer_Walkthrough.ipynb) Every key theorem is derived inline, with annotated cells you can inspect and modify. Run all cells — the full verification takes under a minute.

**2. Browser — zero install.** Open the [Interactive Derivation DAG](https://ethan-brooke.github.io/APF-Paper-0-What-Physics-Permits/). Explore the dependency graph. Hover any node for its mathematical statement, key result, and shortest derivation chain to A1. Click **Run Checks** to watch all theorems verify in topological order.

**3. Local execution.**

```bash
git clone https://github.com/Ethan-Brooke/APF-Paper-0-What-Physics-Permits.git
cd APF-Paper-0-What-Physics-Permits
pip install -e .
python run_checks.py
```

Expected output:

```
      Paper 0 (What Physics Permits): 20 passed, 0 failed, 20 total — verified in <minutes>
```

**4. Individual inspection.**

```python
from apf.bank import get_check
r = get_check('check_L_epsilon_star')()
print(r['key_result'])
```

For reviewers, a [dedicated guide](REVIEWERS_GUIDE.md) walks through the logical architecture, the structural assumptions, and the anticipated objections.

---

## Theorem mapping table

This table maps every result in the manuscript to its executable verification.

| Check | Type | Summary |
|-------|------|---------|
| `check_L_epsilon_star` | Lemma | L_epsilon*: Minimum Enforceable Distinction. |
| `check_L_loc` | Lemma | L_loc: Locality from Admissibility Physics. |
| `check_L_nc` | Lemma | L_nc: Non-Closure from Admissibility Physics + Locality. |
| `check_T_canonical` | Theorem | T_canonical: The Canonical Object (Theorem 9.16, Paper 13 Section 9). |
| `check_T_alg` | Theorem | T_alg: Enforcement algebra A = Alg{E_d} cannot be faithfully represented |
| `check_T_Born` | Theorem | T_Born: Born Rule from Admissibility Invariance. |
| `check_T_Tsirelson` | Theorem | T_Tsirelson: CHSH bound <= 2*sqrt(2) from enforcement noncommutativity. |
| `check_L_gauge_template_uniqueness` | Lemma | L_gauge_template_uniqueness: SU(N_c)×SU(2)×U(1) is the Unique Gauge Template. |
| `check_T_gauge` | Theorem | T_gauge: SU(3)*SU(2)*U(1) from Capacity Budget. |
| `check_T_field` | Theorem | T_field: SM Fermion Content -- Exhaustive Derivation. |
| `check_L_Gram_generation` | Lemma | L_Gram_generation: Gram Bilinear for Generation Routing [P]. |
| `check_T_second_law` | Theorem | T_second_law: Second Law of Thermodynamics [P]. |
| `check_T_horizon_reciprocity` | Theorem | T_horizon_reciprocity: Bulk vs Horizon Entropy from Second-Epsilon Structure [P]. |
| `check_T7` | Theorem | T7: Generation Bound N_gen = 3 [P]. |
| `check_T_CKM` | Theorem | T_CKM: Zero-Parameter CKM Matrix Prediction [P]. |
| `check_T_CPTP` | Theorem | T_CPTP: CPTP Maps from Admissibility-Preserving Evolution. |
| `check_A9_closure` | Other | A9_closure: Unified Lovelock-Prerequisite Closure (A9.1..A9.5) [P]. |
| `check_L_spectral_action_internal` | Lemma | L_spectral_action_internal: Spectral Action = APF Partition Function [P]. |
| `check_T6B_beta_one_loop` | Theorem | T6B_beta_one_loop: 1-Loop SM Beta Functions from APF Content [P]. |
| `check_L_seesaw_type_I` | Lemma | L_seesaw_type_I: Type-I Seesaw from APF Dirac Operator [P]. |

All check functions reside in `apf/core.py`. Every function listed above can be called independently and returns a structured result including its logical dependencies and the mathematical content it verifies.

---

## The derivation chain

```
  Level 0: L_epsilon_star · L_loc · L_nc · T_canonical · T_alg · T_Born · T_Tsirelson · L_gauge_template_uniqueness · T_gauge · T_field · L_Gram_generation · T_second_law · T_horizon_reciprocity · T7 · T_CKM · T_CPTP · A9_closure · L_spectral_action_internal · T6B_beta_one_loop · L_seesaw_type_I
```

The [interactive DAG](https://ethan-brooke.github.io/APF-Paper-0-What-Physics-Permits/) shows the full graph with hover details and animated verification.

---

## Repository structure

```
├── README.md                              ← you are here
├── START_HERE.md                          ← AI operational checklist; read-first for AI agents
├── REVIEWERS_GUIDE.md                     ← physics-first walkthrough for peer reviewers
├── interactive_dag.html                   ← interactive D3.js derivation DAG (also served at docs/ via GitHub Pages)
├── repo_map.json                          ← machine-readable map of this repo (root copy of ai_context/repo_map.json)
├── theorems.json                          ← theorem catalog (root copy of ai_context/theorems.json)
├── derivation_graph.json                  ← theorem DAG as JSON (root copy of ai_context/derivation_graph.json)
├── ai_context/                            ← AI onboarding pack (corpus map, theorems, glossary, etc.)
│   ├── AGENTS.md                          ← authoritative entry point for AI agents
│   ├── FRAMEWORK_OVERVIEW.md              ← APF in 5 minutes
│   ├── GLOSSARY.md                        ← axioms, PLEC primitives, epistemic tags
│   ├── AUDIT_DISCIPLINE.md                ← engagement posture for critique/proposal
│   ├── OPEN_PROBLEMS.md                   ← catalog of open problems + verdicts
│   ├── repo_map.json                      ← machine-readable map of this repo
│   ├── theorems.json                      ← machine-readable theorem catalog
│   ├── derivation_graph.json              ← theorem DAG as JSON
│   └── wiki/                              ← bundled APF wiki (concepts, papers, codebase)
├── apf/
│   ├── core.py                            ← 20 theorem check functions
│   ├── apf_utils.py                       ← exact arithmetic + helpers
│   └── bank.py                            ← registry and runner
├── docs/
│   └── index.html                         ← interactive derivation DAG (GitHub Pages)
├── APF_Reviewer_Walkthrough.ipynb         ← Colab notebook
├── run_checks.py                          ← convenience entry point
├── pyproject.toml                         ← package metadata
├── zenodo.json                            ← archival metadata
├── Paper_0_What_Physics_Permits_v3.0.tex                ← the paper

└── LICENSE                                ← MIT
```

---

## What this paper derives and what it does not

**Derived:** (see Theorem mapping table above)

**Not derived here:** Specific results outside this paper's scope live in companion papers — see the corpus table below for the full 9-paper series.

---

## Citation

```bibtex
@software{apf-paper0,
  title   = {What Physics Permits: An Ontology for Admissibility Physics},
  author  = {Brooke, Ethan},
  year    = {2026},
  doi     = {10.5281/zenodo.18605692},
  url     = {https://github.com/Ethan-Brooke/APF-Paper-0-What-Physics-Permits}
}
```

For the full citation lineage (concept-DOI vs version-DOI, related identifiers, bibtex for all corpus papers), see [`ai_context/CITING.md`](ai_context/CITING.md).

---

## The full APF corpus

This repository is **one paper-companion** in a 9-paper series. Each paper has its own companion repo following this same layout. The full corpus, with canonical references:

| # | Title | Zenodo DOI | GitHub repo | Status |
|---|---|---|---|---|
| 0 | What Physics Permits **(this repo)** | [10.5281/zenodo.18605692](https://doi.org/10.5281/zenodo.18605692) | [`APF-Paper-0-What-Physics-Permits`](https://github.com/Ethan-Brooke/APF-Paper-0-What-Physics-Permits) | public |
| 1 | The Enforceability of Distinction | [10.5281/zenodo.18604678](https://doi.org/10.5281/zenodo.18604678) | [`APF-Paper-1-The-Enforceability-of-Distinction`](https://github.com/Ethan-Brooke/APF-Paper-1-The-Enforceability-of-Distinction) | public |
| 2 | The Structure of Admissible Physics | [10.5281/zenodo.18604839](https://doi.org/10.5281/zenodo.18604839) | [`APF-Paper-2-The-Structure-of-Admissible-Physics`](https://github.com/Ethan-Brooke/APF-Paper-2-The-Structure-of-Admissible-Physics) | public |
| 3 | Ledgers | [10.5281/zenodo.18604844](https://doi.org/10.5281/zenodo.18604844) | [`APF-Paper-3-Ledgers-Entropy-Time-Cost`](https://github.com/Ethan-Brooke/APF-Paper-3-Ledgers-Entropy-Time-Cost) | public |
| 4 | Admissibility Constraints and Structural Saturation | [10.5281/zenodo.18604845](https://doi.org/10.5281/zenodo.18604845) | [`APF-Paper-4-Admissibility-Constraints-Field-Content`](https://github.com/Ethan-Brooke/APF-Paper-4-Admissibility-Constraints-Field-Content) | public |
| 5 | Quantum Structure from Finite Enforceability | [10.5281/zenodo.18604861](https://doi.org/10.5281/zenodo.18604861) | [`APF-Paper-5-Quantum-Structure-Hilbert-Born`](https://github.com/Ethan-Brooke/APF-Paper-5-Quantum-Structure-Hilbert-Born) | public |
| 6 | Dynamics and Geometry as Optimal Admissible Reallocation | [10.5281/zenodo.18604874](https://doi.org/10.5281/zenodo.18604874) | [`APF-Paper-6-Dynamics-Geometry-Spacetime-Gravity`](https://github.com/Ethan-Brooke/APF-Paper-6-Dynamics-Geometry-Spacetime-Gravity) | public |
| 7 | Action, Internalization, and the Lagrangian | [10.5281/zenodo.18604875](https://doi.org/10.5281/zenodo.18604875) | [`APF-Paper-7-Action-Internalization-Lagrangian`](https://github.com/Ethan-Brooke/APF-Paper-7-Action-Internalization-Lagrangian) | public |
| 13 | The Minimal Admissibility Core | [10.5281/zenodo.18614663](https://doi.org/10.5281/zenodo.18614663) | [`APF-Paper-13-The-Minimal-Admissibility-Core`](https://github.com/Ethan-Brooke/APF-Paper-13-The-Minimal-Admissibility-Core) | public |
| — | Canonical codebase (v6.9) | [10.5281/zenodo.18604548](https://doi.org/10.5281/zenodo.18604548) | [`APF-Codebase`](https://github.com/Ethan-Brooke/APF-Codebase) | pending |

The canonical computational engine — the full bank of 342 theorems across 19 modules — is the **APF Codebase** ([Zenodo](https://doi.org/10.5281/zenodo.18604548)). Every per-paper repo is a faithful subset of that engine.

---

## License

MIT. See [LICENSE](LICENSE).

---

*Generated by the APF `create-repo` skill on 2026-04-19. Codebase snapshot: v6.9 (frozen 2026-04-18; 355 verify_all checks, 342 bank-registered theorems, 48 quantitative predictions).*
