from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from core.config import settings

# Usamos la URL que definimos en core/config.py
engine = create_engine(settings.DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Dependencia para los endpoints
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()