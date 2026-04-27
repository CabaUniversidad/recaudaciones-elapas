from sqlalchemy import Column, String, ForeignKey, DateTime, Boolean, Numeric, Text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
import uuid
from app.db.base_class import Base

class Medidor(Base):
    __tablename__ = "medidor"
    id_medidor = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    codigo = Column(String, unique=True, index=True)
    id_usuario = Column(UUID(as_uuid=True), ForeignKey("usuario.id_usuario"))
    id_ruta = Column(UUID(as_uuid=True), ForeignKey("ruta.id_ruta"))
    estado = Column(String)

    usuario = relationship("Usuario", back_populates="medidores")
    ruta = relationship("Ruta", back_populates="medidores")
    lecturas = relationship("Lectura", back_populates="medidor")
    cortes = relationship("CorteServicio", back_populates="medidor")