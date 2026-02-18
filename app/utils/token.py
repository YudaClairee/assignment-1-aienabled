import uuid

from sqlmodel import Session
from fastapi import Depends, HTTPException
from fastapi.security import HTTPBearer

from app.models.database import User
from app.models.engine import get_db
from app.utils.auth import validate_token

security = HTTPBearer()


def get_current_user(token=Depends(security), db: Session = Depends(get_db)):
    current_user = validate_token(token.credentials)
    if not current_user:
        raise HTTPException(401, "Invalid Token")
    # user = db.get(User, current_user.get("id"))
    user_id = current_user.get("id")
    if not user_id:
        raise HTTPException(401, "Invalid Token")

    user = db.get(User, uuid.UUID(user_id))
    if not user:
        raise HTTPException(400, "User not found!")

    return user
