from app.core.enums.categoria import CategoriaEnum
from fastapi import APIRouter, HTTPException, Depends
from fastapi import Response
from app.adapters.out.produto_repository import ProdutoRepository
from app.use_cases.produto.criar_produto_use_case import CriarProdutoUseCase
from app.core.schemas.produto.produto import ProdutoCreateSchema, ProdutoResponseSchema
from app.use_cases.produto.listar_produtos_use_case import ListarProdutosUseCase
from app.use_cases.produto.buscar_produto_por_id_use_case import BuscarProdutoPorIdUseCase
from app.use_cases.produto.atualizar_produto_use_case import AtualizarProdutoUseCase
from app.use_cases.produto.deletar_produto_use_case import DeletarProdutoUseCase
from app.core.schemas.produto.produto import ProdutoUpdateSchema
from app.adapters.db.database import get_db
from sqlalchemy.orm import Session
from app.use_cases.produto.listar_produtos_por_categoria_use_case import ListarProdutosPorCategoriaUseCase

router = APIRouter(prefix="/produtos", tags=["produtos"])

def get_produto_repository(db: Session = Depends(get_db)) -> ProdutoRepository:
    return ProdutoRepository(db_session=db)

@router.post("/", response_model=ProdutoResponseSchema, status_code=201)
def criar_produto(produto: ProdutoCreateSchema, repository: ProdutoRepository = Depends(get_produto_repository)):
    try:
        use_case = CriarProdutoUseCase(repository)
        produto_criado = use_case.executar(**produto.model_dump())
        return ProdutoResponseSchema(**produto_criado.model_dump())
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/", response_model=list[ProdutoResponseSchema])
def listar_produtos(repository: ProdutoRepository = Depends(get_produto_repository)):
    try:
        use_case = ListarProdutosUseCase(repository)
        return use_case.executar()
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/categoria/{categoria}", response_model=list[ProdutoResponseSchema])
def listar_produtos_por_categoria(categoria: CategoriaEnum, repository: ProdutoRepository = Depends(get_produto_repository)):
    try:
        use_case = ListarProdutosPorCategoriaUseCase(repository)
        produtos = use_case.executar(categoria)
        return produtos  # Retorna lista vazia com 200 se não houver produtos
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/{produto_id}", response_model=ProdutoResponseSchema)
def buscar_produto(produto_id: int, repository: ProdutoRepository = Depends(get_produto_repository)):
    try:
        use_case = BuscarProdutoPorIdUseCase(repository)
        return use_case.executar(produto_id)
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.put("/{produto_id}", response_model=ProdutoResponseSchema)
def atualizar_produto(produto_id: int, produto: ProdutoUpdateSchema, repository: ProdutoRepository = Depends(get_produto_repository)):
    try:
        use_case = AtualizarProdutoUseCase(repository)
        return use_case.executar(produto_id, produto_data=produto)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.delete("/{produto_id}")
def deletar_produto(produto_id: int, repository: ProdutoRepository = Depends(get_produto_repository)):
    try:
        use_case = DeletarProdutoUseCase(repository)
        use_case.executar(produto_id)
        return Response(status_code=204)
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))