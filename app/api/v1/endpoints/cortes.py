from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError

from app.db.session import get_db
from app.schemas.CorteServicioSchema import CorteServicioCreate, CorteServicioSchema
from app.repositories.CorteServicioRepository import corte_repo

router = APIRouter()


# POST /cortes
@router.post("/", response_model=CorteServicioSchema)
def crear(data: CorteServicioCreate, db: Session = Depends(get_db)):
    try:
        return corte_repo.create(db, data.dict())
    except SQLAlchemyError:
        raise HTTPException(status_code=500, detail="Error interno")


# GET /cortes
@router.get("/", response_model=list[CorteServicioSchema])
def listar(db: Session = Depends(get_db)):
    try:
        return corte_repo.get_all(db)
    except SQLAlchemyError:
        raise HTTPException(status_code=500, detail="Error interno")


# GET /cortes/{id_corte}
@router.get("/{id_corte}", response_model=CorteServicioSchema)
def obtener(id_corte: str, db: Session = Depends(get_db)):
    obj = corte_repo.get(db, id_corte)
    if not obj:
        raise HTTPException(status_code=404, detail="No encontrado")
    return obj


# GET /cortes/medidor/{id_medidor}
@router.get("/medidor/{id_medidor}", response_model=list[CorteServicioSchema])
def por_medidor(id_medidor: str, db: Session = Depends(get_db)):
    try:
        return corte_repo.get_by_medidor(db, id_medidor)
    except SQLAlchemyError:
        raise HTTPException(status_code=500, detail="Error interno")