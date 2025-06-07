from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        # Use top level .env file (one level above ./backend/)
        env_file=".env",
    )

    ENVIRONMENT: str
    DATABASE_URL: str
    AUTH_TOKEN: str
    APP_TITLE: str
    APP_DESCRIPTION: str


settings = Settings()
print(settings)
