from passlib.context import CryptContext
from fastapi import Depends
from .. import main

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash(data: str):
    hash = pwd_context.hash(data)
    return hash

def verify(plain_pwd, hashed_pwd):
    return pwd_context.verify(plain_pwd, hashed_pwd)

def row_to_dict(row):

    converted_dict = {}
    for column in row.__table__.columns:
        converted_dict[column.name] = getattr(row, column.name)

    return converted_dict