from decouple import config
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = config("APP_NAME", default="Leads API")
    mongodb_uri: str = config(
        "MONGODB_URI", default="mongodb://root:example@mongodb:27017/?authSource=admin"
    )
    mongodb_db: str = config("MONGODB_DB", default="blips")
    dummy_user_url: str = config("DUMMY_USER_URL", default="https://dummyjson.com/users/1")
    port: int = config("PORT", default=8000, cast=int)

    model_config = SettingsConfigDict(extra="ignore")


settings = Settings()
