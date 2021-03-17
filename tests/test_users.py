import pytest
import requests
from fastapi_example.db import db
from fastapi_example.schemas.users import UserCreate

@pytest.mark.skip
def test_users(client: requests.Session) -> None:
    user = db.add_user(UserCreate(first_name="other", last_name="user"))
    response = client.get("/api/v1/users/")
    assert next(u for u in response.json() if u["id"] == user.id)