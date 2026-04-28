from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import or_

from app.db.session import get_db
from app.schemas.UsuarioSchema import UsuarioCreate, UsuarioSchema, UsuarioUpdate
from app.repositories.UsuarioRepository import usuario_repo

router = APIRouter()

@router.post("/", response_model=UsuarioSchema)
def crear(data: UsuarioCreate, db: Session = Depends(get_db)):
    try:
        return usuario_repo.create(db, data.dict())
    except SQLAlchemyError:
        raise HTTPException(status_code=500, detail="Error interno")


@router.get("/", response_model=list[UsuarioSchema])
def listar(db: Session = Depends(get_db)):
    try:
        return usuario_repo.get_all(db)
    except SQLAlchemyError:
        raise HTTPException(status_code=500, detail="Error interno")


@router.get("/buscar", response_model=list[UsuarioSchema])
def buscar(q: str = Query(..., min_length=1), db: Session = Depends(get_db)):
    try:
        return usuario_repo.search(db, q)
    except SQLAlchemyError:
        raise HTTPException(status_code=500, detail="Error interno")


@router.get("/{id}", response_model=UsuarioSchema)
def obtener(id: str, db: Session = Depends(get_db)):
    obj = usuario_repo.get(db, id)
    if not obj:
        raise HTTPException(status_code=404, detail="Recurso no encontrado")
    return obj


@router.put("/{id}", response_model=UsuarioSchema)
def actualizar(id: str, data: UsuarioUpdate, db: Session = Depends(get_db)):
    obj = usuario_repo.get(db, id)
    if not obj:
        raise HTTPException(status_code=404, detail="Recurso no encontrado")

    try:
        return usuario_repo.update(db, obj, data.dict(exclude_unset=True))
    except SQLAlchemyError:
        raise HTTPException(status_code=500, detail="Error interno")


@router.delete("/{id}")
def eliminar(id: str, db: Session = Depends(get_db)):
    obj = usuario_repo.get(db, id)
    if not obj:
        raise HTTPException(status_code=404, detail="Recurso no encontrado")

    try:
        usuario_repo.delete(db, id)
        return {"ok": True}
    except SQLAlchemyError:
        raise HTTPException(status_code=500, detail="Error interno")