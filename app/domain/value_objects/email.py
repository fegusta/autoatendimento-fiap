import re

class Email:
    def __init__(self, valor: str):
        valor = valor.strip().lower()
        if not re.match(r"^[^@]+@[^@]+\.[^@]+$", valor):
            raise ValueError("E-mail inválido.")
        self.valor = valor

    def __str__(self) -> str:
        return self.valor

    def __eq__(self, other) -> bool:
        return str(self) == str(other)

    def __repr__(self) -> str:
        return f"Email('{self.valor}')"
