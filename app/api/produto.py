from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from app.adapters.db.database import get_db
from app.core.schemas.produto import ProdutoCreateSchema, ProdutoResponseSchema
from app.core.enums.categoria import CategoriaEnum
from app.use_cases.produto.criar_produto_use_case import CriarProdutoUseCase
from app.use_cases.produto.buscar_produto_por_id_use_case import BuscarProdutoPorIdUseCase
from app.use_cases.produto.listar_produtos_use_case import ListarProdutosUseCase
from app.use_cases.produto.listar_produtos_por_categoria_use_case import ListarProdutosPorCategoriaUseCase
from app.adapters.out.produto_repository import ProdutoRepository
from app.use_cases.produto.deletar_produto_use_case import DeletarProdutoUseCase
from app.use_cases.produto.atualizar_produto_use_case import AtualizarProdutoUseCase

router = APIRouter(prefix="/produtos", tags=["Produtos"])

# 🔁 Funções responsáveis por injetar dependências nos casos de uso.
# Cada uma instancia um repositório e o fornece ao caso de uso correspondente.
def get_criar_produto_use_case(db: Session = Depends(get_db)) -> CriarProdutoUseCase:
    repo = ProdutoRepository(db)
    return CriarProdutoUseCase(repo)

def get_buscar_produto_use_case(db: Session = Depends(get_db)) -> BuscarProdutoPorIdUseCase:
    repo = ProdutoRepository(db)
    return BuscarProdutoPorIdUseCase(repo)

def get_listar_produtos_use_case(db: Session = Depends(get_db)) -> ListarProdutosUseCase:
    repo = ProdutoRepository(db)
    return ListarProdutosUseCase(repo)

def get_deletar_produto_use_case(db: Session = Depends(get_db)) -> DeletarProdutoUseCase:
    repo = ProdutoRepository(db)
    return DeletarProdutoUseCase(repo)

def get_listar_produtos_por_categoria_use_case(db: Session = Depends(get_db)) -> ListarProdutosPorCategoriaUseCase:
    repo = ProdutoRepository(db)
    return ListarProdutosPorCategoriaUseCase(repo)

# 🧩 Criar um novo produto
@router.post("/", response_model=ProdutoResponseSchema, status_code=status.HTTP_201_CREATED)
def criar_produto(
    produto: ProdutoCreateSchema,
    use_case: CriarProdutoUseCase = Depends(get_criar_produto_use_case)
):
    return use_case.executar(
        nome=produto.nome,
        descricao=produto.descricao,
        preco=produto.preco,
        categoria=produto.categoria
    )

# 🧩 Listar todos os produtos
@router.get("/", response_model=List[ProdutoResponseSchema])
def listar_produtos(use_case: ListarProdutosUseCase = Depends(get_listar_produtos_use_case)):
    # Chamando o método .executar() do caso de uso que aplica as regras de negócio e retorna os dados.
    return use_case.executar()

# 🧩 Buscar um produto pelo ID
@router.get("/{produto_id}", response_model=ProdutoResponseSchema)
def buscar_produto(
    produto_id: int,
    use_case: BuscarProdutoPorIdUseCase = Depends(get_buscar_produto_use_case)
):
    try:
        produto = use_case.executar(produto_id)
        return produto
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

# 🧩 Atualizar um produto existente
def get_atualizar_produto_use_case(db: Session = Depends(get_db)) -> AtualizarProdutoUseCase:
    repo = ProdutoRepository(db)
    return AtualizarProdutoUseCase(repo)

@router.put("/{produto_id}", response_model=ProdutoResponseSchema)
def atualizar_produto(
    produto_id: int,
    produto: ProdutoCreateSchema,
    use_case: AtualizarProdutoUseCase = Depends(get_atualizar_produto_use_case)
):
    try:
        return use_case.executar(produto_id, produto)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

# 🧩 Deletar um produto
@router.delete("/{produto_id}", status_code=status.HTTP_204_NO_CONTENT)
def deletar_produto(
    produto_id: int,
    use_case: DeletarProdutoUseCase = Depends(get_deletar_produto_use_case)
):
    try:
        sucesso = use_case.executar(produto_id)
        if sucesso:
            return
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

# 🧩 Listar produtos por categoria
@router.get("/categoria/{categoria}", response_model=List[ProdutoResponseSchema])
def listar_produtos_por_categoria(
    categoria: CategoriaEnum,
    use_case: ListarProdutosPorCategoriaUseCase = Depends(get_listar_produtos_por_categoria_use_case)
):
    return use_case.executar(categoria)
