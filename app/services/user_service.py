from app.repositories.user_repository import UserRepository
from app.schemas.user_schema import UserCreate, UserUpdate

class UserService:

    def __init__(self, user_repo: UserRepository):
        self.user_repo = user_repo

    def get_user(self, user_id: int):
        return self.user_repo.get_user(user_id)

    def get_user_by_email(self, email: str):
        return self.user_repo.get_user_by_email(email)

    def get_users(self, skip: int = 0, limit: int = 100):
        return self.user_repo.get_users(skip, limit)

    def create_user(self, user: UserCreate):
        return self.user_repo.create_user(user)

    def update_user(self, user_id: int, user: UserUpdate):
        return self.user_repo.update_user(user_id, user)

    def delete_user(self, user_id: int):
        return self.user_repo.delete_user(user_id)