from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db import get_db
from app.users.schemas.user import UserCreate, UserResponse
from app.users.infrastructure.user_repository_sql import SQLUserRepository

router = APIRouter()

@router.post("/register", response_model=UserResponse)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    user_repository = SQLUserRepository(db)
    new_user = user_repository.create_user(user)
    return new_user

