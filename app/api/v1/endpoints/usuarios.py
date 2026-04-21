from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.schemas.UsuarioSchema import UsuarioCrear, UsuarioVer
from app.repositories.UsuarioRepository import usuario_repo

router = APIRouter()

@router.post("/", response_model=UsuarioVer)
def crear_usuario(usuario_in: UsuarioCrear, db: Session = Depends(get_db)):
    # Verificamos si ya existe por carnet
    # (Podrías añadir un método buscar_por_carnet en el repo)
    return usuario_repo.create(db, objeto_in=usuario_in)

@router.get("/{usuario_id}", response_model=UsuarioVer)
def leer_usuario(usuario_id: int, db: Session = Depends(get_db)):
    usuario = usuario_repo.get(db, id=usuario_id)
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return usuario