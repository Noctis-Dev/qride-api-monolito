
from sqlalchemy import Column, Integer, String
from app.db import Base

class DBUser(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)  # Asegúrate de que existe este campo

    def __repr__(self):
        return f"<DBUser(username={self.username}, email={self.email})>"