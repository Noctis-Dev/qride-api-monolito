import pytest
from fastapi.testclient import TestClient
from app.main import app  # Asegúrate de importar la aplicación FastAPI desde el archivo adecuado
from app.db import SessionLocal, engine, Base  # Ajusta el import según tu configuración
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

@pytest.fixture(scope="module")
def test_db():
    # Crear todas las tablas en la base de datos de prueba
    Base.metadata.create_all(bind=engine)
    yield
    # Eliminar todas las tablas después de las pruebas
    Base.metadata.drop_all(bind=engine)

@pytest.fixture(scope="function")
def db_session(test_db):
    # Crear una nueva sesión para cada prueba
    connection = engine.connect()
    transaction = connection.begin()
    session = SessionLocal(bind=connection)
    yield session
    session.close()
    transaction.rollback()
    connection.close()

@pytest.fixture(scope="module")
def client():
    return TestClient(app)
