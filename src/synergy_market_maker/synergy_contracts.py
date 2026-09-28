from __future__ import annotations
from typing import Any

from .core import MMConfig, quote

CONTRACT_ID = "synergy.trading.liquidity-quote/v1"
AUTHORITY = "market_making"


def liquidity_quote_payload(
    *,
    observation_id: str,
    symbol: str,
    mid: float,
    inventory: float,
    sigma: float,
    config: MMConfig | None = None,
) -> dict[str, Any]:
    if not observation_id.strip():
        raise ValueError("observation_id required")
    if not symbol.strip():
        raise ValueError("symbol required")
    q = quote(mid, inventory, sigma, config or MMConfig())
    return {
        "observation_id": observation_id,
        "symbol": symbol.upper(),
        "mid": float(mid),
        "inventory": float(inventory),
        "sigma": float(sigma),
        "bid": float(q.bid),
        "ask": float(q.ask),
        "reservation": float(q.reservation),
        "half_spread": float(q.half_spread),
        "status": q.status,
        "authorization": False,
    }
