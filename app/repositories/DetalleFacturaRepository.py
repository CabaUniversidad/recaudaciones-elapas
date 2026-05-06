from sqlalchemy.orm import Session
from app.models.DetalleFactura import DetalleFactura
from app.repositories.BaseRepository import BaseRepository

class DetalleFacturaRepository(BaseRepository[DetalleFactura]):
    def __init__(self):
        super().__init__(DetalleFactura, "id_detalle")

    def create(self, db: Session, data: dict) -> DetalleFactura:
        obj = DetalleFactura(**data)
        db.add(obj)
        # Aquí no hacemos commit, lo hace el CobroService para que sea una sola transacción
        return obj

detalle_repo = DetalleFacturaRepository()