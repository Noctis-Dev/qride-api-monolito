from fastapi import APIRouter, HTTPException, Depends, Request
from sqlalchemy.orm import Session
from app.schemas.payments_schema import MPPaymentRequest, MPPaymentResponse
from app.services.payments.payment_service import PaymentService
from app.services.payments.mercado_pago_client import MercadoPagoClient
from app.services.transaction_service import TransactionService
from app.db import get_db


router = APIRouter()

@router.post("/payments/mercadopago/subscription", response_model=MPPaymentResponse)
async def create_subscription(payment_request: MPPaymentRequest, db: Session = Depends(get_db)):
    mercado_pago_client = MercadoPagoClient()  
    transaction_service = TransactionService(db)
    payment_service = PaymentService(transaction_service=transaction_service, mercado_pago_client=mercado_pago_client)
    response = await payment_service.create_and_process_subscription(payment_request.user_id, payment_request.price)
    return response

@router.post("/payments/mercadopago/notifications")
async def mercadopago_notifications(request: Request, db: Session = Depends(get_db)):
    mercado_pago_client = MercadoPagoClient()  
    transaction_service = TransactionService(db)
    payment_service = PaymentService(transaction_service=transaction_service, mercado_pago_client=mercado_pago_client)
    try:
        notification = await request.json()
        await payment_service.process_mercadopago_notification(notification)
        return {"status": "success"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al procesar notificación: {str(e)}")