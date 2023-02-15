from typing import Optional, List
from fastapi import FastAPI, Response, status, HTTPException, APIRouter, Depends
from sqlalchemy.orm import Session
from ..models import sa_models
from ..models.schemas import Extras as extra_schemas
from ..utilities import oauth2, utils
from .. import database

router = APIRouter(
    prefix="/loadAll",
    tags=["Load All Data"]
)

@router.get("/", response_model=extra_schemas.LoadAll)
def load_all(db: Session = Depends(database.get_db), current_user: int = Depends(oauth2.get_current_user)):

    exercises = db.query(sa_models.Exercise).all()
    resources = db.query(sa_models.Resource).all()
    prompts = db.query(sa_models.Prompt).all()
    user = db.query(sa_models.User).filter(sa_models.User.id == current_user.id).first()

    return extra_schemas.LoadAll(exercises=exercises, resources=resources, prompts=prompts, completed_exercise_info=user.completed_exercise_info, journal_entries=user.journal_entries)