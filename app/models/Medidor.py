from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base_class import Base

class Medidor(Base):
    __tablename__ = "medidores"

    id = Column(Integer, primary_key=True, index=True)
    codigo_serial = Column(String, unique=True)
    tipo_tarifa = Column(String)  # Ejemplo: 'Doméstico' o 'Comercial'
    usuario_id = Column(Integer, ForeignKey("usuarios.id"))

    dueño = relationship("Usuario", back_populates="medidores")
    lecturas = relationship("Lectura", back_populates="medidor")