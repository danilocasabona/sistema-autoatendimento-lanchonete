from sqlalchemy.exc import IntegrityError

from app.entities.pagamento.model import PagamentoModel
from app.models.pagamento import Pagamento as PagamentoORM
from app.entities.pagamento.entity import PagamentoEntity
from typing import List, Optional
from app.schemas.pagamento import PagamentoResponseSchema

class PagamentoGateway(PagamentoEntity):
    def __init__(self, db_session):
        
        self.db_session = db_session

    def create(self, pedido_pagamento: PagamentoModel) -> PagamentoModel:
        try:
            db_pagamento = PagamentoORM(
                pedido=pedido_pagamento.pedido,
                codigo_pagamento=pedido_pagamento.codigo_pagamento,
                status=pedido_pagamento.status
            )
            self.db_session.add(db_pagamento)
            self.db_session.commit()           
        except IntegrityError as e:            
            self.db_session.rollback()
            
            raise Exception(f"Erro de integridade ao salvar pagamento: {e}")
        
        self.db_session.refresh(db_pagamento)

        return pedido_pagamento
    
    def getByCode(self, codigoPagamento: str) -> Optional[PagamentoModel]: 
        entity = self.db_session.query(PagamentoORM).filter_by(codigo_pagamento = codigoPagamento).first()

        if not entity:
            raise ValueError("Pagamento não encontrado")
        
        return entity
    
    def getAll(self)-> List[PagamentoModel]:
        
        return self.db_session.query(PagamentoORM).all()
    
    def update(self, pagamento: PagamentoModel) -> PagamentoModel: 
        entity = self.db_session.query(PagamentoORM).filter_by(codigo_pagamento = pagamento.codigo_pagamento).first()
        if not entity:
            raise ValueError("Pagamento não encontrado")
        
        entity.status = pagamento.status
        
        self.db_session.commit()
        self.db_session.refresh(entity)
        
        response: PagamentoResponseSchema = (PagamentoResponseSchema(
                pedido_id = entity.pedido, 
                codigo_pagamento = entity.codigo_pagamento, 
                status = entity.status
            ))
        
        return response
    
    def delete(self, pagamento: PagamentoModel): 
        entity = self.db_session.query(PagamentoORM).filter_by(codigo_pagamento = pagamento.codigo_pagamento).first()

        if not entity:
            raise ValueError("Pagamento não encontrado")
        
        self.db_session.delete(entity)
        self.db_session.commit()