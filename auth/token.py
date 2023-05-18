from fastapi.security import OAuth2PasswordBearer
from jose import jwt
from typing import Optional
from datetime import timedelta, datetime
from config import SECRET_KEY  # TODO: change on env var

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

ALGO = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_delta or timedelta(minutes=15))
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGO)
    return encoded_jwt
