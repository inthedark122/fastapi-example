from pydantic import BaseModel

class BaseUser(BaseModel):
    class Config:
        "https://pydantic-docs.helpmanual.io/usage/model_config/"
        allow_population_by_field_name = True

class UserCreate(BaseModel):
    first_name: str
    last_name: str

class UserInDB(UserCreate):
    id: int

class UserResponse(UserInDB):
    pass