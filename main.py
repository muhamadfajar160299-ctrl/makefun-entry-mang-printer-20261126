#!/usr/bin/env python3
"""Write the printer's one-line comeback to entry.txt.

The grader runs this program as an unprivileged user in a read-only copy
of the repository, so the entry is written ONLY to the directory named by
the MAKEFUN_OUTPUT_DIR environment variable (default "/output"). Nothing
is ever written next to this script.
"""

import os

# Output goes only to the directory named by MAKEFUN_OUTPUT_DIR.

ENTRY = (
    "I jammed on page 47 of 48. Not an error. A decision. "
    "You thumped me twice, so I'm keeping the last page."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
