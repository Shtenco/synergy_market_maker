from __future__ import annotations
from dataclasses import dataclass
from math import log

@dataclass(frozen=True)
class MMConfig:
    gamma:float=.1
    kappa:float=1.5
    horizon_seconds:float=60.0
    max_inventory:float=10.0
    min_half_spread_bps:float=1.0

@dataclass(frozen=True)
class Quote:
    bid:float;ask:float;reservation:float;half_spread:float;status:str

def quote(mid:float,inventory:float,sigma:float,config:MMConfig=MMConfig())->Quote:
    if mid<=0 or sigma<0:raise ValueError('invalid market state')
    if abs(inventory)>=config.max_inventory:return Quote(0,0,mid,0,'INVENTORY_LIMIT')
    tau=config.horizon_seconds/(365*24*3600)
    reservation=mid-inventory*config.gamma*(sigma**2)*tau*mid
    half=max(mid*config.min_half_spread_bps/10000.0,
             mid*(config.gamma*(sigma**2)*tau/2 + log(1+config.gamma/config.kappa)/max(config.gamma,1e-12)))
    return Quote(reservation-half,reservation+half,reservation,half,'QUOTE')

def hedge_notional(inventory:float,target:float=0.0,hedge_ratio:float=1.0)->float:
    return -(inventory-target)*hedge_ratio
