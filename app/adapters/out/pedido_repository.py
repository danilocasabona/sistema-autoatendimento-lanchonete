from decimal import Decimal
from sqlalchemy.exc import IntegrityError

from app.core.domain.pedido.ports import PedidoRepositoryPort, Pedido
from app.core.models.pedido import Pedido as PedidoORM

class PedidoRepository(PedidoRepositoryPort):
    def __init__(self, db_session):
        self.db_session = db_session

    def criarPedido(self, pedido: Pedido) -> Pedido:
        try:
            self.db_session.add(pedido)
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
        pedido_orm = self.db_session.query(PedidoORM).filter_by(pedido_id=pedido.pedido_id).first()

        if not pedido_orm:
            raise ValueError("Pedido não encontrado")
        
        for field, value in pedido.model_dump().items():
            setattr(pedido_orm, field, value)

        self.db_session.commit()
        self.db_session.refresh(pedido_orm)

        return pedido_orm