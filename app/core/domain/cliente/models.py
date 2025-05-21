from pydantic import BaseModel, EmailStr
from typing import Optional

class Cliente(BaseModel):
    id: Optional[int] = None
    nome: str
    email: EmailStr
    telefone: Optional[str] = None
    cpf: str

    model_config = {"from_attributes": True}