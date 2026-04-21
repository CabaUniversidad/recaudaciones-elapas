from fastapi import APIRouter, HTTPException
from typing import List
from app.schemas.MedidorSchema import MedidorCrear, MedidorVer

router = APIRouter()

@router.post("/", response_model=MedidorVer)
def registrar_medidor(datos: MedidorCrear):
    # Aquí iría la lógica para insertar en la base de datos
    # Por ahora simulamos la respuesta
    
    return {
        "id": 1,
        "codigo_serial": datos.codigo_serial,
        "tipo_tarifa": datos.tipo_tarifa,
        "usuario_id": datos.usuario_id
    }

@router.get("/usuario/{usuario_id}", response_model=List[MedidorVer])
def obtener_medidores_por_usuario(usuario_id: int):
    # Esto sirve para ver qué medidores tiene una persona
    return [
        {"id": 1, "codigo_serial": "ABC-123", "tipo_tarifa": "Doméstico", "usuario_id": usuario_id}
    ]