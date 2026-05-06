from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
import uuid
from app.db.base_class import Base

class Medidor(Base):
    __tablename__ = "medidor"

    id_medidor = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    codigo = Column(String, unique=True, nullable=False)
    id_cliente = Column(UUID(as_uuid=True), ForeignKey("cliente.id_cliente"))
    id_ruta = Column(UUID(as_uuid=True), ForeignKey("ruta.id_ruta"))
    id_tarifa = Column(UUID(as_uuid=True), ForeignKey("tarifa.id_tarifa"))
    estado = Column(String, default="activo")

    # Relaciones
    cliente = relationship("Cliente", back_populates="medidores")
    ruta = relationship("Ruta", back_populates="medidores")
    tarifa = relationship("Tarifa")
    lecturas = relationship("Lectura", back_populates="medidor")
    
    # ESTA ES LA LÍNEA QUE FALTA:
    cortes = relationship("CorteServicio", back_populates="medidor")