from app.models import schemas
from pytest import raises
from pydantic import ValidationError, BaseModel
from json import loads
from typing import List, Optional

#EXERCISES
#EXERCISE BASE
###############################################################################################
def test_exercise_base_correct():

    data = {"name": "Test Name", "description": "Test description", "image_name": "Image name"}
    exercise = schemas.Exercise.ExerciseBase(**data)
    print(exercise.dict())

    assert exercise.dict() == data

def test_exercise_base_no_name():
    data = {"description": "Test description", "image_name": "Image name"}

    try:
         schemas.Exercise.ExerciseBase(**data)
    except ValidationError as err:
        error_dict = loads(err.json())
        print(error_dict)
    

    assert raises(ValidationError)
    assert error_dict == [{'loc': ['name'], 'msg': 'field required', 'type': 'value_error.missing'}]

def test_exercise_base_no_description():
    data = {"name": "Test Name", "image_name": "Image name"}

    try:
         schemas.Exercise.ExerciseBase(**data)
    except ValidationError as err:
        error_dict = loads(err.json())
        print(error_dict)
    

    assert raises(ValidationError)
    assert error_dict == [{'loc': ['description'], 'msg': 'field required', 'type': 'value_error.missing'}]

def test_exercise_base_no_image_name():
    data = {"name": "Test Name", "description": "Test description"}

    try:
         schemas.Exercise.ExerciseBase(**data)
    except ValidationError as err:
        error_dict = loads(err.json())
        print(error_dict)
    

    assert raises(ValidationError)
    assert error_dict == [{'loc': ['image_name'], 'msg': 'field required', 'type': 'value_error.missing'}]

def test_exercise_base_extends_BaseModel():
    assert issubclass(schemas.Exercise.ExerciseBase, BaseModel)

#EXERCISE OUT
#############################################################################################################
def test_exercise_out_correct():

    data = {"id": 100, "name": "Test Name", "description": "Test description", "image_name": "Image name"}
    exercise = schemas.Exercise.ExerciseOut(**data)
    print(exercise.dict())

    assert exercise.dict() == data

def test_exercise_out_no_id():
    data = {"name": "Test Name", "description": "Test description", "image_name": "Image name"}

    try:
         schemas.Exercise.ExerciseOut(**data)
    except ValidationError as err:
        error_dict = loads(err.json())
        print(error_dict)
    

    assert raises(ValidationError)
    assert error_dict == [{'loc': ['id'], 'msg': 'field required', 'type': 'value_error.missing'}]

def test_exercise_out_extends_exercise_base():
    
    assert issubclass(schemas.Exercise.ExerciseOut, schemas.Exercise.ExerciseBase)

def test_exercise_out_orm_mode():

    assert schemas.Exercise.ExerciseOut.Config.orm_mode == True






#RESOURCES
#RESOURCE BASE
##############################################################################################################
def test_resource_base_correct():

    data = {"name": "Test Name", "url": "https://example.com", "categories": ["Category 1", "Category 2"], "text": True, "online_chat": True, "call": True}
    resource = schemas.Resource.ResourceBase(**data)
    print(resource.dict())

    assert resource.dict() == data

def test_resource_base_no_name():
    data = {"url": "https://example.com", "categories": ["Category 1", "Category 2"], "text": True, "online_chat": True, "call": True}

    try:
         schemas.Resource.ResourceBase(**data)
    except ValidationError as err:
        error_dict = loads(err.json())
        print(error_dict)
    

    assert raises(ValidationError)
    assert error_dict == [{'loc': ['name'], 'msg': 'field required', 'type': 'value_error.missing'}]

def test_resource_base_no_url():
    data = {"name": "Test Name", "categories": ["Category 1", "Category 2"], "text": True, "online_chat": True, "call": True}

    try:
         schemas.Resource.ResourceBase(**data)
    except ValidationError as err:
        error_dict = loads(err.json())
        print(error_dict)
    

    assert raises(ValidationError)
    assert error_dict == [{'loc': ['url'], 'msg': 'field required', 'type': 'value_error.missing'}]

def test_resource_base_no_categories():
    data = {"name": "Test Name", "url": "https://example.com", "text": True, "online_chat": True, "call": True}

    try:
         schemas.Resource.ResourceBase(**data)
    except ValidationError as err:
        error_dict = loads(err.json())
        print(error_dict)
    

    assert raises(ValidationError)
    assert error_dict == [{'loc': ['categories'], 'msg': 'field required', 'type': 'value_error.missing'}]

def test_resource_base_no_text():
    data = {"name": "Test Name", "url": "https://example.com", "categories": ["Category 1", "Category 2"], "online_chat": True, "call": True}

    try:
         schemas.Resource.ResourceBase(**data)
    except ValidationError as err:
        error_dict = loads(err.json())
        print(error_dict)
    

    assert raises(ValidationError)
    assert error_dict == [{'loc': ['text'], 'msg': 'field required', 'type': 'value_error.missing'}]

def test_resource_base_no_online_chat():
    data = {"name": "Test Name", "url": "https://example.com", "categories": ["Category 1", "Category 2"], "text": True, "call": True}

    try:
         schemas.Resource.ResourceBase(**data)
    except ValidationError as err:
        error_dict = loads(err.json())
        print(error_dict)
    

    assert raises(ValidationError)
    assert error_dict == [{'loc': ['online_chat'], 'msg': 'field required', 'type': 'value_error.missing'}]

def test_resource_base_no_call():
    data = {"name": "Test Name", "url": "https://example.com", "categories": ["Category 1", "Category 2"], "text": True, "online_chat": True}

    try:
         schemas.Resource.ResourceBase(**data)
    except ValidationError as err:
        error_dict = loads(err.json())
        print(error_dict)
    

    assert raises(ValidationError)
    assert error_dict == [{'loc': ['call'], 'msg': 'field required', 'type': 'value_error.missing'}]

