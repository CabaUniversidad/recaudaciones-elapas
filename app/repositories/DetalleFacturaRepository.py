from app.repositories.BaseRepository import BaseRepository
from sqlalchemy.orm import Session
from app.models.DetalleFactura import DetalleFactura

class DetalleFacturaRepository(BaseRepository[DetalleFactura]):

    def __init__(self):
        super().__init__(DetalleFactura, "id_detalle")

    def create(self, db: Session, data: dict) -> DetalleFactura:
        obj = DetalleFactura(**data)
        db.add(obj)
        db.commit()
        db.refresh(obj)
        return obj


detalle_repo = DetalleFacturaRepository()