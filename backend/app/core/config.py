from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    secret_key: str = "secret"

settings = Settings()
