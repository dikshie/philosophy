#!/usr/bin/env python3
"""
Week 07: Epistemic Logic & Gettier Problem with Z3 SMT Solver
Focus: Formalizing JTB, SMT Countermodel Generation, and the No-False-Lemma Condition
"""

import z3


def z3_gettier_countermodel():
    print("--- 1. Z3 SMT Analysis of the Gettier Counterexample ---")
    Agent = z3.DeclareSort("Agent")
    Proposition = z3.DeclareSort("Proposition")

    Believes = z3.Function("Believes", Agent, Proposition, z3.BoolSort())
    IsTrue = z3.Function("IsTrue", Proposition, z3.BoolSort())
    Justified = z3.Function("Justified", Agent, Proposition, z3.BoolSort())
    ReliesOnFalseLemma = z3.Function("ReliesOnFalseLemma", Agent, Proposition, z3.BoolSort())

    # Classical Definition: Knowledge ↔ Believed ∧ True ∧ Justified
    def JTB(a, p):
        return z3.And(Believes(a, p), IsTrue(p), Justified(a, p))

    # Anti-luck condition (Armstrong / Harman No-False-Lemma):
    def NFL_Knowledge(a, p):
        return z3.And(JTB(a, p), z3.Not(ReliesOnFalseLemma(a, p)))

    smith = z3.Const("Smith", Agent)
    target_prop = z3.Const("TargetProp", Proposition)  # "The man who gets the job has 10 coins in his pocket"

    solver = z3.Solver()
    # 1. Smith believes target_prop
    solver.add(Believes(smith, target_prop) == True)
    # 2. target_prop is objectively TRUE
    solver.add(IsTrue(target_prop) == True)
    # 3. Smith is epistemicly justified in believing target_prop
    solver.add(Justified(smith, target_prop) == True)
    # 4. BUT Smith's justification was derived via a false premise ("Jones gets the job")
    solver.add(ReliesOnFalseLemma(smith, target_prop) == True)

    print("Gettier Setup:")
    print("  - Believes(Smith, P) = True")
    print("  - IsTrue(P) = True")
    print("  - Justified(Smith, P) = True")
    print("  - ReliesOnFalseLemma(Smith, P) = True")

    if solver.check() == z3.sat:
        m = solver.model()
        print("\nSMT Model Evaluation:")
        val_jtb = m.eval(JTB(smith, target_prop))
        val_nfl = m.eval(NFL_Knowledge(smith, target_prop))
        print(f"  -> Classical JTB Satisfied?   : {val_jtb}")
        print(f"  -> No-False-Lemma Satisfied?  : {val_nfl}")
        print("  => CONCLUSION: A model exists where JTB is satisfied but knowledge fails due to false lemma dependency!")
    print()


def z3_prove_epistemic_veridicality():
    print("--- 2. Epistemic Veridicality (Axiom T) Prover ---")
    PropSort = z3.DeclareSort("PropSort")
    K = z3.Function("K", PropSort, z3.BoolSort())
    Truth = z3.Function("Truth", PropSort, z3.BoolSort())

    p = z3.Const("p", PropSort)
    solver = z3.Solver()

    # Axiom T of Epistemic Logic: K(p) → Truth(p) ("One cannot know what is false")
    axiom_T = z3.ForAll([p], z3.Implies(K(p), Truth(p)))

    solver.add(axiom_T)
    # Question: Can an agent know a false proposition? (K(p) ∧ ¬Truth(p))
    solver.push()
    test_p = z3.Const("test_p", PropSort)
    solver.add(K(test_p) == True)
    solver.add(Truth(test_p) == False)
    res = solver.check()
    print(f"Can an agent know a falsehood under Axiom T? {'NO (UNSAT - Epistemic Veridicality Preserved)' if res == z3.unsat else 'YES'}")
    solver.pop()


if __name__ == "__main__":
    print("=== Week 07: Epistemic Logic & The Gettier Problem (Z3 SMT) ===\n")
    z3_gettier_countermodel()
    z3_prove_epistemic_veridicality()
