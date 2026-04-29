from sqlalchemy import Column, String, DateTime, Text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
import uuid
from app.db.base_class import Base

class Cliente(Base):
    __tablename__ = "cliente"
    id_cliente = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    nombre = Column(String, nullable=False)
    apellido = Column(String, nullable=False)
    ci = Column(String, unique=True, index=True)
    direccion = Column(Text)
    telefono = Column(String)
    email = Column(String, unique=True)
    estado = Column(String, default="activo")
    created_at = Column(DateTime, server_default=func.now())

    # Relaciones corregidas [cite: 28]
    medidores = relationship("Medidor", back_populates="cliente")
    facturas = relationship("Factura", back_populates="cliente")
    pagos = relationship("Pago", back_populates="cliente")