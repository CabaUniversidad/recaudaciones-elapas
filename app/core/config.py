from pydantic_settings import BaseSettings, SettingsConfigDict
from pathlib import Path
import os

# Buscamos el archivo .env en la raíz del proyecto
env_path = Path(__file__).parent.parent / ".env"

class Settings(BaseSettings):
    PROJECT_NAME: str = "Sistema de Gestión de Agua"
    API_V1_STR: str = "/api/v1"
    
    # Definimos las variables de la DB
    # Si no están en el .env, usará estos valores por defecto
    POSTGRES_USER: str = "postgres"
    POSTGRES_PASSWORD: str = "password"
    POSTGRES_SERVER: str = "localhost"
    POSTGRES_PORT: int = 5432
    POSTGRES_DB: str = "postgres"
    
    # Propiedad calculada para la URL de conexión
    @property
    def DATABASE_URL(self) -> str:
        return f"postgresql://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@{self.POSTGRES_SERVER}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}"

    # Configuración de Pydantic para leer el archivo .env
    model_config = SettingsConfigDict(
        env_file=env_path,
        env_file_encoding='utf-8',
        case_sensitive=True
    )

settings = Settings()