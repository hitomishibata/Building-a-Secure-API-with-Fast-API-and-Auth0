from functools import lru_cache
from pydantic import BaseSettings

class Settings(BaseSettings):
    auth0_domain: str
    auth0_audience: str
    auth0_client: str
    auth0_algorithms: str

    class Config:
        env_file = ".env"

@lru_cache()
def get_settings():
    return Settings()