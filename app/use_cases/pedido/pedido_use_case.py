from app.domain.pedido.ports import PedidoRepositoryPort 
from app.core.schemas.pedido.pedido import PedidoCreateSchema, PedidoResponseSchema, PedidoAtualizaSchema
from app.core.models.pedido import Pedido
from app.core.enums.status_pedido import PedidoStatusEnum
import datetime

class PedidoUseCase:
    def __init__(self, pedido_repository: PedidoRepositoryPort):
        self.pedido_repository = pedido_repository

    def criarPedido(self, pedidoRequest: PedidoCreateSchema) -> PedidoResponseSchema:
        pedidoEntity: Pedido = Pedido(cliente=pedidoRequest.cliente,produto1=pedidoRequest.produto_1,produto2=pedidoRequest.produto_2,produto3=pedidoRequest.produto_3, produto4=pedidoRequest.produto_4,status=1)
        pedidoEntity.status = PedidoStatusEnum.Recebido
        pedidoEntity.data_criacao = datetime.datetime.now()
        pedidoCriado: Pedido = self.pedido_repository.criarPedido(pedido=pedidoEntity)
        pedidoResponse: PedidoResponseSchema = PedidoResponseSchema(id=pedidoCriado.pedido_id, cliente=pedidoCriado.cliente, produto1=pedidoCriado.produto_1, produto2=pedidoCriado.produto_2, produto3=pedidoCriado.produto_3, produto4=pedidoCriado.produto_4, status=pedidoCriado.status, dataCriacao=pedidoCriado.data_criacao)
        return pedidoResponse
    
    def buscar_por_id(self, pedido_id: int) -> PedidoResponseSchema:
        pedidoBusca: Pedido = self.pedido_repository.buscar_por_id(id=pedido_id)
        pedidoResponse: PedidoResponseSchema = PedidoResponseSchema(id=pedidoBusca.pedido_id, cliente=pedidoBusca.cliente, produto1=pedidoBusca.produto_1, produto2=pedidoBusca.produto_2, produto3=pedidoBusca.produto_3, produto4=pedidoBusca.produto_4, status=pedidoBusca.status, dataCriacao=pedidoBusca.data_criacao)
        return pedidoResponse
    
    def listar_todos(self) -> list[PedidoResponseSchema]:
        pedidosBusca: list[Pedido] = self.pedido_repository.listar_todos()
        pedidosResponse: list[PedidoResponseSchema] = []
        for pedidoBusca in pedidosBusca:
            pedidosResponse.append(PedidoResponseSchema(id=pedidoBusca.pedido_id, cliente=pedidoBusca.cliente, produto1=pedidoBusca.produto_1, produto2=pedidoBusca.produto_2, produto3=pedidoBusca.produto_3, produto4=pedidoBusca.produto_4, status=pedidoBusca.status, dataCriacao=pedidoBusca.data_criacao))
        return pedidosResponse
    
    def atualiza(self, pedido_id: int,  pedidoRequest: PedidoAtualizaSchema) -> PedidoResponseSchema:
        pedidoEntity: Pedido = self.buscar_por_id(pedido_id=pedido_id)
        pedidoEntity.pedido_id = pedidoRequest.id
        pedidoEntity.data_finalizacao = datetime.datetime.now()
        pedidoEntity.status = pedidoRequest.status
        pedidoCriado: Pedido = self.pedido_repository.atualizarPedido(pedido=pedidoEntity)
        pedidoResponse: PedidoResponseSchema = PedidoResponseSchema(id=pedidoCriado.pedido_id, cliente=pedidoCriado.cliente, produto1=pedidoCriado.produto_1, produto2=pedidoCriado.produto_2, produto3=pedidoCriado.produto_3, produto4=pedidoCriado.produto_4, status=pedidoCriado.status, dataCriacao=pedidoCriado.data_criacao)
        return pedidoResponse
    
    def deletar(self, pedido_id: int) -> None:
        self.pedido_repository.deletar(id=pedido_id)