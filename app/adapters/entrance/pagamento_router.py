from fastapi import APIRouter, HTTPException, Depends, Response
from sqlalchemy.orm import Session

from app.adapters.out.pagamento_repository import PagamentoRepository
from app.core.use_cases.pagamento.pagamento_use_case import PagamentoUseCase
from app.core.schemas.pagamento import *
from app.infrastructure.db.database import get_db

router = APIRouter(prefix="/pagamento", tags=["pagamento"])

def get_pagamento_repository(db: Session = Depends(get_db)) -> PagamentoRepository:
    return PagamentoRepository(db_session=db)

@router.get("/", response_model=list[PagamentoResponseSchema], summary="Listar todos os pagamentos realizado")
def listar_pagamentos(repository: PagamentoRepository = Depends(get_pagamento_repository)):
    try:
        
        return PagamentoUseCase(repository).listar_todos_pagamentos()
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/", response_model=PagamentoResponseSchema, status_code=201, summary="Criar pagamento do pedido")
def efetuar_pagamento_pedido(pedido_id: PagamentoCreateSchema, repository: PagamentoRepository = Depends(get_pagamento_repository)):
    try:
        
        return PagamentoUseCase(repository).criar_pagamento(pedido_pagamento=pedido_id)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/{codigo_pagamento}", response_model=PagamentoResponseSchema)
def buscar_pagamento(codigo_pagamento: str, repository: PagamentoRepository = Depends(get_pagamento_repository)):
    try:
        
        return PagamentoUseCase(repository).buscar_pagamento_por_codigo(codigo_pagamento=codigo_pagamento)
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.put("/{codigo_pagamento}", response_model=PagamentoResponseSchema)
def atualizar_pagamento(codigo_pagamento: str, pagamento_data: PagamentoAtualizaSchema, repository: PagamentoRepository = Depends(get_pagamento_repository)):
    try:
        
        return PagamentoUseCase(repository).atualizar_pagamento(codigo=codigo_pagamento, pagamento_request=pagamento_data)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.delete("/{codigo_pagamento}")
def deletar_pagamento(codigo_pagamento: str, repository: PagamentoRepository = Depends(get_pagamento_repository)):
    try:
        PagamentoUseCase(repository).deletar_pagamento(codigo_pagamento=codigo_pagamento)
        
        return Response(status_code=204)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))
