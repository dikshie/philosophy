/-
  Week 03: Formal Computability & Halting Problem in Lean 4
  Focus: Abstract Machines, Decidability, Diagonalization, and Undecidability
-/

namespace Week03

-- Abstract program representation as natural numbers
def Program := Nat
def Input := Nat

-- Oracle / hypothetical decider for halting: Halts(p, i) means program p halts on input i
def Decider := Program → Input → Bool

-- If a total decider exists that correctly answers whether p halts on input i
def DecidesHalting (H : Decider) (Halts : Program → Input → Prop) : Prop :=
  ∀ (p : Program) (i : Input), H p i = true ↔ Halts p i

-- Diagonal construction: D takes program index p, runs H(p, p), and loops if H returns true, halts if H returns false
def DiagonalProgram (H : Decider) (Halts : Program → Input → Prop) (D : Program) : Prop :=
  ∀ (p : Program), Halts D p ↔ H p p = false

-- Theorem: No general halting decider can exist (Turing 1936)
theorem halting_problem_undecidable
    (Halts : Program → Input → Prop)
    (H : Decider)
    (h_decides : DecidesHalting H Halts)
    (D : Program)
    (h_diag : DiagonalProgram H Halts D) : False := by
  have h_d_on_d := h_diag D
  have h_dec_d := h_decides D D
  -- We now have: Halts D D ↔ H D D = false, and H D D = true ↔ Halts D D
  cases h_val : H D D with
  | true =>
    have h_halts : Halts D D := (h_dec_d.mp h_val)
    have h_not_halts : H D D = false := (h_d_on_d.mp h_halts)
    rw [h_val] at h_not_halts
    contradiction
  | false =>
    have h_halts : Halts D D := (h_d_on_d.mpr h_val)
    have h_true : H D D = true := (h_dec_d.mpr h_halts)
    rw [h_val] at h_true
    contradiction

end Week03
