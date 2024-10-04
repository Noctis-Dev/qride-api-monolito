import mercadopago
from dotenv import load_dotenv
import os

load_dotenv()
token = os.getenv("ACCESS_TOKEN_MERCADOPAGO")

sdk = mercadopago.SDK(token)

class MercadoPagoClient:

    def create_preference(self, preference_data: dict):
        preference_response = sdk.preference().create(preference_data)
        return preference_response["response"]

    def get_payment(self, payment_id: str):
        return sdk.payment().get(payment_id)["response"]