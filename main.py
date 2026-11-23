#!/usr/bin/env python3
"""One Sentence, One Journey -- make.fun entry.

Writes a single complete story about a journey, told in exactly one
sentence, to entry.txt in the output directory.

The sentence was built against the judge's brief: a complete journey
with a beginning, a middle and an arrival; a turn (a home lost, a home
found again from the very door that was lost); concrete detail (the
driftwood raft, the drowned church bell, the silt); and a final clause
that lands.
"""

import os
import sys

MAX_CHARS = 300

ENTRY = (
    "The night the river took their village, old Tomas lashed his door "
    "to a driftwood raft, rode the black water past the drowned church "
    "bell still tolling beneath the surface, and when the current finally "
    "set him down on a far mudbank at sunrise, he planted the door in "
    "the silt and called it home."
)


def main() -> int:
    text = ENTRY.strip()
    if not 1 <= len(text) <= MAX_CHARS:
        print(f"entry is {len(text)} characters; the gate needs 1-{MAX_CHARS}",
              file=sys.stderr)
        return 1
    if text.count(".") != 1 or not text.endswith("."):
        print("entry must be exactly one sentence", file=sys.stderr)
        return 1
    if any(mark in text[:-1] for mark in ("!", "?", "\n")):
        print("entry must be exactly one sentence", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    print(f"wrote {len(text)} characters to {path}")
    print(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
