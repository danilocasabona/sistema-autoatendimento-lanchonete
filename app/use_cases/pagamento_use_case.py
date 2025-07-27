import uuid

from app.entities.pagamento.entity import PagamentoEntity
from app.entities.pagamento.model import PagamentoModel

from app.schemas.pagamento import PagamentoCreateSchema, PagamentoResponseSchema, PagamentoAtualizaSchema
from app.core.enums.status_pagamento import PagamentoStatusEnum

class PagamentoUseCase:
    def __init__(self, entity: PagamentoEntity):
        self.pagamentoEntity = entity
    
    def criar_pagamento(self, pedidoPagamento: PagamentoCreateSchema) -> PagamentoResponseSchema:
        codigoPagamento = str(uuid.uuid4())
        statusPagamento = PagamentoStatusEnum.EmAndamento

        pagamentoEntity: PagamentoModel = PagamentoModel(pedido=pedidoPagamento.pedido_id, codigo_pagamento=codigoPagamento, status=statusPagamento)
        pagamentoEntity: PagamentoModel = self.pagamentoEntity.create(pedido_pagamento=pagamentoEntity)
        
        pagamentoResponse: PagamentoResponseSchema = PagamentoResponseSchema(pedido_id=pagamentoEntity.pedido, codigo_pagamento=pagamentoEntity.codigo_pagamento, status=pagamentoEntity.status)
        
        return pagamentoResponse
    
    def buscar_por_codigo(self, codigoPagamento: str) -> PagamentoResponseSchema:
        pagamento_consulta: PagamentoModel = self.pagamentoEntity.getByCode(codigoPagamento=codigoPagamento)
        pagamento_response: PagamentoResponseSchema = PagamentoResponseSchema(pedido_id=pagamento_consulta.pedido, codigo_pagamento=pagamento_consulta.codigo_pagamento, status=pagamento_consulta.status)

        return pagamento_response
    
    def listar_todos(self) -> list[PagamentoResponseSchema]: 
        pagamentos: list[PagamentoModel] = self.pagamentoEntity.getAll()
        response: list[PagamentoResponseSchema] = []
        
        for pagamento in pagamentos:
            response.append(
                PagamentoResponseSchema(pedido_id=pagamento.pedido, codigo_pagamento=pagamento.codigo_pagamento, status=pagamento.status)
            )
        
        return response
    
    def atualizar_pagamento(self, codigo: str, pagamento_request: PagamentoAtualizaSchema) -> PagamentoResponseSchema: 
        pagamento: PagamentoModel = self.buscar_por_codigo(codigoPagamento=codigo)
        
        if not pagamento:
            raise ValueError("Pagamento não encontrado")
              
        pagamento.status = pagamento_request.status
        pagamento.codigo_pagamento = codigo

        clienteAtualizado: PagamentoModel = self.pagamentoEntity.update(pagamento=pagamento)
        pagamento_response: PagamentoResponseSchema = PagamentoResponseSchema(pedido_id=clienteAtualizado.pedido_id, codigo_pagamento=clienteAtualizado.codigo_pagamento, status=clienteAtualizado.status)

        return pagamento_response
    
    def deletar_pagamento(self, codigo_pagamento: str): 
        pagamento: PagamentoModel = self.buscarPorCodigo(codigoPagamento=codigo_pagamento)

        self.pagamentoEntity.delete(pagamento)