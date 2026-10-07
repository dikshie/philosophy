#!/usr/bin/env python3
"""
Week 10: Scientific Realism vs Constructive Empiricism Evaluator
Focus: Model-Theoretic Empirical Adequacy, Observable Substructures, and Unobservables
"""

from typing import Dict, List, Set


class TheoreticalModel:
    def __init__(self, name: str, unobservable_entities: Set[str], observable_predictions: Dict[str, float]):
        self.name = name
        self.unobservables = unobservable_entities  # e.g. quarks, wavefunction, Higgs field
        self.observable_predictions = observable_predictions  # metric -> predicted value

    def is_empirically_adequate(self, empirical_observations: Dict[str, float], tolerance: float = 0.05) -> bool:
        """Van Fraassen criterion: A theory is empirically adequate if its observable
           submodel matches all actual observable phenomena within experimental tolerance."""
        for obs_key, actual_val in empirical_observations.items():
            if obs_key not in self.observable_predictions:
                return False
            pred_val = self.observable_predictions[obs_key]
            if abs(pred_val - actual_val) > tolerance:
                return False
        return True


def evaluate_epistemic_stances(model: TheoreticalModel, empirical_data: Dict[str, float]):
    adequate = model.is_empirically_adequate(empirical_data)
    print(f"Theory Model: {model.name}")
    print(f"  Unobservable Entities Posited: {list(model.unobservables)}")
    print(f"  Observable Data Match: {adequate}")

    print("\n  Philosophical Assessment:")
    print("  1. Constructive Empiricist Stance (Bas van Fraassen):")
    if adequate:
        print("     -> ACCEPT the theory as EMPIRICALLY ADEQUATE. Withhold belief regarding the literal reality of unobservables.")
    else:
        print("     -> REJECT the theory: Fails empirical adequacy.")

    print("  2. Scientific Realist Stance (Richard Boyd, Stathis Psillos):")
    if adequate:
        print("     -> BELIEVE the theory as APPROXIMATELY TRUE. Commit to the physical existence of posited unobservables (No-Miracles Argument).")
    else:
        print("     -> REJECT or refine theoretical postulates.")
    print("-" * 60)


if __name__ == "__main__":
    print("=== Week 10: Scientific Realism vs Constructive Empiricism ===\n")

    empirical_observations = {
        "anomalous_magnetic_moment_g2": 2.00231930436,
        "cross_section_higgs_fb": 55.6,
        "spectral_line_shift_nm": 656.28
    }

    # Model A: Standard Model QFT (Posits unobservable quarks, gluons, vacuum fields)
    model_sm = TheoreticalModel(
        name="Standard Model QFT",
        unobservable_entities={"Quarks", "Gluons", "Higgs Field Vacuum Expectation Value"},
        observable_predictions={
            "anomalous_magnetic_moment_g2": 2.00231930436,
            "cross_section_higgs_fb": 55.6,
            "spectral_line_shift_nm": 656.28
        }
    )

    evaluate_epistemic_stances(model_sm, empirical_observations)