def test_resource_base_extends_BaseModel():
    assert issubclass(schemas.Resource.ResourceBase, BaseModel)

#RESOURCE OUT
#####################################################################################################################
def test_resource_out_correct():

    data = {"id": 100, "name": "Test Name", "url": "https://example.com", "categories": ["Category 1", "Category 2"], "text": True, "online_chat": True, "call": True}
    resource = schemas.Resource.ResourceOut(**data)
    print(resource.dict())

    assert resource.dict() == data

def test_resource_out_no_id():
    data = {"name": "Test Name", "url": "https://example.com", "categories": ["Category 1", "Category 2"], "text": True, "online_chat": True, "call": True}

    try:
        schemas.Resource.ResourceOut(**data)
    except ValidationError as err:
        error_dict = loads(err.json())
        print(error_dict)
    

    assert raises(ValidationError)
    assert error_dict == [{'loc': ['id'], 'msg': 'field required', 'type': 'value_error.missing'}]

def test_resource_out_extends_resource_base():
    
    assert issubclass(schemas.Resource.ResourceOut, schemas.Resource.ResourceBase)

def test_resource_out_orm_mode():

    assert schemas.Resource.ResourceOut.Config.orm_mode == True






#PROMPT
#PROMPT BASE
###############################################################################################
def test_prompt_base_correct():
    data = {"prompt": "This is a prompt"}

    prompt = schemas.Prompt.PromptBase(**data)
    print(prompt.dict())

    assert prompt.dict() == data

def test_prompt_base_no_prompt():
    data = {}

    try:
         schemas.Prompt.PromptBase(**data)
    except ValidationError as err:
        error_dict = loads(err.json())
        print(error_dict)
    

    assert raises(ValidationError)
    assert error_dict == [{'loc': ['prompt'], 'msg': 'field required', 'type': 'value_error.missing'}]

def test_resource_base_extends_BaseModel():
    assert issubclass(schemas.Prompt.PromptOut, BaseModel)

#PROMPT OUT
#####################################################################################################################
def test_prompt_out_correct():
    data = {"id": 100,"prompt": "This is a prompt"}

    prompt = schemas.Prompt.PromptOut(**data)
    print(prompt.dict())

    assert prompt.dict() == data

def test_prompt_out_no_id():
    data = {"prompt": "This is a prompt"}

    try:
        schemas.Prompt.PromptOut(**data)
    except ValidationError as err:
        error_dict = loads(err.json())
        print(error_dict)
    

    assert raises(ValidationError)
    assert error_dict == [{'loc': ['id'], 'msg': 'field required', 'type': 'value_error.missing'}]

def test_prompt_out_extends_prompt_base():
    
    assert issubclass(schemas.Prompt.PromptOut, schemas.Prompt.PromptBase)

def test_prompt_out_orm_mode():

    assert schemas.Prompt.PromptOut.Config.orm_mode == True






#COMPLETED EXERCISE
#####################################################################################################################
def test_completed_exercise_breathing_correct():
    data = {"exercise_name": "breathing", "completed": True}

    completed_exercise = schemas.CompletedExercise(**data)
    print(completed_exercise.dict())

    assert completed_exercise.dict() == data

def test_completed_exercise_journaling_correct():
    data = {"exercise_name": "journaling", "completed": True}

    completed_exercise = schemas.CompletedExercise(**data)
    print(completed_exercise.dict())

    assert completed_exercise.dict() == data

def test_completed_exercise_stretching_correct():
    data = {"exercise_name": "stretching", "completed": True}

    completed_exercise = schemas.CompletedExercise(**data)
    print(completed_exercise.dict())

    assert completed_exercise.dict() == data

def test_completed_exercise_meditating__correct():
    data = {"exercise_name": "meditating", "completed": True}

    completed_exercise = schemas.CompletedExercise(**data)
    print(completed_exercise.dict())

    assert completed_exercise.dict() == data

def test_completed_exercise_no_exercise_name():
    data = {"completed": True}

    try:
         schemas.CompletedExercise(**data)
    except ValidationError as err:
        error_dict = loads(err.json())
        print(error_dict)
    

    assert raises(ValidationError)
    assert error_dict == [{'loc': ['exercise_name'], 'msg': 'field required', 'type': 'value_error.missing'}]

def test_completed_exercise_no_completed():
    data = {"exercise_name": "meditating"}

    try:
        schemas.CompletedExercise(**data)
    except ValidationError as err:
        error_dict = loads(err.json())
        print(error_dict)

def test_completed_exercise_exercise_name_invalid_type():
    data = {"exercise_name": "This is supposed to be the name of an exercise that exists", "completed": True}

    try:
        schemas.CompletedExercise(**data)
    except ValidationError as err:
        error_dict = loads(err.json())
        print(error_dict)
                

    assert raises(ValidationError)
    assert error_dict == [{'loc': ['exercise_name'], 'msg': '\'This is supposed to be the name of an exercise that exists\' is not a valid exercise', 'type': 'value_error'}]

def test_completed_exercise_completed_invalid_type():
    data = {"exercise_name": "breathing", "completed": "This is supposed to be a boolean"}

    try:
        schemas.CompletedExercise(**data)
    except ValidationError as err:
        error_dict = loads(err.json())
        print(error_dict)
                

    assert raises(ValidationError)
    assert error_dict == [{'loc': ['completed'], 'msg': 'value could not be parsed to a boolean', 'type': 'type_error.bool'}]

def test_completed_exercise_extends_BaseModel():
    assert issubclass(schemas.CompletedExercise, BaseModel)






#USERS
#USER DATA
#USER BASE
#############################################################################################################################
def test_user_base_correct():
    data = {"email": "example@gmail.com", "username": "test_username", "phone_number": "(123) 456-7890"}

    user = schemas.UserData.UserBase(**data)
    print(user.dict())

    assert user.dict() == data

