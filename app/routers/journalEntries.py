from typing import Optional, List
from fastapi import FastAPI, Response, status, HTTPException, APIRouter, Depends
from sqlalchemy.orm import Session
from ..models import sa_models
from ..models.schemas import UserData
from ..utilities import oauth2, utils
from .. import database
import uuid
from datetime import datetime
import pytz

router = APIRouter(
    prefix="/journalentries",
    tags=["Journal Entires"]
)

journalEntries = UserData.JournalEntries

@router.get("/", response_model=List[journalEntries.JournalEntryOut])
def get_journal_entries(db: Session = Depends(database.get_db), current_user: int = Depends(oauth2.get_current_user)):

    journal_entries_col = db.query(sa_models.User.journal_entries).filter(sa_models.User.id == current_user.id).first()

    return journal_entries_col.journal_entries

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=journalEntries.JournalEntryOut)
def create_journal_entry(new_journal_entry: journalEntries.JournalEntryBase, db: Session = Depends(database.get_db), current_user: int = Depends(oauth2.get_current_user)):

    user_query = db.query(sa_models.User).filter(sa_models.User.id == current_user.id)
    user = user_query.first()
    
    #creates the new journal entry with defaults for id and time
    journal_entry_dict = new_journal_entry.dict()
    id = str(uuid.uuid1())
    journal_entry_dict['id'] = id
    journal_entry_dict['created_at'] = datetime.now(pytz.utc).isoformat()
    
    #updates user with the new journal entry
    user.journal_entries.append(journal_entry_dict)

    updated_user = utils.row_to_dict(user)
    user_query.update(updated_user, synchronize_session=False)

    db.commit()

    return journal_entry_dict

@router.get("/{id}", response_model=journalEntries.JournalEntryOut)
def get_journal_entry(id: str, db: Session = Depends(database.get_db), current_user: int = Depends(oauth2.get_current_user)):

    user = db.query(sa_models.User).filter(sa_models.User.id == current_user.id).first()
    
    journal_entries = user.journal_entries
    journal_entries_index = utils.Search.linear_search_id(journal_entries, id)

    if journal_entries_index == -1:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Journal entry with id: {id} does not exist")
    
    return journal_entries[journal_entries_index]

@router.put("/{id}", response_model=journalEntries.JournalEntryOut)
def update_journal_entry(id: str, updated_entry: journalEntries.JournalEntryBase, db: Session = Depends(database.get_db), current_user: int = Depends(oauth2.get_current_user)):

    user_query = db.query(sa_models.User).filter(sa_models.User.id == current_user.id)
    user = user_query.first()

    journal_entries = user.journal_entries
    journal_entries_index = utils.Search.linear_search_id(journal_entries, id)

    #saves he data not included in the updated data
    entry_id = journal_entries[journal_entries_index]['id']
    created_at = journal_entries[journal_entries_index]['created_at']

    #sets the data not included in the updated data
    journal_entry_dict = updated_entry.dict()
    journal_entry_dict['id'] = entry_id
    journal_entry_dict['created_at'] = created_at
    
    #replaces the old data
    journal_entries[journal_entries_index] = journal_entry_dict

    if journal_entries_index == -1:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Journal entry with id: {id} does not exist")

    user_query.update(utils.row_to_dict(user), synchronize_session=False)
    db.commit()

    return journal_entries[journal_entries_index]

@router.delete("/{id}")
def delete_journal_entry(id: str, db: Session = Depends(database.get_db), current_user: int = Depends(oauth2.get_current_user)):

    user_query = db.query(sa_models.User).filter(sa_models.User.id == current_user.id)
    user = user_query.first()

    journal_entries = user.journal_entries
    journal_entry_index = utils.Search.linear_search_id(journal_entries, id)
    journal_entries.pop(journal_entry_index)

    user.journal_entries = journal_entries

    if journal_entry_index == -1:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Journal entry with id: {id} does not exist")


    user_query.update(utils.row_to_dict(user), synchronize_session=False)
    db.commit()

    return Response(status_code=status.HTTP_204_NO_CONTENT) 