/-
  Week 08: Bayesian Epistemology & Confirmation in Lean 4
  Focus: Probability Spaces, Bayes' Rule, and Incremental Confirmation
-/

namespace Week08

structure ProbabilitySpace (Event : Type) where
  P : Event → Float
  non_negative : ∀ e, P e ≥ 0.0
  total_one    : ∀ top, P top = 1.0

-- Conditional Probability definition
def cond_prob {Event : Type} (ps : ProbabilitySpace Event) (inter : Event → Event → Event)
    (A B : Event) (h_pos : ps.P B > 0.0) : Float :=
  (ps.P (inter A B)) / (ps.P B)

-- Incremental Confirmation: Evidence E confirms Hypothesis H iff P(H|E) > P(H)
def confirms {Event : Type} (ps : ProbabilitySpace Event) (inter : Event → Event → Event)
    (H E : Event) (h_pos : ps.P E > 0.0) : Prop :=
  cond_prob ps inter H E h_pos > ps.P H

-- Disconfirmation: Evidence E disconfirms Hypothesis H iff P(H|E) < P(H)
def disconfirms {Event : Type} (ps : ProbabilitySpace Event) (inter : Event → Event → Event)
    (H E : Event) (h_pos : ps.P E > 0.0) : Prop :=
  cond_prob ps inter H E h_pos < ps.P H

-- Bayesian Likelihood Ratio (Bayes Factor)
def bayes_factor {Event : Type} (ps : ProbabilitySpace Event) (inter : Event → Event → Event)
    (H1 H2 E : Event) (hE1 : ps.P H1 > 0.0) (hE2 : ps.P H2 > 0.0) : Float :=
  let pEH1 := (ps.P (inter E H1)) / (ps.P H1)
  let pEH2 := (ps.P (inter E H2)) / (ps.P H2)
  pEH1 / pEH2

end Week08
