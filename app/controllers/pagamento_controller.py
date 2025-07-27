from fastapi import status, HTTPException

from app.use_cases.pagamento_use_case import PagamentoUseCase

class PagamentoController:
    
    @staticmethod
    def criar_pagamento(pagamento_data, gateway):
        try:
            return PagamentoUseCase(gateway).criar_pagamento(pagamento_data)
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
    
    @staticmethod
    def buscar_pagamento_por_codigo(codigo_pagamento, gateway):
        try:
            return PagamentoUseCase(gateway).buscar_por_codigo(codigo_pagamento)
        except ValueError as e:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
    
    @staticmethod
    def listar_pagamentos(gateway):
        
        try:
            return PagamentoUseCase(gateway).listar_todos()
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

    @staticmethod
    def atualizar_pagamento(codigo_pagamento, pagamento_data, gateway):
        try:
            return PagamentoUseCase(gateway).atualizar_pagamento(codigo=codigo_pagamento, pagamento_request=pagamento_data)
        except ValueError as e:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
    
    @staticmethod
    def deletar_pagamento(codigo_pagamento: int, gateway):
        try:
            PagamentoUseCase(gateway).deletar_pagamento(codigo_pagamento=codigo_pagamento)
        except ValueError as e:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

    @staticmethod
    def atualizar_pagamento_webhook(pagamento_data, gateway):
        try:
            return PagamentoUseCase(gateway).atualizar_pagamento(codigo=pagamento_data.codigo_pagamento, pagamento_request=pagamento_data)
        except ValueError as e:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))