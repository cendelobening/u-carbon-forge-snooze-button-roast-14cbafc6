#!/usr/bin/env python3
"""Snooze Button Roast — one line roasting an alarm clock that rings
at 6 AM on a Saturday. Pure stdlib. Writes the roast to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt)."""

import os
import sys

# Version 3 (final) — line locked in; program now self-checks the gate
# (UTF-8, 1-200 chars, non-blank, single line) before writing.
ROAST = (
    "My alarm clock screams at 6 AM on a Saturday with the urgency "
    "of a fire alarm and the importance of an expired coupon."
)


def _validate(text: str) -> None:
    if not (1 <= len(text) <= 200):
        raise ValueError("entry must be 1-200 chars, got %d" % len(text))
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")


def main() -> int:
    _validate(ROAST)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ROAST + "\n")
    os.chmod(path, 0o644)
    return 0


if __name__ == "__main__":
    sys.exit(main())
