from sqlalchemy import BigInteger, Column, String
from app.db import Base

class Role(Base):
    __tablename__ = 'roles'

    rol_id = Column(BigInteger, primary_key=True, autoincrement=True)
    role_uuid = Column(String(36), nullable=False)
    role_name = Column(String(15), nullable=False, unique=True)