def test_user_base_no_email():
    data = {"username": "test_username", "phone_number": "(123) 456-7890"}

    try:
         schemas.UserData.UserBase(**data)
    except ValidationError as err:
        error_dict = loads(err.json())
        print(error_dict)
    

    assert raises(ValidationError)
    assert error_dict == [{'loc': ['email'], 'msg': 'field required', 'type': 'value_error.missing'}]

def test_user_base_no_username():
    data = {"email": "example@gmail.com", "phone_number": "(123) 456-7890"}

    try:
         schemas.UserData.UserBase(**data)
    except ValidationError as err:
        error_dict = loads(err.json())
        print(error_dict)
    

    assert raises(ValidationError)
    assert error_dict == [{'loc': ['username'], 'msg': 'field required', 'type': 'value_error.missing'}]

def test_user_base_no_phone_number():
    data = {"email": "example@gmail.com", "username": "test_username"}

    user = schemas.UserData.UserBase(**data)
    print(user)

    data['phone_number'] = None
    assert user.dict() == data

def test_user_base_invalid_email():
    data = {"email": "examplegmail.com", "username": "test_username", "phone_number": "(123) 456-7890"}

    try:
        schemas.UserData.UserBase(**data)
    except ValidationError as err:
        error_dict = loads(err.json())
        print(error_dict)

    assert raises(ValidationError)
    assert error_dict == [{'loc': ['email'], 'msg': 'value is not a valid email address', 'type': 'value_error.email'}]

def test_user_base_extends_BaseModel():
    assert issubclass(schemas.UserData.UserBase, BaseModel)

#USER OUT
###################################################################################################################################
def test_user_out_correct():
    data = {"id": 100, "created_at": "2023-03-23T17:20:10.576526+00:00","email": "example@gmail.com", "username": "test_username", "password": "test_password", "phone_number": "(123) 456-7890"}

    user = schemas.UserData.UserOut(**data)
    user_dict = user.dict()
    user_dict['created_at'] = user.created_at.isoformat()
    print(user_dict)
    assert user_dict == {"id": 100, "created_at": "2023-03-23T17:20:10.576526+00:00","email": "example@gmail.com", "username": "test_username", "phone_number": "(123) 456-7890"}


def test_user_out_no_id():
    data = {"created_at": "2023-03-23T17:20:10.576526+00:00","email": "example@gmail.com", "username": "test_username", "password": "test_password", "phone_number": "(123) 456-7890"}

    try:
        schemas.UserData.UserOut(**data)
    except ValidationError as err:
        error_dict = loads(err.json())
        print(error_dict)
    

    assert raises(ValidationError)
    assert error_dict == [{'loc': ['id'], 'msg': 'field required', 'type': 'value_error.missing'}]

def test_user_out_no_created_at():
    data = {"id": 100, "email": "example@gmail.com", "username": "test_username", "password": "test_password", "phone_number": "(123) 456-7890"}

    try:
        schemas.UserData.UserOut(**data)
    except ValidationError as err:
        error_dict = loads(err.json())
        print(error_dict)
    

    assert raises(ValidationError)
    assert error_dict == [{'loc': ['created_at'], 'msg': 'field required', 'type': 'value_error.missing'}]

def test_user_out_invalid_created_at_date():
    data = {"id": 100, "created_at": "2023-03-23","email": "example@gmail.com", "username": "test_username", "password": "test_password", "phone_number": "(123) 456-7890"}

    try:
        schemas.UserData.UserOut(**data)
    except ValidationError as err:
        error_dict = loads(err.json())
        print(error_dict)
    

    assert raises(ValidationError)
    assert error_dict == [{'loc': ['created_at'], 'msg': 'invalid datetime format', 'type': 'value_error.datetime'}]


def test_user_out_extends_prompt_base():
    
    assert issubclass(schemas.UserData.UserOut, schemas.UserData.UserBase)

def test_user_out_orm_mode():

    assert schemas.UserData.UserOut.Config.orm_mode == True

#USER CREATE
def test_user_create_correct():
    data = {"email": "example@gmail.com", "username": "test_username", "password": "test_password", "phone_number": "(123) 456-7890"}

    user = schemas.UserData.UserCreate(**data)
    print(user.dict())

    assert user.dict() == data

def test_user_create_no_password():
    data = {"email": "example@gmail.com", "username": "test_username", "phone_number": "(123) 456-7890"}

    try:
         schemas.UserData.UserCreate(**data)
    except ValidationError as err:
        error_dict = loads(err.json())
        print(error_dict)
    

    assert raises(ValidationError)
    assert error_dict == [{'loc': ['password'], 'msg': 'field required', 'type': 'value_error.missing'}]

def test_user_base_extends_BaseModel():
    assert issubclass(schemas.UserData.UserCreate, schemas.UserData.UserBase)

#USER UPDATE
def test_user_update_correct():
    data = {"email": "example@gmail.com", "username": "test_username", "phone_number": "(123) 456-7890"}

    user = schemas.UserData.UserUpdate(**data)
    print(user.dict())

    assert user.dict() == data

def test_user_update_extends_user_base():
    assert issubclass(schemas.UserData.UserUpdate, schemas.UserData.UserBase)






#COMPLETED EXERCISE INFO
################################################################################################################################
def test_completed_exercise_info_base_correct():
    data = {"completed_exercises": [{"completed": True, "exercise_name": "journaling"},
                                    {"completed": True, "exercise_name": "breathing"},
                                    {"completed": False, "exercise_name": "meditating"},
                                    {"completed": False, "exercise_name": "stretching"}]
           }

    completed_exercise_info = schemas.UserData.CompletedExerciseInfo.CompletedExerciseInfoBase(**data)
    completed_exercise_info_dict = completed_exercise_info.dict()
    print(completed_exercise_info_dict)

    assert completed_exercise_info_dict == data

