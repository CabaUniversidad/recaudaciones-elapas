from sqlalchemy import Column, String, ForeignKey, DateTime, Boolean, Numeric, Text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
import uuid
from app.db.base_class import Base

class Pago(Base):
    __tablename__ = "pago"
    id_pago = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    id_factura = Column(UUID(as_uuid=True), ForeignKey("factura.id_factura"))
    fecha_pago = Column(DateTime, server_default=func.now())
    monto = Column(Numeric)
    metodo = Column(String)
    referencia = Column(String)

    factura = relationship("Factura", back_populates="pagos")