#!/usr/bin/env python3
"""
Week 04: Simply Typed Lambda Calculus & Curry-Howard Type Checker
Focus: Propositions-as-Types, Typing Judgements, and Term Evaluation
"""

from typing import Dict, Optional


class Type:
    pass


class BaseType(Type):
    def __init__(self, name: str):
        self.name = name

    def __str__(self):
        return self.name

    def __eq__(self, other):
        return isinstance(other, BaseType) and self.name == other.name


class ArrowType(Type):
    def __init__(self, from_t: Type, to_t: Type):
        self.from_t = from_t
        self.to_t = to_t

    def __str__(self):
        return f"({self.from_t} → {self.to_t})"

    def __eq__(self, other):
        return isinstance(other, ArrowType) and self.from_t == other.from_t and self.to_t == other.to_t


class Term:
    pass


class Var(Term):
    def __init__(self, name: str):
        self.name = name

    def __str__(self):
        return self.name


class Lam(Term):
    def __init__(self, var: str, var_type: Type, body: Term):
        self.var = var
        self.var_type = var_type
        self.body = body

    def __str__(self):
        return f"(λ{self.var}:{self.var_type}. {self.body})"


class App(Term):
    def __init__(self, func: Term, arg: Term):
        self.func = func
        self.arg = arg

    def __str__(self):
        return f"({self.func} {self.arg})"


def typecheck(term: Term, env: Dict[str, Type]) -> Optional[Type]:
    """Derive the type of a lambda term under typing context env: Γ ⊢ e : τ"""
    if isinstance(term, Var):
        if term.name in env:
            return env[term.name]
        raise TypeError(f"Unbound variable: {term.name}")

    elif isinstance(term, Lam):
        new_env = dict(env)
        new_env[term.var] = term.var_type
        body_type = typecheck(term.body, new_env)
        return ArrowType(term.var_type, body_type)

    elif isinstance(term, App):
        func_type = typecheck(term.func, env)
        arg_type = typecheck(term.arg, env)
        if isinstance(func_type, ArrowType):
            if func_type.from_t == arg_type:
                return func_type.to_t
            else:
                raise TypeError(f"Type mismatch: Expected {func_type.from_t}, got {arg_type}")
        else:
            raise TypeError(f"Attempted to apply non-function of type {func_type}")

    raise ValueError("Unknown term type")


if __name__ == "__main__":
    print("=== Week 04: Simply Typed Lambda Calculus (Curry-Howard) ===\n")
    A = BaseType("A")
    B = BaseType("B")
    C = BaseType("C")

    # 1. Identity Term: λx:A. x  (Proves: A → A)
    id_term = Lam("x", A, Var("x"))
    id_type = typecheck(id_term, {})
    print(f"Term: {id_term}")
    print(f"Type (Theorem Proved): {id_type}\n")

    # 2. Composition Term: λf:(B → C). λg:(A → B). λx:A. f (g x)
    # Proves: (B → C) → (A → B) → (A → C)  [Hypothetical Syllogism]
    b_to_c = ArrowType(B, C)
    a_to_b = ArrowType(A, B)
    comp_term = Lam(
        "f", b_to_c,
        Lam(
            "g", a_to_b,
            Lam(
                "x", A,
                App(Var("f"), App(Var("g"), Var("x")))
            )
        )
    )
    comp_type = typecheck(comp_term, {})
    print(f"Term: {comp_term}")
    print(f"Type (Theorem Proved): {comp_type}\n")

    # 3. Modus Ponens Term Application: (λx:A. x) applied to an argument of type A
    applied = App(id_term, Var("my_a"))
    applied_type = typecheck(applied, {"my_a": A})
    print(f"Modus Ponens Elimination: {applied} with env {{my_a : A}}")
    print(f"Resulting Type: {applied_type}")
