from sqlalchemy import Column, String, ForeignKey, DateTime, Boolean, Numeric, Text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
import uuid
from app.db.base_class import Base

class Zona(Base):
    __tablename__ = "zona"
    id_zona = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    nombre = Column(String, nullable=False)
    descripcion = Column(Text)
    
    rutas = relationship("Ruta", back_populates="zona")