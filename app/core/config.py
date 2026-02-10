from functools import lru_cache

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "URL Shortener"
    environment: str = Field(default="dev", examples=["dev", "prod", "test"])
    debug: bool = True

    host: str = "127.0.0.1"
    port: int = 8000

    database_path: str = "db.sqlite3"

    short_code_length: int = 7

    model_config = SettingsConfigDict(
        env_file=".env",
        env_prefix="APP_",
    )


@lru_cache
def get_settings() -> Settings:
    return Settings()  # type: ignore[arg-type]
