from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """ Class with settings and configs for the project """
    model_config = SettingsConfigDict(env_file='.env', extra='ignore')

    app_host: str
    app_port: int

    postgres_host: str
    postgres_db: str
    postgres_password: str
    postgres_user: str
    postgres_port: int

    postgres_host_test: str
    postgres_db_test: str
    postgres_password_test: str
    postgres_user_test: str
    postgres_port_test: int


settings = Settings()
