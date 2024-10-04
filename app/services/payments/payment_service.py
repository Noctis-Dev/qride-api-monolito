from app.services.transaction_service import TransactionService
from app.services.payments.mercado_pago_client import MercadoPagoClient
from app.schemas.payments_schema import MPPaymentResponse

class PaymentService:
    def __init__(self, transaction_service: TransactionService, mercado_pago_client: MercadoPagoClient):
        self.transaction_service = transaction_service
        self.mercado_pago_client = mercado_pago_client

    async def create_and_process_subscription(self, user_id: int, amount: float) -> MPPaymentResponse:
        # 1. Crear la transacción usando el servicio de transacciones
        transaction = await self.transaction_service.create_transaction(user_id, "subscription", amount, "pending")
        
        # 2. Solicitar la preferencia de pago a Mercado Pago
        preference_data = {
            "items": [
                {"title": "Subscription payment", "quantity": 1, "unit_price": float(amount), "currency_id": "MXN"}
            ],
            "back_urls": {
                "success": "https://youtu.be/xvFZjo5PgG0?si=sKj8k1NQTptHh5OZ",
                "failure": "https://www.tuweb.com/failure",
                "pending": "https://www.tuweb.com/pending"
            },
            "auto_return": "approved",
            "external_reference": transaction.transaction_uuid
        }
        preference = self.mercado_pago_client.create_preference(preference_data)
        
        # 3. Retornar la respuesta de pago
        return MPPaymentResponse(id=transaction.transaction_uuid, init_point=preference["init_point"])

    async def process_mercadopago_notification(self, notification: dict):
        if notification["type"] == "payment":
            payment_id = notification["data"]["id"]
            payment = self.mercado_pago_client.get_payment(payment_id)

            if payment["status"] == "approved":
                await self.transaction_service.update_transaction_by_uuid(payment["external_reference"], {"description": "Payment approved"})
            elif payment["status"] == "rejected":
                await self.transaction_service.update_transaction_by_uuid(payment["external_reference"], {"description": "Payment rejected"})