from pydantic import BaseModel
from uuid import UUID
from datetime import datetime
from decimal import Decimal
from typing import Optional, List

class MedidorBase(BaseModel):
    codigo: str
    estado: Optional[str] = None

class MedidorCreate(MedidorBase):
    id_usuario: UUID
    id_ruta: UUID

class MedidorUpdate(BaseModel):
    codigo: Optional[str] = None
    estado: Optional[str] = None

class MedidorSchema(MedidorBase):
    id_medidor: UUID
    id_usuario: UUID
    id_ruta: UUID

    class Config:
        from_attributes = True