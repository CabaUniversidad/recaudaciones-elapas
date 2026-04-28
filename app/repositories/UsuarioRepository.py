from sqlalchemy.orm import Session
from sqlalchemy import or_
from app.models.Usuario import Usuario
from app.repositories.BaseRepository import BaseRepository

class UsuarioRepository(BaseRepository[Usuario]):

    def __init__(self):
        super().__init__(Usuario, "id_usuario")

    def create(self, db: Session, data: dict) -> Usuario:
        obj = Usuario(**data)
        db.add(obj)
        db.commit()
        db.refresh(obj)
        return obj

    def update(self, db: Session, db_obj: Usuario, data: dict) -> Usuario:
        for key, value in data.items():
            setattr(db_obj, key, value)

        db.commit()
        db.refresh(db_obj)
        return db_obj
    def search(self, db: Session, q: str):
        return db.query(Usuario).filter(
            or_(
                Usuario.nombre.ilike(f"%{q}%"),
                Usuario.apellido.ilike(f"%{q}%"),
                Usuario.ci.ilike(f"%{q}%"),
                Usuario.email.ilike(f"%{q}%")
            )
        ).all()

usuario_repo = UsuarioRepository()