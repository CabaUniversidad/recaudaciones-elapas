import os
from pydantic_settings import BaseSettings, SettingsConfigDict

ENV = os.getenv("ENV", "production")  # export ENV=production / local: export ENV=local
env_file = f".env.{ENV}"

class Settings(BaseSettings):
    PROJECT_NAME: str
    API_V1_STR: str
    ENVIRONMENT: str

    # Configuración de Base de Datos
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_SERVER: str
    POSTGRES_PORT: int = 5432
    POSTGRES_DB: str

    # --- NUEVAS VARIABLES DE SEGURIDAD ---
    SECRET_KEY: str
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 1440 # 1 día por defecto (60 * 24)

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
        case_sensitive=True,
        extra="ignore" # Ignora variables extra en el .env que no estén aquí
    )

settings = Settings()