/-
  Week 05: Gödel Incompleteness & Formal Theories in Lean 4
  Focus: Formal Theories, Provability Predicate, Consistency, and Independence
-/

namespace Week05

-- Sentence and Theory representations
def Sentence := Nat

structure FormalTheory where
  Provable : Sentence → Prop
  Negation : Sentence → Sentence
  Falsum   : Sentence

-- Consistency: The theory cannot prove both φ and ¬φ, nor can it prove Falsum
def Consistent (T : FormalTheory) : Prop :=
  ¬(T.Provable T.Falsum)

-- Soundness with respect to an evaluation / model
def Sound (T : FormalTheory) (IsTrue : Sentence → Prop) : Prop :=
  ∀ s, T.Provable s → IsTrue s

-- Gödel Sentence G: G asserts its own unprovability: IsTrue(G) ↔ ¬Provable(G)
structure GodelSentence (T : FormalTheory) (IsTrue : Sentence → Prop) where
  G : Sentence
  fixed_point : IsTrue G ↔ ¬(T.Provable G)

-- Theorem: If T is sound with respect to truth, then G cannot be provable in T
theorem godel_sentence_unprovable (T : FormalTheory) (IsTrue : Sentence → Prop)
    (h_sound : Sound T IsTrue) (gs : GodelSentence T IsTrue) :
    ¬(T.Provable gs.G) := by
  intro h_prov
  have h_true := h_sound gs.G h_prov
  have h_not_prov := gs.fixed_point.mp h_true
  exact h_not_prov h_prov

-- Corollary: If G is unprovable in T, then G is true!
theorem godel_sentence_is_true (T : FormalTheory) (IsTrue : Sentence → Prop)
    (h_sound : Sound T IsTrue) (gs : GodelSentence T IsTrue) :
    IsTrue gs.G := by
  have h_unprov := godel_sentence_unprovable T IsTrue h_sound gs
  exact gs.fixed_point.mpr h_unprov

end Week05
