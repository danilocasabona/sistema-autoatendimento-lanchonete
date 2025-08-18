from pydantic import BaseModel

class PagamentoAtualizaWebhookSchema(BaseModel):
    codigo_pagamento: str
    status: int