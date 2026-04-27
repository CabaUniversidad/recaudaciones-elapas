from sqlalchemy import Column, String, ForeignKey, DateTime, Boolean, Numeric, Text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
import uuid
from app.db.base_class import Base

class Usuario(Base):
    __tablename__ = "usuario"
    id_usuario = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    nombre = Column(String, nullable=False)
    apellido = Column(String, nullable=False)
    ci = Column(String, unique=True, index=True)
    direccion = Column(Text)
    telefono = Column(String)
    email = Column(String, unique=True)
    estado = Column(String)
    created_at = Column(DateTime, server_default=func.now())

    medidores = relationship("Medidor", back_populates="usuario")
    facturas = relationship("Factura", back_populates="usuario")