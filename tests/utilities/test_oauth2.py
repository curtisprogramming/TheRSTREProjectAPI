from app.utilities import oauth2
from pytest import raises
from fastapi import HTTPException, status
from pydantic import ValidationError
from json import loads
from datetime import datetime, timedelta
from jose import jwt
from app.config import settings

credentials_exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, 
    detail=f"Could not validate credentials", headers={"WWW-Authenticate": "Bearer"})

def test_create_verify_access_token_correct():
    data = {'user_id': 100, 'admin': True}
    JWT_token = oauth2.create_access_token(data)

    assert oauth2.verify_access_token(JWT_token, credentials_exception)

def test_create_access_token_incorrect():
    data = {'user_id': 100, 'admin': True}

    try:
        JWT_token = oauth2.create_access_token(data) + "Im wrong now hehehehe"
        oauth2.verify_access_token(JWT_token, credentials_exception)

    except HTTPException as err:
        error_dict = err.__dict__
        print(error_dict)
    
    assert raises(HTTPException)
    assert error_dict == {'status_code': 401, 'detail': 'Could not validate credentials', 'headers': {'WWW-Authenticate': 'Bearer'}}

def test_create_access_token_wrong_user_id_key():
    data = {'incorrect_user_id_key': 100, 'admin': True}

    try:
        oauth2.create_access_token(data)
    except ValidationError as err:
        error_dict = loads(err.json())
        print(error_dict)
        
    assert raises(ValidationError)
    assert error_dict == [{'loc': ['user_id'], 'msg': 'field required', 'type': 'value_error.missing'}]

def test_create_access_token_wrong_user_admin_key():
    data = {'user_id': 100, 'incorrect_admin_key': True}

    try:
        oauth2.create_access_token(data)
    except ValidationError as err:
        error_dict = loads(err.json())
        print(error_dict)
        
    assert raises(ValidationError)
    assert error_dict == [{'loc': ['admin'], 'msg': 'field required', 'type': 'value_error.missing'}]


def test_create_access_token_wrong_user_id_type():
    data = {'user_id': "This should be an integer", 'admin': True}

    try:
        oauth2.create_access_token(data)
    except ValidationError as err:
        error_dict = loads(err.json())
        print(error_dict)

    assert raises(ValidationError)
    assert error_dict == [{'loc': ['user_id'], 'msg': 'value is not a valid integer', 'type': 'type_error.integer'}]


def test_create_access_token_wrong_admin_type():
    data = {'user_id': 100, 'admin': "This should be a boolean"}

    try:
        oauth2.create_access_token(data)
    except ValidationError as err:
        error_dict = loads(err.json())
        print(error_dict)

    assert raises(ValidationError)
    assert error_dict == [{'loc': ['admin'], 'msg': 'value could not be parsed to a boolean', 'type': 'type_error.bool'}]

def test_verify_access_token_user_id_correct():
    data = {'user_id': 100, 'admin': True}
    JWT_token = oauth2.create_access_token(data)
    JWT_data = oauth2.verify_access_token(JWT_token, credentials_exception)
    assert JWT_data.user_id == 100

def test_verify_access_token_admin_correct():
    data = {'user_id': 100, 'admin': True}
    JWT_token = oauth2.create_access_token(data)
    JWT_data = oauth2.verify_access_token(JWT_token, credentials_exception)
    assert JWT_data.admin == True

def test_verify_acces_token_no_id():

    SECRET_KEY = settings.secret_key
    ALGORITHM = settings.algorithm
    ACCESS_TOKEN_EXPIRE_MINUTES = settings.access_token_expire_minutes  

    data = {'user_id': None, 'admin': True}
    to_encode = data.copy()

    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})

    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

    try:
        oauth2.verify_access_token(encoded_jwt, credentials_exception)
    except HTTPException as err:
        err_dict = err.__dict__
        print(err_dict)

    assert raises(HTTPException)
    assert err_dict == {'status_code': 401, 'detail': 'Could not validate credentials', 'headers': {'WWW-Authenticate': 'Bearer'}}

def test_verify_acces_token_no_admin():

    SECRET_KEY = settings.secret_key
    ALGORITHM = settings.algorithm
    ACCESS_TOKEN_EXPIRE_MINUTES = settings.access_token_expire_minutes  

    data = {'user_id': 100, 'admin': None}
    to_encode = data.copy()

    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})

    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

    try:
        oauth2.verify_access_token(encoded_jwt, credentials_exception)
    except HTTPException as err:
        err_dict = err.__dict__
        print(err_dict)

    assert raises(HTTPException)
    assert err_dict == {'status_code': 401, 'detail': 'Could not validate credentials', 'headers': {'WWW-Authenticate': 'Bearer'}}