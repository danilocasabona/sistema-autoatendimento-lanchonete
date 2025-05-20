from app.domain.produto.ports import ProdutoRepositoryPort
from app.domain.produto.models import Produto
from app.core.enums.categoria import CategoriaEnum

class CriarProdutoUseCase:
    def __init__(self, repo: ProdutoRepositoryPort):
        self.repo = repo

    def executar(self, nome, descricao, preco, categoria):
        produto = Produto(nome, descricao, preco, CategoriaEnum.ACOMPANHAMENTO.checkEnum(value=categoria))
        return self.repo.salvar(produto)