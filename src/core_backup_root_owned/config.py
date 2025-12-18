from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "Leads API"
    mongodb_uri: str = "mongodb://root:example@mongodb:27017/?authSource=admin"
    mongodb_db: str = "blips"
    dummy_user_url: str = "https://dummyjson.com/users/1"
    port: int = 8000

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")


settings = Settings()
