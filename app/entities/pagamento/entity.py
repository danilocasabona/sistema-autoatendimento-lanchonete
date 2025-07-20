from abc import ABC, abstractmethod
from typing import List

from app.entities.pagamento.model import PagamentoModel

class PagamentoEntity(ABC):
    @abstractmethod
    def create(self, pedido_pagamento: PagamentoModel) -> PagamentoModel: pass
    
    @abstractmethod
    def getByCode(self, codigoPagamento: str): pass

    @abstractmethod
    def getAll(self) -> List[PagamentoModel]: pass   

    @abstractmethod
    def update(self, pagamento: PagamentoModel): pass

    @abstractmethod
    def delete(self, pagamento: PagamentoModel): pass
