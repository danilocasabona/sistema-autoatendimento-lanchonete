from pydantic import BaseModel

class CreatePagamentoSchemas(BaseModel):
    pedido_id: int

class ResponsePagamentoSchemas(BaseModel):
    pedido: int
    codigo_pagamento: str
    status: int