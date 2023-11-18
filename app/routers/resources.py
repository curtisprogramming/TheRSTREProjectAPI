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
    """
    Get a list of resources.

    Parameters:
      db (Session): Database session.

    Returns:
      List[Resource.ResourceOut]: List of resources.
    """
    query = db.query(sa_models.Resource)
    resources = query.all()

    return resources

@router.post("/", response_model=List[Resource.ResourceOut], status_code=status.HTTP_201_CREATED)
def create_resource(
    resources: List[Resource.ResourceBase],
    db: Session = Depends(database.get_db),
    current_user: int = Depends(oauth2.get_current_user)
):
    """
    Create new resources.

    Parameters:
      resources (List[Resource.ResourceBase]): List of resources to create.
      db (Session): Database session.
      current_user (int): Current user ID.

    Returns:
      List[Resource.ResourceOut]: List of created resources.
    """
    if not current_user.admin:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=f"User with id: {current_user.id} is not an admin")

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
    """
    Get a resource by ID.

    Parameters:
      id (int): Resource ID.
      db (Session): Database session.

    Returns:
      Resource.ResourceOut: The requested resource.
    """
    resource = db.query(sa_models.Resource).filter(sa_models.Resource.id == id).first()

    if not resource:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Resource with id: {id} does not exist")

    return resource

@router.put("/{id}", response_model=Resource.ResourceOut)
def update_resource(
    id: int,
    updated_resource: Resource.ResourceBase,
    db: Session = Depends(database.get_db),
    current_user: int = Depends(oauth2.get_current_user)
):
    """
    Update a resource by ID.

    Parameters:
      id (int): Resource ID.
      updated_resource (Resource.ResourceBase): Updated resource data.
      db (Session): Database session.
      current_user (int): Current user ID.

    Returns:
      Resource.ResourceOut: The updated resource.
    """
    resource_query = db.query(sa_models.Resource).filter(sa_models.Resource.id == id)
    resource = resource_query.first()

    if not resource:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Resource with id: {id} does not exist")

    if not current_user.admin:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=f"User with id: {current_user.id} is not an admin")

    resource_query.update(updated_resource.dict(), synchronize_session=False)
    db.commit()

    return resource

@router.delete("/{id}")
def delete_resources(
    id: int,
    db: Session = Depends(database.get_db),
    current_user: int = Depends(oauth2.get_current_user)
):
    """
    Delete a resource by ID.

    Parameters:
      id (int): Resource ID.
      db (Session): Database session.
      current_user (int): Current user ID.

    Returns:
      Response: HTTP response indicating success.
    """
    resource_query = db.query(sa_models.Resource).filter(sa_models.Resource.id == id)
    resource = resource_query.first()

    if not resource:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Resource with id: {id} does not exist")

    if not current_user.admin:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=f"User with id: {current_user.id} is not an admin")

    resource_query.delete(synchronize_session=False)
    db.commit()

    return Response(status_code=status.HTTP_204_NO_CONTENT)