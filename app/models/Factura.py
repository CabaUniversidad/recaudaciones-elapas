from sqlalchemy import Column, String, ForeignKey, DateTime, Numeric, Date
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
import uuid
from app.db.base_class import Base

class Factura(Base):
    __tablename__ = "factura"
    id_factura = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    id_cliente = Column(UUID(as_uuid=True), ForeignKey("cliente.id_cliente"))
    fecha_emision = Column(DateTime, server_default=func.now())
    total = Column(Numeric, default=0)
    estado = Column(String, default="pendiente")
    periodo = Column(String)
    fecha_inicio = Column(Date)
    fecha_fin = Column(Date)
    saldo = Column(Numeric, default=0)

    cliente = relationship("Cliente", back_populates="facturas")
    detalles = relationship("DetalleFactura", back_populates="factura")
    pagos = relationship("Pago", back_populates="factura")