from decimal import Decimal
from pydantic import BaseModel
from typing import Optional 
from uuid import UUID 
from datetime import datetime

class CorteServicioBase(BaseModel):
    motivo: Optional[str] = None
    latitud: Optional[Decimal] = None
    longitud: Optional[Decimal] = None
    foto_url: Optional[str] = None


class CorteServicioCreate(CorteServicioBase):
    id_medidor: UUID
    id_empleado: UUID  # <-- Nuevo: El móvil debe enviar quién hace el corte


class CorteServicioUpdate(BaseModel):
    motivo: Optional[str] = None
    latitud: Optional[Decimal] = None
    longitud: Optional[Decimal] = None
    foto_url: Optional[str] = None


class CorteServicioSchema(CorteServicioBase):
    id_corte: UUID
    id_medidor: UUID
    fecha: datetime

    class Config:
        from_attributes = True