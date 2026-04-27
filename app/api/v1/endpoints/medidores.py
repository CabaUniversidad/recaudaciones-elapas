from fastapi import APIRouter, Depends, HTTPException
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
        raise HTTPException(500, "Error interno")


@router.get("/", response_model=list[MedidorSchema])
def listar(db: Session = Depends(get_db)):
    try:
        return medidor_repo.get_all(db)
    except SQLAlchemyError:
        raise HTTPException(500, "Error interno")