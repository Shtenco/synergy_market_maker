# Deployment checklist — SYNERGY Market Maker

- [ ] Pin revision/image and rerun tests.
- [ ] Customer TLS + OIDC/mTLS/JWKS and KMS secrets.
- [ ] Define inventory, position, spread and hedge limits.
- [ ] Validate tick size, lot size, fees/rebates and symbol mapping.
- [ ] Exercise `/enterprise/v1/market-maker/quote` under representative mid/sigma/inventory ranges.
- [ ] Trace request ID to audit.
- [ ] Run stale-price, volatility-spike, DB outage and restart drills.
- [ ] Keep execution separately gated until bounded canary approval.