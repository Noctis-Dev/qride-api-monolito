
from sqlalchemy.orm import Session
from app.users.domain.user import DBUser
from app.users.schemas.user import UserCreate

class SQLUserRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_user(self, user_create: UserCreate):
        # Asegúrate de que el nombre del atributo coincide con el modelo
        db_user = DBUser(
            username=user_create.username,
            email=user_create.email,
            hashed_password=user_create.password  # Hashea la contraseña antes de guardarla
        )
        self.db.add(db_user)
        self.db.commit()
        self.db.refresh(db_user)
        return db_user
