from app.repositories.BaseRepository import BaseRepository
from sqlalchemy.orm import Session
from app.models.CorteServicio import CorteServicio

class CorteServicioRepository(BaseRepository[CorteServicio]):

    def __init__(self):
        super().__init__(CorteServicio, "id_corte")

    def create(self, db: Session, data: dict) -> CorteServicio:
        obj = CorteServicio(**data)
        db.add(obj)
        db.commit()
        db.refresh(obj)
        return obj


corte_repo = CorteServicioRepository()