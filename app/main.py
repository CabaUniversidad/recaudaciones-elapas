import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware # <--- NUEVO
from app.api.v1.router import api_router
from app.db.session import engine
from app.db.base_class import Base
from app.core.config import settings

import app.models

# Lógica de creación de tablas
if settings.ENVIRONMENT == "local": 
    try:
        Base.metadata.create_all(bind=engine)
        print("Tablas creadas en entorno local")
    except Exception as e:
        print(f"Error creando tablas: {e}")
else:
    print(f"Modo {settings.ENVIRONMENT}: no se crean tablas automáticamente")

app = FastAPI(
    title=settings.PROJECT_NAME, #
    version="1.0.0",
    # Define la ruta de la documentación basada en tu versión de API
    openapi_url=f"{settings.API_V1_STR}/openapi.json" 
)

# --- CONFIGURACIÓN DE CORS (CRÍTICO) ---
# Esto permite que tu app móvil o web se comunique con el backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # En producción, cámbialo por los dominios específicos
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Inclusión de rutas principales
app.include_router(api_router, prefix=settings.API_V1_STR) #[cite: 1]

@app.get("/", tags=["Health"])
def home():
    return {
        "status": "online",
        "project": settings.PROJECT_NAME,
        "environment": settings.ENVIRONMENT
    }
if __name__ == "__main__":
    #python -m app.main
    #uvicorn.run("app.main:app", host="0.0.0.0", port=10000, reload=True)
    uvicorn.run("app.main:app", port=8000, reload=True)