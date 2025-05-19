from fastapi import APIRouter, HTTPException, Depends
from fastapi import Response
from app.adapters.out.pagamento_repository import PagamentoRepository
from app.use_cases.pagamento.pagamento_use_case import PagamentoUseCase
from app.core.schemas.pagamento import *
from app.adapters.db.database import get_db
from sqlalchemy.orm import Session


router = APIRouter(prefix="/pagamento", tags=["pagamento"])

def get_pagamento_repository(db: Session = Depends(get_db)) -> PagamentoRepository:
    return PagamentoRepository(db_session=db)

@router.post("/pedido", response_model=PagamentoResponseSchema, status_code=201, summary="Efetuar pagamento do pedido do cliente")
def criar_pagamento(pedido_id: PagamentoCreateSchema, repository: PagamentoRepository = Depends(get_pagamento_repository)):
    
    try:
        use_case = PagamentoUseCase(repository)
        pagamento_efetuado = use_case.criar_pagamento(pagamento_request=pedido_id)
        return pagamento_efetuado
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

# @router.get("/", response_model=list[PedidoResponseSchema])
# def listar_pedidos(repository: PagamentoRepository = Depends(get_pedido_repository)):
#     try:
#         use_case = PedidoUseCase(repository)
#         return use_case.listar_todos()
#     except Exception as e:
#         raise HTTPException(status_code=400, detail=str(e))

# @router.get("/{pedido_id}", response_model=PedidoResponseSchema)
# def buscar_pedido(pedido_id: int, repository: PagamentoRepository = Depends(get_pedido_repository)):
#     try:
#         use_case = PedidoUseCase(repository)
#         return use_case.buscar_por_id(pedido_id)
#     except Exception as e:
#         raise HTTPException(status_code=404, detail=str(e))

# @router.put("/{pedido_id}", response_model=PedidoResponseSchema)
# def atualizar_pedido(pedido_id: int, pedido: PedidoAtualizaSchema, repository: PagamentoRepository = Depends(get_pedido_repository)):
#     try:
#         use_case = PedidoUseCase(repository)
#         return use_case.atualiza(pedido_id, pedidoRequest=pedido)
#     except ValueError as e:
#         raise HTTPException(status_code=404, detail=str(e))
#     except Exception as e:
#         raise HTTPException(status_code=400, detail=str(e))

# @router.delete("/{pedido_id}")
# def deletar_pedido(pedido_id: int, repository: PagamentoRepository = Depends(get_pedido_repository)):
#     try:
#         use_case = PedidoUseCase(repository)
#         use_case.deletar(pedido_id)
#         return Response(status_code=204)
#     except Exception as e:
#         raise HTTPException(status_code=404, detail=str(e))