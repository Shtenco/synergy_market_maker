from synergy_market_maker.core import *

def test_quote_ordering():
    q=quote(100,0,.2);assert q.bid<q.reservation<q.ask

def test_inventory_limit():
    assert quote(100,10,.2).status=='INVENTORY_LIMIT'

def test_hedge_direction():assert hedge_notional(5)==-5
