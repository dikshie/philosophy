# Philosophy Study Workspace

A structured 1-Year Self-Study program in fundamental Philosophy tailored specifically for backgrounds in **Physics** (Special Relativity, General Relativity, Time, and Quantum Field Theory) and **Computer Science** (Type Theory, Formal Systems, Neural Systems & Connectionism), utilizing exclusively the peer-reviewed [Stanford Encyclopedia of Philosophy (SEP)](https://plato.stanford.edu/).

## Structure & Schedule

- **Time Commitment**: 2 hours/day, 5 days/week (Monday–Friday, excluding weekends & national holidays).
- **Duration**: 52 Weeks (48 active academic weeks, 4 holiday/consolidation buffer weeks).
- **Core Plan**: See [`STUDY_PLAN.md`](STUDY_PLAN.md) for the master daily and weekly syllabus.
- **Reference Standard**: 100% textbook-free; all citations point to canonical SEP articles.

---

## Directory Structure

```text
philosophy/
├── README.md                          # Workspace orientation
├── STUDY_PLAN.md                      # Comprehensive 52-week master curriculum
├── formal_logic/                      # Mathematical and formal specifications (W01–W13)
│   └── FORMAL_LOGIC_W01_W13.md        # Comprehensive formal logic treatise for Weeks 01 to 13
├── lean/                              # Lean 4 formal proofs & interactive verification (W01–W13)
│   ├── Week01_ClassicalLogic.lean     # Natural deduction, De Morgan, classical principles
│   ├── Week02_ModalLogic.lean         # Kripke frames, accessibility relations, K, T, S4, S5
│   ├── Week03_Computability.lean      # Halting problem undecidability, reduction
│   ├── Week04_TypeTheory.lean         # Curry-Howard isomorphism, propositions-as-types
│   ├── Week05_Incompleteness.lean     # Formal theories, consistency, Gödel sentence
│   ├── Week06_Information.lean        # Semantic information, veridicality, Landauer bound
│   ├── Week07_EpistemicLogic.lean     # Knowledge operators, JTB, Gettier counterexamples
│   ├── Week08_BayesianEpistemology.lean# Probability spaces, conditionalization, Dutch books
│   ├── Week09_Demarcation.lean        # Popperian falsification, Duhem-Quine bundles
│   ├── Week10_ScientificRealism.lean  # Empirical adequacy, unobservables, submodels
│   ├── Week11_TheoryReduction.lean    # Nagelian bridge laws, reduction relations
│   ├── Week12_EpistemicSynthesis.lean # Constructive proof & Bayesian evidence synthesis
│   └── Week13_OntologySubstance.lean  # Quinean ontological commitment, mereology axioms
├── python/                            # Runnable Python simulations & computational tools (W01–W13)
│   ├── week01_sat_prover.py           # Truth table generator & DPLL SAT solver
│   ├── week02_kripke_checker.py       # Modal logic Kripke model checker (Box, Diamond)
│   ├── week03_turing_machine.py       # Deterministic Turing Machine simulator & Halting demo
│   ├── week04_lambda_typechecker.py   # Simply-typed lambda calculus & Curry-Howard typechecker
│   ├── week05_godel_numbering.py      # Prime factorization Gödel encoder & Diagonal simulator
│   ├── week06_information_theory.py   # Shannon entropy vs Floridi semantic information
│   ├── week07_gettier_simulator.py    # Epistemic state evaluator & Gettier case diagnosis
│   ├── week08_bayesian_updater.py     # Bayesian sequential updater & Dutch Book checker
│   ├── week09_falsification_engine.py # Popperian falsifier & Duhem-Quine web simulator
│   ├── week10_realism_evaluator.py    # van Fraassen constructive empiricism evaluator
│   ├── week11_nagelian_reduction.py   # Nagelian bridge law derivation engine
│   ├── week12_q1_formal_verifier.py   # Unified test runner across all Q1 Python tools
│   └── week13_mereology_ontology.py   # Classical Extensional Mereology & Quine commitment
└── notes/
    ├── templates/
    │   └── daily-note-template.md     # Standard 2-hour daily note-taking template
    ├── q1/ (Weeks 01–12)              # Logic, Type Theory, Computability & Epistemology
    ├── q2/ (Weeks 13–24)              # Metaphysics, SR, GR, Time & QFT
    ├── q3/ (Weeks 25–36)              # Mind, Language, Neural Systems & AI Ethics
    ├── q4/ (Weeks 37–48)              # Ethics, Political Philosophy & Western Canon
    └── capstone/ (Weeks 49–52)        # Three Capstone Treatises & Annual Retrospective
```

---

## Executing the Computational Tools

### Python Verifier Suite
Run the unified test runner for all Quarter 1 tools:
```bash
python3 python/week12_q1_formal_verifier.py
python3 python/week13_mereology_ontology.py
```

### Lean 4 Interactive Proofs
Open any file in the `lean/` directory (e.g., `lean/Week04_TypeTheory.lean`) inside VS Code with the Lean 4 extension, or verify from the terminal:
```bash
lean lean/Week01_ClassicalLogic.lean
```

---

## The Four Quarters at a Glance

1. **Quarter 1: Logic, Type Theory, Computability & Epistemology (Weeks 1–12)**
   - Classical & Modal Logic, Turing Computability, **Intuitionistic Type Theory & Curry-Howard Isomorphism**, Gödelian Limits, Information Theory, Bayesian Epistemology, Popperian Demarcation, and Scientific Realism.
2. **Quarter 2: Metaphysics, Spacetime, Time & Quantum Field Theory (Weeks 13–24)**
   - Core Ontology, Mereology, Causality & Determinism, **Special Relativity & Conventionality of Simultaneity**, **General Relativity & The Hole Argument**, **Metaphysics of Time (A/B Series, Presentism)**, **Thermodynamic Arrow & Past Hypothesis**, **Time Travel & CTCs in GR**, and **QFT Ontology (Haag's Theorem, Particles vs Fields, Ontic Structural Realism)**.
3. **Quarter 3: Philosophy of Mind, Language, and Neural Systems (Weeks 25–36)**
   - Dualism vs. Physicalism, Functionalism, Consciousness (Hard Problem/Qualia), Intentionality, Chinese Room Argument, **Neural Systems & Connectionism (PDP, high-dimensional latent manifolds)**, **Neural vs. Symbolic Computation (Systematicity debate)**, Frege, Russell, Wittgenstein, and AI Ethics/Safety.
4. **Quarter 4: Ethics, Political Philosophy, and the Western Canon (Weeks 37–48)**
   - Metaethics, Utilitarianism, Kantian Deontology, Virtue Ethics, Rawlsian Justice & Social Contract, Philosophy of Technology, Presocratics, Plato, Aristotle, Early Modern Rationalists & Empiricists, Kant, and Naturalism/Pragmatism.
5. **Weeks 49–52: Integrated Capstone & Year-End Synthesis**
   - Three formal capstone research treatises synthesizing physics invariants, type systems, and neural architectures with philosophical foundations.