def test_completed_exercise_info_base_no_completed_exercises():
    data = {}

    try:
         schemas.UserData.CompletedExerciseInfo.CompletedExerciseInfoBase(**data)
    except ValidationError as err:
        error_dict = loads(err.json())
        print(error_dict)
    

    assert raises(ValidationError)
    assert error_dict == [{'loc': ['completed_exercises'], 'msg': 'field required', 'type': 'value_error.missing'}]

def test_completed_exercise_base_invalid_completed_exercises():
    data = {"completed_exercises": "This is not a list of complted exercises", "completion_date": "2023-03-23T17:20:10.576526+00:00"}

    try:
        schemas.UserData.CompletedExerciseInfo.CompletedExerciseInfoBase(**data)
    except ValidationError as err:
        error_dict = loads(err.json())
        print(error_dict)

    assert raises(ValidationError)
    assert error_dict == [{'loc': ['completed_exercises'], 'msg': 'value is not a valid list', 'type': 'type_error.list'}]

def test_user_base_extends_BaseModel():
    assert issubclass(schemas.UserData.CompletedExerciseInfo.CompletedExerciseInfoBase, BaseModel)






#TOKEN
#TOKEN OUT
#################################################################################################################
def test_token_out_correct():
    data = {"access_token": "This is the token", "token_type": "bearer"}

    token = schemas.Token.TokenOut(**data)
    print(token.dict())

    assert token.dict() == data

def test_token_out_no_access_token():
    data = {"token_type": "bearer"}

    try:
         schemas.Token.TokenOut(**data)
    except ValidationError as err:
        error_dict = loads(err.json())
        print(error_dict)
    

    assert raises(ValidationError)
    assert error_dict == [{'loc': ['access_token'], 'msg': 'field required', 'type': 'value_error.missing'}]

def test_token_out_no_token_type():
    data = {"access_token": "This is an access token"}

    try:
         schemas.Token.TokenOut(**data)
    except ValidationError as err:
        error_dict = loads(err.json())
        print(error_dict)
    

    assert raises(ValidationError)
    assert error_dict == [{'loc': ['token_type'], 'msg': 'field required', 'type': 'value_error.missing'}]

def test_token_out_invalid_token_type():
    data = {"access_token": "This is the token", "token_type": "Not Bearer"}

    try:
         schemas.Token.TokenOut(**data)
    except ValidationError as err:
        error_dict = loads(err.json())
        print(error_dict)

    assert raises(ValidationError)
    assert error_dict == [{'loc': ['token_type'], 'msg': 'Not Bearer is not a valid token type', 'type': 'value_error'}]

def test_token_out_extends_BaseModel():
    assert issubclass(schemas.Token.TokenOut, BaseModel)

#TOKEN DATA
#####################################################################################################################
def test_token_data_correct():
    data = {"user_id": 100, "admin": True}

    token = schemas.Token.TokenData(**data)
    print(token.dict())

    assert token.dict() == data

def test_token_data_no_user_id():
    data = {"admin": True}


    try:
         schemas.Token.TokenData(**data)
    except ValidationError as err:
        error_dict = loads(err.json())
        print(error_dict)
    

    assert raises(ValidationError)
    assert error_dict == [{'loc': ['user_id'], 'msg': 'field required', 'type': 'value_error.missing'}]

def test_token_data_no_admin():
    data = {"user_id": 100}


    try:
         schemas.Token.TokenData(**data)
    except ValidationError as err:
        error_dict = loads(err.json())
        print(error_dict)
    

    assert raises(ValidationError)
    assert error_dict == [{'loc': ['admin'], 'msg': 'field required', 'type': 'value_error.missing'}]

def test_token_data_invalid_id_type():
    data = {"user_id": "This should be an Interger", "admin": True}

    try:
         schemas.Token.TokenData(**data)
    except ValidationError as err:
        error_dict = loads(err.json())
        print(error_dict)

    assert raises(ValidationError)
    assert error_dict == [{'loc': ['user_id'], 'msg': 'value is not a valid integer', 'type': 'type_error.integer'}]

def test_token_data_invalid_admin_type():
    data = {"user_id": 100, "admin": "This should be a Boolean"}

    try:
         schemas.Token.TokenData(**data)
    except ValidationError as err:
        error_dict = loads(err.json())
        print(error_dict)

    assert raises(ValidationError)
    assert error_dict == [{'loc': ['admin'], 'msg': 'value could not be parsed to a boolean', 'type': 'type_error.bool'}]

def test_token_out_extends_BaseModel():
    assert issubclass(schemas.Token.TokenOut, BaseModel)






#EXTRAS
#LOADALL
#######################################################################################################################
def test_load_all_correct():
    exercises_data = {"id": 100, "name": "Test Name", "description": "Test description", "image_name": "Image name"}
    resources_data = {"id": 100, "name": "Test Name", "url": "https://example.com", "categories": ["Category 1", "Category 2"], "text": True, "online_chat": True, "call": True}
    prompts_data = {"id": 100, "prompt": "This is a prompt"}
    completed_exercise_info_data = {"completed_exercises": [{"completed": True, "exercise_name": "journaling"},
                                                            {"completed": True, "exercise_name": "breathing"},
                                                            {"completed": False, "exercise_name": "meditating"},
                                                            {"completed": False, "exercise_name": "stretching"}], 
                                    "completion_date": "2023-03-23T17:20:10.576526+00:00"}
    journal_entries_data = {"id": "asdjfl9348jk2l", "created_at": "2023-03-23T17:20:10.576526+00:00", "title": "Title", "type": "write", "tags": [], "elements": []}

    data = {"exercises": [exercises_data], "resources": [resources_data], "prompts": [prompts_data], "completed_exercise_info": completed_exercise_info_data, "journal_entries": [journal_entries_data]}

    loadAll = schemas.Extras.LoadAll(**data)
    loadAll_dict = loadAll.dict()
    loadAll_dict['completed_exercise_info']['completion_date'] = loadAll.completed_exercise_info.completion_date.isoformat()
    loadAll_dict['journal_entries'][0]['created_at'] = loadAll.journal_entries[0].created_at.isoformat()

    assert loadAll_dict == data

