from typing import Any
from sqlalchemy.ext.declarative import as_declarative, declared_attr
from sqlalchemy.orm import Session

@as_declarative()
class Base:
    id: Any
    __name__: str

    # Genera el nombre de la tabla automáticamente (Usuario -> usuario)
    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.lower()

def init_db(engine):
    # Creamos todo las tablas en docker
    Base.metadata.create_all(bind=engine)
    pass