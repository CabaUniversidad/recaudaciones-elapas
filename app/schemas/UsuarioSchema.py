from pydantic import BaseModel

class UsuarioBase(BaseModel):
    nombre_completo: str
    carnet_identidad: str
    direccion: str

class UsuarioCrear(UsuarioBase):
    pass

class UsuarioVer(UsuarioBase):
    id: int
    class Config:
        from_attributes = True