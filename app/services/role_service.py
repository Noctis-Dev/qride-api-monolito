from app.repositories.role_repository import RoleRepository

class RoleService:

    def __init__(self, role_repo: RoleRepository):
        self.role_repo = role_repo

    def initialize_roles(self):
        roles = ["passenger", "passenger_plus", "driver", "driver_admin", "checker"]
        for role_name in roles:
            role = self.role_repo.get_role_by_name(role_name)
            if not role:
                self.role_repo.create_role(role_name)