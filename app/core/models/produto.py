from sqlalchemy import Column, Integer, String, DECIMAL, ForeignKey
from app.adapters.db.database import Base

class Produto(Base):
    __tablename__ = "produto"

    produto_id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(255), nullable=False)
    descricao = Column(String(255), nullable=False)
    preco = Column(DECIMAL(10, 2), nullable=False)
    categoria = Column(Integer, nullable=False)
    imagem = Column(String(255), nullable=True)
    cliente = Column(Integer, ForeignKey("cliente.cliente_id"), nullable=True)