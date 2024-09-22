from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from fastapi import Depends

# Ruta de la base de datos SQLite
DATABASE_URL = "sqlite:///./app.db"  # Aquí se crea el archivo en la raíz de 'app/'

# Crear el motor de base de datos
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

# Crear la sesión de la base de datos
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Declarar la base para los modelos ORM
Base = declarative_base()

# Dependency: cada solicitud tiene su propia sesión de base de datos
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
