from sqlalchemy.exc import IntegrityError
from sqlmodel import Session, select
from starlette.status import (
    HTTP_201_CREATED,
    HTTP_409_CONFLICT,
    HTTP_400_BAD_REQUEST,
    HTTP_200_OK,
    HTTP_401_UNAUTHORIZED,
)
from fastapi import APIRouter, Depends, HTTPException

from app.models.engine import get_db
from app.schema.auth import LoginUser, RegisterUser
from app.utils.auth import generate_token, hash_password, is_valid_password
from app.models.database import User

auth_router = APIRouter(prefix="/auth", tags=["Auth"])


@auth_router.post(
    "/register", status_code=HTTP_201_CREATED, response_model=RegisterUser
)
def register_user(body: RegisterUser, db: Session = Depends(get_db)):
    try:
        hashed_password = hash_password(body.password)
        new_user = User(name=body.name, email=body.email, password=hashed_password)
        db.add(new_user)
        db.commit()
    except IntegrityError as e:
        print(e)
        raise HTTPException(status_code=HTTP_409_CONFLICT, detail="User already exist")
    except Exception as e:
        print(e)
        raise HTTPException(status_code=HTTP_400_BAD_REQUEST, detail="Bad Request")

    return RegisterUser(name=body.name, email=body.email, password="")


@auth_router.post("/login", status_code=HTTP_200_OK)
def login_user(body: LoginUser, db: Session = Depends(get_db)):
    user = db.exec(select(User).where(User.email == body.email)).first()

    if not user:
        raise HTTPException(
            status_code=HTTP_401_UNAUTHORIZED, detail="Invalid Credentials"
        )

    if not is_valid_password(body.password, user.password):
        raise HTTPException(
            status_code=HTTP_401_UNAUTHORIZED, detail="Invalid Credentials"
        )

    token = generate_token({"id": str(user.id)})

    return {"Message": "Login Success", "token": token}
