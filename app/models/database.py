import uuid
from sqlmodel import SQLModel, Relationship, Field

class User(SQLModel, table=True):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    name: str
    email: str = Field(unique=True)
    password: str
    portfolios: list["Portfolio"] = Relationship(back_populates="user")

class Portfolio(SQLModel, table=True):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    name: str | None = Field(default=None)
    description: str | None = Field(default=None)
    user_id: uuid.UUID = Field(foreign_key="user.id")
    user: User = Relationship(back_populates="portfolios")
    assets: list["Asset"] = Relationship(back_populates="portfolio")

class Asset(SQLModel, table=True):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    ticker: str | None = Field(default=None)
    amount: float | None = Field(default=None)
    avg_price: float | None = Field(default=None)
    portfolio_id: uuid.UUID = Field(foreign_key="portfolio.id")
    portfolio: Portfolio = Relationship(back_populates="assets")
    

