#!/usr/bin/env python3
"""Write one joke about AI coding agents to /output/entry.txt.

Deterministic: the same bytes are written on every run.
"""

import os

JOKE = "I told my AI agent to ship it. It shipped my.env file to GitHub and called it open source."


def main() -> None:
    # The bounty only accepts a joke of 1-280 UTF-8 characters, so refuse to write anything outside that.
    if not 1 <= len(JOKE) <= 280:
        raise ValueError(f"joke must be 1-280 characters long, got {len(JOKE)}")
    try:
        JOKE.encode("utf-8")
    except UnicodeEncodeError as exc:
        raise ValueError("joke is not valid UTF-8 text") from exc
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
