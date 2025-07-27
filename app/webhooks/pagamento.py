from fastapi import APIRouter, HTTPException, Depends, Response, status, FastAPI
from sqlalchemy.orm import Session

from app.gateways.pagamento_gateway import PagamentoGateway
from app.infrastructure.db.database import get_db
from app.schemas.pagamento import PagamentoAtualizaWebhookSchema
from app.controllers.pagamento_controller import PagamentoController

router = APIRouter(prefix="/webhook", tags=["webhook"])

def get_pagamento_gateway(db: Session = Depends(get_db)) -> PagamentoGateway:
    
    return PagamentoGateway(db_session=db)

@router.post("/update-payment")
def atualizar_pagamento(pagamento_data: PagamentoAtualizaWebhookSchema, gateway: PagamentoGateway = Depends(get_pagamento_gateway)):
    try:
        
        return PagamentoController().atualizar_pagamento_webhook(pagamento_data, gateway)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))