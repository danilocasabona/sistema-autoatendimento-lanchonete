from sqlalchemy.orm import Session
from app.core.schemas.status import Status
from app.core.models.pedido import Pedido
from app.core.models.pedido_status import PedidoStatus

class StatusRepository:
    def __init__(self, db: Session):
        self.db = db

    def buscar_por_pedido_id(self, pedido_id: int) -> Status:
        result = (
            self.db.query(Pedido.pedido_id, PedidoStatus.status)
            .join(PedidoStatus, Pedido.status == PedidoStatus.pedido_status_id)
            .filter(Pedido.pedido_id == pedido_id)
            .first()
        )

        if not result:
            raise ValueError("Pedido não encontrado")

        return Status(
            pedido_id=result.pedido_id,
            status=result.status
        )
