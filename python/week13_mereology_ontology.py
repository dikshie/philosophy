#!/usr/bin/env python3
"""
Week 13: Formal Mereology & Quinean Ontological Commitment Simulator
Focus: Classical Extensional Mereology (CEM), Parthood, Overlap, and Bound Variables
"""

from typing import Dict, List, Set


class MereologicalUniverse:
    def __init__(self, entities: List[str], atomic_parts: Dict[str, Set[str]]):
        self.entities = set(entities)
        # atomic_parts: maps each entity to the set of fundamental atoms it contains
        self.atomic_parts = atomic_parts

    def is_part_of(self, x: str, y: str) -> bool:
        """x is part of y iff the atoms of x are a subset of the atoms of y: P(x, y)"""
        return self.atomic_parts[x].issubset(self.atomic_parts[y])

    def is_proper_part_of(self, x: str, y: str) -> bool:
        """x is a proper part of y iff P(x, y) and x != y: PP(x, y)"""
        return self.is_part_of(x, y) and x != y

    def overlaps(self, x: str, y: str) -> bool:
        """x overlaps y iff they share at least one part (common atom): O(x, y)"""
        return len(self.atomic_parts[x] & self.atomic_parts[y]) > 0

    def is_disjoint(self, x: str, y: str) -> bool:
        """x and y are mereologically disjoint iff they do not overlap: D(x, y)"""
        return not self.overlaps(x, y)

    def find_mereological_fusion(self, subset_entities: Set[str]) -> str:
        """Find the mereological sum / fusion of a subset of entities."""
        combined_atoms = set()
        for e in subset_entities:
            combined_atoms |= self.atomic_parts[e]

        for e, atoms in self.atomic_parts.items():
            if atoms == combined_atoms:
                return e
        return f"Composite Object containing atoms {combined_atoms}"


def check_quinean_commitment(theory_axioms: List[str]):
    print("Quinean Ontological Commitment Analysis:")
    print("Criterion: 'To be is to be the value of a bound variable.'")
    print("Theory statements:")
    for ax in theory_axioms:
        print(f"  - {ax}")
        if "∃" in ax:
            entity = ax.split("∃")[-1].split()[0].strip(",")
            print(f"    => Theory is ONTOLOGICALLY COMMITTED to the existence of entities bound by '{entity}'.")


if __name__ == "__main__":
    print("=== Week 13: Classical Extensional Mereology & Ontology ===\n")

    # Define a simple physical composition universe
    # Atoms: electron_1, electron_2, proton_1
    universe = MereologicalUniverse(
        entities=["electron_1", "proton_1", "hydrogen_atom", "water_molecule"],
        atomic_parts={
            "electron_1": {"e1"},
            "proton_1": {"p1"},
            "hydrogen_atom": {"e1", "p1"},
            "water_molecule": {"e1", "e2", "p1", "p2", "o1"}
        }
    )

    print("Checking Mereological Relations:")
    print(f"Is electron_1 part of hydrogen_atom? : {universe.is_part_of('electron_1', 'hydrogen_atom')}")
    print(f"Is hydrogen_atom proper part of water? : {universe.is_proper_part_of('hydrogen_atom', 'water_molecule')}")
    print(f"Does electron_1 overlap proton_1?    : {universe.overlaps('electron_1', 'proton_1')}")
    print(f"Are electron_1 and proton_1 disjoint?  : {universe.is_disjoint('electron_1', 'proton_1')}")

    print("\nMereological Fusion:")
    fus = universe.find_mereological_fusion({"electron_1", "proton_1"})
    print(f"Fusion of electron_1 and proton_1 -> {fus}")

    print()
    check_quinean_commitment([
        "∀x (Particle(x) → HasMass(x))",
        "∃x (HiggsBoson(x) ∧ Mass(x, 125GeV))",
        "∃y (SpacetimeCurvature(y) ∧ GeneratedBy(y, StressEnergyTensor))"
    ])
