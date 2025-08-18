from fastapi import status, HTTPException
from app.use_cases.pagamento.pagamento_use_case import PagamentoUseCase

class PagamentoWebhookController:
    
    def __init__(self, db_session):
        self.db_session = db_session
    
    def atualizar_pagamento(self, codigo: int, pagamento_request):
        try:

            return PagamentoUseCase(self.db_session).atualizar_pagamento(codigo=codigo, pagamento_request=pagamento_request)
        except ValueError as e:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))