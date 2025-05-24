from enum import Enum

class StatusPagamentoEnum(str, Enum):
    Aprovado = "1"
    Reprovado = "2"
    Andamento = "3"
    Cancelado = "4"