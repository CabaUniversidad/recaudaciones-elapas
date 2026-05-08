from pydantic import BaseModel
from typing import List

class ConsultaDeudaRequest(BaseModel):
    ci: str  # Coincide con el JSON
    codigo_medidor: str  # Coincide con el JSON

class FacturaPublica(BaseModel):
    periodo: str
    monto: float
    fecha_vencimiento: str
    estado: str

class PublicDeudaResponse(BaseModel):
    nombre_cliente: str
    apellido_cliente: str
    codigo_medidor: str
    total_deuda: float
    cantidad_facturas_pendientes: int
    facturas: List[FacturaPublica]