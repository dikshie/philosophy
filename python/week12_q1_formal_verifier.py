#!/usr/bin/env python3
"""
Week 12: Unified Formal Logic & Epistemic Verification Suite
Runs automated sanity checks across all Quarter 1 tools (Weeks 01–11).
"""

import subprocess
import sys


SCRIPTS = [
    "python/week01_sat_prover.py",
    "python/week02_kripke_checker.py",
    "python/week03_turing_machine.py",
    "python/week04_lambda_typechecker.py",
    "python/week05_godel_numbering.py",
    "python/week06_information_theory.py",
    "python/week07_gettier_simulator.py",
    "python/week08_bayesian_updater.py",
    "python/week09_falsification_engine.py",
    "python/week10_realism_evaluator.py",
    "python/week11_nagelian_reduction.py",
]


def run_all_formal_verifiers():
    print("=" * 70)
    print("  QUARTER 1 UNIFIED FORMAL VERIFICATION SUITE (WEEKS 01 - 12)")
    print("=" * 70 + "\n")

    passed = 0
    for script in SCRIPTS:
        sys.stdout.write(f"Executing {script.split('/')[-1]} ... ")
        sys.stdout.flush()
        res = subprocess.run([sys.executable, script], capture_output=True, text=True)
        if res.returncode == 0:
            print("[PASSED]")
            passed += 1
        else:
            print(f"[FAILED with code {res.returncode}]")
            print(res.stderr)

    print(f"\nVerification Results: {passed}/{len(SCRIPTS)} modules passed successfully.")


if __name__ == "__main__":
    run_all_formal_verifiers()
