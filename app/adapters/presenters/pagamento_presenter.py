from pydantic import BaseModel
from app.adapters.schemas.pagamento import PagamentoAtualizaSchema

class WebhookResponse(BaseModel):
    status: str
    data: PagamentoAtualizaSchema