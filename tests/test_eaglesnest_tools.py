from pathlib import Path

from en_chain_builder import build_chain, sha256_of
from en_packager import package
from en_table_gen import parse_tsv, render
from en_verification_logger import log_entry


def test_sha256_of(tmp_path: Path) -> None:
    p = tmp_path / "x.txt"
    p.write_text("x", encoding="utf-8")
    assert len(sha256_of(p)) == 64


def test_build_chain(tmp_path: Path) -> None:
    artifact = tmp_path / "a.txt"
    artifact.write_text("sample", encoding="utf-8")
    chain = build_chain(artifact, "source", "site", "ret", "verified")
    assert chain["source"] == "source"
    assert len(chain["hash"]) == 64


def test_package(tmp_path: Path) -> None:
    artifact = tmp_path / "a.txt"
    chain = tmp_path / "c.json"
    artifact.write_text("sample", encoding="utf-8")
    chain.write_text("{}", encoding="utf-8")
    out = package(artifact, chain, tmp_path, "pkg-001")
    assert out.exists()
    assert out.name == "pkg-001.manifest.json"


def test_parse_and_render_tsv(tmp_path: Path) -> None:
    tsv = tmp_path / "t.tsv"
    tsv.write_text(
        "tool\turl\tnotes\tverified\nGEE\thttps://earthengine.google.com\tEO\ttoday\n",
        encoding="utf-8",
    )
    rows = parse_tsv(tsv)
    assert rows[0]["tool"] == "GEE"
    rendered = render("GEOINT", rows)
    assert "GEOINT" in rendered
    assert "| GEOINT" in rendered or "# GEOINT" in rendered


def test_log_entry() -> None:
    entry = log_entry("t", "live", "s", "h", "r")
    assert entry["status"] == "live"
    assert entry["tool"] == "t"
