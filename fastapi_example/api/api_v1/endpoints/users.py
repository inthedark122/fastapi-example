from fastapi import APIRouter

router = APIRouter()

from typing import Any, List

from fastapi_example.schemas.users import UserResponse, UserCreate
from fastapi_example.db import db

@router.get("/")
def index() -> List[UserResponse]:
    return [UserResponse(**u.dict()) for u in db.get_users()]

@router.post("/")
def create_user(user_in: UserCreate) -> UserResponse:
    user_new = db.add_user(user_in)

    return UserResponse(**user_new.dict())
