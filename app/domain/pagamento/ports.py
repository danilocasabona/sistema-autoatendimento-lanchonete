from abc import ABC, abstractmethod
from ...core.models import Pagamento

class PagamentoRepositoryPort(ABC):
    @abstractmethod
    def criar_pagamento(self, pagamento: Pagamento): pass
    @abstractmethod
    def listar_todos(self): pass
    @abstractmethod
    def buscar_por_id(self, id: int): pass
    @abstractmethod
    def deletar(self, id: int): pass
    @abstractmethod
    def atualizar_pagamento(self, pagamento: Pagamento): pass
