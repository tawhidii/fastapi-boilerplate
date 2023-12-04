import json
from tests.random import random_email, random_password, random_username


def test_create_user(test_app_with_db):
    _user = random_username()
    _email = random_email()
    _password = random_password()
    response = test_app_with_db.post("/users/create",data=json.dumps(
        {"user_name": _user, "email": _email, "password": _password}))
    assert response.status_code == 201
    assert response.json()['user_name'] == _user
    assert response.json()['email'] == _email


