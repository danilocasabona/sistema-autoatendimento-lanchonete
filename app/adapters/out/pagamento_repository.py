from app.core.domain.pagamento.ports import PagamentoRepositoryPort
from app.core.models.pagamento import Pagamento
from sqlalchemy.exc import IntegrityError
from typing import List, Optional
from app.core.schemas.pagamento import PagamentoAtualizaSchema

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
    
    def listar_todos_pagamentos(self)-> List[Pagamento]:
        
        listagem_pagamento = self.db_session.query(Pagamento).all()

        return listagem_pagamento
    
    def buscar_pagamento_por_id(self, codigo_pagamento: str) -> Optional[Pagamento]: 
        consulta_pagamento = self.db_session.query(Pagamento).filter_by(codigo_pagamento=codigo_pagamento).first()

        if not consulta_pagamento:
            raise ValueError("Pagamento não encontrado")
        
        return consulta_pagamento
    
    def atualizar_pagamento(self, codigo: Pagamento) -> Pagamento: 
        pagamento_response = self.db_session.query(Pagamento).filter_by(codigo_pagamento=codigo.codigo_pagamento).first()

        if not pagamento_response:
            raise ValueError("Pagamento não encontrado")
        
        for field, value in codigo.model_dump().items():
            setattr(pagamento_response, field, value)

        self.db_session.commit()
        self.db_session.refresh(pagamento_response)

        return pagamento_response
    
    def deletar_pagamento(self, codigo_pagamento: str): 
        pagamento_deletar = self.db_session.query(Pagamento).filter_by(codigo_pagamento=codigo_pagamento).first()

        if not pagamento_deletar:
            raise ValueError("Pagamento não encontrado")
        
        self.db_session.delete(pagamento_deletar)
        self.db_session.commit()