from sqlalchemy.orm import Session
from app.models.user_model import User

class UserRepository:

    def __init__(self, db: Session):
        self.db = db

    def create_user(self, name: str, email: str):
        db_user = User(name=name, email=email)
        self.db.add(db_user)
        self.db.commit()
        self.db.refresh(db_user)
        return db_user

    def get_user(self, user_id: int):
        return self.db.query(User).filter(User.id == user_id).first()

    def update_user(self, user_id: int, name: str, email: str):
        db_user = self.db.query(User).filter(User.id == user_id).first()
        if db_user:
            db_user.name = name
            db_user.email = email
            self.db.commit()
            self.db.refresh(db_user)
        return db_user

    def delete_user(self, user_id: int):
        db_user = self.db.query(User).filter(User.id == user_id).first()
        if db_user:
            self.db.delete(db_user)
            self.db.commit()
        return db_user
