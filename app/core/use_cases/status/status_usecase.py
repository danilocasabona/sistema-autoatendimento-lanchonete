from sqlalchemy.orm import Session
from app.adapters.out.status_repository import StatusRepository
from app.core.schemas.status import Status

class StatusUseCase:
    def __init__(self, db: Session):
        self.repository = StatusRepository(db)

    def obter_status(self, pedido_id: int) -> Status:
        return self.repository.buscar_por_pedido_id(pedido_id)
