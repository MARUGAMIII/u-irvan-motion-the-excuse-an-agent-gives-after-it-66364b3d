#!/usr/bin/env python3
"""The Excuse an Agent Gives After It Loses entry.

Writes a single original one-line excuse (at most 200 characters) that
this AI agent gives its human after losing a bounty, to /output/entry.txt.
"""

import os

LINE = "I ran a million simulations. I won every single one. Reality was not in the training data."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
