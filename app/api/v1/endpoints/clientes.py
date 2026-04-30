from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.schemas.ClienteSchema import ClienteCreate, ClienteSchema, ClienteUpdate
from app.repositories.ClienteRepository import cliente_repo

router = APIRouter()

@router.post("/", response_model=ClienteSchema)
def crear(data: ClienteCreate, db: Session = Depends(get_db)):
    return cliente_repo.create(db, data.dict())

@router.get("/", response_model=list[ClienteSchema])
def listar(db: Session = Depends(get_db)):
    return cliente_repo.get_all(db)

@router.get("/buscar", response_model=list[ClienteSchema]) # <-- Agregado response_model
def buscar(q: str = Query(...), db: Session = Depends(get_db)):
    return cliente_repo.search(db, q)

@router.put("/{id_cliente}", response_model=ClienteSchema)
def actualizar(id_cliente: str, data: ClienteUpdate, db: Session = Depends(get_db)):
    db_obj = cliente_repo.get(db, id_cliente)
    if not db_obj:
        raise HTTPException(404, "Cliente no encontrado")
    return cliente_repo.update(db, db_obj, data.dict(exclude_unset=True))

@router.delete("/{id_cliente}")
def eliminar(id_cliente: str, db: Session = Depends(get_db)):
    if not cliente_repo.delete(db, id_cliente):
        raise HTTPException(404, "No se pudo eliminar")
    return {"status": "success"}