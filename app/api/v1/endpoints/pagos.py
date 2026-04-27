from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from app.db.session import get_db
from app.schemas.PagoSchema import PagoCreate, PagoSchema
from app.repositories.PagoRepository import pago_repo

router = APIRouter()

@router.post("/", response_model=PagoSchema)
def pagar(data: PagoCreate, db: Session = Depends(get_db)):
    try:
        return pago_repo.create(db, data.dict())
    except SQLAlchemyError:
        raise HTTPException(500, "Error al procesar el pago")