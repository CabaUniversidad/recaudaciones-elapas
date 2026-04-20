import uvicorn
from fastapi import FastAPI
from api.v1.router import api_router

app = FastAPI(
    title="Sistema de Gestión de Agua - Módulo A",
    description="API para Facturación, Catastro y Lecturas",
    version="1.0.0"
)

# Incluimos el router central que ya trae todas las sub-rutas
app.include_router(api_router, prefix="/api/v1")

@app.get("/", tags=["General"])
def estado_del_servidor():
    return {
        "estado": "en línea",
        "sistema": "Gestión de Agua",
        "documentacion": "/docs"
    }

if __name__ == "__main__":
    # Importante: se usa "app.main:app" para que reconozca la ruta desde la raíz
    uvicorn.run("main:app", port=8000, reload=True)