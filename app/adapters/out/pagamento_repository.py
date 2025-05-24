from decimal import Decimal
from sqlalchemy.exc import IntegrityError
from app.core.models.pagamento import Pagamento
from app.core.domain.pagamento.ports import PagamentoRepositoryPort

class PagamentoRepository(PagamentoRepositoryPort):
    
    def __init__(self, db_session):
        self.db_session = db_session

    def efetuar_pagamento(self, pagamento_pedido: Pagamento) -> Pagamento:

        self.db_session.add(pagamento_pedido)
        
        try:
            self.db_session.commit()
        except IntegrityError as e:
            self.db_session.rollback()
            raise ValueError(f"Erro de integridade ao salvar pedido: {e}")
        self.db_session.refresh(Pagamento)

        return Pagamento
    
    def listar_pagamento_realizado(pedido_id):
        pass