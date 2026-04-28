from pydantic import BaseModel
from uuid import UUID
from typing import Optional


class EmpleadoBase(BaseModel):
    nombre: str
    apellido: str
    rol: Optional[str] = None
    telefono: Optional[str] = None
    estado: Optional[str] = None


class EmpleadoCreate(EmpleadoBase):
    pass


class EmpleadoUpdate(BaseModel):
    nombre: Optional[str] = None
    apellido: Optional[str] = None
    rol: Optional[str] = None
    telefono: Optional[str] = None
    estado: Optional[str] = None


class EmpleadoSchema(EmpleadoBase):
    id_empleado: UUID

    class Config:
        from_attributes = True