from datetime import datetime
from sqlalchemy.orm import Session
from app.models.vehicle_model import Vehicle
from app.models.vehicle_users_model import VehicleUser
from app.schemas.vehicle_schema import VehicleCreate, VehicleUpdate
from app.repositories.user_repository import UserRepository

class VehicleRepository:

    def __init__(self, db: Session):
        self.db = db

    def get_vehicle(self, vehicle_uuid: str):
        return self.db.query(Vehicle).filter(Vehicle.vehicle_uuid == vehicle_uuid).first()

    def get_vehicle_by_route(self, route_id: int):
        return self.db.query(Vehicle).filter(Vehicle.route_id == route_id).all()

    def get_vehicles(self, skip: int = 0, limit: int = 100):
        return self.db.query(Vehicle).offset(skip).limit(limit).all()

    def create_vehicle(self, vehicle: VehicleCreate, user_uuid: str):
        db_vehicle = Vehicle(**vehicle.dict())
        self.db.add(db_vehicle)
        self.db.commit()
        self.db.refresh(db_vehicle)

        # Obtener el ID del usuario
        user_db = UserRepository(self.db).get_user(user_uuid)

        # Crear la relación en vehicle_users
        db_vehicle_user = VehicleUser(
            vehicle_id=db_vehicle.vehicle_id,
            user_id= user_db.user_id,
            start_date=datetime.utcnow(),
            is_owner=True  # Asumimos que el usuario que crea el vehículo es el propietario
        )
        self.db.add(db_vehicle_user)
        self.db.commit()
        self.db.refresh(db_vehicle_user)

        return db_vehicle

    def update_vehicle(self, vehicle_uuid: str, vehicle: VehicleUpdate):
        db_vehicle = self.get_vehicle(vehicle_uuid)
        if db_vehicle:
            for key, value in vehicle.dict(exclude_unset=True).items():
                setattr(db_vehicle, key, value)
            self.db.commit()
            self.db.refresh(db_vehicle)
        return db_vehicle

    def delete_vehicle(self, vehicle_uuid: str):
        db_vehicle = self.get_vehicle(vehicle_uuid)
        if db_vehicle:
            self.db.delete(db_vehicle)
            self.db.commit()
        return db_vehicle

    def get_users_by_vehicle(self, vehicle_uuid: str):
        db_vehicle = self.get_vehicle(vehicle_uuid)
        return self.db.query(VehicleUser).filter(VehicleUser.vehicle_id == db_vehicle.vehicle_id).all()

    def get_vehicles_by_user(self, user_uuid: str):
        db_user = UserRepository(self.db).get_user(user_uuid)
        return self.db.query(VehicleUser).filter(VehicleUser.user_id == db_user.user_id).all()