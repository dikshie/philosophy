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

## Installing Lean 4

Lean 4 is managed via **`elan`** (the official Lean version manager, similar to `rustup` in Rust). Below are platform-specific installation instructions for macOS, Linux, FreeBSD, and Windows 11.

### 1. macOS (Apple Silicon & Intel)

#### Option A: Via Homebrew (Recommended)
```bash
brew install elan-init
elan toolchain install stable
elan default stable
```

#### Option B: Via Official Shell Script
```bash
# 1. Download and run elan installer
curl -sSf https://raw.githubusercontent.com/leanprover/elan/master/elan-init.sh | sh -s -- -y

# 2. Source environment in current shell (and add to ~/.zshrc)
source "$HOME/.elan/env"

# 3. Set stable toolchain
elan default stable
```

---

### 2. Linux (Ubuntu, Debian, Fedora, Arch) & FreeBSD

#### Linux (Ubuntu / Debian / Fedora / Arch)
1. Ensure build prerequisites and `curl` are installed:
   ```bash
   # Ubuntu / Debian
   sudo apt update && sudo apt install -y curl git gcc g++ make

   # Fedora / RHEL
   sudo dnf install -y curl git gcc gcc-c++ make

   # Arch Linux
   sudo pacman -S curl git base-devel
   ```
2. Install `elan`:
   ```bash
   curl -sSf https://raw.githubusercontent.com/leanprover/elan/master/elan-init.sh | sh -s -- -y
   source "$HOME/.elan/env"
   elan default stable
   ```

#### FreeBSD
On FreeBSD, install prerequisites using `pkg`:
```bash
# 1. Install prerequisites
sudo pkg install curl git bash gmake llvm

# 2. Run elan-init using bash
curl -sSf https://raw.githubusercontent.com/leanprover/elan/master/elan-init.sh | bash -s -- -y

# 3. Add elan to your shell profile (~/.shrc, ~/.bashrc, or ~/.zshrc)
echo 'export PATH="$HOME/.elan/bin:$PATH"' >> ~/.zshrc
source ~/.zshrc

# 4. Set toolchain
elan default stable
```
*(Note: If precompiled FreeBSD binaries are unavailable for a specific snapshot, FreeBSD Linux binary compatibility can be enabled via `kldload linux64`, or build via FreeBSD ports `math/lean4`.)*

---

### 3. Windows 11

#### Option A: Native PowerShell (Recommended)
1. Open **PowerShell** (Run as Administrator or standard terminal) and execute:
   ```powershell
   Invoke-WebRequest -Uri "https://raw.githubusercontent.com/leanprover/elan/master/elan-init.ps1" -OutFile "elan-init.ps1"
   .\elan-init.ps1 -y
   Remove-Item .\elan-init.ps1
   ```
2. Close and re-open PowerShell to refresh your `PATH`.
3. Set default toolchain:
   ```powershell
   elan default stable
   ```

#### Option B: Via Windows Package Manager (`winget`)
```powershell
winget install leanprover.elan
elan default stable
```

#### Option C: Via WSL2 (Windows Subsystem for Linux)
If working within WSL2 (Ubuntu on Windows 11), follow the standard [Linux instructions](#linux-ubuntu--debian--fedora--arch):
```bash
curl -sSf https://raw.githubusercontent.com/leanprover/elan/master/elan-init.sh | sh -s -- -y
source "$HOME/.elan/env"
elan default stable
```

---

### 4. Recommended Editor Setup: Visual Studio Code

Regardless of operating system:
1. Install [Visual Studio Code](https://code.visualstudio.com/).
2. Open VS Code Extensions (`Ctrl+Shift+X` or `Cmd+Shift+X`).
3. Search for and install **`Lean 4`** (Extension ID: `leanprover.lean4`).
4. When opening any `.lean` file (e.g., `lean/Week01_ClassicalLogic.lean`), the extension will automatically connect to your `elan` toolchain, providing interactive proof states, syntax highlighting, and inline diagnostic messages.

---

### 5. Verifying Your Lean 4 Installation

Run the following commands in your terminal:
```bash
# Check elan version
elan --version

# Check Lean 4 compiler version
lean --version
# Expected output: Lean (version 4.x.x, ...)

# Check Lake (Lean build tool and package manager)
lake --version
```

To type-check any file from this study repository:
```bash
lean lean/Week01_ClassicalLogic.lean
lean lean/Week04_TypeTheory.lean
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
