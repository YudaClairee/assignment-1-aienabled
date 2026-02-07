import uuid
from sqlmodel import SQLModel, Relationship, Field

class Portfolio(SQLModel, table=True):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    name: str
    description: str | None = None
    assets: list["Asset"] = Relationship(back_populates="portfolio")

class Asset(SQLModel, table=True):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    ticker: str  
    amount: float
    avg_price: float
    portfolio_id: uuid.UUID = Field(foreign_key="portfolio.id")
    portfolio: Portfolio = Relationship(back_populates="assets")

