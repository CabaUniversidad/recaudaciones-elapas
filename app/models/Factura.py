from sqlalchemy import Column, Integer, Float, String, ForeignKey, DateTime, Boolean
from sqlalchemy.orm import relationship
from datetime import datetime
from app.db.base_class import Base

class Factura(Base):
    __tablename__ = "facturas"

    id = Column(Integer, primary_key=True, index=True)
    monto_total = Column(Float, nullable=False)
    fecha_emision = Column(DateTime, default=datetime.now)
    fecha_vencimiento = Column(DateTime)
    pagada = Column(Boolean, default=False)
    codigo_control = Column(String, nullable=True) # Para temas impositivos/QR
    
    # La llave foránea apunta a la lectura que originó esta factura
    lectura_id = Column(Integer, ForeignKey("lecturas.id"), unique=True)

    # Relación inversa: apunta de vuelta a Lectura
    # uselist=False asegura que sea una relación 1 a 1
    lectura_origen = relationship("Lectura", back_populates="factura")

    def __repr__(self):
        return f"<Factura(id={self.id}, monto={self.monto_total}, pagada={self.pagada})>"