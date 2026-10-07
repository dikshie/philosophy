#!/usr/bin/env python3
"""
Week 02: Modal Logic & Kripke Semantics with Z3 SMT Solver
Focus: First-Order Kripke Frame Encoding, S5/S4 Axiom Verification & Countermodels
"""

import z3


def prove_frame_correspondence_with_z3():
    print("--- 1. Proving Modal Axiom Correspondence with Z3 ---")
    World = z3.DeclareSort("World")
    R = z3.Function("R", World, World, z3.BoolSort())
    P = z3.Function("P", World, z3.BoolSort())

    w = z3.Const("w", World)
    v = z3.Const("v", World)
    u = z3.Const("u", World)

    # Modal definition: Box P at world w: ∀v (w R v → P(v))
    def Box_P(world):
        v_var = z3.Const("v_acc", World)
        return z3.ForAll([v_var], z3.Implies(R(world, v_var), P(v_var)))

    # Modal definition: Diamond P at world w: ∃v (w R v ∧ P(v))
    def Diamond_P(world):
        v_var = z3.Const("v_acc", World)
        return z3.Exists([v_var], z3.And(R(world, v_var), P(v_var)))

    # Theorem 1: If R is reflexive, Axiom T (Box P → P) holds universally
    solver = z3.Solver()
    reflexivity = z3.ForAll([w], R(w, w))
    axiom_T = z3.ForAll([w], z3.Implies(Box_P(w), P(w)))

    # Check if Reflexivity ⊢ Axiom T (i.e., Reflexivity ∧ ¬Axiom T is UNSAT)
    solver.push()
    solver.add(reflexivity)
    solver.add(z3.Not(axiom_T))
    res = solver.check()
    print(f"Checking Axiom T (Box P → P) on Reflexive Frame: {'VALID (Proven)' if res == z3.unsat else 'FAILED'}")
    solver.pop()

    # Theorem 2: If R is transitive, Axiom 4 (Box P → Box Box P) holds universally
    transitivity = z3.ForAll([w, v, u], z3.Implies(z3.And(R(w, v), R(v, u)), R(w, u)))
    box_box_P = lambda world: z3.ForAll([z3.Const("v1", World)], z3.Implies(R(world, z3.Const("v1", World)), Box_P(z3.Const("v1", World))))
    axiom_4 = z3.ForAll([w], z3.Implies(Box_P(w), box_box_P(w)))

    solver.push()
    solver.add(transitivity)
    solver.add(z3.Not(axiom_4))
    res = solver.check()
    print(f"Checking Axiom 4 (Box P → Box Box P) on Transitive Frame: {'VALID (Proven)' if res == z3.unsat else 'FAILED'}")
    solver.pop()

    # Countermodel: What happens to Axiom T if the frame is NOT reflexive?
    solver.push()
    # Serial but not reflexive
    solver.add(z3.ForAll([w], z3.Exists([v], R(w, v))))
    solver.add(z3.Not(axiom_T))
    res = solver.check()
    if res == z3.sat:
        print("Non-reflexive frame check: Countermodel found! Axiom T fails without reflexivity.")
    solver.pop()
    print()


def evaluate_finite_kripke_model():
    print("--- 2. Finite Kripke Model Checking ---")
    worlds = ["w0", "w1", "w2"]
    relations = {("w0", "w0"), ("w1", "w1"), ("w2", "w2"), ("w0", "w1"), ("w1", "w2"), ("w0", "w2")}
    val_P = {"w0": True, "w1": True, "w2": False}

    def box_p(w):
        acc = [v for (u, v) in relations if u == w]
        return all(val_P[v] for v in acc)

    def diamond_p(w):
        acc = [v for (u, v) in relations if u == w]
        return any(val_P[v] for v in acc)

    for w in worlds:
        print(f"World {w}: P={val_P[w]} | □P={box_p(w)} | ◇P={diamond_p(w)}")


if __name__ == "__main__":
    print("=== Week 02: Modal Logic & Kripke Semantics (Z3 SMT) ===\n")
    prove_frame_correspondence_with_z3()
    evaluate_finite_kripke_model()
