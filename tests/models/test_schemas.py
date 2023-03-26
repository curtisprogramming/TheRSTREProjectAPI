from app.models import schemas
from pytest import raises
from pydantic import ValidationError, BaseModel
from json import loads

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
    data = {"completed_exercises": [{"exercise_name": "breathing", "completed": True}], "completion_date": "2023-03-23T17:20:10.576526+00:00"}

    completed_exercise_info = schemas.UserData.CompletedExerciseInfo(**data)
    completed_exercise_info_dict = completed_exercise_info.dict()
    completed_exercise_info_dict['completion_date'] = completed_exercise_info.completion_date.isoformat()
    print(completed_exercise_info_dict)

    assert completed_exercise_info_dict == data

def test_completed_exercise_info_base_no_completed_exercises():
    data = {"completion_date": "2023-03-23T17:20:10.576526+00:00"}

    try:
         schemas.UserData.CompletedExerciseInfo(**data)
    except ValidationError as err:
        error_dict = loads(err.json())
        print(error_dict)
    

    assert raises(ValidationError)
    assert error_dict == [{'loc': ['completed_exercises'], 'msg': 'field required', 'type': 'value_error.missing'}]

def test_completed_exercise_info_base_no_completion_date():
    data = {"completed_exercises": [{"exercise_name": "breathing", "completed": True}]}

    try:
         schemas.UserData.CompletedExerciseInfo(**data)
    except ValidationError as err:
        error_dict = loads(err.json())
        print(error_dict)
    

    assert raises(ValidationError)
    assert error_dict == [{'loc': ['completion_date'], 'msg': 'field required', 'type': 'value_error.missing'}]

def test_completed_exercise_base_invalid_completed_exercises():
    data = {"completed_exercises": "This is not a list of complted exercises", "completion_date": "2023-03-23T17:20:10.576526+00:00"}

    try:
        schemas.UserData.CompletedExerciseInfo(**data)
    except ValidationError as err:
        error_dict = loads(err.json())
        print(error_dict)

    assert raises(ValidationError)
    assert error_dict == [{'loc': ['completed_exercises'], 'msg': 'value is not a valid list', 'type': 'type_error.list'}]

def test_completed_exercise_base_invalid_completion_date():
    data = {"completed_exercises": [{"exercise_name": "breathing", "completed": True}], "completion_date": "2023-03-23"}

    try:
        schemas.UserData.CompletedExerciseInfo(**data)
    except ValidationError as err:
        error_dict = loads(err.json())
        print(error_dict)

    assert raises(ValidationError)
    assert error_dict == [{'loc': ['completion_date'], 'msg': 'invalid datetime format', 'type': 'value_error.datetime'}]

def test_user_base_extends_BaseModel():
    assert issubclass(schemas.UserData.CompletedExerciseInfo, BaseModel)






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
