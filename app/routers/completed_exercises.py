from typing import Optional, List
from fastapi import FastAPI, Response, status, HTTPException, APIRouter, Depends
from sqlalchemy.orm import Session
from ..models import schemas, sa_models
from ..utilities import oauth2, utils
from .. import database

router = APIRouter(
    prefix="/completed_exercises",
    tags=["Completed Exercises"]
)

@router.get("/", response_model=schemas.CompletedExercisesOut)
def get_exercises(db: Session = Depends(database.get_db), current_user: int = Depends(oauth2.get_current_user)):
   
    query = db.query(sa_models.User.completed_exercises).filter(sa_models.User.id == current_user.id)
    completed_exercises = query.first()

    return completed_exercises

@router.put("/", response_model=schemas.CompletedExercisesOut)
def update_exercise(updated_exercises: schemas.CompletedExercises, db: Session = Depends(database.get_db), current_user: int = Depends(oauth2.get_current_user)):

    user_query = db.query(sa_models.User).filter(sa_models.User.id == current_user.id)
    user = user_query.first()
    user.completed_exercises = updated_exercises.dict()

    updated_user = utils.row_to_dict(user)
    updated_user["completed_exercises"]["completion_date"] = str(updated_user["completed_exercises"]["completion_date"])
    user_query.update(updated_user, synchronize_session=False)

    db.commit()

    return updated_user["completed_exercises"]