from app import database
from app.config import settings
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

def test_database_url():
    correct_url = f'postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}'
    assert database.SQLALCHEMY_DATABASE_URL == correct_url

def test_db_bind():
    url = f'postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}'
    correct_bind = create_engine(url)
    session = database.get_db()
    assert f'{session.__next__().bind}' == f'{correct_bind}'

def test_db_autocommit():
    correct_value = False
    session = database.get_db()
    assert session.__next__().autocommit == correct_value

def test_db_autoflush():
    correct_value = False
    session = database.get_db()
    assert session.__next__().autoflush == correct_value
