from pydantic import BaseModel, EmailStr, constr, ConfigDict
from typing import Optional

class ClienteCreateSchema(BaseModel):
    nome: constr(min_length=3, max_length=100)
    email: EmailStr
    telefone: Optional[constr(min_length=10, max_length=11, pattern=r'^\d{10,11}$')] = None  # Ex: 11912345678
    cpf: constr(min_length=11, max_length=11, pattern=r'^\d{11}$')

class ClienteResponseSchema(ClienteCreateSchema):
    id: int
    telefone: Optional[str] = None

    model_config = ConfigDict(from_attributes=True)

class ClienteUpdateSchema(BaseModel):
    nome: Optional[constr(min_length=3, max_length=100)] = None
    email: Optional[EmailStr] = None
    telefone: Optional[constr(min_length=10, max_length=15)] = None
    cpf: Optional[constr(min_length=11, max_length=11, pattern=r'^\d{11}$')] = None