"""One-star review of gravity, an everyday essential.

Deadpan complaint, one joke, turn in the last few words: gravity does
the cosmic heavy lifting flawlessly (oceans, planets), then fumbles
the one small job everyone actually notices — a phone, screen-first,
every single time. No exclamation marks, no winking, no second joke.
"""

import os

ENTRY = "Gravity: holds the oceans in place, yet cannot be trusted with a phone for five seconds."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
