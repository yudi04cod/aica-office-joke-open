#!/usr/bin/env python3
"""Write the office-joke entry to /output/entry.txt.

Deterministic: the same single line is written on every run.
Standard library only.
"""

import os

JOKE = (
    "HR asked why I CC'd the office plant on every email \u2014 "
    "it's the only one here that listens, waters itself, "
    "and never replies all."
)


def validate(text: str) -> None:
    """Enforce the competition gate: 1-200 characters, not only whitespace."""
    if not (1 <= len(text) <= 200):
        raise ValueError(f"entry must be 1-200 chars, got {len(text)}")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")


def main() -> None:
    validate(JOKE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
