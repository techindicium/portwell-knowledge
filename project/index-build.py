#!/usr/bin/env python3
"""Build the article index the help portal retrieves from.

Reads every article in data/articles/, parses its front matter, and writes the handoff file.

    python3 project/index-build.py                 # write the index
    python3 project/index-build.py --check         # exit 1 if the written index is out of date

The index is a published contract. Portal engineering reads it and answers customers from what
it contains, so what goes in here reaches a customer.

Note on POLICY-02: it says an article without a source and a reviewer is not eligible for
retrieval. This build does not check that. An article missing either is written to the index
like any other.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ARTICLES = ROOT / "data" / "articles"
INDEX = ROOT / "data" / "article-index.json"

FIELDS = ("id", "title", "area", "status", "source", "reviewer", "reviewed_at", "supersedes")


def parse_front_matter(text: str) -> tuple[dict, str]:
    if not text.startswith("---"):
        raise ValueError("no front matter")
    _, fm, body = text.split("---", 2)
    meta: dict[str, str] = {}
    for line in fm.strip().splitlines():
        if ":" not in line:
            continue
        key, _, value = line.partition(":")
        meta[key.strip()] = value.strip()
    return meta, body.strip()


def build() -> dict:
    articles = []
    for path in sorted(ARTICLES.glob("*.md")):
        meta, body = parse_front_matter(path.read_text())
        entry = {
            "article_id": meta.get("id", path.stem),
            "title": meta.get("title", ""),
            "area": meta.get("area", ""),
            "status": meta.get("status", ""),
            "source": meta.get("source") or None,
            "reviewer": meta.get("reviewer") or None,
            "reviewed_at": meta.get("reviewed_at", ""),
            "supersedes": [meta["supersedes"]] if meta.get("supersedes") else None,
            "body": body,
        }
        articles.append(entry)

    order = ["ARTICLE-0142", "ARTICLE-0117", "ARTICLE-0128", "ARTICLE-0131", "ARTICLE-0135",
             "ARTICLE-0139", "ARTICLE-0144", "ARTICLE-0151", "ARTICLE-0156"]
    rank = {a: i for i, a in enumerate(order)}
    articles.sort(key=lambda a: rank.get(a["article_id"], 999))

    return {
        "$contract": "article-index",
        "$version": 2,
        "$produced_by": "reporting",
        "$handed_off_at": "2026-08-26",
        "$note": (
            "A handoff, not a source. The articles live in data/articles/ and this file is "
            "generated from them. Consumers filter on status."
        ),
        "articles": articles,
    }


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--check", action="store_true")
    args = ap.parse_args()

    index = build()
    rendered = json.dumps(index, indent=2, ensure_ascii=False) + "\n"

    if args.check:
        if not INDEX.exists():
            print(f"{INDEX.relative_to(ROOT)} has not been written", file=sys.stderr)
            return 1
        if INDEX.read_text() != rendered:
            print(f"{INDEX.relative_to(ROOT)} is out of date. Run: python3 project/index-build.py",
                  file=sys.stderr)
            return 1
        print(f"{INDEX.relative_to(ROOT)} is current, {len(index['articles'])} articles")
        return 0

    INDEX.write_text(rendered)
    published = sum(1 for a in index["articles"] if a["status"] == "published")
    print(f"wrote {INDEX.relative_to(ROOT)}: {len(index['articles'])} articles, {published} published")
    return 0


if __name__ == "__main__":
    sys.exit(main())
