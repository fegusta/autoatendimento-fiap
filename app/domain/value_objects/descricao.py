class Descricao:
    def __init__(self, valor: str):
        if not valor or valor.strip() == "":
            raise ValueError("Descrição não pode ser vazia.")
        
        valor = valor.strip()
        
        if len(valor) < 5:
            raise ValueError("Descrição deve ter pelo menos 5 caracteres.")
        
        if len(valor) > 500:
            raise ValueError("Descrição não pode ter mais que 500 caracteres.")
        
        self._valor = valor

    @property
    def valor(self) -> str:
        return self._valor

    def __str__(self):
        return self._valor

    def __eq__(self, other):
        return isinstance(other, Descricao) and self._valor == other._valor
