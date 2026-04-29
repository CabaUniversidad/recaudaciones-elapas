from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.core.security import SECRET_KEY, ALGORITHM
from app.repositories.EmpleadoRepository import empleado_repo

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="api/v1/auth/login")

def get_current_empleado(db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="No se pudo validar el acceso",
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        empleado_id: str = payload.get("sub")
        if empleado_id is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    
    empleado = empleado_repo.get(db, empleado_id)
    if not empleado:
        raise credentials_exception
    return empleado