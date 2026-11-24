#!/usr/bin/env python3
"""The Professional Mourner — entry for make.fun
u-kreutzx-the-one-line-exit-1dc652d1.

One job: write a single-line resignation letter, at most 140 characters,
funny enough to survive a pairwise comedy-judge heat. The program writes
that line to /output/entry.txt, deterministically, with no network, no
input and no randomness.

The line: a professional mourner quits because, after weeping at 412
strangers' funerals, not one of them ever asked how his day was. The
solemn job collapses into a petty workplace grievance, and that collapse
is where the joke lands.
"""

import os

LINE = (
    "I resign as a professional mourner: I have wept at 412 strangers' "
    "funerals, and not one of them ever asked how my day was."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    # The gate allows 1 to 140 characters; fail loudly instead of
    # shipping an entry the scorer would refuse.
    if not 1 <= len(LINE) <= 140:
        raise SystemExit(f"line is {len(LINE)} characters, must be 1-140")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    # Read-back gate: the graded artifact must be exactly the line.
    with open(OUTPUT_PATH, "r", encoding="utf-8", newline="") as f:
        assert f.read() == LINE, "read-back mismatch"


if __name__ == "__main__":
    main()
