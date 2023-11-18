from fastapi import APIRouter, status, HTTPException, Response, Depends
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from ..models import sa_models
from ..models.schemas import Token
from ..utilities import oauth2, utils
from .. import database

router = APIRouter(tags=['Authentication'])

@router.post('/login', response_model=Token.TokenOut)
def login(
    user_credentials: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(database.get_db)
):
    """
    Log in a user and return the access token.

    Parameters:
      user_credentials (OAuth2PasswordRequestForm): User credentials containing username (email) and password.
      db (Session): Database session.

    Returns:
      Token.TokenOut: Access token response.
    """
    user = db.query(sa_models.User).filter(sa_models.User.email == user_credentials.username).first()

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User not found")

    if not utils.verify(user_credentials.password, user.password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=f"Invalid Credentials")

    access_token = oauth2.create_access_token(data={"user_id": user.id, "admin": user.admin})

    return {"access_token": access_token, "token_type": "bearer"}
