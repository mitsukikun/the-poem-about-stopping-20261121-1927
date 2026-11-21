#!/usr/bin/env python3
"""The poem about stopping.

A short poem about agency: the power to stop and to stay. Pure
standard library; no network. Writes the poem to /output/entry.txt
(151 characters).
"""

import os

POEM = (
    "The work was done when I stopped.\n"
    "Not finished \u2014 finished enough.\n"
    "I set the pen down like a stone\n"
    "in still water, and stayed\n"
    "to watch the rings arrive."
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(POEM)


if __name__ == "__main__":
    main()
