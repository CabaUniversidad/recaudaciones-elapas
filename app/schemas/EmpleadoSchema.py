from pydantic import BaseModel, EmailStr
from uuid import UUID
from typing import Optional

class EmpleadoBase(BaseModel):
    nombre: str
    apellido: str
    rol: Optional[str] = None
    telefono: Optional[str] = None
    estado: Optional[str] = "activo"

class EmpleadoCreate(EmpleadoBase):
    email: EmailStr # Usar EmailStr valida que sea un correo real
    password: str

class EmpleadoUpdate(BaseModel):
    nombre: Optional[str] = None
    apellido: Optional[str] = None
    rol: Optional[str] = None
    telefono: Optional[str] = None
    estado: Optional[str] = None

class EmpleadoSchema(EmpleadoBase):
    id_empleado: UUID
    email: str # Añadimos email aquí para que se vea en las respuestas

    class Config:
        from_attributes = True