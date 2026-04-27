from decimal import Decimal
from pydantic import BaseModel
from typing import Optional 
from uuid import UUID
from datetime import datetime

class FacturaBase(BaseModel):
    total: Optional[Decimal] = None
    estado: Optional[str] = None


class FacturaCreate(FacturaBase):
    id_usuario: UUID


class FacturaUpdate(BaseModel):
    total: Optional[Decimal] = None
    estado: Optional[str] = None


class FacturaSchema(FacturaBase):
    id_factura: UUID
    id_usuario: UUID
    fecha_emision: datetime

    class Config:
        from_attributes = True