from __future__ import annotations
from fastapi import APIRouter, Depends
from pydantic import BaseModel
from ..core import MMConfig, hedge_notional, quote
from .models import Principal, Role
from .service import EnterpriseRuntime, principal_dependency, request_id_header

class QuoteRequest(BaseModel): mid:float; inventory:float; sigma:float; target_inventory:float=0.0; hedge_ratio:float=1.0

def build_product_router(runtime:EnterpriseRuntime)->APIRouter:
    router=APIRouter(prefix="/enterprise/v1/market-maker",tags=["enterprise-market-maker"])
    @router.post("/quote")
    async def make_quote(req:QuoteRequest, principal:Principal=Depends(principal_dependency(runtime,{Role.TRADER,Role.RISK})), request_id:str=Depends(request_id_header)):
        q=quote(req.mid,req.inventory,req.sigma,MMConfig());hedge=hedge_notional(req.inventory,req.target_inventory,req.hedge_ratio)
        result={**q.__dict__,"hedge_notional":hedge,"request_id":request_id}
        runtime.record(principal,action="market_maker.quote",request_id=request_id,payload={"status":q.status,"inventory":req.inventory,"reservation":q.reservation,"hedge_notional":hedge})
        return result
    return router
