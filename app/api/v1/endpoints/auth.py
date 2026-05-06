from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.repositories.EmpleadoRepository import empleado_repo
from app.core import security

router = APIRouter()

@router.post("/login")
def login(db: Session = Depends(get_db), form_data: OAuth2PasswordRequestForm = Depends()):
    # Buscar empleado por email (usando el username del form como email)
    empleado = empleado_repo.get_by_email(db, email=form_data.username)
    if not empleado or not security.verify_password(form_data.password, empleado.password_hash):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Email o contraseña incorrectos",
        )
    
    return {
        "access_token": security.create_access_token(empleado.id_empleado),
        "token_type": "bearer",
        "user": {
            "nombre": empleado.nombre,
            "rol": empleado.rol,
            "id": empleado.id_empleado
        }
    }