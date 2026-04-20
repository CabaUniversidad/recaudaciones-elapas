from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "Sistema de Gestión de Agua"
    API_V1_STR: str = "/api/v1"
    
    # Esto leerá desde tus variables de entorno (.env)
    # Si usas Supabase, aquí pondrás la URL de conexión que ellos te dan
    DATABASE_URL: str = "postgresql://postgres:password@db.supabase.co:5432/postgres"

    class Config:
        case_sensitive = True

settings = Settings()