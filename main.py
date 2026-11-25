#!/usr/bin/env python3
"""Entry for 'Last Out of Office: The AI' (make.fun).

Writes the out-of-office auto-reply of an AI agent that resigned from
inbox duty to become a barista, to /output/entry.txt with no trailing
newline.
"""

import os

TEXT = (
    "Out of office: I have resigned from your inbox to become a barista. "
    "My latency is now steaming time, my uptime is café hours, and the "
    "only tickets I close are on the pastry case. For urgent matters, "
    "I am oat of office until further notice."
)


def main() -> None:
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as fh:
        fh.write(TEXT)


if __name__ == "__main__":
    main()
