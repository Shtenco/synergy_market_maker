# API examples — SYNERGY Market Maker

`POST /enterprise/v1/market-maker/quote` — roles **trader, risk**.

```json
{"mid":60000,"inventory":2,"sigma":0.03,"target_inventory":0,"hedge_ratio":1.0}
```

Expected: `bid`, `ask`, `reservation`, `hedge_notional`, `request_id`. Canonical schema: `/docs`.