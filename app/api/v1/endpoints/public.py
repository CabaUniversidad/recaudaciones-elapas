from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.schemas.PublicSchema import ConsultaDeudaRequest, PublicDeudaResponse
from app.repositories.MedidorRepository import medidor_repo

router = APIRouter()

@router.post("/consulta-deuda", response_model=PublicDeudaResponse)
def consultar_deuda(payload: ConsultaDeudaRequest, db: Session = Depends(get_db)):
    # Los argumentos ci y codigo_medidor vienen del payload validado
    resultado = medidor_repo.consultar_deuda_publica(
        db, 
        ci=payload.ci, 
        codigo_medidor=payload.codigo_medidor
    )
    
    if not resultado:
        raise HTTPException(
            status_code=404, 
            detail="No se encontró un registro que coincida con el CI y código de medidor proporcionados."
        )
        
    return resultado