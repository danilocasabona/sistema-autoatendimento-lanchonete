from app.core.domain.status_pedido.ports import StatusPedidoRepositoryPort
from app.core.schemas.status_pedido import StatusPedidoCreateSchema, StatusPedidoResponseSchema, StatusPedidoUpdateSchema
from app.core.domain.status_pedido.models import StatusPedido
from app.core.utils.debug import var_dump_die

class StatusPedidoUseCase:
    def __init__(self, status_repository: StatusPedidoRepositoryPort):
        self.status_repository = status_repository

    def criar(self, dataRequest: StatusPedidoCreateSchema) -> StatusPedidoResponseSchema:
        entity: StatusPedido = StatusPedido(descricao=dataRequest.descricao)
        created: StatusPedido = self.status_repository.criar(status=entity)

        response: StatusPedidoResponseSchema = StatusPedidoResponseSchema(id=created.id, descricao=created.descricao)

        return response

    def buscar_por_id(self, id: int) -> StatusPedidoResponseSchema:
        search: StatusPedido = self.status_repository.buscar_por_id(id=id)
        response: StatusPedidoResponseSchema = StatusPedidoResponseSchema(id=search.id, descricao=search.descricao)

        return response

    def listar_todos(self) -> list[StatusPedidoResponseSchema]:
        fetchedRows: list[StatusPedido] = self.status_repository.listar_todos()
        response: list[StatusPedidoResponseSchema] = []
        
        for row in fetchedRows:
            response.append(
                StatusPedidoResponseSchema(id=row.id, descricao=row.descricao)
            )
        
        return response

    def atualizar(self, id: int,  dataRequest: StatusPedidoUpdateSchema) -> StatusPedidoResponseSchema:
        entity: StatusPedido = self.buscar_por_id(id=id)
        entity.id = id
        entity.descricao = dataRequest.descricao
        
        updatedEntity: StatusPedido = self.status_repository.atualizar(status=entity)
        response: StatusPedidoResponseSchema = StatusPedidoResponseSchema(id=updatedEntity.id, descricao=updatedEntity.descricao)

        return response

    def deletar(self, id: int) -> None:
        
        self.status_repository.deletar(id=id)
