#!/usr/bin/env python3
"""
Week 01: Propositional Logic Truth Table Generator & DPLL SAT Solver
Focus: Formal Syntax, Valuation, Semantic Entailment, and Satisfiability
"""

from typing import Dict, List, Set, Tuple


class PropFormula:
    pass


class Atom(PropFormula):
    def __init__(self, name: str):
        self.name = name

    def evaluate(self, env: Dict[str, bool]) -> bool:
        return env[self.name]

    def atoms(self) -> Set[str]:
        return {self.name}

    def __str__(self):
        return self.name


class Not(PropFormula):
    def __init__(self, inner: PropFormula):
        self.inner = inner

    def evaluate(self, env: Dict[str, bool]) -> bool:
        return not self.inner.evaluate(env)

    def atoms(self) -> Set[str]:
        return self.inner.atoms()

    def __str__(self):
        return f"¬{self.inner}"


class And(PropFormula):
    def __init__(self, left: PropFormula, right: PropFormula):
        self.left = left
        self.right = right

    def evaluate(self, env: Dict[str, bool]) -> bool:
        return self.left.evaluate(env) and self.right.evaluate(env)

    def atoms(self) -> Set[str]:
        return self.left.atoms() | self.right.atoms()

    def __str__(self):
        return f"({self.left} ∧ {self.right})"


class Or(PropFormula):
    def __init__(self, left: PropFormula, right: PropFormula):
        self.left = left
        self.right = right

    def evaluate(self, env: Dict[str, bool]) -> bool:
        return self.left.evaluate(env) or self.right.evaluate(env)

    def atoms(self) -> Set[str]:
        return self.left.atoms() | self.right.atoms()

    def __str__(self):
        return f"({self.left} ∨ {self.right})"


class Implies(PropFormula):
    def __init__(self, antecedent: PropFormula, consequent: PropFormula):
        self.antecedent = antecedent
        self.consequent = consequent

    def evaluate(self, env: Dict[str, bool]) -> bool:
        return (not self.antecedent.evaluate(env)) or self.consequent.evaluate(env)

    def atoms(self) -> Set[str]:
        return self.antecedent.atoms() | self.consequent.atoms()

    def __str__(self):
        return f"({self.antecedent} → {self.consequent})"


def generate_truth_table(formula: PropFormula) -> None:
    """Print the complete truth table for a given propositional formula."""
    var_list = sorted(list(formula.atoms()))
    header = " | ".join(var_list) + f" | {formula}"
    print(header)
    print("-" * len(header))

    n = len(var_list)
    is_tautology = True
    is_satisfiable = False

    for i in range(1 << n):
        env = {}
        for bit_idx, var in enumerate(var_list):
            val = bool((i >> (n - 1 - bit_idx)) & 1)
            env[var] = val

        res = formula.evaluate(env)
        if res:
            is_satisfiable = True
        else:
            is_tautology = False

        row_str = " | ".join(str(int(env[v])) for v in var_list)
        print(f"{row_str} |   {int(res)}")

    print("-" * len(header))
    print(f"Status: Tautology (Valid): {is_tautology} | Satisfiable: {is_satisfiable}\n")


def dpll_sat_solve(clauses: List[Set[str]], assignment: Dict[str, bool] = None) -> Tuple[bool, Dict[str, bool]]:
    """DPLL algorithm for deciding satisfiability in Conjunctive Normal Form (CNF)."""
    if assignment is None:
        assignment = {}

    # Simplify clauses under current assignment
    simplified = []
    for clause in clauses:
        clause_true = False
        new_clause = set()
        for lit in clause:
            var = lit.lstrip('~')
            sign = not lit.startswith('~')
            if var in assignment:
                if assignment[var] == sign:
                    clause_true = True
                    break
            else:
                new_clause.add(lit)
        if not clause_true:
            if not new_clause:
                return False, {}  # Empty clause: contradiction
            simplified.append(new_clause)

    if not simplified:
        return True, assignment  # All clauses satisfied

    # Unit Propagation
    for clause in simplified:
        if len(clause) == 1:
            lit = next(iter(clause))
            var = lit.lstrip('~')
            val = not lit.startswith('~')
            new_assign = dict(assignment)
            new_assign[var] = val
            return dpll_sat_solve(simplified, new_assign)

    # Pick branching variable
    var = next(iter(simplified[0])).lstrip('~')

    # Try assigning True
    sat, res = dpll_sat_solve(simplified, {**assignment, var: True})
    if sat:
        return True, res

    # Try assigning False
    return dpll_sat_solve(simplified, {**assignment, var: False})


if __name__ == "__main__":
    print("=== Week 01: Classical Propositional Logic Solver ===\n")
    p, q = Atom("P"), Atom("Q")

    # 1. Modus Ponens valid implication: ((P → Q) ∧ P) → Q
    f1 = Implies(And(Implies(p, q), p), q)
    print(f"Checking Modus Ponens: {f1}")
    generate_truth_table(f1)

    # 2. De Morgan Law: ¬(P ∨ Q) ↔ (¬P ∧ ¬Q)
    f2 = Implies(Not(Or(p, q)), And(Not(p), Not(q)))
    print(f"Checking De Morgan Direction: {f2}")
    generate_truth_table(f2)

    # 3. DPLL SAT Check on CNF: (P ∨ Q) ∧ (¬P ∨ Q) ∧ (¬Q)
    print("DPLL SAT Solver test:")
    cnf = [{"P", "Q"}, {"~P", "Q"}, {"~Q"}]
    print(f"Clauses: {cnf}")
    is_sat, model = dpll_sat_solve(cnf)
    print(f"Satisfiable: {is_sat} | Model: {model}")
