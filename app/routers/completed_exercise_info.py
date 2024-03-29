from typing import Optional, List
from fastapi import FastAPI, Response, status, HTTPException, APIRouter, Depends
from sqlalchemy.orm import Session
from ..models import sa_models
from ..models.schemas import UserData
from ..utilities import oauth2, utils
from .. import database
from datetime import datetime
import pytz

router = APIRouter(
    prefix="/completed_exercise_info",
    tags=["Completed Exercise Info"]
)

completedInfo = UserData.CompletedExerciseInfo

@router.get("/", response_model=completedInfo.CompletedExerciseInfoOut)
def get_exercises(
    db: Session = Depends(database.get_db),
    current_user: int = Depends(oauth2.get_current_user)
):
    """
    Get completed exercise information for the current user.

    Parameters:
      db (Session): Database session.
      current_user (int): Current user ID.

    Returns:
      completedInfo.CompletedExerciseInfoOut: Completed exercise information.
    """
    query = db.query(sa_models.User.completed_exercise_info).filter(sa_models.User.id == current_user.id)
    completed_exercises_col = query.first()

    return completed_exercises_col.completed_exercise_info

@router.put("/", response_model=completedInfo.CompletedExerciseInfoOut)
def update_exercise(
    updated_exercises: completedInfo.CompletedExerciseInfoBase,
    db: Session = Depends(database.get_db),
    current_user: int = Depends(oauth2.get_current_user)
):
    """
    Update completed exercise information for the current user.

    Parameters:
      updated_exercises (completedInfo.CompletedExerciseInfoBase): Updated completed exercise information.
      db (Session): Database session.
      current_user (int): Current user ID.

    Returns:
      completedInfo.CompletedExerciseInfoOut: Updated completed exercise information.
    """
    user_query = db.query(sa_models.User).filter(sa_models.User.id == current_user.id)
    user = user_query.first()
    user.completed_exercise_info = updated_exercises.dict()

    updated_user = utils.row_to_dict(user)
    updated_user["completed_exercise_info"]["completion_date"] = datetime.now(pytz.utc).isoformat()
    user_query.update(updated_user, synchronize_session=False)

    db.commit()

    return updated_user["completed_exercise_info"]

@router.get("/{id}", response_model=completedInfo.CompletedExerciseInfoOut)
def get_one_exercise(
    id: int,
    db: Session = Depends(database.get_db),
    current_user: int = Depends(oauth2.get_current_user)
):
    """
    Get completed exercise information for a specific user.

    Parameters:
      id (int): User ID.
      db (Session): Database session.
      current_user (int): Current user ID.

    Returns:
      completedInfo.CompletedExerciseInfoOut: Completed exercise information.
    """
    if current_user.admin or id == current_user.id:
        query = db.query(sa_models.User).filter(sa_models.User.id == id)
        completed_exercise_col = query.first()

        return completed_exercise_col.completed_exercise_info
    
    else:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=f"Unauthorized to access user with id: {id}")

@router.put("/{id}", response_model=completedInfo.CompletedExerciseInfoOut)
def update_exercises_by_id(
    id: int,
    updated_info: completedInfo.CompletedExerciseInfoBase,
    db: Session = Depends(database.get_db),
    current_user: int = Depends(oauth2.get_current_user)
):
    """
    Update completed exercise information for a specific user.

    Parameters:
      id (int): User ID.
      updated_info (completedInfo.CompletedExerciseInfoBase): Updated completed exercise information.
      db (Session): Database session.
      current_user (int): Current user ID.

    Returns:
      completedInfo.CompletedExerciseInfoOut: Updated completed exercise information.
    """
    if current_user.admin or id == current_user.id:
        user_query = db.query(sa_models.User).filter(sa_models.User.id == id)
        user = user_query.first()
        user.completed_exercise_info = updated_info.dict()

        updated_user = utils.row_to_dict(user)
        updated_user["completed_exercise_info"]["completion_date"] = datetime.now(pytz.utc).isoformat()
        user_query.update(updated_user, synchronize_session=False)

        db.commit()

        return updated_user["completed_exercise_info"]
    
    else:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=f"Unauthorized to access user with id: {id}")