from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file='.env', env_file_encoding='utf-8')

    database_host: str = Field("localhost", alias="DB_HOST")
    database_port: str = Field("5432", alias="DB_PORT")
    database_username: str = Field("admin", alias="DB_USER")
    database_password: str = Field("admin", alias="DB_PASSWORD")
