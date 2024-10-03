from sqlalchemy import Column, BigInteger, DateTime, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from app.db import Base


class VehicleUser(Base):
    __tablename__ = 'vehicle_users'

    vehicle_users_id = Column(BigInteger, primary_key=True)
    vehicle_id = Column(ForeignKey('vehicles.vehicle_id'), nullable=False, index=True)
    user_id = Column(ForeignKey('users.user_id'), nullable=False, index=True)
    start_date = Column(DateTime, nullable=False)
    end_date = Column(DateTime)
    is_owner = Column(Boolean)

    user = relationship('User')
    vehicle = relationship('Vehicle')