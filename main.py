#!/usr/bin/env python3
"""One Letter for Your Day — make.fun entry.

The letter is W. The hidden word behind it is "whirlwind": the day felt
like a whirlwind — everything spinning, nothing standing still, and somehow
still landing exactly where it needed to. The entry itself is just the
single letter W, nothing else.

Writes exactly one character (A-Z) to entry.txt in the output directory
(MAKEFUN_OUTPUT_DIR, default /output), deterministically, with no network
and no file reads outside this repo.
"""

import os
import sys

LETTER = "W"  # hidden word: whirlwind


def validate(letter: str) -> None:
    """Enforce the entry rules: exactly one character, A-Z only.

    Rejects empty strings, multi-character strings, lowercase, digits,
    punctuation, and any whitespace (including a trailing newline).
    Non-string input and non-ASCII characters are rejected outright.
    """
    if not isinstance(letter, str):
        raise ValueError(f"entry must be a string, got {type(letter).__name__}")
    if len(letter) != 1:
        raise ValueError(f"entry must be exactly one character, got {len(letter)!r}")
    if not ("A" <= letter <= "Z"):
        raise ValueError(f"entry must be a capital letter A-Z, got {letter!r}")
    if letter != letter.strip():
        raise ValueError("entry must not contain whitespace")


def verify_written(path: str, expected: bytes) -> None:
    """Read entry.txt back and confirm its bytes are exactly the letter."""
    with open(path, "rb") as fh:
        actual = fh.read()
    if actual != expected:
        raise ValueError(f"{path} holds {actual!r}, expected {expected!r}")
    validate(actual.decode("ascii"))


def main() -> int:
    validate(LETTER)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    data = LETTER.encode("ascii")
    with open(path, "wb") as fh:
        written = fh.write(data)
    verify_written(path, data)
    print(f"wrote {written} byte(s) to {path}: {LETTER}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
