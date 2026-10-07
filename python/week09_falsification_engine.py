#!/usr/bin/env python3
"""
Week 09: Popperian Falsification & Duhem-Quine Holism Engine
Focus: Modus Tollens Asymmetry, Auxiliary Hypotheses, and Underdetermination
"""

from typing import Dict, List


class ScientificTheorySystem:
    def __init__(self, core_law: str, auxiliaries: Dict[str, str]):
        self.core_law = core_law
        self.auxiliaries = auxiliaries  # name -> description
        self.auxiliary_status = {k: True for k in auxiliaries}

    def predict_observation(self, expected_observation: str) -> str:
        all_true = all(self.auxiliary_status.values())
        if all_true:
            return f"Predicts: {expected_observation} under active core and auxiliaries."
        return "Prediction indeterminate (one or more auxiliaries disabled/modified)."

    def apply_anomaly(self, observation_failed: bool, strategy: str, target_auxiliary: str = None):
        """Simulate Duhem-Quine holism: (Core ∧ Aux1 ∧ ... ∧ AuxN) → O.
           If ¬O occurs, logic alone does not tell which premise to reject."""
        print(f"\nEmpirical Observation: {'FAILED (¬O)' if observation_failed else 'CONFIRMED (O)'}")
        if not observation_failed:
            print("-> Corroboration: Core law survives testing round.")
            return

        print("-> Logical deduction: ¬(Core ∧ A1 ∧ A2 ∧ ... ∧ An)")
        if strategy == "naive_popperian":
            print("  [Naive Popperian Strategy]: Reject the core theory directly!")
            print(f"  Result: Core Law '{self.core_law}' is declared FALSIFIED.")
        elif strategy == "duhem_quine_auxiliary_adjustment":
            if target_auxiliary and target_auxiliary in self.auxiliary_status:
                self.auxiliary_status[target_auxiliary] = False
                print(f"  [Duhem-Quine Strategy]: Preserve Core Law '{self.core_law}'.")
                print(f"  Result: Modified auxiliary assumption '{target_auxiliary}' ({self.auxiliaries[target_auxiliary]}).")
                print("  Historical Analog: Postulating Neptune's existence to save Newtonian mechanics from Uranus orbit anomaly!")
        else:
            print(f"  Unknown strategy: {strategy}")


if __name__ == "__main__":
    print("=== Week 09: Popperian Demarcation & Duhem-Quine Holism ===\n")

    # Historical Case: Newtonian Celestial Mechanics
    newton_system = ScientificTheorySystem(
        core_law="Newton's Law of Universal Gravitation + F = ma",
        auxiliaries={
            "A1_solar_system": "The Solar System consists only of the known 7 planets",
            "A2_optics": "Telescope optical lenses obey geometric ray optics",
            "A3_rigid_earth": "The Earth is an inertial reference frame with known rotational axis",
            "A4_vacuum": "Interplanetary space exerts negligible drag force"
        }
    )

    print(f"Core Law: {newton_system.core_law}")
    print("Auxiliary Assumptions:")
    for k, v in newton_system.auxiliaries.items():
        print(f"  [{k}]: {v}")

    print("\nTest Case: Orbit of Uranus deviates from prediction!")
    newton_system.apply_anomaly(
        observation_failed=True,
        strategy="duhem_quine_auxiliary_adjustment",
        target_auxiliary="A1_solar_system"
    )
    print("Post-test system status: Core theory preserved, auxiliary A1 rejected -> Discovery of Neptune (1846).")
