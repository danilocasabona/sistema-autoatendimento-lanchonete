from decimal import Decimal
from sqlalchemy.exc import IntegrityError

from app.core.domain.pedido.ports import PedidoRepositoryPort, Pedido

class PedidoRepository(PedidoRepositoryPort):
    def __init__(self, db_session):
        self.db_session = db_session

    def criarPedido(self, pedido: Pedido) -> Pedido:

        self.db_session.add(pedido)
        try:
            self.db_session.commit()
        except IntegrityError as e:
            self.db_session.rollback()
            raise ValueError(f"Erro de integridade ao salvar pedido: {e}")
        self.db_session.refresh(pedido)

        return pedido

    def buscar_por_id(self, id: int) -> Pedido:
        db_pedido = self.db_session.query(Pedido).filter(Pedido.pedido_id == id).first()
        if not db_pedido:
            raise ValueError("Pedido não encontrado")

        return db_pedido

    def listar_todos(self) -> list[Pedido]:
        db_pedidos = self.db_session.query(Pedido).all()
        pedidos = []
        for pedido in db_pedidos:
            pedidos.append(pedido)
        return pedidos

    def deletar(self, id: int) -> None:
        db_pedido = self.db_session.query(Pedido).filter(Pedido.pedido_id == id).first()
        if not db_pedido:
            raise ValueError("Pedido não encontrado")
        self.db_session.delete(db_pedido)
        self.db_session.commit()
        #self.db_session.flush()

    def atualizarPedido(self, pedido: Pedido) -> Pedido:

        try:
            self.db_session.commit()
        except IntegrityError as e:
            self.db_session.rollback()
            raise ValueError(f"Erro de integridade ao atualizar pedido: {e}")
        self.db_session.refresh(pedido)

        return pedido
