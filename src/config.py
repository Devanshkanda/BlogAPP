from pydantic_settings import BaseSettings, SettingsConfigDict

class EnvConfigSettings(BaseSettings):
    mongodb_uri: str | None
    db_name: str | None

    model_config = SettingsConfigDict(env_file=".env")