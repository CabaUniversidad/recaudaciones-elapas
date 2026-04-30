from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError

from app.db.session import get_db
from app.schemas.MedidorSchema import MedidorCreate, MedidorSchema
from app.repositories.MedidorRepository import medidor_repo

router = APIRouter()


@router.post("/", response_model=MedidorSchema)
def crear(data: MedidorCreate, db: Session = Depends(get_db)):
    try:
        return medidor_repo.create(db, data.dict())
    except SQLAlchemyError:
        raise HTTPException(status_code=500, detail="Error interno")


@router.get("/", response_model=list[MedidorSchema])
def listar(db: Session = Depends(get_db)):
    try:
        return medidor_repo.get_all(db)
    except SQLAlchemyError:
        raise HTTPException(status_code=500, detail="Error interno")


# 1. Medidor por usuario
# Cambiar el nombre del parámetro y la ruta
@router.get("/cliente/{id_cliente}", response_model=list[MedidorSchema])
def por_cliente(id_cliente: str, db: Session = Depends(get_db)):
    try:
        return medidor_repo.get_by_user(db, id_cliente)
    except SQLAlchemyError:
        raise HTTPException(status_code=500, detail="Error interno")


# 2. Buscar por código o usuario
@router.get("/buscar", response_model=list[MedidorSchema])
def buscar(q: str = Query(..., min_length=1), db: Session = Depends(get_db)):
    try:
        return medidor_repo.search(db, q)
    except SQLAlchemyError:
        raise HTTPException(status_code=500, detail="Error interno")


# 3. Detalle por id
@router.get("/{id_medidor}", response_model=MedidorSchema)
def obtener(id_medidor: str, db: Session = Depends(get_db)):
    obj = medidor_repo.get(db, id_medidor)
    if not obj:
        raise HTTPException(status_code=404, detail="No encontrado")
    return obj

#4. Buscar por cliente (ci, nombre o apellido)
@router.get("/buscar/cliente", response_model=list[MedidorSchema])
def buscar_por_cliente(q: str, db: Session = Depends(get_db)):
    try:
        return medidor_repo.search_by_user(db, q)
    except SQLAlchemyError:
        raise HTTPException(status_code=500, detail="Error interno")