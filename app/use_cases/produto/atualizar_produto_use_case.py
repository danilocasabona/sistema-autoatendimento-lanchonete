from app.domain.produto.ports import ProdutoRepositoryPort
from app.core.schemas.produto import ProdutoCreateSchema, ProdutoResponseSchema

class AtualizarProdutoUseCase:
    def __init__(self, produto_repository: ProdutoRepositoryPort):
        self.produto_repository = produto_repository

    def executar(self, produto_id: int, produto_data: ProdutoCreateSchema) -> ProdutoResponseSchema:
        produto_atualizado = self.produto_repository.atualizar(produto_id, produto_data)
        return ProdutoResponseSchema.model_validate(produto_atualizado)