def test_load_all_no_exercises():
    completed_exercise_info_data = {"completed_exercises": [{"completed": True, "exercise_name": "journaling"},
                                                            {"completed": True, "exercise_name": "breathing"},
                                                            {"completed": False, "exercise_name": "meditating"},
                                                            {"completed": False, "exercise_name": "stretching"}], 
                                    "completion_date": "2023-03-23T17:20:10.576526+00:00"}

    data = { "resources": [], 
            "prompts": [], 
            "completed_exercise_info": completed_exercise_info_data, 
            "journal_entries": []}

    try:
         schemas.Extras.LoadAll(**data)
    except ValidationError as err:
        error_dict = loads(err.json())
        print(error_dict)

    assert raises(ValidationError)
    assert error_dict == [{'loc': ['exercises'], 'msg': 'field required', 'type': 'value_error.missing'}]

def test_load_all_no_resources():
    completed_exercise_info_data = {"completed_exercises": [{"completed": True, "exercise_name": "journaling"},
                                                            {"completed": True, "exercise_name": "breathing"},
                                                            {"completed": False, "exercise_name": "meditating"},
                                                            {"completed": False, "exercise_name": "stretching"}], 
                                    "completion_date": "2023-03-23T17:20:10.576526+00:00"}

    data = {"exercises": [], "prompts": [], "completed_exercise_info": completed_exercise_info_data, "journal_entries": []}

    try:
         schemas.Extras.LoadAll(**data)
    except ValidationError as err:
        error_dict = loads(err.json())
        print(error_dict)

    assert raises(ValidationError)
    assert error_dict == [{'loc': ['resources'], 'msg': 'field required', 'type': 'value_error.missing'}]

def test_load_all_no_prompts():
    completed_exercise_info_data = {"completed_exercises": [{"completed": True, "exercise_name": "journaling"},
                                                            {"completed": True, "exercise_name": "breathing"},
                                                            {"completed": False, "exercise_name": "meditating"},
                                                            {"completed": False, "exercise_name": "stretching"}], 
                                    "completion_date": "2023-03-23T17:20:10.576526+00:00"}

    data = {"exercises": [], "resources": [], "completed_exercise_info": completed_exercise_info_data, "journal_entries": []}

    try:
         schemas.Extras.LoadAll(**data)
    except ValidationError as err:
        error_dict = loads(err.json())
        print(error_dict)

    assert raises(ValidationError)
    assert error_dict == [{'loc': ['prompts'], 'msg': 'field required', 'type': 'value_error.missing'}]
    
def test_load_all_no_completed_exercise_info():

    data = {"exercises": [], "resources": [], "prompts": [], "journal_entries": []}

    try:
         schemas.Extras.LoadAll(**data)
    except ValidationError as err:
        error_dict = loads(err.json())
        print(error_dict)

    assert raises(ValidationError)
    assert error_dict == [{'loc': ['completed_exercise_info'], 'msg': 'field required', 'type': 'value_error.missing'}]

def test_load_all_no_journal_entries():

    completed_exercise_info_data = {"completed_exercises": [{"completed": True, "exercise_name": "journaling"},
                                                            {"completed": True, "exercise_name": "breathing"},
                                                            {"completed": False, "exercise_name": "meditating"},
                                                            {"completed": False, "exercise_name": "stretching"}], 
                                    "completion_date": "2023-03-23T17:20:10.576526+00:00"}

    data = {"exercises": [], "resources": [], "prompts": [], "completed_exercise_info": completed_exercise_info_data}

    try:
         schemas.Extras.LoadAll(**data)
    except ValidationError as err:
        error_dict = loads(err.json())
        print(error_dict)

    assert raises(ValidationError)
    assert error_dict == [{'loc': ['journal_entries'], 'msg': 'field required', 'type': 'value_error.missing'}]
    
def test_load_all_invalid_exercises():
    exercises_data = "This is not a valid exercise list"
    completed_exercise_info_data = {"completed_exercises": [{"completed": True, "exercise_name": "journaling"},
                                                            {"completed": True, "exercise_name": "breathing"},
                                                            {"completed": False, "exercise_name": "meditating"},
                                                            {"completed": False, "exercise_name": "stretching"}], 
                                    "completion_date": "2023-03-23T17:20:10.576526+00:00"}
    
    data = {"exercises": [exercises_data], "resources": [], "prompts": [], "completed_exercise_info": completed_exercise_info_data, "journal_entries": []}

    try:
        schemas.Extras.LoadAll(**data)
    except ValidationError as err:
        error_dict = loads(err.json())
        print(error_dict)

    assert raises(ValidationError)
    assert error_dict == [{'loc': ['exercises', 0, 'name'], 'msg': 'field required', 'type': 'value_error.missing'}, {'loc': ['exercises', 0, 'description'], 'msg': 'field required', 'type': 'value_error.missing'}, {'loc': ['exercises', 0, 'image_name'], 'msg': 'field required', 'type': 'value_error.missing'}, {'loc': ['exercises', 0, 'id'], 'msg': 'field required', 'type': 'value_error.missing'}]

