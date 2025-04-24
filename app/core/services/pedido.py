from sqlalchemy.orm import Session
from app.core.schemas.pedido import PedidoCreateSchema
from app.core.models.pedido import Pedido
from app.core.models.cliente import Cliente
from app.core.enums.Status_pedido import StatusEnum
import datetime

# 🧩 Função para criar um novo produto
def criar_pedido(db: Session, pedido: PedidoCreateSchema):
    id_cliente =  db.query(Cliente).filter(Cliente.cpf == pedido.cliente.cpf).first()
    
    novo_pedido = Pedido(
        cliente_id = id_cliente,
        produto_1 = pedido.produto_1.id,
        produto_2 = pedido.produto_2.id,
        produto_3 = pedido.produto_3.id,
        produto_4 = pedido.produto_4.id,
        status = StatusEnum.Recebido.value
        data_criacao = datetime.datetime.now,
        data_finalizacao = ""
        
    )
    db.add(novo_pedido)
    db.commit()
    db.refresh(novo_pedido)
    return novo_pedido

