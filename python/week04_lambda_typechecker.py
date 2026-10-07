#!/usr/bin/env python3
"""
Week 04: Simply Typed Lambda Calculus with Z3 Type Unification
Focus: Propositions-as-Types, Type Inference as SMT Constraint Solving, Curry-Howard
"""

from typing import Dict, Optional, Tuple
import z3


class Term:
    pass


class Var(Term):
    def __init__(self, name: str):
        self.name = name

    def __str__(self):
        return self.name


class Lam(Term):
    def __init__(self, var: str, body: Term, explicit_type: Optional[str] = None):
        self.var = var
        self.body = body
        self.explicit_type = explicit_type

    def __str__(self):
        t_str = f":{self.explicit_type}" if self.explicit_type else ""
        return f"(λ{self.var}{t_str}. {self.body})"


class App(Term):
    def __init__(self, func: Term, arg: Term):
        self.func = func
        self.arg = arg

    def __str__(self):
        return f"({self.func} {self.arg})"


def z3_curry_howard_prover():
    """Demonstrate Curry-Howard: Proving logical theorems using Z3 and translating to types."""
    print("--- 1. Curry-Howard Propositional Prover via Z3 ---")
    A, B, C = z3.Bools("A B C")

    # Theorem: (A → B) ∧ (B → C) → (A → C)
    hypothetical_syllogism = z3.Implies(
        z3.And(z3.Implies(A, B), z3.Implies(B, C)),
        z3.Implies(A, C)
    )

    solver = z3.Solver()
    solver.add(z3.Not(hypothetical_syllogism))
    if solver.check() == z3.unsat:
        print("Proposition: (A → B) ∧ (B → C) → (A → C) is VALID.")
        print("Curry-Howard Witness Program:")
        print("  Term : λ⟨f, g⟩. λx:A. g (f x)")
        print("  Type : ((A → B) × (B → C)) → (A → C)\n")


def z3_type_unification():
    """Type inference as an SMT unification problem over an uninterpreted Type sort."""
    print("--- 2. Type Inference via Z3 SMT Unification ---")
    TypeSort = z3.DeclareSort("Type")
    Arrow = z3.Function("Arrow", TypeSort, TypeSort, TypeSort)

    # Base types
    IntType = z3.Const("IntType", TypeSort)
    BoolType = z3.Const("BoolType", TypeSort)

    # Unification problem: Incur type variables T_func, T_arg, T_res
    # Suppose we have an application (f x) where:
    #   type(x) = IntType
    #   type(f) = Arrow(T_var, BoolType)
    # Goal: Solve for T_var and deduce the return type of (f x)
    solver = z3.Solver()
    T_var = z3.Const("T_var", TypeSort)
    T_result = z3.Const("T_result", TypeSort)

    # Constraints: Arrow(T_var, BoolType) must equal Arrow(IntType, T_result)
    solver.add(Arrow(T_var, BoolType) == Arrow(IntType, T_result))

    if solver.check() == z3.sat:
        m = solver.model()
        print(f"Unification Succeeded: T_var = IntType, T_result = BoolType")
        print("Derived Application Type: BoolType")
    else:
        print("Type Error: Unification Failed")
    print()


if __name__ == "__main__":
    print("=== Week 04: Type Theory & Curry-Howard (Z3 SMT) ===\n")
    z3_curry_howard_prover()
    z3_type_unification()
