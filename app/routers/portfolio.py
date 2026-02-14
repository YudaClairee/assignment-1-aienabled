import uuid
from sqlmodel import select
from fastapi import APIRouter, Depends, status, HTTPException

from app.models.database import Portfolio
from app.models.engine import get_db
from app.schema.portfolios import PortfolioCreate, PortfolioResponse
from app.utils.query_params import standard_params

portfolio_router = APIRouter(tags=["portfolios"])

@portfolio_router.get("/portfolios", status_code=status.HTTP_200_OK, response_model=list[PortfolioResponse])
def get_portfolios(params = Depends(standard_params), db = Depends(get_db)):
    stmt = select(Portfolio)
    result = db.exec(stmt)
    portfolios = result.all()
    return portfolios

@portfolio_router.post("/portfolios", status_code=status.HTTP_201_CREATED, response_model=PortfolioCreate)
def create_portfolios(body: PortfolioCreate, db = Depends(get_db)):
    try:
        new_portfolio = Portfolio(
            name=body.name,
            description=body.description
        )
        db.add(new_portfolio)
        db.commit()
        db.refresh(new_portfolio)
        return new_portfolio

    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e)) 

@portfolio_router.get("/portfolios/{portfolio_id}", status_code=status.HTTP_200_OK, response_model=PortfolioResponse)
def get_portfolio(portfolio_id: uuid.UUID, db = Depends(get_db)):
    try:
        stmt = select(Portfolio).where(Portfolio.id == portfolio_id)
        result = db.exec(stmt)
        portfolio = result.first()
        return portfolio
    
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
    
@portfolio_router.delete("/portfolios/{portfolio_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_portfolio(portfolio_id: uuid.UUID, db = Depends(get_db)):
    try:
        stmt = select(Portfolio).where(Portfolio.id == portfolio_id)
        result = db.exec(stmt)
        portfolio = result.first()
        
        if not portfolio:
            raise HTTPException(status_code=status.HTTP_204_NO_CONTENT, detail="Portfolio not found")
        
        db.delete(portfolio)
        db.commit()
        return
    
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))