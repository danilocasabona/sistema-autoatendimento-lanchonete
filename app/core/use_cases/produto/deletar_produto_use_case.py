from app.core.domain.produto.ports import ProdutoRepositoryPort

class DeletarProdutoUseCase:
    def __init__(self, produto_repository: ProdutoRepositoryPort):
        self.produto_repository = produto_repository

    def executar(self, produto_id: int):
        return self.produto_repository.deletar(produto_id)