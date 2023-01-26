from typing import Optional, List
from fastapi import FastAPI, Response, status, HTTPException, APIRouter, Depends
from sqlalchemy.orm import Session
from .. import schemas, models, database, utils, oauth2

router = APIRouter(
    prefix="/exercises",
    tags=["Exercises"]
)

@router.get("/", response_model=List[schemas.ExerciseOut])
def get_exercises(db: Session = Depends(database.get_db)):
   
    query = db.query(models.Exercise)
    exercises = query.all()

    return exercises

@router.post("/", response_model=schemas.ExerciseOut)
def create_exercise(exercise: schemas.ExerciseBase, status_code=status.HTTP_201_CREATED, db: Session = Depends(database.get_db), current_user: int = Depends(oauth2.get_current_user)):

    if not current_user.admin:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=f"User with id: {current_user.id} is not an admin")

    new_exercise = models.Exercise(**exercise.dict())
    db.add(new_exercise)
    db.commit()
    db.refresh(new_exercise)

    return new_exercise

@router.get("/{id}", response_model=schemas.ExerciseOut)
def get_exercise(id: int, db: Session = Depends(database.get_db)):

    exercise = db.query(models.Exercise).filter(models.Exercise.id == id).first()

    if not exercise:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Exercise with id: {id} does not exist")

    return exercise

@router.put("/{id}", response_model=schemas.ExerciseOut)
def update_exercise(id: int, updated_exercise: schemas.ExerciseBase, db: Session = Depends(database.get_db), current_user: int = Depends(oauth2.get_current_user)):

    exercise_query = db.query(models.Exercise).filter(models.Exercise.id == id)
    exercise = exercise_query.first()

    if not exercise:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Exercise with id: {id} does not exist")

    if not current_user.admin:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=f"User with id: {current_user.id} is not an admin")

    exercise_query.update(updated_exercise.dict(), synchronize_session=False)
    db.commit()

    return exercise

@router.delete("/{id}")
def delete_exercise(id: int, db: Session = Depends(database.get_db), current_user: int = Depends(oauth2.get_current_user)):

    exercise_query = db.query(models.Exercise).filter(models.Exercise.id == id)
    exercise = exercise_query.first()

    if not exercise:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Exercise with id: {id} does not exist")

    if not current_user.admin:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=f"User with id: {current_user.id} is not an admin")

    exercise_query.delete(synchronize_session=False)
    db.commit()

    return Response(status_code=status.HTTP_204_NO_CONTENT)