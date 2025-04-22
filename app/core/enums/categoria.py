from enum import Enum

class CategoriaEnum(str, Enum):
    lanche = "Lanche"
    acompanhamento = "Acompanhamento"
    bebida = "Bebida"
    sobremesa = "Sobremesa"