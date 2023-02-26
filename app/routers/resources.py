from typing import Optional, List
from fastapi import FastAPI, Response, status, HTTPException, APIRouter, Depends
from sqlalchemy.orm import Session
from ..models import sa_models
from ..models.schemas import Resource
from ..utilities import oauth2, utils
from .. import database

router = APIRouter(
    prefix="/resources",
    tags=["Resources"]
)

@router.get("/", response_model=List[Resource.ResourceOut])
def get_resources(db: Session = Depends(database.get_db)):
   
    query = db.query(sa_models.Resource)
    resources = query.all()

    return resources

@router.post("/", response_model=List[Resource.ResourceOut], status_code=status.HTTP_201_CREATED)
def create_resource(resources: List[Resource.ResourceBase], db: Session = Depends(database.get_db), current_user: int = Depends(oauth2.get_current_user)):

    if not current_user.admin:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=f"User with id: {current_user.id} is not an admin")

    updated_resources = []

    for resource in resources:
        new_resource = sa_models.Resource(**resource.dict())
        updated_resources.append(new_resource)
        db.add(new_resource)
        db.commit()
        db.refresh(new_resource)

    return updated_resources

@router.get("/{id}", response_model=Resource.ResourceOut)
def get_resource(id: int, db: Session = Depends(database.get_db)):

    resource = db.query(sa_models.Resource).filter(sa_models.Resource.id == id).first()

    if not resource:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Resource with id: {id} does not exist")

    return resource

@router.put("/{id}", response_model=Resource.ResourceOut)
def update_resource(id: int, updated_resource: Resource.ResourceBase, db: Session = Depends(database.get_db), current_user: int = Depends(oauth2.get_current_user)):

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

    


    




