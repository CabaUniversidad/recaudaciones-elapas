from sqlalchemy import Column, String, ForeignKey, DateTime, Boolean, Numeric, Text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
import uuid
from app.db.base_class import Base
class Ruta(Base):
    __tablename__ = "ruta"
    id_ruta = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    nombre = Column(String, nullable=False)
    id_zona = Column(UUID(as_uuid=True), ForeignKey("zona.id_zona"))
    
    zona = relationship("Zona", back_populates="rutas")
    medidores = relationship("Medidor", back_populates="ruta")