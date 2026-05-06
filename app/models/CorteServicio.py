from sqlalchemy import Column, String, DateTime, Numeric, ForeignKey, Text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
import uuid
from app.db.base_class import Base

class CorteServicio(Base):
    __tablename__ = "corte_servicio"

    id_corte = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    id_medidor = Column(UUID(as_uuid=True), ForeignKey("medidor.id_medidor"))
    id_empleado = Column(UUID(as_uuid=True), ForeignKey("empleado.id_empleado"))
    fecha = Column(DateTime)
    motivo = Column(Text)
    latitud = Column(Numeric)
    longitud = Column(Numeric)
    foto_url = Column(Text)

    # Relaciones
    # Debe decir back_populates="cortes" para coincidir con Medidor
    medidor = relationship("Medidor", back_populates="cortes")
    empleado = relationship("Empleado")