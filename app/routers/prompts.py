from typing import Optional, List
from fastapi import FastAPI, Response, status, HTTPException, APIRouter, Depends
from sqlalchemy.orm import Session
from ..models import sa_models
from ..models.schemas import Prompt
from ..utilities import oauth2, utils
from .. import database

router = APIRouter(
    prefix="/prompts",
    tags=["Prompts"]
)

@router.get("/", response_model=List[Prompt.PromptOut])
def get_prompts(db: Session = Depends(database.get_db)):
    """
    Get a list of prompts.

    Parameters:
      db (Session): Database session.

    Returns:
      List[Prompt.PromptOut]: List of prompts.
    """
    query = db.query(sa_models.Prompt)
    prompts = query.all()

    return prompts

@router.post("/", response_model=List[Prompt.PromptOut], status_code=status.HTTP_201_CREATED)
def create_prompt(
    prompts: List[Prompt.PromptBase],
    db: Session = Depends(database.get_db),
    current_user: int = Depends(oauth2.get_current_user)
):
    """
    Create new prompts.

    Parameters:
      prompts (List[Prompt.PromptBase]): List of prompts to create.
      db (Session): Database session.
      current_user (int): Current user ID.

    Returns:
      List[Prompt.PromptOut]: List of created prompts.
    """
    if not current_user.admin:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=f"User with id: {current_user.id} is not an admin")

    updated_prompts = []

    for prompt in prompts:
        new_prompt = sa_models.Prompt(**prompt.dict())
        updated_prompts.append(new_prompt)
        db.add(new_prompt)
        db.commit()
        db.refresh(new_prompt)

    return updated_prompts

@router.get("/{id}", response_model=Prompt.PromptOut)
def get_prompt(id: int, db: Session = Depends(database.get_db)):
    """
    Get a prompt by ID.

    Parameters:
      id (int): Prompt ID.
      db (Session): Database session.

    Returns:
      Prompt.PromptOut: The requested prompt.
    """
    prompt = db.query(sa_models.Prompt).filter(sa_models.Prompt.id == id).first()

    if not prompt:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Prompt with id: {id} does not exist")

    return prompt

@router.put("/{id}", response_model=Prompt.PromptOut)
def update_prompt(
    id: int,
    updated_prompt: Prompt.PromptBase,
    db: Session = Depends(database.get_db),
    current_user: int = Depends(oauth2.get_current_user)
):
    """
    Update a prompt by ID.

    Parameters:
      id (int): Prompt ID.
      updated_prompt (Prompt.PromptBase): Updated prompt data.
      db (Session): Database session.
      current_user (int): Current user ID.

    Returns:
      Prompt.PromptOut: The updated prompt.
    """
    prompt_query = db.query(sa_models.Prompt).filter(sa_models.Prompt.id == id)
    prompt = prompt_query.first()

    if not prompt:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Prompt with id: {id} does not exist")

    if not current_user.admin:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=f"User with id: {current_user.id} is not an admin")

    prompt_query.update(updated_prompt.dict(), synchronize_session=False)
    db.commit()

    return prompt

@router.delete("/{id}")
def delete_prompt(
    id: int,
    db: Session = Depends(database.get_db),
    current_user: int = Depends(oauth2.get_current_user)
):
    """
    Delete a prompt by ID.

    Parameters:
      id (int): Prompt ID.
      db (Session): Database session.
      current_user (int): Current user ID.

    Returns:
      Response: HTTP response indicating success.
    """
    prompt_query = db.query(sa_models.Prompt).filter(sa_models.Prompt.id == id)
    prompt = prompt_query.first()

    if not prompt:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Prompt with id: {id} does not exist")

    if not current_user.admin:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=f"User with id: {current_user.id} is not an admin")

    prompt_query.delete(synchronize_session=False)
    db.commit()

    return Response(status_code=status.HTTP_204_NO_CONTENT)