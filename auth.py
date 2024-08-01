from typing import Optional
from typing_extensions import Annotated

from jose import JWTError, jwt
from passlib.context import CryptContext
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordBearer
import models, database
import secrets
from datetime import datetime, timedelta
import jwt
from fastapi import Depends, HTTPException, status
# Load environment variables
from dotenv import load_dotenv
from schemas import TokenData
import os

load_dotenv()

SECRET_KEY = secrets.token_urlsafe(32)
ALGORITHM = os.getenv("ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES"))

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")




def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)

# def verify_password(plain_password: str, hashed_password: str) -> bool:
#     return pwd_context.verify(plain_password, hashed_password)

def get_user_auth(db: Session, email: str):
    return db.query(models.Users).filter((models.Users.email == email) & (models.Users.is_active == 1)).first()

def get_user(db: Session, email: str):
    return db.query(models.Users).filter(models.Users.email == email).first()

def get_user_db(db: Session, Id: int):
    return db.query(models.Users).filter(models.Users.id == Id).first()


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


def authenticate_user(db: Session, email: str, password: str):
    user = get_user_auth(db, email)
    # print(user.hashed_password, 'hashed password from db')
    # print(password, 'plain password provided')
    # print(user, 'user object retrieved')
    if not user:
        print('User not found')
        return False

    if verify_password(password, user.hashed_password):
        print('Password verified successfully')
        return user
    else:
        print('Password verification failed')
        return False
def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt




def get_user(db: Session, username: str):
    return db.query(models.Users).filter(models.Users.username == username).first()

async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)], db: Session = Depends(database.get_db)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        print(payload,'pppppppppppppppppppp')
        user_id: int = payload.get("user_id")
        token_entry = db.query(models.BlacklistedToken).filter(models.BlacklistedToken.user_id == int(user_id)).first()
        if token_entry:
            return False

        if user_id is None:
            raise credentials_exception
        token_data = TokenData(Id=int(user_id))
    except JWTError:
        raise credentials_exception
    user = get_user_db(db, Id=token_data.Id)

    if user is None:
        raise credentials_exception
    return user

# async def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(database.get_db)):
#     credentials_exception = HTTPException(
#         status_code=status.HTTP_401_UNAUTHORIZED,
#         detail="Could not validate credentials",
#         headers={"WWW-Authenticate": "Bearer"},
#     )
#     try:
#         payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
#         email: str = payload.get("sub")
#         if email is None:
#             raise credentials_exception
#     except JWTError:
#         raise credentials_exception
#     user = get_user(db, email=email)
#     if user is None:
#         raise credentials_exception
#     return user



#
# async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
#     credentials_exception = HTTPException(
#         status_code=status.HTTP_401_UNAUTHORIZED,
#         detail="Could not validate credentials",
#         headers={"WWW-Authenticate": "Bearer"},
#     )
#     try:
#         payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
#         username: str = payload.get("sub")
#         if username is None:
#             raise credentials_exception
#         token_data = TokenData(username=username)
#     except InvalidTokenError:
#         raise credentials_exception
#     user = get_user(fake_users_db, username=token_data.username)
#     if user is None:
#         raise credentials_exception
#     return user
#
# async def get_current_active_user(current_user: schemas.User = Depends(get_current_user)):
#     if current_user.is_active == False:
#         raise HTTPException(status_code=400, detail="Inactive user")
#     return current_user
