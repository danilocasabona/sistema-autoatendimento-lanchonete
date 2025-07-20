from fastapi import APIRouter, HTTPException, Depends, Response, status
from sqlalchemy.orm import Session

from app.infrastructure.db.database import get_db
from app.gateways.pedido_repository import PedidoRepository
from app.gateways.pedido_produto_repository import PedidoProdutoRepository
from app.gateways.produto_repository import ProdutoGateway
from app.core.use_cases.pedido.pedido_use_case import PedidoUseCase
from app.core.use_cases.pedido_produtos.pedido_produtos_use_case import PedidoProdutosUseCase
from app.core.schemas.pedido import PedidoCreateSchema, PedidoResponseSchema, PedidoAtualizaSchema, PedidoProdutosResponseSchema

router = APIRouter(prefix="/pedidos", tags=["pedidos"])

def get_pedido_repository(db: Session = Depends(get_db)) -> PedidoRepository:
    return PedidoRepository(db_session=db)

def get_pedido_produto_repository(db: Session = Depends(get_db)) -> PedidoProdutoRepository:
    return PedidoProdutoRepository(db_session=db)

def get_produto_repository(db: Session = Depends(get_db)) -> ProdutoGateway:
    return ProdutoGateway(db_session=db)

@router.post("/", response_model=PedidoProdutosResponseSchema, status_code=status.HTTP_201_CREATED, responses={
    400: {
        "description": "Erro de validação",
        "content": {
            "application/json": {
                "example": {
                    "message": "Erro de integridade ao salvar o pedido | Erro de integridade ao salvar produtos no pedido"
                }
            }
        }
    }
})
def criar_pedido(
        pedido: PedidoCreateSchema, 
        pedidoRepository: PedidoRepository = Depends(get_pedido_repository), 
        pedidoProdutosRepository: PedidoProdutoRepository = Depends(get_pedido_produto_repository), 
        produtoRepository: ProdutoGateway = Depends(get_produto_repository)
    ):
    try:
        orderUseCase = PedidoUseCase(pedidoRepository).criarPedido(pedidoRequest=pedido)

        productOrderUseCase = (PedidoProdutosUseCase(pedidoProdutosRepository)
            .criarPedidoProdutos(orderUseCase.pedido_id, pedido.produtos, produtoRepository=produtoRepository))

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
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

@router.get("/", response_model=list[PedidoResponseSchema], responses={
    400: {
        "description": "Erro de validação",
        "content": {
            "application/json": {
                "example": {
                    "message": ""
                }
            }
        }
    },
}, 
openapi_extra={
    "responses": {
        "422": None  
    }
})
def listar_pedidos(repository: PedidoRepository = Depends(get_pedido_repository)):
    try:

        return PedidoUseCase(repository).listar_todos()
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

@router.get("/{pedido_id}", response_model=PedidoProdutosResponseSchema, responses={
    404: {
        "description": "Erro de validação",
        "content": {
            "application/json": {
                "example": {
                    "message": "Pedido não encontrado | Produto(s) do pedido não encontrado(s)"
                }
            }
        }
    },
    400: {
        "description": "Erro de validação",
        "content": {
            "application/json": {
                "example": {
                    "message": ""
                }
            }
        }
    }
}, openapi_extra={
    "responses": {
        "422": None  
    }
})
def buscar_pedido(
        pedido_id: int, 
        repository: PedidoRepository = Depends(get_pedido_repository), 
        pedidoProdutosRepository: PedidoProdutoRepository = Depends(get_pedido_produto_repository),
        produtoRepository: ProdutoGateway = Depends(get_produto_repository)
    ):
    try:
        orderUseCase = PedidoUseCase(repository).buscar_por_id(pedido_id)
        productOrderUseCase = PedidoProdutosUseCase(pedidoProdutosRepository).buscarPorIdPedido(orderUseCase.pedido_id, produtoRepository=produtoRepository)
        
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
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_NOT_FOUND, detail=str(e))

@router.put("/{pedido_id}", response_model=PedidoResponseSchema, responses={
    404: {
        "description": "Erro de validação",
        "content": {
            "application/json": {
                "example": {
                    "message": "Pedido não encontrado"
                }
            }
        }
    },
    400: {
        "description": "Erro de validação",
        "content": {
            "application/json": {
                "example": {
                    "message": "Pedido já finalizado"
                }
            }
        }
    }
})
def atualizar_pedido(pedido_id: int, pedido: PedidoAtualizaSchema, repository: PedidoRepository = Depends(get_pedido_repository)):
    try:

        return PedidoUseCase(repository).atualiza(pedido_id, pedidoRequest=pedido)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
    
@router.delete("/{pedido_id}", status_code=status.HTTP_204_NO_CONTENT, responses={
    404: {
        "description": "Erro de validação",
        "content": {
            "application/json": {
                "example": {
                    "message": "Pedido não encontrado"
                }
            }
        }
    },
    400: {
        "description": "Erro de validação",
        "content": {
            "application/json": {
                "example": {
                    "message": "Erro de integridade ao deletar o pedido"
                }
            }
        }
    },
    204: {
        "description": "Pedido deletado com sucesso",
        "content": {
            "application/json": {
                "example": {}
            }
        }
    }
})
def deletar_pedido(pedido_id: int, repository: PedidoRepository = Depends(get_pedido_repository), repositoryProductOrder: PedidoProdutoRepository = Depends(get_pedido_produto_repository)):
    try:
        PedidoProdutosUseCase(repositoryProductOrder).deletarPorPedido(pedido_id)
        PedidoUseCase(repository).deletar(pedido_id)

        return Response(status_code=status.HTTP_204_NO_CONTENT)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))