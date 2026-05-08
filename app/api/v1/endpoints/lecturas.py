from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError

from app.db.session import get_db
from app.api import deps
from app.schemas.LecturaSchema import LecturaCreate, LecturaSchema
from app.schemas.UploadSchema import PhotoPathUpdate
from app.repositories.LecturaRepository import lectura_repo
from app.services.lectura_service import LecturaService

router = APIRouter()

@router.post("/", response_model=LecturaSchema)
def crear(data: LecturaCreate, db: Session = Depends(get_db),
    current_user = Depends(deps.get_current_empleado)):
    service = LecturaService(lectura_repo)
    try:
        return service.crear(db, data)
    except SQLAlchemyError as e:
        raise HTTPException(status_code=500, detail=f"Error de base de datos: {str(e)}")

@router.get("/", response_model=list[LecturaSchema])
def listar(db: Session = Depends(get_db),
    current_user = Depends(deps.get_current_empleado)):
    try:
        return lectura_repo.get_all(db)
    except SQLAlchemyError:
        raise HTTPException(status_code=500, detail="Error interno al listar lecturas")

@router.get("/{id_lectura}", response_model=LecturaSchema)
def obtener(id_lectura: str, db: Session = Depends(get_db),
    current_user = Depends(deps.get_current_empleado)):
    obj = lectura_repo.get(db, id_lectura)
    if not obj:
        raise HTTPException(status_code=404, detail="Lectura no encontrada")
    return obj

@router.get("/medidor/{id_medidor}", response_model=list[LecturaSchema])
def por_medidor(id_medidor: str, db: Session = Depends(get_db),
    current_user = Depends(deps.get_current_empleado)):
    try:
        return lectura_repo.get_by_medidor(db, id_medidor)
    except SQLAlchemyError:
        raise HTTPException(status_code=500, detail="Error al buscar por medidor")

@router.patch("/{id_lectura}/foto")
def vincular_foto(
    id_lectura: str,
    payload: PhotoPathUpdate,
    db: Session = Depends(get_db),
    current_user = Depends(deps.get_current_empleado)
):
    """
    Actualiza el campo foto_url con el path del Storage de Supabase.
    """
    obj = lectura_repo.update_foto(db, id_lectura, payload.foto_url)
    if not obj:
        raise HTTPException(status_code=404, detail="Registro no encontrado")
    
    return {"status": "success", "path": obj.foto_url}