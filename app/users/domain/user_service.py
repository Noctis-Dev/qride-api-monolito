from qride_api_monolito.app.users.domain.user import User
from qride_api_monolito.app.users.domain.user_repository import UserRepository


class UserService:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def register_user(self, user_id: int, name: str, email: str):
        if self.user_repository.find_by_email(email):
            raise ValueError("El usuario ya existe")
        
        new_user = User(user_id, name, email)
        self.user_repository.save(new_user)
        return new_user
