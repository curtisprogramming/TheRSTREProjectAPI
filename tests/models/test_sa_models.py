from app.models import sa_models
from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.dialects.postgresql import ARRAY, JSONB






#USER TABLE
########################################################################
def test_user_table_name():
    assert sa_models.User.__tablename__ == "users"

def test_user_table_id_column():
    id_column = sa_models.User.id
    assert type(id_column.type) == Integer
    assert id_column.primary_key == True
    assert id_column.nullable == False

def test_user_table_admin_column():
    admin_column = sa_models.User.admin
    assert type(admin_column.type) == Boolean
    assert admin_column.nullable == False
    assert admin_column.server_default.arg.text == 'False'

def test_user_table_username_column():
    username_column = sa_models.User.username
    assert type(username_column.type) == String
    assert username_column.nullable == False
    assert username_column.unique == True

def test_user_table_email_column():
    email_column = sa_models.User.email
    assert type(email_column.type) == String
    assert email_column.nullable == False
    assert email_column.unique == True

def test_user_table_password_column():
    password_column = sa_models.User.password
    assert type(password_column.type) == String
    assert password_column.nullable == False

def test_user_table_created_at_column():
    created_at_column = sa_models.User.created_at
    assert type(created_at_column.type) == TIMESTAMP
    assert created_at_column.type.timezone == True
    assert created_at_column.nullable == False
    assert created_at_column.server_default.arg.text == 'now()'

def test_user_table_phone_number_column():
    phone_number_column = sa_models.User.phone_number
    assert type(phone_number_column.type) == String
    assert phone_number_column.nullable == True

def test_user_table_completed_exercise_info_column():
    completed_exercise_info_column = sa_models.User.completed_exercise_info
    assert type(completed_exercise_info_column.type) == JSONB
    assert completed_exercise_info_column.nullable == False
    assert completed_exercise_info_column.server_default.arg.text == "'{}'::jsonb"

def test_user_table_journal_entries_column():
    journal_entries_column = sa_models.User.journal_entries
    assert type(journal_entries_column.type) == JSONB
    assert journal_entries_column.nullable == True
    assert journal_entries_column.server_default.arg.text == "'[]'::jsonb"






#RESOURCE TABLE
########################################################################
def test_resource_table_name():
    assert sa_models.Resource.__tablename__ == "resources"

def test_resource_table_id_column():
    id_column = sa_models.Resource.id
    assert type(id_column.type) == Integer
    assert id_column.primary_key == True
    assert id_column.nullable == False

def test_resource_table_name_column():
    name_column = sa_models.Resource.name
    assert type(name_column.type) == String
    assert name_column.nullable == False

def test_resource_table_url_column():
    url_column = sa_models.Resource.url
    assert type(url_column.type) == String
    assert url_column.nullable == False

def test_resource_table_categories_column():
    categories_column = sa_models.Resource.categories
    assert type(categories_column.type) == ARRAY
    assert categories_column.nullable == False

def test_resource_table_call_column():
    categories_column = sa_models.Resource.call
    assert type(categories_column.type) == Boolean
    assert categories_column.nullable == False

def test_resource_table_text_column():
    text_column = sa_models.Resource.text
    assert type(text_column.type) == Boolean
    assert text_column.nullable == False
    
def test_resource_table_online_chat_column():
    online_chat__column = sa_models.Resource.online_chat
    assert type(online_chat__column.type) == Boolean
    assert online_chat__column.nullable == False






#EXERCISE TABLE
########################################################################
def test_exercise_table_name():
    assert sa_models.Exercise.__tablename__ == "exercises"

def test_exercise_table_id_column():
    id_column = sa_models.Exercise.id
    assert type(id_column.type) == Integer
    assert id_column.primary_key == True
    assert id_column.nullable == False

def test_exercise_table_name_column():
    name_column = sa_models.Exercise.name
    assert type(name_column.type) == String
    assert name_column.nullable == False

def test_exercise_table_description_column():
    description_column = sa_models.Exercise.description
    assert type(description_column.type) == String
    assert description_column.nullable == False

def test_exercise_table_image_name_column():
    image_name_column = sa_models.Exercise.image_name
    assert type(image_name_column.type) == String
    assert image_name_column.nullable == False






#PROMPT TABLE
########################################################################
def test_prompt_table_name():
    assert sa_models.Prompt.__tablename__ == "prompts"

def test_prompt_table_id_column():
    id_column = sa_models.Prompt.id
    assert type(id_column.type) == Integer
    assert id_column.primary_key == True
    assert id_column.nullable == False

def test_exercise_table_prompt_column():
    prompt_column = sa_models.Prompt.prompt
    assert type(prompt_column.type) == String
    assert prompt_column.nullable == False

