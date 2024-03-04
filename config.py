from pydantic import PostgresDsn
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """ Class with settings and configs for the project """
    model_config = SettingsConfigDict(env_file='.env')

    postgres: PostgresDsn
    postgres_test: PostgresDsn


settings = Settings()
