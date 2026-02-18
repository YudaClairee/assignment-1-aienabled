from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    APP_NAME: str = "Asset Management App for Pribadi"
    VERSION: str = "0.0.1"
    JWT_EXPIRE_MINUTES: int = 1
    SECRET_KEY: str = "not-very-secret"

    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()
