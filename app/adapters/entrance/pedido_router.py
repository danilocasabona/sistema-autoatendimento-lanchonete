from fastapi import APIRouter, HTTPException, Depends
from fastapi import Response
from sqlalchemy.orm import Session

from app.adapters.out.pedido_repository import PedidoRepository
from app.adapters.out.pedido_produto_repository import PedidoProdutoRepository
from app.infrastructure.db.database import get_db
from app.core.use_cases.pedido.pedido_use_case import PedidoUseCase
from app.core.use_cases.pedido_produtos.pedido_produtos_use_case import PedidoProdutosUseCase
from app.core.schemas.pedido import *
from app.core.utils.debug import var_dump_die

router = APIRouter(prefix="/pedidos", tags=["pedidos"])

def get_pedido_repository(db: Session = Depends(get_db)) -> PedidoRepository:
    return PedidoRepository(db_session=db)

def get_pedido_produto_repository(db: Session = Depends(get_db)) -> PedidoProdutoRepository:
    return PedidoProdutoRepository(db_session=db)

@router.post("/", response_model=PedidoProdutosResponseSchema, status_code=201)
def criar_pedido(pedido: PedidoCreateSchema, repository: PedidoRepository = Depends(get_pedido_repository), repositoryProductOrder: PedidoProdutoRepository = Depends(get_pedido_produto_repository)):
    try:
        orderUseCase = PedidoUseCase(repository).criarPedido(pedidoRequest=pedido)
        productOrderUseCase = PedidoProdutosUseCase(repositoryProductOrder).criarPedidoProdutos(orderUseCase.pedido_id, pedido.produtos)

        pedidoResponse: PedidoProdutosResponseSchema = PedidoProdutosResponseSchema(
            pedido_id=orderUseCase.pedido_id,
            cliente_id=orderUseCase.cliente_id,
            status=orderUseCase.status,
            data_criacao=orderUseCase.data_criacao,
            data_alteracao=orderUseCase.data_alteracao,
            data_finalizacao=orderUseCase.data_finalizacao,
            produtos=productOrderUseCase
        )

        return pedidoResponse
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/", response_model=list[PedidoResponseSchema])
def listar_pedidos(repository: PedidoRepository = Depends(get_pedido_repository)):
    try:

        return PedidoUseCase(repository).listar_todos()
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/{pedido_id}", response_model=PedidoProdutosResponseSchema)
def buscar_pedido(pedido_id: int, repository: PedidoRepository = Depends(get_pedido_repository), repositoryProductOrder: PedidoProdutoRepository = Depends(get_pedido_produto_repository)):
    try:
        orderUseCase = PedidoUseCase(repository).buscar_por_id(pedido_id)
        productOrderUseCase = PedidoProdutosUseCase(repositoryProductOrder).buscarPorIdPedido(orderUseCase.pedido_id)

        pedidoResponse: PedidoProdutosResponseSchema = PedidoProdutosResponseSchema(
            pedido_id=orderUseCase.pedido_id,
            cliente_id=orderUseCase.cliente_id,
            status=orderUseCase.status,
            data_criacao=orderUseCase.data_criacao,
            data_alteracao=orderUseCase.data_alteracao,
            data_finalizacao=orderUseCase.data_finalizacao,
            produtos=productOrderUseCase 
        )
        
        return pedidoResponse
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.put("/{pedido_id}", response_model=PedidoResponseSchema)
def atualizar_pedido(pedido_id: int, pedido: PedidoAtualizaSchema, repository: PedidoRepository = Depends(get_pedido_repository)):
    try:

        return PedidoUseCase(repository).atualiza(pedido_id, pedidoRequest=pedido)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    
@router.delete("/{pedido_id}")
def deletar_pedido(pedido_id: int, repository: PedidoRepository = Depends(get_pedido_repository), repositoryProductOrder: PedidoProdutoRepository = Depends(get_pedido_produto_repository)):
    try:
        PedidoProdutosUseCase(repositoryProductOrder).deletarPorPedido(pedido_id)
        PedidoUseCase(repository).deletar(pedido_id)

        return Response(status_code=204)
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))