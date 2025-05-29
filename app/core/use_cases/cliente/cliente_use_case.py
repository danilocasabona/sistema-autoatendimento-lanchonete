from app.core.domain.cliente.ports import ClienteRepositoryPort
from app.core.domain.cliente.models import Cliente
from app.core.schemas.cliente import ClienteCreateSchema, ClienteResponseSchema, ClienteUpdateSchema

class ClienteUseCase:
    def __init__(self, cliente_repository: ClienteRepositoryPort):
        self.cliente_repository = cliente_repository

    def criarCliente(self, clienteRequest: ClienteCreateSchema) -> ClienteCreateSchema:
        clienteEntity: Cliente = Cliente(nome=clienteRequest.nome, email=clienteRequest.email, telefone=clienteRequest.telefone, cpf=clienteRequest.cpf)
        clienteCriado: Cliente = self.cliente_repository.criarCliente(cliente=clienteEntity)
        clienteResponse: ClienteResponseSchema = ClienteResponseSchema(cliente_id=clienteCriado.cliente_id, nome=clienteCriado.nome, email=clienteCriado.email, telefone=clienteCriado.telefone, cpf=clienteCriado.cpf)

        return clienteResponse
    
    def buscar_cliente_por_cpf(self, cpf: str) -> ClienteResponseSchema:
        clienteBusca: Cliente = self.cliente_repository.buscar_por_cpf(cpf=cpf)
        clienteResponse: ClienteResponseSchema = ClienteResponseSchema(cliente_id=clienteBusca.cliente_id, nome=clienteBusca.nome, email=clienteBusca.email, telefone=clienteBusca.telefone, cpf=clienteBusca.cpf)

        return clienteResponse
    
    def buscar_cliente_por_id(self, cliente_id: int) -> ClienteResponseSchema:
        clienteBusca: Cliente = self.cliente_repository.buscar_por_id(cliente_id=cliente_id)
        clienteResponse: ClienteResponseSchema = ClienteResponseSchema(cliente_id=clienteBusca.cliente_id, nome=clienteBusca.nome, email=clienteBusca.email, telefone=clienteBusca.telefone, cpf=clienteBusca.cpf)

        return clienteResponse
    
    def listar_clientes(self) -> list[ClienteResponseSchema]:
        clientesBusca: list[Cliente] = self.cliente_repository.listar_todos()
        clienteResponse: list[ClienteResponseSchema] = []
        
        for row in clientesBusca:
            clienteResponse.append(
                ClienteResponseSchema(cliente_id=row.cliente_id, nome=row.nome, email=row.email, telefone=row.telefone, cpf=row.cpf)
            )
        
        return clienteResponse

    def atualizar_cliente(self, cliente_id: int,  clienteRequest: ClienteUpdateSchema) -> ClienteResponseSchema:
        clienteEntity: Cliente = self.buscar_cliente_por_id(cliente_id=cliente_id)
        clienteEntity.cliente_id = cliente_id
        clienteEntity.nome = clienteRequest.nome
        clienteEntity.email = clienteRequest.email
        clienteEntity.telefone = clienteRequest.telefone
        clienteEntity.cpf = clienteRequest.cpf
        
        clienteAtualizado: Cliente = self.cliente_repository.atualizar_cliente(cliente=clienteEntity)
        clienteResponse: ClienteResponseSchema = ClienteResponseSchema(cliente_id=clienteAtualizado.cliente_id, nome=clienteAtualizado.nome, email=clienteAtualizado.email, telefone=clienteAtualizado.telefone, cpf=clienteAtualizado.cpf)

        return clienteResponse

    def deletar_cliente(self, cliente_id: int) -> None:
        
        self.cliente_repository.deletar_cliente(cliente_id=cliente_id)