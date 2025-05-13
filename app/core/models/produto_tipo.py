from sqlalchemy import Column, Integer, String
from app.adapters.db.database import Base

class ProdutoTipo(Base):
    
    __tablename__ = "produto_tipo"

    produto_tipo_id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(255), nullable=False)