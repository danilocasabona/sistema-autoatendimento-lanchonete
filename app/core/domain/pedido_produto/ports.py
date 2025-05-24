from abc import ABC, abstractmethod
from app.core.models.pedido_produto import PedidoProduto

class PedidoProdutoRepositoryPort(ABC):
    @abstractmethod
    def criarPedidoProduto(self, pedidoProduto: PedidoProduto): pass

    @abstractmethod
    def buscarPorIdPedido(self, pedido_id: int): pass

    @abstractmethod
    def deletar(self, pedido_produto_id: int): pass
    