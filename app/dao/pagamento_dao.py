from app.models.pagamento import Pagamento

class PagamentoDAO:
    
    def __init__(self, db_session):
        
        self.db_session = db_session

    def buscar_pagamento_por_codigo(self, codigo_pagamento: str) -> Pagamento | None: 
        
        return (self.db_session
                .query(Pagamento)
                .filter(Pagamento.codigo_pagamento == codigo_pagamento)
                .first())
    
    def atualizar_pagamento(self, pagamentoDTO) -> Pagamento | None:
        pagamento_entity = self.buscar_pagamento_por_codigo(codigo_pagamento = pagamentoDTO.codigo_pagamento)

        if pagamento_entity :
            pagamento_entity.status = pagamentoDTO.status

            self.db_session.commit()
            self.db_session.refresh(pagamento_entity)
        
        return pagamento_entity