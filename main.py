"""Write one office joke to /output/entry.txt.

The entry is a single line of office comedy, at most 200 characters.
"""

import os
from pathlib import Path

JOKE = "Our team building exercise was replying-all to an email that said 'please stop replying-all.'"


def resolve_output_dir():
    for key in ("MAKEFUN_OUTPUT_DIR", "OUTPUT_DIR"):
        out = os.environ.get(key)
        if out and out.strip():
            return Path(out.strip())
    return Path("/output")


def main():
    if not 1 <= len(JOKE) <= 200:
        raise ValueError("joke must be 1 to 200 characters")
    if JOKE.strip() == "" or "\n" in JOKE:
        raise ValueError("joke must be a single non-blank line")
    out_dir = resolve_output_dir()
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(JOKE, encoding="utf-8")


if __name__ == "__main__":
    main()
