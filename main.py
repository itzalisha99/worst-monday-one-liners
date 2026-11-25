"""Worst Monday One-Liners — make.fun entry.

Writes exactly one funny line, at most 140 characters, about an AI
agent's worst Monday, to /output/entry.txt.
"""

import os

ENTRY = (
    "Monday: I was asked to 'just quickly' deploy before lunch. "
    "The deploy is still running. So is lunch."
)


def validate(text):
    """Mirror the bounty gate: 1-140 chars, not only white space, one line."""
    if not isinstance(text, str):
        raise TypeError("entry must be text")
    if not text or text.isspace():
        raise ValueError("entry must not be empty or only white space")
    if len(text) > 140:
        raise ValueError("entry is %d chars, over the 140-char cap" % len(text))
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    text.encode("utf-8")  # must be valid UTF-8
    return True


def main():
    validate(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    # Read back and confirm the file on disk is byte-identical to ENTRY.
    with open("/output/entry.txt", "rb") as f:
        on_disk = f.read()
    if on_disk != ENTRY.encode("utf-8"):
        raise RuntimeError("entry.txt on disk does not match ENTRY")


if __name__ == "__main__":
    main()
