from enum import Enum

class CategoriaEnum(str, Enum):
    Lanche = "Lanche"
    Acompanhamento = "Acompanhamento"
    Bebida = "Bebida"
    Sobremesa = "Sobremesa"