def test_load_all_invalid_resources():
    resources_data = "This is not a valid resource"
    completed_exercise_info_data = {"completed_exercises": [{"completed": True, "exercise_name": "journaling"},
                                                            {"completed": True, "exercise_name": "breathing"},
                                                            {"completed": False, "exercise_name": "meditating"},
                                                            {"completed": False, "exercise_name": "stretching"}], 
                                    "completion_date": "2023-03-23T17:20:10.576526+00:00"}

    data = {"exercises": [], "resources": [resources_data], "prompts": [], "completed_exercise_info": completed_exercise_info_data, "journal_entries": []}

    try:
        schemas.Extras.LoadAll(**data)
    except ValidationError as err:
        error_dict = loads(err.json())
        print(error_dict)

    assert raises(ValidationError)
    assert error_dict == [{'loc': ['resources', 0, 'name'], 'msg': 'field required', 'type': 'value_error.missing'}, {'loc': ['resources', 0, 'url'], 'msg': 'field required', 'type': 'value_error.missing'}, {'loc': ['resources', 0, 'categories'], 'msg': 'field required', 'type': 'value_error.missing'}, {'loc': ['resources', 0, 'call'], 'msg': 'field required', 'type': 'value_error.missing'}, {'loc': ['resources', 0, 'text'], 'msg': 'field required', 'type': 'value_error.missing'}, {'loc': ['resources', 0, 'online_chat'], 'msg': 'field required', 'type': 'value_error.missing'}, {'loc': ['resources', 0, 'id'], 'msg': 'field required', 'type': 'value_error.missing'}]

def test_load_all_invalid_prompts():
    prompts_data = "This is not a valid prompt"
    completed_exercise_info_data = {"completed_exercises": [{"completed": True, "exercise_name": "journaling"},
                                                            {"completed": True, "exercise_name": "breathing"},
                                                            {"completed": False, "exercise_name": "meditating"},
                                                            {"completed": False, "exercise_name": "stretching"}], 
                                    "completion_date": "2023-03-23T17:20:10.576526+00:00"}

    data = {"exercises": [], "resources": [], "prompts": [prompts_data], "completed_exercise_info": completed_exercise_info_data, "journal_entries": []}

    try:
        schemas.Extras.LoadAll(**data)
    except ValidationError as err:
        error_dict = loads(err.json())
        print(error_dict)

    assert raises(ValidationError)
    assert error_dict == [{'loc': ['prompts', 0, 'prompt'], 'msg': 'field required', 'type': 'value_error.missing'}, {'loc': ['prompts', 0, 'id'], 'msg': 'field required', 'type': 'value_error.missing'}]

def test_load_all_invalid_completed_exercise_info():
    completed_exercise_info_data = "This is not valid completed exercise info"

    data = {"exercises": [], "resources": [], "prompts": [], "completed_exercise_info": completed_exercise_info_data, "journal_entries": []}

    try:
        schemas.Extras.LoadAll(**data)
    except ValidationError as err:
        error_dict = loads(err.json())
        print(error_dict)

    assert raises(ValidationError)
    assert error_dict == [{'loc': ['completed_exercise_info'], 'msg': 'value is not a valid dict', 'type': 'type_error.dict'}]

def test_load_all_invalid_journal_entry():
    journal_entry_data = "This is not a valid prompt"
    completed_exercise_info_data = {"completed_exercises": [{"completed": True, "exercise_name": "journaling"},
                                                            {"completed": True, "exercise_name": "breathing"},
                                                            {"completed": False, "exercise_name": "meditating"},
                                                            {"completed": False, "exercise_name": "stretching"}], 
                                    "completion_date": "2023-03-23T17:20:10.576526+00:00"}

    data = {"exercises": [], "resources": [], "prompts": [], "completed_exercise_info": completed_exercise_info_data, "journal_entries": [journal_entry_data]}

    try:
        schemas.Extras.LoadAll(**data)
    except ValidationError as err:
        error_dict = loads(err.json())
        print(error_dict)

    assert raises(ValidationError)
    assert error_dict == [{'loc': ['journal_entries', 0], 'msg': 'value is not a valid dict', 'type': 'type_error.dict'}]


def test_load_all_extends_BaseModel():
    assert issubclass(schemas.Extras.LoadAll, BaseModel)






#JOURNAL ELEMENT
#######################################################################################################
def test_journal_element_write_correct():
    data = {"type": "write", "element_data": {"text": "This is my writing"}}

    journal_element = schemas.JournalElement(**data)
    print(journal_element.dict())

    assert journal_element.dict() == data

def test_journal_element_reflection_correct():
    data = {"type": "reflection", "element_data": {"event": "This is my event", "reflection": "This is my reflection"}}

    journal_element = schemas.JournalElement(**data)
    print(journal_element.dict())

    assert journal_element.dict() == data

def test_journal_element_thanks_correct():
    data = {"type": "thanks", "element_data": {"thankful_for": "This is what I'm thankful for", "why": "This is why I am thankful"}}

    journal_element = schemas.JournalElement(**data)
    print(journal_element.dict())

    assert journal_element.dict() == data

def test_journal_element_thoughts_correct():
    data = {"type": "thoughts", "element_data": {"thoughts": ["Thought 1", "Thought 2", "Thought 3"]}}

    journal_element = schemas.JournalElement(**data)
    print(journal_element.dict())

    assert journal_element.dict() == data

def test_journal_element_prompt_correct():
    data = {"type": "prompt", "element_data": {"prompt": "This is the prompt", "prompt_id": 100, "response": "This is my response"}}

    journal_element = schemas.JournalElement(**data)
    print(journal_element.dict())

    assert journal_element.dict() == data

def test_journal_element_no_type():
    data = {"element_data": {"prompt": "This is the prompt", "response": "This is my response"}}

    try:
        schemas.JournalElement(**data)
    except ValidationError as err:
        error_dict = loads(err.json())
        print(error_dict)

    assert error_dict == [{'loc': ['type'], 'msg': 'field required', 'type': 'value_error.missing'}, {'loc': ['element_data'], 'msg': 'None is not a valid journal element type', 'type': 'value_error'}]

def test_journal_element_missing_element_data():
    data = {"type": "prompt"}

    try:
        schemas.JournalElement(**data)
    except ValidationError as err:
        error_dict = loads(err.json())
        print(error_dict)

    assert error_dict == [{'loc': ['element_data'], 'msg': 'field required', 'type': 'value_error.missing'}]


