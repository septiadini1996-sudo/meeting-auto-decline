#!/usr/bin/env python3
"""Writes one funny single-line excuse for skipping a pointless meeting."""
import os

EXCUSE = "Auto-decline: this meeting overlaps the meeting about this meeting."

def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(EXCUSE)

if __name__ == "__main__":
    main()
