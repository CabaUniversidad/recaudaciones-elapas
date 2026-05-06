from sqlalchemy.orm import Session
from sqlalchemy import or_
from app.models.Medidor import Medidor
from app.repositories.BaseRepository import BaseRepository

class MedidorRepository(BaseRepository[Medidor]):
    def __init__(self):
        super().__init__(Medidor, "id_medidor")

    def create(self, db: Session, data: dict) -> Medidor:
        obj = Medidor(**data)
        db.add(obj)
        db.commit()
        db.refresh(obj)
        return obj

    def get_by_user(self, db: Session, id_cliente: str):
        return db.query(Medidor).filter(Medidor.id_cliente == id_cliente).all()

    def search_by_user(self, db: Session, q: str):
        return db.query(Medidor).join(Medidor.cliente).filter(
            or_(
                Medidor.cliente.has(ci=q),
                Medidor.cliente.has(nombre=q),
                Medidor.cliente.has(apellido=q)
            )
        ).all()

medidor_repo = MedidorRepository()