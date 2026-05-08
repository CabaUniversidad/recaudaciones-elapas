from fastapi import APIRouter, Depends
from app.api.deps import get_current_empleado
from app.api.v1.endpoints import (
    clientes, medidores, lecturas, facturacion, 
    pagos, cortes, empleados, auth, configuracion,uploads, public
)

api_router = APIRouter()

api_router.include_router(auth.router, prefix='/auth', tags=['Autenticación'])
api_router.include_router(clientes.router, prefix='/clientes', tags=['Clientes'],dependencies=[Depends(get_current_empleado)])
api_router.include_router(medidores.router, prefix='/medidores', tags=['Medidores'],dependencies=[Depends(get_current_empleado)])
api_router.include_router(lecturas.router, prefix='/lecturas', tags=['Lecturas'])
api_router.include_router(uploads.router, prefix='/uploads', tags=['Storage'])
api_router.include_router(facturacion.router, prefix='/facturacion', tags=['Facturación'],dependencies=[Depends(get_current_empleado)])
api_router.include_router(pagos.router, prefix='/pagos', tags=['Pagos'],dependencies=[Depends(get_current_empleado)])
api_router.include_router(cortes.router, prefix='/cortes', tags=['Cortes de Servicio'],dependencies=[Depends(get_current_empleado)])
api_router.include_router(empleados.router, prefix='/empleados', tags=['Empleados'],dependencies=[Depends(get_current_empleado)])
api_router.include_router(public.router, prefix="/public", tags=["Portal Público"])