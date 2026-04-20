from fastapi import APIRouter
from api.v1.endpoints import usuarios, medidores, lecturas, facturacion

api_router = APIRouter()

# Registro de rutas con sus respectivos prefijos y etiquetas (tags) para la doc de Swagger
api_router.include_router(usuarios.router, prefix='/usuarios', tags=['Usuarios'])
api_router.include_router(medidores.router, prefix='/medidores', tags=['Medidores'])
api_router.include_router(lecturas.router, prefix='/lecturas', tags=['Lecturas'])
api_router.include_router(facturacion.router, prefix='/facturacion', tags=['Facturación'])