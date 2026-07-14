"""A small pushdown automaton simulator for the language a^n b^n."""

from __future__ import annotations

import argparse
from dataclasses import dataclass


@dataclass(frozen=True)
class SimulationResult:
    """The outcome of processing one input string."""

    accepted: bool
    reason: str


class PDASimulator:
    """Recognize strings in L = {a^n b^n | n >= 0}.

    The automaton pushes one marker for each ``a`` and pops one marker for each
    ``b``. Once it starts reading ``b`` symbols, no more ``a`` symbols are
    allowed.
    """

    def __init__(self) -> None:
        self.stack: list[str] = []

    def process(self, input_string: str) -> bool:
        """Return whether *input_string* is accepted by the automaton."""
        return self.simulate(input_string).accepted

    def simulate(self, input_string: str) -> SimulationResult:
        """Process *input_string* and return its result with an explanation."""
        self.stack = []
        reading_bs = False

        for position, char in enumerate(input_string, start=1):
            if char == "a" and not reading_bs:
                self.stack.append("A")
            elif char == "b":
                reading_bs = True
                if not self.stack:
                    return SimulationResult(
                        False, f"position {position}: 'b' has no matching 'a'"
                    )
                self.stack.pop()
            elif char == "a":
                return SimulationResult(
                    False, f"position {position}: 'a' cannot follow a 'b'"
                )
            else:
                return SimulationResult(
                    False, f"position {position}: invalid symbol {char!r}"
                )

        if self.stack:
            return SimulationResult(False, "not every 'a' has a matching 'b'")
        return SimulationResult(True, "input belongs to a^n b^n")


def main() -> None:
    """Run the simulator from the command line."""
    parser = argparse.ArgumentParser(
        description="Recognize strings in L = {a^n b^n | n >= 0}."
    )
    parser.add_argument("input", nargs="?", help="String to test (for example: aabb)")
    args = parser.parse_args()

    if args.input is not None:
        result = PDASimulator().simulate(args.input)
        print(f"{args.input!r} -> {'Accepted' if result.accepted else 'Rejected'}")
        print(result.reason)
        return

    for value in ("ab", "aabb", "aaabbb", "aab", "abb", "bbaa", ""):
        result = PDASimulator().simulate(value)
        print(f"{value!r} -> {'Accepted' if result.accepted else 'Rejected'}")


if __name__ == "__main__":
    main()
