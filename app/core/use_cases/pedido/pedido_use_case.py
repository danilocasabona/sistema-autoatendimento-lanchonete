import datetime

from app.core.domain.pedido.ports import PedidoRepositoryPort 
from app.core.enums.status_pedido import StatusPedidoEnum
from app.core.models.pedido import Pedido

from app.core.schemas.pedido import PedidoCreateSchema, PedidoResponseSchema, PedidoAtualizaSchema
from app.core.utils.debug import var_dump_die

class PedidoUseCase:
    def __init__(self, pedido_repository: PedidoRepositoryPort):
        self.pedido_repository = pedido_repository

    def criarPedido(self, pedidoRequest: PedidoCreateSchema) -> PedidoResponseSchema:
        pedidoEntity: Pedido = Pedido(cliente_id=pedidoRequest.cliente_id, status=1)
        pedidoEntity.status = StatusPedidoEnum.Recebido
        pedidoEntity.data_criacao = datetime.datetime.now()
        
        pedidoCriado: Pedido = self.pedido_repository.criarPedido(pedido=pedidoEntity)
        pedidoResponse: PedidoResponseSchema = PedidoResponseSchema(pedido_id=pedidoCriado.pedido_id, cliente_id=pedidoCriado.cliente_id, status=pedidoCriado.status, data_criacao=pedidoCriado.data_criacao, data_alteracao=pedidoCriado.data_alteracao, data_finalizacao=pedidoCriado.data_finalizacao)

        return pedidoResponse

    def buscar_por_id(self, pedido_id: int) -> PedidoResponseSchema:
        pedidoBusca: Pedido = self.pedido_repository.buscar_por_id(id=pedido_id)
        pedidoResponse: PedidoResponseSchema = PedidoResponseSchema(pedido_id=pedidoBusca.pedido_id, cliente_id=pedidoBusca.cliente_id, status=pedidoBusca.status, data_criacao=pedidoBusca.data_criacao, data_alteracao=pedidoBusca.data_alteracao, data_finalizacao=pedidoBusca.data_finalizacao)
        
        return pedidoResponse
    
    def listar_todos(self) -> list[PedidoResponseSchema]:
        pedidosBusca: list[Pedido] = self.pedido_repository.listar_todos()
        pedidosResponse: list[PedidoResponseSchema] = []
        
        for pedidoBusca in pedidosBusca:
            pedidosResponse.append(PedidoResponseSchema(pedido_id=pedidoBusca.pedido_id, cliente_id=pedidoBusca.cliente_id, status=pedidoBusca.status, data_criacao=pedidoBusca.data_criacao, data_alteracao=pedidoBusca.data_alteracao, data_finalizacao=pedidoBusca.data_finalizacao))
        
        return pedidosResponse
    
    def atualiza(self, pedido_id: int,  pedidoRequest: PedidoAtualizaSchema) -> PedidoResponseSchema:
        pedidoEntity: Pedido = self.buscar_por_id(pedido_id=pedido_id)
        pedidoEntity.pedido_id = pedido_id
        pedidoEntity.status = pedidoRequest.status
        pedidoEntity.data_alteracao = datetime.datetime.now()

        if pedidoRequest.status == 4:
            pedidoEntity.data_finalizacao = datetime.datetime.now()

        pedidoAlterado: Pedido = self.pedido_repository.atualizarPedido(pedido=pedidoEntity)
        pedidoResponse: PedidoResponseSchema = PedidoResponseSchema(pedido_id=pedidoAlterado.pedido_id, cliente_id=pedidoAlterado.cliente_id, status=pedidoAlterado.status, data_criacao=pedidoAlterado.data_criacao, data_alteracao=pedidoAlterado.data_alteracao, data_finalizacao=pedidoAlterado.data_finalizacao)

        return pedidoResponse
    
    def deletar(self, pedido_id: int) -> None:
        self.pedido_repository.deletar(id=pedido_id)