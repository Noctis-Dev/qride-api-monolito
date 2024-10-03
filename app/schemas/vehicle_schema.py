from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class VehicleBase(BaseModel):
    vehicle_uuid: str
    route_id: int
    current_location: Optional[str] = None
    status: Optional[str] = None

class VehicleCreate(VehicleBase):
    pass

class VehicleUpdate(VehicleBase):
    pass

class Vehicle(VehicleBase):
    vehicle_id: int

    class Config:
        orm_mode = True

class VehicleUserBase(BaseModel):
    vehicle_id: int
    user_id: int
    start_date: datetime
    end_date: Optional[datetime] = None
    is_owner: Optional[bool] = None

class VehicleUserCreate(VehicleUserBase):
    pass

class VehicleUserUpdate(VehicleUserBase):
    pass

class VehicleUser(VehicleUserBase):
    vehicle_users_id: int

    class Config:
        orm_mode = True