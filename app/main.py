import uvicorn
from fastapi import FastAPI
from app.api.v1.router import api_router
from app.db.session import engine
from app.db.base_class import Base 

# Importar modelos para que SQLAlchemy los "vea"
from app.models.Usuario import Usuario
from app.models.Medidor import Medidor
from app.models.Lectura import Lectura
from app.models.Factura import Factura

# Crear tablas
try:
    Base.metadata.create_all(bind=engine)
    print("✅ Tablas creadas/verificadas exitosamente.")
except Exception as e:
    print(f"❌ Error creando tablas: {e}")

app = FastAPI(
    title="Sistema de Gestión de Agua",
    version="1.0.0", 
)

app.include_router(api_router, prefix="/api/v1")

@app.get("/", tags=["General"])
def home():
    return {"status": "online"}

if __name__ == "__main__":
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)