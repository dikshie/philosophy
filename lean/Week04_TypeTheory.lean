/-
  Week 04: Type Theory & Curry-Howard Isomorphism in Lean 4
  Focus: Propositions-as-Types, Proofs-as-Programs, Constructive Type Checking
-/

namespace Week04

-- The Curry-Howard Correspondence:
-- Every logical connective is represented by a type constructor.

-- 1. Implication is Function Type (A → B)
def modus_ponens_term {A B : Type} (f : A → B) (x : A) : B :=
  f x

-- 2. Conjunction is Product Type (A × B)
def and_intro_term {A B : Type} (x : A) (y : B) : A × B :=
  (x, y)

def and_elim_left {A B : Type} (p : A × B) : A :=
  p.1

def and_elim_right {A B : Type} (p : A × B) : B :=
  p.2

-- 3. Disjunction is Sum / Either Type (Sum A B)
def or_intro_left {A B : Type} (x : A) : Sum A B :=
  Sum.inl x

def or_intro_right {A B : Type} (y : B) : Sum A B :=
  Sum.inr y

def or_elim_term {A B C : Type} (s : Sum A B) (f : A → C) (g : B → C) : C :=
  match s with
  | Sum.inl x => f x
  | Sum.inr y => g y

-- 4. Negation is Function to Empty Type (A → Empty)
def Neg (A : Type) : Type := A → Empty

def non_contradiction_term {A : Type} : Neg (A × Neg A) :=
  fun ⟨x, not_x⟩ => not_x x

-- 5. Currying isomorphism: (A × B → C) ≃ (A → B → C)
def curry {A B C : Type} (f : A × B → C) : A → B → C :=
  fun a b => f (a, b)

def uncurry {A B C : Type} (f : A → B → C) : A × B → C :=
  fun ⟨a, b⟩ => f a b

-- 6. Constructive Double Negation Introduction
def double_neg_intro {A : Type} (x : A) : Neg (Neg A) :=
  fun not_a => not_a x

end Week04
