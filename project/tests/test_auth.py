import json
from tests.random import random_email, random_password, random_username

def test_login_for_access_token(test_app_with_db):
    _user = random_username()
    _email = random_email()
    _password = random_password()
    
    response = test_app_with_db.post("/users/create",data=json.dumps(
        {"user_name": _user, "email": _email, "password": _password}))
    assert response.status_code == 201
    assert response.json()['user_name'] == _user
    assert response.json()['email'] == _email
    response = test_app_with_db.post("/users/token",data=json.dumps(
        {"username": _user, "password": _password}))
    assert response.status_code == 200
    assert response.json()['access_token'] is not None
    assert response.json()['token_type'] == 'bearer'