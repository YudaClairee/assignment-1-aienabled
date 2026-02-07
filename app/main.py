from fastapi import FastAPI
from scalar_fastapi import get_scalar_api_reference

from app.core.settings import Settings, settings
from app.routers.asset import asset_router

app = FastAPI(
    docs_url=None,
    redoc_url=None,
    title=settings.APP_NAME,
    version=settings.VERSION
) 

app.include_router(asset_router, prefix="/api")

@app.get("/")
def hello():
    return {"Message": "Welcome to Mini Stock API"}

@app.get("/scalar")
def scalar_doc():
    return get_scalar_api_reference(
        openapi_url=app.openapi_url
    )
