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


    # 1. medidores por usuario
    def get_by_user(self, db: Session, id_usuario: str):
        return db.query(Medidor).filter(
            Medidor.id_usuario == id_usuario
        ).all()


    # 2. búsqueda por código o relación usuario
    def search(self, db: Session, q: str):
        return db.query(Medidor).filter(
            or_(
                Medidor.codigo.ilike(f"%{q}%")
            )
        ).all()
    def search_by_user(self, db: Session, q: str):
        return db.query(Medidor).join(Medidor.usuario).filter(
            or_(
                Medidor.usuario.has(ci=q),
                Medidor.usuario.has(nombre=q),
                Medidor.usuario.has(apellido=q)
            )
        ).all()

medidor_repo = MedidorRepository()