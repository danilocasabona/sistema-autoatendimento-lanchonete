from fastapi import APIRouter, HTTPException, Depends, Response, status
from sqlalchemy.orm import Session

from app.adapters.out.produto_repository import ProdutoRepository
from app.core.use_cases.produto.produto_use_case import ProdutoUseCase
from app.core.schemas.produto import ProdutoCreateSchema, ProdutoResponseSchema, ProdutoUpdateSchema
from app.infrastructure.db.database import get_db

router = APIRouter(prefix="/produtos", tags=["produtos"])

def get_produto_repository(db: Session = Depends(get_db)) -> ProdutoRepository:
    return ProdutoRepository(db_session=db)

@router.post("/", response_model=ProdutoResponseSchema, status_code=status.HTTP_201_CREATED, responses={
    400: {
        "description": "Erro de validação",
        "content": {
            "application/json": {
                "example": {
                    "message": "Erro de integridade ao criar o produto"
                }
            }
        }
    }
})
def criar_produto(produto: ProdutoCreateSchema, repository: ProdutoRepository = Depends(get_produto_repository)):
    try:
        produto_criado = ProdutoUseCase(repository).criar_produto(**produto.model_dump())

        return ProdutoResponseSchema(**produto_criado.model_dump())
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

@router.get("/", response_model=list[ProdutoResponseSchema], responses={
    400: {
        "description": "Erro de validação",
        "content": {
            "application/json": {
                "example": {
                    "message": "Erro de integridade ao buscar os produtos"
                }
            }
        }
    }
}, openapi_extra={
    "responses": {
        "422": None  
    }
})
def listar_produtos(repository: ProdutoRepository = Depends(get_produto_repository)):
    try:

        return ProdutoUseCase(repository).listar_todos()
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

@router.get("/categoria/{categoria}", response_model=list[ProdutoResponseSchema], responses={
    400: {
        "description": "Erro de validação",
        "content": {
            "application/json": {
                "example": {
                    "message": "Erro de integridade ao buscar o produto"
                }
            }
        }
    }
}, openapi_extra={
    "responses": {
        "422": None  
    }
})
def listar_produtos_por_categoria(categoria: int, repository: ProdutoRepository = Depends(get_produto_repository)):
    try:

        return ProdutoUseCase(repository).listar_por_categoria(categoria)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

@router.get("/{produto_id}", response_model=ProdutoResponseSchema, responses={
    400: {
        "description": "Erro de validação",
        "content": {
            "application/json": {
                "example": {
                    "message": "Erro de integridade ao buscar o produto"
                }
            }
        }
    },
    404: {
        "description": "Erro de validação",
        "content": {
            "application/json": {
                "example": {
                    "message": "Produto não encontrado"
                }
            }
        }
    }
}, openapi_extra={
    "responses": {
        "422": None  
    }
})
def buscar_produto(produto_id: int, repository: ProdutoRepository = Depends(get_produto_repository)):
    try:

        return ProdutoUseCase(repository).buscar_por_id(produto_id)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

@router.put("/{produto_id}", response_model=ProdutoResponseSchema, responses={
    404: {
        "description": "Erro de validação",
        "content": {
            "application/json": {
                "example": {
                    "message": "Produto não encontrado"
                }
            }
        }
    },
    400: {
        "description": "Erro de validação",
        "content": {
            "application/json": {
                "example": {
                    "message": "Erro de integridade ao atualizar o produto"
                }
            }
        }
    }
})
def atualizar_produto(produto_id: int, produto: ProdutoUpdateSchema, repository: ProdutoRepository = Depends(get_produto_repository)):
    try:

        return ProdutoUseCase(repository).atualizar_produto(produto_id, produto_data=produto)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

@router.delete("/{produto_id}", status_code=status.HTTP_204_NO_CONTENT, responses={
    404: {
        "description": "Erro de validação",
        "content": {
            "application/json": {
                "example": {
                    "message": "Produto não encontrado"
                }
            }
        }
    },
    400: {
        "description": "Erro de validação",
        "content": {
            "application/json": {
                "example": {
                    "message": "Erro de integridade ao remover o produto"
                }
            }
        }
    },
    204: {
        "description": "Produto deletado com sucesso",
        "content": {
            "application/json": {
                "example": {}
            }
        }
    }
})
def deletar_produto(produto_id: int, repository: ProdutoRepository = Depends(get_produto_repository)):
    try:
        ProdutoUseCase(repository).deletar_produto(produto_id)

        return Response(status_code=status.HTTP_204_NO_CONTENT)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))