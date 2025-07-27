import re

class CPF:
    def __init__(self, valor: str):
        valor_limpo = re.sub(r'\D', '', valor)

        if not valor_limpo.isdigit() or len(valor_limpo) != 11:
            raise ValueError("CPF deve conter exatamente 11 dígitos numéricos.")

        self.valor = f"{valor_limpo[:3]}.{valor_limpo[3:6]}.{valor_limpo[6:9]}-{valor_limpo[9:]}"

    def __str__(self) -> str:
        return self.valor

    def __eq__(self, other) -> bool:
        return str(self) == str(other)

    def __repr__(self) -> str:
        return f"CPF('{self.valor}')"
