/-
  Week 06: Semantic Information & Computation in Lean 4
  Focus: Floridi's Theory of Strongly Semantic Information (TSSI), Veridicality
-/

namespace Week06

-- Data structure: Well-formed, meaningful datum
structure SemanticDatum where
  content : String
  isWellFormed : Bool
  isMeaningful : Bool

-- Strongly Semantic Information requires truth (Veridicality condition)
structure SemanticInformation where
  datum : SemanticDatum
  truthValue : Bool
  well_formed : datum.isWellFormed = true
  meaningful : datum.isMeaningful = true
  veridical : truthValue = true

-- Untrue data is misinformation or disinformation, not semantic information
def IsMisinformation (d : SemanticDatum) (truthValue : Bool) : Prop :=
  d.isWellFormed = true ∧ d.isMeaningful = true ∧ truthValue = false

theorem misinformation_is_not_semantic_info (d : SemanticDatum) (tv : Bool)
    (h_mis : IsMisinformation d tv) :
    ¬(∃ (info : SemanticInformation), info.datum = d ∧ info.truthValue = tv) := by
  intro ⟨info, hd, htv⟩
  have h_ver := info.veridical
  have h_false := h_mis.2.2
  rw [htv] at h_ver
  rw [h_ver] at h_false
  contradiction

-- Physical Landauer bound relation
structure LandauerBound where
  temperature : Float -- Kelvins (T > 0)
  kB : Float          -- Boltzmann constant
  entropy_change : Float
  erased_bits : Nat
  erasure_inequality : entropy_change ≥ (erased_bits.toFloat) * kB * 0.693147

end Week06
