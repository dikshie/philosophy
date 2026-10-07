#!/usr/bin/env python3
"""
Week 09: Popperian Falsification & Duhem-Quine Holism with Z3 Unsat Cores
Focus: Modus Tollens Asymmetry, Auxiliary Hypotheses, and SMT Minimal Unsatisfiable Cores
"""

import z3


def z3_duhem_quine_unsat_core_diagnosis():
    print("--- 1. Duhem-Quine Diagnosis via Z3 Unsat Cores ---")
    # A scientific testing setup:
    # Core Theory T: Newtonian Gravitation
    # Auxiliaries:
    #   A1: Only 7 planets exist in the Solar System
    #   A2: Telescopes obey ray optics
    #   A3: Space is Euclidean
    # Prediction: Observation O (Uranus follows predicted orbit)

    T = z3.Bool("Core_Newtonian_Gravity")
    A1 = z3.Bool("Aux_Only_7_Planets")
    A2 = z3.Bool("Aux_Telescope_Optics")
    A3 = z3.Bool("Aux_Euclidean_Space")
    O = z3.Bool("Obs_Uranus_Orbit")

    solver = z3.Solver()

    # The deductive testing bundle: (T ∧ A1 ∧ A2 ∧ A3) → O
    bundle_law = z3.Implies(z3.And(T, A1, A2, A3), O)
    solver.add(bundle_law)

    # Empirical Observation ANOMALY: Uranus orbit deviates (¬O)
    solver.add(O == False)

    # We track which hypotheses are active using Z3 tracked assumptions
    assumptions = [T, A1, A2, A3]

    print("Testing active hypotheses under observation ¬O:")
    check_res = solver.check(assumptions)
    print(f"Joint consistency check: {check_res} (Anomaly detected!)")

    if check_res == z3.unsat:
        core = solver.unsat_core()
        print(f"Minimal Inconsistent Set (Unsat Core): {core}")
        print("=> Duhem-Quine Thesis in Action: Logic refutes the CONJUNCTION, not the Core Law alone!")

    # Duhem-Quine Revision Strategy:
    # Instead of discarding Core_Newtonian_Gravity, we reject Aux_Only_7_Planets (Postulate Neptune!)
    print("\nApplying Duhem-Quine Revision (Dropping A1: Only 7 planets):")
    revised_assumptions = [T, A2, A3]  # A1 is dropped
    revised_check = solver.check(revised_assumptions)
    print(f"Revised consistency check with Core Theory retained: {revised_check} (Consistent!)")
    if revised_check == z3.sat:
        print("=> The core theory is preserved; auxiliary modification leads to discovery of Neptune (1846).")
    print()


def z3_popperian_modus_tollens():
    print("--- 2. Popperian Modus Tollens Asymmetry Prover ---")
    Theory = z3.Bool("Theory")
    Observation = z3.Bool("Observation")

    solver = z3.Solver()
    # Modus Tollens: ((T → O) ∧ ¬O) → ¬T
    modus_tollens = z3.Implies(z3.And(z3.Implies(Theory, Observation), z3.Not(Observation)), z3.Not(Theory))
    solver.add(z3.Not(modus_tollens))
    res = solver.check()
    print(f"Popperian Modus Tollens is valid theorem: {'VALID (Proven)' if res == z3.unsat else 'INVALID'}\n")


if __name__ == "__main__":
    print("=== Week 09: Popperian Demarcation & Duhem-Quine Holism (Z3) ===\n")
    z3_duhem_quine_unsat_core_diagnosis()
    z3_popperian_modus_tollens()
