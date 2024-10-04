from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.services.transaction_service import TransactionService
from app.schemas.transaction_schema import TransactionCreate, TransactionUpdate, Transaction
from app.db import get_db

router = APIRouter()

@router.get("/transactions/{transaction_id}", response_model=Transaction)
def read_transaction(transaction_id: int, db: Session = Depends(get_db)):
    transaction_service = TransactionService(db)
    transaction = transaction_service.get_transaction(transaction_id)
    if transaction is None:
        raise HTTPException(status_code=404, detail="Transaction not found")
    return transaction

@router.get("/transactions/", response_model=list[Transaction])
def read_transactions(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    transaction_service = TransactionService(db)
    return transaction_service.get_transactions(skip, limit)

@router.post("/transactions/", response_model=Transaction)
def create_transaction(transaction: TransactionCreate, db: Session = Depends(get_db)):
    transaction_service = TransactionService(db)
    return transaction_service.create_transaction(transaction)

@router.put("/transactions/{transaction_id}", response_model=Transaction)
def update_transaction(transaction_id: int, transaction: TransactionUpdate, db: Session = Depends(get_db)):
    transaction_service = TransactionService(db)
    return transaction_service.update_transaction(transaction_id, transaction)

@router.delete("/transactions/{transaction_id}", response_model=Transaction)
def delete_transaction(transaction_id: int, db: Session = Depends(get_db)):
    transaction_service = TransactionService(db)
    return transaction_service.delete_transaction(transaction_id)

