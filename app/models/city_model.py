from sqlalchemy import Column, BigInteger, String
from app.db import Base  

class City(Base):
    __tablename__ = 'cities'

    city_id = Column(BigInteger, primary_key=True)
    city_uuid = Column(String(36), nullable=False)
    city_name = Column(String(50), nullable=False, unique=True)