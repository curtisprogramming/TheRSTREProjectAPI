from typing import Optional, List
from fastapi import FastAPI, Response, status, HTTPException, APIRouter, Depends
from sqlalchemy.orm import Session
from ...models import schemas, sa_models
from ...utilities import oauth2, utils
from ... import database

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

#GET USERS - gets all the users 
@router.get("/", response_model=List[schemas.UserOut])
def get_users(db: Session = Depends(database.get_db), current_user: int = Depends(oauth2.get_current_user)):

    users = db.query(sa_models.User).all()

    if not current_user.admin:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=f"User with id: {current_user.id} is not an admin")

    return users

#CREATE USER - creates a new user
@router.post("/", response_model=schemas.UserOut)
def create_user(user: schemas.UserBase, status_code=status.HTTP_201_CREATED, db: Session = Depends(database.get_db)):
    
    #hash the password
    hashed_pwd = utils.hash(user.password)
    user.password = hashed_pwd

    user_check = db.query(sa_models.User).filter(sa_models.User.email == user.email).first()
    if user_check:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=f"User with email {user_check.email} already exists")

    new_user = sa_models.User(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user


#GET USER - gets a user with a certain id
@router.get("/{id}", response_model=schemas.UserOut)
def get_user(id: int, db: Session = Depends(database.get_db), current_user: int = Depends(oauth2.get_current_user)):

    user = db.query(sa_models.User).filter(sa_models.User.id == id).first() 

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with id: {id} was not found")

    if id != current_user.id:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=f"Unauthorized to access user with id: {id}")  

    return user


#DELETE USER - deletes a user with certain id
@router.delete("/{id}")
def delete_user(id: int, db: Session = Depends(database.get_db), current_user: int = Depends(oauth2.get_current_user)):

    user_query = db.query(sa_models.User).filter(sa_models.User.id == id)
    user = user_query.first()

    if user == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with id: {id} was not found") 

    if id != current_user.id:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=f"Unauthorized to access user with id: {id}")  

    user_query.delete(synchronize_session=False)
    db.commit()

    return Response(status_code=status.HTTP_204_NO_CONTENT)


#UPDATE USER - updates the user
@router.put("/{id}", response_model=schemas.UserOut)
def update_user(id: int, updated_user: schemas.UserUpdate, db: Session = Depends(database.get_db), current_user: int = Depends(oauth2.get_current_user)):

    user_query = db.query(sa_models.User).filter(sa_models.User.id == id)
    user = user_query.first()

    if user == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with id: {id} was not found")

    if id != current_user.id:
       raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=f"Unauthorized to access user with id: {id}") 

    user_query.update(updated_user.dict(), synchronize_session=False)
    db.commit()

    return user