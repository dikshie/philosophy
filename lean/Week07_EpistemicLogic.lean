/-
  Week 07: Epistemic Logic & The Gettier Problem in Lean 4
  Focus: Justified True Belief (JTB), Gettier Counterexamples, Epistemic Luck
-/

namespace Week07

variable (Agent : Type) (PropType : Type)

-- Definition of JTB conditions
structure JTB (a : Agent) (p : PropType) where
  believes : Prop
  is_true : Prop
  justified : Prop

-- The Classical Definition: Knowledge = JTB
def ClassicalKnowledge (a : Agent) (p : PropType) (jtb : JTB Agent PropType a p) : Prop :=
  jtb.believes ∧ jtb.is_true ∧ jtb.justified

-- A Gettier scenario: Belief based on a justified false lemma
structure GettierScenario where
  agent : Agent
  false_lemma : PropType
  target_prop : PropType
  -- The lemma is false
  lemma_is_false : Prop
  -- Agent is justified in believing the false lemma
  justified_in_lemma : Prop
  -- The target proposition is deductively inferred from the lemma
  deductive_inference : Prop
  -- The target proposition is accidentally true via independent circumstances
  target_is_true : Prop
  -- Epistemic defect: True belief was attained via a false step
  luck_dependent : Prop

-- Theorem: A Gettier agent satisfies the formal conditions of JTB
def gettier_satisfies_jtb (gs : GettierScenario Agent PropType) :
    JTB Agent PropType gs.agent gs.target_prop := {
  believes := gs.deductive_inference,
  is_true := gs.target_is_true,
  justified := gs.justified_in_lemma ∧ gs.deductive_inference
}

-- The anti-luck / No-False-Lemma epistemic condition (Armstrong / Harman)
def NoFalseLemmaKnowledge (a : Agent) (p : PropType) (jtb : JTB Agent PropType a p)
    (relies_on_false_lemma : Prop) : Prop :=
  ClassicalKnowledge Agent PropType a p jtb ∧ ¬relies_on_false_lemma

end Week07
