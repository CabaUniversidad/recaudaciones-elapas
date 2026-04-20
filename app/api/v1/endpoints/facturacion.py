from fastapi import APIRouter
from schemas.LecturaSchema import LecturaCrear, LecturaVer

router = APIRouter()

@router.post("/registrar-lectura", response_model=LecturaVer)
def guardar_lectura(datos: LecturaCrear):
    # Aquí recibes el número del medidor y lo guardas
    return {**datos.dict(), "id": 100, "fecha_toma": "2026-04-20T08:00:00"}

@router.get("/estado-cuenta/{usuario_id}")
def ver_deudas(usuario_id: int):
    # Aquí buscas cuánto debe el usuario
    return {"usuario_id": usuario_id, "monto_pendiente": 50.5, "mes": "Abril"}