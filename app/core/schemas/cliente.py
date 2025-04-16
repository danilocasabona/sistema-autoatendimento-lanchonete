from pydantic import BaseModel, EmailStr, constr
from typing import Optional

class ClienteCreateSchema(BaseModel):
    nome: constr(min_length=3, max_length=100)
    email: EmailStr
    telefone: constr(min_length=10, max_length=15) | None = None  # Ex: +5511912345678
    cpf: constr(min_length=11, max_length=11, pattern=r'^\d{11}$')

class ClienteResponseSchema(ClienteCreateSchema):
    id: int

    class Config:
        from_attributes = True  # substitui o orm_mode do Pydantic v1

class ClienteUpdateSchema(BaseModel):
    nome: Optional[constr(min_length=3, max_length=100)] = None
    email: Optional[EmailStr] = None
    telefone: Optional[constr(min_length=10, max_length=15)] = None
    cpf: Optional[constr(min_length=11, max_length=11, pattern=r'^\d{11}$')] = None