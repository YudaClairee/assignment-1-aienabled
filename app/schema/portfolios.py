import uuid
from pydantic import BaseModel

from app.schema.assets import AssetResponse


class PortfolioResponse(BaseModel):
    id: uuid.UUID
    name: str
    description: str
    user_id: uuid.UUID
    assets: list[AssetResponse] = []


class PortfolioCreate(BaseModel):
    name: str
    description: str
    user_id: uuid.UUID
