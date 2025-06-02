from decimal import Decimal, ROUND_HALF_UP

class Preco:
    def __init__(self, valor):
        # Convertendo para Decimal para evitar erros de float
        try:
            preco_decimal = Decimal(valor)
        except:
            raise ValueError("Preço deve ser um número válido.")

        if preco_decimal <= 0:
            raise ValueError("Preço deve ser maior que zero.")

        # Arredonda para 2 casas decimais
        preco_decimal = preco_decimal.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)

        # Opcional: limite máximo
        if preco_decimal > Decimal("1000000"):
            raise ValueError("Preço não pode ser maior que 1.000.000.")

        self._valor = preco_decimal

    @property
    def valor(self) -> Decimal:
        return self._valor

    def __str__(self):
        return f"{self._valor:.2f}"

    def __eq__(self, other):
        return isinstance(other, Preco) and self._valor == other._valor
