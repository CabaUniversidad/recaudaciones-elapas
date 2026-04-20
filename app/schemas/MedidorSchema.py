from pydantic import BaseModel

class MedidorBase(BaseModel):
    codigo_serial: str
    tipo_tarifa: str
    usuario_id: int

class MedidorCrear(MedidorBase):
    pass

class MedidorVer(MedidorBase):
    id: int
    class Config:
        from_attributes = True