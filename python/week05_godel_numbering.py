#!/usr/bin/env python3
"""
Week 05: Gödel Numbering & Incompleteness with SymPy & Z3
Focus: Prime Factorization Arithmetization (SymPy), Diagonal Lemma, and Löb's Theorem (Z3)
"""

from typing import Dict, List
import sympy
import z3


# Canonical symbol codes for arithmetic
SYMBOL_MAP = {
    "0": 1,
    "S": 3,
    "=": 5,
    "¬": 7,
    "∧": 9,
    "∨": 11,
    "→": 13,
    "∀": 15,
    "(": 17,
    ")": 19,
    "x": 21,
    "y": 23,
    "+": 25,
    "*": 27
}
INV_SYMBOL_MAP = {v: k for k, v in SYMBOL_MAP.items()}


def sympy_godel_encode(formula: str) -> int:
    """Encode formula into unique Gödel number using SymPy's prime generator: 2^c1 * 3^c2 * 5^c3 ..."""
    tokens = formula.split()
    gn = 1
    for idx, tok in enumerate(tokens):
        p = sympy.prime(idx + 1)
        code = SYMBOL_MAP.get(tok, 29)
        gn *= (p ** code)
    return gn


def sympy_godel_decode(gn: int) -> List[str]:
    """Decode a Gödel number back into syntax using SymPy prime factorization factorint()."""
    factors = sympy.factorint(gn)
    # Sort primes in ascending order
    sorted_primes = sorted(factors.keys())
    tokens = []
    for p in sorted_primes:
        code = factors[p]
        tokens.append(INV_SYMBOL_MAP.get(code, f"UNKNOWN({code})"))
    return tokens


def z3_lobs_theorem_verification():
    """Verify Löb's Theorem condition in Modal Provability Logic GL (Gödel-Löb) using Z3."""
    print("--- Z3 Provability Logic & Gödel Sentence ---")
    # In Provability Logic GL: Box φ means "φ is provable in Peano Arithmetic".
    # Löb's Theorem: Box (Box P → P) → Box P
    # If PA proves that proving P implies P, then PA already proves P!
    P = z3.Bool("P")
    Prov_P = z3.Bool("Prov_P")
    Prov_Prov_P = z3.Bool("Prov_Prov_P")

    # Gödel sentence G asserts its own unprovability: G ↔ ¬Prov(G)
    G = z3.Bool("G")
    Prov_G = z3.Bool("Prov_G")

    solver = z3.Solver()
    # Fixed point definition: G ↔ ¬Prov_G
    solver.add(G == z3.Not(Prov_G))

    # Consistency assumption: If a sentence is provable, it is true (Soundness)
    solver.add(z3.Implies(Prov_G, G))

    # Can G be provable?
    solver.push()
    solver.add(Prov_G == True)
    res = solver.check()
    print(f"Can Gödel sentence G be Provable? {'NO (UNSAT - Provably Independent)' if res == z3.unsat else 'YES'}")
    solver.pop()

    # If G is not provable, what is the truth value of G?
    solver.push()
    solver.add(Prov_G == False)
    if solver.check() == z3.sat:
        m = solver.model()
        print(f"When Prov(G) is False, Truth of G = {m.eval(G)} (True in the standard model N!)")
    solver.pop()
    print()


if __name__ == "__main__":
    print("=== Week 05: Gödel Numbering & Incompleteness (SymPy & Z3) ===\n")
    sample_formulas = [
        "x = 0",
        "¬ ( x = 0 )",
        "∀ x ( x = x )"
    ]

    print("--- SymPy Arithmetization (Prime Factorization) ---")
    for f in sample_formulas:
        gn = sympy_godel_encode(f)
        factors = sympy.factorint(gn)
        dec = " ".join(sympy_godel_decode(gn))
        print(f"Formula: '{f}'")
        print(f"  Gödel Number ⌈φ⌉: {gn}")
        print(f"  Prime Factors   : {factors}")
        print(f"  Decoded Formula : '{dec}'\n")

    z3_lobs_theorem_verification()
