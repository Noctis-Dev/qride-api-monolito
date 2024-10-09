from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.services.vehicle_service import VehicleService
from app.schemas.vehicle_schema import VehicleCreate, VehicleUpdate, Vehicle, VehicleUser
from app.db import get_db

router = APIRouter()

@router.get("/vehicles/{vehicle_uuid}", response_model=Vehicle)
def read_vehicle(vehicle_uuid: str, db: Session = Depends(get_db)):
    vehicle_service = VehicleService(db)
    vehicle = vehicle_service.get_vehicle(vehicle_uuid)
    if vehicle is None:
        raise HTTPException(status_code=404, detail="Vehicle not found")
    return vehicle

@router.get("/vehicles/", response_model=list[Vehicle])
def read_vehicles(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    vehicle_service = VehicleService(db)
    return vehicle_service.get_vehicles(skip, limit)

@router.post("/vehicles/", response_model=Vehicle)
def create_vehicle(vehicle: VehicleCreate, user_uuid: str, db: Session = Depends(get_db)):
    vehicle_service = VehicleService(db)
    return vehicle_service.create_vehicle(vehicle, user_uuid)

@router.put("/vehicles/{vehicle_uuid}", response_model=Vehicle)
def update_vehicle(vehicle_uuid: str, vehicle: VehicleUpdate, db: Session = Depends(get_db)):
    vehicle_service = VehicleService(db)
    return vehicle_service.update_vehicle(vehicle_uuid, vehicle)

@router.delete("/vehicles/{vehicle_uuid}", response_model=Vehicle)
def delete_vehicle(vehicle_uuid: str, db: Session = Depends(get_db)):
    vehicle_service = VehicleService(db)
    return vehicle_service.delete_vehicle(vehicle_uuid)

@router.get("/vehicles/{vehicle_uuid}/users", response_model=list[VehicleUser])
def read_users_by_vehicle(vehicle_uuid: str, db: Session = Depends(get_db)):
    vehicle_service = VehicleService(db)
    return vehicle_service.get_users_by_vehicle(vehicle_uuid)

@router.get("/users/{user_uuid}/vehicles", response_model=list[VehicleUser])
def read_vehicles_by_user(user_uuid: int, db: Session = Depends(get_db)):
    vehicle_service = VehicleService(db)
    return vehicle_service.get_vehicles_by_user(user_uuid)