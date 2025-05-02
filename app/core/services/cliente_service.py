from typing import List, Optional
from app.domain.cliente.models import Cliente
from app.domain.cliente.ports import ClienteRepositoryPort
from fastapi import HTTPException

class ClienteService:
    def __init__(self, repository: ClienteRepositoryPort):
        self.repository = repository

    def criar_cliente(self, cliente: Cliente) -> Cliente:
        return self.repository.criar(cliente)

    def buscar_cliente_por_id(self, cliente_id: int) -> Optional[Cliente]:
        return self.repository.buscar_por_id(cliente_id)

    def listar_clientes(self) -> List[Cliente]:
        return self.repository.listar_todos()

    def atualizar_cliente(self, cliente: Cliente) -> Cliente:
        return self.repository.atualizar(cliente)

    def deletar_cliente(self, cliente_id: int) -> None:
        cliente = self.repository.buscar_por_id(cliente_id)
        if not cliente:
            raise HTTPException(status_code=404, detail="Cliente não encontrado")
        self.repository.deletar(cliente_id)

    def buscar_cliente_por_cpf(self, cpf: str) -> Optional[Cliente]:
        cliente = self.repository.buscar_por_cpf(cpf)
        if not cliente:
            raise ValueError("Cliente não encontrado")
        return cliente