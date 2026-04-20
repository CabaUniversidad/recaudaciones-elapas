from fastapi import APIRouter
from schemas.LecturaSchema import LecturaCrear, LecturaVer

router = APIRouter()

@router.post("/", response_model=LecturaVer)
def registrar_nueva_lectura(datos: LecturaCrear):
    # Lógica: Se recibe el número que marca el medidor
    return {
        "id": 50,
        "valor_marcado": datos.valor_marcado,
        "fecha_toma": "2026-04-20T08:00:00",
        "medidor_id": datos.medidor_id
    }

@router.get("/historial/{medidor_id}")
def ver_historial_de_lecturas(medidor_id: int):
    # Sirve para ver cómo ha ido consumiendo el usuario en el tiempo
    return {
        "medidor_id": medidor_id,
        "lecturas": [
            {"fecha": "2026-02-20", "valor": 1050.5},
            {"fecha": "2026-03-20", "valor": 1100.2}
        ]
    }