from app.domain.pagamento.ports import PagamentoRepositoryPort
from app.core.schemas.pagamento import PagamentoCreateSchema, PagamentoResponseSchema
from app.core.models.pagamento import Pagamento
from app.core.enums.status_pagamento import PagamentoStatusEnum
import uuid

class PagamentoUseCase:
    def __init__(self, pagamento_repository: PagamentoRepositoryPort):
        self.pagamento_repository = pagamento_repository

    def criar_pagamento(self, pagamento_request: PagamentoCreateSchema) -> PagamentoResponseSchema:
        
        codigo_pagamento = str(uuid.uuid4())
       
        pagamento_entity: Pagamento = Pagamento(pedido=pagamento_request.pedido_id, codigo_pagamento=codigo_pagamento, status=PagamentoStatusEnum.EmAndamento)
        pagamento_entity: Pagamento = self.pagamento_repository.criar_pagamento(pagamento=pagamento_entity)
        pagamento_response: PagamentoResponseSchema = PagamentoResponseSchema(codigo_pagamento=codigo_pagamento)
        return pagamento_response