from sqlalchemy import Column, BigInteger, String, ForeignKey
from sqlalchemy.orm import relationship
from app.db import Base  
from app.models.city_model import City

class Route(Base):
    __tablename__ = 'routes'

    route_id = Column(BigInteger, primary_key=True)
    route_uuid = Column(String(36), nullable=False)
    route_name = Column(String(50), nullable=False)
    city_id = Column(ForeignKey('cities.city_id'), nullable=False, index=True)

    city = relationship('City')