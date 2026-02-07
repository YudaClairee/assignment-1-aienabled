from fastapi import APIRouter, Depends, status

from app.utils.query_params import standard_params

asset_router = APIRouter(tags=["assets"])

@asset_router.get("/assets", status_code=status.HTTP_200_OK)
def get_assets(params = Depends(standard_params)):
    return {"params": params}