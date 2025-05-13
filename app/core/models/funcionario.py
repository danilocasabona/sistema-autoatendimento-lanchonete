from sqlalchemy import Column, Integer, String
from app.adapters.db.database import Base

class Funcionario(Base):
    __tablename__ = "funcionario"

    funcionario_id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(255), nullable=False)
    senha = Column(String(110), nullable=False)
    cargo = Column(String(255), nullable=False)