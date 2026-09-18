# SYNERGY Market Maker

> **Inventory-aware quoting and hedge sizing with explicit risk-control boundaries**

**Enterprise v2.0.0** · FastAPI/OpenAPI · Docker/Compose · RBAC/JWT · PostgreSQL/ClickHouse audit

**Designed for:** Market makers, exchanges, OTC desks and liquidity providers  
**Primary endpoint:** `POST /enterprise/v1/market-maker/quote`

> [!IMPORTANT]
> Quoting/risk infrastructure only. No guarantee of spread capture, fills or profitability; live execution remains separately controlled.

## Verification
**21 tests passed** · health smoke **80/80 200** · local p95 **55.6 ms** (~637 req/s). Health smoke only.

## Quick start
```bash
pip install -e '.[dev,enterprise]'
pytest -q
python -m synergy_market_maker.api
```

## CTO package
[Due diligence](docs/CTO_DUE_DILIGENCE.md) · [Architecture](docs/ARCHITECTURE_DIAGRAMS.md) · [API](docs/API_EXAMPLES.md) · [Security](SECURITY.md) · [Benchmarks](docs/BENCHMARKS_AND_ACCEPTANCE.md) · [SLA/SLO](docs/SLA_SLO.md) · [Deployment](docs/DEPLOYMENT_CHECKLIST.md) · [Pilot](docs/CUSTOMER_PILOT.md)
