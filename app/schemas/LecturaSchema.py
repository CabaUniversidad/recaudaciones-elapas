from pydantic import BaseModel
from datetime import datetime

class LecturaCrear(BaseModel):
    valor_marcado: float
    medidor_id: int

class LecturaVer(BaseModel):
    id: int
    valor_marcado: float
    fecha_toma: datetime
    class Config:
        from_attributes = True