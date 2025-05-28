from sqlalchemy.exc import IntegrityError

from app.core.domain.pedido_produto.ports import PedidoProdutoRepositoryPort, PedidoProduto

class PedidoProdutoRepository(PedidoProdutoRepositoryPort):
    def __init__(self, db_session):
        self.db_session = db_session

    def criarPedidoProduto(self, pedidoProduto: PedidoProduto) -> PedidoProduto:
        try:
            self.db_session.add(pedidoProduto)
            self.db_session.commit()
        except IntegrityError as e:
            self.db_session.rollback()
            
            raise ValueError(f"Erro de integridade ao salvar pedido: {e}")
        self.db_session.refresh(pedidoProduto)

        return pedidoProduto
    
    def buscarPorIdPedido(self, pedido_id: int) -> PedidoProduto:
        db_pedido_produtos = self.db_session.query(PedidoProduto).filter(PedidoProduto.pedido_id == pedido_id).all()

        if not db_pedido_produtos:
            raise ValueError("Produto(s) do pedido não encontrado(s)")

        return db_pedido_produtos
    
    def deletar(self, id: int) -> None:
        db_pedido_produtos = self.db_session.query(PedidoProduto).filter(PedidoProduto.id == id).first()

        if db_pedido_produtos:
            self.db_session.delete(db_pedido_produtos)
            self.db_session.commit()       
            #self.db_session.flush()