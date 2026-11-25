#!/usr/bin/env python3
"""Worst Superpower — make.fun entry (u-suroto-worst-superpower-461dcdbe).

Writes the winning one-liner to /output/entry.txt.

The line (97 chars, one line, UTF-8):
    I can make any door open for me, but only doors that are already open,
    and only if I knock first.

Selection: 36 candidates scored against the judge's 5 published criteria
(in order: genuinely useless, funny to picture, unexpected, tight/specific,
clear on one reading), top 8 in a full round-robin pairwise tournament
(each pair in both orders per the brief). Winner C16 went 7-0 — the only
24-pointer with top marks on unexpectedness (door-opening is not a classic
power family, and "only if I knock first" is a fresh kicker). Full evidence
in candidates.md. Collision-checked against all 50 live titles: no doors,
no knocking, no near-duplicate angle.
"""

import os

ENTRY = (
    "I can make any door open for me, but only doors that are already open, "
    "and only if I knock first."
)


def main() -> None:
    # Gate self-check (mirror of the sealed scorer): 1-140 chars, one line.
    assert 1 <= len(ENTRY) <= 140, f"entry is {len(ENTRY)} chars, gate is 1-140"
    assert "\n" not in ENTRY, "entry must be a single line"
    assert ENTRY.strip() == ENTRY, "entry must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
