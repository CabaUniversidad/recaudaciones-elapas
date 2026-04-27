from app.repositories.BaseRepository import BaseRepository
from sqlalchemy.orm import Session
from app.models.Pago import Pago

class PagoRepository(BaseRepository[Pago]):

    def __init__(self):
        super().__init__(Pago, "id_pago")

    def create(self, db: Session, data: dict) -> Pago:
        obj = Pago(**data)
        db.add(obj)
        db.commit()
        db.refresh(obj)
        return obj


pago_repo = PagoRepository()