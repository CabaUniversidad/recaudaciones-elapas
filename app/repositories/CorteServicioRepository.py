from sqlalchemy.orm import Session
from app.models.CorteServicio import CorteServicio
from app.repositories.BaseRepository import BaseRepository
from datetime import datetime

class CorteServicioRepository(BaseRepository[CorteServicio]):

    def __init__(self):
        super().__init__(CorteServicio, "id_corte")

    def create(self, db: Session, data: dict) -> CorteServicio:
        # Si el móvil no envía fecha, la generamos aquí
        if "fecha" not in data or data["fecha"] is None:
            data["fecha"] = datetime.now() #
            
        obj = CorteServicio(**data)
        db.add(obj)
        db.commit()
        db.refresh(obj)
        return obj


    # historial por medidor
    def get_by_medidor(self, db: Session, id_medidor: str):
        return db.query(CorteServicio).filter(
            CorteServicio.id_medidor == id_medidor
        ).order_by(CorteServicio.fecha.desc()).all()


corte_repo = CorteServicioRepository()