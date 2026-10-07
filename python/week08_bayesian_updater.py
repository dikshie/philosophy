#!/usr/bin/env python3
"""
Week 08: Bayesian Epistemic Updater & Dutch Book Calculator
Focus: Prior Probabilities, Conditionalization, Confirmation Measures, and Rational Betting
"""

from typing import List, Tuple


class BayesianHypothesis:
    def __init__(self, name: str, prior: float):
        self.name = name
        self.prior = prior
        self.posterior = prior

    def update(self, likelihood: float, p_evidence: float) -> float:
        """Apply Bayes' Theorem: P(H|E) = P(E|H) * P(H) / P(E)"""
        self.posterior = (likelihood * self.prior) / p_evidence
        return self.posterior

    def confirmation_measure(self) -> float:
        """Incremental confirmation: c(H, E) = P(H|E) - P(H)"""
        return self.posterior - self.prior


def sequential_bayesian_update(
    hypotheses: List[BayesianHypothesis],
    evidence_likelihoods: List[Tuple[str, List[float]]]
):
    pass  # Defined directly below


def simulate_bayesian_learning():
    print("Sequential Bayesian Updating on Physics Hypotheses:")
    # Two competing theories for an anomaly:
    # H1: New Fundamental Particle (e.g. Dark Matter candidate)
    # H2: Instrumentation Calibration Artifact
    h1 = BayesianHypothesis("H1 (New Particle)", prior=0.05)
    h2 = BayesianHypothesis("H2 (Detector Artifact)", prior=0.95)

    # Sequence of independent experiment runs yielding anomalous 5-sigma signals
    # P(Signal | H1) = 0.90, P(Signal | H2) = 0.02
    signal_runs = [
        {"run": 1, "p_E_given_H1": 0.90, "p_E_given_H2": 0.05},
        {"run": 2, "p_E_given_H1": 0.90, "p_E_given_H2": 0.05},
        {"run": 3, "p_E_given_H1": 0.90, "p_E_given_H2": 0.05},
        {"run": 4, "p_E_given_H1": 0.90, "p_E_given_H2": 0.05},
    ]

    for step in signal_runs:
        run_num = step["run"]
        l1 = step["p_E_given_H1"]
        l2 = step["p_E_given_H2"]

        p_e = (l1 * h1.posterior) + (l2 * h2.posterior)
        old_h1 = h1.posterior
        h1.posterior = (l1 * old_h1) / p_e
        h2.posterior = (l2 * h2.posterior) / p_e

        conf = h1.posterior - old_h1
        print(f"Run {run_num}: P(H1|E) = {h1.posterior:.4f} | P(H2|E) = {h2.posterior:.4f} | Incr. Confirmation: {conf:+.4f}")


def check_dutch_book(p_a: float, p_not_a: float):
    """Demonstrate a Dutch Book (guaranteed monetary loss) if credences fail Kolmogorov additivity."""
    total = p_a + p_not_a
    print(f"\nEvaluating Credences: P(A) = {p_a}, P(¬A) = {p_not_a} (Sum = {total})")
    if abs(total - 1.0) < 1e-6:
        print("-> Coherent credences: Satisfies Kolmogorov axioms. No Dutch Book possible.")
    elif total > 1.0:
        # Overconfidence Dutch Book
        print(f"-> INCOHERENT (Sum > 1.0). Bookie can sell bets on both A and ¬A for a guaranteed profit of {total - 1.0:.2f} per $1 bet!")
    else:
        # Underconfidence Dutch Book
        print(f"-> INCOHERENT (Sum < 1.0). Bookie can buy bets on both A and ¬A for a guaranteed profit of {1.0 - total:.2f}!")


if __name__ == "__main__":
    print("=== Week 08: Bayesian Epistemic Updater ===\n")
    simulate_bayesian_learning()

    print("\nDutch Book Theorem Test:")
    check_dutch_book(0.60, 0.40)  # Coherent
    check_dutch_book(0.70, 0.50)  # Incoherent (overconfident)
    check_dutch_book(0.30, 0.40)  # Incoherent (underconfident)
