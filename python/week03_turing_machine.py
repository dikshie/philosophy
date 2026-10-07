#!/usr/bin/env python3
"""
Week 03: Turing Machine Simulator & Halting Problem Paradox Demo
Focus: Formal Computation, Tape Transitions, and Undecidability
"""

from typing import Dict, List, Tuple


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


def simulate_halting_paradox():
    print("Simulating Diagonalization in the Halting Problem:")
    print("Suppose an oracle H(code, input) decides whether code halts on input.")
    
    def hypothetical_H(program_name: str, inp: str) -> bool:
        # Mock oracle
        return True

    def diagonal_D(program_name: str):
        # D calls H on (program, program) and does the opposite
        halts = hypothetical_H(program_name, program_name)
        if halts:
            return "Loops forever"
        else:
            return "Halts immediately"

    print("Evaluating D(D):")
    print(f"If H(D, D) = True, D does: {diagonal_D('D')}")
    print("Contradiction: D halts iff D does not halt. Therefore H cannot exist.\n")


if __name__ == "__main__":
    print("=== Week 03: Turing Machine Simulator ===\n")
    # Binary Incrementer Machine (adds 1 to a binary string)
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
    for inp in inputs:
        accepted, out, steps = tm.run(inp)
        print(f"Input: {inp} (dec {int(inp, 2)}) -> Output: {out} (dec {int(out, 2)}) in {steps} steps")

    print()
    simulate_halting_paradox()
