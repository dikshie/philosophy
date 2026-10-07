/-
  Week 13: Formal Ontology & Mereology in Lean 4
  Focus: Quinean Ontological Commitment, Classical Extensional Mereology (CEM)
-/

namespace Week13

variable (U : Type)

-- 1. Quine's Ontological Commitment:
-- Theory T is committed to F iff T entails ∃ x, F x
def OntologicallyCommittedTo (Theory : Prop) (Property : U → Prop) : Prop :=
  Theory → ∃ x, Property x

-- 2. Classical Extensional Mereology (CEM)
structure MereologicalSystem where
  -- Binary relation: Part(x, y) means "x is a part of y"
  part : U → U → Prop
  -- Axiom 1: Reflexivity of Parthood
  part_refl : ∀ x, part x x
  -- Axiom 2: Antisymmetry of Parthood
  part_antisymm : ∀ x y, part x y → part y x → x = y
  -- Axiom 3: Transitivity of Parthood
  part_trans : ∀ x y z, part x y → part y z → part x z

-- Derived relations in Mereology
def ProperPart (M : MereologicalSystem U) (x y : U) : Prop :=
  M.part x y ∧ x ≠ y

def Overlap (M : MereologicalSystem U) (x y : U) : Prop :=
  ∃ z, M.part z x ∧ M.part z y

def Disjoint (M : MereologicalSystem U) (x y : U) : Prop :=
  ¬(Overlap U M x y)

-- Theorem: Every entity overlaps with itself
theorem overlap_refl (M : MereologicalSystem U) (x : U) : Overlap U M x x := by
  use x
  exact ⟨M.part_refl x, M.part_refl x⟩

-- Theorem: Overlap is symmetric
theorem overlap_symm (M : MereologicalSystem U) (x y : U) (h : Overlap U M x y) :
    Overlap U M y x := by
  rcases h with ⟨z, hzx, hzy⟩
  use z
  exact ⟨hzy, hzx⟩

end Week13