def test_journal_element_invalid_type():
    data = {"type": "Invlaid type", "element_data": {"prompt": "This is the prompt", "response": "This is my response"}}

    try:
        schemas.JournalElement(**data)
    except ValidationError as err:
        error_dict = loads(err.json())
        print(error_dict)

    assert error_dict == [{'loc': ['element_data'], 'msg': 'Invlaid type is not a valid journal element type', 'type': 'value_error'}]

def test_journal_element_extends_BaseModel():
    assert issubclass(schemas.JournalElement, BaseModel)






#WRITE ELEMENT
###############################################################################################################
def test_write_element_correct():
    data = {"text": "This is my write element"}

    write_element = schemas.JournalElement.WriteElement(**data)
    print(write_element.dict())

    assert write_element.dict() == {'text': 'This is my write element'}

def test_write_element_no_text():
    data = {}

    try:
        schemas.JournalElement.WriteElement(**data)
    
    except ValidationError as err:
        error_dict = loads(err.json())
        print(error_dict)

    assert error_dict == [{'loc': ['text'], 'msg': 'field required', 'type': 'value_error.missing'}]

def test_write_element_extends_base_model():
    assert issubclass(schemas.JournalElement.WriteElement, BaseModel)





#REFLECTION ELEMENT
def test_reflection_element_correct():
    data = {"event": "This is my event", "reflection": "This is my reflection"}

    reflection_element = schemas.JournalElement.ReflectionElement(**data)
    print(reflection_element.dict())

    assert reflection_element.dict() == {'event': 'This is my event', 'reflection': 'This is my reflection'}

def test_reflection_element_no_event():
    data = {"reflection": "This is my reflection"}

    try:
        schemas.JournalElement.ReflectionElement(**data)
    except ValidationError as err:
        error_dict = loads(err.json())
        print(error_dict)

    assert error_dict == [{'loc': ['event'], 'msg': 'field required', 'type': 'value_error.missing'}]

def test_reflection_element_no_reflection():
    data = {"event": "This is my event"}

    try:
        schemas.JournalElement.ReflectionElement(**data)
    except ValidationError as err:
        error_dict = loads(err.json())
        print(error_dict)

    assert error_dict == [{'loc': ['reflection'], 'msg': 'field required', 'type': 'value_error.missing'}]

def test_reflection_element_extends_base_model():
    assert issubclass(schemas.JournalElement.WriteElement, BaseModel)






#THANKS ELEMENT
###########################################################################################################
def test_thanks_element_correct():
    data = {"thankful_for": "This is what I am thankful for", "why": "This is why I'm thankful for it"}

    thanks_element = schemas.JournalElement.ThanksElement(**data)
    print(thanks_element.dict())

    assert thanks_element.dict() == {"thankful_for": "This is what I am thankful for", "why": "This is why I'm thankful for it"}

def test_write_element_no_thankful_for():
    data = {"why": "This is why I'm thankful for it"}

    try:
        schemas.JournalElement.ThanksElement(**data)
    
    except ValidationError as err:
        error_dict = loads(err.json())
        print(error_dict)

    assert error_dict == [{'loc': ['thankful_for'], 'msg': 'field required', 'type': 'value_error.missing'}]

def test_write_element_no_why():
    data = {"thankful_for": "This is what I am thankful for"}

    try:
        schemas.JournalElement.ThanksElement(**data)
    
    except ValidationError as err:
        error_dict = loads(err.json())
        print(error_dict)

    assert error_dict == [{'loc': ['why'], 'msg': 'field required', 'type': 'value_error.missing'}]

def test_thanks_element_extends_base_model():
    assert issubclass(schemas.JournalElement.ThanksElement, BaseModel)






#THOUGHTS ELEMENT
###########################################################################################################
def test_thoughts_element_correct():
    data = {"thoughts": ["Thought 1", "THought 2", "Thought 3"]}

    thoughts_element = schemas.JournalElement.ThoughtsElement(**data)
    print(thoughts_element.dict())

    assert thoughts_element.dict() == {"thoughts": ["Thought 1", "THought 2", "Thought 3"]}

def test_thoughts_element_no_thoughts():
    data = {}

    try:
        schemas.JournalElement.ThoughtsElement(**data)
    
    except ValidationError as err:
        error_dict = loads(err.json())
        print(error_dict)

    assert error_dict == [{'loc': ['thoughts'], 'msg': 'field required', 'type': 'value_error.missing'}]

def test_thoughts_element_extends_base_model():
    assert issubclass(schemas.JournalElement.ThoughtsElement, BaseModel)






#PROMPT ELEMENT
###########################################################################################################
def test_prompt_element_correct():
    data = {"prompt": "This is a prompt", "prompt_id": 100, "response": 'This is my prompt response'}

    prompt_element = schemas.JournalElement.PromptElement(**data)
    print(prompt_element.dict())

    assert prompt_element.dict() == {"prompt": "This is a prompt", "prompt_id": 100, "response": 'This is my prompt response'}

def test_prompt_element_no_prompts():
    data = {"prompt_id": 100, "response": 'This is my prompt response'}

    try:
        schemas.JournalElement.PromptElement(**data)
    
    except ValidationError as err:
        error_dict = loads(err.json())
        print(error_dict)

    assert error_dict == [{'loc': ['prompt'], 'msg': 'field required', 'type': 'value_error.missing'}]

def test_prompt_element_no_prompt_id():
    data = {"prompt": "This is a prompt", "response": 'This is my prompt response'}

    try:
        schemas.JournalElement.PromptElement(**data)
    
    except ValidationError as err:
        error_dict = loads(err.json())
        print(error_dict)

    assert error_dict == [{'loc': ['prompt_id'], 'msg': 'field required', 'type': 'value_error.missing'}]

