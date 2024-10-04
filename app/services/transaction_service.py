from sqlalchemy.orm import Session
from app.repositories.transaction_repository import TransactionRepository
from app.schemas.transaction_schema import TransactionCreate, TransactionUpdate

class TransactionService:

    def __init__(self, db: Session):
        self.transaction_repository = TransactionRepository(db)

    async def get_transaction(self, transaction_id: int):
        return self.transaction_repository.get_transaction(transaction_id)

    async def get_transactions(self, skip: int = 0, limit: int = 100):
        return self.transaction_repository.get_transactions(skip, limit)

    async def create_transaction(self, user_id: int, transaction_type: str, amount: float, description: str):
        transaction = TransactionCreate(
            user_id=user_id,
            transaction_type=transaction_type,
            amount=amount,
            commission=0.00,
            description=description
        )
        return self.transaction_repository.create_transaction(transaction)

    async def update_transaction(self, transaction_id: int, transaction: TransactionUpdate):
        return self.transaction_repository.update_transaction(transaction_id, transaction)

    async def delete_transaction(self, transaction_id: int):
        return self.transaction_repository.delete_transaction(transaction_id)

    async def update_transaction_by_uuid(self, transaction_uuid: str, update_data: dict):
        transaction = self.transaction_repository.get_transaction_by_uuid(transaction_uuid)
        if transaction:
            for key, value in update_data.items():
                setattr(transaction, key, value)
            self.transaction_repository.db.commit()
            self.transaction_repository.db.refresh(transaction)
        return transaction