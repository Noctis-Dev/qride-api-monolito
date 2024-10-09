import uuid
from sqlalchemy.orm import Session
from app.models.user_model import User
from app.schemas.user_schema import UserCreate, UserUpdate
from app.models.transaction_model import Transaction

class UserRepository:

    def __init__(self, db: Session):
        self.db = db

    def get_user(self, user_uuid: str):
        return self.db.query(User).filter(User.user_uuid == user_uuid).first()

    def get_user_by_email(self, email: str):
        return self.db.query(User).filter(User.email == email).first()

    def get_users(self, skip: int = 0, limit: int = 100):
        return self.db.query(User).offset(skip).limit(limit).all()

    def create_user(self, user: UserCreate):
        user_uuid = str(uuid.uuid4())  # Generar un UUID
        db_user = User(user_uuid=user_uuid, **user.dict())
        self.db.add(db_user)
        self.db.commit()
        self.db.refresh(db_user)
        return db_user

    def update_user(self, user_uuid: str, user: UserUpdate):
        db_user = self.get_user(user_uuid)
        if db_user:
            db_user.email = user.email
            db_user.full_name = user.full_name
            db_user.profile_picture = user.profile_picture
            db_user.current_points = user.current_points
            db_user.balance = user.balance
            db_user.phone_number = user.phone_number
            if user.password is not None:
                db_user.password = user.password 
            if user.user_rol is not None:
                db_user.user_rol = user.user_rol
            self.db.commit()
            self.db.refresh(db_user)
        return db_user

    def delete_user(self, user_uuid: str):
        db_user = self.get_user(user_uuid)
        if db_user:
            # Eliminar transacciones asociadas
            self.db.query(Transaction).filter(Transaction.user_id == db_user.user_id).delete()
            self.db.delete(db_user)
            self.db.commit()
        return db_user