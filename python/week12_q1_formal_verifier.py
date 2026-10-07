#!/usr/bin/env python3
"""
Week 12: Unified Formal Logic & Epistemic Verification Suite (SymPy & Z3)
Runs automated sanity checks across all Quarter 1 tools (Weeks 01–11) + Week 13.
"""

import subprocess
import sys


SCRIPTS = [
    ("Week 01: Classical Logic SAT Prover", "python/week01_sat_prover.py"),
    ("Week 02: Modal Kripke SMT Checker", "python/week02_kripke_checker.py"),
    ("Week 03: Turing Bounded Model Checker", "python/week03_turing_machine.py"),
    ("Week 04: Lambda Calculus Type Unifier", "python/week04_lambda_typechecker.py"),
    ("Week 05: Gödel Numbering & Incompleteness", "python/week05_godel_numbering.py"),
    ("Week 06: Information & Landauer Limits", "python/week06_information_theory.py"),
    ("Week 07: Epistemic Logic & Gettier SMT", "python/week07_gettier_simulator.py"),
    ("Week 08: Bayesian Epistemic Updater", "python/week08_bayesian_updater.py"),
    ("Week 09: Popperian Falsification & Duhem-Quine", "python/week09_falsification_engine.py"),
    ("Week 10: Realism vs Constructive Empiricism", "python/week10_realism_evaluator.py"),
    ("Week 11: Inter-Theoretic Nagelian Reduction", "python/week11_nagelian_reduction.py"),
    ("Week 13: Mereology & Quinean Ontology", "python/week13_mereology_ontology.py"),
]


def run_all_formal_verifiers():
    print("=" * 75)
    print("  QUARTER 1 UNIFIED FORMAL VERIFICATION SUITE (WEEKS 01 - 13)")
    print("  Engine: SymPy (Symbolic Algebra) & Z3 SMT Solver (Theorem Proving)")
    print("=" * 75 + "\n")

    passed = 0
    for name, script in SCRIPTS:
        sys.stdout.write(f"Testing {name:46} ... ")
        sys.stdout.flush()
        res = subprocess.run([sys.executable, script], capture_output=True, text=True)
        if res.returncode == 0:
            print("[PASSED]")
            passed += 1
        else:
            print(f"[FAILED with code {res.returncode}]")
            print(res.stderr)

    print(f"\nVerification Results: {passed}/{len(SCRIPTS)} modules passed successfully.")
    return passed == len(SCRIPTS)


if __name__ == "__main__":
    success = run_all_formal_verifiers()
    sys.exit(0 if success else 1)
