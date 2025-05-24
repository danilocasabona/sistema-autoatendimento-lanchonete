from abc import ABC, abstractmethod

class PagamentoRepositoryPort(ABC):
    @abstractmethod
    def listar_pedido():
        pass