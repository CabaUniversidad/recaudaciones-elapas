from sqlalchemy.orm import Session
from app.models.Empleado import Empleado
from app.repositories.BaseRepository import BaseRepository
from app.core.security import get_password_hash

class EmpleadoRepository(BaseRepository[Empleado]):
    def __init__(self):
        super().__init__(Empleado, "id_empleado")

    def create(self, db, data: dict):
        # Extraemos la contraseña plana y la hasheamos inmediatamente
        password_plana = data.pop("password") 
        data["password_hash"] = get_password_hash(password_plana)
        
        # Ahora 'data' ya no tiene la contraseña original, solo el hash seguro
        db_obj = self.model(**data)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def get_by_email(self, db: Session, email: str):
        return db.query(Empleado).filter(Empleado.email == email).first()

empleado_repo = EmpleadoRepository()