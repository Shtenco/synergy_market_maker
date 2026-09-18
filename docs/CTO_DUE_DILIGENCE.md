# CTO due diligence — SYNERGY Market Maker

Use case: Inventory-aware quoting and hedge sizing with explicit risk-control boundaries. Buyer: Market makers, exchanges, OTC desks and liquidity providers. Endpoint `/enterprise/v1/market-maker/quote`, roles **trader, risk**.

Implemented: deterministic quote/hedge core, tenant RBAC, request-ID audit, PostgreSQL/ClickHouse, metrics and deployment assets.

Evidence: **21 tests passed**; health smoke 80/80 200, local p95 **55.6 ms**. Boundary: no guarantee of spread capture, fills, inventory neutrality or profitability.