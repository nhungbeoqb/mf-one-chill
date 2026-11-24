#!/usr/bin/env python3
"""One Line, One Chill entry.

Writes one original horror sentence (under 200 characters) to
/output/entry.txt. Python 3 standard library only; deterministic output.
"""

import os

LINE = (
    "The dentist pulled my wisdom tooth, held it to the light, "
    "and went pale: curled inside the root was a tiny, perfect "
    "fingerprint \u2014 and it wasn't mine."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
