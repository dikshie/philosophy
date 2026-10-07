#!/usr/bin/env python3
"""
Week 01: Propositional Logic Solver with SymPy and Z3
Focus: Formal Syntax, Truth Tables, CNF Conversion, and SMT Theorem Proving
"""

import sympy
from sympy.logic.boolalg import And as SymAnd, Or as SymOr, Not as SymNot, Implies as SymImplies, Equivalent as SymEquiv
from sympy.logic.boolalg import truth_table, to_cnf, simplify_logic
import z3


def analyze_with_sympy():
    print("--- 1. SymPy Propositional Analysis ---")
    P, Q, R = sympy.symbols("P Q R")

    # Modus Ponens: ((P → Q) ∧ P) → Q
    modus_ponens = SymImplies(SymAnd(SymImplies(P, Q), P), Q)
    print(f"Modus Ponens Formula : {modus_ponens}")
    print(f"Simplified Formula   : {simplify_logic(modus_ponens)} (Tautology)")
    print(f"Conjunctive Normal Form: {to_cnf(modus_ponens)}")

    # De Morgan's Law: ¬(P ∨ Q) ↔ (¬P ∧ ¬Q)
    de_morgan = SymEquiv(SymNot(SymOr(P, Q)), SymAnd(SymNot(P), SymNot(Q)))
    print(f"\nDe Morgan Formula   : {de_morgan}")
    print(f"Simplified Formula   : {simplify_logic(de_morgan)} (Tautology)")

    # Truth Table for (P → Q)
    imp_formula = SymImplies(P, Q)
    print(f"\nTruth Table for {imp_formula}:")
    table = truth_table(imp_formula, [P, Q])
    for row, result in table:
        p_val, q_val = [int(v) for v in row]
        print(f"  P={p_val}, Q={q_val} => Result={int(bool(result))}")
    print()


def prove_with_z3():
    print("--- 2. Z3 SMT Theorem Proving & SAT Solving ---")
    P = z3.Bool("P")
    Q = z3.Bool("Q")
    R = z3.Bool("R")

    solver = z3.Solver()

    # To prove a theorem φ is valid, we check if ¬φ is UNSAT
    # Theorem: Peirce's Law ((P → Q) → P) → P
    peirces_law = z3.Implies(z3.Implies(z3.Implies(P, Q), P), P)
    print(f"Proving Peirce's Law via Z3: ((P → Q) → P) → P")

    solver.push()
    solver.add(z3.Not(peirces_law))
    check_result = solver.check()
    if check_result == z3.unsat:
        print("  -> Negation is UNSAT. Peirce's Law is mathematically VALID (Theorem Proven).")
    else:
        print(f"  -> Countermodel found: {solver.model()}")
    solver.pop()

    # SAT Solving: Find satisfying model for (P ∨ Q) ∧ (¬P ∨ R) ∧ (¬Q ∨ R) ∧ ¬R
    print("\nSAT Solving with Z3:")
    clauses = z3.And(
        z3.Or(P, Q),
        z3.Or(z3.Not(P), R),
        z3.Or(z3.Not(Q), R)
    )
    solver.push()
    solver.add(clauses)
    if solver.check() == z3.sat:
        print(f"  Formula is Satisfiable with model: {solver.model()}")
    solver.pop()


if __name__ == "__main__":
    print("=== Week 01: Classical Propositional Logic (SymPy & Z3) ===\n")
    analyze_with_sympy()
    prove_with_z3()
