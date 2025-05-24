from sqlalchemy import Column, Integer, String

from app.infrastructure.db.database import Base

class PedidoStatus(Base):
    __tablename__ = "pedido_status"

    pedido_status_id = Column(Integer, primary_key=True, index=True)
    status = Column(String(50), nullable=False)
