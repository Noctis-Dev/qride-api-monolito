from fastapi import FastAPI
from app.db import engine, Base, SessionLocal
from app.controllers.user_controller import router as user_router
from app.controllers.vehicle_controller import router as vehicle_router
from app.controllers.transaction_controller import router as transaction_router
from app.controllers.payments_controller import router as payments_router
from app.repositories.role_repository import RoleRepository
from app.services.role_service import RoleService


# Crear la base de datos y las tablas
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Inicializar los roles
def initialize_roles():
    db = SessionLocal()
    role_repo = RoleRepository(db)
    role_service = RoleService(role_repo)
    role_service.initialize_roles()
    db.close()

initialize_roles()

app.include_router(user_router, prefix="/api/v1")
app.include_router(vehicle_router , prefix="/api/v1")
app.include_router(transaction_router, prefix="/api/v1")
app.include_router(payments_router, prefix="/api/v1")

@app.get("/")
def read_root():
    return {"message": "Welcome to Qride API"}

