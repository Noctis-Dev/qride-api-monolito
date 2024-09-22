from fastapi import FastAPI
from app.db import engine, Base
from app.controllers.user_controller import router as user_router

app = FastAPI()

app.include_router(user_router, prefix="/api/v1")

@app.get("/")
def read_root():
    return {"message": "Welcome to Qride API"}

