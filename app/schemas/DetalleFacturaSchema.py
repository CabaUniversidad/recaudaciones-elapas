from decimal import Decimal
from pydantic import BaseModel
from typing import Optional 
from uuid import UUID 

class DetalleFacturaBase(BaseModel):
    monto: Decimal


class DetalleFacturaCreate(DetalleFacturaBase):
    id_factura: UUID
    id_lectura: UUID


class DetalleFacturaUpdate(BaseModel):
    monto: Optional[Decimal] = None


class DetalleFacturaSchema(DetalleFacturaBase):
    id_detalle: UUID
    id_factura: UUID
    id_lectura: UUID

    class Config:
        from_attributes = True