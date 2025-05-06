from pydantic import BaseModel

class PagamentoResponseSchema(BaseModel):
    id: int

class PagamentoCreateSchema(BaseModel):
    id: int