from typing import List

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    base_url: str
    model_config = SettingsConfigDict(env_file='.env', env_file_encoding='utf-8')

    database_host: str = Field("localhost", alias="DB_HOST")
    database_port: str = Field("5432", alias="DB_PORT")
    database_name: str = Field("dndhelper", alias="DB_NAME")
    database_username: str = Field("admin", alias="DB_USER")
    database_password: str = Field("admin", alias="DB_PASSWORD")

    whitelist: List[str] = [
        "http://127.0.0.1:5173",
        "http://localhost"
    ]

    @property
    def database_url(self):
        return f"postgresql://{self.database_username}:{self.database_password}@{self.database_host}:{self.database_port}/{self.database_name}"


settings = Settings()
