#!/usr/bin/env python3
"""
Week 08: Bayesian Epistemic Updater with SymPy & Z3
Focus: Exact Rational Updating (SymPy), Bayes Factors, and Dutch Book Arbitrage Solver (Z3)
"""

import sympy
from sympy import Rational, symbols
import z3


def sympy_exact_bayesian_update():
    print("--- 1. SymPy Exact Rational Bayesian Updating ---")
    # Competing physics hypotheses for a 5-sigma resonance:
    # H1: Genuine new fundamental particle
    # H2: Statistical fluctuation / detector noise
    p_h1 = Rational(1, 20)     # Prior: 5%
    p_h2 = Rational(19, 20)    # Prior: 95%

    # Likelihoods:
    # P(Signal | H1) = 9/10, P(Signal | H2) = 1/50
    p_e_given_h1 = Rational(9, 10)
    p_e_given_h2 = Rational(1, 50)

    # Law of Total Probability for Evidence P(E):
    p_e = (p_e_given_h1 * p_h1) + (p_e_given_h2 * p_h2)

    # Posterior P(H1 | E)
    post_h1 = (p_e_given_h1 * p_h1) / p_e
    post_h2 = (p_e_given_h2 * p_h2) / p_e

    # Bayes Factor: P(E | H1) / P(E | H2)
    bayes_factor = p_e_given_h1 / p_e_given_h2

    print(f"Prior P(H1)           : {p_h1} ({float(p_h1):.4f})")
    print(f"Prior P(H2)           : {p_h2} ({float(p_h2):.4f})")
    print(f"Bayes Factor B12      : {bayes_factor} (Evidence strongly favors H1)")
    print(f"Posterior P(H1 | E)   : {post_h1} ({float(post_h1):.4f})")
    print(f"Posterior P(H2 | E)   : {post_h2} ({float(post_h2):.4f})")
    print(f"Incremental Confirmation: {post_h1 - p_h1} ({float(post_h1 - p_h1):+.4f})\n")


def z3_dutch_book_arbitrage_solver(p_A: float, p_notA: float):
    """Use Z3 SMT linear programming to prove/find Dutch Book arbitrage if credences violate additivity."""
    print(f"--- 2. Z3 Dutch Book Arbitrage Solver for Credences P(A)={p_A}, P(¬A)={p_notA} ---")
    # In betting semantics, an agent with credence p will accept bets with payoff:
    # Bet on A with stake S1: If A occurs, payout = S1 * (1 - p); if ¬A occurs, payout = -S1 * p
    # Bookie seeks stakes S1, S2 such that Bookie Profit > 0 in ALL possible states of the world!
    
    S1 = z3.Real("S1")  # Stake on A
    S2 = z3.Real("S2")  # Stake on ¬A

    solver = z3.Solver()

    # Bookie's profit if A is true: S1*p_A - S1*(1 - p_A) is payoff to agent
    # Equivalently, agent profit in state A = S1 * (1 - p_A) - S2 * p_notA
    # Bookie profit in state A = S1 * p_A - S1 * (1 - p_A) ?
    # Standard betting contract: Price to enter bet is P. Payout is 1 if event occurs, 0 otherwise.
    # Agent pays (S1 * p_A) and (S2 * p_notA).
    # If A occurs: Bookie pays S1 to agent. Bookie Net Profit = (S1*p_A + S2*p_notA) - S1
    # If ¬A occurs: Bookie pays S2 to agent. Bookie Net Profit = (S1*p_A + S2*p_notA) - S2

    profit_if_A = (S1 * p_A + S2 * p_notA) - S1
    profit_if_notA = (S1 * p_A + S2 * p_notA) - S2

    # A Dutch Book exists if there exist non-negative stakes where Bookie Profit > 0 in BOTH worlds!
    min_profit = z3.Real("min_profit")
    solver.add(S1 >= 0, S2 >= 0, z3.Or(S1 > 0, S2 > 0))
    solver.add(profit_if_A >= min_profit)
    solver.add(profit_if_notA >= min_profit)
    solver.add(min_profit > 0)

    if solver.check() == z3.sat:
        m = solver.model()
        s1_val = m.eval(S1)
        s2_val = m.eval(S2)
        p_val = m.eval(min_profit)
        print(f"  -> DUTCH BOOK ARBITRAGE FOUND (Credences are Incoherent!)")
        print(f"  -> Bookie stakes: Bet on A = ${s1_val}, Bet on ¬A = ${s2_val}")
        print(f"  -> Guaranteed Bookie Net Profit: >= ${p_val} regardless of reality!\n")
    else:
        print("  -> Credences are Coherent (Satisfies Kolmogorov Axiom P(A) + P(¬A) = 1.0). No Dutch Book possible!\n")


if __name__ == "__main__":
    print("=== Week 08: Bayesian Epistemic Updater (SymPy & Z3) ===\n")
    sympy_exact_bayesian_update()

    # Case 1: Incoherent overconfident credences (0.7 + 0.5 = 1.2 > 1)
    z3_dutch_book_arbitrage_solver(p_A=0.70, p_notA=0.50)

    # Case 2: Coherent credences (0.6 + 0.4 = 1.0)
    z3_dutch_book_arbitrage_solver(p_A=0.60, p_notA=0.40)
