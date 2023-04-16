from typing import Optional, List
from fastapi import FastAPI, Response, status, HTTPException, APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from ..models import sa_models
from ..models.schemas import UserData
from ..utilities import oauth2, utils
from .. import database
from datetime import datetime

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

#GET USERS - gets all the users 
@router.get("/", response_model=List[UserData.UserOut])
def get_users(db: Session = Depends(database.get_db), current_user: int = Depends(oauth2.get_current_user)):

    users = db.query(sa_models.User).all()

    if not current_user.admin:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=f"User with id: {current_user.id} is not an admin")

    return users

#CREATE USER - creates a new user
@router.post("/", response_model=UserData.UserOut, status_code=status.HTTP_201_CREATED)
def create_user(user: UserData.UserCreate, db: Session = Depends(database.get_db)):
    
    #hash the password
    hashed_pwd = utils.hash(user.password)
    user.password = hashed_pwd

    #sets completed_exerccise_info
    user_dict = user.dict()
    completed_exercise_info_dict = {"completion_date": datetime.now().isoformat(), "completed_exercises": [{"exercise_name":"journaling","completed":False},{"exercise_name":"breathing","completed":False},{"exercise_name":"meditating","completed":False},{"exercise_name":"stretching","completed":False}]}
    verified_completed_exercise_info = UserData.CompletedExerciseInfo.CompletedExerciseInfoOut(**completed_exercise_info_dict)
    user_dict['completed_exercise_info'] = verified_completed_exercise_info.dict()
    user_dict['completed_exercise_info']['completion_date'] = verified_completed_exercise_info.completion_date.isoformat()

    try:
        new_user = sa_models.User(**user_dict)
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        
        
    except IntegrityError as err:
        err_msg = err.args[0]
        if "duplicate key value violates unique constraint \"users_email_key\"" in err_msg:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=f"User with email: {user.email} already exists")

        elif "duplicate key value violates unique constraint \"users_username_key\"" in err_msg:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=f"User with username: {user.username} already exists")

        else:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=err_msg)

    return new_user


#GET USER - gets a user with a certain id
@router.get("/{id}", response_model=UserData.UserOut)
def get_user(id: int, db: Session = Depends(database.get_db), current_user: int = Depends(oauth2.get_current_user)):

    user = db.query(sa_models.User).filter(sa_models.User.id == id).first() 

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with id: {id} does not exist")

    if current_user.admin or current_user.id == id:
        pass
    else:
       raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=f"Unauthorized to access user with id: {id}")  

    return user


#DELETE USER - deletes a user with certain id
@router.delete("/{id}")
def delete_user(id: int, db: Session = Depends(database.get_db), current_user: int = Depends(oauth2.get_current_user)):

    user_query = db.query(sa_models.User).filter(sa_models.User.id == id)
    user = user_query.first()

    if user == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with id: {id} does not exist")  

    if current_user.admin or current_user.id == id:
        user_query.delete(synchronize_session=False)
        db.commit()
    else:
       raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=f"Unauthorized to access user with id: {id}") 

    return Response(status_code=status.HTTP_204_NO_CONTENT)


#UPDATE USER - updates the user
@router.put("/{id}", response_model=UserData.UserOut)
def update_user(id: int, updated_user: UserData.UserUpdate, db: Session = Depends(database.get_db), current_user: int = Depends(oauth2.get_current_user)):

    user_query = db.query(sa_models.User).filter(sa_models.User.id == id)
    user = user_query.first()

    if user == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with id: {id} does not exist")

    if current_user.admin or current_user.id == id:

        try:
            user_query.update(updated_user.dict(), synchronize_session=False)
            db.commit()
        except IntegrityError as err:
            err_msg = err.args[0]
            if "duplicate key value violates unique constraint \"users_email_key\"" in err_msg:
                raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=f"User with email: {updated_user.email} already exists")

            elif "duplicate key value violates unique constraint \"users_username_key\"" in err_msg:
                raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=f"User with username: {updated_user.username} already exists")

            else:
                raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=err_msg)

    else:
       raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=f"Unauthorized to access user with id: {id}") 

    return user