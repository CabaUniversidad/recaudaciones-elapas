from pydantic import BaseModel
from uuid import UUID
from datetime import datetime
from decimal import Decimal
from typing import Optional, List

class LecturaBase(BaseModel):
    lectura_actual: Decimal
    lectura_anterior: Optional[Decimal] = None
    consumo: Optional[Decimal] = None
    latitud: Optional[Decimal] = None
    longitud: Optional[Decimal] = None
    foto_url: Optional[str] = None
    
class LecturaCreate(LecturaBase):
    id_medidor: UUID
    id_empleado: UUID  

class LecturaUpdate(BaseModel):
    lectura_actual: Optional[Decimal] = None
    lectura_anterior: Optional[Decimal] = None
    consumo: Optional[Decimal] = None
    latitud: Optional[Decimal] = None
    longitud: Optional[Decimal] = None
    foto_url: Optional[str] = None
    sincronizado: Optional[bool] = None
    
    
class LecturaSchema(LecturaBase):
    id_lectura: UUID
    id_medidor: UUID
    fecha: datetime
    sincronizado: bool
    created_at: datetime

    class Config:
        from_attributes = True