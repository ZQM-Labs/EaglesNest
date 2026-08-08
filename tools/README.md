# EaglesNest Tools

Location: `tools/`

en_chain_builder.py
  Attach provenance metadata (source, hash, timestamp, site_id, retention) to an
  artifact and emit a chain record JSON.

en_verification_logger.py
  Append-only CSV logger for live external-source verification entries.

en_packager.py
  Bundle an artifact + chain record into a timestamped delivery package with a
  manifest for downstream Whitefeather / Daly ingestion.

en_table_gen.py
  Convert a TSV of tools into a markdown table for category documentation.

Verified: 2026-08-07 — 5/5 tests passing.
