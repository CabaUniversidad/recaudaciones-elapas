from typing import Generic, TypeVar, Type, Optional, List
from sqlalchemy.orm import Session
from app.db.base_class import Base

ModelType = TypeVar("ModelType", bound=Base)

class BaseRepository(Generic[ModelType]):
    def __init__(self, model: Type[ModelType], id_field: str):
        self.model = model
        self.id_field = id_field

    def get(self, db: Session, id_value) -> Optional[ModelType]:
        return db.query(self.model).filter(
            getattr(self.model, self.id_field) == id_value
        ).first()

    def get_all(self, db: Session) -> List[ModelType]:
        return db.query(self.model).all()

    def delete(self, db: Session, id_value) -> Optional[ModelType]:
        obj = self.get(db, id_value)
        if obj:
            db.delete(obj)
            db.commit()
        return obj