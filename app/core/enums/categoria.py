from enum import Enum

class CategoriaEnum(str, Enum):
    LANCHE = 1
    ACOMPANHAMENTO = 2
    BEBIDA = 3
    SOBREMESA = 4
    
    def checkEnum(self, value: str) -> int:
        if(value.__eq__(self.LANCHE.name.upper)):
            return self.LANCHE
        if(value.__eq__(self.ACOMPANHAMENTO.name.upper)):
            return self.ACOMPANHAMENTO
        if(value.__eq__(self.BEBIDA.name.upper)):
            return self.BEBIDA
        if(value.__eq__(self.SOBREMESA.name.upper)):
            return self.SOBREMESA
            