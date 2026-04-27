from sqlalchemy import Column, String, ForeignKey, DateTime, Boolean, Numeric, Text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
import uuid
from app.db.base_class import Base

class Lectura(Base):
    __tablename__ = "lectura"
    id_lectura = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    id_medidor = Column(UUID(as_uuid=True), ForeignKey("medidor.id_medidor"))
    fecha = Column(DateTime, server_default=func.now())
    lectura_actual = Column(Numeric)
    lectura_anterior = Column(Numeric)
    consumo = Column(Numeric)
    latitud = Column(Numeric)
    longitud = Column(Numeric)
    foto_url = Column(Text)
    sincronizado = Column(Boolean, default=False)
    created_at = Column(DateTime, server_default=func.now())

    medidor = relationship("Medidor", back_populates="lecturas")
    detalles_factura = relationship("DetalleFactura", back_populates="lectura")