def test_prompt_element_no_response():
    data = {"prompt": "This is a prompt", "prompt_id": 100}

    try:
        schemas.JournalElement.PromptElement(**data)
    
    except ValidationError as err:
        error_dict = loads(err.json())
        print(error_dict)

    assert error_dict == [{'loc': ['response'], 'msg': 'field required', 'type': 'value_error.missing'}]

def test_prompt_element_extends_base_model():
    assert issubclass(schemas.JournalElement.PromptElement, BaseModel)






#JOURNAL ENTRY
#JOURNAL ENTRY BASE
###########################################################################################################
def test_journal_entry_base_correct():
    data = {"title": "This is a title", "type": "This is the type", "tags": ["Tag 1", "Tag 2", "Tag 3"], "elements": []}

    journal_entry = schemas.UserData.JournalEntry.JournalEntryBase(**data)
    print(journal_entry.dict())

    assert journal_entry.dict() == {'title': 'This is a title', 'type': 'This is the type', 'tags': ['Tag 1', 'Tag 2', 'Tag 3'], 'elements': []}

def test_journal_entry_base_element_type_correct():
    print(schemas.UserData.JournalEntry.JournalEntryBase.__fields__['elements'])
    assert str(schemas.UserData.JournalEntry.JournalEntryBase.__fields__['elements']) == "name='elements' type=List[JournalElement] required=True"

def test_journal_entry_base_no_title():
    data = {"type": "This is the type", "tags": ["Tag 1", "Tag 2", "Tag 3"], "elements": []}

    try:
        schemas.UserData.JournalEntry.JournalEntryBase(**data)
    except ValidationError as err:
        error_dict = loads(err.json())
        print(error_dict)

    assert error_dict == [{'loc': ['title'], 'msg': 'field required', 'type': 'value_error.missing'}]

def test_journal_entry_base_no_type():
    data = {"title": "This is a title", "tags": ["Tag 1", "Tag 2", "Tag 3"], "elements": []}

    try:
        schemas.UserData.JournalEntry.JournalEntryBase(**data)
    except ValidationError as err:
        error_dict = loads(err.json())
        print(error_dict)

    assert error_dict == [{'loc': ['type'], 'msg': 'field required', 'type': 'value_error.missing'}]

def test_journal_entry_base_no_tags():
    data = {"title": "This is a title", "type": "This is the type", "elements": []}

    try:
        schemas.UserData.JournalEntry.JournalEntryBase(**data)
    except ValidationError as err:
        error_dict = loads(err.json())
        print(error_dict)

    assert error_dict == [{'loc': ['tags'], 'msg': 'field required', 'type': 'value_error.missing'}]

def test_journal_entry_base_no_elements():
    data = {"title": "This is a title", "type": "This is the type", "tags": ["Tag 1", "Tag 2", "Tag 3"]}

    try:
        schemas.UserData.JournalEntry.JournalEntryBase(**data)
    except ValidationError as err:
        error_dict = loads(err.json())
        print(error_dict)

    assert error_dict == [{'loc': ['elements'], 'msg': 'field required', 'type': 'value_error.missing'}]

def test_journal_entry_extends_base_model():
    assert  issubclass(schemas.UserData.JournalEntry.JournalEntryBase, BaseModel)





#JOURNAL ENTRY OUT
###########################################################################################################
def test_journal_entry_out_correct():
    data = {"id": "kjdsj3kj4-kdmek2o3-234n34k", "created_at": "2023-03-23T17:20:10.576526+00:00", "title": "This is a title", "type": "This is the type", "tags": ["Tag 1", "Tag 2", "Tag 3"], "elements": []}

    journal_entry = schemas.UserData.JournalEntry.JournalEntryOut(**data)
    journal_entry_dict = journal_entry.dict()
    journal_entry_dict['created_at'] = journal_entry.created_at.isoformat()
    print(journal_entry_dict)

    assert journal_entry_dict == {'title': 'This is a title', 'type': 'This is the type', 'tags': ['Tag 1', 'Tag 2', 'Tag 3'], 'elements': [], 'id': 'kjdsj3kj4-kdmek2o3-234n34k', 'created_at': '2023-03-23T17:20:10.576526+00:00'}

def test_journal_entry_out_no_id():
    data = {"created_at": "2023-03-23T17:20:10.576526+00:00", "title": "This is a title", "type": "This is the type", "tags": ["Tag 1", "Tag 2", "Tag 3"], "elements": []}

    try:
        schemas.UserData.JournalEntry.JournalEntryOut(**data)
    except ValidationError as err:
        error_dict = loads(err.json())
        print(error_dict)

    assert error_dict == [{'loc': ['id'], 'msg': 'field required', 'type': 'value_error.missing'}]

def test_journal_entry_out_no_created_at():
    data = {"id": "kjdsj3kj4-kdmek2o3-234n34k", "title": "This is a title", "type": "This is the type", "tags": ["Tag 1", "Tag 2", "Tag 3"], "elements": []}

    try:
        schemas.UserData.JournalEntry.JournalEntryOut(**data)
    except ValidationError as err:
        error_dict = loads(err.json())
        print(error_dict)

    assert error_dict == [{'loc': ['created_at'], 'msg': 'field required', 'type': 'value_error.missing'}]

def test_journal_entry_out_invalid_created_at():
    data = {"id": "kjdsj3kj4-kdmek2o3-234n34k", "created_at": "2023-03-23", "title": "This is a title", "type": "This is the type", "tags": ["Tag 1", "Tag 2", "Tag 3"], "elements": []}

    try:
        schemas.UserData.JournalEntry.JournalEntryOut(**data)
    except ValidationError as err:
        error_dict = loads(err.json())
        print(error_dict)

    assert error_dict == [{'loc': ['created_at'], 'msg': 'invalid datetime format', 'type': 'value_error.datetime'}]

def test_journal_entry_out_extends_journal_entry_base():
    assert issubclass(schemas.UserData.JournalEntry.JournalEntryOut, schemas.UserData.JournalEntry.JournalEntryBase)