from typing import Optional, List
from fastapi import FastAPI, Response, status, HTTPException, APIRouter, Depends
from sqlalchemy.orm import Session
from ..models import sa_models
from ..models.schemas import UserData 
from ..utilities import oauth2, utils
from .. import database

router = APIRouter(
    prefix="/journalentries",
    tags=["Journal Entires"]
)

journalEntries = UserData.JournalEntries

@router.get("/", response_model=journalEntries.JournalEntryOut)
def get_journal_entries(db: Session = Depends(database.get_db), current_user: int = Depends(oauth2.get_current_user)):

    journal_entries = db.query(sa_models.JournalEntry).filter(sa_models.JournalEntry.owner_id == current_user.id).all()

    return journal_entries

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=journalEntries.JournalEntryOut)
def create_journal_entry(journal_entry: journalEntries.JournalEntryBase, db: Session = Depends(database.get_db), current_user: int = Depends(oauth2.get_current_user)):
    
    new_entry = sa_models.JournalEntry(owner_id=current_user.id, **journal_entry.dict())

    db.add(new_entry)
    db.commit()
    db.refresh(new_entry)

    return new_entry

@router.get("/{id}", response_model=journalEntries.JournalEntryOut)
def get_journal_entry(id: int, db: Session = Depends(database.get_db), current_user: int = Depends(oauth2.get_current_user)):

    journal_entry = db.query(sa_models.JournalEntry).filter(sa_models.JournalEntry.id == id).first()

    if not journal_entry:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Journal entry with id: {id} does not exist")

    if current_user.id != journal_entry.owner_id:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=f"Unauthorized to access with user id: {id}")
    
    return journal_entry

@router.put("/{id}")#, response_model=schemas.JournalEntryOut)
def update_journal_entry(id: int, updated_entry: journalEntries.JournalEntryBase, db: Session = Depends(database.get_db), current_user: int = Depends(oauth2.get_current_user)):

    entry_query = db.query(sa_models.JournalEntry).filter(sa_models.JournalEntry.id == id)
    journal_entry = entry_query.first()

    if not journal_entry:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Journal entry with id: {id} does not exist")

    if current_user.id != journal_entry.owner_id:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=f"Unauthorized to access with user id: {id}")

    entry_query.update(updated_entry.dict(), synchronize_session=False)
    db.commit()

    return entry_query

@router.delete("/{id}")
def delete_journal_entry(id: int, db: Session = Depends(database.get_db), current_user: int = Depends(oauth2.get_current_user)):

    entry_query = db.query(sa_models.JournalEntry).filter(sa_models.JournalEntry.id == id)
    journal_entry = entry_query.first()

    if not journal_entry:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Journal entry with id: {id} does not exist")

    if current_user.id != journal_entry.owner_id:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=f"Unauthorized to access with user id: {id}")

    entry_query.delete(synchronize_session=False)
    db.commit()

    return Response(status_code=status.HTTP_204_NO_CONTENT)