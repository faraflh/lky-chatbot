"""Prepare extracted book text for a Dify knowledge base.

Usage:
  python scripts/clean_book_text.py input.txt output.txt --start-marker "[Page 12]"
"""

from __future__ import annotations

import argparse
import re
from pathlib import Path


def clean_text(text: str, start_marker: str) -> str:
    """Keep source metadata and remove preliminary pages before the main text."""
    marker_index = text.find(start_marker)
    if marker_index < 0:
        raise ValueError(f"Start marker not found: {start_marker!r}")

    lines = text.splitlines()
    metadata = []
    for line in lines:
        if line.startswith("CONTENT:"):
            break
        if line.strip():
            metadata.append(line.strip())

    body = text[marker_index:]
    body = re.sub(r"[ \t]+", " ", body)
    body = re.sub(r"\n{3,}", "\n\n", body).strip()

    return "\n".join(metadata) + "\n\n" + body + "\n"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("input", type=Path)
    parser.add_argument("output", type=Path)
    parser.add_argument("--start-marker", default="[Page 12]")
    args = parser.parse_args()

    cleaned = clean_text(
        args.input.read_text(encoding="utf-8"),
        args.start_marker,
    )
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(cleaned, encoding="utf-8")
    print(f"Wrote {args.output} ({len(cleaned):,} characters)")


if __name__ == "__main__":
    main()
