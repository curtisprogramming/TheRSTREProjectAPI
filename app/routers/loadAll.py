from typing import Optional, List
from fastapi import FastAPI, Response, status, HTTPException, APIRouter, Depends
from sqlalchemy.orm import Session
from ..models import schemas, sa_models
from ..utilities import oauth2, utils
from .. import database

router = APIRouter(
    prefix="/loadAll",
    tags=["Load All Data"]
)

@router.get("/")#, response_model=schemas.LoadAll)
def load_all(db: Session = Depends(database.get_db), current_user: int = Depends(oauth2.get_current_user)):

    exercises = db.query(sa_models.Exercise).all()
    resources = db.query(sa_models.Resource).all()
    prompts = db.query(sa_models.Prompt).all()
    completed_exercises = db.query(sa_models.User.completed_exercises).filter(sa_models.User.id == current_user.id).first()

    return schemas.LoadAll(exercises=exercises, resources=resources, prompts=prompts, completed_exercises=completed_exercises.completed_exercises)