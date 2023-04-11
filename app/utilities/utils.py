from passlib.context import CryptContext

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

class Search:

    def linear_search_id(arr, target):

        for i in range(len(arr)):
            if arr[i]['id'] == target:
                return i

        return -1