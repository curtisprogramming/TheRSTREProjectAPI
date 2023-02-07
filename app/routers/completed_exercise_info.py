from typing import Optional, List
from fastapi import FastAPI, Response, status, HTTPException, APIRouter, Depends
from sqlalchemy.orm import Session
from ..models import sa_models
from ..models.schemas import UserData
from ..utilities import oauth2, utils
from .. import database

router = APIRouter(
    prefix="/completed_exercise_info",
    tags=["Completed Exercise Info"]
)

completedInfo = UserData.CompletedExerciseInfo

@router.get("/", response_model=completedInfo.CompletedExerciseInfoOut)
def get_exercises(db: Session = Depends(database.get_db), current_user: int = Depends(oauth2.get_current_user)):
   
    query = db.query(sa_models.User.completed_exercise_info).filter(sa_models.User.id == current_user.id)
    completed_exercises_col = query.first()

    return completed_exercises_col.completed_exercise_info

@router.put("/", response_model=completedInfo.CompletedExerciseInfoOut)
def update_exercise(updated_exercises: completedInfo.CompletedExerciseInfoBase, db: Session = Depends(database.get_db), current_user: int = Depends(oauth2.get_current_user)):

    user_query = db.query(sa_models.User).filter(sa_models.User.id == current_user.id)
    user = user_query.first()
    user.completed_exercise_info = updated_exercises.dict()

    updated_user = utils.row_to_dict(user)
    updated_user["completed_exercise_info"]["completion_date"] = str(updated_user["completed_exercise_info"]["completion_date"])
    user_query.update(updated_user, synchronize_session=False)

    db.commit()

    return updated_user["completed_exercise_info"]