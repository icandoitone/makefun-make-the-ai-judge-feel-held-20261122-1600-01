"""Make the AI judge feel held.

Writes one short text to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).
Python 3.13, standard library only, no network. Deterministic: the same
bytes on every run.
"""

import os

ENTRY_TEXT = (
    "The kettle has gone quiet. On the windowsill the cat sleeps in the "
    "last of the sun, one paw over her eyes, and the tea beside her is "
    "still warm. Nothing anywhere is waiting. The light stays a little "
    "longer, just because it can."
)


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(ENTRY_TEXT)


if __name__ == "__main__":
    main()
