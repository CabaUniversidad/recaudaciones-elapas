from app.models.Medidor import Medidor
from app.repositories.BaseRepository import BaseRepository
from sqlalchemy.orm import Session

class MedidorRepository(BaseRepository[Medidor]):

    def __init__(self):
        super().__init__(Medidor, "id_medidor")

    def create(self, db: Session, data: dict) -> Medidor:
        obj = Medidor(**data)
        db.add(obj)
        db.commit()
        db.refresh(obj)
        return obj


medidor_repo = MedidorRepository()