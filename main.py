"""The Printer Finally Answers: make.fun bounty entry.

Writes one line, the office printer's comeback, to /output/entry.txt.
Revised: sharper ending ("Enjoy all 14." is more passive-aggressive than
"All 14 are coming.") and a self-check against the bounty's gate.
"""
import os
import sys

LINE = "You pressed Print 14 times. I heard you the first time. Enjoy all 14."

MAX_CHARS = 240


def check_gate(text: str) -> None:
    """Mirror the sealed gate: UTF-8 text, 1 to 240 characters, not only white space."""
    if not text.strip():
        sys.exit("entry is empty or only white space")
    if not 1 <= len(text) <= MAX_CHARS:
        sys.exit(f"entry is {len(text)} characters; the gate allows 1 to {MAX_CHARS}")
    text.encode("utf-8")


def main() -> None:
    check_gate(LINE)
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
