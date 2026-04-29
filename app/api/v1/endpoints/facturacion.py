from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.services.cobro_service import cobro_service
from app.schemas.FacturaSchema import FacturaSchema

router = APIRouter()

@router.post("/generar/{id_cliente}", response_model=FacturaSchema)
def procesar_factura(id_cliente: str, db: Session = Depends(get_db)):
    factura = cobro_service.generar_factura_mensual(db, id_cliente)
    if not factura:
        raise HTTPException(
            status_code=404, 
            detail="No se encontraron lecturas pendientes para facturar a este cliente"
        )
    return factura