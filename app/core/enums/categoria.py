from enum import Enum

class CategoriaEnum(str, Enum):
    LANCHE = "Lanche"
    ACOMPANHAMENTO = "Acompanhamento"
    BEBIDA = "Bebida"
    SOBREMESA = "Sobremesa"