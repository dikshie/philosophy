#!/usr/bin/env python3
"""
Week 07: Epistemic Logic & Gettier Problem Evaluator
Focus: Justified True Belief (JTB), Epistemic Luck, and Anti-Luck Defeasibility
"""

from typing import Dict


class BeliefState:
    def __init__(
        self,
        proposition: str,
        believed: bool,
        is_true: bool,
        justified: bool,
        relies_on_false_lemma: bool,
        tracks_truth_subjunctively: bool
    ):
        self.prop = proposition
        self.believed = believed
        self.is_true = is_true
        self.justified = justified
        self.relies_on_false_lemma = relies_on_false_lemma
        self.tracks_truth = tracks_truth_subjunctively

    def satisfies_classical_jtb(self) -> bool:
        """The standard Platonic / Tripartite definition: Knowledge = Justified True Belief."""
        return self.believed and self.is_true and self.justified

    def satisfies_no_false_lemma(self) -> bool:
        """Armstrong / Harman criterion: JTB without inferring via a false premise."""
        return self.satisfies_classical_jtb() and (not self.relies_on_false_lemma)

    def satisfies_nozick_tracking(self) -> bool:
        """Robert Nozick's Subjunctive Tracking: S believes P, P is true, and if P were false, S would not believe P."""
        return self.satisfies_classical_jtb() and self.tracks_truth


def evaluate_epistemic_case(name: str, state: BeliefState):
    print(f"Case: {name}")
    print(f"  Proposition: '{state.prop}'")
    print(f"  Believed: {state.believed} | True: {state.is_true} | Justified: {state.justified}")
    print(f"  Relies on False Lemma: {state.relies_on_false_lemma}")
    print(f"  Tracks Truth Subjunctively: {state.tracks_truth}")
    
    jtb = state.satisfies_classical_jtb()
    nfl = state.satisfies_no_false_lemma()
    nozick = state.satisfies_nozick_tracking()
    
    print(f"  -> Satisfies Classical JTB : {jtb}")
    print(f"  -> No-False-Lemma Knowledge: {nfl}")
    print(f"  -> Nozick Tracking Knowledge: {nozick}")
    if jtb and not nfl:
        print("  => DIAGNOSIS: GETTIER ANOMALY DETECTED (Epistemic Luck). JTB fails to guarantee genuine knowledge!\n")
    else:
        print("  => DIAGNOSIS: Normal Epistemic State.\n")


if __name__ == "__main__":
    print("=== Week 07: Epistemic Logic & Gettier Case Simulator ===\n")

    # Case 1: Standard Valid Knowledge
    case_normal = BeliefState(
        proposition="The speed of light in vacuum is invariant",
        believed=True,
        is_true=True,
        justified=True,
        relies_on_false_lemma=False,
        tracks_truth_subjunctively=True
    )
    evaluate_epistemic_case("Standard Scientific Knowledge", case_normal)

    # Case 2: Classic Gettier Case 1 (Smith and Jones / Job and Coins)
    # Smith believes: "The man who gets the job has 10 coins in his pocket."
    # Justification: Smith was told Jones will get the job, and Smith counted 10 coins in Jones's pocket.
    # False Lemma: "Jones will get the job."
    # Accidental Truth: Smith gets the job, and Smith unbeknownst to himself has 10 coins in his own pocket!
    case_gettier_1 = BeliefState(
        proposition="The person who gets the job has 10 coins in their pocket",
        believed=True,
        is_true=True,
        justified=True,
        relies_on_false_lemma=True,
        tracks_truth_subjunctively=False
    )
    evaluate_epistemic_case("Gettier Case 1 (Smith & Jones Coins)", case_gettier_1)

    # Case 3: Fake Barn Country (Goldman)
    # Henry sees a real barn and forms the true justified belief "That is a barn".
    # But he is surrounded by 99 visually identical papier-mâché fake barns.
    case_fake_barn = BeliefState(
        proposition="That object in the field is a barn",
        believed=True,
        is_true=True,
        justified=True,
        relies_on_false_lemma=False,  # No explicit false premise used
        tracks_truth_subjunctively=False  # Had it been a fake barn, he still would have believed it was real
    )
    evaluate_epistemic_case("Goldman's Fake Barn Country", case_fake_barn)
