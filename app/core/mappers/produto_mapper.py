from app.core.schemas.produto.produto import ProdutoResponse, ProdutoCreate
from app.domain.produto.models import Produto
from app.core.enums.categoria import CategoriaEnum

def mapear_para_schema(produto: Produto) -> ProdutoResponse:
    return ProdutoResponse(
        id=produto.id,
        nome=produto.nome,
        preco=produto.preco,
        categoria=CategoriaEnum(produto.categoria)
    )

def mapear_para_dominio(produto_create: ProdutoCreate) -> Produto:
    return Produto(
        id=None,
        nome=produto_create.nome,
        preco=produto_create.preco,
        categoria=produto_create.categoria.value
    )
