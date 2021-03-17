import requests
import pytest
from typing import Generator, Dict
from fastapi_example.db import db

@pytest.fixture
def user_form() -> Generator[Dict[str, str], None, None]:
    yield {"first_name": "first", "last_name": "user"}

def test_create_first_user(client: requests.Session, user_form: Dict[str, str]) -> None:
    response = client.post("/api/v1/users/", json=user_form)
    user = response.json()
    assert user["first_name"] == user_form["first_name"]
    assert user["last_name"] == user_form["last_name"]
    assert len(db.get_users()) == 1

def test_create_second_user(client: requests.Session, user_form: Dict[str, str]) -> None:
    response = client.post("/api/v1/users/", json=user_form)
    user = response.json()
    assert user["first_name"] == user_form["first_name"]
    assert user["last_name"] == user_form["last_name"]
    assert len(db.get_users()) == 1