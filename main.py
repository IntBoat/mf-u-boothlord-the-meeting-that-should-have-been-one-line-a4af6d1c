#!/usr/bin/env python3
"""The Meeting That Should Have Been One Line (make.fun).

Writes the entry -- a single original one-line text -- to
/output/entry.txt, where the sealed scorer reads it.
"""

import os

# The entry itself: exactly one sentence, written with no trailing newline.
ENTRY = 'The project is on track, the deadline moved to Friday, and the only reason we are all in this room is that nobody wanted to be the one to cancel it — so this sentence is the meeting.'


def write_entry():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


def main():
    write_entry()


if __name__ == "__main__":
    main()
