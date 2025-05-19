from app.domain.pagamento.ports import PagamentoRepositoryPort
from app.core.models.pagamento import Pagamento
from sqlalchemy.exc import IntegrityError

class PagamentoRepository(PagamentoRepositoryPort):
    
    def __init__(self, db_session):
        
        self.db_session = db_session

    def criar_pagamento(self, pagamento: Pagamento) -> Pagamento:

        self.db_session.add(pagamento)
        
        try:
            
            self.db_session.commit()
            
        except IntegrityError as e:
            
            self.db_session.rollback()
            
            raise ValueError(f"Erro de integridade ao salvar pagamento: {e}")
        
        self.db_session.refresh(pagamento)

        return pagamento
    
    def listar_todos(self): pass
    def buscar_por_id(self, id: int): pass
    def deletar(self, id: int): pass
    def atualizar_pagamento(self, pagamento: Pagamento): pass