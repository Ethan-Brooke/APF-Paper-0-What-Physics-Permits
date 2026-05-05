# LANGUAGE_CONVENTION.md — Operational/structural translation for AI-assisted readers

This file captures the framework's eternalist commitment and the operational/structural translation rule that governs every prose deliverable in the corpus. AI agents working on APF code, papers, or documentation should read this once, then apply the convention silently throughout any output.

The canonical source is **Paper 0 §1 ("A note on language")** + **Paper 0 Descriptive Reading chapter** (subsection: "Temporal language and the eternalist commitment"). The canonical supplement-level companion is **Paper 1 supplement v8.24 §1 ("On the use of operational language")**.

---

## The commitment, in one paragraph

Admissibility Physics is, at its deepest level, a structural framework. **Admissibility space is a static algebraic object**, and what reads in the prose throughout the corpus as enforcement, maintenance, evolution, propagation, equilibration, recruitment, or perturbation is the **local reading of that structure under a temporal slicing**. Time itself is derived: Paper 3 derives the arrow of time as the loss of global admissible coordination, and Paper 6 derives the metric and dimensionality of spacetime. The framework cannot use time-language in its primitives without smuggling what it is supposed to derive.

The framework is, philosophically, an **eternalist position**. APF sits in the company of block-universe readings of general relativity, the Wheeler–DeWitt timeless quantum gravity programme, and the Page–Wootters mechanism for time emergence in entangled quantum systems — structural at the foundation, with time as a derived feature of how the structure is read locally.

---

## The translation rule

The corpus uses operational vocabulary throughout. Both readings refer to the same fact — the structural reading is what the framework fundamentally commits to, and the operational reading is what that commitment looks like under temporal slicing.

| Operational reading (local) | Structural reading (foundation) |
|---|---|
| "The world maintains the distinction." | "Admissibility space at the interface carries the distinction." |
| "Enforcement holds the partition against perturbation." | "The partition admits a finite positive cost commitment." |
| "Capacity is paid out instant by instant." | "Capacity is the structural budget bound at the interface." |
| "The field carries the cost moment by moment." | "The field is what carries the cost commitment at the interface." |
| "X enforces Y." | "Y is the pattern of distinctions sustained by enforcement at interface X." |
| "Capacity is consumed / spent / dissipated." | "Capacity is committed / partitioned / arranged." (No agent, no irreversibility implied.) |
| "Enforcement requires a finite budget at every interface." | "The world enforces only finitely much at each interface." (A1 content; the first phrasing is correct.) |
| "Records form" / "paths extremize" / "saturation reaches the endpoint." | Static structures on the admissible set. |
| "Becomes available only after gates close." | "Conditional on the gates' joint structural validity." |
| "Admissible chart changes become diffeomorphism-type relabelings." | "In the smooth represented regime, the admissible relabelings are exactly the diffeomorphism-type ones." |

A reader (or AI agent) who wants the structural reading can take every operational verb as shorthand for the local reading of the corresponding admissibility-space structure.

---

## Why this matters for code and AI work

The codebase is the framework's operational specification: every check function is a static algebraic test on admissibility-space structure. AI agents reading or extending the code should:

1. **Treat docstring temporal verbs as descriptive convention, not foundational primitives.** A function named `check_T_decoherence` does not commit the framework to "decoherence as a process that happens in time"; it tests a static algebraic property of the admissibility class transition that the broader framework reads operationally as decoherence.

2. **Do not invent temporal premises in proofs.** If a check function's claim can be stated structurally (admissibility-set property, capacity bound, cost-functional minimum, identity between projections), state it that way. Avoid premises of the form "if the system evolves..." when the structural premise is "if the configuration sits in admissible class A and the cost-functional admits an argmin in class B...".

3. **Apply the no-rearview discipline** when writing prose for paper bodies, supplement passages, READMEs, ai_context files, or Zenodo descriptions: cut version stamps, phase numbers, rearview comparatives, internal-process framings. Body prose should work for a reader who has never seen any earlier version.

4. **Honor the descriptive convention when explaining APF results to a user.** Operational vocabulary is licensed (it grounds the abstract structure in the experimental world physicists actually inhabit), and the structural reading is always available on request.

---

## Where the convention is anchored, paper by paper

| Paper | Anchor location |
|---|---|
| Paper 0 (Ontology) | §1 "A note on language" + Descriptive Reading chapter, "Temporal language and the eternalist commitment" |
| Paper 1 supplement (Spine) | §1 "On the use of operational language" |
| Paper 3 supplement (Ledgers, Entropy, Time, Cost) | front-matter "On operational language" note |
| Paper 5 supplement (Quantum Structure) | front-matter "On operational language" note |
| Paper 6 supplement (Dynamics and Geometry) | front-matter "On the use of operational language" note |
| Paper 7 supplement (Action) | front-matter tcolorbox "On operational language: variational vocabulary as locator-language" |
| Paper 9 (Geometric Substrate) | §1 "On operational language" — addresses metric-emergence ladder |
| Paper 10 (Calculus of Finite Continuability) | §1 "On operational language" — language-layer commitment + dual reading of $\Gamma\vDash_C D\rightsquigarrow E$ |
| Papers 2 / 4 / 8 / 24 supplements | brief front-matter cross-reference to canonical sources |
| Main papers (3, 5, 6, 7) | brief framework-positioning note cross-referencing Paper 0 §1 + Paper 1 sup §1 |

---

## House-voice corollary

The voice guide (`Reference - APF House Voice (2026-04-30).md` in `APF Reference Docs/`) develops the prose register; the eternalist commitment is the substantive content the voice serves at the level of foundational claims. Apply both: the voice tells you how to say it, the convention tells you what the saying is committed to.

---

## TL;DR for AI agents

- Operational vocabulary in APF prose is **descriptive convention**, not foundation.
- The framework commits to **admissibility space as a static algebraic object**.
- Time is **derived** (Paper 3 + Paper 6), not presupposed.
- When in doubt, translate operational verbs to structural-reading equivalents from the table above.
- The canonical sources for the convention are Paper 0 §1 + Paper 0 Descriptive Reading chapter + Paper 1 supplement v8.24 §1.
