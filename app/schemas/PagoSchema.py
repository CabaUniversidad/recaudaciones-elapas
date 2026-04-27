from decimal import Decimal
from pydantic import BaseModel
from typing import Optional 
from uuid import UUID
from datetime import datetime

class PagoBase(BaseModel):
    monto: Decimal
    metodo: Optional[str] = None
    referencia: Optional[str] = None


class PagoCreate(PagoBase):
    id_factura: UUID


class PagoUpdate(BaseModel):
    monto: Optional[Decimal] = None
    metodo: Optional[str] = None
    referencia: Optional[str] = None


class PagoSchema(PagoBase):
    id_pago: UUID
    id_factura: UUID
    fecha_pago: datetime

    class Config:
        from_attributes = True