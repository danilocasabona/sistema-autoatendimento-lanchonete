from sqlalchemy import Column, Integer, String
from app.adapters.db.database import Base

class PagamentoStatus(Base):
    __tablename__ = "pagamento_status"

    pagamento_status_id = Column(Integer, primary_key=True, index=True)
    status = Column(String(50), nullable=False)
