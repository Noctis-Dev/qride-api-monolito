# coding: utf-8
from sqlalchemy import BigInteger, Column, DECIMAL, DateTime, Float, ForeignKey, Integer, String, TIMESTAMP, text
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.mysql import TINYINT
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class City(Base):
    __tablename__ = 'cities'

    city_id = Column(BigInteger, primary_key=True)
    city_name = Column(String(50), nullable=False, unique=True)


class Role(Base):
    __tablename__ = 'roles'

    rol_id = Column(BigInteger, primary_key=True)
    role_uuid = Column(String(36), nullable=False)
    role_name = Column(String(15), nullable=False, unique=True)


class Stop(Base):
    __tablename__ = 'stops'

    stop_id = Column(BigInteger, primary_key=True)
    stop_name = Column(String(255), nullable=False)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)


class Route(Base):
    __tablename__ = 'routes'

    route_id = Column(BigInteger, primary_key=True)
    route_name = Column(String(50), nullable=False)
    city_id = Column(ForeignKey('cities.city_id'), nullable=False, index=True)

    city = relationship('City')


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

    role = relationship('Role')


class Chat(Base):
    __tablename__ = 'chats'

    chat_id = Column(BigInteger, primary_key=True)
    route_id = Column(ForeignKey('routes.route_id'), index=True)
    city_id = Column(ForeignKey('cities.city_id'), nullable=False, index=True)
    created_at = Column(DateTime)

    city = relationship('City')
    route = relationship('Route')


class Notification(Base):
    __tablename__ = 'notifications'

    notification_id = Column(BigInteger, primary_key=True)
    user_id = Column(ForeignKey('users.user_id'), nullable=False, index=True)
    notification_type = Column(String(255), nullable=False)
    notification_message = Column(String(255), nullable=False)
    notification_time = Column(DateTime)
    is_read = Column(TINYINT(1))

    user = relationship('User')


class PointsTransaction(Base):
    __tablename__ = 'points_transactions'

    transaction_id = Column(BigInteger, primary_key=True)
    user_id = Column(ForeignKey('users.user_id'), nullable=False, index=True)
    points = Column(Integer, nullable=False)
    transaction_type = Column(String(255))
    description = Column(String(255))
    transaction_date = Column(DateTime)

    user = relationship('User')


class RouteStop(Base):
    __tablename__ = 'route_stops'

    route_stop_id = Column(BigInteger, primary_key=True)
    route_id = Column(ForeignKey('routes.route_id'), nullable=False, index=True)
    stop_id = Column(ForeignKey('stops.stop_id'), nullable=False, index=True)
    stop_order = Column(Integer, nullable=False)

    route = relationship('Route')
    stop = relationship('Stop')


class Transaction(Base):
    __tablename__ = 'transactions'

    transaction_id = Column(BigInteger, primary_key=True)
    user_id = Column(ForeignKey('users.user_id'), nullable=False, index=True)
    transaction_type = Column(String(50), nullable=False)
    amount = Column(DECIMAL(10, 2), nullable=False)
    commission = Column(DECIMAL(10, 2), nullable=False, server_default=text("'0.00'"))
    description = Column(String(255))
    transaction_date = Column(TIMESTAMP, nullable=False)
    related_transaction_id = Column(BigInteger)

    user = relationship('User')


class Vehicle(Base):
    __tablename__ = 'vehicles'

    vehicle_id = Column(BigInteger, primary_key=True)
    route_id = Column(ForeignKey('routes.route_id'), nullable=False, index=True)
    current_location = Column(String(255))
    status = Column(String(255))

    route = relationship('Route')


class Incident(Base):
    __tablename__ = 'incidents'

    incident_id = Column(BigInteger, primary_key=True)
    vehicle_id = Column(ForeignKey('vehicles.vehicle_id'), nullable=False, index=True)
    incident_type = Column(String(255), nullable=False)
    incident_description = Column(String(255))
    incident_time = Column(DateTime)

    vehicle = relationship('Vehicle')


class Message(Base):
    __tablename__ = 'messages'

    message_id = Column(BigInteger, primary_key=True)
    chat_id = Column(ForeignKey('chats.chat_id'), nullable=False, index=True)
    sender_id = Column(ForeignKey('users.user_id'), nullable=False, index=True)
    message_content = Column(String(255), nullable=False)
    sent_at = Column(DateTime)
    message_type = Column(String(20), nullable=False, server_default=text("'TEXT'"))

    chat = relationship('Chat')
    sender = relationship('User')


class QrCode(Base):
    __tablename__ = 'qr_codes'

    qr_code_id = Column(BigInteger, primary_key=True)
    qr_code_data = Column(String(255), nullable=False)
    stop_id = Column(ForeignKey('route_stops.route_stop_id'), nullable=False, index=True)

    stop = relationship('RouteStop')


class Trip(Base):
    __tablename__ = 'trips'

    trip_id = Column(BigInteger, primary_key=True)
    vehicle_id = Column(ForeignKey('vehicles.vehicle_id'), nullable=False, index=True)
    start_time = Column(DateTime)
    end_time = Column(DateTime)

    vehicle = relationship('Vehicle')


class VehicleUser(Base):
    __tablename__ = 'vehicle_users'

    vehicle_users_id = Column(BigInteger, primary_key=True)
    vehicle_id = Column(ForeignKey('vehicles.vehicle_id'), nullable=False, index=True)
    user_id = Column(ForeignKey('users.user_id'), nullable=False, index=True)
    start_date = Column(DateTime, nullable=False)
    end_date = Column(DateTime)
    is_owner = Column(TINYINT(1))

    user = relationship('User')
    vehicle = relationship('Vehicle')


class UsersTrip(Base):
    __tablename__ = 'users_trips'

    users_trips_id = Column(BigInteger, primary_key=True)
    trip_id = Column(ForeignKey('trips.trip_id'), nullable=False, index=True)
    user_id = Column(ForeignKey('users.user_id'), nullable=False, index=True)
    boarding_time = Column(DateTime)
    alighting_time = Column(DateTime)

    trip = relationship('Trip')
    user = relationship('User')
