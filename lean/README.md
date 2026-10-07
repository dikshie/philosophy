# Lean 4 Formal Philosophy & Logic Suite

This directory contains formally verified, interactive theorem proving scripts written in **[Lean 4](https://lean-lang.org/)**, accompanying Weeks 01 through 13 of the 1-Year Philosophy Study Plan.

Every file encodes canonical philosophical arguments, logical systems, and foundational theorems into Lean 4's dependently typed kernel.

---

## Quick Navigation

- [1. Prerequisites & Installation](#1-prerequisites--installation)
- [2. How to Run & Verify Lean Scripts](#2-how-to-run--verify-lean-scripts)
  - [Option A: Command-Line Verification (Fastest)](#option-a-command-line-verification-fastest)
  - [Option B: Interactive Theorem Proving in VS Code (Recommended)](#option-b-interactive-theorem-proving-in-vs-code-recommended)
  - [Option C: Batch Verification Script](#option-c-batch-verification-script)
- [3. Module Inventory & Key Theorems](#3-module-inventory--key-theorems)
- [4. Troubleshooting & FAQ](#4-troubleshooting--faq)

---

## 1. Prerequisites & Installation

Lean 4 is managed using **`elan`** (the official version manager).

### Quick Install by OS

- **macOS**:
  ```bash
  brew install elan-init
  elan default stable
  ```
  *Or via shell:*
  ```bash
  curl -sSf https://raw.githubusercontent.com/leanprover/elan/master/elan-init.sh | sh -s -- -y
  source "$HOME/.elan/env"
  elan default stable
  ```

- **Linux (Ubuntu / Debian / Fedora / Arch)**:
  ```bash
  curl -sSf https://raw.githubusercontent.com/leanprover/elan/master/elan-init.sh | sh -s -- -y
  source "$HOME/.elan/env"
  elan default stable
  ```

- **FreeBSD**:
  ```bash
  sudo pkg install curl git bash gmake llvm
  curl -sSf https://raw.githubusercontent.com/leanprover/elan/master/elan-init.sh | bash -s -- -y
  echo 'export PATH="$HOME/.elan/bin:$PATH"' >> ~/.zshrc
  source ~/.zshrc
  elan default stable
  ```

- **Windows 11 (PowerShell)**:
  ```powershell
  Invoke-WebRequest -Uri "https://raw.githubusercontent.com/leanprover/elan/master/elan-init.ps1" -OutFile "elan-init.ps1"
  .\elan-init.ps1 -y
  Remove-Item .\elan-init.ps1
  elan default stable
  ```

### Verify Installation
```bash
elan --version
lean --version
```
Expected output: `Lean (version 4.x.x, ...)`

---

## 2. How to Run & Verify Lean Scripts

### Option A: Command-Line Verification (Fastest)

You can type-check and verify any Lean 4 script directly using the `lean` compiler.

Navigate to the repository root or the `lean/` directory:

```bash
cd /Users/dikshie/VIRTUAL/philosophy/lean
```

Verify a specific week:

```bash
# Week 01: Classical & Intuitionistic Logic
lean Week01_ClassicalLogic.lean

# Week 02: Modal Logic & Kripke Semantics
lean Week02_ModalLogic.lean

# Week 03: Halting Problem Undecidability
lean Week03_Computability.lean

# Week 04: Type Theory & Curry-Howard Isomorphism
lean Week04_TypeTheory.lean

# Week 13: Mereology & Quinean Ontology
lean Week13_OntologySubstance.lean
```

> **Note**: In Lean 4, if a command exits with code `0` and produces **no output**, it means **all theorems, types, and proofs are sound, type-checked, and completely verified** by Lean's kernel. If there is a logical flaw or type mismatch, Lean will print an error message indicating the exact line and failed goal.

---

### Option B: Interactive Theorem Proving in VS Code (Recommended)

To step through proofs interactively, inspect the proof state, and see goal hypotheses update in real time:

1. **Install Visual Studio Code**: Download from [code.visualstudio.com](https://code.visualstudio.com/).
2. **Install the Lean 4 Extension**:
   - In VS Code, press `Ctrl+Shift+X` (or `Cmd+Shift+X` on macOS).
   - Search for **`Lean 4`** (Extension ID: `leanprover.lean4`) and click **Install**.
3. **Open the Project Folder**:
   - Open `/Users/dikshie/VIRTUAL/philosophy` in VS Code (`File > Open Folder...`).
4. **Open Any `.lean` File**:
   - Open e.g., `lean/Week04_TypeTheory.lean` or `lean/Week01_ClassicalLogic.lean`.
5. **Open the Lean Infoview**:
   - Click the **∀** symbol in the top-right corner of the editor, or press `Ctrl+Shift+Enter` (`Cmd+Shift+Enter` on macOS).
   - Place your cursor inside any proof block (`by`, `intro`, `cases`, `constructor`) to see the live proof state, current hypotheses, and remaining goals.

```
┌─────────────────────────────────┐
│ Lean Infoview                   │
│ ------------------------------- │
│ 1 goal                          │
│ P Q : Prop                      │
│ h : P ∧ Q                       │
│ ⊢ Q ∧ P                         │
└─────────────────────────────────┘
```

---

### Option C: Batch Verification Script

To verify all 13 Lean files in a single command from your terminal:

#### Bash / Zsh (macOS / Linux / FreeBSD)
```bash
cd lean
for file in Week*.lean; do
  echo -n "Checking $file ... "
  lean "$file" && echo "[VERIFIED]" || echo "[FAILED]"
done
```

#### Windows PowerShell
```powershell
Set-Location lean
Get-ChildItem -Filter "Week*.lean" | ForEach-Object {
    Write-Host -NoNewline "Checking $($_.Name) ... "
    lean $_.Name
    if ($LASTEXITCODE -eq 0) { Write-Host "[VERIFIED]" -ForegroundColor Green }
    else { Write-Host "[FAILED]" -ForegroundColor Red }
}
```

---

## 3. Module Inventory & Key Theorems

| File | Philosophical Focus | Key Theorems & Formal Definitions |
| :--- | :--- | :--- |
| **[Week01_ClassicalLogic.lean](Week01_ClassicalLogic.lean)** | Classical & Intuitionistic Logic | Natural deduction (`modus_ponens`, `hypothetical_syllogism`), De Morgan laws, double negation elimination (`¬¬P → P`), and Peirce's law. |
| **[Week02_ModalLogic.lean](Week02_ModalLogic.lean)** | Modal Logic & Kripke Semantics | Frame correspondence theorems: Reflexivity $\models$ Axiom T (`Box P → P`), Transitivity $\models$ Axiom 4 (`Box P → Box Box P`). |
| **[Week03_Computability.lean](Week03_Computability.lean)** | Computability & Turing Limits | Abstract program deciders, diagonal program construction, and the formal proof of the **Halting Problem undecidability**. |
| **[Week04_TypeTheory.lean](Week04_TypeTheory.lean)** | Type Theory & Curry-Howard | Propositions-as-types, product types ($\wedge$), sum types ($\vee$), function types ($\to$), and constructive negation as $A \to \text{Empty}$. |
| **[Week05_Incompleteness.lean](Week05_Incompleteness.lean)** | Gödel Incompleteness | Formal theories, provability predicates, consistency, and the deductive independence of the Gödel sentence $G$. |
| **[Week06_Information.lean](Week06_Information.lean)** | Semantic Information | Floridi's Theory of Strongly Semantic Information (TSSI), veridicality condition, and physical Landauer erasure energy bounds. |
| **[Week07_EpistemicLogic.lean](Week07_EpistemicLogic.lean)** | Epistemic Logic & Gettier | Justified True Belief (JTB) specification, Gettier luck dependency, and Armstrong's No-False-Lemma epistemic condition. |
| **[Week08_BayesianEpistemology.lean](Week08_BayesianEpistemology.lean)** | Bayesian Epistemology | Probability spaces, conditional probability, incremental confirmation predicates ($P(H \mid E) > P(H)$), and Bayes factors. |
| **[Week09_Demarcation.lean](Week09_Demarcation.lean)** | Popper & Duhem-Quine | Popperian modus tollens falsification and the Duhem-Quine underdetermination theorem ($\neg(T \wedge A) \to \neg T \vee \neg A$). |
| **[Week10_ScientificRealism.lean](Week10_ScientificRealism.lean)** | Scientific Realism | van Fraassen's constructive empiricism, theoretical states, observable projections, and proof that empirical adequacy does not entail unobservable realism. |
| **[Week11_TheoryReduction.lean](Week11_TheoryReduction.lean)** | Theory Reduction | Micro/macro properties, Nagelian bridge laws ($B \models \forall x (P_1(x) \leftrightarrow P_2(x))$), and multiple realizability. |
| **[Week12_EpistemicSynthesis.lean](Week12_EpistemicSynthesis.lean)** | Epistemic Synthesis | Composite epistemic warrants combining constructive proof witnesses with probabilistic confidence thresholds. |
| **[Week13_OntologySubstance.lean](Week13_OntologySubstance.lean)** | Formal Ontology & Mereology | Quinean ontological commitment to bound variables ($\exists x Fx$) and Classical Extensional Mereology (CEM) axioms: parthood partial order, overlap symmetry, and proper parthood asymmetry. |

---

## 4. Troubleshooting & FAQ

### 1. `command not found: lean`
- Ensure that `~/.elan/bin` is in your shell `PATH`:
  ```bash
  export PATH="$HOME/.elan/bin:$PATH"
  ```
- Or run `source "$HOME/.elan/env"`.

### 2. `elan: default toolchain not set`
- Run:
  ```bash
  elan default stable
  ```
  This downloads and configures the latest stable Lean 4 compiler.

### 3. Lean output is blank
- In Lean 4, a silent exit with status code `0` indicates complete success. To verify verbosely, you can use interactive mode in VS Code to view proof states in the Infoview.
