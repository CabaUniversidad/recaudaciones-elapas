from pydantic import BaseModel
from uuid import UUID
from datetime import datetime
from decimal import Decimal
from typing import Optional, List
from pydantic import BaseModel, field_validator
from app.core.config import settings
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

    @field_validator("foto_url")
    @classmethod
    def assemble_full_url(cls, v: str | None) -> str | None:
        if v and not v.startswith("http"):
            # Construye la URL pública de Supabase
            return f"{settings.SUPABASE_URL}/storage/v1/object/public/{settings.SUPABASE_BUCKET}/{v}"
        return v

    class Config:
        from_attributes = True

