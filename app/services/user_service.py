from sqlalchemy.orm import Session
from app.repositories.user_repository import UserRepository

class UserService:

    def __init__(self, db: Session):
        self.user_repository = UserRepository(db)

    def create_user(self, name: str, email: str):
        return self.user_repository.create_user(name, email)

    def get_user(self, user_id: int):
        return self.user_repository.get_user(user_id)

    def update_user(self, user_id: int, name: str, email: str):
        return self.user_repository.update_user(user_id, name, email)

    def delete_user(self, user_id: int):
        return self.user_repository.delete_user(user_id)
