from app.core.schemas.pagamento import CreatePagamentoSchemas, ResponsePagamentoSchemas
from app.core.domain.pagamento.ports import PagamentoRepositoryPort
from app.adapters.out.pagamento_repository import PagamentoRepository
from app.core.domain.pagamento.entity import PagamentoEntity
from app.core.enums.status_pagamento import StatusPagamentoEnum
from app.core.models.pagamento import Pagamento
import uuid

class pagamentoUseCase():
    
    def __init__(self, pagamento_repository: PagamentoRepositoryPort):
        self.pagamento_repository = pagamento_repository
    
    def efetuar_pagamento(self, pagamento_pedido: CreatePagamentoSchemas) -> CreatePagamentoSchemas:
        
        codigo_pagamento = str(uuid.uuid4())
        status_pagamento = StatusPagamentoEnum.Aprovado
        
        pagamento_entity: Pagamento = Pagamento(pedido=pagamento_pedido, codigo_pagamento=codigo_pagamento, status=status_pagamento)
        pagamento_criado: PagamentoRepository = self.pagamento_repository.efetuar_pagamento(pagamento_pedido=pagamento_entity)
        pagamento_response: ResponsePagamentoSchemas = ResponsePagamentoSchemas(pedido=pagamento_criado.pedido, codigo_pagamento=pagamento_criado.codigo_pagamento, status=pagamento_criado.status)

        # pagamento_entity: PagamentoEntity = PagamentoEntity(pedido=pagamento_pedido, codigo_pagamento=codigo_pagamento, status=status_pagamento)
        # pagamento_criado: PagamentoRepository = self.pagamento_repository.efetuar_pagamento(pagamento=pagamento_entity)
        # pagamento_response: ResponsePagamentoSchemas = ResponsePagamentoSchemas(pedido=pagamento_criado.pedido, codigo_pagamento=pagamento_criado.codigo_pagamento, status=pagamento_criado.status)
    
        return pagamento_response
    
    def listar_pagamento_realizado():
        pass
  