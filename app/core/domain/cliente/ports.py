from abc import ABC, abstractmethod
from typing import List, Optional

from app.core.domain.cliente.models import Cliente

class ClienteRepositoryPort(ABC):
    @abstractmethod
    def criar(self, cliente: Cliente) -> Cliente:
        pass

    @abstractmethod
    def buscar_por_id(self, cliente_id: int) -> Optional[Cliente]:
        pass

    @abstractmethod
    def buscar_por_cpf(self, cpf: str) -> Optional[Cliente]:
        pass

    @abstractmethod
    def listar_todos(self) -> List[Cliente]:
        pass

    @abstractmethod
    def atualizar(self, cliente: Cliente) -> Cliente:
        pass

    @abstractmethod
    def deletar(self, cliente_id: int) -> None:
        pass