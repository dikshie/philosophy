#!/usr/bin/env python3
"""
Week 05: Gödel Numbering & Diagonal Lemma Simulator
Focus: Arithmetization of Syntax, Incompleteness, and Self-Reference
"""

from typing import Dict, List


PRIMES = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]

# Symbol to base Gödel code mapping
SYMBOL_CODES: Dict[str, int] = {
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
INV_SYMBOL_CODES = {v: k for k, v in SYMBOL_CODES.items()}


def godel_encode(formula: str) -> int:
    """Encode a string of formal symbols into a unique Gödel number via prime powers."""
    symbols = formula.split()
    if len(symbols) > len(PRIMES):
        raise ValueError(f"Formula too long for base prime table (max {len(PRIMES)} symbols)")

    result = 1
    for i, sym in enumerate(symbols):
        if sym not in SYMBOL_CODES:
            raise KeyError(f"Unknown symbol: {sym}")
        code = SYMBOL_CODES[sym]
        result *= (PRIMES[i] ** code)
    return result


def godel_decode(n: int) -> List[str]:
    """Deconstruct a Gödel number back into its sequence of formal symbols."""
    symbols = []
    temp = n
    for prime in PRIMES:
        if temp == 1:
            break
        count = 0
        while temp % prime == 0:
            count += 1
            temp //= prime
        if count > 0:
            symbols.append(INV_SYMBOL_CODES.get(count, f"UNKNOWN({count})"))
    return symbols


def simulate_diagonal_lemma():
    """Demonstrate the Diagonalization Lemma fixed-point mechanism."""
    print("Diagonalization Lemma Demonstration:")
    print("Let sub(formula_code, var_code, numeral) replace free variable with numeral.")
    
    # We construct a self-referential sentence G:
    # "This sentence is not provable in formal theory T"
    formula_template = "¬ Prov ( sub ( x , x ) )"
    print(f"Given formula with free variable: {formula_template}")
    
    # In Gödel's proof, evaluating sub(g, g) constructs sentence G whose Gödel number
    # encodes the statement of its own unprovability.
    print("Fixed Point Property: T ⊢ G ↔ ¬Prov_T( ⌈G⌉ )")
    print("Consequence: If T is consistent, T ⊬ G. But because G asserts its own unprovability, G is TRUE!")


if __name__ == "__main__":
    print("=== Week 05: Gödel Numbering & Arithmetization ===\n")
    sample_formulas = [
        "x = 0",
        "¬ ( x = 0 )",
        "∀ x ( x = x )"
    ]

    for f in sample_formulas:
        gn = godel_encode(f)
        dec = " ".join(godel_decode(gn))
        print(f"Formula: '{f}'")
        print(f"  Gödel Number ⌈φ⌉: {gn}")
        print(f"  Decoded Formula : '{dec}'\n")

    simulate_diagonal_lemma()
