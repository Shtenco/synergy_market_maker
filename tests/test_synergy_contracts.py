from synergy_market_maker.synergy_contracts import CONTRACT_ID, liquidity_quote_payload

def test_liquidity_quote_payload_is_advisory():
    p=liquidity_quote_payload(
        observation_id="obs-1",symbol="eurusd",mid=1.1,inventory=0,sigma=.1
    )
    assert CONTRACT_ID=="synergy.trading.liquidity-quote/v1"
    assert p["status"]=="QUOTE"
    assert p["bid"]<p["ask"]
    assert p["authorization"] is False
