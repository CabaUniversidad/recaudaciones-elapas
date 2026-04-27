import os
from pydantic_settings import BaseSettings, SettingsConfigDict

ENV = os.getenv("ENV", "local")  # export ENV=production / local: export ENV=local

env_file = f".env.{ENV}"

class Settings(BaseSettings):
    PROJECT_NAME: str
    API_V1_STR: str

    ENVIRONMENT: str

    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_SERVER: str
    POSTGRES_PORT: int = 5432
    POSTGRES_DB: str

    @property
    def DATABASE_URL(self) -> str:
        base = (
            f"postgresql://{self.POSTGRES_USER}:"
            f"{self.POSTGRES_PASSWORD}@"
            f"{self.POSTGRES_SERVER}:"
            f"{self.POSTGRES_PORT}/"
            f"{self.POSTGRES_DB}"
        )

        if self.ENVIRONMENT == "production":
            return f"{base}?sslmode=require"

        return base
    
    model_config = SettingsConfigDict(
        env_file=env_file,
        env_file_encoding="utf-8",
        case_sensitive=True
    )

settings = Settings()
print("URL:", settings.DATABASE_URL)