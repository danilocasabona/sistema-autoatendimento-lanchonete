from sqlalchemy import Column, Integer, String
from app.adapters.db.database import Base
from sqlalchemy.orm import (
    declarative_base,
    mapped_column,
    relationship,
    sessionmaker,
    Mapped
)
import typing

class Cliente(Base):
    __tablename__ = "clientes"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    telefone = Column(String, nullable=True)
    cpf = Column(String(11), unique=True, nullable=False)
    pedidos: Mapped[typing.List["Pedido"]] = relationship("Pedido", back_populates="cliente")