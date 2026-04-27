from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from app.db.session import get_db
from app.repositories.FacturaRepository import factura_repo
from app.repositories.DetalleFacturaRepository import detalle_repo
from app.repositories.LecturaRepository import lectura_repo
from app.services.cobro_service import CobroService

router = APIRouter()

@router.post("/generar/{id_usuario}")
def generar_factura(id_usuario: str, db: Session = Depends(get_db)):

    lecturas = lectura_repo.get_all(db)

    if not lecturas:
        raise HTTPException(404, "No hay datos disponibles")

    service = CobroService(factura_repo, detalle_repo)

    try:
        return service.generar_factura(db, id_usuario, lecturas)
    except SQLAlchemyError:
        raise HTTPException(500, "Error al generar factura")