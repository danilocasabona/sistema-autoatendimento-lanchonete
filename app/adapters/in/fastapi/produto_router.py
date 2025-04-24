from fastapi import APIRouter, HTTPException
from app.adapters.out.produto_repository import ProdutoRepository
from app.use_cases.produto.criar_produto_use_case import CriarProdutoUseCase
from app.core.schemas.produto import ProdutoCreateSchema, ProdutoResponseSchema

router = APIRouter(prefix="/produtos", tags=["produtos"])

@router.post("/", response_model=ProdutoResponseSchema)
def criar_produto(produto: ProdutoCreateSchema):
    try:
        use_case = CriarProdutoUseCase(ProdutoRepository())
        produto_criado = use_case.executar(**produto.dict())
        return produto_criado
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))