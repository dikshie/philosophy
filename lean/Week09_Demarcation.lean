/-
  Week 09: Demarcation, Falsification & Duhem-Quine Holism in Lean 4
  Focus: Modus Tollens Asymmetry, Auxiliary Hypotheses, Underdetermination
-/

namespace Week09

variable (Theory Observation Auxiliary : Prop)

-- 1. Popperian Falsification via Modus Tollens
theorem popper_modus_tollens
    (h_predict : Theory → Observation)
    (h_not_obs : ¬Observation) :
    ¬Theory :=
  fun hT => h_not_obs (h_predict hT)

-- 2. Duhem-Quine Holism: Real tests involve auxiliary assumptions
theorem duhem_quine_holism
    (h_bundle_predict : (Theory ∧ Auxiliary) → Observation)
    (h_not_obs : ¬Observation) :
    ¬Theory ∨ ¬Auxiliary := by
  have h_not_bundle : ¬(Theory ∧ Auxiliary) :=
    fun ⟨hT, hA⟩ => h_not_obs (h_bundle_predict ⟨hT, hA⟩)
  -- Classically, ¬(T ∧ A) ↔ ¬T ∨ ¬A
  cases Classical.em Theory with
  | inl hT =>
    right
    intro hA
    exact h_not_bundle ⟨hT, hA⟩
  | inr hnT =>
    left
    exact hnT

-- Epistemic conclusion: Refutation of observation O cannot uniquely isolate Theory T as false
theorem cannot_isolate_refutation
    (h_bundle : (Theory ∧ Auxiliary) → Observation)
    (h_not_obs : ¬Observation)
    (h_save_theory : Theory) :
    ¬Auxiliary := by
  intro hA
  exact h_not_obs (h_bundle ⟨h_save_theory, hA⟩)

end Week09
