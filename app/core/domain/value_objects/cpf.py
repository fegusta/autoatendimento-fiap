import re

class CPF:
    def __init__(self, valor: str):
        valor_limpo = re.sub(r'\D', '', valor)
        if len(valor_limpo) != 11:
            raise ValueError("CPF deve conter 11 dígitos.")
        self.valor = f"{valor_limpo[:3]}.{valor_limpo[3:6]}.{valor_limpo[6:9]}-{valor_limpo[9:]}"

    def __str__(self):
        return self.valor
