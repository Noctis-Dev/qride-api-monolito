from sqlalchemy.orm import Session
from app.models.role_model import Role
import uuid

class RoleRepository:

    def __init__(self, db: Session):
        self.db = db

    def get_role_by_name(self, role_name: str):
        return self.db.query(Role).filter(Role.role_name == role_name).first()

    def create_role(self, role_name: str):
        role_uuid = str(uuid.uuid4())  # Generar un UUID
        role = Role(role_name=role_name, role_uuid=role_uuid)
        self.db.add(role)
        self.db.commit()
        self.db.refresh(role)
        return role