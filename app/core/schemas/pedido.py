import datetime
from pydantic import BaseModel
from typing import Optional
from typing import List

from app.core.schemas.cliente import ClienteResponseSchema
from app.core.schemas.produto import ProdutoResponseSchema
from app.core.schemas.status_pedido import StatusPedidoResponseSchema

class PedidoCreateSchema(BaseModel):
    cliente_id: Optional[int]
    produtos: list

class PedidoResponseSchema(BaseModel):
    pedido_id: int
    cliente_id: ClienteResponseSchema
    status: StatusPedidoResponseSchema
    data_criacao: datetime.time
    data_alteracao: Optional[datetime.time]
    data_finalizacao: Optional[datetime.time]

    class Config:
        allow_population_by_field_name = True
class PedidoAtualizaSchema(BaseModel):
    status: int
    
class PedidoProdutosResponseSchema(BaseModel):
    pedido_id: int
    cliente_id: ClienteResponseSchema
    status: StatusPedidoResponseSchema
    data_criacao: datetime.time
    data_alteracao: Optional[datetime.time]
    data_finalizacao: Optional[datetime.time]
    produtos: Optional[List[ProdutoResponseSchema]]
    
    class Config:
        allow_population_by_field_name = True

