from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class TransactionBase(BaseModel):
    user_id: int
    transaction_type: str
    amount: float
    commission: Optional[float] = 0.00
    description: Optional[str] = None

class TransactionCreate(TransactionBase):
    pass

class TransactionUpdate(TransactionBase):
    pass

class Transaction(TransactionBase):
    transaction_id: int

    class Config:
        from_attributes = True