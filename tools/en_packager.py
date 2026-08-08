"""EaglesNest evidentiary packager.

Bundles an artifact + its chain record into a timestamped delivery package
with manifest.json for downstream Whitefeather/Daly ingestion.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from datetime import UTC, datetime
from pathlib import Path


def sha256_of(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            h.update(chunk)
    return h.hexdigest()


def package(artifact: Path, chain: Path, out_dir: Path, package_id: str) -> Path:
    out_dir.mkdir(parents=True, exist_ok=True)
    # Minimal tar-like packaging via file concatenation is avoided; write manifest instead.
    manifest = {
        "package_id": package_id,
        "created": datetime.now(UTC).isoformat(),
        "artifact": str(artifact),
        "artifact_hash": sha256_of(artifact),
        "chain": str(chain),
        "chain_hash": sha256_of(chain),
    }
    manifest_path = out_dir / f"{package_id}.manifest.json"
    manifest_path.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    print(f"package manifest: {manifest_path}")
    return manifest_path


def main() -> int:
    ap = argparse.ArgumentParser(description="EaglesNest evidentiary packager")
    ap.add_argument("--artifact", type=Path, required=True)
    ap.add_argument("--chain", type=Path, required=True)
    ap.add_argument("--out-dir", type=Path, required=True)
    ap.add_argument("--package-id", required=True)
    args = ap.parse_args()
    if not args.artifact.exists() or not args.chain.exists():
        raise SystemExit("artifact or chain missing")
    package(args.artifact, args.chain, args.out_dir, args.package_id)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
