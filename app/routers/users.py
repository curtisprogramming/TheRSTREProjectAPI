from typing import Optional, List
from fastapi import FastAPI, Response, status, HTTPException, APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from ..models import sa_models
from ..models.schemas import UserData
from ..utilities import oauth2, utils
from .. import database
from datetime import datetime
import pytz

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

@router.get("/", response_model=List[UserData.UserOut])
def get_users(db: Session = Depends(database.get_db), current_user: int = Depends(oauth2.get_current_user)):
    """
    Get all users.

    Parameters:
        db (Session): The database session.
        current_user (int): The ID of the current user.

    Returns:
        List[UserData.UserOut]: List of user data.
    """
    users = db.query(sa_models.User).all()

    if not current_user.admin:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=f"User with id: {current_user.id} is not an admin")

    return users

@router.post("/", response_model=UserData.UserOut, status_code=status.HTTP_201_CREATED)
def create_user(user: UserData.UserCreate, db: Session = Depends(database.get_db)):
    """
    Create a new user.

    Parameters:
        user (UserData.UserCreate): The user data for creation.
        db (Session): The database session.

    Returns:
        UserData.UserOut: The newly created user.
    """
    #hash the password
    hashed_pwd = utils.hash(user.password)
    user.password = hashed_pwd

    #sets completed_exercise_info
    user_dict = user.dict()
    completed_exercise_info_dict = {"completion_date": datetime.now(pytz.utc).isoformat(), "completed_exercises": [{"exercise_name":"journaling","completed":False},{"exercise_name":"breathing","completed":False},{"exercise_name":"meditating","completed":False},{"exercise_name":"stretching","completed":False}]}
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

@router.get("/{id}", response_model=UserData.UserOut)
def get_user(id: int, db: Session = Depends(database.get_db), current_user: int = Depends(oauth2.get_current_user)):
    """
    Get a user by ID.

    Parameters:
        id (int): The ID of the user to retrieve.
        db (Session): The database session.
        current_user (int): The ID of the current user.

    Returns:
        UserData.UserOut: The user data.
    """
    user = db.query(sa_models.User).filter(sa_models.User.id == id).first() 

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with id: {id} does not exist")

    if current_user.admin or current_user.id == id:
        pass
    else:
       raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=f"Unauthorized to access user with id: {id}")  

    return user

@router.delete("/{id}")
def delete_user(id: int, db: Session = Depends(database.get_db), current_user: int = Depends(oauth2.get_current_user)):
    """
    Delete a user by ID.

    Parameters:
        id (int): The ID of the user to delete.
        db (Session): The database session.
        current_user (int): The ID of the current user.

    Returns:
        Response: HTTP 204 No Content.
    """
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

@router.put("/{id}", response_model=UserData.UserOut)
def update_user(id: int, updated_user: UserData.UserUpdate, db: Session = Depends(database.get_db), current_user: int = Depends(oauth2.get_current_user)):
    """
    Update a user by ID.

    Parameters:
        id (int): The ID of the user to update.
        updated_user (UserData.UserUpdate): The updated user data.
        db (Session): The database session.
        current_user (int): The ID of the current user.

    Returns:
        UserData.UserOut: The updated user data.
    """
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
