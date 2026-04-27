from sqlalchemy import Column, String, ForeignKey, DateTime, Boolean, Numeric, Text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
import uuid
from app.db.base_class import Base

class Factura(Base):
    __tablename__ = "factura"
    id_factura = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    id_usuario = Column(UUID(as_uuid=True), ForeignKey("usuario.id_usuario"))
    fecha_emision = Column(DateTime, server_default=func.now())
    total = Column(Numeric)
    estado = Column(String)

    usuario = relationship("Usuario", back_populates="facturas")
    detalles = relationship("DetalleFactura", back_populates="factura")
    pagos = relationship("Pago", back_populates="factura")