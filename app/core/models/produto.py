from sqlalchemy import Column, Integer, String, DECIMAL
from app.adapters.db.database import Base

class Produto(Base):
    __tablename__ = "produtos"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    descricao = Column(String, nullable=True)
    preco = Column(DECIMAL(10, 2), nullable=False)