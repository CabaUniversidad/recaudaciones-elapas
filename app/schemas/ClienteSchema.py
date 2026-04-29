from pydantic import BaseModel, EmailStr
from uuid import UUID
from datetime import datetime
from typing import Optional

class ClienteBase(BaseModel):
    nombre: str
    apellido: str
    ci: str
    direccion: Optional[str] = None
    telefono: Optional[str] = None
    email: Optional[EmailStr] = None # Este campo es el que pedía la librería
    estado: Optional[str] = "activo"

class ClienteCreate(ClienteBase):
    pass

class ClienteUpdate(BaseModel): # Esto soluciona el "desactivado" que mencionaste antes
    nombre: Optional[str] = None
    apellido: Optional[str] = None
    direccion: Optional[str] = None
    telefono: Optional[str] = None
    email: Optional[EmailStr] = None
    estado: Optional[str] = None

class ClienteSchema(ClienteBase):
    id_cliente: UUID
    created_at: datetime

    class Config:
        from_attributes = True