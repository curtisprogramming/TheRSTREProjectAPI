from app.utilities import utils
from app.models import sa_models
from passlib.context import CryptContext
import pytest

def test_hash_verify():
    pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
    test_data = "fakepasswordtohash"
    hashed_test_data = pwd_context.hash(test_data)
    
    assert utils.verify(test_data, hashed_test_data)

def test_row_to_dict():
    row = sa_models.Prompt
    row.prompt = "This is a test prompt"
    row.id = 100
    row_dict = utils.row_to_dict(row=row)
    correct_dict = {'prompt': 'This is a test prompt', 'id': 100}
    assert row_dict == correct_dict



    