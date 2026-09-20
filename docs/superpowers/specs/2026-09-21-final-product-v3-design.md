# Market Maker V3 Final Product Design

**Version:** 3.0.0  
**Branch:** `production/v3.0.0`  
**Status:** architecture specification for human review

## Goal
Convert Market Maker from a quote formula endpoint into a market-making control product with authoritative instrument policy, inventory state, market freshness, quote sessions, halt logic and hedge intents.

## Current gap
The current endpoint constructs default MMConfig in code and trusts caller-supplied inventory/mid/sigma. No inventory lifecycle, market snapshot identity, quote TTL or halt state is persisted.

## Durable resources
- InstrumentConfig
- MarketMakingPolicy
- InventoryState
- MarketSnapshot
- QuoteSession
- QuoteDecision
- HedgeIntent
- HaltState

## Core invariants
1. Production policy is server-side and versioned.
2. Inventory is authoritative and persisted.
3. Every quote references policy version + inventory version + market snapshot.
4. Stale market snapshot blocks quoting.
5. Tick size and lot size are enforced.
6. Quote TTL is explicit.
7. Persistent volatility/inventory/manual halts override quote generation.
8. HedgeIntent is not equal to executed hedge; execution is delegated to TradeMux or external adapter.
9. No endpoint promises spread capture or profitability.

## V3 API
- `PUT /enterprise/v3/instruments/{id}/policy`
- `POST /enterprise/v3/instruments/{id}/market-snapshots`
- `POST /enterprise/v3/instruments/{id}/inventory`
- `POST /enterprise/v3/quote-sessions`
- `GET /enterprise/v3/quote-sessions/{id}`
- `POST /enterprise/v3/quote-sessions/{id}/hedge`
- `POST /enterprise/v3/instruments/{id}/halt`
- `POST /enterprise/v3/instruments/{id}/resume`

## Persistence
PostgreSQL:
- instrument_configs
- market_making_policies
- inventory_states
- market_snapshots
- quote_sessions
- quote_decisions
- hedge_intents
- halt_states
- idempotency_keys
- audit_events

## Acceptance gates
- stale snapshot blocks quote;
- inventory state survives restart;
- tick/lot rounding deterministic;
- halt persists across restart;
- hedge intent references quote session;
- policy cannot be overridden by trader request;
- tenant isolation;
- DB outage -> readiness 503;
- V2 tests remain green.
