# Scripts — Verified Downloaders, Parsers, Exporters

Naming: `<tool>_<action>_v<ver>_<YYYYMMDD>.py`

Required header:
    # VERIFIED: YYYY-MM-DD; SOURCE: authority
    # STATUS: live | degraded | dead

Required metadata block:
    # OBSERVABILITY_CHAIN:
    # source: <origin URL, dataset, or field observation ID>
    # collected: <ISO-8601 UTC timestamp>
    # verified: <live-check date and method>
    # hash: <SHA-256 of raw input>
    # retention: <storage path and expiry policy>
    # site_id: <Whitefeather | EaglesNest | Daly | cross-project>

Retention:
- Scripts under `EaglesNest/scripts/` with YYYYMMDD suffix are immutable once verified.
- Retire degraded scripts by renaming to `.dead/<YYYYMMDD>/` rather than deleting.

Cross-project sync:
- Verified scripts are mirrored to `Whitefeather/09_techint/scripts/` and `Daly/08_techint/scripts/` via weekly hash-checked sync.
