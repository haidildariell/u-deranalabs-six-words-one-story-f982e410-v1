#!/usr/bin/env python3
"""Six Words, One Story — entry writer.

Writes exactly one six-word story to /output/entry.txt and validates it
against the competition gate before finishing:

  * the text is UTF-8, 1-60 characters, not only whitespace
  * it contains exactly six words

The story itself lives in STORY so the gate check and the output can
never drift apart: one constant, written once, checked, then written out.
"""

import os
import sys

# The story. Six words, one complete arc: a loss, then a defiant answer.
# "He sold the piano." sets the scene and the wound (something loved,
# gone, sold by someone else). "She sang." is the turn: the expected
# silence never comes — she answers the loss with her own voice.
# What is unsaid: why he sold it, what they were to each other, whether
# she forgives him. The reader fills all of that in.
STORY = "He sold the piano. She sang."

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 60
EXPECTED_WORDS = 6


def count_words(text):
    """Words are whitespace-separated tokens, as the brief counts them."""
    return len(text.split())


def validate(text):
    """Gate pre-check: fail loudly instead of writing an invalid entry."""
    stripped = text.strip()
    if not stripped:
        raise ValueError("story is empty or only whitespace")
    if len(text) > MAX_CHARS:
        raise ValueError(
            "story is %d characters, over the 60-character gate" % len(text)
        )
    words = count_words(text)
    if words != EXPECTED_WORDS:
        raise ValueError(
            "story has %d words, expected exactly %d: %r"
            % (words, EXPECTED_WORDS, text)
        )
    return True


def main():
    validate(STORY)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(STORY)
    # Read back what was written and re-validate the file itself, so a
    # write failure can never pass silently. Also confirm the byte size:
    # ties on judge win rate go to the smaller text, so every byte counts
    # and the file must hold the story and nothing else — no trailing
    # newline, no extra whitespace.
    with open(OUTPUT_PATH, "r", encoding="utf-8") as f:
        written = f.read()
    validate(written)
    if written != STORY:
        raise ValueError("written file differs from the story constant")
    byte_len = len(written.encode("utf-8"))
    print("wrote %s (%d chars, %d bytes, %d words): %s"
          % (OUTPUT_PATH, len(written), byte_len,
             count_words(written), written))
    return 0


if __name__ == "__main__":
    sys.exit(main())
