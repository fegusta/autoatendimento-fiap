class Nome:
    def __init__(self, valor: str):
        if not valor or valor.strip() == "":
            raise ValueError("Nome não pode ser vazio.")
        if len(valor.strip()) < 3:
            raise ValueError("Nome deve ter pelo menos 3 caracteres.")
        self._valor = valor.strip()

    @property
    def valor(self) -> str:
        return self._valor

    def __str__(self):
        return self._valor

    def __eq__(self, other):
        return isinstance(other, Nome) and self._valor == other._valor
