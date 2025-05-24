import datetime
from pydantic import BaseModel, Field, EmailStr, constr, ConfigDict
from typing import Optional
from typing import List

from app.core.enums import status_pedido
from app.core.schemas.cliente import ClienteResponseSchema
from app.core.schemas.produto import ProdutoResponseSchema
from app.core.schemas.pedido_produto import ProdutoPedidoResponseSchema

class PedidoCreateSchema(BaseModel):
    cliente_id: Optional[int]
    produtos: list

class PedidoResponseSchema(BaseModel):
    pedido_id: int
    cliente_id: int
    status: int
    data_criacao: datetime.time
    data_alteracao: Optional[datetime.time]
    data_finalizacao: Optional[datetime.time]

    class Config:
        allow_population_by_field_name = True
class PedidoAtualizaSchema(BaseModel):
    pedido_id: int
    status: int
    
class PedidoProdutosResponseSchema(BaseModel):
    pedido_id: int
    cliente_id: int
    status: int
    data_criacao: datetime.time
    data_alteracao: Optional[datetime.time]
    data_finalizacao: Optional[datetime.time]
    produtos: Optional[List[ProdutoPedidoResponseSchema]]
    
    class Config:
        allow_population_by_field_name = True

