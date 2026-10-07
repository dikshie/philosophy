# Formal Logic Foundations: Weeks 01 to 13
*Comprehensive Mathematical and Formal Specifications for Philosophy, Physics, and Computer Science*

---

## Table of Contents
1. [Week 01: Classical Propositional & First-Order Predicate Logic](#week-01-classical-logic)
2. [Week 02: Modal Logic & Kripke Possible Worlds Semantics](#week-02-modal-logic)
3. [Week 03: Formal Computability, Turing Reductions & Rice's Theorem](#week-03-computability)
4. [Week 04: Type Theory, Intuitionistic Logic & Curry-Howard Isomorphism](#week-04-type-theory)
5. [Week 05: Gödel Incompleteness, Arithmetization & Metamathematics](#week-05-incompleteness)
6. [Week 06: Semantic Information & Thermodynamics of Computation](#week-06-semantic-information)
7. [Week 07: Epistemic Logic & Formalization of the Gettier Problem](#week-07-epistemic-logic)
8. [Week 08: Bayesian Confirmation Theory & The Problem of Induction](#week-08-bayesian-epistemology)
9. [Week 09: Demarcation, Falsification & The Duhem-Quine Thesis](#week-09-scientific-method)
10. [Week 10: Scientific Realism & Model-Theoretic Empirical Adequacy](#week-10-scientific-realism)
11. [Week 11: Inter-Theoretic Reduction & Structural Bridge Laws](#week-11-theory-reduction)
12. [Week 12: Formal Epistemic Synthesis](#week-12-formal-synthesis)
13. [Week 13: Formal Ontology, Quinean Quantification & Mereology](#week-13-formal-ontology)

---

<a name="week-01-classical-logic"></a>
## Week 01: Classical Propositional & First-Order Predicate Logic

### 1.1 Propositional Syntax and Semantics
- **Alphabet**: Countable set of atomic propositions $\mathcal{P} = \{p_1, p_2, \dots\}$, connectives $\{\neg, \wedge, \vee, \to, \leftrightarrow\}$, parentheses $\{ (, ) \}$.
- **Formation Rules**:
  $$\phi ::= p \mid \neg \phi \mid (\phi \wedge \psi) \mid (\phi \vee \psi) \mid (\phi \to \psi) \mid (\phi \leftrightarrow \psi)$$
- **Valuation Function**: $v : \mathcal{P} \to \{0, 1\}$.
- **Truth Conditions**:
  - $v(\neg \phi) = 1 - v(\phi)$
  - $v(\phi \wedge \psi) = \min(v(\phi), v(\psi))$
  - $v(\phi \vee \psi) = \max(v(\phi), v(\psi))$
  - $v(\phi \to \psi) = \max(1 - v(\phi), v(\psi))$
  - $v(\phi \leftrightarrow \psi) = 1$ if $v(\phi) = v(\psi)$ else $0$

### 1.2 First-Order Logic (FOL) with Identity
- **Signature**: $\mathcal{L} = \langle \mathcal{C}, \mathcal{F}, \mathcal{R} \rangle$ where $\mathcal{C}$ are constant symbols, $\mathcal{F}$ are function symbols with arity $n$, and $\mathcal{R}$ are relation symbols with arity $m$.
- **Structure**: $\mathfrak{M} = \langle \mathcal{D}, \mathcal{I} \rangle$ where $\mathcal{D} \neq \emptyset$ is the domain of discourse, and interpretation function $\mathcal{I}$ assigns:
  - For $c \in \mathcal{C}$: $c^\mathfrak{M} \in \mathcal{D}$
  - For $f \in \mathcal{F}$ of arity $n$: $f^\mathfrak{M} : \mathcal{D}^n \to \mathcal{D}$
  - For $R \in \mathcal{R}$ of arity $m$: $R^\mathfrak{M} \subseteq \mathcal{D}^m$
- **Variable Assignment**: $g : \mathcal{V} \to \mathcal{D}$.
- **Quantifier Semantics**:
  - $\mathfrak{M}, g \models \forall x \, \phi \iff \text{for all } d \in \mathcal{D}, \mathfrak{M}, g[x \mapsto d] \models \phi$
  - $\mathfrak{M}, g \models \exists x \, \phi \iff \text{there exists } d \in \mathcal{D}, \mathfrak{M}, g[x \mapsto d] \models \phi$

### 1.3 Metalogical Metatheorems
1. **Soundness**: $\Gamma \vdash \phi \implies \Gamma \models \phi$
2. **Gödel's Completeness Theorem (1929)**: $\Gamma \models \phi \implies \Gamma \vdash \phi$
3. **Compactness Theorem**: $\Gamma \models \phi \iff \exists \Gamma_0 \subseteq_{\text{fin}} \Gamma \text{ s.t. } \Gamma_0 \models \phi$
4. **Löwenheim-Skolem Theorem**: If a first-order theory has an infinite model, it has models of every infinite cardinality.

---

<a name="week-02-modal-logic"></a>
## Week 02: Modal Logic & Kripke Possible Worlds Semantics

### 2.1 Kripke Frames and Models
- **Kripke Frame**: $\mathcal{F} = \langle W, R \rangle$, where:
  - $W \neq \emptyset$ is the set of possible worlds (states).
  - $R \subseteq W \times W$ is the binary accessibility relation.
- **Kripke Model**: $\mathcal{M} = \langle W, R, V \rangle$, where valuation $V : \mathcal{P} \to \mathcal{P}(W)$.

### 2.2 Modal Satisfaction
For world $w \in W$:
$$\mathcal{M}, w \models p \iff w \in V(p)$$
$$\mathcal{M}, w \models \Box \phi \iff \forall u \in W \, (w R u \implies \mathcal{M}, u \models \phi)$$
$$\mathcal{M}, w \models \Diamond \phi \iff \exists u \in W \, (w R u \wedge \mathcal{M}, u \models \phi)$$

Dual equivalence: $\Diamond \phi \equiv \neg \Box \neg \phi$.

### 2.3 Modal Axiom Systems & Frame Correspondence
| System | Axioms | Relational Property of $R$ | First-Order Condition |
| :--- | :--- | :--- | :--- |
| **K** | $\Box(\phi \to \psi) \to (\Box \phi \to \Box \psi)$ | Any relation | None |
| **T** | System K + $\Box \phi \to \phi$ (Axiom M) | Reflexive | $\forall x \, (x R x)$ |
| **D** | System K + $\Box \phi \to \Diamond \phi$ | Serial | $\forall x \exists y \, (x R y)$ |
| **B** | System T + $\phi \to \Box \Diamond \phi$ (Axiom B) | Symmetric | $\forall x, y \, (x R y \to y R x)$ |
| **S4** | System T + $\Box \phi \to \Box \Box \phi$ (Axiom 4) | Reflexive + Transitive | Preorder: $x R x \wedge (x R y \wedge y R z \to x R z)$ |
| **S5** | System S4 + $\Diamond \phi \to \Box \Diamond \phi$ (Axiom 5) | Equivalence Relation | Reflexive, Symmetric, and Transitive |

---

<a name="week-03-computability"></a>
## Week 03: Formal Computability, Turing Reductions & Rice's Theorem

### 3.1 Formal Turing Machine Definition
A deterministic 1-tape Turing Machine is a 7-tuple:
$$M = \langle Q, \Sigma, \Gamma, \delta, q_0, q_{acc}, q_{rej} \rangle$$
- $Q$: Finite set of states.
- $\Sigma$: Input alphabet (blank symbol $\sqcup \notin \Sigma$).
- $\Gamma$: Tape alphabet ($\Sigma \cup \{\sqcup\} \subseteq \Gamma$).
- $\delta : (Q \setminus \{q_{acc}, q_{rej}\}) \times \Gamma \to Q \times \Gamma \times \{L, R\}$: Transition function.
- $q_0 \in Q$: Start state.
- $q_{acc}, q_{rej} \in Q$: Halting states ($q_{acc} \neq q_{rej}$).

### 3.2 The Halting Problem & Undecidability
Let language $A_{TM} = \{ \langle M, w \rangle \mid M \text{ is a TM and } M \text{ accepts } w \}$.
- **Theorem**: $A_{TM}$ is undecidable.
- **Proof by Diagonalization**:
  Assume decider $H(\langle M, w \rangle)$ exists. Construct $D$:
  $$D(\langle M \rangle) = \begin{cases} \text{reject} & \text{if } H(\langle M, \langle M \rangle \rangle) \text{ accepts} \\ \text{accept} & \text{if } H(\langle M, \langle M \rangle \rangle) \text{ rejects} \end{cases}$$
  Evaluating $D(\langle D \rangle)$ yields contradiction: $D(\langle D \rangle) \text{ accepts} \iff D(\langle D \rangle) \text{ rejects}$. $\blacksquare$

### 3.3 Rice's Theorem
Let $\mathcal{P}$ be any non-trivial semantic property of Turing-recognizable languages (i.e. $\exists L_1, L_2$ s.t. $L_1 \in \mathcal{P}$ and $L_2 \notin \mathcal{P}$).
Then $L_\mathcal{P} = \{ \langle M \rangle \mid L(M) \in \mathcal{P} \}$ is undecidable.

---

<a name="week-04-type-theory"></a>
## Week 04: Type Theory, Intuitionistic Logic & Curry-Howard Isomorphism

### 4.1 Simply Typed Lambda Calculus ($\lambda^\to$)
- **Types**: $\tau ::= B \mid \tau_1 \to \tau_2$ (where $B$ is a base type).
- **Terms**: $e ::= x \mid \lambda x : \tau . \, e \mid e_1 \, e_2$.
- **Typing Judgements**: Context $\Gamma = \{ x_1 : \tau_1, \dots, x_n : \tau_n \}$.
  $$\frac{x : \tau \in \Gamma}{\Gamma \vdash x : \tau} \quad (\text{Var})$$
  $$\frac{\Gamma, x : \tau_1 \vdash e : \tau_2}{\Gamma \vdash (\lambda x : \tau_1 . \, e) : \tau_1 \to \tau_2} \quad (\to\text{-Intro})$$
  $$\frac{\Gamma \vdash e_1 : \tau_1 \to \tau_2 \quad \Gamma \vdash e_2 : \tau_1}{\Gamma \vdash e_1 \, e_2 : \tau_2} \quad (\to\text{-Elim / Modus Ponens})$$

### 4.2 The Curry-Howard-Lambek Isomorphism
| Intuitionistic Logic | Type Theory ($\lambda$-Calculus) | Category Theory |
| :--- | :--- | :--- |
| Proposition $\phi$ | Type $\tau$ | Object $A$ |
| Proof of $\phi$ | Term / Program $e : \tau$ | Morphism $f : 1 \to A$ |
| Implication $\phi \to \psi$ | Function Type $\tau_1 \to \tau_2$ | Exponential Object $B^A$ |
| Conjunction $\phi \wedge \psi$ | Product Type $\tau_1 \times \tau_2$ | Categorical Product $A \times B$ |
| Disjunction $\phi \vee \psi$ | Sum / Either Type $\tau_1 + \tau_2$ | Coproduct $A \amalg B$ |
| True $\top$ | Unit Type `()` | Terminal Object $1$ |
| False $\bot$ | Empty / Void Type | Initial Object $0$ |

### 4.3 Constructive vs Classical Principles
In intuitionistic logic, the following classical axioms are **not** derivable:
1. Law of Excluded Middle (LEM): $\forall P, P \vee \neg P$.
2. Double Negation Elimination (DNE): $\forall P, \neg \neg P \to P$.
3. Peirce's Law: $\forall P Q, ((P \to Q) \to P) \to P$.

---

<a name="week-05-incompleteness"></a>
## Week 05: Gödel Incompleteness, Arithmetization & Metamathematics

### 5.1 Gödel Numbering (Arithmetization)
An injective effective encoding $\ulcorner \cdot \urcorner : \text{Formulas} \to \mathbb{N}$:
$$\ulcorner x_i \urcorner = 2^i, \quad \ulcorner \phi \wedge \psi \urcorner = 2^3 \cdot 3^{\ulcorner \phi \urcorner} \cdot 5^{\ulcorner \psi \urcorner}, \dots$$

### 5.2 The Diagonalization Lemma (Carnap / Gödel)
For any theory $T$ containing Robinson arithmetic $\mathcal{Q}$, and any formula $\psi(x)$ with one free variable, there exists a sentence $\phi$ such that:
$$T \vdash \phi \leftrightarrow \psi(\ulcorner \phi \urcorner)$$

### 5.3 Gödel's Incompleteness Theorems
1. **First Incompleteness Theorem**: Let $T$ be a recursively axiomatizable, consistent theory containing Robinson arithmetic $\mathcal{Q}$. Let $\text{Prov}_T(x)$ be the provability predicate. Applying Diagonalization to $\neg \text{Prov}_T(x)$ yields sentence $G$:
   $$T \vdash G \leftrightarrow \neg \text{Prov}_T(\ulcorner G \urcorner)$$
   - If $T$ is consistent: $T \nvdash G$.
   - If $T$ is $\omega$-consistent: $T \nvdash \neg G$.
   Thus $G$ is independent of $T$, yet true in the standard model $\mathbb{N}$.
2. **Second Incompleteness Theorem**: Let $\text{Con}(T) \equiv \neg \text{Prov}_T(\ulcorner \bot \urcorner)$.
   $$T \nvdash \text{Con}(T)$$

---

<a name="week-06-semantic-information"></a>
## Week 06: Semantic Information & Thermodynamics of Computation

### 6.1 Shannon Entropy vs Semantic Information
- **Shannon Information**: $H(X) = -\sum_{i=1}^n P(x_i) \log_2 P(x_i)$. Measures purely syntactic statistical surprisal; indifferent to truth or semantic reference.
- **Floridi's Theory of Strongly Semantic Information (TSSI)**:
  An information structure $\sigma$ constitutes semantic information iff:
  1. $\sigma$ consists of well-formed and meaningful data $D$.
  2. $\sigma$ is **veridical**: $\text{TruthValue}(\sigma) = 1$.
  Therefore, misinformation and disinformation are pseudo-information, not semantic information.

### 6.2 The Physical Nature of Information: Landauer's Principle
For any logically irreversible operation (such as erasing 1 bit of information):
$$\Delta S_{\text{environment}} \ge k_B \ln 2 \implies \Delta Q \ge k_B T \ln 2$$
Where $k_B$ is the Boltzmann constant and $T$ is absolute temperature in Kelvin.

---

<a name="week-07-epistemic-logic"></a>
## Week 07: Epistemic Logic & Formalization of the Gettier Problem

### 7.1 Epistemic Logic Framework (Hintikka S4 / S5)
- Operator $K_a \phi$: Agent $a$ knows proposition $\phi$.
- Operator $B_a \phi$: Agent $a$ believes proposition $\phi$.
- **Axioms**:
  - **Truth Axiom (Veridicality)**: $K_a \phi \to \phi$ (Axiom T).
  - **Positive Introspection (KK Thesis)**: $K_a \phi \to K_a K_a \phi$ (Axiom 4).
  - **Negative Introspection**: $\neg K_a \phi \to K_a \neg K_a \phi$ (Axiom 5).

### 7.2 The Tripartite Analysis of Knowledge (JTB)
$$\text{Knowledge}(a, \phi) \iff B_a \phi \wedge \phi \wedge J(a, \phi)$$
Where $J(a, \phi)$ is epistemic justification.

### 7.3 Formal Gettier Counterexamples (1963)
Gettier proved that $\text{JTB} \not\implies \text{Knowledge}$ by showing cases where:
1. $J(a, p)$ holds for a false proposition $p$ ($v(p) = 0$).
2. Agent $a$ deductively infers $q = p \vee r$ via valid disjunction introduction:
   $$\frac{p}{p \vee r}$$
3. Therefore $J(a, q)$ and $B_a q$ hold.
4. Coincidentally, unknown to agent $a$, $r$ happens to be true ($v(r) = 1$), making $q$ true ($v(q) = 1$).
5. Thus $B_a q \wedge q \wedge J(a, q)$ is satisfied, but $a$ does not *know* $q$ because the true belief was epistemic luck.

---

<a name="week-08-bayesian-epistemology"></a>
## Week 08: Bayesian Confirmation Theory & The Problem of Induction

### 8.1 Kolmogorov Probability Axioms
1. For any event $A \subseteq \Omega$: $P(A) \ge 0$.
2. $P(\Omega) = 1$.
3. For mutually exclusive events $A, B$ ($A \cap B = \emptyset$): $P(A \cup B) = P(A) + P(B)$.

### 8.2 Conditional Probability & Bayes' Theorem
$$P(A \mid B) = \frac{P(A \cap B)}{P(B)} \quad (P(B) > 0)$$
$$P(H \mid E) = \frac{P(E \mid H) \cdot P(H)}{P(E)} = \frac{P(E \mid H) \cdot P(H)}{P(E \mid H)P(H) + P(E \mid \neg H)P(\neg H)}$$

### 8.3 Confirmation Measures
Evidence $E$ incrementally confirms hypothesis $H$ iff:
$$c(H, E) = P(H \mid E) - P(H) > 0 \iff P(E \mid H) > P(E)$$

---

<a name="week-09-scientific-method"></a>
## Week 09: Demarcation, Falsification & The Duhem-Quine Thesis

### 9.1 Popperian Falsification Model
- **Demarcation Criterion**: Theory $T$ is scientific iff its class of potential falsifiers is non-empty:
  $$\text{Falsifiers}(T) = \{ e \in \text{BasicStatements} \mid T \cup \{e\} \vdash \bot \} \neq \emptyset$$
- **Modus Tollens Asymmetry**:
  $$\frac{T \to O \quad \neg O}{\neg T}$$

### 9.2 The Duhem-Quine Holism Challenge
In real physics experiments, a hypothesis $H$ never predicts observation $O$ in isolation; it requires auxiliary hypotheses $A_1, \dots, A_n$, initial conditions $C$, and instrumentation calibration $I$:
$$(H \wedge A_1 \wedge \dots \wedge A_n \wedge C \wedge I) \to O$$
Upon empirical anomaly $\neg O$:
$$\neg(H \wedge A_1 \wedge \dots \wedge A_n \wedge C \wedge I) \equiv \neg H \vee \neg A_1 \vee \dots \vee \neg A_n \vee \neg C \vee \neg I$$
Logic alone does not specify whether $H$ is false or an auxiliary assumption $A_k$ is defect.

---

<a name="week-10-scientific-realism"></a>
## Week 10: Scientific Realism & Model-Theoretic Empirical Adequacy

### 10.1 Scientific Realism vs Constructive Empiricism
- **Scientific Realism (Boyd, Psillos)**:
  1. *Metaphysical*: The physical world exists independent of our cognitive perception.
  2. *Semantic*: Theoretical terms (quarks, wavefunctions) refer to real entities.
  3. *Epistemic*: Accepted theories are approximately true.
  - *No-Miracles Argument*: Realism is the only philosophy that doesn't make the empirical success of science a miracle.

- **Constructive Empiricism (Bas van Fraassen)**:
  Science aims to give theories that are **empirically adequate**, not necessarily true.
  $$\text{Theory } T \text{ is empirically adequate} \iff \text{All observable phenomena } E \text{ embed isomorphically into an empirical submodel of } T:$$
  $$\exists \mathfrak{M} \models T \text{ and } \mathfrak{e} \in \text{Sub}_{\text{observable}}(\mathfrak{M}) \text{ s.t. } \mathfrak{e} \cong \mathcal{E}$$

---

<a name="week-11-theory-reduction"></a>
## Week 11: Inter-Theoretic Reduction & Structural Bridge Laws

### 11.1 Nagelian Reduction (Ernest Nagel, 1961)
Target theory $T_1$ (e.g. Thermodynamics) reduces to base theory $T_2$ (e.g. Statistical Mechanics) iff:
1. **Connectability**: For every predicate $P_1$ in $T_1$ not in $T_2$, there exists a bridge law $B$ linking $P_1$ to predicate $P_2$ in $T_2$:
   $$B \models \forall x \, (P_1(x) \leftrightarrow P_2(x))$$
   *(Example: Temperature $T = \frac{2}{3 k_B} \langle E_k \rangle$)*
2. **Derivability**: The laws of $T_1$ are logically deductible from $T_2 \cup B$:
   $$T_2 \cup B \vdash T_1$$

---

<a name="week-12-formal-synthesis"></a>
## Week 12: Formal Epistemic Synthesis

### 12.1 Unified Formal Proof Architecture
Formal science integrates three interlocking layers:
1. **Proof-Theoretic Layer (Type Theory)**: Constructive propositions-as-types ($\Gamma \vdash t : \tau$) guaranteeing computational decidability and operational definitions.
2. **Probabilistic Layer (Bayesian Inference)**: Consistent conditional belief networks over empirical evidence updates.
3. **Invariance Layer (Physical Symmetries)**: Coordinate-free tensor/gauge mappings under relativistic and gauge transformations ($SO(1,3), U(1) \times SU(2) \times SU(3)$).

---

<a name="week-13-formal-ontology"></a>
## Week 13: Formal Ontology, Quinean Quantification & Mereology

### 13.1 Quine's Criterion of Ontological Commitment
- "To be is to be the value of a bound variable."
- Theory $T$ is ontologically committed to entity type $F$ iff:
  $$T \models \exists x \, F(x)$$
  cannot be paraphrased away without loss of explanatory or predictive power.

### 13.2 Classical Extensional Mereology (CEM)
Let binary relation $P(x, y)$ denote "x is a part of y".

1. **Axioms of Parthood**:
   - **Reflexivity**: $\forall x \, P(x, x)$
   - **Antisymmetry**: $\forall x y \, (P(x, y) \wedge P(y, x) \to x = y)$
   - **Transitivity**: $\forall x y z \, (P(x, y) \wedge P(y, z) \to P(x, z))$

2. **Derived Mereological Relations**:
   - **Proper Parthood**: $PP(x, y) \equiv P(x, y) \wedge x \neq y$
   - **Overlap**: $O(x, y) \equiv \exists z \, (P(z, x) \wedge P(z, y))$
   - **Disjointness (Underlap)**: $D(x, y) \equiv \neg O(x, y)$

3. **Strong Supplementation Principle (SSP)**:
   $$\neg P(x, y) \implies \exists z \, (P(z, x) \wedge \neg O(z, y))$$

4. **Unrestricted Mereological Fusion (General Sum)**:
   For any non-empty property $\phi$:
   $$\exists x \, \phi(x) \implies \exists z \forall w \, (O(w, z) \leftrightarrow \exists v \, (\phi(v) \wedge O(w, v)))$$
