from pydantic import BaseModel
from typing import Optional
from decimal import Decimal

# 🧩 Schema para entrada de dados (criação de produto)
class ProdutoCreateSchema(BaseModel):
    nome: str
    descricao: Optional[str] = None
    preco: Decimal

# 🧩 Schema para saída de dados (resposta da API)
class ProdutoResponseSchema(BaseModel):
    id: int
    nome: str
    descricao: Optional[str] = None
    preco: Decimal

    class Config:
        orm_mode = True
