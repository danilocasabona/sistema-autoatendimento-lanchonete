from app.core.domain.produto.ports import ProdutoRepositoryPort
from app.core.domain.produto.models import Produto

class CriarProdutoUseCase:
    def __init__(self, repo: ProdutoRepositoryPort):
        self.repo = repo

    def executar(self, nome, descricao, preco, categoria):
        produto = Produto(nome, descricao, preco, categoria)
        return self.repo.salvar(produto)