from sqlalchemy import Column, Integer, ForeignKey, Time
from sqlalchemy.orm import relationship
from app.adapters.db.database import Base

class Pedido(Base):
    
    __tablename__ = "pedido"

    pedido_id = Column(Integer, primary_key=True)  
    cliente = Column(Integer, ForeignKey("cliente.cliente_id"), nullable=True)

    produto_1 = Column(Integer, ForeignKey("produto.produto_id"), nullable=True)
    produto_2 = Column(Integer, ForeignKey("produto.produto_id"), nullable=True)
    produto_3 = Column(Integer, ForeignKey("produto.produto_id"), nullable=True)
    produto_4 = Column(Integer, ForeignKey("produto.produto_id"), nullable=True)

    status = Column(Integer, ForeignKey("pedido_status.pedido_status_id"), nullable=True)
    
    data_criacao = Column(Time, nullable=False)
    data_finalizacao = Column(Time, nullable=True)

    cliente_rel = relationship("Cliente", backref="pedidos")
    status_rel = relationship("PedidoStatus", backref="pedidos")
    produto_1_rel = relationship("Produto", foreign_keys=[produto_1])
    produto_2_rel = relationship("Produto", foreign_keys=[produto_2])
    produto_3_rel = relationship("Produto", foreign_keys=[produto_3])
    produto_4_rel = relationship("Produto", foreign_keys=[produto_4])
