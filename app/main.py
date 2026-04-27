import uvicorn
from fastapi import FastAPI
from app.api.v1.router import api_router
from app.db.session import engine
from app.db.base_class import Base
from app.core.config import settings

import app.models

# SOLO crea tablas en local
if settings.ENVIRONMENT == "local": 
    try:
        Base.metadata.create_all(bind=engine)
        print("Tablas creadas en entorno local")
    except Exception as e:
        print(f"Error creando tablas: {e}")
else:
    print("Modo producción: no se crean tablas")

app = FastAPI(
    title=settings.PROJECT_NAME,
    version="1.0.0",
)

app.include_router(api_router, prefix=settings.API_V1_STR)

@app.get("/")
def home():
    return {"status": "online"}

if __name__ == "__main__":
    #python -m app.main
    uvicorn.run("app.main:app", host="0.0.0.0", port=10000, reload=True)
    #uvicorn.run("app.main:app", port=8000, reload=True)