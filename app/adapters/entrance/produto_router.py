from fastapi import APIRouter, HTTPException, Depends
from fastapi import Response
from sqlalchemy.orm import Session

from app.adapters.out.produto_repository import ProdutoRepository
from app.core.use_cases.produto.produto_use_case import ProdutoUseCase
from app.core.schemas.produto import ProdutoCreateSchema, ProdutoResponseSchema, ProdutoUpdateSchema
from app.infrastructure.db.database import get_db

router = APIRouter(prefix="/produtos", tags=["produtos"])

def get_produto_repository(db: Session = Depends(get_db)) -> ProdutoRepository:
    return ProdutoRepository(db_session=db)

@router.post("/", response_model=ProdutoResponseSchema, status_code=201)
def criar_produto(produto: ProdutoCreateSchema, repository: ProdutoRepository = Depends(get_produto_repository)):
    try:
        produto_criado = ProdutoUseCase(repository).criar_produto(**produto.model_dump())

        return ProdutoResponseSchema(**produto_criado.model_dump())
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/", response_model=list[ProdutoResponseSchema])
def listar_produtos(repository: ProdutoRepository = Depends(get_produto_repository)):
    try:

        return ProdutoUseCase(repository).listar_todos()
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/categoria/{categoria}", response_model=list[ProdutoResponseSchema])
def listar_produtos_por_categoria(categoria: int, repository: ProdutoRepository = Depends(get_produto_repository)):
    try:

        return ProdutoUseCase(repository).listar_por_categoria(categoria)  # Retorna lista vazia com 200 se não houver produtos
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/{produto_id}", response_model=ProdutoResponseSchema)
def buscar_produto(produto_id: int, repository: ProdutoRepository = Depends(get_produto_repository)):
    try:

        return ProdutoUseCase(repository).buscar_por_id(produto_id)
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.put("/{produto_id}", response_model=ProdutoResponseSchema)
def atualizar_produto(produto_id: int, produto: ProdutoUpdateSchema, repository: ProdutoRepository = Depends(get_produto_repository)):
    try:

        return ProdutoUseCase(repository).atualizar_produto(produto_id, produto_data=produto)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.delete("/{produto_id}")
def deletar_produto(produto_id: int, repository: ProdutoRepository = Depends(get_produto_repository)):
    try:
        ProdutoUseCase(repository).deletar_produto(produto_id)

        return Response(status_code=204)
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))