from typing import List

from app.core.domain.produto.ports import ProdutoRepositoryPort
from app.core.domain.produto.models import Produto
from app.core.schemas.produto import ProdutoResponseSchema, ProdutoCreateSchema

class ProdutoUseCase:
    def __init__(self, produto_repository: ProdutoRepositoryPort):
        self.produto_repository = produto_repository

    def criar_produto(self, nome, descricao, preco, categoria):
        produto = Produto(nome, descricao, preco, categoria)
        
        return self.produto_repository.criar_produto(produto)
    
    def listar_todos(self) -> List[ProdutoResponseSchema]:
        produtos = self.produto_repository.listar_todos()

        return [ProdutoResponseSchema.model_validate(produto) for produto in produtos]
    
    def listar_por_categoria(self, categoria: str) -> List[ProdutoResponseSchema]:
        produtos = self.produto_repository.listar_por_categoria(categoria)

        return [ProdutoResponseSchema.model_validate(produto) for produto in produtos]
    
    def buscar_por_id(self, produto_id: int) -> ProdutoResponseSchema:
        produto = self.produto_repository.buscar_por_id(produto_id)

        return ProdutoResponseSchema.model_validate(produto)
    
    def atualizar_produto(self, produto_id: int, produto_data: ProdutoCreateSchema) -> ProdutoResponseSchema:
        produto_atualizado = self.produto_repository.atualizar_produto(produto_id, produto_data)

        return ProdutoResponseSchema.model_validate(produto_atualizado)
    
    def deletar_produto(self, produto_id: int):

        return self.produto_repository.deletar_produto(produto_id)