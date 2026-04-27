from sqlalchemy import Column, String, ForeignKey, DateTime, Boolean, Numeric, Text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
import uuid
from app.db.base_class import Base

class CorteServicio(Base):
    __tablename__ = "corte_servicio"
    id_corte = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    id_medidor = Column(UUID(as_uuid=True), ForeignKey("medidor.id_medidor"))
    fecha = Column(DateTime, server_default=func.now())
    motivo = Column(Text)
    latitud = Column(Numeric)
    longitud = Column(Numeric)
    foto_url = Column(Text)

    medidor = relationship("Medidor", back_populates="cortes")