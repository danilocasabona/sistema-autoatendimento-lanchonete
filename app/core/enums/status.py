from enum import Enum

class PedidoStatus(str, Enum):
    RECEBIDO = "RECEBIDO"
    EM_PREPARO = "EM_PREPARO"
    PRONTO = "PRONTO"
    A_CAMINHO = "A_CAMINHO"
    ENTREGUE = "ENTREGUE"
    CANCELADO = "CANCELADO"
