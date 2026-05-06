from fastapi import APIRouter
from app.api.v1.endpoints import (
    clientes, medidores, lecturas, facturacion, 
    pagos, cortes, empleados, auth, configuracion # configuracion para zonas/rutas
)

api_router = APIRouter()

api_router.include_router(auth.router, prefix='/auth', tags=['Autenticación'])
api_router.include_router(clientes.router, prefix='/clientes', tags=['Clientes'])
api_router.include_router(medidores.router, prefix='/medidores', tags=['Medidores'])
api_router.include_router(lecturas.router, prefix='/lecturas', tags=['Lecturas'])
api_router.include_router(facturacion.router, prefix='/facturacion', tags=['Facturación'])
api_router.include_router(pagos.router, prefix='/pagos', tags=['Pagos'])
api_router.include_router(cortes.router, prefix='/cortes', tags=['Cortes de Servicio'])
api_router.include_router(empleados.router, prefix='/empleados', tags=['Empleados'])