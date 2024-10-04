from sqlalchemy import Column, BigInteger, TIMESTAMP, String, ForeignKey, DECIMAL
from sqlalchemy.orm import relationship
from app.db import Base  

class Transaction(Base):
    __tablename__ = 'transactions'

    transaction_id = Column(BigInteger, primary_key=True)
    transaction_uuid = Column(String(36), nullable=False)
    user_id = Column(ForeignKey('users.user_id'), nullable=False, index=True)
    transaction_type = Column(String(50), nullable=False)
    amount = Column(DECIMAL(10, 2), nullable=False)
    commission = Column(DECIMAL(10, 2), nullable=False, server_default=("'0.00'"))
    description = Column(String(255))
    transaction_date = Column(TIMESTAMP, nullable=False)
    related_transaction_id = Column(BigInteger)

    user = relationship('User')