from sqlalchemy.orm import Session
from app.models.Empleado import Empleado
from app.repositories.BaseRepository import BaseRepository


class EmpleadoRepository(BaseRepository[Empleado]):

    def __init__(self):
        super().__init__(Empleado, "id_empleado")

    def create(self, db: Session, data: dict) -> Empleado:
        obj = Empleado(**data)
        db.add(obj)
        db.commit()
        db.refresh(obj)
        return obj


empleado_repo = EmpleadoRepository()