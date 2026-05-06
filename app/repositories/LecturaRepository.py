from sqlalchemy.orm import Session
from app.models.Lectura import Lectura
from app.repositories.BaseRepository import BaseRepository


class LecturaRepository(BaseRepository[Lectura]):

    def __init__(self):
        super().__init__(Lectura, "id_lectura")

    def create(self, db: Session, data: dict) -> Lectura:
        obj = Lectura(**data)
        db.add(obj)
        db.commit()
        db.refresh(obj)
        return obj


    # NUEVO: historial por medidor
    def get_by_medidor(self, db: Session, id_medidor: str):
        return db.query(Lectura).filter(
            Lectura.id_medidor == id_medidor
        ).order_by(Lectura.fecha.desc()).all()


lectura_repo = LecturaRepository()