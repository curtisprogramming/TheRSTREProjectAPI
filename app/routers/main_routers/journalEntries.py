from typing import Optional, List
from fastapi import FastAPI, Response, status, HTTPException, APIRouter, Depends
from sqlalchemy.orm import Session
from ...models import schemas, sa_models
from ...utilities import oauth2, utils
from ... import database

router = APIRouter(
    prefix="/journalentries",
    tags=["Journal Entires"]
)

@router.get("/")
def get_journal_entries(db: Session = Depends(database.get_db), current_user: int = Depends(oauth2.get_current_user)):
    
    journal_entries = db.query(sa_models.JournalEntry).filter()
