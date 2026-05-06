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
    except SQLAlchemyError as e:
        print(f"DEBUG ERROR: {e}") # Esto imprimirá el error real en los logs de Render
        raise HTTPException(status_code=500, detail=str(e)) # Muestra el error en Swagger


# GET /lecturas (web)
@router.get("/", response_model=list[LecturaSchema])
def listar(db: Session = Depends(get_db)):
    try:
        return lectura_repo.get_all(db)
    except SQLAlchemyError:
        raise HTTPException(status_code=500, detail="Error interno")


# GET /lecturas/{id_lectura}
@router.get("/{id_lectura}", response_model=LecturaSchema)
def obtener(id_lectura: str, db: Session = Depends(get_db)):
    obj = lectura_repo.get(db, id_lectura)
    if not obj:
        raise HTTPException(status_code=404, detail="No encontrado")
    return obj


# GET /lecturas/medidor/{id_medidor}
@router.get("/medidor/{id_medidor}", response_model=list[LecturaSchema])
def por_medidor(id_medidor: str, db: Session = Depends(get_db)):
    try:
        return lectura_repo.get_by_medidor(db, id_medidor)
    except SQLAlchemyError:
        raise HTTPException(status_code=500, detail="Error interno")