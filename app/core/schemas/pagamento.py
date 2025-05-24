from pydantic import BaseModel

class PagamentoSchemas(BaseModel):
    pedido_id: int

class ResponsePagamentoSchemas(BaseModel):
    pedido_id: int
    cliente: int
    produto_1: int
    produto_2: int
    produto_3: int
    produto_4: int
    status: int