from pydantic import BaseModel, EmailStr
from typing import Optional

class Cliente():
    #id: Optional[int] = None
    # nome: str
    # email: EmailStr
    # telefone: Optional[str] = None
    # cpf: str

    def __init__(self, nome: str, email: EmailStr, telefone: str, cpf: str):
        self.nome = nome
        self.email = email
        self.telefone = telefone
        self.cpf = cpf

    model_config = {
        "from_attributes": True
    }