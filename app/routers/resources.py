from typing import Optional, List
from fastapi import FastAPI, Response, status, HTTPException, APIRouter, Depends
from sqlalchemy.orm import Session
from ..models import schemas, sa_models
from ..utilities import oauth2, utils
from .. import database

router = APIRouter(
    prefix="/resources",
    tags=["Resources"]
)

@router.get("/", response_model=List[schemas.ResourceOut])
def get_resources(db: Session = Depends(database.get_db)):
   
    query = db.query(sa_models.Resource)
    resources = query.all()

    return resources

@router.post("/", response_model=schemas.ResourceOut)
def create_resource(resource: schemas.ResourceBase, status_code=status.HTTP_201_CREATED, db: Session = Depends(database.get_db), current_user: int = Depends(oauth2.get_current_user)):

    if not current_user.admin:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=f"User with id: {current_user.id} is not an admin")


    new_resource = sa_models.Resource(**resource.dict())
    db.add(new_resource)
    db.commit()
    db.refresh(new_resource)

    return resource

@router.get("/{id}", response_model=schemas.ResourceOut)
def get_resource(id: int, db: Session = Depends(database.get_db)):

    resource = db.query(sa_models.Resource).filter(sa_models.Resource.id == id).first()

    if not resource:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Resource with id: {id} does not exist")

    return resource

@router.put("/{id}", response_model=schemas.ResourceOut)
def update_resource(id: int, updated_resource: schemas.ResourceBase, db: Session = Depends(database.get_db), current_user: int = Depends(oauth2.get_current_user)):

    resource_query = db.query(sa_models.Resource).filter(sa_models.Resource.id == id)
    resource = resource_query.first()

    if not resource:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Resource with id: {id} does not exist")

    if not current_user.admin:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=f"User with id: {current_user.id} is not an admin")

    resource_query.update(updated_resource.dict(), synchronize_session=False)
    db.commit()

    return resource

@router.delete("/{id}")
def delete_resources(id: int, db: Session = Depends(database.get_db), current_user: int = Depends(oauth2.get_current_user)):
    resource_query = db.query(sa_models.Resource).filter(sa_models.Resource.id == id)
    resource = resource_query.first()

    if not resource:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Resource with id: {id} does not exist")

    if not current_user.admin:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=f"User with id: {current_user.id} is not an admin")

    resource_query.delete(synchronize_session=False)
    db.commit()

    return Response(status_code=status.HTTP_204_NO_CONTENT)

    


    




