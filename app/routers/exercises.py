from typing import Optional, List
from fastapi import FastAPI, Response, status, HTTPException, APIRouter, Depends
from sqlalchemy.orm import Session
from ..models import sa_models
from ..models.schemas import Exercise
from ..utilities import oauth2, utils
from .. import database

router = APIRouter(
    prefix="/exercises",
    tags=["Exercises"]
)

@router.get("/", response_model=List[Exercise.ExerciseOut])
def get_exercises(
    db: Session = Depends(database.get_db)
):
    """
    Get a list of all exercises.

    Parameters:
      db (Session): Database session.

    Returns:
      List[Exercise.ExerciseOut]: List of exercises.
    """
    query = db.query(sa_models.Exercise)
    exercises = query.all()

    return exercises

@router.post("/", response_model=List[Exercise.ExerciseOut], status_code=status.HTTP_201_CREATED)
def create_exercise(
    exercises: List[Exercise.ExerciseBase],
    db: Session = Depends(database.get_db),
    current_user: int = Depends(oauth2.get_current_user)
):
    """
    Create new exercises.

    Parameters:
      exercises (List[Exercise.ExerciseBase]): List of exercises to create.
      db (Session): Database session.
      current_user (int): Current user ID.

    Returns:
      List[Exercise.ExerciseOut]: List of created exercises.
    """
    if not current_user.admin:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=f"User with id: {current_user.id} is not an admin")

    updated_exercises = []

    for exercise in exercises:
        new_exercise = sa_models.Exercise(**exercise.dict())
        updated_exercises.append(new_exercise)
        db.add(new_exercise)
        db.commit()
        db.refresh(new_exercise)

    return updated_exercises

@router.get("/{id}", response_model=Exercise.ExerciseOut)
def get_exercise(
    id: int,
    db: Session = Depends(database.get_db)
):
    """
    Get details of a specific exercise.

    Parameters:
      id (int): Exercise ID.
      db (Session): Database session.

    Returns:
      Exercise.ExerciseOut: Details of the specified exercise.
    """
    exercise = db.query(sa_models.Exercise).filter(sa_models.Exercise.id == id).first()

    if not exercise:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Exercise with id: {id} does not exist")

    return exercise

@router.put("/{id}", response_model=Exercise.ExerciseOut)
def update_exercise(
    id: int,
    updated_exercise: Exercise.ExerciseBase,
    db: Session = Depends(database.get_db),
    current_user: int = Depends(oauth2.get_current_user)
):
    """
    Update details of a specific exercise.

    Parameters:
      id (int): Exercise ID.
      updated_exercise (Exercise.ExerciseBase): Updated details of the exercise.
      db (Session): Database session.
      current_user (int): Current user ID.

    Returns:
      Exercise.ExerciseOut: Updated details of the exercise.
    """
    exercise_query = db.query(sa_models.Exercise).filter(sa_models.Exercise.id == id)
    exercise = exercise_query.first()

    if not exercise:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Exercise with id: {id} does not exist")

    if not current_user.admin:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=f"User with id: {current_user.id} is not an admin")

    exercise_query.update(updated_exercise.dict(), synchronize_session=False)
    db.commit()

    return exercise

@router.delete("/{id}")
def delete_exercise(
    id: int,
    db: Session = Depends(database.get_db),
    current_user: int = Depends(oauth2.get_current_user)
):
    """
    Delete a specific exercise.

    Parameters:
      id (int): Exercise ID.
      db (Session): Database session.
      current_user (int): Current user ID.

    Returns:
      Response: HTTP Response indicating success.
    """
    exercise_query = db.query(sa_models.Exercise).filter(sa_models.Exercise.id == id)
    exercise = exercise_query.first()

    if not exercise:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Exercise with id: {id} does not exist")

    if not current_user.admin:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=f"User with id: {current_user.id} is not an admin")

    exercise_query.delete(synchronize_session=False)
    db.commit()

    return Response(status_code=status.HTTP_204_NO_CONTENT)
