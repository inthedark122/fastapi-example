
from typing import List
from ..schemas.users import UserCreate, UserInDB

users: List[UserInDB] = []

def add_user(user: UserCreate) -> UserInDB:
    user_id = 1 if len(users) == 0 else users[-1].id + 1
    user = UserInDB(
        id=user_id,
        first_name=user.first_name,
        last_name=user.last_name
    )
    users.append(user)

    return user

def remove_user(user_id: int) -> None:
    user = next((u for u in users if u.id == user_id), None)

    if user:
        users.remove(user)


def get_users() -> List[UserInDB]:
    return users