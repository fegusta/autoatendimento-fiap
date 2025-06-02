class CPF:
    def __init__(self, valor: str):
        if not valor or valor.strip() == "":
            raise ValueError("CPF não pode ser vazio.")
        if len(valor.strip()) != 14:
            raise ValueError("CPF deve conter exatamente 14 caracteres.")
        self._valor = valor.strip()

    @property
    def valor(self) -> str:
        return self._valor

    def __str__(self):
        return self._valor

    def __eq__(self, other):
        return isinstance(other, CPF) and self._valor == other._valor
