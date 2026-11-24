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


def main() -> None:
    text = SENTENCE.strip()
    if not text:
        raise SystemExit("entry is empty")
    if len(text) > 200:
        raise SystemExit(f"entry is {len(text)} characters, over the 200 limit")
    if text.count(".") != 1 or not text.endswith("."):
        raise SystemExit("entry must be exactly one sentence")
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    print(f"wrote {len(text)} characters to {path}")


if __name__ == "__main__":
    main()
