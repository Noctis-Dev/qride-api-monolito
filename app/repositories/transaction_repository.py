import uuid
from datetime import datetime
from sqlalchemy.orm import Session
from app.models.transaction_model import Transaction
from app.schemas.transaction_schema import TransactionCreate, TransactionUpdate

class TransactionRepository:

    def __init__(self, db: Session):
        self.db = db

    def get_transaction(self, transaction_uuid: str):
        return self.db.query(Transaction).filter(Transaction.transaction_uuid == transaction_uuid).first()

    def get_transaction_by_uuid(self, transaction_uuid: str):
        return self.db.query(Transaction).filter(Transaction.transaction_uuid == transaction_uuid).first()

    def get_transactions(self, skip: int = 0, limit: int = 100):
        return self.db.query(Transaction).offset(skip).limit(limit).all()

    def create_transaction(self, transaction: TransactionCreate):
        db_transaction = Transaction(
            transaction_uuid=str(uuid.uuid4()),
            user_id=transaction.user_id,
            transaction_type=transaction.transaction_type,
            amount=transaction.amount,
            commission=transaction.commission,
            description=transaction.description,
            transaction_date=datetime.utcnow()
        )
        self.db.add(db_transaction)
        self.db.commit()
        self.db.refresh(db_transaction)
        return db_transaction

    def update_transaction(self, transaction_uuid: str, transaction: TransactionUpdate):
        db_transaction = self.get_transaction(transaction_uuid)
        if db_transaction:
            for key, value in transaction.dict(exclude_unset=True).items():
                setattr(db_transaction, key, value)
            self.db.commit()
            self.db.refresh(db_transaction)
        return db_transaction

    def delete_transaction(self, transaction_uuid: str):
        db_transaction = self.get_transaction(transaction_uuid)
        if db_transaction:
            self.db.delete(db_transaction)
            self.db.commit()
        return db_transaction