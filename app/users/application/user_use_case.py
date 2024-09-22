
from users.domain.user_service import UserService
from users.application.user_dto import UserDTO

class RegisterUserUseCase:
    def __init__(self, user_service: UserService):
        self.user_service = user_service

    def execute(self, user_dto: UserDTO):
        return self.user_service.register_user(
            user_id=user_dto.id, 
            name=user_dto.name, 
            email=user_dto.email
        )
