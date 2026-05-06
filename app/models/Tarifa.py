from sqlalchemy import Column, String, Numeric
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
import uuid
from app.db.base_class import Base

class Tarifa(Base):
    __tablename__ = "tarifa"
    id_tarifa = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    nombre = Column(String)
    precio_por_m3 = Column(Numeric, nullable=False)
    rango_min = Column(Numeric)
    rango_max = Column(Numeric)

    medidores = relationship("Medidor", back_populates="tarifa")