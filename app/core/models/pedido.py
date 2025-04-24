from sqlalchemy import (
    Column,
    ForeignKey,
    Integer,
    String,
    create_engine,
    select,
    DateTime
)
import datetime
import sqlalchemy as sa
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.adapters.db.database import Base
from core.models.cliente import Cliente
from core.models.produto import Produto

class Pedido(Base):
    __tablename__ = "pedidos"

    id: Mapped[int] = mapped_column(primary_key=True)
    cliente_id: int = sa.Column(sa.Integer, sa.ForeignKey("clientes.id"), nullable=True)
    produto_1: int = sa.Column(sa.Integer, sa.ForeignKey("produtos.id"), nullable=True)
    produto_2: int = sa.Column(sa.Integer, sa.ForeignKey("produtos.id"), nullable=True)
    produto_3: int = sa.Column(sa.Integer, sa.ForeignKey("produtos.id"), nullable=True)
    produto_4: int = sa.Column(sa.Integer, sa.ForeignKey("produtos.id"), nullable=True)
    status: int = sa.Column(sa.Integer)
    data_criacao = Column(DateTime, default=datetime.datetime.now)
    data_finalizacao = Column(DateTime)
    cliente: Mapped["Cliente"] = relationship("Cliente", back_populates="pedidos")
    