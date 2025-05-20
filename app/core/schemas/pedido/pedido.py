from pydantic import BaseModel, EmailStr, constr, ConfigDict
from app.core.schemas.cliente import ClienteResponseSchema, ClienteCreateSchema 
from app.core.schemas.produto.produto import ProdutoCreateSchema, ProdutoResponseSchema
from typing import Optional
import datetime

# 🧩 Schema para entrada de dados (criação de pedido)
class PedidoCreateSchema(BaseModel):
    produtos: Optional[list[int]]
    cliente: Optional[int]

    model_config = ConfigDict(extra="forbid", from_attributes=True)

# 🧩 Schema para saída de dados (resposta da API)
class PedidoResponseSchema(BaseModel):
    id: int
    cliente: ClienteResponseSchema
    produtos: list[ProdutoResponseSchema]
    status: str
    data_criacao: str
    
    model_config = ConfigDict(from_attributes=True)


# 🧩 Schema para atualização de dados (update)
class PedidoAtualizaSchema(BaseModel):
    produtos: Optional[list[int]]
    cliente: int

    model_config = ConfigDict(extra="forbid", from_attributes=True)
    

# class PedidoCreateSchema(BaseModel):
#     cliente: Optional[int]
#     produto_1: Optional[int]
#     produto_2: Optional[int]
#     produto_3: Optional[int]
#     produto_4: Optional[int]

# class PedidoAtualizaSchema(BaseModel):
#     id: int
#     cliente: Optional[int]
#     produto_1: Optional[int]
#     produto_2: Optional[int]
#     produto_3: Optional[int]
#     produto_4: Optional[int]
#     status: str
    
# class PedidoResponseSchema():
#     def __init__(self, id: int, cliente: ClienteResponseSchema, produto1: ProdutoResponseSchema, produto2: ProdutoResponseSchema, produto3: ProdutoResponseSchema, produto4: ProdutoResponseSchema, status: str, dataCriacao: str):
#         self.id = id
#         self.cliente = cliente
#         self.produto_1 = produto1
#         self.produto_2 = produto2
#         self.produto_3 = produto3
#         self.produto_4 = produto4
#         self.status = status
#         self.data_criacao = dataCriacao
        
#     id: int
#     cliente: ClienteResponseSchema
#     produto_1: ProdutoResponseSchema
#     produto_2: ProdutoResponseSchema
#     produto_3: ProdutoResponseSchema
#     produto_4: ProdutoResponseSchema
#     status: str
#     data_criacao: str
    
# class PedidosResponseSchema(BaseModel):
#     pedidos: [PedidoResponseSchema]
    
    
