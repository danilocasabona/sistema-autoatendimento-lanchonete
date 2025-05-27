from pydantic import BaseModel, EmailStr, constr, ConfigDict
from app.core.schemas.cliente import *
from app.core.schemas.produto import *
from app.core.enums import status_pedido
from typing import Optional
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
    
    model_config = ConfigDict(arbitrary_types_allowed=True)
    
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

