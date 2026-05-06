from pydantic import BaseModel
from uuid import UUID
from datetime import datetime, date
from typing import List, Optional

class DetalleFacturaSchema(BaseModel):
    id_detalle: UUID
    id_lectura: UUID
    monto: float
    class Config: from_attributes = True

class FacturaSchema(BaseModel):
    id_factura: UUID
    id_cliente: UUID
    total: float
    estado: str
    periodo: Optional[str]
    fecha_inicio: Optional[date]
    fecha_fin: Optional[date]
    saldo: float
    detalles: List[DetalleFacturaSchema] = []

    class Config: from_attributes = True