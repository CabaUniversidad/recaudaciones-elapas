from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.db.base_class import Base

class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, index=True)
    nombre_completo = Column(String)
    carnet_identidad = Column(String, unique=True)
    direccion = Column(String)
    
    # Relación con el medidor
    medidores = relationship("Medidor", back_populates="dueño")