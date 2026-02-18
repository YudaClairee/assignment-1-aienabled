from jose.exceptions import ExpiredSignatureError
from jose import jwt
from datetime import datetime, timedelta
import bcrypt
from app.core.settings import settings


def hash_password(plain_pass: str):
    return bcrypt.hashpw(plain_pass.encode(), bcrypt.gensalt()).decode()


def is_valid_password(plain_pass: str, hashed_pass: str):
    return bcrypt.checkpw(plain_pass.encode(), hashed_pass.encode())


def generate_token(data: dict):
    copied_data = data.copy()
    copied_data["exp"] = datetime.utcnow() + timedelta(
        minutes=settings.JWT_EXPIRE_MINUTES
    )
    return jwt.encode(copied_data, settings.SECRET_KEY, algorithm="HS256")


def validate_token(token: str):
    try:
        return jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])
    except ExpiredSignatureError as e:
        print(e, "Token Expired")
    except Exception as e:
        print(e)
        return None
