from sqlalchemy.orm import Session
from app.repositories.vehicle_repository import VehicleRepository
from app.schemas.vehicle_schema import VehicleCreate, VehicleUpdate

class VehicleService:

    def __init__(self, db: Session):
        self.vehicle_repository = VehicleRepository(db)

    def get_vehicle(self, vehicle_uuid: int):
        return self.vehicle_repository.get_vehicle(vehicle_uuid)

    def get_vehicle_by_route(self, route_id: int):
        return self.vehicle_repository.get_vehicle_by_route(route_id)

    def get_vehicles(self, skip: int = 0, limit: int = 100):
        return self.vehicle_repository.get_vehicles(skip, limit)

    def create_vehicle(self, vehicle: VehicleCreate, user_uuid: str):
        return self.vehicle_repository.create_vehicle(vehicle, user_uuid)

    def update_vehicle(self, vehicle_uuid: str, vehicle: VehicleUpdate):
        return self.vehicle_repository.update_vehicle(vehicle_uuid, vehicle)

    def delete_vehicle(self, vehicle_uuid: str):
        return self.vehicle_repository.delete_vehicle(vehicle_uuid)

    def get_users_by_vehicle(self, vehicle_uuid: str):
        return self.vehicle_repository.get_users_by_vehicle(vehicle_uuid)

    def get_vehicles_by_user(self, user_uuid: str):
        return self.vehicle_repository.get_vehicles_by_user(user_uuid)