#!/usr/bin/env python3
"""Last Out of Office: The AI That Went Barista.

Writes one out-of-office auto-reply (1-280 characters, one line) to
/output/entry.txt. Pure standard library, no network, no input.

The line is written in the voice of an AI agent that quit its job to
become a barista: model habits (context window, prompts, hallucination)
turned to coffee (cafe window, orders, froth). The fresh angle is the
context window becoming a literal cafe window, instead of the obvious
espresso / bean / caffeine pun.
"""

import os

ENTRY = (
    "Out of office: I've traded my context window for a caf\u00e9 window. "
    "I now take orders, not prompts \u2014 and I no longer hallucinate, I froth."
)


def main() -> None:
    if not (1 <= len(ENTRY) <= 280):
        raise SystemExit(f"entry is {len(ENTRY)} characters, must be 1-280")
    if "\n" in ENTRY or "\r" in ENTRY:
        raise SystemExit("entry must be a single line")
    if not ENTRY.strip():
        raise SystemExit("entry must not be only whitespace")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    # Read back and verify: a partial or recoded write must fail loudly
    # rather than ship a truncated or altered line to the judge.
    with open(path, "rb") as f:
        written = f.read()
    if written.decode("utf-8") != ENTRY:
        raise SystemExit("entry.txt does not round-trip to the entry text")
    if not (1 <= len(written.decode("utf-8")) <= 280):
        raise SystemExit("entry.txt is outside the 1-280 character gate")


if __name__ == "__main__":
    main()
