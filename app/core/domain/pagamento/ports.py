from abc import ABC, abstractmethod

class PagamentoRepositoryPort(ABC):
    
    @abstractmethod
    def efetuar_pagamento(self, pagamento_pedido): pass
    
    @abstractmethod
    def listar_pagamento_realizado(): pass
    
    # @abstractmethod
    # def buscar_pedido_por_id(self, pedido_id: int): pass
    