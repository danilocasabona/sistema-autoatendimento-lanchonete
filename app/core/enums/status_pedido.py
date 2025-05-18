from enum import Enum

class PedidoStatusEnum(str, Enum):
    Recebido = 1
    emPreparacao = 2
    pronto = 3
    Finalizado = 4
    
