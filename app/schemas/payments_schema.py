from pydantic import BaseModel

class MPPaymentRequest(BaseModel):
    title: str
    quantity: int
    price: float
    user_id: int

class MPPaymentResponse(BaseModel):
    id: str
    init_point: str