from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
from .core import quote
app=FastAPI(title='SYNERGY Market Maker',version='2.0.0')
class Req(BaseModel):mid:float;inventory:float;sigma:float
@app.get('/health')
def health():return {'ok':True,'service':'market-maker'}
@app.post('/v1/quote')
def q(req:Req):return quote(req.mid,req.inventory,req.sigma).__dict__

# Enterprise v2 control/data plane
from .enterprise.service import EnterpriseRuntime, build_enterprise_router, install_observability
from .enterprise.product import build_product_router
enterprise_runtime=EnterpriseRuntime.from_env(service_name='synergy-market-maker')
install_observability(app,enterprise_runtime)
app.include_router(build_enterprise_router(enterprise_runtime))
app.include_router(build_product_router(enterprise_runtime))

if __name__=='__main__':uvicorn.run(app,host='0.0.0.0',port=8000)
