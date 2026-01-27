from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "Bombacar Nayo"
    database_url: str = "postgresql+asyncpg://user:pass@localhost:5432/bombacar_nayo"
    db_ssl_no_verify: bool = False
    secret_key: str = "change-me"
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 60 * 8

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")


settings = Settings()
