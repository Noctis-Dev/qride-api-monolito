from pydantic import BaseModel

class MPPaymentRequest(BaseModel):
    user_id: int
    price: float

class MPPaymentResponse(BaseModel):
    id: str
    init_point: str
    whatsapp_status: dict 