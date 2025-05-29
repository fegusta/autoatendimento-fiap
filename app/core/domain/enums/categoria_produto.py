from enum import Enum

class CategoriaProduto(str, Enum):
    LANCHE = "Lanche"
    ACOMPANHAMENTO = "Acompanhamento"
    BEBIDA = "Bebida"
    SOBREMESA = "Sobremesa"