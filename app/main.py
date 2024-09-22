from fastapi import FastAPI
from app.db import engine, Base
from app.users.infrastructure import user_controller  # Importa los controladores

app = FastAPI()

# Crea las tablas en la base de datos (solo necesario si usas un ORM como SQLAlchemy)
Base.metadata.create_all(bind=engine)

# Incluye las rutas del módulo de usuarios
app.include_router(user_controller.router)


@app.get("/")
def read_root():
    return {"message": "Welcome to Qride API"}

