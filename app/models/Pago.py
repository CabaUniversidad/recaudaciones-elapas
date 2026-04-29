from sqlalchemy import Column, String, DateTime, Numeric, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
import uuid
from app.db.base_class import Base

class Pago(Base):
    __tablename__ = "pago"

    id_pago = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    id_factura = Column(UUID(as_uuid=True), ForeignKey("factura.id_factura"))
    # Esta es la línea que falta o está mal:
    id_cliente = Column(UUID(as_uuid=True), ForeignKey("cliente.id_cliente"))
    
    fecha_pago = Column(DateTime)
    monto = Column(Numeric)
    metodo = Column(String)
    referencia = Column(String)

    # Relaciones
    factura = relationship("Factura", back_populates="pagos")
    cliente = relationship("Cliente", back_populates="pagos")