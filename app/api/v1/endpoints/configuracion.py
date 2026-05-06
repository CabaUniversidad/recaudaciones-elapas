from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.models.Zona import Zona
from app.models.Ruta import Ruta
from app.models.Tarifa import Tarifa
import uuid

router = APIRouter()

@router.post("/zonas")
def crear_zona(nombre: str, descripcion: str = None, db: Session = Depends(get_db)):
    obj = Zona(nombre=nombre, descripcion=descripcion)
    db.add(obj)
    db.commit()
    return obj

@router.post("/rutas")
def crear_ruta(nombre: str, id_zona: str, db: Session = Depends(get_db)):
    obj = Ruta(nombre=nombre, id_zona=uuid.UUID(id_zona))
    db.add(obj)
    db.commit()
    return obj

@router.post("/tarifas")
def crear_tarifa(nombre: str, precio: float, db: Session = Depends(get_db)):
    obj = Tarifa(nombre=nombre, precio_por_m3=precio)
    db.add(obj)
    db.commit()
    return obj

@router.get("/tarifas")
def listar_tarifas(db: Session = Depends(get_db)):
    return db.query(Tarifa).all()