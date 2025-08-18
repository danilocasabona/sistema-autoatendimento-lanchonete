from sqlalchemy.exc import IntegrityError

from app.entities.pagamento.entities import PagamentoEntities
from app.models.pagamento import Pagamento
from typing import List, Optional
from app.adapters.schemas.pagamento import PagamentoResponseSchema
from app.dao.pagamento_dao import PagamentoDAO

class PagamentoGateway(PagamentoEntities):
    def __init__(self, db_session):
        
        self.dao = PagamentoDAO(db_session)

    def criar_pagamento(self, pagamento: Pagamento) -> Pagamento:
        self.db_session.add(pagamento)
        
        try:
            self.db_session.commit()           
        except IntegrityError as e:            
            self.db_session.rollback()
            
            raise Exception(f"Erro de integridade ao salvar pagamento: {e}")
        self.db_session.refresh(pagamento)

        return pagamento
    
    def listar_todos_pagamentos(self)-> List[Pagamento]:
        
        return self.db_session.query(Pagamento).all()
    
    def buscar_pagamento_por_codigo(self, codigo_pagamento: str) -> Optional[Pagamento]: 
        
        return self.dao.buscar_pagamento_por_codigo(codigo_pagamento = codigo_pagamento)
    
    def atualizar_pagamento(self, pagamentoDTO) -> Pagamento: 
        
        return self.dao.atualizar_pagamento(pagamentoDTO)
    
    def deletar_pagamento(self, codigo_pagamento: str): 
        pagamento_deletar = self.db_session.query(Pagamento).filter(Pagamento.codigo_pagamento == codigo_pagamento).first()

        if not pagamento_deletar:
            raise ValueError("Pagamento não encontrado")
        
        self.db_session.delete(pagamento_deletar)
        self.db_session.commit()