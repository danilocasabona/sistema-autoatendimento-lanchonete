from typing import List
from app.domain.produto.models import Produto
from app.domain.produto.ports import ProdutoRepositoryPort
from app.core.schemas.produto.produto import ProdutoResponseSchema


class ListarProdutosUseCase:
    def __init__(self, repository: ProdutoRepositoryPort):
        self.repository = repository

    def executar(self) -> List[ProdutoResponseSchema]:
        produtos = self.repository.listar_todos()
        return [ProdutoResponseSchema.model_validate(produto) for produto in produtos]
