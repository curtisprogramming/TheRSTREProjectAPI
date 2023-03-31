from jose import JWTError, jwt
from datetime import datetime, timedelta
from ..models import sa_models
from ..models.schemas import Token
from .. import database
from fastapi import Depends, status, HTTPException
from fastapi.security import OAuth2PasswordBearer
from ..config import settings
from sqlalchemy.orm import Session

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='login')

SECRET_KEY = settings.secret_key
ALGORITHM = settings.algorithm
ACCESS_TOKEN_EXPIRE_MINUTES = settings.access_token_expire_minutes  

def create_access_token(data: dict):

    #validates data
    Token.TokenData(**data)

    to_encode = data.copy()

    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

    return encoded_jwt

def verify_access_token(token: str, credentials_exception):

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])

        id = payload.get("user_id")
        admin = payload.get("admin")

        if id is None or admin is None:
            raise credentials_exception

        token_data = Token.TokenData(user_id=id, admin=admin)

    except JWTError:
        raise credentials_exception

    return token_data

def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(database.get_db)):
    
    credentials_exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, 
    detail=f"Could not validate credentials", headers={"WWW-Authenticate": "Bearer"})

    token = verify_access_token(token, credentials_exception)

    user = db.query(sa_models.User).filter(sa_models.User.id == token.user_id).first()

    if user == None:
        raise credentials_exception

    return user