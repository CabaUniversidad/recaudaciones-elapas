from sqlalchemy import Column, Integer, Float, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from app.db.base_class import Base

class Lectura(Base):
    __tablename__ = "lecturas"

    id = Column(Integer, primary_key=True, index=True)
    valor_marcado = Column(Float)
    fecha_toma = Column(DateTime, default=datetime.now)
    medidor_id = Column(Integer, ForeignKey("medidores.id"))

    medidor = relationship("Medidor", back_populates="lecturas")
    factura = relationship("Factura", back_populates="lectura_origen", uselist=False)