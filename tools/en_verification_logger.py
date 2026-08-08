"""EaglesNest verification logger.

Append-only CSV logger for live external source verification.
"""

from __future__ import annotations

import argparse
import csv
from datetime import UTC, datetime
from pathlib import Path


def log_entry(
    tool: str,
    status: str,
    site_id: str,
    source_hash: str,
    retention_path: str,
    notes: str = "",
) -> dict:
    return {
        "timestamp": datetime.now(UTC).isoformat(),
        "tool": tool,
        "status": status,
        "site_id": site_id,
        "source_hash": source_hash,
        "retention_path": retention_path,
        "notes": notes,
    }


def main() -> int:
    ap = argparse.ArgumentParser(description="EaglesNest verification logger")
    ap.add_argument("--tool", required=True)
    ap.add_argument("--status", required=True, choices=["live", "degraded", "dead"])
    ap.add_argument("--site-id", required=True)
    ap.add_argument("--source-hash", default="")
    ap.add_argument("--retention-path", default="")
    ap.add_argument("--notes", default="")
    ap.add_argument("--out", type=Path, required=True)
    args = ap.parse_args()

    entry = log_entry(
        args.tool,
        args.status,
        args.site_id,
        args.source_hash,
        args.retention_path,
        args.notes,
    )
    args.out.parent.mkdir(parents=True, exist_ok=True)
    file_exists = args.out.exists() and args.out.stat().st_size > 0
    with args.out.open("a", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=list(entry.keys()))
        if not file_exists:
            writer.writeheader()
        writer.writerow(entry)
    print(f"logged: {args.tool} -> {args.status}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
