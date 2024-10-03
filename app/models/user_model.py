from sqlalchemy import Column, BigInteger, Integer, String, ForeignKey, DECIMAL
from sqlalchemy.orm import relationship
from app.db import Base  

class User(Base):
    __tablename__ = 'users'

    user_id = Column(BigInteger, primary_key=True)
    user_uuid = Column(String(36), nullable=False)
    email = Column(String(50), nullable=False)
    password = Column(String(255), nullable=False)
    user_rol = Column(ForeignKey('roles.rol_id'), nullable=False, index=True)
    full_name = Column(String(100), nullable=False)
    profile_picture = Column(String(255), nullable=False)
    current_points = Column(Integer)
    balance = Column(DECIMAL(10, 2))
    phone_number = Column(String(15))

    role = relationship('Role')