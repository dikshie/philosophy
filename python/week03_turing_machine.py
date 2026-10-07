#!/usr/bin/env python3
"""
Week 03: Turing Machine Simulator & Z3 Bounded Model Checking (BMC)
Focus: Deterministic Execution, Halting Decidability, and SMT Reachability Verification
"""

from typing import Dict, List, Tuple
import z3


class TuringMachine:
    def __init__(
        self,
        states: List[str],
        transitions: Dict[Tuple[str, str], Tuple[str, str, str]],
        start_state: str,
        accept_state: str,
        reject_state: str,
        blank_symbol: str = "_"
    ):
        self.states = set(states)
        self.transitions = transitions
        self.start_state = start_state
        self.accept_state = accept_state
        self.reject_state = reject_state
        self.blank = blank_symbol

    def run(self, input_tape: str, max_steps: int = 1000) -> Tuple[bool, str, int]:
        tape = list(input_tape) if input_tape else [self.blank]
        head = 0
        state = self.start_state
        step = 0

        while step < max_steps:
            if state == self.accept_state:
                return True, "".join(tape).strip(self.blank), step
            if state == self.reject_state:
                return False, "".join(tape).strip(self.blank), step

            symbol = tape[head] if head < len(tape) else self.blank
            key = (state, symbol)

            if key not in self.transitions:
                return False, "".join(tape).strip(self.blank), step

            next_state, write_sym, direction = self.transitions[key]
            tape[head] = write_sym

            if direction == "R":
                head += 1
                if head == len(tape):
                    tape.append(self.blank)
            elif direction == "L":
                if head > 0:
                    head -= 1
                else:
                    tape.insert(0, self.blank)

            state = next_state
            step += 1

        return False, "".join(tape).strip(self.blank), step


def z3_bounded_model_check_reachability(k_steps: int = 5):
    """Verify state reachability of a discrete transition system using Z3 SMT solver."""
    print("--- Z3 Bounded Model Checking (BMC) for Turing Invariants ---")
    # States: 0 = q0 (start), 1 = q1, 2 = q_acc (accept), 3 = q_rej (reject)
    state = [z3.Int(f"state_{t}") for t in range(k_steps + 1)]
    tape_val = [z3.Int(f"tape_{t}") for t in range(k_steps + 1)]

    solver = z3.Solver()
    # Initial condition: starts at q0 with tape = 0
    solver.add(state[0] == 0)
    solver.add(tape_val[0] == 0)

    # Transition logic over time steps:
    # If state=0: transitions to state=1, increments tape by 1
    # If state=1 and tape > 0: transitions to state=2 (accept)
    for t in range(k_steps):
        s_cur = state[t]
        s_next = state[t + 1]
        v_cur = tape_val[t]
        v_next = tape_val[t + 1]

        t_trans = z3.Or(
            z3.And(s_cur == 0, s_next == 1, v_next == v_cur + 1),
            z3.And(s_cur == 1, v_cur > 0, s_next == 2, v_next == v_cur),
            z3.And(s_cur == 2, s_next == 2, v_next == v_cur)  # Halt/Accept
        )
        solver.add(t_trans)

    # Question: Is the Accept State (state=2) reachable within k steps?
    goal = z3.Or([state[t] == 2 for t in range(k_steps + 1)])
    solver.push()
    solver.add(goal)
    if solver.check() == z3.sat:
        m = solver.model()
        print(f"Goal (Accept state reachability within {k_steps} steps): REACHABLE (SAT)")
        trace = [(m.eval(state[t]).as_long(), m.eval(tape_val[t]).as_long()) for t in range(k_steps + 1)]
        print(f"Verified Execution Trace (State, Tape): {trace}")
    else:
        print("Goal: UNREACHABLE")
    solver.pop()
    print()


if __name__ == "__main__":
    print("=== Week 03: Turing Machines & SMT Verification ===\n")
    # Concrete Python Binary Incrementer
    transitions = {
        ("q0", "0"): ("q0", "0", "R"),
        ("q0", "1"): ("q0", "1", "R"),
        ("q0", "_"): ("q1", "_", "L"),
        ("q1", "0"): ("q_acc", "1", "R"),
        ("q1", "1"): ("q1", "0", "L"),
        ("q1", "_"): ("q_acc", "1", "R"),
    }
    tm = TuringMachine(
        states=["q0", "q1", "q_acc", "q_rej"],
        transitions=transitions,
        start_state="q0",
        accept_state="q_acc",
        reject_state="q_rej"
    )

    inputs = ["1011", "111", "1000"]
    print("Concrete TM Execution:")
    for inp in inputs:
        accepted, out, steps = tm.run(inp)
        print(f"  Input: {inp} (dec {int(inp, 2)}) -> Output: {out} (dec {int(out, 2)}) in {steps} steps")
    print()

    z3_bounded_model_check_reachability(k_steps=4)
