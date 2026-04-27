from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from app.db.session import get_db
from app.schemas.LecturaSchema import LecturaCreate, LecturaSchema
from app.repositories.LecturaRepository import lectura_repo
from app.services.lectura_service import LecturaService

router = APIRouter()

@router.post("/", response_model=LecturaSchema)
def crear(data: LecturaCreate, db: Session = Depends(get_db)):
    service = LecturaService(lectura_repo)

    try:
        return service.crear(db, data)
    except SQLAlchemyError:
        raise HTTPException(500, "Error interno")


@router.get("/", response_model=list[LecturaSchema])
def listar(db: Session = Depends(get_db)):
    try:
        return lectura_repo.get_all(db)
    except SQLAlchemyError:
        raise HTTPException(500, "Error interno")