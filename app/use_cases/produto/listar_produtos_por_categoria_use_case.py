from app.adapters.out.produto_repository import ProdutoRepositoryPort
from app.core.schemas.produto.produto import ProdutoResponseSchema
from typing import List


class ListarProdutosPorCategoriaUseCase:
    def __init__(self, produto_repository: ProdutoRepositoryPort):
        self.produto_repository = produto_repository

    def executar(self, categoria: str) -> List[ProdutoResponseSchema]:
        produtos = self.produto_repository.listar_por_categoria(categoria)
        return [ProdutoResponseSchema.model_validate(produto) for produto in produtos]