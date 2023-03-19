from app import main
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

def test_middleware_cls():
    middleware = main.app.user_middleware[0]
    assert middleware.cls == CORSMiddleware

def test_middleware_allow_origins():
    middleware = main.app.user_middleware[0]
    middleware_options = middleware.options
    assert middleware_options['allow_origins'] == ['*']

def test_middleware_allow_credentials():
    middleware = main.app.user_middleware[0]
    middleware_options = middleware.options
    assert middleware_options['allow_credentials'] == True

def test_middleware_allow_methods():
    middleware = main.app.user_middleware[0]
    middleware_options = middleware.options
    assert middleware_options['allow_methods'] == ['*']

def test_middleware_allow_headers():
    middleware = main.app.user_middleware[0]
    middleware_options = middleware.options
    assert middleware_options['allow_headers'] == ['*']

def test_add_user_routes():
    route_name = 'users'
    routes = main.app.routes
    user_routes = []
    for route in routes:
        if route_name in route.path:
            user_routes.append(route)

    assert len(user_routes) == 5

def test_add_resources_routes():
    route_name = 'resources'
    routes = main.app.routes
    user_routes = []
    for route in routes:
        if route_name in route.path:
            user_routes.append(route)

    assert len(user_routes) == 5

def test_add_exercises_routes():
    route_name = 'exercises'
    routes = main.app.routes
    user_routes = []
    for route in routes:
        if route_name in route.path:
            user_routes.append(route)

    assert len(user_routes) == 5

def test_add_login_route():
    route_name = 'login'
    routes = main.app.routes
    user_routes = []
    for route in routes:
        if route_name in route.path:
            user_routes.append(route)

    assert len(user_routes) == 1

def test_add_prompt_routes():
    route_name = 'prompts'
    routes = main.app.routes
    user_routes = []
    for route in routes:
        if route_name in route.path:
            user_routes.append(route)

    assert len(user_routes) == 5

def test_add_journal_entries_route():
    route_name = 'journalentries'
    routes = main.app.routes
    user_routes = []
    for route in routes:
        if route_name in route.path:
            user_routes.append(route)

    assert len(user_routes) == 5

def test_add_completed_exercise_info_routes():
    route_name = 'completed_exercise_info'
    routes = main.app.routes
    user_routes = []
    for route in routes:
        if route_name in route.path:
            user_routes.append(route)

    assert len(user_routes) == 4

def test_add_load_all_route():
    route_name = 'loadAll'
    routes = main.app.routes
    user_routes = []
    for route in routes:
        if route_name in route.path:
            user_routes.append(route)

    assert len(user_routes) == 1

def test_root():
    root_value = main.root()
    assert root_value == "Welcome to The RSTRE Project API!!"