from sqlalchemy.orm import Session
from app.models.Usuario import Usuario
from app.schemas.UsuarioSchema import UsuarioCrear
from app.repositories.BaseRepository import BaseRepository

class UsuarioRepository(BaseRepository[Usuario]):
    def create(self, db: Session, objeto_in: UsuarioCrear) -> Usuario:
        db_usuario = Usuario(
            nombre_completo=objeto_in.nombre_completo,
            carnet_identidad=objeto_in.carnet_identidad,
            direccion=objeto_in.direccion
        )
        db.add(db_usuario)
        db.commit()
        db.refresh(db_usuario)
        return db_usuario

# Instancia para usar en los endpoints
usuario_repo = UsuarioRepository(Usuario)