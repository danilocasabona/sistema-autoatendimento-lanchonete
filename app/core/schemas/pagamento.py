from pydantic import BaseModel

<<<<<<< HEAD
class PagamentoCreateSchema(BaseModel):
    pedido_id: int
    
class PagamentoResponseSchema(BaseModel):
    codigo_pagamento:str
=======
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
>>>>>>> a46bd34a851478509f221f283c95751bffbe1290
