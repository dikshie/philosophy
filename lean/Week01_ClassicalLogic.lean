/-
  Week 01: Classical & Intuitionistic Propositional Logic in Lean 4
  Focus: Syntax, Natural Deduction, Proofs, and Classical Principles
-/

namespace Week01

-- 1. Constructive proofs using standard Lean 4 natural deduction
theorem modus_ponens {P Q : Prop} (h1 : P → Q) (h2 : P) : Q :=
  h1 h2

theorem and_commutativity {P Q : Prop} (h : P ∧ Q) : Q ∧ P :=
  ⟨h.right, h.left⟩

theorem or_commutativity {P Q : Prop} (h : P ∨ Q) : Q ∨ P :=
  h.elim (fun hp => Or.inr hp) (fun hq => Or.inl hq)

theorem hypothetical_syllogism {P Q R : Prop} (h1 : P → Q) (h2 : Q → R) : P → R :=
  fun hp => h2 (h1 hp)

-- 2. De Morgan's Laws (Constructive fragments)
theorem de_morgan_not_or {P Q : Prop} (h : ¬(P ∨ Q)) : ¬P ∧ ¬Q :=
  ⟨fun hp => h (Or.inl hp), fun hq => h (Or.inr hq)⟩

theorem de_morgan_or_not {P Q : Prop} (h : ¬P ∨ ¬Q) : ¬(P ∧ Q) :=
  fun ⟨hp, hq⟩ =>
    h.elim (fun hnp => hnp hp) (fun hnq => hnq hq)

-- 3. Triple Negation reduces to Single Negation constructively
theorem not_not_not_equiv_not {P : Prop} : ¬¬¬P ↔ ¬P := by
  constructor
  · intro hnnnp hp
    exact hnnnp (fun hnp => hnp hp)
  · intro hnp hnnp
    exact hnnp hnp

-- 4. Classical Principles (Requiring Classical Axioms)
open Classical

theorem double_negation_elimination {P : Prop} (h : ¬¬P) : P :=
  byContradiction (fun hnp => h hnp)

theorem law_of_excluded_middle (P : Prop) : P ∨ ¬P :=
  em P

theorem peirce_law {P Q : Prop} : ((P → Q) → P) → P := by
  intro h
  cases em P with
  | inl hp => exact hp
  | inr hnp =>
    have hpq : P → Q := fun hp => False.elim (hnp hp)
    exact h hpq

end Week01
