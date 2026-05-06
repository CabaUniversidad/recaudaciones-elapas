from sqlalchemy.orm import Session
from sqlalchemy import or_
from app.models.Cliente import Cliente
from app.repositories.BaseRepository import BaseRepository

class ClienteRepository(BaseRepository[Cliente]):
    def __init__(self):
        super().__init__(Cliente, "id_cliente")

    def create(self, db: Session, data: dict) -> Cliente:
        obj = Cliente(**data)
        db.add(obj)
        db.commit()
        db.refresh(obj)
        return obj

    def update(self, db: Session, db_obj: Cliente, data: dict) -> Cliente:
        for key, value in data.items():
            setattr(db_obj, key, value)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def search(self, db: Session, q: str):
        return db.query(Cliente).filter(
            or_(
                Cliente.nombre.ilike(f"%{q}%"),
                Cliente.apellido.ilike(f"%{q}%"),
                Cliente.ci.ilike(f"%{q}%")
            )
        ).all()

cliente_repo = ClienteRepository()