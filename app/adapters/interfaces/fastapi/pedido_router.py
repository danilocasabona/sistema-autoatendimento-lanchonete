from fastapi import APIRouter, HTTPException, Depends
from fastapi import Response
from app.adapters.out.pedido_repository import PedidoRepository
from app.use_cases.pedido.pedido_use_case import PedidoUseCase
from app.core.schemas.pedido.pedido import *

from app.adapters.db.database import get_db
from sqlalchemy.orm import Session

router = APIRouter(prefix="/pedidos", tags=["pedidos"])

def get_pedido_repository(db: Session = Depends(get_db)) -> PedidoRepository:
    return PedidoRepository(db_session=db)

@router.post("/", response_model=PedidoResponseSchema, status_code=201)
def criar_pedido(pedido: PedidoCreateSchema, repository: PedidoRepository = Depends(get_pedido_repository)):
    try:
        use_case = PedidoUseCase(repository)
        pedido_criado = use_case.criarPedido(pedidoRequest=pedido)
        return pedido_criado
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/", response_model=list[PedidoResponseSchema])
def listar_pedidos(repository: PedidoRepository = Depends(get_pedido_repository)):
    try:
        use_case = PedidoUseCase(repository)
        return use_case.listar_todos()
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/{pedido_id}", response_model=PedidoResponseSchema)
def buscar_pedido(pedido_id: int, repository: PedidoRepository = Depends(get_pedido_repository)):
    try:
        use_case = PedidoUseCase(repository)
        return use_case.buscar_por_id(pedido_id)
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.put("/{pedido_id}", response_model=PedidoResponseSchema)
def atualizar_pedido(pedido_id: int, pedido: PedidoAtualizaSchema, repository: PedidoRepository = Depends(get_pedido_repository)):
    try:
        use_case = PedidoUseCase(repository)
        return use_case.atualiza(pedido_id, pedidoRequest=pedido)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.delete("/{pedido_id}")
def deletar_pedido(pedido_id: int, repository: PedidoRepository = Depends(get_pedido_repository)):
    try:
        use_case = PedidoUseCase(repository)
        use_case.deletar(pedido_id)
        return Response(status_code=204)
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))