from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_prefix="BLUEMAGE_", env_file=".env")

    database_url: str = "sqlite:///./bluemage.db"
    frontend_dist: str | None = None
    runner_token: str | None = None


@lru_cache
def get_settings() -> Settings:
    return Settings()
