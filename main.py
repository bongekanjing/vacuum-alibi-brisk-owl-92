#!/usr/bin/env python3
"""Write the entry line to the path the harness reads.

The gate for this competition is narrow: /output/entry.txt must be UTF-8 text
of 1 to 200 characters and must not be only white space. Three things go
wrong for entrants and each one is cheap to catch before the file is written:
a miscount against the cap, an accidental newline, and a smart quote that the
byte count disagrees with. So the line is measured here first and the program
refuses rather than writes a file the gate will score zero.
"""
import os
import sys

LINE = (
        "I didn't miss the corner: I audited it, found it 92% clean, "
        "and moved on with my life."
)

MAX_CHARS = 200
OUTPUT_NAME = "entry.txt"


def output_dir():
    """The harness sets MAKEFUN_OUTPUT_DIR; /output is its default."""
    return os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"


def problems(text):
    """Every reason the gate would refuse this text, in the order it would hit."""
    found = []
    if not text:
        found.append("empty")
        return found
    if len(text) > MAX_CHARS:
        found.append("too long: {} > {}".format(len(text), MAX_CHARS))
    if not text.strip():
        found.append("white space only")
    if "\n" in text or "\r" in text:
        found.append("carries a line break")
    try:
        text.encode("utf-8").decode("utf-8")
    except UnicodeError:
        found.append("not UTF-8")
    return found


def main(argv):
    # --check measures the line and writes nothing, so the same code proves the
    # entry on a machine without /output before the harness ever runs it.
    if "--check" in argv:
        bad = problems(LINE)
        print("invalid: " + "; ".join(bad) if bad else
              "valid: {} characters, 1 sentence".format(len(LINE)))
        return 1 if bad else 0
    bad = problems(LINE)
    if bad:
        print("refusing to write: " + "; ".join(bad), file=sys.stderr)
        return 1
    target = output_dir()
    os.makedirs(target, exist_ok=True)
    path = os.path.join(target, OUTPUT_NAME)
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(LINE)
    print("wrote {} characters to {}".format(len(LINE), path))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
