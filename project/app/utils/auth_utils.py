from jose import JWTError,jwt
from passlib.context import CryptContext
from app.models.users import Users
from datetime import datetime, timedelta
from fastapi import Depends, HTTPException, status
from typing import Annotated, Union
from fastapi.security import OAuth2PasswordBearer


SECRET_KEY = 'be0fa35cc4931bfa08e58cb5879b1bf753f4271ac282cdb33631323887400f50'
ALGORITHM = 'HS256'

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def get_password_hash(password):
    return pwd_context.hash(password)

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


async def authenticate_user(username: str, password: str)-> Union[Users, bool]:
    user = await get_user(username)
    if not user:
        return False
    if not verify_password(password, user.password):
        return False
    return user


async def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


async def get_user(username: str) -> Users | None:
    print("username",username)
    user = await Users.get(user_name=username)
    print("user",user.password)
    return user


    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
       
    except JWTError:
        raise credentials_exception
    user = await get_user()
    if user is None:
        raise credentials_exception
    return user