from sqlalchemy import Column, String, DateTime, Numeric, ForeignKey, Boolean, CheckConstraint
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
import uuid
from app.db.base_class import Base

class Lectura(Base):
    __tablename__ = "lectura"

    id_lectura = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    id_medidor = Column(UUID(as_uuid=True), ForeignKey("medidor.id_medidor"))
    fecha = Column(DateTime, nullable=False)
    lectura_actual = Column(Numeric)
    lectura_anterior = Column(Numeric)
    consumo = Column(Numeric)
    latitud = Column(Numeric)
    longitud = Column(Numeric)
    foto_url = Column(String)
    sincronizado = Column(Boolean, default=False)
    created_at = Column(DateTime, server_default=func.now())
    id_empleado = Column(UUID(as_uuid=True), ForeignKey("empleado.id_empleado"))

    # Restricción de consumo positivo
    __table_args__ = (CheckConstraint('consumo >= 0', name='check_consumo_positivo'),)

    # Relaciones
    medidor = relationship("Medidor", back_populates="lecturas")
    empleado = relationship("Empleado")
    detalles_factura = relationship("DetalleFactura", back_populates="lectura")