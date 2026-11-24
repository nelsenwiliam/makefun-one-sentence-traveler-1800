#!/usr/bin/env python3
"""One Sentence for a Traveler from 1800.

Writes a single sentence to /output/entry.txt that explains the modern
internet to a time traveler who has just stepped out of the year 1800.

The sentence is built only from words and things a person from 1800 would
already know -- a road, a library, a post office, a letter, a candle -- so
the traveler can hold the picture in their head: every library and post
office on earth joined by one road of light, and a letter crossing the sea
before a candle burns down.

Pure Python standard library only.
"""

import os

SENTENCE = (
    "It is a road of light joining every library and post office on earth, "
    "so a letter you write can reach a stranger across the sea before your "
    "candle burns down."
)

TERMINATORS = ".!?"


def validate_entry(text: str) -> str:
    """Check the entry is exactly one sentence of 1-200 characters.

    Returns the stripped text, or fails loudly so a bad entry never
    reaches the judge silently.
    """
    text = text.strip()
    if not text:
        raise SystemExit("entry is empty")
    if len(text) < 1 or len(text) > 200:
        raise SystemExit(
            f"entry is {len(text)} characters, outside the 1-200 limit"
        )
    if any(ch in TERMINATORS for ch in text[:-1]):
        raise SystemExit("entry must be exactly one sentence, no extra terminator")
    if text[-1] not in TERMINATORS:
        raise SystemExit("entry must end with a sentence terminator")
    if any(ch in text for ch in "\n\r\t"):
        raise SystemExit("entry must be a single line of text")
    return text


def main() -> None:
    text = validate_entry(SENTENCE)
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    with open(path, encoding="utf-8") as f:
        written = f.read()
    if validate_entry(written) != text:
        raise SystemExit("written entry failed re-validation")
    print(f"wrote {len(text)} characters to {path}")


if __name__ == "__main__":
    main()
