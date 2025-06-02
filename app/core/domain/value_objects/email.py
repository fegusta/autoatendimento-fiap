import re

class Email:
    EMAIL_REGEX = re.compile(r"^[\w\.-]+@[\w\.-]+\.\w{2,}$")

    def __init__(self, valor: str):
        if not valor or valor.strip() == "":
            raise ValueError("Email não pode ser vazio.")

        valor = valor.strip()

        if not self.EMAIL_REGEX.match(valor):
            raise ValueError("Email inválido.")

        self._valor = valor

    @property
    def valor(self) -> str:
        return self._valor

    def __str__(self):
        return self._valor

    def __eq__(self, other):
        return isinstance(other, Email) and self._valor == other._valor
