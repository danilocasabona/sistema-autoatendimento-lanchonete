from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

from app.infrastructure.db.database import get_db
from app.core.schemas.pagamento import CreatePagamentoSchemas
from app.core.use_cases.pagamento.pagamento_use_case import pagamentoUseCase
from app.adapters.out.pagamento_repository import PagamentoRepository

router = APIRouter(prefix="/pagamento", tags=["pagamento"])

# Dependência para injetar o service
def get_pagamento_repository(db: Session = Depends(get_db)) -> PagamentoRepository:
    return PagamentoRepository(db_session=db)
    
@router.post('/pedido')
def pagamento_pedido(pedido_id: CreatePagamentoSchemas, repository: PagamentoRepository = Depends(get_pagamento_repository)):
    
    try:
        return pagamentoUseCase(repository).efetuar_pagamento(pedido_id.pedido_id)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
