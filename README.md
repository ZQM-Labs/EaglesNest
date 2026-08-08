# EaglesNest — Global Intelligence Observatory
Close upstream observability source for Whitefeather and Daly.
Global public observability platform across full INT taxonomy.

Cross-project index: `C:\Users\zqmco\INT_TOOLKIT_INDEX.md`

## Categories
- GEOINT — geospatial/imagery/terrain
- OSINT — open-source media/government/corporate/cyber
- SIGINT — RF/spectrum, legal/local only
- Field — mobile/GPS/offline collection
- CYBINT — cyber infrastructure/threat intel
- HUMINT — observer notes, behavior, ethics/consent required
- MASINT — acoustic/thermal/radar/telemetry signatures
- FININT — financial registries, blockchain, trade
- TECHINT — hardware/firmware/processes
- MEDINT/BIOINT — medical/biological environmental sensors
- IMINT — exterior/roof/antenna imagery
- ACINT — acoustic diagnostics
- RADINT — local RF interference
- SOCINT — social-media public context
- GEOFININT — financial/geospatial linkage

## Tooling surface
- `scripts.md` — verified downloaders/parsers/exporters
- `verification.md` — live external source verification log
- Per-category `.md` files — verified tool tables with source + date + status

## Observability chain
Every artifact emitted from this project must carry:
- `source:` — origin URL, dataset name, or field observation ID
- `collected:` — ISO-8601 UTC timestamp
- `verified:` — live-check date and method
- `hash:` — SHA-256 of raw input
- `retention:` — storage location and expiry policy

## Governance
- Open to global contributors.
- No Sierra Club restriction; ownership-independent.
- Ethical/legal compliance is per-jurisdiction; contributors must validate local law before collection.
- Active adversarial collection requires explicit authorization scoped to target + method + retention.

## Integration: zqm-intel-platforms
This repo vendors `zqm-intel-platforms>=0.1.0` as a dependency. Use the shared SIEM/OSINT/CTI wrappers for Splunk HEC, Loki, and Windows-telemetry export defined in that package.
