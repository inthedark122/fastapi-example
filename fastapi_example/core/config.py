from pydantic import BaseSettings

class Settings(BaseSettings):
    description: str = "Please use environment variable"

settings = Settings()
