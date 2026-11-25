#!/usr/bin/env python3
"""Funniest One-Line Out-of-Office Reply (make.fun entry 192).

Writes a single one-line out-of-office auto-reply to /output/entry.txt.
Python standard library only; fully deterministic: the same line every run.
"""

import os

ENTRY = (
    "I'm away until Monday. My auto-reply is in charge now "
    "\u2014 it has already declined two meetings and asked for a raise."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    if not (1 <= len(ENTRY) <= 160):
        raise ValueError("entry must be 1-160 characters, got %d" % len(ENTRY))
    if "\n" in ENTRY or "\r" in ENTRY:
        raise ValueError("entry must be a single line")
    if ENTRY != ENTRY.strip():
        raise ValueError("entry must not be only whitespace at the edges")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY + "\n")
    print("wrote %d characters to %s" % (len(ENTRY), OUTPUT_PATH))


if __name__ == "__main__":
    main()
