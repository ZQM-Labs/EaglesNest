# Verification Checklist — Global Observatory

## Live checks
- [ ] GEE NGO tier eligibility confirmed
- [ ] EPA ECHO workflow validated end-to-end
- [ ] EO Browser / Copernicus bulk download tested
- [ ] FOIA request templates drafted
- [ ] Overpass Turbo query library built for land-use features
- [ ] Sentinel-2 download script with cloud mask verified live
- [ ] WebODM photogrammetry test completed
- [ ] Record retention schedule drafted
- [ ] Every external API/portal verified live with timestamp
- [ ] Observability chain metadata validated for all exported artifacts
- [ ] Cross-project sync to Whitefeather + Daly verified weekly
- [ ] Provenance hash chain from source → collection → export verified

## Log format
`tool,date,status,site_id,source_hash,retention_path,notes`

## Log file
`verification/verified_tools_<YYYYMMDD>.csv`
