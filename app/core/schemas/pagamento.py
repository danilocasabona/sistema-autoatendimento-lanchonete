from pydantic import BaseModel
from typing import Optional
from app.core.enums.status_pagamento import PagamentoStatusEnum

class PagamentoCreateSchema(BaseModel):
    pedido_id: int
    
class PagamentoResponseSchema(BaseModel):
    pedido_id: int
    codigo_pagamento:str
    status: str
    
class PagamentoAtualizaSchema(BaseModel):
    pedido_id: int
    codigo_pagamento:str
    status: str