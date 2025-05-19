from pydantic import BaseModel

class PagamentoCreateSchema(BaseModel):
    pedido_id: int
    
class PagamentoResponseSchema(BaseModel):
    codigo_pagamento:str