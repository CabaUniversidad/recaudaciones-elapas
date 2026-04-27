from app.repositories.BaseRepository import BaseRepository
from sqlalchemy.orm import Session
from app.models.Lectura import Lectura

class LecturaRepository(BaseRepository[Lectura]):

    def __init__(self):
        super().__init__(Lectura, "id_lectura")

    def create(self, db: Session, data: dict) -> Lectura:
        obj = Lectura(**data)
        db.add(obj)
        db.commit()
        db.refresh(obj)
        return obj


lectura_repo = LecturaRepository()