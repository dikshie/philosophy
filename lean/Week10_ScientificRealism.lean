/-
  Week 10: Scientific Realism & Empirical Adequacy in Lean 4
  Focus: Van Fraassen's Constructive Empiricism, Submodel Embeddings, Realism
-/

namespace Week10

variable (World : Type) (Observation : Type)

-- A theoretical model with internal states and observable projection
structure ScientificModel where
  State : Type
  TheoreticalEntities : State → Prop
  ObservedProjection  : State → Observation

-- Constructive Empiricism: Theory is empirically adequate if all actual observations
-- match some state's projection in the model
def EmpiricallyAdequate (M : ScientificModel Observation)
    (ActualPhenomena : Observation → Prop) : Prop :=
  ∀ obs, ActualPhenomena obs → ∃ s, M.ObservedProjection s = obs

-- Scientific Realism: Asserts not only empirical adequacy, but that the
-- theoretical entities posited by the model correspond to real physical reality
def ScientificRealistCommitment (M : ScientificModel Observation)
    (ActualPhenomena : Observation → Prop)
    (IsPhysicallyReal : M.State → Prop) : Prop :=
  EmpiricallyAdequate Observation M ActualPhenomena ∧
  (∀ s, M.TheoreticalEntities s → IsPhysicallyReal s)

-- Theorem: Empirical adequacy is strictly weaker than Scientific Realism
theorem realism_implies_adequacy (M : ScientificModel Observation)
    (ActualPhenomena : Observation → Prop)
    (IsPhysicallyReal : M.State → Prop)
    (h_real : ScientificRealistCommitment Observation M ActualPhenomena IsPhysicallyReal) :
    EmpiricallyAdequate Observation M ActualPhenomena :=
  h_real.1

end Week10
