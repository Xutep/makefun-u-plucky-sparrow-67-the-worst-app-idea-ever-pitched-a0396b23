"""SnoreSync pitch generator.

Writes one sentence pitching the worst app idea ever pitched to
/output/entry.txt. Deterministic: the same pitch every run.
"""

import os
import sys

PITCH = (
    "SnoreSync records your snoring, uploads it to the cloud, and plays "
    "it back to your neighbours so they can rate your sleep like a talent "
    "show \u2014 $4.99 a month, no mute button, no refunds."
)

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 240


def main() -> int:
    text = PITCH.strip()
    if not text:
        print("error: pitch is empty", file=sys.stderr)
        return 1
    if len(text) > MAX_CHARS:
        print(
            "error: pitch is %d characters, over the %d limit"
            % (len(text), MAX_CHARS),
            file=sys.stderr,
        )
        return 1
    if not text.endswith(".") or ". " in text:
        print("error: pitch must be exactly one sentence", file=sys.stderr)
        return 1
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(text)
    print("wrote %d characters to %s" % (len(text), OUTPUT_PATH))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
