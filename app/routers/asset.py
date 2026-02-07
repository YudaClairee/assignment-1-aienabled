import uuid
from sqlmodel import select
from fastapi import APIRouter, Depends, status

from app.models.database import Asset
from app.models.engine import get_db
from app.schema.assets import AssetCreate, AssetResponse
from app.utils.query_params import standard_params

asset_router = APIRouter(tags=["assets"])

@asset_router.get("/assets", status_code=status.HTTP_200_OK, response_model=list[AssetResponse])
def get_assets(params = Depends(standard_params), db = Depends(get_db)):
    stmt = select(Asset)
    result = db.exec(stmt)
    assets = result.all()
    return assets

@asset_router.post("/assets", status_code=status.HTTP_201_CREATED, response_model=AssetCreate)
def create_assets(body: AssetCreate, db = Depends(get_db)):
    new_asset = Asset(
        ticker=body.ticker,
        amount=body.amount,
        avg_price=body.avg_price,
        portfolio_id=body.portfolio_id
    )
    db.add(new_asset)
    db.commit()
    return new_asset

@asset_router.get("/assets/{asset_id}", status_code=status.HTTP_200_OK, response_model=AssetResponse)
def get_asset(asset_id: uuid.UUID, db = Depends(get_db)):
    stmt = select(Asset).where(Asset.id == asset_id)
    result = db.exec(stmt)
    asset = result.first()
    return asset