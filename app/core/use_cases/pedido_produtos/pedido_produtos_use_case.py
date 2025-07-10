from app.core.domain.pedido_produto.ports import PedidoProdutoRepositoryPort
from app.core.models.pedido_produto import PedidoProduto
from app.core.schemas.pedido_produto import ProdutoPedidoResponseSchema
from app.core.schemas.produto import ProdutoResponseSchema
from app.gateways.produto_repository import ProdutoGateway

class PedidoProdutosUseCase:
    def __init__(self, pedido_produtos_repository: PedidoProdutoRepositoryPort):
        self.pedido_produtos_repository = pedido_produtos_repository

    def criarPedidoProdutos(self, pedido_id: int, produtos: list, produtoRepository: ProdutoGateway) -> ProdutoPedidoResponseSchema:
        if isinstance(produtos, list):
            produtosCriados = [];
            
            for produto in produtos:
                produtosCriados.append(self._criarPedidoProduto(pedido_id=pedido_id, produto_id=produto, produtoRepository=produtoRepository));

        return produtosCriados
    
    def _criarPedidoProduto(self, pedido_id: int, produto_id: list, produtoRepository: ProdutoGateway) -> ProdutoResponseSchema: 
        pedidoProdutosEntity: PedidoProduto = PedidoProduto(pedido_id=pedido_id, produto_id=produto_id)  
        pedidoProdutosEntity.pedido_id = pedido_id
        pedidoProdutosEntity.produto_id = produto_id

        pedidoProdutoCriado: PedidoProdutoRepositoryPort = self.pedido_produtos_repository.criarPedidoProduto(pedidoProduto=pedidoProdutosEntity)
        produtoResponse = produtoRepository.buscar_por_id(pedidoProdutoCriado.produto_id)

        return produtoResponse
    
    def buscarPorIdPedido(self, pedido_id: int, produtoRepository: ProdutoGateway) -> ProdutoPedidoResponseSchema:
        pedidoProdutos: PedidoProduto = self.pedido_produtos_repository.buscarPorIdPedido(pedido_id=pedido_id)
        produtos = []
        
        for produto in pedidoProdutos:
            produtoResponse = produtoRepository.buscar_por_id(produto.produto_id)
            
            produtos.append(produtoResponse)

        return produtos
    
    def deletarPorPedido(self, pedido_id: int) -> None:
        pedidoProdutos: PedidoProduto = self.pedido_produtos_repository.buscarPorIdPedido(pedido_id=pedido_id)
        
        if pedidoProdutos:
            for pedidoProduto in pedidoProdutos:
                self.pedido_produtos_repository.deletar(id=pedidoProduto.id)