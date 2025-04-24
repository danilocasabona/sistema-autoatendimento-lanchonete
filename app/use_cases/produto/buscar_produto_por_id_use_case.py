from app.domain.produto.models import Produto
from app.core.schemas.produto import ProdutoResponseSchema
from app.domain.produto.ports import ProdutoOutputPort

class BuscarProdutoPorIdUseCase:
    def __init__(self, output_port: ProdutoOutputPort):
        self.output_port = output_port

    def executar(self, produto_id: int) -> ProdutoResponseSchema:
        produto = self.output_port.buscar_por_id(produto_id)
        return ProdutoResponseSchema.model_validate(produto)
