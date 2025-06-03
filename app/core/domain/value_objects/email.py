import re

class Email:
    def __init__(self, valor: str):
        if not re.match(r"[^@]+@[^@]+\.[^@]+", valor):
            raise ValueError("E-mail inválido.")
        self.valor = valor

    def __str__(self):
        return self.valor