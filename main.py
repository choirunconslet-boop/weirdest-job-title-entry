"""Weirdest Job Title entry: writes one job title to /output/entry.txt."""

import os

TITLE = "Senior Vice President of Apologizing to Geese"

# Gate: entry must be UTF-8 text of 1 to 60 characters, not only whitespace.
assert 1 <= len(TITLE) <= 60 and TITLE.strip(), "title violates the 1-60 char gate"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TITLE)


if __name__ == "__main__":
    main()
