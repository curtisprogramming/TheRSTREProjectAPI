from typing import Optional, List
from fastapi import FastAPI, Response, status, HTTPException, APIRouter, Depends
from sqlalchemy.orm import Session
from .. import schemas, models, database, utils, oauth2

router = APIRouter(
    prefix="/prompts",
    tags=["Promts"]
)

@router.get("/", response_model=List[schemas.PromptOut])
def get_prompts(db: Session = Depends(database.get_db)):
   
    query = db.query(models.Prompt)
    prompts = query.all()

    return prompts

@router.post("/", response_model=schemas.PromptOut)
def create_prompt(prompt: schemas.PromptBase, status_code=status.HTTP_201_CREATED, db: Session = Depends(database.get_db), current_user: int = Depends(oauth2.get_current_user)):

    if not current_user.admin:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=f"User with id: {current_user.id} is not an admin")

    new_prompt = models.Prompt(**prompt.dict())
    db.add(new_prompt)
    db.commit()
    db.refresh(new_prompt)

    return new_prompt

@router.get("/{id}", response_model=schemas.PromptOut)
def get_prompt(id: int, db: Session = Depends(database.get_db)):

    prompt = db.query(models.Prompt).filter(models.Prompt.id == id).first()

    if not prompt:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Prompt with id: {id} does not exist")

    return prompt

@router.put("/{id}", response_model=schemas.PromptOut)
def update_prompt(id: int, updated_prompt: schemas.PromptBase, db: Session = Depends(database.get_db), current_user: int = Depends(oauth2.get_current_user)):

    prompt_query = db.query(models.Prompt).filter(models.Prompt.id == id)
    prompt = prompt_query.first()

    if not prompt:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Prompt with id: {id} does not exist")

    if not current_user.admin:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=f"User with id: {current_user.id} is not an admin")

    prompt_query.update(updated_prompt.dict(), synchronize_session=False)
    db.commit()

    return prompt

@router.delete("/{id}")
def delete_prompt(id: int, db: Session = Depends(database.get_db), current_user: int = Depends(oauth2.get_current_user)):

    prompt_query = db.query(models.Prompt).filter(models.Prompt.id == id)
    prompt = prompt_query.first()

    if not prompt:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Prompt with id: {id} does not exist")

    if not current_user.admin:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=f"User with id: {current_user.id} is not an admin")

    prompt_query.delete(synchronize_session=False)
    db.commit()

    return Response(status_code=status.HTTP_204_NO_CONTENT)