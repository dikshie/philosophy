#!/usr/bin/env python3
"""
Week 02: Modal Logic Kripke Model Checker
Focus: Possible Worlds, Accessibility Relations, Box (Necessity) & Diamond (Possibility)
"""

from typing import Dict, List, Set


class KripkeFrame:
    def __init__(self, worlds: List[str], relations: List[tuple]):
        self.worlds = set(worlds)
        self.relations = set(relations)  # set of (w1, w2)

    def accessible(self, w: str) -> Set[str]:
        return {w2 for (w1, w2) in self.relations if w1 == w}

    def is_reflexive(self) -> bool:
        return all((w, w) in self.relations for w in self.worlds)

    def is_symmetric(self) -> bool:
        return all((w2, w1) in self.relations for (w1, w2) in self.relations)

    def is_transitive(self) -> bool:
        for (w1, w2) in self.relations:
            for (w2_prime, w3) in self.relations:
                if w2 == w2_prime and (w1, w3) not in self.relations:
                    return False
        return True

    def modal_system(self) -> str:
        refl = self.is_reflexive()
        symm = self.is_symmetric()
        trans = self.is_transitive()
        if refl and symm and trans:
            return "S5 (Equivalence Relation)"
        elif refl and trans:
            return "S4 (Preorder)"
        elif refl and symm:
            return "B (Brouwerian)"
        elif refl:
            return "T (Reflexive)"
        else:
            return "K (Basic Modal Logic)"


class KripkeModel:
    def __init__(self, frame: KripkeFrame, valuation: Dict[str, Set[str]]):
        self.frame = frame
        # valuation: prop_name -> set of worlds where prop is true
        self.valuation = valuation

    def evaluate(self, formula: dict, world: str) -> bool:
        op = formula["op"]
        if op == "atom":
            prop = formula["name"]
            return world in self.valuation.get(prop, set())
        elif op == "not":
            return not self.evaluate(formula["arg"], world)
        elif op == "and":
            return self.evaluate(formula["left"], world) and self.evaluate(formula["right"], world)
        elif op == "or":
            return self.evaluate(formula["left"], world) or self.evaluate(formula["right"], world)
        elif op == "box":  # Necessarily phi: true in all accessible worlds
            target = formula["arg"]
            return all(self.evaluate(target, v) for v in self.frame.accessible(world))
        elif op == "diamond":  # Possibly phi: true in at least one accessible world
            target = formula["arg"]
            return any(self.evaluate(target, v) for v in self.frame.accessible(world))
        else:
            raise ValueError(f"Unknown operator: {op}")


if __name__ == "__main__":
    print("=== Week 02: Modal Logic Kripke Model Checker ===\n")
    # Define 3 possible worlds: w0 (Actual), w1, w2
    worlds = ["w0", "w1", "w2"]
    
    # S4 / S5 frame construction: Reflexive + Transitive + Symmetric
    relations = [
        ("w0", "w0"), ("w1", "w1"), ("w2", "w2"),
        ("w0", "w1"), ("w1", "w0"),
        ("w1", "w2"), ("w2", "w1"),
        ("w0", "w2"), ("w2", "w0")
    ]
    frame = KripkeFrame(worlds, relations)
    print(f"Frame worlds: {worlds}")
    print(f"Modal classification: {frame.modal_system()}")

    # Valuation: p is true in w0 and w1, false in w2; q is true only in w0
    valuation = {
        "p": {"w0", "w1"},
        "q": {"w0"}
    }
    model = KripkeModel(frame, valuation)

    p_atom = {"op": "atom", "name": "p"}
    box_p = {"op": "box", "arg": p_atom}
    diamond_p = {"op": "diamond", "arg": p_atom}

    print("\nModel evaluation:")
    for w in worlds:
        val_p = model.evaluate(p_atom, w)
        val_box_p = model.evaluate(box_p, w)
        val_diam_p = model.evaluate(diamond_p, w)
        print(f"World {w}: p = {val_p} | □p = {val_box_p} | ◇p = {val_diam_p}")
