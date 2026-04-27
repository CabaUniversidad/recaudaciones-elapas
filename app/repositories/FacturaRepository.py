from app.repositories.BaseRepository import BaseRepository
from sqlalchemy.orm import Session
from app.models.Factura import Factura

class FacturaRepository(BaseRepository[Factura]):

    def __init__(self):
        super().__init__(Factura, "id_factura")

    def create(self, db: Session, data: dict) -> Factura:
        obj = Factura(**data)
        db.add(obj)
        db.commit()
        db.refresh(obj)
        return obj


factura_repo = FacturaRepository()