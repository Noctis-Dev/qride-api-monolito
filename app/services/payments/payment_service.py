import requests
import json
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
        
        # 3. Enviar mensaje de WhatsApp
        whatsapp_response = await self.send_whatsapp_message(to="529512198832", template_name="soa_test")

        # 4. Retornar la respuesta de pago y la respuesta de WhatsApp
        return MPPaymentResponse(id=transaction.transaction_uuid, init_point=preference["init_point"], whatsapp_status=whatsapp_response)

    async def send_whatsapp_message(self, to: str, template_name: str, language_code: str = "es_MX"):
        # Tu token de autenticación (asegúrate de reemplazarlo)
        AUTH_TOKEN = "EAAYbJsPcZAXYBO322VPZAey7P5I8VbHZBtRMujZAMZAN4MIoEQFgSRlKjxnTohoKRRIY9gQUrOa9uGJIZBDnBsP4wOZA3UXHqZCc1Gj9UcvuQ4braLtfzZALEpFg3w1UziiUHQ5TLLoRYRFnK0PD7BjhuYgAMVlje7ub0oS1Gq3l6ZAYMhbFVji0AYCVk9pKTwVkN9zA1rGpbZANg5ktGoA3TewHbj0ujTC"
        # URL de la API de WhatsApp
        WHATSAPP_API_URL = "https://graph.facebook.com/v20.0/470243629495943/messages"

        # Cuerpo de la solicitud (el JSON con los detalles del mensaje)
        payload = {
            "messaging_product": "whatsapp",
            "to": to,  # Número del destinatario
            "type": "template",
            "template": {
                "name": template_name,
                "language": {
                    "code": language_code
                }
            }
        }

        # Encabezados
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {AUTH_TOKEN}"
        }

        # Enviar la solicitud POST con un tiempo de espera aumentado
        try:
            response = requests.post(WHATSAPP_API_URL, headers=headers, data=json.dumps(payload), timeout=30)
            response.raise_for_status()  # Levanta una excepción para códigos de estado HTTP 4xx/5xx
        except requests.exceptions.RequestException as e:
            return {
                "status": "error",
                "details": str(e)
            }

        # Verificar si el mensaje fue enviado con éxito
        if response.status_code == 200:
            return {"status": "success", "message": "Mensaje enviado"}
        else:
            return {
                "status": "error",
                "code": response.status_code,
                "details": response.text
            }

    async def process_mercadopago_notification(self, notification: dict):
        if notification["type"] == "payment":
            payment_id = notification["data"]["id"]
            payment = self.mercado_pago_client.get_payment(payment_id)

            if payment["status"] == "approved":
                await self.transaction_service.update_transaction_by_uuid(payment["external_reference"], {"description": "Payment approved"})
            elif payment["status"] == "rejected":
                await self.transaction_service.update_transaction_by_uuid(payment["external_reference"], {"description": "Payment rejected"})