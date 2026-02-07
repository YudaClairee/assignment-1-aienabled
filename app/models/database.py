import uuid
from sqlmodel import SQLModel, Relationship, Field

class Portfolio(SQLModel, table=True):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    name: str | None = Field(default=None) 
    description: str | None = Field(default=None) 
    assets: list["Asset"] | None = Relationship(back_populates="portfolio")

class Asset(SQLModel, table=True):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    ticker: str | None = Field(default=None) 
    amount: float | None = Field(default=None) 
    avg_price: float | None = Field(default=None) 
    portfolio_id: uuid.UUID = Field(foreign_key="portfolio.id")
    portfolio: Portfolio = Relationship(back_populates="assets")

