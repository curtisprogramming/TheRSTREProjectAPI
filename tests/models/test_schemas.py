from app.models import schemas
from pytest import raises
from pydantic import ValidationError
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

#RESOURCE OUT
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