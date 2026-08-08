"""EaglesNest verified tool table generator.

Reads a category-specific TSV of tools and emits a markdown table with
verification metadata for inclusion in category `.md` files.
"""

from __future__ import annotations

import argparse
from datetime import UTC, datetime
from pathlib import Path


def parse_tsv(path: Path) -> list[dict]:
    rows: list[dict] = []
    with path.open("r", encoding="utf-8") as f:
        header = None
        for line in f:
            line = line.rstrip("\n")
            if not line.strip() or line.startswith("#"):
                continue
            parts = line.split("\t")
            if header is None:
                header = parts
                continue
            rows.append(dict(zip(header, parts)))
    return rows


def render(category: str, rows: list[dict]) -> str:
    today = datetime.now(UTC).strftime("%Y-%m-%d")
    lines = [
        f"# {category} — {today} verifiable index",
        "",
        "| Tool | URL | Notes | verified |",
        "|------|-----|-------|----------|",
    ]
    for r in rows:
        lines.append(
            f"| {r.get('tool', '')} | {r.get('url', '')} | {r.get('notes', '')} | {r.get('verified', today)} |"
        )
    return "\n".join(lines) + "\n"


def main() -> int:
    ap = argparse.ArgumentParser(description="EaglesNest category table generator")
    ap.add_argument("--tsv", type=Path, required=True)
    ap.add_argument("--category", required=True)
    ap.add_argument("--out", type=Path, required=True)
    args = ap.parse_args()
    rows = parse_tsv(args.tsv)
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(render(args.category, rows), encoding="utf-8")
    print(f"table written: {args.out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
