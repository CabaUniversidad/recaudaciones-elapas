from pydantic import BaseModel
from uuid import UUID
from typing import Optional

class MedidorBase(BaseModel):
    codigo: str
    estado: Optional[str] = "activo"

class MedidorCreate(MedidorBase):
    id_cliente: UUID  # <-- Cambiado de id_usuario
    id_ruta: UUID
    id_tarifa: UUID  # Añadido para consistencia con el modelo de BD

class MedidorUpdate(BaseModel):
    codigo: Optional[str] = None
    estado: Optional[str] = None

class MedidorSchema(MedidorBase):
    id_medidor: UUID
    id_cliente: UUID  # <-- Cambiado de id_usuario
    id_ruta: UUID

    class Config:
        from_attributes = True