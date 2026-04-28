from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError

from app.db.session import get_db
from app.schemas.EmpleadoSchema import EmpleadoCreate, EmpleadoSchema, EmpleadoUpdate
from app.repositories.EmpleadoRepository import empleado_repo

router = APIRouter()


@router.post("/", response_model=EmpleadoSchema)
def crear(data: EmpleadoCreate, db: Session = Depends(get_db)):
    try:
        return empleado_repo.create(db, data.dict())
    except SQLAlchemyError:
        raise HTTPException(status_code=500, detail="Error interno")


@router.get("/", response_model=list[EmpleadoSchema])
def listar(db: Session = Depends(get_db)):
    try:
        return empleado_repo.get_all(db)
    except SQLAlchemyError:
        raise HTTPException(status_code=500, detail="Error interno")


@router.get("/{id_empleado}", response_model=EmpleadoSchema)
def obtener(id_empleado: str, db: Session = Depends(get_db)):
    obj = empleado_repo.get(db, id_empleado)
    if not obj:
        raise HTTPException(status_code=404, detail="No encontrado")
    return obj