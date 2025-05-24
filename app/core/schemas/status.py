from pydantic import BaseModel

class Status(BaseModel):
    pedido_id: int
    status: str
