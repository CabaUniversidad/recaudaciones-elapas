from sqlalchemy import Column, String, ForeignKey, DateTime, Boolean, Numeric, Text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
import uuid
from app.db.base_class import Base

class DetalleFactura(Base):
    __tablename__ = "detalle_factura"
    id_detalle = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    id_factura = Column(UUID(as_uuid=True), ForeignKey("factura.id_factura"))
    id_lectura = Column(UUID(as_uuid=True), ForeignKey("lectura.id_lectura"))
    monto = Column(Numeric)

    factura = relationship("Factura", back_populates="detalles")
    lectura = relationship("Lectura", back_populates="detalles_factura")