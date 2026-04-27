from sqlalchemy.orm import Session
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


usuario_repo = UsuarioRepository()