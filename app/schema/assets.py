import uuid
from pydantic import BaseModel

class AssetResponse(BaseModel):
    id: uuid.UUID
    ticker: str
    amount: float
    avg_price: float
    portfolio_id: uuid.UUID

class AssetCreate(BaseModel):
    ticker: str
    amount: float
    avg_price: float
    portfolio_id: uuid.UUID