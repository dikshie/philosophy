#!/usr/bin/env python3
"""
Week 06: Information Theory & Landauer Principle Calculator
Focus: Shannon Syntactic Entropy vs Floridi Semantic Veridicality & Thermodynamic Limits
"""

import math
from typing import Dict, List


BOLTZMANN_CONSTANT = 1.380649e-23  # J/K


def shannon_entropy(probabilities: List[float]) -> float:
    """Calculate Shannon entropy H(X) = -sum(p * log2(p))."""
    total = sum(probabilities)
    norm_probs = [p / total for p in probabilities if p > 0]
    return -sum(p * math.log2(p) for p in norm_probs)


def floridi_semantic_status(is_well_formed: bool, is_meaningful: bool, is_true: bool) -> str:
    """Classify data under Luciano Floridi's Theory of Strongly Semantic Information (TSSI)."""
    if not is_well_formed:
        return "Malformed Syntax (Not Data)"
    if not is_meaningful:
        return "Syntactic Noise (Lacks Semantics)"
    if not is_true:
        return "Misinformation / Disinformation (Pseudoinformation)"
    return "Veridical Semantic Information (Genuine Knowledge Component)"


def landauer_minimum_heat(erased_bits: int, temp_kelvin: float = 300.0) -> Dict[str, float]:
    """Calculate minimum heat dissipated when erasing bits: Delta Q >= k_B * T * ln(2)."""
    energy_per_bit = BOLTZMANN_CONSTANT * temp_kelvin * math.log(2)
    total_energy_joules = erased_bits * energy_per_bit
    return {
        "erased_bits": erased_bits,
        "temperature_K": temp_kelvin,
        "energy_per_bit_J": energy_per_bit,
        "total_energy_J": total_energy_joules,
        "total_energy_eV": total_energy_joules / 1.602176634e-19
    }


if __name__ == "__main__":
    print("=== Week 06: Semantic Information & Physical Computation ===\n")

    # 1. Shannon Syntactic Entropy
    p_uniform = [0.25, 0.25, 0.25, 0.25]
    p_biased = [0.90, 0.05, 0.03, 0.02]
    print(f"Shannon Entropy (Uniform distribution): {shannon_entropy(p_uniform):.4f} bits")
    print(f"Shannon Entropy (Biased distribution) : {shannon_entropy(p_biased):.4f} bits\n")

    # 2. Floridi Semantic Status
    scenarios = [
        ("Gibberish sequence '&&#@'", False, False, False),
        ("Colorless green ideas sleep furiously", True, False, False),
        ("The Moon is made of green cheese", True, True, False),
        ("Water is H2O", True, True, True),
    ]
    print("Floridi Semantic Classification:")
    for desc, wf, mean, tr in scenarios:
        status = floridi_semantic_status(wf, mean, tr)
        print(f"  Statement: '{desc}' -> Status: {status}")

    # 3. Landauer Principle
    print("\nLandauer Erasure Limit:")
    res = landauer_minimum_heat(erased_bits=10**9, temp_kelvin=300.0)  # 1 Gigabit at room temp
    print(f"  Erasing 1 GB of data at {res['temperature_K']} K requires dissipating:")
    print(f"  {res['total_energy_J']:.6e} Joules ({res['total_energy_eV']:.6e} eV)")
