from enum import Enum

class StatusEnum(str, Enum):
    Recebido = 1
    preparacao = 2
    pronto = 3
    finalizado = 4