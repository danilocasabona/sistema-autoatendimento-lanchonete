from app.entities.cliente.entities import ClienteEntities
from app.entities.cliente.models import Cliente
from app.adapters.schemas.cliente import ClienteResponseSchema
from app.adapters.dto.cliente_dto import ClienteCreateSchema, ClienteUpdateSchema

class ClienteUseCase:
    def __init__(self, entities: ClienteEntities):
        self.cliente_entities = entities

    def criar_cliente(self, clienteRequest: ClienteCreateSchema) -> ClienteCreateSchema:       
        clienteCriado: Cliente = self.cliente_entities.criar_cliente(cliente=clienteRequest)
        
        return (ClienteResponseSchema(
                cliente_id=clienteCriado.cliente_id, 
                nome=clienteCriado.nome, 
                email=clienteCriado.email, 
                telefone=clienteCriado.telefone, 
                cpf=clienteCriado.cpf))
    
    def buscar_cliente_por_cpf(self, cpf_cliente: str) -> ClienteResponseSchema:
        clienteBusca: Cliente = self.cliente_entities.buscar_por_cpf(cpf_cliente=cpf_cliente)
        
        if not clienteBusca :
            raise ValueError("Cliente não encontrado")
            
        return (ClienteResponseSchema(
                cliente_id=clienteBusca.cliente_id, 
                nome=clienteBusca.nome, 
                email=clienteBusca.email, 
                telefone=clienteBusca.telefone, 
                cpf=clienteBusca.cpf))
    
    def buscar_cliente_por_id(self, cliente_id: int) -> ClienteResponseSchema:
        clienteBusca: Cliente = self.cliente_entities.buscar_por_id(cliente_id=cliente_id)
        
        if not clienteBusca :
            raise ValueError("Cliente não encontrado")
        
        return (ClienteResponseSchema(
                cliente_id=clienteBusca.cliente_id, 
                nome=clienteBusca.nome, 
                email=clienteBusca.email, 
                telefone=clienteBusca.telefone, 
                cpf=clienteBusca.cpf))
    
    def listar_clientes(self) -> list[ClienteResponseSchema]:
        clientesBusca: list[Cliente] = self.cliente_entities.listar_todos()
        clienteResponse: list[ClienteResponseSchema] = []
        
        for row in clientesBusca:
            clienteResponse.append(
                (ClienteResponseSchema(
                    cliente_id=row.cliente_id, 
                    nome=row.nome, 
                    email=row.email, 
                    telefone=row.telefone, 
                    cpf=row.cpf))
            )
        
        return clienteResponse

    def atualizar_cliente(self, cliente_id: int,  clienteRequest: ClienteUpdateSchema) -> ClienteResponseSchema:
        clienteEntity: Cliente = self.buscar_cliente_por_id(cliente_id=cliente_id)
        
        if not clienteEntity :
            raise ValueError("Cliente não encontrado")
        
        clienteAtualizado: Cliente = self.cliente_entities.atualizar_cliente(cliente=clienteEntity)

        return (ClienteResponseSchema(
                cliente_id=clienteAtualizado.cliente_id, 
                nome=clienteAtualizado.nome, 
                email=clienteAtualizado.email, 
                telefone=clienteAtualizado.telefone, 
                cpf=clienteAtualizado.cpf))

    def deletar_cliente(self, cliente_id: int) -> None:
        
        self.cliente_entities.deletar_cliente(cliente_id=cliente_id)